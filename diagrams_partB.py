# -*- coding: utf-8 -*-
"""Bespoke lesson diagrams - batch B."""

import math


def _wrap(did, title, body, caption=""):
    cap = f'<div class="w-hint">{caption}</div>' if caption else ""
    return (f'<div class="widget diagram" id="{did}">'
            f'<div class="w-head"><span class="w-icon">&#9672;</span><span class="w-title">{title}</span></div>'
            f'<div class="w-body">{body}</div>{cap}</div>')


# ---------------------------------------------------------------- helpers

def _open(tid, vy, vh, label):
    """Open a figure.

    `vy`/`vh` are the viewBox window, not the authored coordinate space: the
    drawings are authored on a 700-wide canvas and the window is cropped to the
    ink so the rendered height stays inside the 360px budget. That keeps every
    11-unit label at >= 11 CSS px instead of being scaled down by `max-height`.
    `font-family` is pinned because the page font is re-rolled daily and the
    layouts are measured against a sans stack.
    """
    return ('<svg id="%s-fig" viewBox="0 %s 700 %s" preserveAspectRatio="xMidYMid meet" '
            'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s" '
            'font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" '
            'font-size="11" fill="var(--text)" stroke="none" '
            'style="width:100%%;height:auto;max-height:360px">' % (tid, vy, vh, label))

DIM = "var(--text-dim)"
DIMMER = "var(--text-dimmer)"
TXT = "var(--text)"
ACC = "var(--theme-accent)"


def _t(x, y, s, size=11, fill=DIM, anchor="start", weight="normal"):
    return ('<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="%s" font-weight="%s">%s</text>'
            % (x, y, size, fill, anchor, weight, s))


def _stack(x, y, lines, dy=14, size=11, fill=DIM, anchor="start"):
    return "".join(_t(x, y + i * dy, s, size, fill, anchor) for i, s in enumerate(lines))


def _panel(x, y, w, h, fill="var(--surface)", stroke="var(--border)", op=1.0, r=8):
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" fill-opacity="%s" '
            'stroke="%s" stroke-width="1"/>' % (x, y, w, h, r, fill, op, stroke))


def _box(x, y, w, h, op=0.14, stroke=ACC, r=6, fill=ACC):
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" fill-opacity="%s" '
            'stroke="%s" stroke-opacity="0.55" stroke-width="1"/>' % (x, y, w, h, r, fill, op, stroke))


def _line(x1, y1, x2, y2, stroke=DIM, w=1, dash=None, op=1.0):
    d = ' stroke-dasharray="%s"' % dash if dash else ''
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'stroke-opacity="%s" stroke-linecap="round"%s/>' % (x1, y1, x2, y2, stroke, w, op, d))


def _arrow(x1, y1, x2, y2, stroke=DIM, w=1.4, head=7.0, dash=None):
    ang = math.atan2(y2 - y1, x2 - x1)
    bx = x2 - head * math.cos(ang)
    by = y2 - head * math.sin(ang)
    l = math.radians(25)
    p1x = x2 - head * 1.15 * math.cos(ang - l)
    p1y = y2 - head * 1.15 * math.sin(ang - l)
    p2x = x2 - head * 1.15 * math.cos(ang + l)
    p2y = y2 - head * 1.15 * math.sin(ang + l)
    d = ' stroke-dasharray="%s"' % dash if dash else ''
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" '
            'stroke-linecap="round"%s/>'
            '<path d="M %.1f %.1f L %.1f %.1f L %.1f %.1f Z" fill="%s"/>'
            % (x1, y1, bx, by, stroke, w, d, x2, y2, p1x, p1y, p2x, p2y, stroke))


# Reduced-motion guard. Disables the animation only, never the static geometry
# inside the animated group - the same rule the other modules use.
_RM = ('<style>@media (prefers-reduced-motion: reduce){'
       '.dg-anim animate,.dg-anim animateMotion,.dg-anim animateTransform{display:none}}'
       '</style>')


# ---------------------------------------------------------------- 116 sk_categories

def d_sk_categories():
    s = [_open("sk_categories", 22, 336,
           "Three categories of racing skill as cards, a cascade arrow running between them, "
           "and two bars comparing the attention a still-cognitive skill costs with an automatic one"),
         _RM]

    cards = [
        (20, "1 &#183; STANDARDS &amp; ECONOMY",
         ["Reps that still satisfy the",
          "rulebook under fatigue, judging",
          "and pressure &#8212; and the same work",
          "for the least energy wasted.",
          "A no-rep spends the energy and",
          "earns nothing.",
          "TRAIN: drills, mobility, technique",
          "under fatigue, video review."]),
        (246, "2 &#183; PACING INTENSITY",
         ["Regulate effort segment by",
          "segment from your thresholds and",
          "each station's energy price.",
          "Fails BOTH ways: too hot pays at",
          "the sled push, too cautious leaves",
          "capacity unspent at the line.",
          "TRAIN: race-pace intervals,",
          "simulations with biofeedback."]),
        (472, "3 &#183; DECISION MAKING",
         ["Push or recover, station entry,",
          "planned rep breaks, roxzone and",
          "transitions, race positioning,",
          "reacting to competitors, no-reps",
          "and equipment trouble &#8212; all done",
          "heavily fatigued.",
          "TRAIN: simulations and scenarios;",
          "a choice needs a context with it."]),
    ]
    for x, head, lines in cards:
        s.append(_box(x, 24, 208, 172, op=0.10))
        s.append(_t(x + 12, 44, head, 12, TXT, weight="600"))
        s.append(_line(x + 12, 52, x + 196, 52, ACC, 1, op=0.45))
        s.append(_stack(x + 12, 68, lines, 14, 11, DIM))

    # forward cascade
    s.append(_arrow(60, 224, 640, 224, ACC, 2.0, 9))
    s.append(_t(350, 216, "CASCADE &#8212; an economy leak raises cost per rep, which breaks the pacing "
                          "budget, which delivers", 11, DIM, "middle"))
    s.append(_t(350, 240, "the athlete to their decisions earlier and in a worse state.", 11, DIM, "middle"))
    s.append('<g class="dg-anim">'
             '<circle r="4" fill="%s"><animateMotion dur="6s" repeatCount="1" fill="freeze" '
             'path="M 60 224 L 640 224"/></circle></g>' % ACC)
    s.append(_arrow(640, 258, 60, 258, "var(--good)", 1.4, 7, "5 4"))
    s.append(_t(350, 274, "In reverse: disciplined pacing protects the fatigue state in which standards hold "
                          "and decisions stay sharp.", 11, DIM, "middle"))

    # attention budget
    s.append(_t(20, 300, "ATTENTION BUDGET (day 27) &#8212; shaded = attention spent on the movement itself",
                11, TXT, weight="600"))
    s.append(_t(20, 324, "still cognitive", 11, DIM))
    s.append(_panel(150, 312, 330, 16, "var(--surface-2)", "var(--border)"))
    s.append('<rect x="150" y="312" width="270" height="16" rx="4" fill="%s" fill-opacity="0.55"/>' % ACC)
    s.append(_t(690, 324, "little left for pacing or tactics", 11, DIM, "end"))
    s.append(_t(20, 352, "automatic", 11, DIM))
    s.append(_panel(150, 340, 330, 16, "var(--surface-2)", "var(--border)"))
    s.append('<rect x="150" y="340" width="100" height="16" rx="4" fill="%s" fill-opacity="0.55"/>' % ACC)
    s.append(_t(690, 352, "bandwidth free for 2 and 3", 11, DIM, "end"))
    s.append("</svg>")

    return _wrap("dg-sk_categories", "Three categories of racing skill",
                 "".join(s),
                 "Overlearning technique is not only category-one work: it frees the attention that pacing "
                 "and decision making consume.")


