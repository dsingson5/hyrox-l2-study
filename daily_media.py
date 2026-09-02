#!/usr/bin/env python3
"""Daily lesson media — animated infographic + cinematic scene player.

Pure-Python string generation: no network, no binaries, no external deps, so it
runs identically on a laptop and inside the GitHub Actions daily build.

Two artefacts per lesson, both self-contained in the day's page:

  render_infographic(...)  a one-screen animated SVG poster of the lesson —
                           concept hub, radiating key-fact nodes, coaching band.
  render_cinematic(...)    a six-scene autoplaying "video" built from CSS
                           keyframes + a tiny scene stepper: hook, concept,
                           facts, real-world coaching application, recall.

Both are seeded per (topic_id, date) so the motion and layout differ day to day
while staying reproducible for a given day.
"""
from __future__ import annotations

import hashlib
import html as _html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HOOKS_PATH = ROOT / "data" / "hooks.json"

_HOOKS_CACHE = None


def esc(s) -> str:
    return _html.escape(str(s or ""), quote=True)


def _seed(*parts) -> int:
    """Stable integer seed from the given parts."""
    h = hashlib.sha256("|".join(str(p) for p in parts).encode("utf-8")).hexdigest()
    return int(h[:12], 16)


def _pick(options, *seed_parts):
    """Deterministic choice from options."""
    if not options:
        return ""
    return options[_seed(*seed_parts) % len(options)]


def load_hooks() -> dict:
    """Per-topic emotional framing, authored in data/hooks.json.

    Shape: {topic_id: {"hook": str, "stakes": str, "beat": str}}
    Missing topics fall back to a composed hook, so a lesson is never blank.
    """
    global _HOOKS_CACHE
    if _HOOKS_CACHE is None:
        try:
            _HOOKS_CACHE = json.loads(HOOKS_PATH.read_text(encoding="utf-8"))
        except Exception:
            _HOOKS_CACHE = {}
    return _HOOKS_CACHE


# Fallback scene-one framings, chosen by domain. These are deliberately about
# the coaching moment, not the textbook — the point is to attach the fact to a
# situation David has actually stood in.
_FALLBACK_HOOKS = {
    "CM": [
        "An athlete texts you at 11pm the night before their race. What you say back is already decided — or it isn't.",
        "Two athletes, same session, same numbers. One is thriving and one is quietly breaking. What tells you which is which?",
        "The moment an athlete asks you to justify a decision is the moment you find out whether you had a reason.",
    ],
    "SM": [
        "Something hurts. They want to keep going. You have about four seconds to decide what kind of coach you are.",
        "The injury didn't happen today. It happened in a session six weeks ago that looked completely fine.",
        "Knowing when to refer out is not an admission that you're limited. It's the clearest signal that you're competent.",
    ],
    "BM": [
        "Station six. Form is going. You can see exactly what's wrong — can you name it fast enough to fix it?",
        "Every fault you can't see is a fault you'll cue wrong. Every fault you cue wrong costs them minutes.",
        "The difference between a good rep and a no-rep is usually a detail you were never taught to look for.",
    ],
    "PH": [
        "They're fading at the same point every single race. The answer is in a system you can't see from the floor.",
        "Fuel, heat, and pacing decide more races than fitness does — and all three are coachable.",
        "The body is already telling you what it can and can't do. This is how you read it.",
    ],
    "PG": [
        "Twelve weeks out. You have one plan and no second chances. What goes in, and what gets cut?",
        "Every session you add is a session you take from recovery. Programming is subtraction as much as addition.",
        "A plan that survives contact with a real athlete's week is worth more than a perfect one that doesn't.",
    ],
}


def hook_for(lesson: dict) -> dict:
    """Return {"hook","stakes","beat"} for a lesson — authored or composed."""
    tid = lesson.get("topic_id", "")
    authored = load_hooks().get(tid)
    if authored and authored.get("hook"):
        return {
            "hook": authored.get("hook", ""),
            "stakes": authored.get("stakes", "") or _first_sentence(lesson.get("key_concept", "")),
            "beat": authored.get("beat", "") or "Why it matters",
        }
    domain = lesson.get("domain", "CM")
    pool = _FALLBACK_HOOKS.get(domain, _FALLBACK_HOOKS["CM"])
    return {
        "hook": _pick(pool, tid, domain),
        "stakes": _first_sentence(lesson.get("key_concept", "")),
        "beat": "Why it matters",
    }


