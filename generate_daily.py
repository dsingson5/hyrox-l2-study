#!/usr/bin/env python3
"""HYROX L2 Daily Study Generator — Interactive Edition.

Reads curriculum.json + questions.json, picks today's lesson, stacks
spaced-repetition reviews at 1/3/7/14/30/90-day intervals (Cepeda et al. 2008),
injects topic-specific interactive widgets, and writes a self-contained
interactive HTML to ./daily/hyrox_YYYY-MM-DD.html.

Learning-science layer (v2): forced-commitment reveal, FSRS scheduling,
confidence + 4-button grading with per-domain calibration, errorful-generation
pretest, and exam-weighted interleaving. See app.js for the runtime.
"""
from __future__ import annotations

import datetime as _dt
import html as _html
import json
import random
import sys
from pathlib import Path
from typing import Any

import widgets
import themes
import motifs

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUT = ROOT / "daily"
LAST_PAGE_QIDS = []  # core question stable-ids on the last rendered page
STYLES = ROOT / "styles.css"
APP_JS = ROOT / "app.js"

# (The CSCS figure-library and games-embed machinery was removed in v3.1 —
# this site has no figures/ dir and no games.html, so those paths were dead.)

# Shown in the page header (version + Manila build time). Bump on deploys.
SITE_VERSION = "v3.1"

SPACING_DAYS = [1, 3, 7, 14, 30, 90]
SPACING_LABELS = {
    1: "Yesterday (24 hr)",
    3: "3 days back",
    7: "1 week back",
    14: "2 weeks back",
    30: "1 month back",
    90: "3 months back",
}

DOMAIN_THEME = {
    "CM": {"name": "Coaching, Mindset & Individualisation", "accent": "#5ec8ff", "accent_2": "#8fdfff", "glow": "rgba(94, 200, 255, 0.18)",
           "icon": "M5 22a7 7 0 0 0 7-7c0-2 0-3 2-5 1.5-1.5 3-3 3-5a5 5 0 0 0-10 0c0 2 1.5 3.5 3 5 2 2 2 3 2 5a7 7 0 0 0-7 7"},
    "SM": {"name": "Sports Medicine, Recovery & Injury", "accent": "#67e8b0", "accent_2": "#9bf2cf", "glow": "rgba(103, 232, 176, 0.18)",
           "icon": "M12 2C8 6 6 10 6 14a6 6 0 0 0 12 0c0-4-2-8-6-12z"},
    "BM": {"name": "Biomechanics & Technique", "accent": "#ffb86b", "accent_2": "#ffd09a", "glow": "rgba(255, 184, 107, 0.18)",
           "icon": "M6 4l4 4-2 2 4 4 2-2 4 4-4 4-4-4 2-2-4-4-2 2-4-4z"},
    "PH": {"name": "Physiology & Nutrition", "accent": "#c08fff", "accent_2": "#d8b8ff", "glow": "rgba(192, 143, 255, 0.18)",
           "icon": "M12 21C7 17 3 13.5 3 9.5A4.5 4.5 0 0 1 12 6a4.5 4.5 0 0 1 9 3.5c0 4-4 7.5-9 11.5z"},
    "PG": {"name": "Performance Pillars & Programming", "accent": "#ff92c2", "accent_2": "#ffbcd9", "glow": "rgba(255, 146, 194, 0.18)",
           "icon": "M3 17l6-6 4 4 8-8M14 7h7v7"},
}

# Full domain names used on the question cards (match app.js DOMAIN_NAME).
DOMAIN_FULL = {"CM": "Coaching, Mindset & Individualisation", "SM": "Sports Medicine, Recovery & Injury",
               "BM": "Biomechanics & Technique", "PH": "Physiology & Nutrition",
               "PG": "Performance Pillars & Programming"}
# Interleave targets across the five L2 domains, proportional to their share
# of authored lessons (keep in sync with app.js EXAM_WEIGHTS).
EXAM_WEIGHTS = {"CM": 0.23, "SM": 0.15, "BM": 0.20, "PH": 0.16, "PG": 0.26}

# ── Interactive-figure aliases ───────────────────────────────────────────────
# widgets/steppers/biomech/motifs were inherited from the CSCS site and are
# keyed by ITS topic_ids, so every lookup silently missed after the port and no
# HYROX page rendered a single figure. This maps HYROX topic_ids onto the
# generic exercise-science interactives that genuinely fit them (energy-system
# timeline, torque calculator, force-velocity curve, arousal curve, …).
# Topics with no honest analogue are deliberately absent — a wrong diagram is
# worse than none. CSCS-specific pieces (phase1_review = "the four CSCS
# domains") are never aliased.
FIGURE_ALIAS = {
    # Physiology & nutrition
    "ph_energy": "energy_system_interaction",     # energy systems by duration
    "ph_vo2_thresholds": "respiratory",           # gas exchange & the Bohr shift
    "ph_lactate": "glycolysis",                   # splitting sugar for energy
    "ph_compromised": "cardiovascular",           # blood flow / delivery
    "ph_durability": "oxidative",                 # oxidative phosphorylation
    "nu_energy_availability": "macros",           # macro calculator
    "nu_carb_periodization": "nutrient_timing",   # macro calculator
    "nu_raceday": "nutrient_timing",
    # Biomechanics & technique
    "bm_forces": "biomech_levers",                # torque & lever calculator
    "bm_kinetic_chain": "ex_squat",               # movement-analysis stepper
    "bm_sled": "force_velocity_length_tension",   # high force / low velocity
    "bm_carry_lunge_wallball": "ex_squat",
    "rb_gait": "speed_agility",
    "rb_cadence": "speed_agility",
    "rb_drills": "warmup",
    "sk_progressions": "plyometrics",
    # Performance pillars & programming
    "of_ski": "ex_alt_modes",
    "of_row": "ex_alt_modes",
    "of_cross": "ex_alt_modes",
    "pd_models": "aerobic_adaptations",           # polarized vs pyramidal
    "pd_concurrent": "aerobic_programming",       # polarized donut
    # Sports medicine
    "pe_strength": "motor_units",                 # recruitment slider
    "pe_screening": "needs_analysis",
    "sm_return": "rehab",
    # Coaching & mental
    "mp_arousal": "sport_psych",                  # inverted-U arousal curve
    "pc_needs": "needs_analysis",
    # Exam-synthesis days reuse their domain's flagship figure
    "xs_physio": "energy_system_interaction",
    "xs_biomech": "biomech_levers",
    "xs_mental": "sport_psych",
}


