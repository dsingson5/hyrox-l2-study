# -*- coding: utf-8 -*-
"""Bespoke lesson diagrams - batch C."""

import math


def _wrap(did, title, body, caption=""):
    cap = f'<div class="w-hint">{caption}</div>' if caption else ""
    return (f'<div class="widget diagram" id="{did}">'
            f'<div class="w-head"><span class="w-icon">&#9672;</span><span class="w-title">{title}</span></div>'
            f'<div class="w-body">{body}</div>{cap}</div>')


# ---------------------------------------------------------------- primitives

_STYLE = "width:100%;height:auto;max-height:360px;display:block"

_RM = ('<style>@media (prefers-reduced-motion: reduce){'
       '.dg-anim animate,.dg-anim animateMotion,.dg-anim animateTransform{display:none}}'
       '</style>')


def _svg(h, label, body):
    # font-family is pinned: the page font is re-rolled daily and these layouts are
    # measured against a sans stack. fill/stroke defaults are declared so that an
    # undefined colour token can never fall back to the SVG initial black / none.
    return ('<svg viewBox="0 0 700 ' + str(h) + '" preserveAspectRatio="xMidYMid meet" '
            'xmlns="http://www.w3.org/2000/svg" '
            'font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" '
            'font-size="11" fill="var(--text)" stroke="none" '
            'role="img" aria-label="' + label + '" style="' + _STYLE + '">' + body + '</svg>')


def _t(x, y, s, size=11, col="var(--text-dim)", anchor="start", weight="400", extra=""):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" '
            f'text-anchor="{anchor}" font-weight="{weight}"{extra}>{s}</text>')


def _lines(x, y, arr, size=11, col="var(--text-dim)", lh=14, anchor="start", weight="400"):
    ts = "".join(f'<tspan x="{x}" dy="{0 if i == 0 else lh}">{s}</tspan>'
                 for i, s in enumerate(arr))
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{ts}</text>')


def _rect(x, y, w, h, fill="var(--surface-2)", stroke="var(--border)", r=8, op=None, sw=1):
    o = f' fill-opacity="{op}"' if op is not None else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{o} '
            f'stroke="{stroke}" stroke-width="{sw}"/>')


def _line(x1, y1, x2, y2, col="var(--border)", w=1, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" '
            f'stroke-width="{w}" stroke-linecap="round"{d}/>')


def _path(d, col="var(--text-dim)", w=1.6, fill="none", dash="", op=None):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' opacity="{op}"' if op is not None else ""
    return (f'<path d="{d}" fill="{fill}" stroke="{col}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round"{ds}{o}/>')


def _poly(pts, fill="none", stroke="var(--text-dim)", w=1.4, op=None):
    o = f' fill-opacity="{op}"' if op is not None else ""
    p = " ".join(f"{a},{b}" for a, b in pts)
    return f'<polygon points="{p}" fill="{fill}"{o} stroke="{stroke}" stroke-width="{w}"/>'


def _dot(x, y, r, col="var(--theme-accent)", op=None, stroke="none", sw=1):
    o = f' fill-opacity="{op}"' if op is not None else ""
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}"{o} stroke="{stroke}" '
            f'stroke-width="{sw}"/>')


def _head(x, y, dx, dy, size, col):
    m = math.hypot(dx, dy) or 1.0
    ux, uy = dx / m, dy / m
    bx, by = x - size * ux, y - size * uy
    px, py = -uy * size * 0.52, ux * size * 0.52
    return _poly([(round(x, 1), round(y, 1)), (round(bx + px, 1), round(by + py, 1)),
                  (round(bx - px, 1), round(by - py, 1))], col, col, 1)


def _arrow(x1, y1, x2, y2, col="var(--text-dim)", w=1.6, size=8, dash=""):
    m = math.hypot(x2 - x1, y2 - y1) or 1.0
    ux, uy = (x2 - x1) / m, (y2 - y1) / m
    bx, by = x2 - size * ux, y2 - size * uy
    return _line(x1, y1, round(bx, 1), round(by, 1), col, w, dash) + \
        _head(x2, y2, x2 - x1, y2 - y1, size, col)


# ---------------------------------------------------------------- diagrams

def d_hp_see():
    b = [_RM]
    b.append(_t(220, 22, "ALL POSSIBLE TRAINING", 11, "var(--text-dim)", "middle", "600"))
    b.append(_rect(60, 28, 320, 6, "var(--surface-2)", "var(--border)", 3))
    gates = [
        ((60, 62), (380, 62), (344, 116), (96, 116), "var(--good)",
         "1 &#183; SAFETY", "technique before load"),
        ((96, 124), (344, 124), (308, 178), (132, 178), "var(--theme-accent)",
         "2 &#183; EFFICACY", "adaptation, and the standard"),
        ((132, 186), (308, 186), (272, 240), (168, 240), "var(--theme-secondary)",
         "3 &#183; EFFICIENCY", "least time and effort"),
    ]
    for i, (p1, p2, p3, p4, col, name, sub) in enumerate(gates):
        b.append('<g class="dg-anim">' + _poly([p1, p2, p3, p4], col, col, 1.4, 0.13) +
                 '<animate attributeName="stroke-width" values="1.4;3.2;1.4" dur="4.5s" '
                 'begin="' + str(i * 1.1) + 's" repeatCount="indefinite"/></g>')
        b.append(_t(220, p1[1] + 22, name, 13, "var(--text)", "middle", "700"))
        b.append(_t(220, p1[1] + 40, sub, 11, "var(--text-dim)", "middle"))
    b.append(_rect(150, 250, 140, 28, "var(--theme-accent)", "var(--theme-accent)", 6))
    b.append(_t(220, 269, "THE SESSION", 12, "var(--bg)", "middle", "700"))
    # cueing filter
    b.append(_t(400, 44, "Before any cue, ask in this order", 12, "var(--text)", "start", "700"))
    rows = [
        (80, "var(--good)", "1", ["At race effort, is this still the",
                                  "safest way for this athlete to move?"]),
        (142, "var(--theme-accent)", "2", ["Will the change show up where it",
                                           "counts - faster race, cleaner station?"]),
        (204, "var(--theme-secondary)", "3", ["Does it strip out effort or fatigue",
                                       "the athlete does not need to spend?"]),
    ]
    for cy, col, n, txt in rows:
        b.append(_dot(412, cy, 10, col, 0.20, col))
        b.append(_t(412, cy + 4, n, 11, "var(--text)", "middle", "700"))
        b.append(_lines(432, cy - 2, txt))
    b.append(_lines(400, 250, ["A cue that clears none of the three is",
                               "coaching noise - it interrupts and buys nothing."],
                    11, "var(--text-dimmer)"))
    b.append(_rect(20, 290, 660, 44, "var(--bad)", "var(--bad)", 8, 0.10))
    b.append(_lines(34, 308, [
        "Reverse the order and you get the recognisable failures: efficiency first gives fast, sloppy,",
        "injurious reps; efficacy without safety gives a method that works until the athlete breaks."],
        11, "var(--text)"))
    return _wrap("dg-hp_see", "Three pillars, applied in order",
                 _svg(340, "Safety, efficacy and efficiency drawn as three filters in sequence",
                      "".join(b)),
                 "The order is the content: each pillar may only operate inside the space "
                 "the one above it leaves.")