def _first_sentence(text: str, limit: int = 200) -> str:
    t = re.sub(r"\s+", " ", (text or "").strip())
    if not t:
        return ""
    m = re.split(r"(?<=[.!?])\s+", t)
    out = m[0] if m else t
    if len(out) > limit:
        out = out[:limit].rsplit(" ", 1)[0] + "…"
    return out


def _clip_sentence(text: str, limit: int = 200) -> str:
    """Trim to <=limit chars, preferring to end on a sentence boundary."""
    t = re.sub(r"\s+", " ", (text or "").strip())
    if len(t) <= limit:
        return t
    cut = t[:limit]
    for end in (". ", "? ", "! ", "; "):
        k = cut.rfind(end)
        if k > limit * 0.55:
            return cut[:k + 1]
    return cut.rsplit(" ", 1)[0] + "\u2026"


def _short(text: str, limit: int = 118) -> str:
    t = re.sub(r"\s+", " ", (text or "").strip())
    if len(t) <= limit:
        return t
    return t[:limit].rsplit(" ", 1)[0] + "…"


def _wrap(text: str, width: int) -> list[str]:
    """Greedy word wrap to <=width chars per line."""
    words = re.sub(r"\s+", " ", (text or "").strip()).split(" ")
    lines, cur = [], ""
    for w in words:
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= width:
            cur += " " + w
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _tspans(text: str, width: int, x: float, dy_first: float, dy: float,
            max_lines: int = 4, cls: str = "") -> str:
    lines = _wrap(text, width)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(" .,;:") + "…"
    out = []
    for i, ln in enumerate(lines):
        d = dy_first if i == 0 else dy
        c = f' class="{cls}"' if cls else ""
        out.append(f'<tspan x="{x:.1f}" dy="{d:.1f}"{c}>{esc(ln)}</tspan>')
    return "".join(out)