def figure_key(topic_id):
    """CSCS figure key for a HYROX topic (identity if it already matches)."""
    return FIGURE_ALIAS.get(topic_id, topic_id)


# Pinned ts-fsrs (Anki's default scheduler since 23.10). ESM via jsDelivr — no
# build step, runs in a static GitHub Pages site. app.js falls back to an
# internal scheduler if this fails to load.
FSRS_MODULE = (
    '<script type="module">\n'
    "  try {\n"
    "    const m = await import('https://cdn.jsdelivr.net/npm/ts-fsrs@5.4.1/+esm');\n"
    "    window.__FSRS = { createEmptyCard: m.createEmptyCard, fsrs: m.fsrs,\n"
    "      generatorParameters: m.generatorParameters, Rating: m.Rating, State: m.State };\n"
    "  } catch (e) { console.warn('ts-fsrs load failed, using fallback scheduler', e); }\n"
    "  window.dispatchEvent(new Event('fsrs-ready'));\n"
    "</script>"
)


def load_data():
    curriculum = json.loads((DATA / "curriculum.json").read_text(encoding="utf-8"))
    questions = json.loads((DATA / "questions.json").read_text(encoding="utf-8"))
    return curriculum, questions


def day_number(start_date, today):
    return (today - _dt.date.fromisoformat(start_date)).days + 1


def today_local():
    """Return today's date in the curriculum's local timezone.
    Avoids GitHub-runner UTC giving you yesterday's lesson at 11pm Manila."""
    try:
        from zoneinfo import ZoneInfo
        return _dt.datetime.now(ZoneInfo("Asia/Manila")).date()
    except Exception:
        return _dt.date.today()


def relevant_lessons(lessons):
    """Training-relevant lessons (Tiers 1-3 + advanced), in day order.
    Lessons marked relevant=False (Tier-4 test-only) are excluded so the
    Deep-Review rotation and spaced recaps stay training-focused."""
    return [lessons[k] for k in sorted(lessons, key=lambda x: int(x))
            if lessons[k].get("relevant", True)]


def pick_review_lessons(today_day, lessons, seen_through=0):
    """Spaced recaps of prior lessons. Any lesson on a day <= seen_through is a
    lesson the learner has declared 'done and not to be re-reviewed' (meta
    seen_through_day), so it is never resurfaced as a spaced recap."""
    out = []
    for s in SPACING_DAYS:
        t = today_day - s
        if t < 1 or t <= seen_through:
            continue
        if str(t) in lessons and lessons[str(t)].get("relevant", True):
            out.append((s, lessons[str(t)]))
    return out


def get_today_lesson(today_day, lessons):
    # Scheduled days serve their authored lesson as-is.
    if str(today_day) in lessons:
        return lessons[str(today_day)], False
    # Beyond the authored calendar: Deep Review rotates EVENLY through the
    # training-relevant pool only (no random repeats, no Tier-4 test-only).
    pool = relevant_lessons(lessons) or list(lessons.values())
    return pool[(today_day - 1) % len(pool)], True


def sample_questions(topic_id, questions, n, seed):
    """Return [(orig_index, question_dict), ...] — orig_index is the position
    in the source pool so we can build stable IDs for persistence."""
    pool = questions.get(topic_id, [])
    if not pool:
        return []
    rng = random.Random(seed)
    indices = list(range(len(pool)))
    rng.shuffle(indices)
    chosen = indices[:min(n, len(pool))]
    return [(i, pool[i]) for i in chosen]


def esc(s):
    return _html.escape(s, quote=True)