def d_pc_female():
    b = []
    b.append(_t(16, 30, "Three different problems - keep them separate, they need different responses.",
                11, "var(--text-dim)"))
    cols = [
        (16, "var(--theme-accent)", "1 &#183; Sex differences", [
            "Less upper-body lean mass, so the",
            "sled, SkiErg and wall ball sit at a",
            "higher % of maximum - even at the",
            "lighter divisional loads.",
            "",
            "Greater fatigue resistance and more",
            "fat oxidation: suits the long",
            "aerobic middle of the race."],
         "&#8594; train upper body and trunk"),
        (243, "var(--theme-secondary)", "2 &#183; Cycle and contraception", [
            "Group-level phase effects are small,",
            "inconsistent, mostly low quality.",
            "",
            "Individual symptom burden can be",
            "large and real - that is the",
            "actionable signal. Contraception",
            "changes the profile: ask, do not",
            "assume."],
         "&#8594; track and adjust the individual"),
        (470, "var(--bad)", "3 &#183; Low energy availability", [
            "LEA = intake minus exercise cost,",
            "relative to fat-free mass.",
            "",
            "Sustained LEA &#8594; RED-S: bone,",
            "endocrine, immunity, mood, GI,",
            "cardiovascular, performance.",
            "",
            "Not exclusive to women."],
         "&#8594; screen, and refer early"),
    ]
    for x, col, head, body, act in cols:
        b.append(_rect(x, 44, 214, 168))
        b.append(_rect(x, 44, 214, 4, col, col, 2))
        b.append(_t(x + 12, 66, head, 12, "var(--text)", "start", "700"))
        b.append(_lines(x + 12, 86, body))
        b.append(_t(x + 12, 202, act, 11, "var(--text)", "start", "700"))
    b.append(_rect(16, 224, 668, 64, "var(--bad)", "var(--bad)", 8, 0.09))
    b.append(_t(30, 244, "RED FLAGS - refer, do not reassure", 11, "var(--text)", "start", "700"))
    b.append(_lines(30, 262, ["Amenorrhoea in a training athlete",
                              "Menstrual disturbance plus new bone pain"]))
    b.append(_lines(360, 262, ["Unexplained fatigue &#8594; test for iron deficiency",
                               "Pregnancy / postpartum &#8594; clinician-led progression"]))
    b.append(_rect(16, 298, 668, 36))
    b.append(_t(30, 320, "Coaching conduct:", 11, "var(--text)", "start", "700"))
    b.append(_t(144, 320, "no casual body-composition talk, no weigh-ins without "
                          "purpose, no 'lighter is faster'.", 11, "var(--text-dim)"))
    return _wrap("dg-pc_female", "Three things that get wrongly merged",
                 _svg(344, "Sex differences, menstrual cycle and low energy availability as "
                           "three separate coaching problems", "".join(b)),
                 "Sex differences change strategy, the cycle is tracked individually, and low "
                 "energy availability is the one you refer.")


def d_st_sledpull():
    b = [_RM]
    b.append(_rect(16, 20, 330, 76))
    b.append(_t(28, 40, "Force redirection", 12, "var(--text)", "start", "700"))
    b.append(_lines(28, 58, ["The athlete anchors the body and sends force",
                             "through the rope instead of into the sled."]))
    b.append(_rect(356, 20, 328, 76))
    b.append(_t(368, 40, "Lats and trunk start it", 12, "var(--text)", "start", "700"))
    b.append(_lines(368, 58, ["Arms are an extension of the rope, as they are",
                              "an extension of the bar in a deadlift. Breaking",
                              "early at the elbow costs force transfer."]))
    # spine inset
    b.append(_rect(24, 104, 176, 114))
    b.append(_t(36, 122, "Lean back, do not round", 11, "var(--text)", "start", "700"))
    b.append(_line(66, 194, 84, 148, "var(--good)", 3.4))
    b.append(_t(74, 210, "neutral", 11, "var(--good)", "middle"))
    b.append(_path("M136,194 C126,174 138,158 156,150", "var(--bad)", 3.4))
    b.append(_t(150, 210, "shear up", 11, "var(--bad)", "middle"))
    b.append(_lines(24, 240, ["Hip restriction is blamed for low-back load",
                              "and leg lactate at this station."], 11, "var(--text-dimmer)"))
    # scene
    b.append(_line(40, 278, 690, 278, "var(--text-dim)", 1.4))
    b.append(_line(420, 278, 456, 278, "var(--text)", 4))
    b.append(_t(462, 272, "base of support", 11, "var(--text-dimmer)"))
    b.append(_rect(566, 250, 88, 28, "var(--surface-2)", "var(--text-dim)", 4))
    b.append(_dot(590, 264, 5, "var(--text-dim)"))
    b.append(_dot(630, 264, 5, "var(--text-dim)"))
    b.append(_line(470, 214, 566, 250, "var(--text)", 2.6))
    # athlete
    b.append(_line(398, 224, 424, 278, "var(--text)", 3.4))
    b.append(_line(398, 224, 452, 278, "var(--text)", 3.4))
    b.append(_line(398, 224, 376, 178, "var(--text)", 4.6))
    b.append(_line(376, 178, 470, 214, "var(--text)", 3.4))
    b.append(_dot(368, 162, 9, "var(--surface)", None, "var(--text)", 2))
    b.append(_dot(394, 212, 5, "var(--theme-accent)"))
    b.append(_line(394, 212, 394, 278, "var(--text-dim)", 1.2, "4 4"))
    b.append(_t(330, 216, "centre of mass", 11, "var(--text-dim)", "end"))
    b.append(_line(336, 212, 386, 212, "var(--text-dim)", 1, "3 3"))
    b.append('<g class="dg-anim">' + _arrow(440, 290, 372, 290, "var(--theme-accent)", 2.6, 9) +
             '<animate attributeName="opacity" values="0.35;1;0.35" dur="3s" '
             'repeatCount="indefinite"/></g>')
    b.append(_t(406, 304, "backward traction (ground reaction force)", 11,
                "var(--theme-accent)", "middle"))
    # A rope can only pull: the force it applies to the sled points from the sled back
    # toward the athlete, which is also the direction the sled travels.
    b.append('<g class="dg-anim">' + _arrow(552, 245, 486, 220, "var(--theme-accent)", 2.6, 9) +
             '<animate attributeName="opacity" values="0.35;1;0.35" dur="3s" begin="0.5s" '
             'repeatCount="indefinite"/></g>')
    b.append(_t(520, 202, "rope tension pulls the sled in", 11, "var(--theme-accent)"))
    b.append(_t(352, 146, "lats and trunk initiate", 11, "var(--text-dim)", "end"))
    b.append(_line(356, 142, 380, 176, "var(--text-dim)", 1, "3 3"))
    # bottom
    b.append(_rect(16, 310, 330, 46))
    b.append(_lines(28, 328, ["Grip failing is often inhibition from a tight",
                              "shoulder girdle, not forearm weakness."], 11, "var(--text)"))
    b.append(_rect(356, 310, 328, 46))
    b.append(_lines(368, 328, ["Body mass is a real advantage here. Light",
                               "runners must build the posterior chain."], 11, "var(--text)"))
    return _wrap("dg-st_sledpull", "Anchoring the body, redirecting the force",
                 _svg(360, "Side view of the sled pull showing backward traction at the feet, "
                           "force through the rope and the centre of mass behind the base of support",
                      "".join(b)),
                 "Feet make backward traction, the rope carries it - and the lean back only "
                 "works with a spine that stays neutral.")