def render_infographic(lesson: dict, theme: dict, dtheme: dict,
                       day_num: int, date_iso: str) -> str:
    """One-screen animated SVG poster summarising the lesson."""
    import math

    accent = dtheme.get("accent", "#5ec8ff")
    accent2 = dtheme.get("accent_2", "#8fdfff")
    ink = theme.get("text", "#e8e8ea")
    dim = theme.get("text_dim", "#9aa0a8")
    surf = theme.get("surface", "#171a1f")
    surf2 = theme.get("surface_2", "#1f242b")
    bord = theme.get("border", "#33383f")
    tid = lesson.get("topic_id", "")

    facts = [f for f in (lesson.get("key_facts") or []) if f][:5]
    n = len(facts)
    uid = f"ig{_seed(tid, date_iso) % 100000}"

    # Radial node layout — start angle rotates with the day so the poster is
    # laid out differently each morning without ever overlapping the hub.
    start_deg = -90 + (_seed(tid, date_iso, "rot") % 40) - 20
    cx, cy = 500.0, 292.0
    rx, ry = 336.0, 172.0

    nodes, links = [], []
    for i, fact in enumerate(facts):
        ang = math.radians(start_deg + (360.0 / max(n, 1)) * i)
        nx = cx + rx * math.cos(ang)
        ny = cy + ry * math.sin(ang)
        # keep nodes inside the canvas
        nx = min(max(nx, 158.0), 842.0)
        ny = min(max(ny, 152.0), 452.0)
        # nodes low on the canvas get fewer lines so they clear the band
        nlines = 3 if ny > 336.0 else 4
        delay = 0.55 + i * 0.22
        links.append(
            f'<line class="ig-link" x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" '
            f'style="animation-delay:{delay:.2f}s"/>'
        )
        lines = _wrap(_short(fact, 132 if nlines == 4 else 100), 30)
        if len(lines) > nlines:
            lines = lines[:nlines]
            lines[-1] = lines[-1].rstrip(" .,;:") + "\u2026"
        above = ny < cy - 30.0
        first = -(len(lines) - 1) * 15.0 - 16.0 if above else 26.0
        spans = "".join(
            f'<tspan x="{nx:.1f}" dy="{(first if j == 0 else 15.0):.1f}">{esc(ln)}</tspan>'
            for j, ln in enumerate(lines))
        nodes.append(
            f'<g class="ig-node" style="animation-delay:{delay + 0.15:.2f}s">'
            f'<circle class="ig-dot" cx="{nx:.1f}" cy="{ny:.1f}" r="7"/>'
            f'<circle class="ig-halo" cx="{nx:.1f}" cy="{ny:.1f}" r="7" '
            f'style="animation-delay:{delay + 0.6:.2f}s"/>'
            f'<text class="ig-ntext" x="{nx:.1f}" y="{ny:.1f}" text-anchor="middle">'
            f'{spans}</text></g>'
        )

    concept_lines = _tspans(_short(lesson.get("key_concept", ""), 150), 26, cx, 6, 19,
                            max_lines=4)
    title = _short(lesson.get("title", ""), 70)
    coach = _clip_sentence(lesson.get("training_link", ""), 208)
    coach_lines = _tspans(coach, 104, 64, 26, 20, max_lines=2)
    dom_name = dtheme.get("name", "")

    return f"""
<figure class="daily-infographic" id="{uid}" aria-label="Infographic: {esc(title)}">
<figcaption class="ig-cap"><span class="ig-cap-k">Today's picture</span>
<span class="ig-cap-t">{esc(title)}</span></figcaption>
<svg viewBox="0 0 1000 700" role="img" preserveAspectRatio="xMidYMid meet">
  <defs>
    <radialGradient id="{uid}-hub" cx="50%" cy="42%" r="62%">
      <stop offset="0%" stop-color="{accent}" stop-opacity=".30"/>
      <stop offset="70%" stop-color="{accent}" stop-opacity=".06"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="{uid}-band" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{accent}" stop-opacity=".22"/>
      <stop offset="100%" stop-color="{accent2}" stop-opacity=".04"/>
    </linearGradient>
    <filter id="{uid}-soft" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="9"/>
    </filter>
  </defs>

  <rect x="0" y="0" width="1000" height="700" rx="20" fill="{surf}"/>
  <ellipse cx="{cx}" cy="{cy}" rx="428" ry="252" fill="url(#{uid}-hub)"/>

  <text class="ig-day" x="40" y="52">DAY {day_num} · {esc(dom_name.upper())}</text>

  {"".join(links)}

  <g class="ig-hub">
    <ellipse class="ig-hub-e" cx="{cx}" cy="{cy}" rx="196" ry="112"/>
    <ellipse class="ig-hub-glow" cx="{cx}" cy="{cy}" rx="196" ry="112" filter="url(#{uid}-soft)"/>
    <text class="ig-hub-k" x="{cx}" y="{cy - 74:.0f}" text-anchor="middle">THE IDEA</text>
    <text class="ig-hub-t" x="{cx}" y="{cy - 42:.0f}" text-anchor="middle">{concept_lines}</text>
  </g>

  {"".join(nodes)}

  <g class="ig-band">
    <rect x="40" y="576" width="920" height="98" rx="14" fill="url(#{uid}-band)" stroke="{bord}"/>
    <text class="ig-band-k" x="64" y="606">IN YOUR COACHING</text>
    <text class="ig-band-t" x="64" y="606">{coach_lines}</text>
  </g>
</svg>
<style>
#{uid} {{ --a:{accent}; --a2:{accent2}; --ink:{ink}; --dim:{dim}; --surf2:{surf2}; --bord:{bord}; }}
#{uid} .ig-day {{ fill:var(--dim); font:600 13px/1 ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif; letter-spacing:.16em; }}
#{uid} .ig-link {{ stroke:var(--a); stroke-width:1.6; stroke-opacity:.45; stroke-dasharray:420;
  stroke-dashoffset:420; animation:{uid}-draw .85s cubic-bezier(.22,.61,.36,1) forwards; }}
#{uid} .ig-hub-e {{ fill:var(--surf2); stroke:var(--a); stroke-opacity:.55; stroke-width:1.6; }}
#{uid} .ig-hub-glow {{ fill:none; stroke:var(--a); stroke-opacity:.30; stroke-width:2.4; }}
#{uid} .ig-hub {{ opacity:0; animation:{uid}-pop .7s cubic-bezier(.22,1.2,.36,1) .12s forwards; }}
#{uid} .ig-hub-k {{ fill:var(--a); font:700 11px/1 ui-sans-serif,system-ui,sans-serif; letter-spacing:.22em; }}
#{uid} .ig-hub-t {{ fill:var(--ink); font:600 17px/1.35 ui-sans-serif,system-ui,sans-serif; }}
#{uid} .ig-node {{ opacity:0; animation:{uid}-rise .6s cubic-bezier(.22,.61,.36,1) forwards; }}
#{uid} .ig-dot {{ fill:var(--a); }}
#{uid} .ig-halo {{ fill:none; stroke:var(--a); stroke-width:2; opacity:0;
  animation:{uid}-ping 3.4s ease-out infinite; }}
#{uid} .ig-ntext {{ fill:var(--ink); font:500 13px/1.3 ui-sans-serif,system-ui,sans-serif; opacity:.94; }}
#{uid} .ig-band {{ opacity:0; animation:{uid}-rise .7s ease-out 1.9s forwards; }}
#{uid} .ig-band-k {{ fill:var(--a); font:700 10px/1 ui-sans-serif,system-ui,sans-serif; letter-spacing:.2em; }}
#{uid} .ig-band-t {{ fill:var(--ink); font:500 13.5px/1.4 ui-sans-serif,system-ui,sans-serif; }}
@keyframes {uid}-draw {{ to {{ stroke-dashoffset:0; }} }}
@keyframes {uid}-pop {{ from {{ opacity:0; transform:scale(.92); transform-origin:{cx}px {cy}px; }}
  to {{ opacity:1; transform:scale(1); }} }}
@keyframes {uid}-rise {{ from {{ opacity:0; transform:translateY(10px); }} to {{ opacity:1; transform:none; }} }}
@keyframes {uid}-ping {{ 0% {{ opacity:.55; transform:scale(1); transform-box:fill-box; transform-origin:center; }}
  70%,100% {{ opacity:0; transform:scale(3.6); transform-box:fill-box; transform-origin:center; }} }}
@media (prefers-reduced-motion: reduce) {{
  #{uid} .ig-link,#{uid} .ig-hub,#{uid} .ig-node,#{uid} .ig-band {{ animation:none!important; opacity:1!important; stroke-dashoffset:0!important; }}
  #{uid} .ig-halo {{ display:none; }}
}}
</style>
</figure>"""