# ---------------------------------------------------------------- 120 rb_treadmills

def d_rb_treadmills():
    s = [_open("rb_treadmills", 18, 354,
           "Outdoors, flat motorised belt and curved non-motorised treadmill compared row by row "
           "on energy cost, mechanics, tissue bias and best use")]
    cx = [219, 411, 601]

    # venue icons
    s.append('<path d="M 160 44 L 185 38 L 210 46 L 235 36 L 260 44" fill="none" stroke="%s" '
             'stroke-width="2" stroke-linejoin="round"/>' % ACC)
    s.append('<rect x="352" y="36" width="120" height="9" rx="4" fill="%s" fill-opacity="0.5"/>' % ACC)
    s.append(_line(360, 36, 360, 20, DIM, 1.4))
    s.append('<path d="M 542 46 C 578 46 606 34 632 20" fill="none" stroke="%s" stroke-width="3" '
             'stroke-linecap="round"/>' % ACC)
    for i, name in enumerate(["OUTDOORS", "FLAT MOTORISED", "CURVED NON-MOTORISED"]):
        s.append(_t(cx[i], 64, name, 12, TXT, "middle", "600"))
    s.append(_line(10, 74, 690, 74, "var(--border)", 1))

    # cost row
    s.append(_stack(10, 100, ["COST AT", "MATCHED PACE"], 14, 11, TXT))
    s.append(_line(128, 150, 690, 150, "var(--border)", 1))
    for i, (h, lab) in enumerate([(36, "&#8776; equal"), (36, "&#8776; equal"), (56, "HIGHER")]):
        s.append('<rect x="%d" y="%d" width="54" height="%d" rx="3" fill="%s" fill-opacity="%s" '
                 'stroke="%s" stroke-opacity="0.6"/>'
                 % (cx[i] - 27, 150 - h, h, ACC, 0.5 if i < 2 else 0.85, ACC))
        s.append(_t(cx[i], 142 - h, lab, 11, TXT, "middle", "600"))
    s.append(_stack(cx[0], 166, ["flat, windless overground;",
                                 "wind, gradients, bends and uneven",
                                 "ground add stabiliser work"], 14, 11, DIM, "middle"))
    s.append(_stack(cx[1], 166, ["a level belt costs about the same;",
                                 "the 1-2% incline only earns its keep",
                                 "faster than &#8776; 4:21/km (7:00/mile)"], 14, 11, DIM, "middle"))
    s.append(_stack(cx[2], 166, ["&#8593; heart rate, &#8593; oxygen, &#8593; carbohydrate",
                                 "(Morrow 2022; Bruseghini 2019;",
                                 "Edwards 2017) &#8212; hardest of three"], 14, 11, DIM, "middle"))
    s.append(_line(10, 204, 690, 204, "var(--border)", 1))

    s.append(_stack(10, 224, ["MECHANICS", "vs OVERGROUND"], 14, 11, TXT))
    s.append(_stack(cx[0], 224, ["the reference pattern"], 14, 11, DIM, "middle"))
    s.append(_stack(cx[1], 224, ["close &#8212; the belt draws the foot back,",
                                 "the elastic bounce is the same"], 14, 11, DIM, "middle"))
    s.append(_stack(cx[2], 224, ["FURTHEST from overground",
                                 "(Catala-Vilaplana 2023)"], 14, 11, DIM, "middle"))
    s.append(_line(10, 250, 690, 250, "var(--border)", 1))

    s.append(_stack(10, 270, ["TISSUE BIAS", "&amp; REHAB"], 14, 11, TXT))
    s.append(_stack(cx[0], 270, ["varied surfaces distribute load;",
                                 "prefer after calf or Achilles trouble"], 14, 11, DIM, "middle"))
    s.append(_stack(cx[1], 270, ["hamstring activation lower &#8594; use for",
                                 "hamstring return; the ankle works harder"], 14, 11, DIM, "middle"))
    s.append(_stack(cx[2], 270, ["permanent uphill &#8594; below-knee load,",
                                 "plus the toe-tapping fault"], 14, 11, DIM, "middle"))
    s.append(_line(10, 296, 690, 296, "var(--border)", 1))

    s.append(_stack(10, 316, ["BEST USE"], 14, 11, TXT))
    s.append(_stack(cx[0], 316, ["race-like: flat and hard &#8212;",
                                 "plus variety to spread load"], 14, 11, DIM, "middle"))
    s.append(_stack(cx[1], 316, ["race-like and precisely dosed;",
                                 "uphill dosing spares the knee"], 14, 11, DIM, "middle"))
    s.append(_stack(cx[2], 316, ["sprints and acceleration, fast HR",
                                 "drive, cadence &#8212; never race pace"], 14, 11, DIM, "middle"))

    s.append(_t(350, 350, "HYROX is run on flat, hard exhibition-hall floors, so flat overground and the flat "
                          "motorised belt are the race-like venues &#8212;", 11, TXT, "middle"))
    s.append(_t(350, 366, "but any run beats a missed one, and the race skill is running on station-loaded legs "
                          "wherever it is practised.", 11, DIM, "middle"))
    s.append("</svg>")

    return _wrap("dg-rb_treadmills", "Three running venues, sorted by physics",
                 "".join(s),
                 "The curved mill is a permanent hill, not a more natural belt: hardest of the three and "
                 "furthest from overground mechanics.")


# ---------------------------------------------------------------- 119 pd_doublepeak

# Volume against a zero at y=250 and a peak-week plateau at y=128, so the depth of
# each taper is readable: taper 2 bottoms at y=201, i.e. ~40% of peak-week volume
# (the lesson's "cut by up to about 60%"). Taper 1 is only drawn shallower than it -
# the lesson gives it no percentage, so no percentage is implied.
VOL_PATH = ("M 60 130 L 240 128 L 300 182 L 340 188 L 470 126 L 560 201 L 660 196")