def d_pd_inseason():
    b = []
    b.append(_rect(16, 20, 272, 270))
    b.append(_t(28, 40, "The in-season loop", 12, "var(--text)", "start", "700"))
    cx, cy, r = 152, 150, 70
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="var(--text-dimmer)" '
             f'stroke-width="1.2" stroke-dasharray="5 5"/>')
    nodes = [(180, "RACE"), (90, "RELOAD"), (0, "MINI-BUILD"), (270, "TAPER")]
    for deg, name in nodes:
        px = cx + r * math.cos(math.radians(deg))
        py = cy - r * math.sin(math.radians(deg))
        b.append(_rect(round(px - 48, 1), round(py - 14, 1), 96, 28,
                       "var(--theme-accent)", "var(--theme-accent)", 6, 0.14))
        b.append(_t(round(px, 1), round(py + 4, 1), name, 11, "var(--text)", "middle", "700"))
    for deg in (135, 45, 315, 225):
        px = cx + r * math.cos(math.radians(deg))
        py = cy - r * math.sin(math.radians(deg))
        b.append(_head(round(px, 1), round(py, 1), math.sin(math.radians(deg)),
                       math.cos(math.radians(deg)), 10, "var(--theme-accent)"))
    b.append(_lines(28, 250, ["Rank races A / B / C. Only A races get a",
                              "full taper and a full reload; B and C are",
                              "trained through."], 11, "var(--text)"))
    # gap decision
    b.append(_rect(300, 20, 384, 202))
    b.append(_t(312, 40, "How big is the gap to the next race?", 12, "var(--text)", "start", "700"))
    gaps = [(52, "var(--bad)", "under 2 weeks", "recover and taper only - no rebuild"),
            (100, "var(--warn)", "2 - 3 weeks", "maintenance plus short sharpening"),
            (148, "var(--good)", "4 weeks or more", "a real rebuild block is possible")]
    for y, col, lab, det in gaps:
        b.append(_rect(312, y, 360, 40))
        b.append(_rect(312, y, 5, 40, col, col, 2))
        b.append(_t(328, y + 17, lab, 12, "var(--text)", "start", "700"))
        b.append(_t(328, y + 32, det, 11, "var(--text-dim)"))
    b.append(_t(312, 208, "Heuristics, not thresholds - recovery varies widely.",
                11, "var(--text-dimmer)"))
    b.append(_rect(300, 232, 384, 58, "var(--theme-accent)", "var(--theme-accent)", 8, 0.10))
    b.append(_t(312, 252, "Maintenance rule", 12, "var(--text)", "start", "700"))
    b.append(_lines(312, 268, ["Hold INTENSITY, cut volume (commonly about 1/3 to 2/3),",
                               "keep frequency - strength and VO2max largely retained."],
                    11, "var(--text)"))
    # recovery clock
    b.append(_rect(16, 298, 668, 56))
    b.append(_t(28, 314, "Recovery clock", 11, "var(--text)", "start", "700"))
    b.append(_t(668, 314, "relative &#8212; no time scale implied", 11, "var(--text-dimmer)", "end"))
    b.append(_t(300, 316, "HR and HRV", 11, "var(--text-dim)", "end"))
    b.append(_rect(310, 307, 110, 11, "var(--good)", "var(--good)", 3, 0.35))
    b.append(_t(300, 336, "muscle damage", 11, "var(--text-dim)", "end"))
    b.append(_rect(310, 327, 290, 11, "var(--bad)", "var(--bad)", 3, 0.30))
    b.append(_t(610, 336, "longer", 11, "var(--text-dimmer)"))
    b.append(_t(28, 350, "Readiness returns before tissue does - do not restart heavy "
                         "volume on HRV alone.", 11, "var(--text)"))
    return _wrap("dg-pd_inseason", "Race block: loop, gap, and the recovery clock",
                 _svg(360, "The reload mini-build taper race loop, a decision on the gap between "
                           "races, and bars showing muscle damage outlasting heart rate recovery",
                      "".join(b)),
                 "The gap decides the block; only A races get the full taper, and soreness "
                 "outlasts the HRV app.")