def render_lesson_card(lesson, badge, badge_class, show_widget=True, is_today=False):
    domain = lesson.get("domain", "CM")
    theme = DOMAIN_THEME.get(domain, DOMAIN_THEME["CM"])
    motif = motifs.motif_for(figure_key(lesson["topic_id"]))
    hero_html = motifs.render_motif_hero(motif) if (is_today and motif) else ""
    motif_class = " has-motif" if (is_today and motif) else ""
    facts = "".join(f"<li>{esc(f)}</li>" for f in lesson.get("key_facts", []))
    tl = lesson.get("training_link", "").strip()
    tl_html = (f'<div class="training-link"><span class="tl-label">Connection to your training</span>'
               f'<p>{esc(tl)}</p></div>') if tl else ""
    v = lesson.get("video", {}); a = lesson.get("audio", {})
    media = ""
    if v.get("url"):
        media += (f'<a class="media-link video" href="{esc(v["url"])}" target="_blank" rel="noopener">'
                  f'<span class="m-icon">▶</span><div><div class="m-title">{esc(v["title"])}</div>'
                  f'<div class="m-cred">{esc(v.get("credibility", ""))}</div></div></a>')
    if a.get("url"):
        media += (f'<a class="media-link audio" href="{esc(a["url"])}" target="_blank" rel="noopener">'
                  f'<span class="m-icon">♪</span><div><div class="m-title">{esc(a["title"])}</div>'
                  f'<div class="m-cred">{esc(a.get("credibility", ""))}</div></div></a>')
    for rsrc in (lesson.get("resources") or []):
        if rsrc.get("url"):
            media += (f'<a class="media-link resource" href="{esc(rsrc["url"])}" target="_blank" rel="noopener">'
                      f'<span class="m-icon">🔗</span><div><div class="m-title">{esc(rsrc["title"])}</div>'
                      f'<div class="m-cred">{esc(rsrc.get("credibility", ""))}</div></div></a>')
    widget_html = widgets.render(figure_key(lesson["topic_id"])) if show_widget else ""
    chip = (f'<span class="domain-chip" style="background: {theme["glow"]}; color: {theme["accent"]}; border-color: {theme["accent"]}66;">'
            f'<svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="{theme["icon"]}"/></svg>{esc(theme["name"])}</span>')
    # Glossary — animated definition cards for technical terms
    glossary_html = ""
    if lesson.get("glossary"):
        items = ""
        for i, g in enumerate(lesson["glossary"]):
            items += (f'<div class="gloss-card" style="animation-delay: {i*0.08:.2f}s">'
                      f'<div class="gloss-svg">{g.get("svg","")}</div>'
                      f'<div class="gloss-text"><div class="gloss-term">{esc(g["term"])}</div>'
                      f'<div class="gloss-def">{esc(g["def"])}</div></div></div>')
        glossary_html = (f'<div class="glossary"><div class="gloss-title">Visual glossary</div>'
                         f'<div class="gloss-grid">{items}</div></div>')

    return (f'<section class="lesson-card reveal{motif_class}" data-domain="{domain}" '
            f'style="--accent: {theme["accent"]}; --accent-2: {theme["accent_2"]}; --glow: {theme["glow"]};">'
            f'{hero_html}'
            f'<div class="lesson-head"><span class="badge {badge_class}">{esc(badge)}</span>{chip}'
            f'<span class="domain">{esc(lesson.get("chapter", ""))} · {esc(lesson.get("page_refs", ""))}</span></div>'
            f'<h2>{esc(lesson["title"])}</h2>'
            f'<p class="concept">{esc(lesson.get("key_concept", ""))}</p>'
            f'{widget_html}'
            f'<div class="facts"><div class="facts-title">Key facts to memorize</div><ul>{facts}</ul></div>'
            f'{glossary_html}'
            f'{tl_html}<div class="media">{media}</div></section>')


def render_q_card(topic_id, orig_idx, q, qid, domain, label="Q", pretest=False):
    """One interactive retrieval card. Reveal is gated client-side until the
    learner types an attempt or clicks 'I don't know' (forced commitment);
    after reveal, the 4-button Again/Hard/Good/Easy grade feeds FSRS. Applied
    (mechanism) cards also get a self-explanation prompt. Markup mirrors
    app.js questionCardHTML so generator and runtime cards behave identically."""
    qtype = q.get("type", "recall")
    selfexplain = qtype == "applied"
    stable = f"{topic_id}__{orig_idx}"
    se = ""
    if selfexplain:
        se = ('<div class="q-selfexplain"><label>In your own words — why is this true?</label>'
              '<textarea class="se-answer" placeholder="One sentence is enough. The attempt is what builds the memory." '
              'oninput="onSelfExplainInput(event)"></textarea></div>')
    cls = "q pretest" if pretest else "q"
    dom_name = DOMAIN_FULL.get(domain, domain)
    return (
        f'<div class="{cls}" data-qid="{qid}" data-stable="{esc(stable)}" data-domain="{domain}" data-qtype="{qtype}">'
        f'<div class="q-head"><span class="q-num">{label}</span><span class="q-type {qtype}">{qtype}</span>'
        f'<span class="q-domain">{esc(dom_name)}</span>'
        f'<span class="q-status" data-status-for="{qid}"></span><span class="q-last" data-last-for="{qid}" data-stable="{esc(stable)}"></span><span class="q-next" data-stable="{esc(stable)}"></span></div>'
        f'<div class="q-text">{esc(q["q"])}</div>'
        f'<textarea class="q-answer" placeholder="Recall and type your answer first…" oninput="onAnswerInput(event)"></textarea>'
        f'<button type="button" class="mic-btn" aria-pressed="false" title="Answer by voice" onclick="toggleDictation(this)"><svg class="mic-ico" viewBox="0 0 24 24" width="13" height="13" aria-hidden="true"><path fill="currentColor" d="M12 14a3 3 0 0 0 3-3V6a3 3 0 1 0-6 0v5a3 3 0 0 0 3 3z"></path><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M5 11a7 7 0 0 0 14 0M12 18v3"></path></svg><span class="mic-lbl">Speak</span></button>'
        f'<div class="q-confidence"><span class="conf-label">How sure are you?</span>'
        f'<button type="button" class="conf-btn" data-conf="low" onclick="pickConfidence(\'{qid}\',\'low\')">Low</button>'
        f'<button type="button" class="conf-btn" data-conf="med" onclick="pickConfidence(\'{qid}\',\'med\')">Medium</button>'
        f'<button type="button" class="conf-btn" data-conf="high" onclick="pickConfidence(\'{qid}\',\'high\')">High</button></div>'
        f'<div class="q-actions">'
        f'<button type="button" class="btn-reveal" id="revealbtn_{qid}" disabled onclick="revealQ(\'{qid}\')">Reveal answer</button>'
        f'<button type="button" class="btn-idk" onclick="dontKnowQ(\'{qid}\')">I don\'t know</button></div>'
        f'<div class="q-reveal" id="reveal_{qid}"><div class="reveal-label">Answer</div>'
        f'<div class="reveal-body">{esc(q["a"])}</div>{se}'
        f'<div class="q-rate"><div class="rate-label">How did that go? <span class="rate-hint">(this sets when you see it next)</span></div>'
        f'<button type="button" class="rate-btn rate-again" data-grade="1" onclick="rateQ(\'{qid}\',1)">Again<small>&lt;10m</small></button>'
        f'<button type="button" class="rate-btn rate-hard" data-grade="2" onclick="rateQ(\'{qid}\',2)">Hard<small></small></button>'
        f'<button type="button" class="rate-btn rate-good" data-grade="3" onclick="rateQ(\'{qid}\',3)">Good<small></small></button>'
        f'<button type="button" class="rate-btn rate-easy" data-grade="4" onclick="rateQ(\'{qid}\',4)">Easy<small></small></button>'
        f'</div><div class="rate-result"></div></div></div>'
    )