def d_pd_doublepeak():
    s = [_open("pd_doublepeak", 36, 330,
           "Training volume across one macrocycle with two races: a short first taper before the "
           "qualifier, a rebuild, then a deeper second taper before the championship"),
         _RM]

    # peak-form windows
    # Peak form holds ~1-3 wk, i.e. roughly twice the <=7 d TAPER 1 bracket below.
    for x0, w in [(240, 120), (500, 120)]:
        s.append('<rect x="%d" y="86" width="%d" height="164" fill="%s" fill-opacity="0.16"/>'
                 % (x0, w, ACC))
    s.append(_line(60, 250, 675, 250, "var(--border)", 1))
    s.append(_line(60, 86, 60, 250, "var(--border)", 1))
    s.append(_line(64, 201, 675, 201, DIMMER, 1, "3 4"))
    s.append(_t(20, 96, "LOAD", 11, DIMMER))
    s.append(_t(54, 132, "peak wk", 11, DIMMER, "end"))
    s.append(_t(54, 205, "40%", 11, DIMMER, "end"))
    s.append(_t(54, 254, "0", 11, DIMMER, "end"))

    # curves
    s.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-linejoin="round" '
             'stroke-linecap="round"/>' % (VOL_PATH, ACC))
    s.append(_line(60, 168, 598, 168, "var(--good)", 2, "6 5"))
    s.append(_t(606, 172, "intensity", 11, "var(--good)"))
    s.append(_t(606, 132, "volume", 11, ACC))
    s.append('<g class="dg-anim"><circle r="4.5" fill="%s">'
             '<animateMotion dur="9s" repeatCount="indefinite" path="%s"/></circle></g>'
             % (ACC, VOL_PATH))

    # race markers
    for x, name, sub in [(300, "QUALIFIER", "peak 1"), (560, "CHAMPIONSHIP", "peak 2")]:
        s.append(_line(x, 250, x, 76, TXT, 1.4, "4 3"))
        s.append('<path d="M %d 76 L %d 68 L %d 76 Z" fill="%s"/>' % (x - 7, x, x + 7, TXT))
        s.append(_t(x, 62, name, 11, TXT, "middle", "600"))
        s.append(_t(x, 48, sub + " &#183; peak form holds &#8776;1-3 wk", 11, DIMMER, "middle"))

    # phase brackets
    for x0, x1, lab in [(60, 240, "BUILD"), (240, 300, "TAPER 1 &#8804;7 d"),
                        (300, 470, "REBUILD &#8212; several weeks"), (470, 560, "TAPER 2 &#8212; 10-14 d")]:
        s.append(_line(x0 + 3, 258, x1 - 3, 258, DIM, 1))
        s.append(_line(x0 + 3, 254, x0 + 3, 262, DIM, 1))
        s.append(_line(x1 - 3, 254, x1 - 3, 262, DIM, 1))
        s.append(_t((x0 + x1) / 2, 274, lab, 11, TXT, "middle"))

    s.append(_stack(20, 300, [
        "TAPER 1 (&#8804;7 d): intensity high, volume trimmed &#8212; a qualifier needs a good day, not the "
        "season's best.",
        "REBUILD: restore density at a rate a just-raced body can absorb &#8212; too slow reads as detraining, "
        "too fast buries tissue.",
        "TAPER 2 (10-14 d): volume cut by up to &#8776;60%, intensity fully retained (Mujika &amp; Padilla 2003; "
        "Bosquet 2007).",
        "Supercompensation peaks after &#8776;7-14 days of reduced load; peak form then holds only "
        "&#8776;1-3 weeks (Le Meur 2012).",
    ], 15, 11, DIM))
    s.append(_t(20, 360, "RISK: over-tapering across both peaks removes weeks of training density &#8212; blunted "
                         "aerobic gains, eroded strength endurance.", 11, "var(--bad)"))
    s.append("</svg>")

    return _wrap("dg-pd_doublepeak", "Two peaks in one macrocycle",
                 "".join(s),
                 "The tapers are deliberately asymmetric: a short one to earn the start, a full one to use it.")


# ---------------------------------------------------------------- 43 pd_taper

def d_pd_taper():
    s = [_open("pd_taper", 31, 346,
           "Three bars showing weekly volume falling from the peak week to race week while a "
           "dashed intensity line holds, beside a race-week countdown timeline")]

    s.append(_line(70, 180, 370, 180, "var(--border)", 1))
    s.append(_stack(18, 56, ["weekly", "volume"], 14, 11, DIMMER))
    bars = [(90, 130, "100%", "PEAK WK"), (185, 85, "60-70%", "TAPER WK 1"), (280, 58, "40-50%", "RACE WK")]
    for x, h, val, name in bars:
        s.append('<rect x="%d" y="%d" width="70" height="%d" rx="4" fill="%s" fill-opacity="0.22" '
                 'stroke="%s" stroke-opacity="0.7"/>' % (x, 180 - h, h, ACC, ACC))
        s.append(_t(x + 35, 174 - h, val, 12, TXT, "middle", "600"))
        s.append(_t(x + 35, 196, name, 11, DIM, "middle"))
    s.append(_line(80, 140, 360, 140, "var(--good)", 1.8, "6 4"))
    s.append(_t(220, 218, "dashed line = INTENSITY, unchanged across all three weeks", 11, "var(--good)", "middle"))

    s.append(_stack(392, 62, [
        "VOLUME &#8595; 40-60% from the peak week, progressively",
        "INTENSITY held &#8212; the last thing to cut, not the first",
        "FREQUENCY held at &#8776;80%+ of normal (feel and skill)",
        "Duration 7-21 d; &#8776;2 weeks suits most trained athletes",
        "Progressive decay beats a single abrupt step drop",
        "Realistic gain &#8776;1-3% (pooled &#8776;2%; individuals 0-6%)",
        "Over-taper: &gt;3 wk of low load, or losing intensity",
    ], 17, 11, DIM))

    # race-week countdown
    s.append(_t(20, 258, "RACE-WEEK COUNTDOWN", 11, TXT, weight="600"))
    s.append(_line(70, 300, 668, 300, TXT, 1.4))
    ticks = [(70, "14"), (238, "10"), (365, "7"), (449, "5"), (533, "3"), (617, "1"), (660, "RACE")]
    for x, lab in ticks:
        s.append(_line(x, 295, x, 305, DIM, 1))
        s.append(_t(x, 318, lab, 11, DIM if lab != "RACE" else TXT, "middle"))
    s.append(_t(20, 304, "days out", 11, DIMMER))

    for x0, x1, y, ly, lab, anchor, lx in [
            (365, 449, 262, 256, "last genuinely demanding session &#8776;5-7 d out", "middle", 407),
            (238, 365, 282, 276, "stop heavy eccentrics &#8776;7-10 d out", "middle", 301)]:
        s.append(_line(x0, y, x1, y, ACC, 1.4))
        s.append(_line(x0, y, x0, y + 5, ACC, 1.4))
        s.append(_line(x1, y, x1, y + 5, ACC, 1.4))
        s.append(_t(lx, ly, lab, 11, TXT, anchor))
    for x0, x1, y, ly, lab in [
            (533, 660, 332, 348, "short race-pace touches in the final 72 h = priming, not training"),
            (575, 660, 356, 372, "carbohydrate up in the final 1-2 d; +1-2 kg is glycogen and water, not fat")]:
        s.append(_line(x0, y, x1, y, ACC, 1.4))
        s.append(_line(x0, y - 5, x0, y, ACC, 1.4))
        s.append(_line(x1, y - 5, x1, y, ACC, 1.4))
        s.append(_t(690, ly, lab, 11, TXT, "end"))
    s.append("</svg>")

    return _wrap("dg-pd_taper", "The taper: cut volume, keep intensity",
                 "".join(s),
                 "Volume carries the fatigue; intensity carries the sharpness &#8212; so volume is what falls, "
                 "progressively, by 40-60%.")


# ---------------------------------------------------------------- 104 st_sledpush