def d_st_ski():
    b = []
    b.append(_t(20, 16, "Sequence the stroke proximal to distal", 11, "var(--text-dim)"))
    chips = [(20, "1 &#183; LATS"), (176, "2 &#183; TRUNK FLEXORS"),
             (332, "3 &#183; HIP HINGE"), (488, "4 &#183; ARMS FINISH")]
    for i, (x, lab) in enumerate(chips):
        col = "var(--theme-accent)" if i < 3 else "var(--theme-secondary)"
        b.append(_rect(x, 26, 138, 32, col, col, 6, 0.16))
        b.append(_t(x + 69, 46, lab, 11, "var(--text)", "middle", "700"))
        if i < 3:
            b.append(_arrow(x + 141, 42, x + 172, 42, "var(--text-dim)", 1.6, 7))
    b.append(_rect(20, 68, 606, 34, "var(--bad)", "var(--bad)", 6, 0.09))
    b.append(_t(34, 89, "Break at the elbows first and the work goes to biceps and triceps - "
                        "small muscles, quick to fatigue.", 11, "var(--text)"))
    # scene
    b.append(_line(60, 272, 470, 272, "var(--text-dim)", 1.4))
    for px in (206, 456):
        b.append(_line(px, 118, px, 272, "var(--text-dimmer)", 3))
        b.append(_dot(px, 124, 5, "var(--surface)", None, "var(--text-dimmer)"))
    b.append(_line(206, 129, 194, 146, "var(--text-dim)", 1.4))
    b.append(_line(456, 129, 416, 248, "var(--text-dim)", 1.4))
    # start figure - tall and elongated
    b.append(_line(150, 224, 140, 272, "var(--text)", 3.4))
    b.append(_line(150, 224, 162, 272, "var(--text)", 3.4))
    b.append(_line(150, 224, 150, 178, "var(--text)", 4.4))
    b.append(_line(150, 178, 194, 146, "var(--text)", 3.4))
    b.append(_dot(147, 163, 9, "var(--surface)", None, "var(--text)", 2))
    # finish figure - hinged, arms complete
    b.append(_line(402, 226, 392, 272, "var(--text)", 3.4))
    b.append(_line(402, 226, 416, 272, "var(--text)", 3.4))
    b.append(_line(402, 226, 384, 198, "var(--text)", 4.4))
    b.append(_line(384, 198, 416, 248, "var(--text)", 3.4))
    b.append(_dot(376, 184, 9, "var(--surface)", None, "var(--text)", 2))
    b.append(_path("M394,232 Q404,246 418,250", "var(--good)", 1.6, "none", "3 3"))
    b.append(_t(300, 266, "hinge, not squat", 11, "var(--good)", "middle"))
    b.append(_line(348, 262, 390, 240, "var(--good)", 1, "3 3"))
    b.append(_path("M420,240 C356,150 284,148 212,168", "var(--good)", 2))
    b.append(_head(206, 172, -6, 2, 9, "var(--good)"))
    b.append(_t(310, 142, "the return preloads the posterior chain", 11, "var(--good)", "middle"))
    b.append(_t(150, 292, "START: tall, elongated", 11, "var(--text)", "middle", "700"))
    b.append(_t(400, 292, "FINISH: hinged, arms complete", 11, "var(--text)", "middle", "700"))
    # pacing box
    b.append(_rect(490, 112, 194, 174))
    b.append(_t(502, 132, "Station 1: the pacing trap", 12, "var(--text)", "start", "700"))
    b.append(_lines(502, 152, ["Fresh, but heart rate is",
                               "climbing. Establish rhythm",
                               "without spiking it.",
                               "",
                               "Chase POWER PER STROKE,",
                               "not stroke rate - rate is",
                               "the quick route to a",
                               "runaway heart rate.",
                               "",
                               "Start tall for length-tension."]))
    b.append(_rect(20, 300, 330, 38))
    b.append(_t(32, 324, "Neutral neck - flexion overloads the upper traps.", 11, "var(--text)"))
    b.append(_rect(360, 300, 324, 38))
    b.append(_t(372, 324, "Hinge at the hips, not the lumbar spine.", 11, "var(--text)"))
    return _wrap("dg-st_ski", "The stroke, from the inside out",
                 _svg(344, "SkiErg stroke sequence from lats to arms, with start and finish "
                           "positions and the elastic return", "".join(b)),
                 "Big muscles start the stroke, the arms only finish it - and the return is "
                 "a preload, not a rest.")


def d_nu_gut():
    b = []
    # transporters
    b.append(_rect(16, 20, 334, 152))
    b.append(_t(28, 40, "Two doors, two ceilings", 12, "var(--text)", "start", "700"))
    b.append(_rect(34, 52, 300, 32, "var(--theme-accent)", "var(--theme-accent)", 4, 0.10))
    b.append(_rect(34, 84, 300, 26, "var(--surface-2)", "var(--border)", 0))
    b.append(_rect(34, 110, 300, 30, "var(--theme-secondary)", "var(--theme-secondary)", 4, 0.10))
    b.append(_t(42, 72, "LUMEN", 11, "var(--text-dim)"))
    b.append(_t(42, 102, "wall", 11, "var(--text-dim)"))
    b.append(_t(42, 130, "blood", 11, "var(--text-dim)"))
    b.append(_t(120, 72, "glucose", 11, "var(--text)", "middle", "700"))
    b.append(_t(252, 72, "fructose", 11, "var(--text)", "middle", "700"))
    b.append(_arrow(120, 78, 120, 118, "var(--theme-accent)", 2.2, 8))
    b.append(_arrow(252, 78, 252, 118, "var(--good)", 2.2, 8))
    b.append(_t(128, 102, "SGLT1", 11, "var(--theme-accent)", "start", "700"))
    b.append(_t(260, 102, "GLUT5", 11, "var(--good)", "start", "700"))
    b.append(_t(28, 160, "Separate doors are exactly why mixed products work.", 11,
                "var(--text-dim)"))
    # ceiling chart
    b.append(_rect(360, 20, 324, 152))
    b.append(_t(372, 40, "Ceiling on carbohydrate", 12, "var(--text)", "start", "700"))
    b.append(_t(424, 54, "g/h", 11, "var(--text-dimmer)", "end"))
    b.append(_line(430, 56, 430, 140, "var(--text-dim)", 1.2))
    for v in (0, 30, 60, 90):
        y = 140 - v * 0.8
        b.append(_line(430, y, 664, y, "var(--border)", 1, "4 4"))
        b.append(_t(424, y + 4, str(v), 11, "var(--text-dimmer)", "end"))
    b.append(_rect(470, 92, 60, 48, "var(--text-dim)", "var(--text-dim)", 3, 0.28))
    b.append(_t(500, 86, "about 60", 11, "var(--text)", "middle", "700"))
    b.append(_t(500, 156, "glucose only", 11, "var(--text-dim)", "middle"))
    b.append(_rect(576, 68, 60, 72, "var(--theme-accent)", "var(--theme-accent)", 3, 0.30))
    b.append(_t(606, 62, "about 90", 11, "var(--text)", "middle", "700"))
    b.append(_t(606, 156, "plus fructose", 11, "var(--text-dim)", "middle"))
    b.append(_lines(548, 36, ["roughly 2:1 glucose to", "fructose (some 1:0.8)"], 11,
                    "var(--text-dimmer)"))
    # splanchnic
    b.append(_rect(16, 182, 334, 110))
    b.append(_t(28, 202, "Why absorption falls mid-race", 12, "var(--text)", "start", "700"))
    b.append(_rect(34, 214, 100, 32))
    b.append(_t(84, 235, "gut", 11, "var(--text)", "middle", "700"))
    b.append(_rect(216, 214, 118, 32))
    b.append(_t(275, 235, "muscle + skin", 11, "var(--text)", "middle", "700"))
    b.append(_arrow(140, 230, 210, 230, "var(--theme-accent)", 3, 9))
    b.append(_t(175, 222, "blood", 11, "var(--theme-accent)", "middle"))
    b.append(_t(84, 264, "perfusion falls", 11, "var(--bad)", "middle", "700"))
    b.append(_lines(34, 282, ["Worse with high intensity, heat and dehydration."], 11,
                    "var(--text-dim)"))
    # gut training
    b.append(_rect(360, 182, 324, 110))
    b.append(_t(372, 202, "How to train it", 12, "var(--text)", "start", "700"))
    b.append(_line(380, 262, 540, 262, "var(--text-dim)", 1.2))
    for i, h in enumerate((12, 22, 32, 42)):
        x = 386 + i * 38
        b.append(_rect(x, 262 - h, 30, h, "var(--theme-accent)", "var(--theme-accent)", 3, 0.28))
    b.append(_t(460, 276, "weeks", 11, "var(--text-dimmer)", "middle"))
    b.append(_t(374, 232, "g/h", 11, "var(--text-dimmer)", "middle",
                "400", ' transform="rotate(-90 374 232)"'))
    b.append(_lines(548, 216, ["Rehearse the exact",
                               "race-day products,",
                               "concentration and",
                               "timing.",
                               "Some athletes are",
                               "true low absorbers."]))
    b.append(_rect(16, 302, 668, 50))
    b.append(_lines(28, 322, [
        "HYROX twist: jumping, bracing under the sandbag and repeated squat-to-overhead agitate the gut",
        "in ways steady running does not - so rehearse fuelling in station work, not only on runs."],
        11, "var(--text)"))
    return _wrap("dg-nu_gut", "Two transporters, one trainable gut",
                 _svg(360, "Glucose and fructose transporters across the gut wall, the 60 to 90 "
                           "grams per hour ceiling, splanchnic hypoperfusion and a weekly "
                           "progression", "".join(b)),
                 "One pathway caps you near 60 g/h; adding fructose opens a second door - but "
                 "only a rehearsed gut can use it.")