def _interleave(pool):
    """pool: list of dicts with keys topic_id, orig_idx, q, domain. Returns the
    list reordered by exam-weight round-robin so domains appear roughly in
    proportion to NSCA weights and adjacent cards avoid sharing a topic
    (the discrimination practice interleaving buys us)."""
    by_dom = {}
    for it in pool:
        by_dom.setdefault(it["domain"], []).append(it)
    served = {d: 0 for d in by_dom}
    out = []
    last_topic = None
    total = len(pool)
    while len(out) < total:
        best, best_score = None, -1e9
        for d, items in by_dom.items():
            if not items:
                continue
            w = EXAM_WEIGHTS.get(d, 0.1)
            deficit = w - served[d] / max(1, len(out))
            penalty = 0.15 if items[0]["topic_id"] == last_topic else 0.0
            score = deficit - penalty
            if score > best_score:
                best_score, best = score, d
        if best is None:
            break
        it = by_dom[best].pop(0)
        out.append(it)
        served[best] += 1
        last_topic = it["topic_id"]
    return out


def render_practice_section(pool, topic_domain, block_id="px"):
    """Single interleaved practice section (replaces chapter-blocked groups)."""
    if not pool:
        return ""
    ordered = _interleave(pool)
    cards = ""
    for i, it in enumerate(ordered):
        cards += render_q_card(it["topic_id"], it["orig_idx"], it["q"], f"{block_id}_{i}",
                               it["domain"], label=f"Q{i+1}")
    return ('<section class="question-block reveal"><h3>Interleaved practice</h3>'
            '<p class="qs-sub">Mixed across domains by exam weight — this feels harder than drilling one topic, '
            'and that difficulty is the point: it roughly doubles what transfers to test day.</p>'
            f'<div class="qs">{cards}</div></section>')


def render_pretest(topic_id, qs, domain):
    """Errorful-generation pretest: 2 questions BEFORE the lesson. Guessing
    (and being wrong) primes encoding of the upcoming answer."""
    if not qs:
        return ""
    cards = ""
    for i, (orig_idx, q) in enumerate(qs):
        cards += render_q_card(topic_id, orig_idx, q, f"pre_{i}", domain,
                               label="Predict", pretest=True)
    return ('<section class="pretest-section reveal"><div class="pretest-banner">'
            '<span class="pt-icon">&#129504;</span><div><b>Predict first.</b> '
            'Take a guess before you read today\'s lesson. Getting it wrong is fine — '
            'a failed guess primes your brain to remember the right answer when it arrives.</div></div>'
            f'<div class="qs">{cards}</div></section>')



def _archive_dates(meta_start_iso, page_iso=None):
    """All ISO dates from start_date through max(Manila today, latest existing
    daily file, the page being generated). page_iso MUST be included: the dated
    file is written only after render, and the nightly runner's UTC date is a
    day behind Manila — either alone would leave the page out of its own
    archive and bake null prev/next nav."""
    import datetime as _d
    start = _d.date.fromisoformat(meta_start_iso)
    existing = []
    try:
        for p in OUT.glob("hyrox_2*.html"):
            s = p.stem.replace("hyrox_", "")
            if s >= meta_start_iso:
                existing.append(s)
    except Exception:
        pass
    last_iso = max(existing) if existing else meta_start_iso
    last = _d.date.fromisoformat(last_iso)
    end = max(last, today_local())
    if page_iso:
        end = max(end, _d.date.fromisoformat(page_iso))
    out = []
    d = start
    while d <= end:
        out.append(d.isoformat())
        d = d + _d.timedelta(days=1)
    return out