def d_st_sledpush():
    s = [_open("st_sledpush", 46, 346,
           "A side view of the sled push with hips, knees and ankles extending in sequence, beside "
           "a force-against-distance curve whose static peak is repaid after every pause")]

    s.append(_line(24, 54, 54, 54, ACC, 2, "5 4"))
    s.append(_t(62, 58, "ONE VECTOR &#8212; shin angle, torso angle and push direction aligned in a single "
                        "forward line", 11, TXT))
    s.append(_t(24, 76, "1 hips &#8594; 2 knees &#8594; 3 ankles extend in sequence &#8212; a lagging hip is why "
                        "an athlete stalls under load", 11, TXT))

    # ---- figure panel
    s.append(_panel(20, 88, 320, 170))
    s.append(_line(30, 240, 332, 240, "var(--border)", 1.5))
    s.append('<rect x="40" y="224" width="66" height="16" rx="2" fill="%s" fill-opacity="0.28" '
             'stroke="%s" stroke-opacity="0.7"/>' % (ACC, ACC))
    s.append(_line(86, 224, 86, 148, ACC, 3))
    s.append(_line(86, 148, 104, 148, ACC, 3))
    s.append(_t(46, 254, "sled", 11, DIMMER))
    # body: rear ankle -> knee -> hip -> shoulder -> hands (one straight incline)
    s.append('<path d="M 240 238 L 215 220 L 185 200 L 140 166 L 104 148" fill="none" stroke="%s" '
             'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>' % TXT)
    s.append('<path d="M 185 200 L 168 224 L 158 240" fill="none" stroke="%s" stroke-width="3" '
             'stroke-linecap="round" stroke-linejoin="round" stroke-opacity="0.55"/>' % TXT)
    s.append(_line(140, 166, 135, 158, TXT, 2.4))
    s.append('<circle cx="132" cy="148" r="10" fill="none" stroke="%s" stroke-width="2.2"/>' % TXT)
    s.append(_arrow(262, 250, 96, 138, ACC, 2, 9, "6 5"))
    for i, (cx2, cy2, n) in enumerate([(185, 200, "1"), (215, 220, "2"), (240, 238, "3")]):
        s.append('<circle cx="%d" cy="%d" r="9" fill="%s" fill-opacity="0.3" stroke="%s"/>' % (cx2, cy2, ACC, ACC))
        s.append(_t(cx2, cy2 + 4, n, 11, TXT, "middle", "600"))
    s.append(_t(30, 106, "SIDE VIEW &#8212; the push", 11, TXT, weight="600"))

    # ---- friction panel
    s.append(_panel(360, 88, 330, 170))
    s.append(_t(372, 106, "WHY YOU NEVER STOP THE SLED", 11, TXT, weight="600"))
    s.append(_line(388, 122, 388, 224, DIM, 1))
    s.append(_line(388, 224, 676, 224, DIM, 1))
    s.append('<path d="M 390 224 L 396 134 L 412 186 L 486 186 L 486 224 L 500 224 L 506 134 L 522 186 '
             'L 670 186" fill="none" stroke="%s" stroke-width="2.2" stroke-linejoin="round"/>' % ACC)
    s.append(_t(404, 150, "static peak", 11, TXT))
    s.append(_t(524, 128, "paid all over again", 11, "var(--bad)"))
    s.append(_t(418, 180, "kinetic &#8212; moving", 11, DIM))
    s.append(_t(486, 240, "pause", 11, "var(--bad)", "middle"))
    s.append(_t(372, 118, "force needed", 11, DIMMER))
    s.append(_t(676, 240, "distance &#8594;", 11, DIMMER, "end"))
    s.append(_t(372, 252, "Friction, not gravity: resistance is highest at rest.", 11, DIM))

    s.append(_stack(20, 288, [
        "NEUTRAL LUMBAR: flexion under load raises spinal",
        "shear AND stops the hips contributing power.",
        "SCAPULAE protracted, not collapsed &#8212; stabilises the",
        "chain and protects the anterior shoulder.",
        "HIDDEN LIMITER: hip dysfunction destabilises the low",
        "back and blocks force transfer from floor to sled &#8212;",
        "often with no back pain at all (TLF, QL implicated).",
    ], 14, 11, DIM))
    s.append(_stack(370, 288, [
        "S&amp;C: bilateral maximal strength (front and back squat,",
        "barbell or trap-bar deadlift); heavy unilateral work",
        "(Bulgarian split squat) for the glutes and hamstrings",
        "driving hip extension; heavy horizontal sled work;",
        "core bracing &#8212; the legs are an extension of the sled.",
        "Compact mesomorph: low torso angle, don't over-shorten",
        "the steps. Tall ectomorph: slightly higher torso, favour",
    ], 14, 11, DIM))
    s.append(_t(370, 386, "rhythm and stiffness over maximal drive per step.", 11, DIM))
    s.append("</svg>")

    return _wrap("dg-st_sledpush", "Sled push &#8212; one vector, three joints, no pauses",
                 "".join(s),
                 "Frictional resistance is highest at rest, so continuous force beats a powerful but "
                 "intermittent push.")


# ---------------------------------------------------------------- 41 pd_annual

def d_pd_annual():
    s = [_open("pd_annual", 28, 356,
           "An annual plan counted backwards from the A-race: phase bands on a week axis, "
           "simulation markers, race tiers, and the fixed station order")]

    s.append(_t(20, 42, "PLAN BACKWARDS: fix the A-race date &#8594; count the weeks &#8594; assign the phases "
                        "&#8594; only then write sessions", 12, TXT, weight="600"))
    s.append(_arrow(620, 56, 40, 56, ACC, 1.6, 9))
    s.append(_line(40, 72, 620, 72, DIM, 1))
    s.append(_line(40, 68, 40, 76, DIM, 1))
    s.append(_line(620, 68, 620, 76, DIM, 1))
    s.append(_t(330, 66, "16-24 week race-specific block (8-12 only for an already-trained athlete)",
                11, DIM, "middle"))

    for x0, x1, lab, op in [(40, 330, "GENERAL PREP", 0.12), (330, 572, "SPECIFIC PREP", 0.2),
                            (572, 620, "TAPER", 0.32), (620, 684, "TRANS.", 0.12)]:
        s.append('<rect x="%d" y="84" width="%d" height="28" fill="%s" fill-opacity="%s" stroke="%s" '
                 'stroke-opacity="0.5"/>' % (x0, x1 - x0, ACC, op, ACC))
        s.append(_t((x0 + x1) / 2, 102, lab, 11, TXT, "middle", "600"))
    s.append(_line(620, 76, 620, 118, TXT, 1.6))
    s.append(_t(660, 78, "A-RACE", 11, TXT, "middle", "600"))

    for x, lab in [(40, "24"), (233, "16"), (330, "12"), (427, "8"), (475, "6"), (523, "4"),
                   (572, "2"), (620, "0")]:
        s.append(_line(x, 112, x, 120, DIM, 1))
        s.append(_t(x, 132, lab, 11, DIM, "middle"))
    s.append(_t(690, 132, "wk out", 11, DIMMER, "end"))
    s.append(_t(185, 150, "&#8593; volume, &#8595; intensity, wide movement base", 11, DIM, "middle"))
    s.append(_t(451, 150, "&#8595; volume, &#8593; race pace + compromised work", 11, DIM, "middle"))

    s.append(_line(330, 168, 427, 168, ACC, 1.4))
    s.append(_line(330, 168, 330, 174, ACC, 1.4))
    s.append(_line(427, 168, 427, 174, ACC, 1.4))
    s.append(_stack(378, 184, ["compromised run&#8594;station&#8594;run", "introduced meaningfully"],
                    14, 11, TXT, "middle"))
    s.append(_line(475, 168, 523, 168, ACC, 1.4))
    s.append(_line(475, 168, 475, 174, ACC, 1.4))
    s.append(_line(523, 168, 523, 174, ACC, 1.4))
    s.append(_stack(560, 184, ["sharpened in", "the final 4-6 wk"], 14, 11, TXT, "middle"))

    for x in (354, 427, 499, 572):
        s.append('<path d="M %d 212 L %d 219 L %d 226 L %d 219 Z" fill="%s"/>' % (x, x + 7, x, x - 7, ACC))
    s.append(_t(20, 240, "&#9670; full or near-full simulations &#8776; every 3-4 wk in specific prep; the last "
                         "one &#8805; 2 wk out", 11, DIM))
    s.append(_t(690, 258, "taper 7-14 d: volume &#8595; 40-60%, intensity and race-pace touches retained, "
                          "frequency held", 11, DIM, "end"))

    for x0, lab in [(20, "A &#8212; full taper + peak, 1-2 per year"),
                    (245, "B &#8212; tested, but trained through"),
                    (470, "C &#8212; practice exposure, no unload")]:
        s.append(_box(x0, 270, 210, 26, op=0.10))
        s.append(_t(x0 + 12, 287, lab, 11, TXT))
    s.append(_t(20, 314, "Loading pattern commonly 2-3 build weeks : 1 deload &#8212; the deload cuts volume "
                         "first and keeps some intensity.", 11, DIM))

    s.append(_t(20, 334, "FIXED ORDER &#8212; one 1 km run before each station:", 11, TXT, weight="600"))
    names = ["1 Ski", "2 Push", "3 Pull", "4 Burpee", "5 Row", "6 Carry", "7 Lunge", "8 Wall"]
    for i, nm in enumerate(names):
        x = 20 + i * 84
        hot = i >= 6
        s.append('<rect x="%d" y="342" width="76" height="24" rx="5" fill="%s" fill-opacity="%s" '
                 'stroke="%s" stroke-opacity="0.8"/>'
                 % (x, ACC, 0.28 if hot else 0.12, "var(--warn)" if hot else ACC))
        s.append(_t(x + 38, 358, nm, 11, TXT, "middle"))
    s.append(_t(350, 380, "Order is fixed, so plan position dictates fatigue state &#8212; wall balls and sandbag "
                          "lunges are trained PRE-FATIGUED.", 11, DIM, "middle"))
    s.append("</svg>")

    return _wrap("dg-pd_annual", "The annual plan, counted back from the A-race",
                 "".join(s),
                 "Fix the date first: every phase, simulation and taper window is placed by counting weeks "
                 "backwards from it.")