def d_sk_highperf():
    b = []
    b.append(_rect(16, 24, 330, 86, "var(--theme-accent)", "var(--theme-accent)", 8, 0.10))
    b.append(_t(28, 44, "Skill as CAPACITY", 12, "var(--text)", "start", "700"))
    b.append(_lines(28, 62, ["anything with developable range left",
                             "&#8594; never mark a station 'done'; ask how much",
                             "range remains, not whether it passes"], 11, "var(--text)"))
    b.append(_rect(356, 24, 328, 86, "var(--theme-secondary)", "var(--theme-secondary)", 8, 0.10))
    b.append(_t(368, 44, "Skill as EXECUTION", 12, "var(--text)", "start", "700"))
    b.append(_lines(368, 62, ["automatic, on demand, and with intent",
                              "&#8594; the criterion is a clean rep produced",
                              "without deliberation; confidence sits inside"], 11, "var(--text)"))
    b.append(_t(16, 138, "Why running is the highest-leverage skill", 12, "var(--text)",
                "start", "700"))
    b.append(_rect(16, 148, 668, 26, "var(--surface-2)", "var(--border)", 4))
    b.append(_rect(16, 148, 334, 26, "var(--theme-accent)", "var(--theme-accent)", 4, 0.22))
    b.append(_t(183, 165, "8 x 1 km runs - commonly around half of finish time", 11,
                "var(--text)", "middle", "700"))
    b.append(_t(517, 165, "8 stations plus roxzone transitions", 11, "var(--text-dim)", "middle"))
    b.append(_t(16, 188, "A few seconds per kilometre is paid eight times - more than a "
                         "comparable fix on any single station.", 11, "var(--text-dim)"))
    b.append(_rect(16, 198, 384, 140))
    b.append(_t(28, 218, "Limiter drill-down, not more volume", 12, "var(--text)", "start", "700"))
    b.append(_line(34, 230, 34, 310, "var(--theme-accent)", 1.4, "4 4"))
    steps = [(234, "which component actually fails?"),
             (252, "why does that component fail?"),
             (270, "what root constraint produces it?"),
             (288, "fix at the base"),
             (306, "load, volume and intensity LAST")]
    for y, s in steps:
        b.append(_dot(34, y - 4, 4, "var(--theme-accent)"))
        b.append(_t(48, y, s, 11, "var(--text)"))
    b.append(_t(28, 330, "The reflex - pile on daily reps - treats the symptom.", 11, "var(--bad)"))
    b.append(_rect(412, 198, 272, 140))
    b.append(_t(424, 218, "Audit rules", 12, "var(--text)", "start", "700"))
    b.append(_lines(424, 236, ["Order by expected time returned,",
                               "not by how ugly a movement looks.",
                               "",
                               "Rank athletes by developable range,",
                               "not by finish time - the faster",
                               "athlete may have further to go.",
                               "(Practitioner testimony, not evidence.)"]))
    return _wrap("dg-sk_highperf", "Two definitions, one audit",
                 _svg(350, "Capacity and execution definitions of skill, the leverage argument "
                           "for running, and the limiter drill-down sequence", "".join(b)),
                 "Elite practitioner testimony, not evidence: skill is range left plus delivery "
                 "on demand, and running is where the range pays eight times.")


def d_rb_drill_myths():
    b = []
    # correct model
    b.append(_rect(16, 24, 330, 158, "var(--good)", "var(--good)", 8, 0.07))
    b.append(_t(28, 44, "What the ground actually sees", 12, "var(--text)", "start", "700"))
    b.append(_line(30, 146, 336, 146, "var(--text-dim)", 1.4))
    b.append(_dot(110, 88, 10, "none", None, "var(--text-dimmer)"))
    b.append(_dot(210, 88, 10, "var(--theme-accent)", 0.28, "var(--theme-accent)"))
    b.append(_arrow(126, 88, 194, 88, "var(--theme-accent)", 1.8, 8))
    b.append(_t(160, 78, "body travels forward", 11, "var(--theme-accent)", "middle"))
    b.append('<ellipse cx="210" cy="106" rx="9" ry="4" fill="none" stroke="var(--text-dimmer)" '
             'stroke-width="1.2" stroke-dasharray="3 3"/>')
    b.append('<ellipse cx="210" cy="142" rx="9" ry="4" fill="var(--good)" stroke="var(--good)"/>')
    b.append(_arrow(210, 114, 210, 136, "var(--good)", 1.8, 7))
    b.append(_lines(222, 118, ["foot drops", "near-vertically"], 11, "var(--good)"))
    b.append(_lines(28, 162, ["It ends up under the body because the BODY",
                              "moved forward - not because it was pulled back."], 11, "var(--text)"))
    # wrong model
    b.append(_rect(356, 24, 328, 158, "var(--bad)", "var(--bad)", 8, 0.07))
    b.append(_t(368, 44, "The static demo - wrong model", 12, "var(--text)", "start", "700"))
    b.append(_t(368, 60, "(the same explanation ruins the B-skip)", 11, "var(--text-dimmer)"))
    b.append(_line(370, 146, 676, 146, "var(--text-dim)", 1.4))
    b.append(_dot(500, 88, 10, "none", None, "var(--text-dimmer)"))
    b.append('<ellipse cx="600" cy="110" rx="9" ry="4" fill="var(--bad)" stroke="var(--bad)"/>')
    b.append(_t(604, 96, "reach", 11, "var(--bad)", "middle"))
    b.append(_path("M594,116 Q558,144 528,140", "var(--bad)", 2))
    b.append(_head(522, 140, -6, 0, 9, "var(--bad)"))
    b.append(_t(552, 132, "claw", 11, "var(--bad)", "middle"))
    b.append(_lines(368, 162, ["Teaches the foot moving rearward against the",
                               "ground: reach, then claw - overstride and braking."],
                    11, "var(--text)"))
    # wheel cue
    b.append(_rect(16, 192, 330, 148))
    b.append(_t(28, 212, "Rescuing the 'circle' cue", 12, "var(--text)", "start", "700"))
    b.append(_t(28, 228, "touchdown to toe-off to recovery is about HALF a circle", 11,
                "var(--text-dim)"))
    b.append(_dot(92, 250, 6, "var(--theme-accent)", 0.4, "var(--theme-accent)"))
    b.append(f'<circle cx="92" cy="290" r="28" fill="none" stroke="var(--bad)" '
             f'stroke-width="1.6" stroke-dasharray="4 4"/>')
    b.append(_t(104, 254, "as taught", 11, "var(--bad)"))
    b.append(_t(92, 332, "front half needs a reach", 11, "var(--bad)", "middle"))
    b.append(_dot(250, 250, 6, "var(--theme-accent)", 0.4, "var(--theme-accent)"))
    b.append(f'<circle cx="222" cy="290" r="28" fill="none" stroke="var(--good)" '
             f'stroke-width="1.6"/>')
    b.append(_t(262, 254, "rescued", 11, "var(--good)"))
    b.append(_t(250, 332, "behind and beneath", 11, "var(--good)", "middle"))
    b.append(_arrow(300, 292, 334, 292, "var(--text-dimmer)", 1.4, 7))
    b.append(_t(317, 308, "travel", 11, "var(--text-dimmer)", "middle"))
    # discus
    b.append(_rect(356, 192, 328, 148))
    b.append(_t(368, 212, "Running needs vertical impulse too", 12, "var(--text)", "start", "700"))
    b.append(_line(370, 316, 676, 316, "var(--text-dim)", 1.4))
    b.append(_path("M386,316 Q450,296 514,316", "var(--warn)", 1.8))
    b.append(_path("M386,316 Q416,232 452,316", "var(--warn)", 1.8))
    b.append(_path("M386,316 Q520,238 660,316", "var(--theme-accent)", 2.6))
    b.append(_t(518, 310, "flat", 11, "var(--warn)"))
    b.append(_t(456, 306, "too steep", 11, "var(--warn)"))
    b.append(_t(596, 266, "furthest", 11, "var(--theme-accent)", "start", "700"))
    b.append(_t(368, 334, "Minimise vertical movement and you throw it flat.", 11,
                "var(--text)"))
    return _wrap("dg-rb_drill_myths", "The model a drill installs",
                 _svg(350, "Correct near-vertical foot path against the taught pull-back model, "
                           "the rescued wheel cue, and the discus angle analogy for vertical impulse",
                      "".join(b)),
                 "A drill is only as good as its explanation - test the cue on film, not the theory.")