_PLAYER_JS = r"""
(function(){
  var root = document.getElementById('__UID__');
  if(!root) return;
  var scenes = [].slice.call(root.querySelectorAll('.cn-scene'));
  var segs   = [].slice.call(root.querySelectorAll('.cn-seg i'));
  var btn    = root.querySelector('.cn-play');
  var lbl    = root.querySelector('.cn-count');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var i = 0, timer = null, playing = false;
  var DUR = scenes.map(function(s){ return (parseFloat(s.getAttribute('data-dur')) || 6) * 1000; });

  function paint(){
    scenes.forEach(function(s,k){ s.classList.toggle('on', k===i); });
    segs.forEach(function(g,k){
      g.style.transition = 'none';
      g.style.width = k < i ? '100%' : '0%';
    });
    if(lbl) lbl.textContent = (i+1) + ' / ' + scenes.length;
  }
  function runSeg(){
    var g = segs[i]; if(!g) return;
    void g.offsetWidth;
    g.style.transition = 'width ' + (DUR[i]/1000) + 's linear';
    g.style.width = '100%';
  }
  function go(n, keepPlaying){
    i = (n + scenes.length) % scenes.length;
    paint();
    clearTimeout(timer);
    if(playing || keepPlaying){ runSeg(); timer = setTimeout(next, DUR[i]); }
  }
  function next(){
    if(i === scenes.length - 1){ pause(); return; }
    go(i+1, true);
  }
  function play(){
    playing = true; root.classList.add('playing');
    if(btn){ btn.setAttribute('aria-label','Pause'); btn.innerHTML = '<svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>'; }
    go(i, true);
  }
  function pause(){
    playing = false; root.classList.remove('playing');
    clearTimeout(timer);
    segs.forEach(function(g){ var w = getComputedStyle(g).width; g.style.transition='none'; g.style.width = w; });
    if(btn){ btn.setAttribute('aria-label','Play'); btn.innerHTML = '<svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>'; }
  }
  if(btn) btn.addEventListener('click', function(){ playing ? pause() : play(); });
  var pv = root.querySelector('.cn-prev'), nx = root.querySelector('.cn-next');
  if(pv) pv.addEventListener('click', function(){ go(i-1); });
  if(nx) nx.addEventListener('click', function(){ go(i+1); });
  root.addEventListener('keydown', function(e){
    if(e.key === 'ArrowRight'){ go(i+1); e.preventDefault(); }
    if(e.key === 'ArrowLeft'){ go(i-1); e.preventDefault(); }
    if(e.key === ' '){ playing ? pause() : play(); e.preventDefault(); }
  });
  paint();
  if(!reduce && 'IntersectionObserver' in window){
    var seen = false;
    new IntersectionObserver(function(en){
      en.forEach(function(x){
        if(x.isIntersecting && !seen){ seen = true; play(); }
        else if(!x.isIntersecting && playing){ pause(); }
      });
    }, {threshold:.45}).observe(root);
  }
})();
"""