# ---------------------------------------------------------------- 74 sk_sequence

def d_sk_sequence():
    s = [_open("sk_sequence", 30, 355,
           "A five-rung practice-context ladder from isolated drilling up to full simulation, "
           "with bars widening as representativeness rises and phases bracketed on the right")]

    s.append(_t(30, 42, "REPRESENTATIVENESS &#8594;", 11, TXT, weight="600"))
    s.append(_t(182, 42, "how much of the competition environment the rehearsal restores", 11, DIMMER))

    rungs = [
        ("1 &#183; ISOLATED DRILLING", 26,
         ["component pattern away from the implement, fresh, dense feedback,",
          "with a NARROW band of variation &#8212; narrow, not zero"]),
        ("2 &#183; INTACT SKILL, UNOPPOSED", 54,
         ["no opponent and no tactical decisions &#8212; but fatigue is deliberately",
          "present: the pattern must survive a degraded internal state"]),
        ("3 &#183; STRATEGIC PARAMETERS VARY", 82,
         ["set size, pause placement, breathing, doubles switch schedule.",
          "Strategy varies here, not the movement kinematics (day 28)"]),
        ("4 &#183; REDUCED-INTENSITY CONTEXT", 110,
         ["approach and leave at running pace, one nominated strategy, the whole",
          "bout capped below race effort &#8212; the target is context, not conditioning"]),
        ("5 &#183; FULL SIMULATION &#8594; THE RACE", 138,
         ["whole-race structure: station entry, roxzone transitions, in-race",
          "decisions. Defined by structure, not by pace"]),
    ]
    for i, (name, w, lines) in enumerate(rungs):
        y = 52 + i * 56
        s.append('<rect x="30" y="%d" width="%d" height="14" rx="3" fill="%s" fill-opacity="%s"/>'
                 % (y + 16, w, ACC, 0.25 + i * 0.16))
        s.append(_t(182, y + 16, name, 12, TXT, weight="600"))
        s.append(_stack(182, y + 32, lines, 14, 11, DIM))

    for y0, y1, labs in [(52, 158, ["GENERAL", "PREP"]), (164, 270, ["SPECIFIC", "PREP"]),
                         (276, 326, ["PRE-RACE"])]:
        s.append('<rect x="600" y="%d" width="84" height="%d" rx="5" fill="%s" fill-opacity="0.10" '
                 'stroke="%s" stroke-opacity="0.45"/>' % (y0, y1 - y0, ACC, ACC))
        top = (y0 + y1) / 2 + 4 - (7 * (len(labs) - 1))
        s.append(_stack(642, top, labs, 14, 11, TXT, "middle"))

    s.append(_t(30, 348, "A separate axis from day 29's MOVEMENT ladder (load, range, stability, velocity) "
                         "&#8212; say which one you are advancing.", 11, DIM))
    s.append(_t(30, 364, "Contextual interference (blocked vs interleaved) is a separate lever at any rung. "
                         "Track a rung PER SKILL, not per athlete.", 11, DIM))
    s.append(_t(30, 380, "Rung 5 clusters in the weeks before racing &#8212; but never so close that a full "
                         "simulation compromises the taper (day 43).", 11, DIM))
    s.append("</svg>")

    return _wrap("dg-sk_sequence", "The practice-context ladder",
                 "".join(s),
                 "Each rung restores information the one below withheld &#8212; which is why the top rung is "
                 "a poor place to teach anything new.")


# ---------------------------------------------------------------- 91 rb_jogging

RUN_PATH = ("M 110 100 Q 139 68 168 100 Q 197 132 226 100 Q 255 68 284 100 Q 313 132 342 100 "
            "Q 371 68 400 100 Q 429 132 458 100 Q 487 68 516 100 Q 545 132 574 100 Q 603 68 632 100 "
            "Q 661 132 690 100")
JOG_PATH = ("M 110 232 Q 139 222 168 232 Q 197 242 226 232 Q 255 222 284 232 Q 313 242 342 232 "
            "Q 371 222 400 232 Q 429 242 458 232 Q 487 222 516 232 Q 545 242 574 232 Q 603 222 632 232 "
            "Q 661 242 690 232")


def d_rb_jogging():
    s = [_open("rb_jogging", 33, 344,
           "Running drawn as a bouncing spring-mass wave with short ground contacts above jogging "
           "drawn as a flat shuffle with long ones"),
         _RM]

    s.append(_t(20, 46, "RUNNING &#8212; a spring-mass bounce", 12, TXT, weight="600"))
    s.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-linecap="round"/>'
             % (RUN_PATH, ACC))
    s.append(_line(110, 100, 690, 100, DIMMER, 1, "3 4"))
    for x0 in (182, 298, 414, 530, 646):
        s.append('<rect x="%d" y="138" width="30" height="7" rx="3" fill="%s" fill-opacity="0.8"/>'
                 % (x0, ACC))
    s.append(_t(20, 145, "ground contact", 11, DIMMER))
    s.append(_t(255, 62, "flight", 11, DIMMER, "middle"))
    s.append(_t(20, 166, "real flight time &#183; clear vertical oscillation &#183; propulsion from behind the "
                         "body &#183; swing leg recycled elastically", 11, DIM))

    s.append(_t(20, 200, "JOGGING &#8212; a compliant shuffle", 12, TXT, weight="600"))
    s.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4" stroke-linecap="round" '
             'stroke-opacity="0.55"/>' % (JOG_PATH, TXT))
    s.append(_line(110, 232, 690, 232, DIMMER, 1, "3 4"))
    for x0, w in [(150, 100), (266, 100), (382, 100), (498, 100), (614, 76)]:
        s.append('<rect x="%d" y="258" width="%d" height="7" rx="3" fill="%s" fill-opacity="0.45"/>'
                 % (x0, w, TXT))
    s.append(_t(20, 265, "ground contact", 11, DIMMER))
    s.append(_t(20, 280, "little flight &#183; small oscillation &#183; foot lands ahead of the centre of mass "
                         "&#183; swing leg pulled through by hip flexion", 11, DIM))

    s.append('<g class="dg-anim">'
             '<circle r="4.5" fill="%s"><animateMotion dur="5s" repeatCount="indefinite" path="%s"/></circle>'
             '<circle r="4.5" fill="%s" fill-opacity="0.6"><animateMotion dur="5s" repeatCount="indefinite" '
             'path="%s"/></circle></g>' % (ACC, RUN_PATH, TXT, JOG_PATH))

    s.append(_arrow(60, 356, 190, 352, DIM, 1.4, 7))
    s.append(_arrow(60, 356, 168, 306, ACC, 2.2, 8))
    s.append(_arrow(60, 356, 98, 300, DIM, 1.4, 7))
    s.append(_t(196, 356, "too flat", 11, DIM))
    s.append(_t(174, 302, "optimum", 11, TXT))
    s.append(_t(104, 296, "too bouncy", 11, DIM))
    s.append(_stack(280, 308, [
        "Vertical movement is not waste &#8212; the optimum is an ANGLE, not a direction.",
        "Race pace sits well above habitual easy pace, so an athlete who only runs",
        "slowly grooves the jogging pattern and cannot access the running one.",
        "Keep it available: strides, hill sprints, plyometrics, heavy strength.",
        "Watch the drop into jogging mechanics after a station &#8212; a hidden time loss.",
    ], 16, 11, DIM))
    s.append("</svg>")

    return _wrap("dg-rb_jogging", "Two different gaits, not two speeds",
                 "".join(s),
                 "Easy volume is still good aerobic training &#8212; the error is assuming it develops the "
                 "running pattern.")