def d_sm_overtraining():
    b = [_RM]
    b.append(_lines(16, 30, [
        "Acute fatigue clears in hours to days. Beyond that the state can only be named in retrospect,",
        "by how long performance stays suppressed:"], 11, "var(--text-dim)", 16))
    b.append(_t(14, 140, "performance", 11, "var(--text-dimmer)", "middle", "400",
                ' transform="rotate(-90 14 140)"'))
    for_d = "M30,150 C64,150 74,186 104,186 C140,186 152,116 200,116"
    panels = [
        (16, "var(--good)", "Functional overreaching", "days to about 2 weeks",
         for_d, 30, 200, "rebounds ABOVE baseline"),
        (243, "var(--warn)", "Non-functional overreaching", "weeks to months",
         "M257,150 C291,150 301,190 331,190 C371,190 391,186 427,186", 257, 427,
         "no rebound, no gain"),
        (470, "var(--bad)", "Overtraining syndrome", "months or longer, rare",
         "M484,150 C518,150 528,196 558,196 C598,196 620,194 654,194", 484, 654,
         "systemic, diagnosis of exclusion"),
    ]
    for x, col, name, sub, d, bx1, bx2, note in panels:
        b.append(_rect(x, 60, 214, 154))
        b.append(_t(x + 107, 78, name, 12, "var(--text)", "middle", "700"))
        b.append(_t(x + 107, 94, sub, 11, "var(--text-dim)", "middle"))
        b.append(_line(bx1, 150, bx2, 150, "var(--text-dimmer)", 1.2, "5 4"))
        b.append(_path(d, col, 2.4))
        b.append(_t(x + 107, 206, note, 11, col, "middle", "700"))
    b.append(_t(36, 144, "baseline", 11, "var(--text-dimmer)"))
    b.append('<g class="dg-anim"><circle r="4.5" fill="var(--good)">'
             '<animateMotion path="' + for_d + '" dur="7s" repeatCount="indefinite"/>'
             '</circle></g>')
    b.append(_t(684, 228, "time &#8594;", 11, "var(--text-dimmer)", "end"))
    b.append(_rect(16, 236, 330, 104))
    b.append(_t(28, 256, "The functional marker: a repeatable test", 12, "var(--text)",
                "start", "700"))
    b.append(_lines(28, 276, ["At FIXED submaximal pace or power:",
                              "heart-rate cost rises, RPE rises.",
                              "At MAXIMAL effort, the opposite:",
                              "HRmax blunted, peak output down,",
                              "peak blood lactate suppressed."], 11, "var(--text)", 15))
    b.append(_rect(356, 236, 328, 104))
    b.append(_t(368, 256, "Before you say overtraining, exclude", 12, "var(--text)",
                "start", "700"))
    b.append(_lines(368, 276, ["iron / ferritin, thyroid, RED-S or low energy",
                               "availability, infection, depression, sleep apnoea.",
                               "",
                               "Monitor 7-day rolling HRV and RHR - never single",
                               "days - plus sleep, mood and session-RPE load."], 11,
                    "var(--text)", 15))
    return _wrap("dg-sm_overtraining", "Named only by how long it lasts",
                 _svg(350, "Performance against time for functional overreaching, non-functional "
                           "overreaching and overtraining syndrome, with the markers and the "
                           "exclusion list", "".join(b)),
                 "Recovery timeline is the discriminator, not how bad it feels today - which is "
                 "why prevention beats diagnosis.")