def render_html(today, today_day, today_lesson, deep_review, reviews, questions, meta, topic_domain):
    import json as _json2
    page_date = today.isoformat()
    _all = _archive_dates(meta["start_date"], page_date)
    try:
        _i = _all.index(page_date)
    except ValueError:
        _i = -1
    _prev = _all[_i-1] if _i > 0 else None
    _next = _all[_i+1] if _i >= 0 and _i+1 < len(_all) else None
    prev_json = _json2.dumps(_prev)
    next_json = _json2.dumps(_next)

    css = STYLES.read_text(encoding="utf-8")
    js = APP_JS.read_text(encoding="utf-8")
    theme = themes.for_day(today_day)
    theme_css = themes.render_overrides(theme)
    motif = motifs.motif_for(figure_key(today_lesson["topic_id"]))
    motif_css = motifs.render_motif_css(motif, theme) if motif else ""
    badge = "Deep Review" if deep_review else f"Day {today_day} · New lesson"
    badge_class = "badge-review" if deep_review else "badge-new"

    t_topic = today_lesson["topic_id"]
    t_domain = topic_domain.get(t_topic, today_lesson.get("domain", "CM"))

    # ── Pretest (errorful generation) — 2 questions before the lesson ──
    pre_qs = []
    if not deep_review:
        sampled = sample_questions(t_topic, questions, 6, today_day * 7)
        # prefer the harder "applied" items as predictions
        sampled.sort(key=lambda iq: 0 if iq[1].get("type") == "applied" else 1)
        pre_qs = sampled[:2]
    pre_idx = {oi for oi, _ in pre_qs}
    pretest_html = render_pretest(t_topic, pre_qs, t_domain)

    today_card = render_lesson_card(today_lesson, badge, badge_class, True, is_today=True)

    # ── Spaced review lesson cards (full recap incl. the topic animation; questions are pooled) ──
    review_html = ""
    if reviews:
        review_html = ('<div class="review-section">'
                       '<h2 class="rs-title">Spaced review</h2>'
                       '<p class="rs-sub">Concepts you met before, resurfacing at expanding intervals '
                       '(Cepeda et al. 2008). Read the recap, then test yourself in the practice set below.</p>')
        for interval, lesson in reviews:
            label = SPACING_LABELS.get(interval, f"{interval}d review")
            review_html += render_lesson_card(lesson, label, "badge-spaced", True)
        review_html += "</div>"

    # ── Build the interleaved practice pool (exam-weighted, cross-domain) ──
    pool = []
    for oi, q in sample_questions(t_topic, questions, 5, today_day * 7):
        if oi in pre_idx:
            continue
        pool.append({"topic_id": t_topic, "orig_idx": oi, "q": q, "domain": t_domain})
    for interval, lesson in reviews:
        rtopic = lesson["topic_id"]
        rdom = topic_domain.get(rtopic, lesson.get("domain", "CM"))
        for oi, q in sample_questions(rtopic, questions, 2, today_day * 11 + interval):
            pool.append({"topic_id": rtopic, "orig_idx": oi, "q": q, "domain": rdom})
    # cross-domain draws so the queue is never single-domain
    if not deep_review:
        present = {it["topic_id"] for it in pool} | {t_topic}
        others = [t for t in questions if t not in present]
        rng = random.Random(today_day * 13)
        rng.shuffle(others)
        for ot in others[:0]:  # off-lesson cross-domain draws disabled: keep the daily set = today's lesson + due reviews
            ot_qs = sample_questions(ot, questions, 1, today_day * 17 + hash(ot) % 100)
            if ot_qs:
                oi, q = ot_qs[0]
                pool.append({"topic_id": ot, "orig_idx": oi, "q": q,
                             "domain": topic_domain.get(ot, "CM")})
    practice_html = render_practice_section(pool, topic_domain)

    # core question set for the completion-aware resume: a day is 'done'
    # only when ALL of these are graded. Includes pretest + today-topic +
    # review-topic questions; excludes the random cross-domain bonus draws.
    _rtopics = {l['topic_id'] for _i, l in reviews}
    _core = set()
    for _oi, _q in pre_qs:
        _core.add(t_topic + '__' + str(_oi))
    for _it in pool:
        if _it['topic_id'] == t_topic or _it['topic_id'] in _rtopics:
            _core.add(_it['topic_id'] + '__' + str(_it['orig_idx']))
    global LAST_PAGE_QIDS
    LAST_PAGE_QIDS = sorted(_core)

    new_count = len(pre_qs) + len(pool)

    weekday = today.strftime("%A")
    date_str = today.strftime("%B %d, %Y")
    # Version + Manila build stamp (site rule: every page shows when it was built).
    try:
        from zoneinfo import ZoneInfo as _ZI
        _build_now = _dt.datetime.now(_ZI("Asia/Manila"))
    except Exception:
        _build_now = _dt.datetime.now()
    build_stamp = f'{SITE_VERSION} &middot; built {_build_now.strftime("%b %d, %Y %H:%M")} Manila'
    # Total authored days = the last day of the final curriculum phase.
    total_days = max(int(p["days"].split("-")[-1]) for p in meta["phases"])
    phase = next((p for p in meta["phases"]
                  if int(p["days"].split("-")[0]) <= today_day <= int(p["days"].split("-")[1])), None)
    phase_label = f'Phase {phase["phase"]}: {phase["name"]}' if phase else "Deep review phase — curriculum complete"
    domains_html = " ".join(f'<span class="dchip">{esc(v)}</span>' for v in meta["domains"].values())

    questions_json = json.dumps(questions, ensure_ascii=False)
    domains_json = json.dumps(topic_domain, ensure_ascii=False)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>HYROX L2 — {date_str}</title>