# ---------------------------------------------------------------- 4 sm_recovery

def d_sm_recovery():
    s = [_open("sm_recovery", 31, 344,
           "Four recovery clocks of very different lengths drawn on one compressed time axis, "
           "above the shape of a single night of sleep")]

    s.append(_t(20, 44, "FOUR RECOVERY CLOCKS, RUNNING AT DIFFERENT SPEEDS", 12, TXT, weight="600"))
    clocks = [
        (74, 150, 300, "FLUID &amp; ELECTROLYTES &#8212; hours; replace &#8776;125-150% of the deficit "
                       "WITH sodium", 0.55),
        (110, 150, 380, "SUBSTRATE (muscle glycogen) &#8212; &#8776;5%/h with adequate carbohydrate; "
                        "full in 20-24 h", 0.45),
        (146, 380, 525, "TISSUE REPAIR (myofibril, connective) &#8212; 1-3+ days; protein 1.6-2.2 g/kg/day",
         0.35),
        (182, 150, 665, "CENTRAL / AUTONOMIC (drive, mood, motor control) &#8212; hours to WEEKS", 0.25),
    ]
    for ty, x0, x1, lab, op in clocks:
        s.append(_t(20, ty, lab, 11, TXT))
        s.append('<rect x="%d" y="%d" width="%d" height="12" rx="5" fill="%s" fill-opacity="%s"/>'
                 % (x0, ty + 4, x1 - x0, ACC, op))
    s.append(_line(150, 212, 670, 212, DIM, 1))
    for x, lab in [(150, "1 h"), (225, "4 h"), (300, "12 h"), (380, "24 h"), (470, "3 d"),
                   (555, "1 wk"), (660, "weeks")]:
        s.append(_line(x, 208, x, 216, DIM, 1))
        s.append(_t(x, 228, lab, 11, DIMMER, "middle"))

    s.append(_t(676, 244, "the time axis is compressed &#8212; read where each bar reaches, not how "
                           "long it looks", 11, DIMMER, "end"))
    s.append(_t(20, 258, "ONE NIGHT &#8212; 4-6 cycles of &#8776;90 min", 12, TXT, weight="600"))
    s.append(_t(620, 262, "shaded = the last 2 h: cutting it removes disproportionately more REM",
                11, DIM, "end"))
    s.append('<rect x="471" y="266" width="149" height="74" fill="var(--warn)" fill-opacity="0.14"/>')
    s.append(_panel(60, 266, 560, 74, "var(--surface)", "var(--border)", 1.0, 4))
    s.append(_stack(20, 286, ["REM"], 14, 11, DIMMER))
    s.append(_stack(20, 304, ["light"], 14, 11, DIMMER))
    s.append(_stack(20, 330, ["SWS"], 14, 11, DIMMER))
    for x in (172, 284, 396, 508):
        s.append(_line(x, 268, x, 338, "var(--border)", 1, "3 3"))
    for x0, w in [(66, 100), (178, 100), (290, 100), (402, 100), (514, 100)]:
        s.append('<rect x="%d" y="292" width="%d" height="10" rx="3" fill="%s" fill-opacity="0.18"/>'
                 % (x0, w, TXT))
    for x0, w in [(152, 20), (254, 30), (356, 40), (458, 50), (560, 60)]:
        s.append('<rect x="%d" y="274" width="%d" height="11" rx="3" fill="%s" fill-opacity="0.85"/>'
                 % (x0, w, ACC))
    for x0, w in [(66, 52), (178, 44), (290, 28), (402, 14)]:
        s.append('<rect x="%d" y="312" width="%d" height="18" rx="3" fill="%s" fill-opacity="0.45"/>'
                 % (x0, w, ACC))
    s.append(_t(64, 352, "bedtime", 11, DIMMER))
    s.append(_t(620, 352, "wake", 11, DIMMER, "end"))

    s.append(_t(20, 370, "SWS is front-loaded: the largest nocturnal GH pulse, immune and physical restoration "
                         "&#183; REM is back-loaded: motor consolidation, mood.", 11, DIM))
    s.append("</svg>")

    return _wrap("dg-sm_recovery", "Four clocks, and the shape of one night",
                 "".join(s),
                 "Target 7-9 h (8-10 h in heavy blocks); &lt;8 h is associated with &#8776;1.7&#215; the odds "
                 "of injury, and sleep extension is the best-evidenced recovery intervention.")


# ---------------------------------------------------------------- 101 sm_antidoping

def d_sm_antidoping():
    s = [_open("sm_antidoping", 22, 354,
           "Strict liability across the top, then the prohibited list, the rule violations a coach "
           "can personally commit, and the four conditions a TUE must meet")]

    s.append('<rect x="20" y="24" width="670" height="44" rx="8" fill="var(--bad)" fill-opacity="0.12" '
             'stroke="var(--bad)" stroke-opacity="0.55"/>')
    s.append(_t(34, 44, "STRICT LIABILITY &#8212; the athlete is responsible for what is in their body, "
                        "regardless of intent or negligence", 12, TXT, weight="600"))
    s.append(_t(34, 60, "or how it got there. 'My supplement was contaminated' is an explanation, not "
                        "a defence.", 11, DIM))

    # column 1
    s.append(_panel(20, 82, 210, 228))
    s.append(_t(30, 102, "THE PROHIBITED LIST", 12, TXT, weight="600"))
    s.append(_t(30, 118, "updated at least annually", 11, DIMMER))
    for y0, h, lines in [(126, 26, ["Prohibited AT ALL TIMES"]),
                         (158, 40, ["Prohibited IN COMPETITION", "only"]),
                         (204, 40, ["Prohibited in PARTICULAR", "SPORTS"]),
                         (250, 54, ["METHODS too: blood", "manipulation, chemical and",
                                    "physical manipulation, gene doping"])]:
        s.append(_box(30, y0, 190, h, op=0.12))
        s.append(_stack(38, y0 + 17, lines, 13, 11, TXT))

    # column 2
    s.append(_panel(245, 82, 210, 228))
    s.append(_t(255, 102, "RULE VIOLATIONS", 12, TXT, weight="600"))
    s.append(_t(255, 118, "far beyond a positive test", 11, DIMMER))
    items = ["use or attempted use", "refusing or evading a test", "whereabouts failures",
             "tampering", "possession", "trafficking"]
    for i, it in enumerate(items):
        s.append(_t(255, 138 + i * 17, "&#183; " + it, 11, DIM))
    s.append('<rect x="249" y="228" width="200" height="74" rx="6" fill="var(--warn)" fill-opacity="0.14" '
             'stroke="var(--warn)" stroke-opacity="0.6"/>')
    s.append(_t(257, 246, "a COACH can personally commit:", 11, "var(--warn)", weight="600"))
    for i, it in enumerate(["administration", "complicity", "prohibited association"]):
        s.append(_t(257, 264 + i * 16, "&#183; " + it.upper(), 11, TXT))

    # column 3
    s.append(_panel(470, 82, 220, 228))
    s.append(_t(480, 102, "TUE &#8212; all four must hold", 12, TXT, weight="600"))
    s.append(_stack(480, 126, [
        "1  a clear medical need",
        "2  no reasonable permitted",
        "     alternative",
        "3  no extra performance benefit",
        "     beyond return to normal health",
        "4  the need is not the result of",
        "     prior non-therapeutic use",
    ], 16, 11, TXT))
    s.append(_stack(480, 258, ["Apply in ADVANCE. Retroactive",
                               "applications are limited to defined",
                               "circumstances such as emergency",
                               "treatment."], 14, 11, DIM))

    s.append(_box(20, 316, 670, 58, op=0.10))
    s.append(_t(32, 334, "COACH DUTIES", 12, TXT, weight="600"))
    s.append(_t(150, 334, "Check EVERY medication, including over-the-counter cold and allergy remedies.",
                11, DIM))
    s.append(_t(32, 350, "If supplements are used at all, advise third-party batch-tested products &#8212; "
                         "that reduces, never eliminates, risk.", 11, DIM))
    s.append(_t(32, 366, "NEVER supply anything. Advise, document, refer to a physician or pharmacist &#8212; "
                         "education is part of the role.", 11, TXT))
    s.append("</svg>")

    return _wrap("dg-sm_antidoping", "Strict liability, the List, and the TUE gate",
                 "".join(s),
                 "Supplements are the commonest route to an inadvertent violation &#8212; advise, document "
                 "and refer, but never supply.")