def d_mp_goals():
    b = []
    b.append(_rect(16, 24, 330, 190))
    b.append(_t(28, 44, "Three tiers of goal", 12, "var(--text)", "start", "700"))
    tiers = [(56, 160, "var(--text-dim)", "OUTCOME", "placing, qualifying"),
             (100, 220, "var(--theme-secondary)", "PERFORMANCE", "your own time, your own splits"),
             (144, 280, "var(--theme-accent)", "PROCESS", "cadence, grip, breath, tempo")]
    for y, w, col, name, sub in tiers:
        b.append(_rect(60, y, w, 36, col, col, 6, 0.16))
        b.append(_t(70, y + 16, name, 11, "var(--text)", "start", "700"))
        b.append(_t(70, y + 30, sub, 11, "var(--text-dim)"))
    b.append(_arrow(42, 60, 42, 176, "var(--text-dim)", 1.4, 8))
    b.append(_t(32, 118, "athlete's control", 11, "var(--text-dimmer)", "middle", "400",
                ' transform="rotate(90 32 118)"'))
    b.append(_lines(28, 196, ["Race day: attention sits on PROCESS. The performance",
                              "goal runs behind it as a pacing reference."], 11, "var(--text)"))
    b.append(_rect(356, 24, 328, 190))
    b.append(_t(368, 44, "Attentional narrowing", 12, "var(--text)", "start", "700"))
    b.append(_poly([(372, 66), (668, 104), (668, 140), (372, 178)],
                   "var(--theme-accent)", "var(--theme-accent)", 1.4, 0.14))
    b.append(_t(386, 126, "many cues available", 11, "var(--text)"))
    b.append(_lines(598, 118, ["only the", "rehearsed"], 11, "var(--text)", 14))
    b.append(_arrow(372, 192, 668, 192, "var(--text-dim)", 1.4, 8))
    b.append(_t(520, 206, "arousal and fatigue rise", 11, "var(--text-dimmer)", "middle"))
    b.append(_rect(16, 224, 330, 116))
    b.append(_t(28, 244, "Self-efficacy sources, descending", 12, "var(--text)", "start", "700"))
    srcs = [(262, "1 mastery experience", 150), (282, "2 vicarious (modelling)", 112),
            (302, "3 verbal persuasion", 74), (322, "4 how the body feels", 44)]
    for y, lab, w in srcs:
        b.append(_t(28, y, lab, 11, "var(--text)"))
        b.append(_rect(180, y - 9, w, 10, "var(--theme-accent)", "var(--theme-accent)", 3, 0.35))
    b.append(_rect(356, 224, 328, 116))
    b.append(_t(368, 244, "Delivery vehicles", 12, "var(--text)", "start", "700"))
    b.append(_lines(368, 262, ["IMAGERY (PETTLEP): multisensory, real time,",
                               "rehearse coping - not only perfect runs.",
                               "INSTRUCTIONAL self-talk &#8594; technique.",
                               "MOTIVATIONAL self-talk &#8594; sustained effort.",
                               "Routine: breath + cue word + first-action image."],
                    11, "var(--text)", 15))
    return _wrap("dg-mp_goals", "Goals, control and the shrinking cue window",
                 _svg(350, "Outcome, performance and process goals ranked by control, a funnel "
                           "showing attentional narrowing, and the sources of self-efficacy",
                      "".join(b)),
                 "Only process goals can be executed mid-race - and they are all that survives "
                 "the narrowing.")


def d_pc_masters():
    b = []
    xs = lambda v: round(210 + v * 30, 1)
    for v in (0, 5, 10, 15):
        b.append(_line(xs(v), 44, xs(v), 232, "var(--border)", 1, "4 4"))
        b.append(_t(xs(v), 256, str(v) + "%", 11, "var(--text-dimmer)", "middle"))
    b.append(_t(20, 40, "VO2max decline per decade", 12, "var(--text)", "start", "700"))
    rows = [(60, "well-trained masters, under 50", 2, 3, "var(--good)", "2-3%"),
            (84, "highly trained", 3, 5, "var(--good)", "3-5%"),
            (108, "active", 5, 7, "var(--warn)", "5-7%"),
            (132, "sedentary", None, 10, "var(--bad)", "about 10%")]
    for c, lab, lo, hi, col, val in rows:
        b.append(_t(200, c + 4, lab, 11, "var(--text-dim)", "end"))
        if lo is None:
            x = xs(hi)
            b.append(_poly([(x, c - 8), (x + 8, c), (x, c + 8), (x - 8, c)], col, col, 1.2, 0.55))
            b.append(_t(x + 14, c + 4, val, 11, "var(--text)", "start", "700"))
        else:
            b.append(_rect(xs(lo), c - 7, xs(hi) - xs(lo), 14, col, col, 3, 0.35))
            b.append(_t(xs(hi) + 8, c + 4, val, 11, "var(--text)", "start", "700"))
    b.append(_t(20, 156, "VO2max decline accelerates after about 50.", 11, "var(--text-dimmer)"))
    b.append(_line(20, 163, 680, 163, "var(--border)", 1))
    b.append(_t(20, 178, "Maximal strength decline per decade", 12, "var(--text)", "start", "700"))
    srows = [(196, "training consistently", 5, 10, "var(--warn)", "5-10%"),
             (220, "sedentary, after 30", 10, 15, "var(--bad)", "10-15%")]
    for c, lab, lo, hi, col, val in srows:
        b.append(_t(200, c + 4, lab, 11, "var(--text-dim)", "end"))
        b.append(_rect(xs(lo), c - 7, xs(hi) - xs(lo), 14, col, col, 3, 0.35))
        b.append(_t(xs(hi) - 8, c + 4, val, 11, "var(--text)", "end", "700"))
    b.append(_t(410, 238, "after 60, up to about 30% per decade", 11, "var(--bad)", "start"))
    b.append(_arrow(614, 234, 664, 234, "var(--bad)", 1.6, 8))
    b.append(_rect(16, 266, 330, 90))
    b.append(_t(28, 286, "Ages fastest to slowest", 12, "var(--text)", "start", "700"))
    ladder = [(304, "var(--bad)", "sprint and explosive power - falls first"),
              (320, "var(--warn)", "tendon stiffness - but trainable"),
              (336, "var(--warn)", "VO2max - central: max cardiac output"),
              (352, "var(--good)", "economy and thresholds - preserved")]
    for y, col, lab in ladder:
        b.append(_dot(32, y - 4, 4, col))
        b.append(_t(44, y, lab, 11, "var(--text)"))
    b.append(_rect(356, 266, 328, 90))
    b.append(_t(368, 286, "Programming", 12, "var(--text)", "start", "700"))
    b.append(_lines(368, 302, ["Maintain INTENSITY, not just volume - much of",
                               "the measured decline reflects athletes easing",
                               "off. Buy the hard sessions with more recovery",
                               "days rather than deleting intensity. Strength",
                               "and plyometric work defend tendon stiffness."], 11,
                    "var(--text)", 13))
    return _wrap("dg-pc_masters", "What ages, and how fast",
                 _svg(360, "Range bars for VO2max and strength decline per decade by activity "
                           "level, plus the order in which qualities age", "".join(b)),
                 "Explosive qualities go first and economy holds - so the masters answer is more "
                 "recovery, never less intensity.")