def _scene(idx, dur, kicker, body_html, accent_note="", extra_cls=""):
    return (f'<article class="cn-scene {extra_cls}" data-dur="{dur}" data-i="{idx}">'
            f'<div class="cn-kick">{esc(kicker)}</div>'
            f'{body_html}'
            + (f'<div class="cn-note">{esc(accent_note)}</div>' if accent_note else "")
            + '</article>')


def render_cinematic(lesson: dict, theme: dict, dtheme: dict,
                     day_num: int, date_iso: str, video_url: str = "") -> str:
    """Six-scene autoplaying motion piece built from the lesson's own content."""
    accent = dtheme.get("accent", "#5ec8ff")
    accent2 = dtheme.get("accent_2", "#8fdfff")
    ink = theme.get("text", "#e8e8ea")
    dim = theme.get("text_dim", "#9aa0a8")
    surf = theme.get("surface", "#171a1f")
    surf2 = theme.get("surface_2", "#1f242b")
    bord = theme.get("border", "#33383f")
    tid = lesson.get("topic_id", "")
    uid = f"cn{_seed(tid, date_iso, 'cine') % 100000}"

    h = hook_for(lesson)
    title = lesson.get("title", "")
    dom_name = dtheme.get("name", "")
    facts = [f for f in (lesson.get("key_facts") or []) if f][:4]
    coach = lesson.get("training_link", "")
    exam = lesson.get("exam_focus", "")

    # 1 — title card
    s1 = _scene(0, 4.0, f"Day {day_num} · {dom_name}",
                f'<h3 class="cn-title">{esc(title)}</h3>'
                f'<div class="cn-rule"></div>')
    # 2 — the emotional hook
    s2 = _scene(1, 7.0, h["beat"],
                f'<p class="cn-hook">{esc(h["hook"])}</p>', extra_cls="cn-dark")
    # 3 — the idea
    s3 = _scene(2, 8.0, "The idea",
                f'<p class="cn-lead">{esc(_clip_sentence(lesson.get("key_concept", ""), 320))}</p>')
    # 4 — the facts, staggered
    fact_items = "".join(
        f'<li style="--d:{0.35 + k * 0.75:.2f}s"><span class="cn-num">{k+1}</span>'
        f'<span>{esc(_short(f, 190))}</span></li>' for k, f in enumerate(facts))
    s4 = _scene(3, max(6.0, 2.2 + 1.9 * len(facts)), "What has to stick",
                f'<ul class="cn-facts">{fact_items}</ul>')
    # 5 — the real-world coaching application
    s5 = _scene(4, 9.0, "On the floor",
                f'<p class="cn-lead">{esc(_clip_sentence(coach, 330))}</p>',
                accent_note=h["stakes"], extra_cls="cn-warm")
    # 6 — recall prompt
    s6 = _scene(5, 8.0, "Close your eyes and say it",
                f'<p class="cn-recall">{esc(_clip_sentence(exam or lesson.get("key_concept", ""), 300))}</p>',
                extra_cls="cn-dark")

    video_html = ""
    if video_url:
        vid = esc(video_url)
        video_html = (
            f'<details class="cn-video"><summary>Watch the narrated version '
            f'<span class="cn-vhint">· NotebookLM</span></summary>'
            f'<div class="cn-vwrap"><iframe src="{vid}" title="Narrated overview" '
            f'loading="lazy" frameborder="0" allowfullscreen '
            f'allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"></iframe>'
            f'</div></details>')

    js = _PLAYER_JS.replace("__UID__", uid)

    return f"""
<section class="daily-cinematic" id="{uid}" tabindex="0" aria-label="Lesson replay: {esc(title)}">
  <div class="cn-stage">
    {s1}{s2}{s3}{s4}{s5}{s6}
  </div>
  <div class="cn-bar">
    <button class="cn-prev" type="button" aria-label="Previous scene">
      <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M15 5v14L4 12z"/></svg></button>
    <button class="cn-play" type="button" aria-label="Play">
      <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
    <button class="cn-next" type="button" aria-label="Next scene">
      <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M9 5v14l11-7z"/></svg></button>
    <div class="cn-seg">{"".join('<span><i></i></span>' for _ in range(6))}</div>
    <span class="cn-count">1 / 6</span>
  </div>
  {video_html}
<style>
#{uid} {{ --a:{accent}; --a2:{accent2}; --ink:{ink}; --dim:{dim}; --surf:{surf}; --surf2:{surf2}; --bord:{bord};
  display:block; margin:26px 0; border:1px solid var(--bord); border-radius:16px;
  background:var(--surf); overflow:hidden; outline:none; }}
#{uid}:focus-visible {{ box-shadow:0 0 0 2px var(--a); }}
#{uid} .cn-stage {{ position:relative; min-height:274px; display:grid; }}
#{uid} .cn-scene {{ grid-area:1/1; padding:30px 30px 26px; opacity:0; visibility:hidden;
  transition:opacity .5s ease; display:flex; flex-direction:column; justify-content:center; }}
#{uid} .cn-scene.on {{ opacity:1; visibility:visible; }}
#{uid} .cn-scene.cn-dark {{ background:linear-gradient(160deg,rgba(0,0,0,.30),transparent 70%); }}
#{uid} .cn-scene.cn-warm {{ background:radial-gradient(at 100% 0%, color-mix(in srgb, var(--a) 14%, transparent), transparent 62%); }}
#{uid} .cn-kick {{ color:var(--a); font:700 10.5px/1 ui-sans-serif,system-ui,sans-serif;
  letter-spacing:.2em; text-transform:uppercase; margin-bottom:14px; }}
#{uid} .cn-scene.on .cn-kick {{ animation:{uid}-in .55s cubic-bezier(.22,.61,.36,1) both; }}
#{uid} .cn-title {{ margin:0; color:var(--ink); font:700 clamp(21px,3.4vw,30px)/1.22 ui-sans-serif,system-ui,sans-serif; }}
#{uid} .cn-scene.on .cn-title {{ animation:{uid}-in .7s cubic-bezier(.22,.61,.36,1) .1s both; }}
#{uid} .cn-rule {{ height:2px; width:0; margin-top:16px; background:linear-gradient(90deg,var(--a),transparent); }}
#{uid} .cn-scene.on .cn-rule {{ animation:{uid}-rule 1.1s cubic-bezier(.22,.61,.36,1) .35s both; }}
#{uid} .cn-hook {{ margin:0; color:var(--ink); font:500 clamp(16px,2.5vw,21px)/1.5 ui-serif,Georgia,serif; font-style:italic; }}
#{uid} .cn-scene.on .cn-hook {{ animation:{uid}-in .8s cubic-bezier(.22,.61,.36,1) .12s both; }}
#{uid} .cn-lead {{ margin:0; color:var(--ink); font:450 clamp(14.5px,2vw,17px)/1.62 ui-sans-serif,system-ui,sans-serif; }}
#{uid} .cn-scene.on .cn-lead {{ animation:{uid}-in .7s cubic-bezier(.22,.61,.36,1) .12s both; }}
#{uid} .cn-recall {{ margin:0; color:var(--ink); font:600 clamp(15px,2.2vw,19px)/1.55 ui-sans-serif,system-ui,sans-serif; }}
#{uid} .cn-scene.on .cn-recall {{ animation:{uid}-in .7s cubic-bezier(.22,.61,.36,1) .12s both; }}
#{uid} .cn-facts {{ list-style:none; margin:0; padding:0; display:grid; gap:11px; }}
#{uid} .cn-facts li {{ display:grid; grid-template-columns:24px 1fr; gap:11px; align-items:start;
  color:var(--ink); font:450 14.5px/1.5 ui-sans-serif,system-ui,sans-serif; opacity:0; }}
#{uid} .cn-scene.on .cn-facts li {{ animation:{uid}-in .6s cubic-bezier(.22,.61,.36,1) var(--d) both; }}
#{uid} .cn-num {{ display:grid; place-items:center; width:22px; height:22px; border-radius:50%;
  background:color-mix(in srgb, var(--a) 20%, transparent); color:var(--a);
  font:700 11px/1 ui-sans-serif,system-ui,sans-serif; }}
#{uid} .cn-note {{ margin-top:16px; padding-top:13px; border-top:1px dashed var(--bord);
  color:var(--dim); font:500 12.5px/1.5 ui-sans-serif,system-ui,sans-serif; }}
#{uid} .cn-scene.on .cn-note {{ animation:{uid}-in .6s ease-out .8s both; }}
#{uid} .cn-bar {{ display:flex; align-items:center; gap:9px; padding:11px 16px;
  border-top:1px solid var(--bord); background:var(--surf2); }}
#{uid} .cn-bar button {{ display:grid; place-items:center; width:29px; height:29px; flex:none;
  border-radius:50%; border:1px solid var(--bord); background:transparent; color:var(--ink);
  cursor:pointer; transition:.18s; padding:0; }}
#{uid} .cn-bar button:hover {{ border-color:var(--a); color:var(--a); }}
#{uid} .cn-play {{ background:color-mix(in srgb, var(--a) 18%, transparent); border-color:color-mix(in srgb, var(--a) 45%, transparent); }}
#{uid} .cn-seg {{ display:flex; gap:4px; flex:1; margin:0 5px; }}
#{uid} .cn-seg span {{ flex:1; height:3px; border-radius:2px; background:var(--bord); overflow:hidden; }}
#{uid} .cn-seg i {{ display:block; height:100%; width:0; background:var(--a); }}
#{uid} .cn-count {{ color:var(--dim); font:600 11px/1 ui-sans-serif,system-ui,sans-serif;
  letter-spacing:.05em; flex:none; font-variant-numeric:tabular-nums; }}
#{uid} .cn-video {{ border-top:1px solid var(--bord); }}
#{uid} .cn-video summary {{ padding:12px 16px; cursor:pointer; color:var(--a);
  font:600 12.5px/1 ui-sans-serif,system-ui,sans-serif; }}
#{uid} .cn-vhint {{ color:var(--dim); font-weight:500; }}
#{uid} .cn-vwrap {{ position:relative; padding-bottom:56.25%; height:0; }}
#{uid} .cn-vwrap iframe {{ position:absolute; inset:0; width:100%; height:100%; border:0; }}
@keyframes {uid}-in {{ from {{ opacity:0; transform:translateY(13px); }} to {{ opacity:1; transform:none; }} }}
@keyframes {uid}-rule {{ from {{ width:0; }} to {{ width:118px; }} }}
@media (prefers-reduced-motion: reduce) {{
  #{uid} .cn-scene *, #{uid} .cn-scene {{ animation:none!important; transition:none!important; }}
  #{uid} .cn-facts li {{ opacity:1!important; }}
  #{uid} .cn-rule {{ width:118px; }}
}}
</style>
<script>{js}</script>
</section>"""


def render_daily_media(lesson: dict, theme: dict, dtheme: dict,
                       day_num: int, date_iso: str, video_url: str = "") -> str:
    """Infographic + cinematic block for today's lesson."""
    if not lesson:
        return ""
    return ('<div class="daily-media">'
            + render_infographic(lesson, theme, dtheme, day_num, date_iso)
            + render_cinematic(lesson, theme, dtheme, day_num, date_iso, video_url)
            + '</div>')


def video_url_for(topic_id: str, date_iso: str) -> str:
    """Look up a published narrated-video embed URL, if one exists.

    data/videos.json maps either a topic_id or a YYYY-MM-DD date to an embed
    URL, so the nightly NotebookLM job can register a video without touching
    the curriculum. Missing entries simply render no video.
    """
    try:
        m = json.loads((ROOT / "data" / "videos.json").read_text(encoding="utf-8"))
    except Exception:
        return ""
    return m.get(topic_id) or m.get(date_iso) or ""