<style>{css}</style>
<style>{theme_css}</style>
<style>{motif_css}</style>
</head>
<body class="{theme["body_class"]}">
<div class="container">
  <header class="top">
    <div class="h-day">HYROX L2 · Day {today_day} · {weekday}</div>
    <div class="h-date">{date_str}</div>
    <div class="h-build" style="font-size:10px;color:var(--text-dim);opacity:.75;margin-top:2px">{build_stamp}</div>
    <div class="h-phase">{esc(phase_label)}</div>
    <div class="domains">{domains_html}</div>
    <div class="progress"><div class="bar" style="width: {min(100, today_day / total_days * 100):.1f}%;"></div></div>
    <div class="session-goal">Today: <b id="goal-new">{new_count}</b> new &middot; <b id="goal-due">0</b> due &middot; ~<b id="goal-min">25</b> min <span class="sg-note">— attendance, not a streak</span></div>
  </header>
  <nav class="lesson-nav" aria-label="Lesson navigation"><a class="ln-prev" id="ln-prev" href="#" onclick="return cscsNavPrev();">&larr; Previous lesson</a><span class="ln-here">Day {today_day} &middot; {date_str}</span><a class="ln-next" id="ln-next" href="#" onclick="return cscsNavNext();">Next lesson &rarr;</a></nav>
  <div class="browse-all">Everything for this module is on this page. <a href="../modules.html">Browse all modules &amp; lessons</a></div>
  <div class="study-tip">
    <b>How to use this:</b> recall and type an answer <b>before</b> you reveal — the reveal stays locked until you commit.
    After the answer, grade yourself <b>Again / Hard / Good / Easy</b>; that grade schedules the card with
    <b>FSRS</b> (the algorithm behind Anki). Rate <b>confidence first</b> so the dashboard can show where you're
    over- or under-confident. Everything saves in your browser.
    <div style="margin-top: 8px; font-size: 11px; color: var(--text-dim);">
      <span id="lifetime-stats">Lifetime: <b>0</b> tracked · <b>0</b> due now</span> ·
      <a href="#" onclick="exportProgress(); return false;" style="color: var(--theme-accent);">Export progress (JSON)</a> ·
      <label style="cursor: pointer; color: var(--theme-accent);">
        Import <input type="file" accept=".json" style="display:none" onchange="if(this.files[0]) importProgress(this.files[0])">
      </label>
    </div>
  </div>
  <div id="cscs-dashboard"></div>
  <div class="session-summary" id="session-summary">
    <div class="stat"><b>{1 if not deep_review else 0}</b>new lesson{"s" if deep_review else ""}</div>
    <div class="stat"><b>{len(reviews)}</b>spaced reviews</div>
    <div class="stat"><b>{new_count}</b>questions</div>
    <div class="stat"><b id="self-score">0</b>passed today</div>
  </div>
  <button type="button" class="sched-open">&#9201; View full review schedule &mdash; what&rsquo;s coming back &amp; when</button>
  <div id="personal-reviews"></div>
  {pretest_html}
  {today_card}
  {review_html}
  <h2 style="margin: 26px 0 8px; font-size: 20px; font-weight: 700;">Practice questions</h2>
  <p style="font-size: 13px; color: var(--text-dim); margin: 0 0 14px;">Forced retrieval first, then grade yourself. Whatever you miss resurfaces on the FSRS-chosen day.</p>
  {practice_html}
  <footer>
    HYROX Academy — Level 2 <i>Mastering Performance</i> · original study notes · Scheduling: <b>FSRS</b> (ts-fsrs) · spacing principle: Cepeda et al. 2008<br>
    <code>hyrox_{today.isoformat()}.html</code> · also written to <code>hyrox_today.html</code> (rolling, for localStorage persistence)
  </footer>