# ---------------------------------------------------------------- 76 pc_junior

def d_pc_junior():
    s = [_open("pc_junior", 32, 350,
           "Height-velocity curves for girls and boys with the peak-height-velocity window shaded, "
           "beside maturation notes and three panels on training around it")]

    s.append(_panel(20, 34, 450, 216))
    s.append(_t(30, 52, "HEIGHT VELOCITY CURVE", 12, TXT, weight="600"))
    s.append('<rect x="180" y="66" width="120" height="166" fill="var(--warn)" fill-opacity="0.14"/>')
    s.append(_t(240, 62, "VULNERABLE WINDOW", 11, "var(--warn)", "middle"))
    s.append(_line(40, 232, 420, 232, DIM, 1))
    s.append(_line(40, 66, 40, 232, DIM, 1))
    s.append(_t(46, 78, "growth rate", 11, DIMMER))
    s.append(_t(420, 248, "biological age &#8594;", 11, DIMMER, "end"))
    s.append('<path d="M 46 226 C 120 222 158 210 190 120 C 200 92 216 92 226 122 C 244 176 300 218 418 226" '
             'fill="none" stroke="%s" stroke-width="2.4"/>' % ACC)
    s.append('<path d="M 46 228 C 150 224 200 216 240 136 C 252 110 268 110 280 140 C 300 192 348 222 418 228" '
             'fill="none" stroke="%s" stroke-width="2.2" stroke-dasharray="6 4" stroke-opacity="0.75"/>' % TXT)
    s.append(_t(208, 100, "PHV", 11, TXT, "middle", "600"))
    s.append(_t(262, 116, "PHV", 11, TXT, "middle", "600"))
    s.append(_line(316, 78, 332, 78, ACC, 2.4))
    s.append(_t(338, 82, "girls typically earlier", 11, DIM))
    s.append(_line(316, 96, 332, 96, TXT, 2.2, "6 4"))
    s.append(_t(338, 100, "boys later", 11, DIM))
    s.append(_t(338, 118, "wide individual variation", 11, DIMMER))

    chips = [
        (40, 60, ["BIOLOGICAL &#8800; CHRONOLOGICAL", "two children of one birth year",
                  "can be years apart in maturity"]),
        (108, 60, ["RELATIVE AGE EFFECT", "early-in-year births dominate squads",
                   "&#8212; bigger and more mature, not better"]),
        (176, 74, ["SAFE TO LIFT", "supervised, technique-led resistance",
                   "training lowers injury risk; 'lifting",
                   "stunts growth' is not supported"]),
    ]
    for y0, h, lines in chips:
        s.append(_box(478, y0, 212, h, op=0.10))
        s.append(_t(488, y0 + 18, lines[0], 11, TXT, weight="600"))
        s.append(_stack(488, y0 + 34, lines[1:], 14, 11, DIM))

    cells = [
        (20, "AROUND PHV", ["coordination dips; apophyses",
                            "become vulnerable &#8212; Osgood-",
                            "Schlatter (tibial tuberosity),",
                            "Sever's (calcaneus). Cut impact",
                            "and plyo volume, hold technique,",
                            "do not chase load. Height check",
                            "every 4-8 weeks."]),
        (245, "PHYSIOLOGY", ["high aerobic recoverability but",
                             "lower anaerobic and glycolytic",
                             "capacity &#8212; long heavy lactate",
                             "work is a poor fit and low yield.",
                             "Thermoregulation less efficient:",
                             "manage heat exposure and drink",
                             "access proactively."]),
        (470, "HYROX MODIFICATIONS", ["an adult format with fixed loads.",
                                      "Shorten the run legs; lighter sleds",
                                      "and sandbags; reduce wall-ball",
                                      "weight and target height; fewer",
                                      "total stations. Never default to",
                                      "open-division loads. Mastery- and",
                                      "fun-led, or they drop out."]),
    ]
    for x0, head, lines in cells:
        s.append(_panel(x0, 264, 210, 116))
        s.append(_t(x0 + 10, 282, head, 11, TXT, weight="600"))
        s.append(_stack(x0 + 10, 298, lines, 13, 11, DIM))
    s.append("</svg>")

    return _wrap("dg-pc_junior", "Sequencing a junior to biological age",
                 "".join(s),
                 "Around peak height velocity, coordination dips and the apophyses become vulnerable "
                 "&#8212; cut volume and hold technique rather than chasing load.")


# ---------------------------------------------------------------- 3 cm_behaviour