def d_cm_philosophy():
    b = []
    chain = [(16, "VALUES"), (196, "PRIORITIES"), (376, "DECISION RULES")]
    for i, (x, lab) in enumerate(chain):
        b.append(_rect(x, 20, 160, 34, "var(--theme-accent)", "var(--theme-accent)", 6, 0.16))
        b.append(_t(x + 80, 42, lab, 11, "var(--text)", "middle", "700"))
        if i < 2:
            b.append(_arrow(x + 163, 37, x + 192, 37, "var(--text-dim)", 1.6, 7))
    b.append(_lines(552, 30, ["written down, or it", "collapses under", "race-week pressure"],
                    11, "var(--text-dim)", 13))
    b.append(_line(350, 74, 350, 244, "var(--text-dim)", 1.6, "6 5"))
    b.append(_rect(16, 74, 320, 118, "var(--good)", "var(--good)", 8, 0.08))
    b.append(_t(28, 94, "IN SCOPE", 12, "var(--text)", "start", "700"))
    b.append(_lines(28, 112, ["training design and technique coaching",
                              "load management and monitoring",
                              "general nutrition, hydration, sleep education",
                              "motivation and accountability"], 11, "var(--text)", 16))
    b.append(_rect(364, 74, 320, 118, "var(--bad)", "var(--bad)", 8, 0.08))
    b.append(_t(376, 94, "OUT OF SCOPE - refer", 12, "var(--text)", "start", "700"))
    b.append(_lines(376, 112, ["diagnosing injury or illness",
                               "rehabilitation prescription",
                               "individualised medical nutrition therapy",
                               "supplement or drug advice, psychotherapy"], 11, "var(--text)", 16))
    b.append(_arrow(300, 210, 400, 210, "var(--bad)", 2, 9))
    b.append(_t(350, 202, "REFER", 11, "var(--bad)", "middle", "700"))
    b.append(_arrow(400, 232, 300, 232, "var(--good)", 2, 9))
    b.append(_t(350, 246, "keep coaching what is safe and pain-free", 11, "var(--good)", "middle"))
    b.append(_t(16, 268, "Athlete-centred is not athlete-led: athlete owns the goal; coach "
                         "owns the method and the veto on unsafe work.", 11, "var(--text)"))
    b.append(_rect(16, 278, 330, 76))
    b.append(_t(28, 296, "Refer out on", 12, "var(--text)", "start", "700"))
    b.append(_lines(28, 314, ["red-flag pain, or pain unresolved after about",
                              "2-3 weeks; neurological symptoms; chest pain or",
                              "syncope; RED-S or disordered eating; distress."],
                    11, "var(--text-dim)", 14))
    b.append(_rect(356, 278, 328, 76))
    b.append(_t(368, 296, "Duty of care", 12, "var(--text)", "start", "700"))
    b.append(_lines(368, 314, ["screening (PAR-Q+ screens, it does not clear),",
                               "informed consent, safe kit and sled surface, an",
                               "emergency action plan, confidentiality."],
                    11, "var(--text-dim)", 14))
    return _wrap("dg-cm_philosophy", "The line, and what crosses it",
                 _svg(360, "A coaching philosophy chain and the scope-of-practice boundary with "
                           "referral crossing it in one direction and continued coaching in the other",
                      "".join(b)),
                 "Refer, do not abandon: everything past the line goes out, and the safe, "
                 "pain-free work stays with you.")


def d_xs_sportsmed():
    b = []
    b.append(_rect(16, 24, 214, 216))
    b.append(_t(28, 44, "Niggle triage", 12, "var(--text)", "start", "700"))
    lights = [(56, "var(--good)", "GREEN", ["no pain", "train normally"]),
              (116, "var(--warn)", "AMBER", ["pain up to about 3/10 that",
                                             "settles within 24 h: modify"]),
              (176, "var(--bad)", "RED", ["above that, worsening, or",
                                          "changing mechanics: refer"])]
    for y, col, lab, txt in lights:
        b.append(_rect(28, y, 190, 52))
        b.append(_rect(28, y, 5, 52, col, col, 2))
        b.append(_t(44, y + 18, lab, 11, "var(--text)", "start", "700"))
        b.append(_lines(44, y + 34, txt, 11, "var(--text-dim)", 14))
    b.append(_rect(242, 24, 214, 216))
    b.append(_t(254, 44, "Classify by timescale", 12, "var(--text)", "start", "700"))
    b.append(_line(266, 66, 266, 218, "var(--text-dim)", 1.4))
    marks = [(84, "var(--good)", "FOR", ["days to about 2 weeks,",
                                         "rebounds with supercompensation"]),
             (136, "var(--warn)", "NFOR", ["weeks to months,", "no rebound and no gain"]),
             (188, "var(--bad)", "OTS", ["months or longer, rare,",
                                         "a diagnosis of exclusion"])]
    for y, col, lab, txt in marks:
        b.append(_dot(266, y - 4, 5, col))
        b.append(_t(280, y, lab, 11, "var(--text)", "start", "700"))
        b.append(_lines(280, y + 15, txt, 11, "var(--text-dim)", 13))
    b.append(_t(254, 234, "soreness is not a marker", 11, "var(--warn)"))
    b.append(_rect(468, 24, 216, 216))
    b.append(_t(480, 42, "Return: load before speed", 12, "var(--text)", "start", "700"))
    rungs = [(194, "var(--good)", "1 range and pain-free"), (148, "var(--theme-accent)", "2 load"),
             (102, "var(--theme-accent)", "3 speed, plyo, impact"),
             (56, "var(--theme-secondary)", "4 race-specific density")]
    for y, col, lab in rungs:
        b.append(_rect(490, y, 182, 32, col, col, 6, 0.16))
        b.append(_t(502, y + 21, lab, 11, "var(--text)", "start", "700"))
    b.append(_arrow(478, 222, 478, 52, "var(--text-dim)", 1.6, 8))
    b.append(_rect(16, 252, 390, 90))
    b.append(_t(28, 272, "Tools answer different questions", 12, "var(--text)", "start", "700"))
    b.append(_lines(28, 290, ["sRPE = RPE (0-10) x minutes &#8594; internal load in AU",
                              "HRV and RHR &#8594; autonomic status, noisy day to day",
                              "wellness questionnaire &#8594; often shifts earliest",
                              "ACWR = 7-day / 28-day: contested, one signal only"],
                    11, "var(--text)", 14))
    b.append(_rect(416, 252, 268, 90))
    b.append(_t(428, 272, "Recovery", 12, "var(--text)", "start", "700"))
    b.append(_lines(428, 290, ["Sleep has the most consistent",
                               "evidence. Cold water after",
                               "lifting may blunt strength and",
                               "hypertrophy adaptations."], 11, "var(--text)", 14))
    return _wrap("dg-xs_sportsmed", "Monitor, modify, or refer",
                 _svg(350, "Traffic-light niggle triage, the overreaching continuum classified by "
                           "timescale, and the return-to-training ladder", "".join(b)),
                 "Most HYROX injuries are load errors, not dangerous movements - so classify by "
                 "timescale, then monitor, modify or refer.")


DIAGRAMS = {
    "hp_see": d_hp_see,
    "pc_female": d_pc_female,
    "st_sledpull": d_st_sledpull,
    "pd_inseason": d_pd_inseason,
    "st_ski": d_st_ski,
    "nu_gut": d_nu_gut,
    "sk_highperf": d_sk_highperf,
    "rb_drill_myths": d_rb_drill_myths,
    "sm_overtraining": d_sm_overtraining,
    "mp_goals": d_mp_goals,
    "pc_masters": d_pc_masters,
    "cm_philosophy": d_cm_philosophy,
    "xs_sportsmed": d_xs_sportsmed,
}