</div>
<script>window.__CSCS_QUESTIONS = {questions_json};</script>
<script>window.__CSCS_DOMAINS = {domains_json};</script>
<script>window.__CSCS_NEWCOUNT = {new_count};</script>
<script>window.__CSCS_PAGE_DATE = "{page_date}";window.__CSCS_PREV = {prev_json}; window.__CSCS_NEXT = {next_json};</script>
{FSRS_MODULE}
<script>{js}</script>
</body>
</html>
'''


def build_index_html(base_html, available, this_iso, dtopic=None):
    """Wrap the day's page as a self-correcting landing page.
    Injects a tiny script that:
      1. Computes *today* in Asia/Manila (viewer's own clock is irrelevant).
      2. Looks at localStorage hyroxl2.state.v1 to find dates the user has
         already answered questions on (grouped by Manila date).
      3. Redirects to the EARLIEST archive date that is <= today AND has no
         answer activity yet — so missed days resume on the right page rather
         than skipping ahead. If everything up to today is done, goes to today.
      4. On a fresh device (no state yet), defaults to today so a brand-new
         visitor doesn't get sent back to Day 1."""
    days = json.dumps(sorted(available))
    dtopic_json = json.dumps(dtopic or {})
    # Per-day CORE question stable-ids: a day counts as DONE only when the
    # user has graded EVERY one of them. Baked so the redirect can decide
    # completion from graded cards (local UNION remote) with no per-page
    # bookkeeping. Falls back to touchedDays/topic if a day has no set.
    _avail = set(available)
    _dayq = {}
    try:
        _cp = DATA / 'day_completion.json'
        if _cp.exists():
            for _d, _ids in json.loads(_cp.read_text(encoding='utf-8')).items():
                if _d in _avail:
                    _dayq[_d] = _ids
    except Exception:
        _dayq = {}
    dayq_json = json.dumps(_dayq)
    redirect = (
        '<script>(function(){'
        'var DAYS=' + days + ';var DTOPIC=' + dtopic_json + ';var DAYQ=' + dayq_json + ';var THIS="' + this_iso + '";'
        # No gist id is baked (none exists yet for this site) — but once the
        # user configures cloud sync on a device, its stored gist id makes the
        # remote-resume branch live, so a locally-wiped device still resumes.
        'var GIST="";try{GIST=localStorage.getItem("hyroxl2.sync.gist_id")||"";}catch(e){}'
        'var GFILE="hyrox-l2-progress.json";'
        'function mt(d){try{var p=new Intl.DateTimeFormat("en-CA",{timeZone:"Asia/Manila",'
        'year:"numeric",month:"2-digit",day:"2-digit"}).formatToParts(d||new Date());'
        'var o={};p.forEach(function(x){o[x.type]=x.value;});return o.year+"-"+o.month+"-"+o.day;}'
        'catch(e){return null;}}'
        'var today=mt();if(!today){location.replace("daily/hyrox_"+THIS+".html");return;}'
        'function go(t){location.replace("daily/hyrox_"+(t||THIS)+".html");}'
        'try{var ov=document.createElement("div");ov.id="sa-resume";'
        'ov.textContent="Finding your place...";'
        'ov.setAttribute("style","position:fixed;inset:0;display:flex;align-items:center;'
        'justify-content:center;background:#0b0e14;color:#9ba3b4;font:14px -apple-system,Segoe UI,sans-serif;z-index:99999");'
        '(document.documentElement||document).appendChild(ov);'
        'setTimeout(function(){var o=document.getElementById("sa-resume");if(o&&o.parentNode)o.parentNode.removeChild(o);},8000);'
        '}catch(e){}'
        'function readLocal(){try{var raw=localStorage.getItem("hyroxl2.state.v1");return raw?JSON.parse(raw):null;}catch(e){return null;}}'
        'function harvest(s,reviewed,engaged,cards){if(!s)return;var tt=s.touchedDays||{};for(var k in tt){if(tt[k])reviewed[k]=true;}'
        'var cc=s.cards||{};for(var ck in cc){engaged[ck.split("__")[0]]=true;cards[ck]=true;}}'
        # touchedDays is the page-identity truth and wins FIRST: if the user
        # engaged a day, a later change to that day's question set (rewrite /
        # reorder) must never be able to pin them to it forever.
        'function complete(d,reviewed,engaged,cards){if(reviewed[d])return true;'
        'var qs=DAYQ[d];'
        'if(qs&&qs.length){for(var i=0;i<qs.length;i++){if(!cards[qs[i]])return false;}return true;}'
        'return (DTOPIC[d]&&engaged[DTOPIC[d]]);}'
        'function decide(reviewed,engaged,cards,hasState){var tg=null;'
        'if(hasState){for(var i=0;i<DAYS.length;i++){var d=DAYS[i];if(d>today)break;'
        'if(!complete(d,reviewed,engaged,cards)){tg=d;break;}}'
        'if(!tg){tg=(DAYS.indexOf(today)!==-1)?today:DAYS[DAYS.length-1];}}'
        # Fresh visitor: every lesson is already unlocked (dates are backdated),
        # so start at Module 1 Day 1 rather than at 'today' (= the final lesson).
        'else{tg=DAYS[0];}'
        'return tg||THIS;}'
        'var local=readLocal();var settled=false;'
        'function finish(remote){if(settled)return;settled=true;'
        'var reviewed={},engaged={},cards={};harvest(local,reviewed,engaged,cards);harvest(remote,reviewed,engaged,cards);'
        'var hasState=!!(Object.keys(reviewed).length||Object.keys(engaged).length||Object.keys(cards).length);go(decide(reviewed,engaged,cards,hasState));}'
        'var token="";try{token=localStorage.getItem("hyroxl2.sync.token")||"";}catch(e){}'
        'if(!GIST){finish(null);return;}'
        'var to=setTimeout(function(){finish(null);},4500);'
        'try{var hd={"Accept":"application/vnd.github+json"};if(token)hd["Authorization"]="token "+token;'
        'fetch("https://api.github.com/gists/"+GIST,{headers:hd,cache:"no-store"})'
        '.then(function(r){return r.ok?r.json():Promise.reject();})'
        '.then(function(d){var f=d.files&&d.files[GFILE];if(!f)return Promise.reject();'
        'if(f.truncated&&f.raw_url)return fetch(f.raw_url).then(function(x){return x.text();});return f.content;})'
        '.then(function(txt){var p=JSON.parse(txt);clearTimeout(to);finish(p&&p.state?p.state:null);})'
        '.catch(function(){clearTimeout(to);finish(null);});'
        '}catch(e){clearTimeout(to);finish(null);}'
        '})();</script>'
    )
    # The landing page must never be served stale from cache, or an old
    # redirect script (with outdated resume logic) sends the user to the
    # wrong day. GitHub Pages sets max-age=600; these discourage bfcache /
    # heuristic caching so the browser revalidates the index each visit.
    CACHE_META = (
        '<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">'
        '<meta http-equiv="Pragma" content="no-cache">'
        '<meta http-equiv="Expires" content="0">'
    )
    # Root landing page lives beside modules.html, not inside daily/ — undo
    # the daily-relative prefixes for this one output. Normally invisible
    # (the head redirect fires first), but with JS off or a failed redirect
    # these links are what the visitor gets.
    base_html = base_html.replace('href="../modules.html"', 'href="modules.html"')
    base_html = base_html.replace('window.location.href = "hyrox_"', 'window.location.href = "daily/hyrox_"')
    base_html = base_html.replace(
        '<div class="container">',
        '<noscript><div style="padding:12px 16px;font:14px sans-serif;background:#231f1f;color:#eee">'
        'JavaScript is off, so the resume redirect can\'t run — '
        '<a href="modules.html" style="color:#7fd4ff">browse all modules &amp; lessons</a> instead.</div></noscript>'
        '<div class="container">', 1)
    return base_html.replace("<head>", "<head>\n" + CACHE_META + redirect, 1)



def build_day(build_date, curriculum, questions, is_entry):
    """Render one dated daily page. When is_entry is True this date is 'today':
    it also writes the rolling copy and the index.html landing page."""
    meta = curriculum["meta"]
    today_day = day_number(meta["start_date"], build_date)
    if today_day < 1:
        print(f"{build_date} is before curriculum start. No file generated.")
        return 1
    lessons = curriculum["lessons"]
    # Map every question topic to its L2 domain (for interleaving + calibration).
    topic_domain = {l["topic_id"]: l.get("domain", "CM") for l in lessons.values()}
    for t in questions:
        topic_domain.setdefault(t, "CM")
    today_lesson, deep_review = get_today_lesson(today_day, lessons)
    reviews = pick_review_lessons(today_day, lessons, meta.get("seen_through_day", 0))
    html = render_html(build_date, today_day, today_lesson, deep_review, reviews, questions, meta, topic_domain)
    try:
        _cp = DATA / 'day_completion.json'
        _comp = {}
        if _cp.exists():
            _comp = json.loads(_cp.read_text(encoding='utf-8'))
        _comp[build_date.isoformat()] = LAST_PAGE_QIDS
        _cp.write_text(json.dumps(_comp, ensure_ascii=False), encoding='utf-8')
    except Exception:
        pass
    OUT.mkdir(parents=True, exist_ok=True)
    dated_path = OUT / f"hyrox_{build_date.isoformat()}.html"
    dated_path.write_text(html, encoding="utf-8")
    print(f"Wrote {dated_path}")
    if not is_entry:
        return 0
    rolling_path = OUT / "hyrox_today.html"
    index_path = ROOT / "index.html"  # GitHub Pages entry point
    rolling_path.write_text(html, encoding="utf-8")
    # Index is the GitHub Pages entry point: make it self-correct to Manila "today".
    _start = meta["start_date"]
    available = sorted({d for p in OUT.glob("hyrox_2*.html") if (d := p.stem.replace("hyrox_", "")) >= _start})
    if build_date.isoformat() not in available:
        available.append(build_date.isoformat())
        available.sort()
    _sd = _dt.date.fromisoformat(meta["start_date"])
    _lesson_dates = {}
    for _k, _les in lessons.items():
        try:
            _dd = (_sd + _dt.timedelta(days=int(_k) - 1)).isoformat()
            _tid = _les.get("topic_id")
            if _tid:
                _lesson_dates[_dd] = _tid
        except Exception:
            pass
    index_path.write_text(build_index_html(html, available, build_date.isoformat(), _lesson_dates), encoding="utf-8")
    print(f"Wrote {rolling_path} (rolling)")
    print(f"Wrote {index_path} (GitHub Pages entry)")
    return 0


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int, help="Override day_number (e.g. --day 2)")
    parser.add_argument("--date", type=str, help="Pretend today is this ISO date (e.g. --date 2026-05-20)")
    parser.add_argument("--all", action="store_true",
                        help="Rebuild EVERY dated page from start_date through max(today, last existing page)")
    args, _ = parser.parse_known_args()

    curriculum, questions = load_data()
    meta = curriculum["meta"]
    start = _dt.date.fromisoformat(meta["start_date"])
    if args.date:
        today = _dt.date.fromisoformat(args.date)
    elif args.day:
        # If just --day given, compute synthetic "today" so file naming matches
        today = start + _dt.timedelta(days=args.day - 1)
    else:
        today = today_local()

    if args.all:
        # Full regeneration: every date from start through the later of Manila
        # today and the last pre-generated page (the authored calendar runs
        # ahead of the wall clock).
        span = _archive_dates(meta["start_date"])
        for iso in span:
            d = _dt.date.fromisoformat(iso)
            build_day(d, curriculum, questions, is_entry=(d == today))
        if today.isoformat() not in span:
            build_day(today, curriculum, questions, is_entry=True)
        return 0

    if not (args.date or args.day):
        # Self-heal: a failed nightly run used to leave a permanent hole in the
        # archive (the cron only ever built "today"). Backfill any missing
        # dates before building today's page.
        existing = {p.stem.replace("hyrox_", "") for p in OUT.glob("hyrox_2*.html")}
        d = start
        while d < today:
            if d.isoformat() not in existing:
                print(f"Backfilling missed day {d.isoformat()}")
                build_day(d, curriculum, questions, is_entry=False)
            d += _dt.timedelta(days=1)

    return build_day(today, curriculum, questions, is_entry=True)


if __name__ == "__main__":
    sys.exit(main())