def d_cm_behaviour():
    s = [_open("cm_behaviour", 38, 338,
           "The motivation continuum from controlled to internalised, the three basic needs, three "
           "goal types drawn by how much the athlete controls, the habit loop and self-efficacy sources")]

    s.append(_t(45, 50, "CONTROLLED", 11, DIM))
    s.append(_t(670, 50, "INTERNALISED &#8212; the session gets done unsupervised", 11, TXT, "end"))
    s.append(_arrow(45, 72, 672, 72, ACC, 2, 9))
    stops = [(60, "amotivation", 3, 0.35), (168, "external", 4, 0.45), (276, "introjected", 5, 0.55),
             (384, "identified", 6, 0.7), (492, "integrated", 7, 0.85), (600, "intrinsic", 8, 1.0)]
    for x, lab, r, op in stops:
        s.append('<circle cx="%d" cy="72" r="%d" fill="%s" fill-opacity="%s"/>' % (x, r, ACC, op))
        s.append(_t(x, 96, lab, 11, TXT if op > 0.6 else DIM, "middle"))
    s.append(_t(350, 116, "more internalised regulation is generally associated with better persistence",
                11, DIMMER, "middle"))

    s.append(_panel(20, 132, 310, 130))
    s.append(_t(30, 152, "THREE BASIC NEEDS (SDT)", 12, TXT, weight="600"))
    for i, lab in enumerate(["AUTONOMY &#8212; choice and ownership",
                             "COMPETENCE &#8212; visible mastery",
                             "RELATEDNESS &#8212; belonging"]):
        y = 174 + i * 22
        s.append(_arrow(32, y - 4, 58, y - 4, ACC, 1.6, 6))
        s.append(_t(66, y, lab, 11, TXT))
    s.append(_t(30, 240, "Undermine them &#8212; controlling language, arbitrary", 11, "var(--bad)"))
    s.append(_t(30, 256, "loads, constant outcome comparison &#8212; and it collapses.", 11, "var(--bad)"))

    s.append(_panel(350, 132, 340, 130))
    s.append(_t(360, 152, "THREE GOAL TYPES &#8212; use all three, not a ranking", 12, TXT, weight="600"))
    goals = [(172, 34, "OUTCOME &#8212; 'finish top 10': direction, not control"),
             (206, 80, "PERFORMANCE &#8212; 'sub-1:20': a self-referenced standard"),
             (240, 150, "PROCESS &#8212; break scheme, breathing: fully yours")]
    for y, w, lab in goals:
        s.append(_t(360, y, lab, 11, TXT))
        s.append('<rect x="360" y="%d" width="%d" height="6" rx="3" fill="%s" fill-opacity="0.75"/>'
                 % (y + 5, w, ACC))
    s.append(_t(360, 262, "bar = how much of it the athlete actually controls", 11, DIMMER))

    s.append(_panel(20, 274, 310, 100))
    s.append(_t(30, 294, "HABIT LOOP", 12, TXT, weight="600"))
    for x, lab in [(30, "CUE"), (128, "ROUTINE"), (226, "REWARD")]:
        s.append(_box(x, 302, 84, 24, op=0.14))
        s.append(_t(x + 42, 318, lab, 11, TXT, "middle"))
    s.append(_arrow(116, 314, 126, 314, DIM, 1.4, 5))
    s.append(_arrow(214, 314, 224, 314, DIM, 1.4, 5))
    s.append('<path d="M 268 328 Q 170 344 74 330" fill="none" stroke="%s" stroke-width="1.4" '
             'stroke-opacity="0.7"/>' % DIM)
    s.append(_arrow(80, 331, 72, 328, DIM, 1.4, 5))
    s.append(_stack(30, 350, ["stable time and place + an 'if X then Y' plan",
                              "beats intention alone"], 14, 11, DIM))

    s.append(_panel(350, 274, 340, 100))
    s.append(_t(360, 294, "SELF-EFFICACY SOURCES (Bandura) &#8212; strongest first", 12, TXT, weight="600"))
    for i, (w, lab) in enumerate([(310, "mastery experience"), (238, "vicarious &#8212; peer modelling"),
                                  (166, "verbal persuasion"), (112, "reading own state")]):
        y = 302 + i * 18
        s.append('<rect x="360" y="%d" width="%d" height="14" rx="4" fill="%s" fill-opacity="0.16" '
                 'stroke="%s" stroke-opacity="0.5"/>' % (y, w, ACC, ACC))
        s.append(_t(366, y + 11, lab, 11, TXT))
    s.append("</svg>")

    return _wrap("dg-cm_behaviour", "Adherence: the motivation continuum and its levers",
                 "".join(s),
                 "For most amateurs a good plan half-completed loses to a modest plan completed &#8212; so "
                 "feed autonomy, competence and relatedness.")


# ---------------------------------------------------------------- 69 ph_fluidbalance

def d_ph_fluidbalance():
    s = [_open("ph_fluidbalance", 29, 352,
           "Body-water compartments drawn to relative size with plasma highlighted, what sweating "
           "actually does in five steps, and the contested dehydration threshold")]

    s.append(_t(20, 42, "TOTAL BODY WATER &#8776; 45-75% of body mass &#8212; conventionally &#8776;60% in lean "
                        "young men, &#8776;50-55% in women", 12, TXT, weight="600"))
    s.append(_t(20, 58, "It tracks leanness &#8212; the same sweat loss is a larger fraction of reserve in the "
                        "higher-body-fat athlete.", 11, DIM))

    s.append('<rect x="20" y="76" width="206" height="174" rx="6" fill="%s" fill-opacity="0.22" '
             'stroke="%s" stroke-opacity="0.7"/>' % (ACC, ACC))
    s.append(_t(30, 100, "INTRACELLULAR", 12, TXT, weight="600"))
    s.append(_t(30, 116, "&#8776; 2/3 of total body water", 11, DIM))
    s.append('<rect x="226" y="76" width="104" height="130" fill="%s" fill-opacity="0.10" '
             'stroke="%s" stroke-opacity="0.7"/>' % (ACC, ACC))
    s.append('<rect x="226" y="206" width="104" height="44" fill="%s" fill-opacity="0.32" '
             'stroke="%s" stroke-opacity="0.95" stroke-width="1.8"/>' % (ACC, ACC))
    s.append(_stack(234, 94, ["EXTRA-", "CELLULAR &#8776;1/3"], 14, 11, TXT))
    s.append(_stack(234, 134, ["interstitial", "&#8776;3/4 of ECF"], 14, 11, DIM))
    s.append(_stack(234, 226, ["PLASMA", "&#8776;1/4 of ECF"], 14, 11, TXT))
    s.append(_t(20, 266, "Plasma is the smallest MAJOR compartment, and the decisive one.", 11, DIM))
    s.append(_t(20, 282, "(transcellular fluid &#8212; synovial, CSF, gut, ocular &#8212; set aside)", 11, DIMMER))

    s.append(_panel(350, 76, 340, 174))
    s.append(_t(360, 96, "WHAT SWEATING ACTUALLY DOES", 12, TXT, weight="600"))
    s.append(_stack(360, 116, [
        "1  Sweat is HYPOTONIC &#8212; the gland secretes",
        "     near-isotonic fluid, the duct reclaims Na and Cl",
        "2  So sweating CONCENTRATES the extracellular",
        "     space: plasma sodium rises (135-145 mmol/L;",
        "     osmolality defended at 285-295 mOsm/kg)",
        "3  Water leaves the cells down the gradient",
        "4  Plasma volume is partly DEFENDED &#8594; stroke",
        "     volume, cardiac output, skin blood flow",
        "5  Osmoreceptors &#8594; thirst + vasopressin",
    ], 15, 11, TXT))
    s.append(_t(360, 266, "Sodium's role is therefore mostly INDIRECT. Sweat sodium", 11, DIM))
    s.append(_t(360, 282, "loss is not the usual route to hyponatraemia &#8212; excess", 11, DIM))
    s.append(_t(360, 298, "dilute fluid is. Na/K-ATPase: 3 Na out : 2 K in per ATP.", 11, DIM))
    s.append(_t(20, 298, "&#8776;1/5 to 1/3 of resting energy turnover goes on that pump.", 11, DIM))

    s.append(_panel(20, 312, 670, 66, "var(--surface-2)", "var(--border)"))
    s.append(_t(32, 330, "THE EVIDENCE DISAGREES &#8212; and you should be able to say why", 11, TXT,
                weight="600"))
    s.append(_stack(32, 346, [
        "LAB: the share of trials reporting a decrement climbs with the deficit &#8212; a coin flip at 2-3%, "
        "common beyond 4%.",
        "FIELD: across 643 marathon finishers, body-mass change was INVERSELY related to finish time "
        "(Zouhal 2011).",
        "Read that as: lab protocols overstate the field effect, NOT that dehydration helps.",
    ], 15, 11, DIM))
    s.append("</svg>")

    return _wrap("dg-ph_fluidbalance", "Compartments, hypotonic sweat and a contested threshold",
                 "".join(s),
                 "Sweating raises plasma sodium, which pulls water out of the cells and partly defends the "
                 "one compartment that sets your pace.")


DIAGRAMS = {
    "sk_categories": d_sk_categories,
    "rb_treadmills": d_rb_treadmills,
    "pd_doublepeak": d_pd_doublepeak,
    "pd_taper": d_pd_taper,
    "st_sledpush": d_st_sledpush,
    "pd_annual": d_pd_annual,
    "sk_sequence": d_sk_sequence,
    "rb_jogging": d_rb_jogging,
    "sm_recovery": d_sm_recovery,
    "sm_antidoping": d_sm_antidoping,
    "pc_junior": d_pc_junior,
    "cm_behaviour": d_cm_behaviour,
    "ph_fluidbalance": d_ph_fluidbalance,
}
