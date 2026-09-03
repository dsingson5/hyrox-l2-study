# -*- coding: utf-8 -*-
"""Bespoke lesson diagrams - batch A."""


def _wrap(did, title, body, caption=""):
    cap = f'<div class="w-hint">{caption}</div>' if caption else ""
    return (f'<div class="widget diagram" id="{did}">'
            f'<div class="w-head"><span class="w-icon">&#9672;</span><span class="w-title">{title}</span></div>'
            f'<div class="w-body">{body}</div>{cap}</div>')


_SVG = ('<svg viewBox="0 0 700 {h}" preserveAspectRatio="xMidYMid meet" '
        'xmlns="http://www.w3.org/2000/svg" id="{tid}-svg" '
        'role="img" aria-label="{label}" '
        'style="width:100%;height:auto;max-height:360px;display:block" '
        'font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" '
        'font-size="11" fill="var(--text)" stroke="none">')


def d_hp_levels():
    body = _SVG.format(h=340, tid="hp_levels", label="Five level bands with typical time at level, beside a four-category grid in which the lowest graded category sets the athlete&#39;s overall level") + '''
<style>
.hp_levels-pulse{animation:hp_levels-pulse 5s ease-in-out infinite}
@keyframes hp_levels-pulse{0%,100%{opacity:.4}50%{opacity:1}}
@media (prefers-reduced-motion:reduce){.hp_levels-pulse{animation:none;opacity:.85}}
</style>
<rect x="8" y="8" width="330" height="246" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="20" y="28" fill="var(--text-dim)">LEVEL / TYPICAL TIME AT LEVEL</text>
<rect x="20" y="41" width="22" height="22" rx="5" fill="var(--theme-accent)"/>
<text x="31" y="56" text-anchor="middle" font-size="12" font-weight="700" fill="var(--bg)">5</text>
<text x="52" y="50" font-size="12" font-weight="600" fill="var(--text)">ELITE / AGE-GROUP WORLDS</text>
<text x="52" y="63" fill="var(--text-dim)">years, plus a supplemental high-skill library</text>
<rect x="20" y="81" width="22" height="22" rx="5" fill="var(--theme-accent)"/>
<text x="31" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="var(--bg)">4</text>
<text x="52" y="90" font-size="12" font-weight="600" fill="var(--text)">PRO</text>
<text x="52" y="103" fill="var(--text-dim)">years, same patterns heavier and faster</text>
<rect x="20" y="121" width="22" height="22" rx="5" fill="var(--theme-accent)"/>
<text x="31" y="136" text-anchor="middle" font-size="12" font-weight="700" fill="var(--bg)">3</text>
<text x="52" y="130" font-size="12" font-weight="600" fill="var(--text)">OPEN</text>
<text x="52" y="143" fill="var(--text-dim)">years, barbell strength as a % of bodyweight</text>
<rect x="20" y="161" width="22" height="22" rx="5" fill="var(--theme-accent)"/>
<text x="31" y="176" text-anchor="middle" font-size="12" font-weight="700" fill="var(--bg)">2</text>
<text x="52" y="170" font-size="12" font-weight="600" fill="var(--text)">BEGINNER</text>
<text x="52" y="183" fill="var(--text-dim)">about half a year, first racing green light</text>
<rect x="20" y="201" width="22" height="22" rx="5" fill="var(--theme-accent)"/>
<text x="31" y="216" text-anchor="middle" font-size="12" font-weight="700" fill="var(--bg)">1</text>
<text x="52" y="210" font-size="12" font-weight="600" fill="var(--text)">ABSOLUTE NOVICE</text>
<text x="52" y="223" fill="var(--text-dim)">weeks to months, racing not yet advised</text>
<text x="20" y="244" fill="var(--text-dimmer)">Time at level climbs roughly logarithmically.</text>
<rect x="350" y="8" width="342" height="246" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="364" y="28" fill="var(--text-dim)">THE FOUR CATEGORIES</text>
<rect x="516" y="16" width="168" height="22" rx="6" fill="var(--bad)" fill-opacity="0.16" stroke="var(--bad)"/>
<text x="600" y="31" text-anchor="middle" font-weight="700" fill="var(--text)">OVERALL = LEVEL 1</text>
<line x1="392" y1="56" x2="392" y2="226" stroke="var(--border)"/>
<line x1="463" y1="56" x2="463" y2="226" stroke="var(--border)"/>
<line x1="534" y1="56" x2="534" y2="226" stroke="var(--border)"/>
<line x1="605" y1="56" x2="605" y2="226" stroke="var(--border)"/>
<line x1="676" y1="56" x2="676" y2="226" stroke="var(--border)"/>
<text x="364" y="65" fill="var(--text-dim)">CARDIO</text>
<line x1="392" y1="78" x2="676" y2="78" stroke="var(--border)" stroke-width="3" stroke-linecap="round"/>
<circle cx="392" cy="78" r="7" fill="var(--theme-accent)"/>
<text x="406" y="82" fill="var(--bad)">weakest - this one sets the level</text>
<text x="364" y="109" fill="var(--text-dim)">STRENGTH (by movement pattern)</text>
<line x1="392" y1="122" x2="676" y2="122" stroke="var(--border)" stroke-width="3" stroke-linecap="round"/>
<circle cx="676" cy="122" r="7" fill="var(--theme-accent)"/>
<text x="662" y="139" text-anchor="end" fill="var(--text-dimmer)">best - ignored</text>
<text x="364" y="153" fill="var(--text-dim)">HYROX EXERCISE STANDARDS</text>
<line x1="392" y1="166" x2="676" y2="166" stroke="var(--border)" stroke-width="3" stroke-linecap="round"/>
<circle cx="534" cy="166" r="7" fill="var(--theme-accent)"/>
<text x="364" y="197" fill="var(--text-dim)">TIME GUIDELINES</text>
<line x1="392" y1="210" x2="676" y2="210" stroke="var(--border)" stroke-width="3" stroke-linecap="round" stroke-dasharray="4 5"/>
<text x="400" y="226" fill="var(--text-dimmer)">graded the same way - not tested in this example</text><text x="676" y="205" text-anchor="end" fill="var(--text-dimmer)">an ungraded category cannot raise the level</text>
<line x1="392" y1="48" x2="392" y2="230" stroke="var(--bad)" stroke-width="2" stroke-dasharray="5 4" class="dg-anim hp_levels-pulse"/>
<text x="392" y="246" text-anchor="middle" fill="var(--text-dimmer)">1</text>
<text x="463" y="246" text-anchor="middle" fill="var(--text-dimmer)">2</text>
<text x="534" y="246" text-anchor="middle" fill="var(--text-dimmer)">3</text>
<text x="605" y="246" text-anchor="middle" fill="var(--text-dimmer)">4</text>
<text x="676" y="246" text-anchor="middle" fill="var(--text-dimmer)">5</text>
<rect x="8" y="264" width="684" height="34" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<rect x="16" y="270" width="46" height="22" rx="5" fill="var(--theme-accent)"/>
<text x="39" y="285" text-anchor="middle" font-weight="700" fill="var(--bg)">3 to 4</text>
<text x="70" y="280" fill="var(--text)">back squat 80% BW | deadlift 100% BW | 100 wall balls 6/4 kg under 6:00 | 10 km under 55/60</text>
<text x="70" y="293" fill="var(--text-dimmer)">goal race time: sub-1:30 (M) / sub-1:40 (W) Open solo</text>
<rect x="8" y="302" width="684" height="34" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<rect x="16" y="308" width="46" height="22" rx="5" fill="var(--theme-accent)"/>
<text x="39" y="323" text-anchor="middle" font-weight="700" fill="var(--bg)">4 to 5</text>
<text x="70" y="318" fill="var(--text)">back squat 120% BW | deadlift 140% BW | 100 wall balls 9/6 kg under 5:00 | 10 km under 40/45</text>
<text x="70" y="331" fill="var(--text-dimmer)">goal race time: sub-1:03 (M) / sub-1:08 (W) Open solo | sub-1:06 / 1:12 Pro</text>
</svg>'''
    return _wrap("dg-hp_levels", "Five levels, four categories, one rule", body,
                 "An athlete IS their lowest category - so a jagged profile writes the next block by itself.")


def d_hp_movelib():
    body = _SVG.format(h=348, tid="hp_movelib", label="The four-part movement write-up, one sled-push thread climbing the five levels, the correction ladder, and a promotion example that fails on cardio") + '''
<rect x="8" y="8" width="300" height="172" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="20" y="26" fill="var(--text-dim)">THE FOUR-PART WRITE-UP</text>
<rect x="20" y="40" width="20" height="20" rx="4" fill="var(--theme-accent)"/>
<text x="30" y="54" text-anchor="middle" font-weight="700" fill="var(--bg)">1</text>
<text x="48" y="49" font-size="11.5" font-weight="600" fill="var(--text)">SET-UP</text>
<text x="48" y="62" fill="var(--text-dim)">checkable before rep 1: the cheapest fixes</text>
<rect x="20" y="70" width="20" height="20" rx="4" fill="var(--theme-accent)"/>
<text x="30" y="84" text-anchor="middle" font-weight="700" fill="var(--bg)">2</text>
<text x="48" y="79" font-size="11.5" font-weight="600" fill="var(--text)">EXECUTION</text>
<text x="48" y="92" fill="var(--text-dim)">narrates the movement itself</text>
<rect x="20" y="100" width="20" height="20" rx="4" fill="var(--theme-accent)"/>
<text x="30" y="114" text-anchor="middle" font-weight="700" fill="var(--bg)">3</text>
<text x="48" y="109" font-size="11.5" font-weight="600" fill="var(--text)">POINTS OF PERFORMANCE</text>
<text x="48" y="122" fill="var(--text-dim)">the few make-or-break checkpoints</text>
<rect x="20" y="130" width="20" height="20" rx="4" fill="var(--theme-accent)"/>
<text x="30" y="144" text-anchor="middle" font-weight="700" fill="var(--bg)">4</text>
<text x="48" y="139" font-size="11.5" font-weight="600" fill="var(--text)">COMMON FAULTS</text>
<text x="48" y="152" fill="var(--text-dim)">a prediction of where it will break</text>
<text x="20" y="171" fill="var(--text-dimmer)">Read the faults first: it trains the coach eye.</text>
<rect x="320" y="8" width="372" height="172" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="332" y="26" fill="var(--text-dim)">SLED PUSH - ONE THREAD UP THE LADDER</text>
<path d="M612,150 L672,46" stroke="var(--theme-accent)" stroke-width="2" stroke-dasharray="5 5" opacity="0.45" fill="none"/>
<path d="M666,54 L674,42 L678,56 Z" fill="var(--theme-accent)" opacity="0.6"/>
<rect x="332" y="40" width="20" height="20" rx="4" fill="var(--theme-accent)"/>
<text x="342" y="54" text-anchor="middle" font-weight="700" fill="var(--bg)">5</text>
<text x="360" y="54" fill="var(--text)">50 m at Pro load, under 3:00</text>
<rect x="332" y="66" width="20" height="20" rx="4" fill="var(--theme-accent)"/>
<text x="342" y="80" text-anchor="middle" font-weight="700" fill="var(--bg)">4</text>
<text x="360" y="80" fill="var(--text)">50 m at Pro load, under 4:00</text>
<rect x="332" y="92" width="20" height="20" rx="4" fill="var(--theme-accent)"/>
<text x="342" y="106" text-anchor="middle" font-weight="700" fill="var(--bg)">3</text>
<text x="360" y="106" fill="var(--text)">50 m at 102 kg, under 4:00</text>
<rect x="332" y="118" width="20" height="20" rx="4" fill="var(--theme-accent)"/>
<text x="342" y="132" text-anchor="middle" font-weight="700" fill="var(--bg)">2</text>
<text x="360" y="132" fill="var(--text)">15 m at plus 60/45 kg, under 2:00</text>
<rect x="332" y="144" width="20" height="20" rx="4" fill="var(--theme-accent)"/>
<text x="342" y="158" text-anchor="middle" font-weight="700" fill="var(--bg)">1</text>
<text x="360" y="158" fill="var(--text)">15 m with an empty sled, unbroken</text>
<text x="332" y="174" fill="var(--text-dimmer)">The official table writes this gate as one flat load.</text>
<rect x="8" y="192" width="300" height="110" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="20" y="210" fill="var(--text-dim)">CORRECTION LADDER</text>
<rect x="20" y="219" width="20" height="20" rx="4" fill="var(--theme-accent)"/>
<text x="30" y="233" text-anchor="middle" font-weight="700" fill="var(--bg)">1</text>
<text x="48" y="228" font-size="11.5" font-weight="600" fill="var(--text)">VERBAL</text>
<text x="48" y="241" fill="var(--text-dim)">an external cue first (day 2)</text>
<rect x="20" y="249" width="20" height="20" rx="4" fill="var(--theme-accent)"/>
<text x="30" y="263" text-anchor="middle" font-weight="700" fill="var(--bg)">2</text>
<text x="48" y="258" font-size="11.5" font-weight="600" fill="var(--text)">VISUAL</text>
<text x="48" y="271" fill="var(--text-dim)">demo the fault AND the correct action</text>
<rect x="20" y="279" width="20" height="20" rx="4" fill="var(--theme-accent)"/>
<text x="30" y="293" text-anchor="middle" font-weight="700" fill="var(--bg)">3</text>
<text x="48" y="288" font-size="11.5" font-weight="600" fill="var(--text)">TACTILE</text>
<text x="48" y="301" fill="var(--text-dim)">touch target or adjustment - consent first</text>
<rect x="320" y="192" width="372" height="110" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="332" y="210" fill="var(--text-dim)">PROMOTION MEANS THE WHOLE BATTERY</text>
<rect x="332" y="218" width="84" height="22" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="374" y="233" text-anchor="middle" fill="var(--text-dim)">cardio</text>
<rect x="420" y="218" width="84" height="22" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="462" y="233" text-anchor="middle" fill="var(--text-dim)">strength</text>
<rect x="508" y="218" width="84" height="22" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="550" y="233" text-anchor="middle" fill="var(--text-dim)">standards</text>
<rect x="596" y="218" width="84" height="22" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="638" y="233" text-anchor="middle" fill="var(--text-dim)">time</text>
<rect x="332" y="250" width="150" height="26" rx="6" fill="var(--good)" fill-opacity="0.16" stroke="var(--good)"/>
<text x="407" y="267" text-anchor="middle" fill="var(--text)">deadlift 140% BW</text>
<text x="489" y="267" fill="var(--text-dimmer)">but</text>
<rect x="518" y="250" width="150" height="26" rx="6" fill="var(--bad)" fill-opacity="0.16" stroke="var(--bad)"/>
<text x="593" y="267" text-anchor="middle" fill="var(--text)">10 km in 58:00</text>
<text x="332" y="294" fill="var(--text)">fails the level 3-to-4 cardio gate, so: a LEVEL 3 athlete</text>
<text x="14" y="322" fill="var(--text-dim)">Dwell time is roughly logarithmic: weeks to months at level 1, about half a year at level 2, then years at the top.</text>
<text x="14" y="340" fill="var(--text-dim)">Level 5 adds supplemental high-skill work - overhead squat, toes-to-bar, double-unders - none of which is raced.</text>
</svg>'''
    return _wrap("dg-hp_movelib", "One movement, one ladder, one correction order", body,
                 "The library decides which variant the athlete has earned; the fault list is what trains the coach's eye.")


def d_st_framework():
    body = _SVG.format(h=348, tid="st_framework", label="One slow sled push read three ways - biomechanist, physiotherapist and strength coach - with the practical diagnostic order underneath") + '''
<rect x="250" y="10" width="200" height="30" rx="8" fill="var(--theme-accent)"/>
<text x="350" y="30" text-anchor="middle" font-size="13" font-weight="700" fill="var(--bg)">SLOW SLED PUSH</text>
<path d="M330,40 L119,72" stroke="var(--text-dim)" fill="none"/>
<path d="M350,40 L350,72" stroke="var(--text-dim)" fill="none"/>
<path d="M370,40 L581,72" stroke="var(--text-dim)" fill="none"/>
<path d="M114,66 L124,68 L118,76 Z" fill="var(--text-dim)"/>
<path d="M345,66 L355,66 L350,76 Z" fill="var(--text-dim)"/>
<path d="M576,68 L586,66 L582,76 Z" fill="var(--text-dim)"/>
<rect x="8" y="78" width="222" height="172" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="20" y="98" font-size="12" font-weight="700" fill="var(--theme-accent)">BIOMECHANIST</text>
<text x="20" y="118" fill="var(--text)">How is force produced,</text>
<text x="20" y="132" fill="var(--text)">and where does it leak?</text>
<line x1="20" y1="142" x2="218" y2="142" stroke="var(--border)"/>
<text x="20" y="158" fill="var(--text-dimmer)">THINKS IN</text>
<text x="20" y="174" fill="var(--text-dim)">sequencing, force vectors,</text>
<text x="20" y="188" fill="var(--text-dim)">moment arms, a neutral spine</text>
<text x="20" y="202" fill="var(--text-dim)">under load</text>
<text x="20" y="224" fill="var(--text)">verdict: the trunk yields -</text>
<text x="20" y="238" fill="var(--text)">force leaks before the sled</text>
<rect x="239" y="78" width="222" height="172" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="251" y="98" font-size="12" font-weight="700" fill="var(--theme-accent)">PHYSIOTHERAPIST</text>
<text x="251" y="118" fill="var(--text)">What is restricting</text>
<text x="251" y="132" fill="var(--text)">this athlete?</text>
<line x1="251" y1="142" x2="449" y2="142" stroke="var(--border)"/>
<text x="251" y="158" fill="var(--text-dimmer)">THINKS IN</text>
<text x="251" y="174" fill="var(--text-dim)">the limiter sits upstream of</text>
<text x="251" y="188" fill="var(--text-dim)">the complaint; a stiff thorax</text>
<text x="251" y="202" fill="var(--text-dim)">also caps rib-cage breathing</text>
<text x="251" y="224" fill="var(--text)">verdict: restricted hips</text>
<text x="251" y="238" fill="var(--text)">cannot pass on floor force</text>
<rect x="470" y="78" width="222" height="172" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="482" y="98" font-size="12" font-weight="700" fill="var(--theme-accent)">STRENGTH COACH</text>
<text x="482" y="118" fill="var(--text)">Which qualities underpin</text>
<text x="482" y="132" fill="var(--text)">this station?</text>
<line x1="482" y1="142" x2="680" y2="142" stroke="var(--border)"/>
<text x="482" y="158" fill="var(--text-dimmer)">THINKS IN</text>
<text x="482" y="174" fill="var(--text-dim)">max strength for the heavy</text>
<text x="482" y="188" fill="var(--text-dim)">stations, strength-endurance</text>
<text x="482" y="202" fill="var(--text-dim)">for repeats, elastic for a SSC</text>
<text x="482" y="224" fill="var(--text)">verdict: simply not strong</text>
<text x="482" y="238" fill="var(--text)">enough yet</text>
<text x="14" y="274" fill="var(--text-dim)">PRACTICAL DIAGNOSTIC ORDER</text>
<rect x="14" y="282" width="200" height="34" rx="6" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="26" y="298" font-weight="600" fill="var(--text)">1  rule out RESTRICTION</text>
<text x="26" y="311" fill="var(--text-dimmer)">it is the quickest thing to change</text>
<path d="M220,299 L242,299" stroke="var(--text-dim)" fill="none"/>
<path d="M238,294 L248,299 L238,304 Z" fill="var(--text-dim)"/>
<rect x="248" y="282" width="200" height="34" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="260" y="298" font-weight="600" fill="var(--text)">2  check SEQUENCING</text>
<text x="260" y="311" fill="var(--text-dimmer)">on video</text>
<path d="M454,299 L476,299" stroke="var(--text-dim)" fill="none"/>
<path d="M472,294 L482,299 L472,304 Z" fill="var(--text-dim)"/>
<rect x="482" y="282" width="200" height="34" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="494" y="298" font-weight="600" fill="var(--text)">3  treat it as a STRENGTH</text>
<text x="494" y="311" fill="var(--text-dimmer)">deficit</text>
<text x="14" y="338" fill="var(--text-dim)">Somatotype cuts all three: mesomorphs - rhythm and consistency; ectomorphs - trunk stiffness and sequencing.</text>
</svg>'''
    return _wrap("dg-st_framework", "One slow split, three possible causes", body,
                 "Diagnose before you prescribe - the wrong lens gives training that is sound and useless.")


def d_mp_pressure_sim():
    body = _SVG.format(h=348, tid="mp_pressure_sim", label="An inverted-U curve of transfer against stressor dose with too little, target and too much zones, a menu of stressor types, and the five-step debrief chain") + '''
<style>
.mp_pressure_sim-glow{animation:mp_pressure_sim-glow 6s ease-in-out infinite}
@keyframes mp_pressure_sim-glow{0%,100%{opacity:.10}50%{opacity:.26}}
@media (prefers-reduced-motion:reduce){.mp_pressure_sim-glow{animation:none;opacity:.18}}
</style>
<rect x="8" y="8" width="392" height="250" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="20" y="26" fill="var(--text-dim)">DOSING THE STRESSOR</text>
<rect x="44" y="40" width="106" height="164" fill="var(--text-dimmer)" fill-opacity="0.10"/>
<rect x="150" y="40" width="118" height="164" fill="var(--good)" class="dg-anim mp_pressure_sim-glow"/>
<rect x="268" y="40" width="122" height="164" fill="var(--bad)" fill-opacity="0.12"/>
<path d="M48,190 C90,180 120,90 152,72 C190,50 232,50 266,74 C300,100 330,168 386,192"
      fill="none" stroke="var(--theme-accent)" stroke-width="3" stroke-linecap="round"/>
<line x1="44" y1="204" x2="392" y2="204" stroke="var(--border)" stroke-width="2"/>
<line x1="44" y1="36" x2="44" y2="204" stroke="var(--border)" stroke-width="2"/>
<text x="26" y="122" text-anchor="middle" fill="var(--text-dim)" transform="rotate(-90 26 122)">transfer to race day</text>
<text x="97" y="220" text-anchor="middle" fill="var(--text-dim)">too little</text>
<text x="209" y="220" text-anchor="middle" font-weight="700" fill="var(--text)">TARGET</text>
<text x="329" y="220" text-anchor="middle" fill="var(--text-dim)">too much</text>
<text x="97" y="236" text-anchor="middle" fill="var(--text-dimmer)">no transfer</text>
<text x="209" y="236" text-anchor="middle" fill="var(--text-dimmer)">threatened, achievable</text>
<text x="329" y="236" text-anchor="middle" fill="var(--text-dimmer)">collapse is learned</text>
<text x="217" y="252" text-anchor="middle" fill="var(--text-dim)">stressor dose &#8594; (added, then progressed across the block)</text>
<rect x="412" y="8" width="280" height="250" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="424" y="26" fill="var(--text-dim)">STRESSOR MENU</text>
<rect x="424" y="36" width="126" height="26" rx="6" fill="var(--theme-accent)" fill-opacity="0.18" stroke="var(--theme-accent)"/>
<text x="487" y="53" text-anchor="middle" fill="var(--text)">consequence</text>
<rect x="558" y="36" width="126" height="26" rx="6" fill="var(--theme-accent)" fill-opacity="0.18" stroke="var(--theme-accent)"/>
<text x="621" y="53" text-anchor="middle" fill="var(--text)">evaluation</text>
<rect x="424" y="70" width="126" height="26" rx="6" fill="var(--theme-accent)" fill-opacity="0.18" stroke="var(--theme-accent)"/>
<text x="487" y="87" text-anchor="middle" fill="var(--text)">audience</text>
<rect x="558" y="70" width="126" height="26" rx="6" fill="var(--theme-accent)" fill-opacity="0.18" stroke="var(--theme-accent)"/>
<text x="621" y="87" text-anchor="middle" fill="var(--text)">uncertainty</text>
<rect x="424" y="104" width="126" height="26" rx="6" fill="var(--theme-accent)" fill-opacity="0.18" stroke="var(--theme-accent)"/>
<text x="487" y="121" text-anchor="middle" fill="var(--text)">fatigue</text>
<rect x="558" y="104" width="126" height="26" rx="6" fill="var(--theme-accent)" fill-opacity="0.18" stroke="var(--theme-accent)"/>
<text x="621" y="121" text-anchor="middle" fill="var(--text)">time constraint</text>
<text x="424" y="152" fill="var(--text-dim)">Uncertainty is cheap and potent: withhold the</text>
<text x="424" y="166" fill="var(--text-dim)">session details until the warm-up.</text>
<text x="424" y="188" fill="var(--text-dim)">Simulate specifics, not just intensity:</text>
<text x="424" y="202" fill="var(--text-dim)">race timing, start protocol, station order,</text>
<text x="424" y="216" fill="var(--text-dim)">transitions, kit, even nutrition.</text>
<text x="424" y="238" fill="var(--text-dim)">Full sims cost recovery - schedule them as</text>
<text x="424" y="252" fill="var(--text-dim)">key sessions, not extras.</text>
<text x="14" y="278" fill="var(--text-dim)">DEBRIEF - the part most coaches skip, and the part that carries the learning</text>
<rect x="15" y="286" width="118" height="42" rx="6" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="74" y="303" text-anchor="middle" font-weight="700" fill="var(--text)">DOWN-REGULATE</text>
<text x="74" y="318" text-anchor="middle" fill="var(--text-dimmer)">breathing, body scan</text>
<path d="M137,307 L145,307" stroke="var(--text-dim)" fill="none"/>
<path d="M145,302 L153,307 L145,312 Z" fill="var(--text-dim)"/>
<rect x="153" y="286" width="118" height="42" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="212" y="303" text-anchor="middle" font-weight="700" fill="var(--text)">WHAT YOU</text>
<text x="212" y="318" text-anchor="middle" fill="var(--text-dim)">NOTICED</text>
<path d="M275,307 L283,307" stroke="var(--text-dim)" fill="none"/>
<path d="M283,302 L291,307 L283,312 Z" fill="var(--text-dim)"/>
<rect x="291" y="286" width="118" height="42" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="350" y="303" text-anchor="middle" font-weight="700" fill="var(--text)">WHAT YOU</text>
<text x="350" y="318" text-anchor="middle" fill="var(--text-dim)">DID</text>
<path d="M413,307 L421,307" stroke="var(--text-dim)" fill="none"/>
<path d="M421,302 L429,307 L421,312 Z" fill="var(--text-dim)"/>
<rect x="429" y="286" width="118" height="42" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="488" y="303" text-anchor="middle" font-weight="700" fill="var(--text)">WHAT</text>
<text x="488" y="318" text-anchor="middle" fill="var(--text-dim)">WORKED</text>
<path d="M551,307 L559,307" stroke="var(--text-dim)" fill="none"/>
<path d="M559,302 L567,307 L559,312 Z" fill="var(--text-dim)"/>
<rect x="567" y="286" width="118" height="42" rx="6" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="626" y="303" text-anchor="middle" font-weight="700" fill="var(--text)">ONE CHANGE</text>
<text x="626" y="318" text-anchor="middle" fill="var(--text-dimmer)">for next time</text>
<text x="14" y="344" fill="var(--text-dimmer)">Down-shifting back to baseline is training in itself - teaching the system to return is as coachable as driving it up.</text>
</svg>'''
    return _wrap("dg-mp_pressure_sim", "Pressure has a dose, and a debrief", body,
                 "Enough pressure to threaten execution, little enough that success is still possible.")


def d_rb_compromised_tech():
    body = _SVG.format(h=348, tid="rb_compromised_tech", label="The station to roxzone to first 200 metres sequence, the typical fatigue signature, and the self-feeding fault chain drawn as a clockwise loop") + '''
<style>
.rb_compromised_tech-flow{stroke-dasharray:9 7;animation:rb_compromised_tech-flow 3.2s linear infinite}
@keyframes rb_compromised_tech-flow{to{stroke-dashoffset:-32}}
@media (prefers-reduced-motion:reduce){.rb_compromised_tech-flow{animation:none;stroke-dasharray:none}}
</style>
<text x="14" y="26" fill="var(--text-dim)">OUT OF THE STATION</text>
<rect x="14" y="36" width="320" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="26" y="56" fill="var(--text)">STATION - leaves its own mechanical debt</text>
<path d="M164,68 L176,68 L170,73 Z" fill="var(--text-dimmer)"/>
<rect x="14" y="74" width="320" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="26" y="94" fill="var(--text)">ROXZONE - clock never stops; walk with purpose</text>
<path d="M164,106 L176,106 L170,111 Z" fill="var(--text-dimmer)"/>
<rect x="14" y="112" width="320" height="30" rx="6" fill="var(--surface-2)" stroke="var(--theme-accent)"/>
<text x="26" y="132" fill="var(--text)">FIRST 100-200 m - re-patterning, not passing</text>
<path d="M164,144 L176,144 L170,149 Z" fill="var(--text-dimmer)"/>
<rect x="14" y="150" width="320" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="26" y="170" fill="var(--text)">SETTLED - once cadence and breathing steady</text>
<text x="14" y="206" fill="var(--text-dim)">TYPICAL FATIGUE SIGNATURE</text>
<text x="14" y="226" font-size="12" fill="var(--text)">lower cadence / longer ground contact</text>
<text x="14" y="242" font-size="12" fill="var(--text)">more trunk flexion / often more pelvic drop</text>
<text x="14" y="262" font-size="12" font-weight="700" fill="var(--bad)">= overstride with a braking heel strike</text>
<text x="14" y="290" font-weight="700" fill="var(--text)">CADENCE IS THE FASTEST LEVER</text>
<text x="14" y="306" fill="var(--text-dim)">Hold the habitual cadence as pace drops: shorter</text>
<text x="14" y="320" fill="var(--text-dim)">stride, less braking, less peak force from tired legs.</text>
<text x="14" y="340" fill="var(--text-dimmer)">Which station hurts most is individual - measure it, do not assume.</text>
<rect x="350" y="8" width="342" height="332" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="362" y="28" fill="var(--text-dim)">THE FAULT CHAIN, ONCE IT STARTS</text>
<g class="dg-anim rb_compromised_tech-flow" fill="none" stroke="var(--theme-accent)" stroke-width="2.5">
<path d="M521.6,101.8 A80,80 0 0 1 574.3,140"/>
<path d="M584.6,171.6 A80,80 0 0 1 564.4,233.5"/>
<path d="M537.5,253.1 A80,80 0 0 1 472.5,253.1"/>
<path d="M445.6,233.5 A80,80 0 0 1 425.4,171.6"/>
<path d="M435.7,140 A80,80 0 0 1 488.4,101.8"/>
</g>
<path d="M0,-4 L9,0 L0,4 Z" fill="var(--theme-accent)" transform="translate(574.3,140) rotate(60)"/>
<path d="M0,-4 L9,0 L0,4 Z" fill="var(--theme-accent)" transform="translate(564.4,233.5) rotate(132)"/>
<path d="M0,-4 L9,0 L0,4 Z" fill="var(--theme-accent)" transform="translate(472.5,253.1) rotate(204)"/>
<path d="M0,-4 L9,0 L0,4 Z" fill="var(--theme-accent)" transform="translate(425.4,171.6) rotate(276)"/>
<path d="M0,-4 L9,0 L0,4 Z" fill="var(--theme-accent)" transform="translate(488.4,101.8) rotate(348)"/>
<circle cx="505" cy="100" r="8" fill="var(--bad)"/>
<circle cx="581" cy="155" r="8" fill="var(--theme-accent)"/>
<circle cx="552" cy="245" r="8" fill="var(--theme-accent)"/>
<circle cx="458" cy="245" r="8" fill="var(--theme-accent)"/>
<circle cx="429" cy="155" r="8" fill="var(--theme-accent)"/>
<text x="505" y="84" text-anchor="middle" font-weight="700" fill="var(--bad)">quad fatigue</text>
<text x="596" y="152" fill="var(--text)">less knee flexion</text>
<text x="596" y="166" fill="var(--text)">in swing</text>
<text x="552" y="272" text-anchor="middle" fill="var(--text)">overstride</text>
<text x="458" y="272" text-anchor="middle" fill="var(--text)">more braking impulse</text>
<text x="418" y="152" text-anchor="end" fill="var(--text)">higher energy</text>
<text x="418" y="166" text-anchor="end" fill="var(--text)">cost</text>
<text x="505" y="176" text-anchor="middle" fill="var(--text-dim)">SELF-FEEDING</text>
<text x="505" y="192" text-anchor="middle" fill="var(--text-dimmer)">it does not stop on its own</text>
<text x="362" y="312" fill="var(--text-dim)">Compromised running is trainable: general aerobic and</text>
<text x="362" y="328" fill="var(--text-dim)">strength-endurance work, plus station-to-run rehearsal.</text>
</svg>'''
    return _wrap("dg-rb_compromised_tech", "The first 200 m out of the roxzone", body,
                 "Restore posture and cadence before you restore speed - the chain feeds itself otherwise.")


def d_pe_load_mgmt():
    body = _SVG.format(h=348, tid="pe_load_mgmt", label="Soreness, niggle and injury defined, a pain traffic light from 0 to 10, the DOMS timeline and the 24-hour response rule") + '''
<rect x="8" y="8" width="222" height="58" rx="6" fill="var(--good)" fill-opacity="0.12" stroke="var(--good)"/>
<text x="20" y="28" font-size="11.5" font-weight="700" fill="var(--text)">SORENESS</text>
<text x="20" y="44" fill="var(--text-dim)">diffuse, bilateral, symmetrical</text>
<text x="20" y="58" fill="var(--text-dim)">eases with warm-up</text>
<rect x="239" y="8" width="222" height="58" rx="6" fill="var(--warn)" fill-opacity="0.12" stroke="var(--warn)"/>
<text x="251" y="28" font-size="11.5" font-weight="700" fill="var(--text)">NIGGLE</text>
<text x="251" y="44" fill="var(--text-dim)">focal, reproducible on one</text>
<text x="251" y="58" fill="var(--text-dim)">movement, no loss of quality</text>
<rect x="470" y="8" width="222" height="58" rx="6" fill="var(--bad)" fill-opacity="0.12" stroke="var(--bad)"/>
<text x="482" y="28" font-size="11.5" font-weight="700" fill="var(--text)">INJURY</text>
<text x="482" y="44" fill="var(--text-dim)">sharp or night pain, swelling,</text>
<text x="482" y="58" fill="var(--text-dim)">giving way, a change in gait</text>
<text x="14" y="90" fill="var(--text-dim)">TRAFFIC LIGHT - what the in-session pain score buys you</text>
<rect x="30" y="98" width="145" height="24" fill="var(--good)" fill-opacity="0.45" stroke="var(--border)"/>
<rect x="175" y="98" width="174" height="24" fill="var(--warn)" fill-opacity="0.45" stroke="var(--border)"/>
<rect x="349" y="98" width="261" height="24" fill="var(--bad)" fill-opacity="0.45" stroke="var(--border)"/>
<text x="30" y="138" text-anchor="middle" fill="var(--text-dimmer)">0</text>
<text x="146" y="138" text-anchor="middle" fill="var(--text-dimmer)">2</text>
<text x="204" y="138" text-anchor="middle" fill="var(--text-dimmer)">3</text>
<text x="320" y="138" text-anchor="middle" fill="var(--text-dimmer)">5</text>
<text x="610" y="138" text-anchor="middle" fill="var(--text-dimmer)">10</text>
<text x="626" y="115" fill="var(--text-dimmer)">pain / 10</text>
<rect x="30" y="152" width="12" height="12" rx="3" fill="var(--good)"/>
<text x="50" y="162" fill="var(--text)">GREEN 0-2/10, no loss of function - train as planned, monitor</text>
<rect x="30" y="174" width="12" height="12" rx="3" fill="var(--warn)"/>
<text x="50" y="184" fill="var(--text)">AMBER 3-5/10, technique intact - modify ONE variable (volume, intensity, impact, range), keep the intent</text>
<rect x="30" y="196" width="12" height="12" rx="3" fill="var(--bad)"/>
<text x="50" y="206" fill="var(--text)">RED over 5/10, or limp, swelling, night pain - stop the aggravating stimulus and refer</text>
<text x="14" y="238" fill="var(--text-dim)">DOMS TIMELINE</text>
<line x1="30" y1="266" x2="430" y2="266" stroke="var(--border)" stroke-width="2"/>
<rect x="58" y="256" width="29" height="10" fill="var(--warn)" fill-opacity="0.5"/>
<rect x="87" y="250" width="114" height="16" fill="var(--bad)" fill-opacity="0.4"/>
<rect x="315" y="256" width="114" height="10" fill="var(--good)" fill-opacity="0.5"/>
<text x="110" y="244" fill="var(--text)">peaks 24-72 h</text>
<text x="315" y="244" fill="var(--text)">resolves 5-7 d</text>
<text x="58" y="296" fill="var(--text)">onset 12-24 h</text>
<text x="30" y="280" text-anchor="middle" fill="var(--text-dimmer)">0</text>
<text x="201" y="280" text-anchor="middle" fill="var(--text-dimmer)">3 d</text>
<text x="315" y="280" text-anchor="middle" fill="var(--text-dimmer)">5 d</text>
<text x="429" y="280" text-anchor="middle" fill="var(--text-dimmer)">7 d</text>
<text x="160" y="296" fill="var(--text-dimmer)">still worsening after a week = reassess, not push</text>
<rect x="450" y="228" width="242" height="76" rx="6" fill="var(--surface-2)" stroke="var(--theme-accent)"/>
<text x="462" y="248" font-weight="700" fill="var(--text)">24-HOUR RESPONSE RULE</text>
<text x="462" y="266" fill="var(--text-dim)">symptoms may rise during a session,</text>
<text x="462" y="280" fill="var(--text-dim)">but must be back to baseline by the</text>
<text x="462" y="294" fill="var(--text-dim)">next morning - or the load was too high.</text>
<rect x="8" y="312" width="684" height="30" rx="6" fill="var(--bad)" fill-opacity="0.12" stroke="var(--bad)"/>
<circle cx="26" cy="327" r="6" fill="var(--bad)"/>
<text x="42" y="331" fill="var(--text)">RED FLAG: focal, point-tender bone pain, worse with each impact and on single-leg hopping - refer, no trial.</text>
</svg>'''
    return _wrap("dg-pe_load_mgmt", "Triage first, then the traffic light", body,
                 "Coaches triage, they do not diagnose - modify the stimulus, keep the intent, refer the red.")


def d_pc_individualize():
    body = _SVG.format(h=348, tid="pc_individualize", label="Building the training week backwards from ranked limiters, the aerobic intensity distribution, and three progression weeks followed by a deload") + '''
<rect x="8" y="8" width="344" height="270" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="20" y="26" fill="var(--text-dim)">BUILD THE WEEK BACKWARDS</text>
<rect x="20" y="36" width="320" height="76" rx="6" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="32" y="54" font-size="12" font-weight="700" fill="var(--text)">1  RANK LIMITERS BY MINUTES LOST</text>
<text x="32" y="70" fill="var(--text-dim)">not by what feels weakest - compare their station</text>
<text x="32" y="84" fill="var(--text-dim)">splits and roxzone time against division benchmarks</text>
<text x="32" y="102" fill="var(--text-dimmer)">running is usually the biggest single time block</text>
<path d="M174,112 L174,120" stroke="var(--text-dim)" fill="none"/>
<path d="M169,118 L179,118 L174,124 Z" fill="var(--text-dim)"/>
<rect x="20" y="126" width="320" height="88" rx="6" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="32" y="144" font-size="12" font-weight="700" fill="var(--text)">2  LOCK THE FOUR NON-NEGOTIABLES</text>
<text x="32" y="160" fill="var(--text)">1 compromised run (run - station - run)</text>
<text x="32" y="174" fill="var(--text)">1 aerobic long run</text>
<text x="32" y="188" fill="var(--text)">1 heavy lower-body strength day</text>
<text x="32" y="202" fill="var(--text)">1 grip / carry plus pull exposure</text>
<path d="M174,214 L174,222" stroke="var(--text-dim)" fill="none"/>
<path d="M169,220 L179,220 L174,226 Z" fill="var(--text-dim)"/>
<rect x="20" y="228" width="320" height="42" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="32" y="246" font-size="12" font-weight="700" fill="var(--text)">3  EVERYTHING ELSE IS OPTIONAL</text>
<text x="32" y="262" fill="var(--text-dim)">discretionary volume, scaled to real availability</text>
<rect x="364" y="8" width="328" height="270" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="376" y="26" fill="var(--text-dim)">TWO DIALS ON THE TEMPLATE</text>
<text x="376" y="50" font-weight="600" fill="var(--text)">AEROBIC DISTRIBUTION</text>
<rect x="376" y="58" width="228" height="24" fill="var(--theme-accent)" fill-opacity="0.30" stroke="var(--border)"/>
<rect x="604" y="58" width="76" height="24" fill="var(--warn)" fill-opacity="0.45" stroke="var(--border)"/>
<text x="376" y="98" fill="var(--text)">70-80% low intensity</text>
<text x="680" y="98" text-anchor="end" fill="var(--text)">20-30% mod-hard</text>
<text x="376" y="118" fill="var(--text-dimmer)">race-specific compromised work sits in the hard</text>
<text x="376" y="132" fill="var(--text-dimmer)">bucket - cap it at 1-2 sessions a week.</text>
<text x="376" y="158" font-weight="600" fill="var(--text)">PROGRESS, THEN DELOAD</text><text x="374" y="212" text-anchor="middle" fill="var(--text-dimmer)" transform="rotate(-90 374 212)">weekly volume</text>
<line x1="384" y1="250" x2="616" y2="250" stroke="var(--border)" stroke-width="2"/>
<rect x="390" y="190" width="40" height="60" fill="var(--theme-accent)" fill-opacity="0.45"/>
<rect x="450" y="186" width="40" height="64" fill="var(--theme-accent)" fill-opacity="0.45"/>
<rect x="510" y="182" width="40" height="68" fill="var(--theme-accent)" fill-opacity="0.45"/>
<rect x="570" y="218" width="40" height="32" fill="var(--warn)" fill-opacity="0.5"/>
<text x="410" y="184" text-anchor="middle" fill="var(--text-dimmer)">base</text>
<text x="470" y="180" text-anchor="middle" fill="var(--text-dimmer)">+5-10%</text>
<text x="530" y="176" text-anchor="middle" fill="var(--text-dimmer)">+5-10%</text>
<text x="590" y="212" text-anchor="middle" fill="var(--text-dimmer)">40-60%</text>
<text x="410" y="264" text-anchor="middle" fill="var(--text-dim)">wk 1</text>
<text x="470" y="264" text-anchor="middle" fill="var(--text-dim)">wk 2</text>
<text x="530" y="264" text-anchor="middle" fill="var(--text-dim)">wk 3</text>
<text x="590" y="264" text-anchor="middle" fill="var(--text-dim)">wk 4</text>
<line x1="384" y1="200" x2="616" y2="200" stroke="var(--good)" stroke-width="2" stroke-dasharray="4 4"/>
<text x="622" y="198" fill="var(--good)">intensity</text>
<text x="622" y="212" fill="var(--good)">retained</text>
<text x="376" y="274" fill="var(--text-dimmer)">Reassess every 3-4 weeks on a repeated benchmark.</text>
<rect x="8" y="286" width="222" height="58" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="20" y="304" font-weight="700" fill="var(--text)">RUNNER-TYPE</text>
<text x="20" y="320" fill="var(--text-dim)">more strength and station</text>
<text x="20" y="334" fill="var(--text-dim)">density; keep 2 easy runs</text>
<rect x="239" y="286" width="222" height="58" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="251" y="304" font-weight="700" fill="var(--text)">STRENGTH-TYPE</text>
<text x="251" y="320" fill="var(--text-dim)">more aerobic base; cap heavy</text>
<text x="251" y="334" fill="var(--text-dim)">lifting at 2; less hypertrophy</text>
<rect x="470" y="286" width="222" height="58" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="482" y="304" font-weight="700" fill="var(--text)">TIME-POOR (4-5 h/wk)</text>
<text x="482" y="320" fill="var(--text-dim)">merge qualities - drop</text>
<text x="482" y="334" fill="var(--text-dim)">isolation, not specificity</text>
</svg>'''
    return _wrap("dg-pc_individualize", "From limiter ranking to a weekly template", body,
                 "Allocate sessions to the biggest leak first - strength serves the stations, not the mirror.")


def d_rb_footsep():
    body = _SVG.format(h=356, tid="rb_footsep", label="Runner and jogger stick figures at touchdown, comparing wide and narrow foot separation") + '''
<text x="160" y="28" text-anchor="middle" font-size="13" font-weight="700" fill="var(--theme-accent)">RUNNER</text>
<text x="160" y="44" text-anchor="middle" fill="var(--text-dim)">wide separation at touchdown</text>
<text x="500" y="28" text-anchor="middle" font-size="13" font-weight="700" fill="var(--text-dim)">JOGGER</text>
<text x="500" y="44" text-anchor="middle" fill="var(--text-dim)">narrow separation, low heel recovery</text>
<line x1="20" y1="246" x2="680" y2="246" stroke="var(--border)" stroke-width="2"/>
<line x1="350" y1="60" x2="350" y2="300" stroke="var(--border)" stroke-dasharray="4 6"/>
<g stroke="var(--theme-accent)" stroke-width="3.5" stroke-linecap="round" fill="none">
<path d="M156,158 L164,106"/>
<path d="M156,158 L192,196 L214,244"/>
<path d="M156,158 L124,180 L104,148"/>
<path d="M164,106 L140,132 L120,120"/>
<path d="M164,106 L190,132 L206,116"/>
</g>
<circle cx="167" cy="92" r="11" fill="var(--theme-accent)"/>
<text x="96" y="70" text-anchor="middle" fill="var(--text)">heel recovers high</text>
<path d="M100,76 L108,140" stroke="var(--text-dim)" stroke-dasharray="3 3" fill="none"/>
<text x="248" y="122" fill="var(--text)">trailing hip</text>
<text x="248" y="136" fill="var(--text)">still extended</text>
<path d="M244,130 L140,172" stroke="var(--text-dim)" stroke-dasharray="3 3" fill="none"/>
<line x1="104" y1="152" x2="104" y2="258" stroke="var(--text-dimmer)" stroke-dasharray="3 4"/>
<line x1="214" y1="248" x2="214" y2="258" stroke="var(--text-dimmer)" stroke-dasharray="3 4"/>
<line x1="104" y1="262" x2="214" y2="262" stroke="var(--theme-accent)" stroke-width="2"/>
<line x1="104" y1="256" x2="104" y2="268" stroke="var(--theme-accent)" stroke-width="2"/>
<line x1="214" y1="256" x2="214" y2="268" stroke="var(--theme-accent)" stroke-width="2"/>
<text x="159" y="284" text-anchor="middle" font-size="12" font-weight="700" fill="var(--text)">wide separation</text>
<text x="159" y="300" text-anchor="middle" fill="var(--text-dim)">real flight time, elastic recoil</text>
<g stroke="var(--text-dim)" stroke-width="3.5" stroke-linecap="round" fill="none">
<path d="M496,160 L498,108"/>
<path d="M496,160 L512,198 L520,244"/>
<path d="M496,160 L482,198 L470,242"/>
<path d="M498,108 L476,132 L462,124"/>
<path d="M498,108 L518,132 L532,126"/>
</g>
<circle cx="500" cy="94" r="11" fill="var(--text-dim)"/>
<text x="500" y="70" text-anchor="middle" fill="var(--text)">low heel recovery, minimal flight</text>
<line x1="470" y1="246" x2="470" y2="258" stroke="var(--text-dimmer)" stroke-dasharray="3 4"/>
<line x1="520" y1="248" x2="520" y2="258" stroke="var(--text-dimmer)" stroke-dasharray="3 4"/>
<line x1="470" y1="262" x2="520" y2="262" stroke="var(--text-dim)" stroke-width="2"/>
<line x1="470" y1="256" x2="470" y2="268" stroke="var(--text-dim)" stroke-width="2"/>
<line x1="520" y1="256" x2="520" y2="268" stroke="var(--text-dim)" stroke-width="2"/>
<text x="495" y="284" text-anchor="middle" font-size="12" font-weight="700" fill="var(--text)">narrow separation</text>
<text x="495" y="300" text-anchor="middle" fill="var(--text-dim)">stepping, not springing</text>
<text x="20" y="322" fill="var(--text)">Separation is an OUTPUT of hip extension and leg stiffness - never manufacture it by reaching further forward.</text>
<text x="20" y="338" fill="var(--text-dim)">Levers: hip extension range / stiffness and plyometric work / strides and hill sprints. Cue: heel to the back pocket.</text>
<text x="20" y="352" fill="var(--text-dimmer)">Measure it: side-on video, one freeze at touchdown, athlete against their own past. It collapses first under fatigue.</text>
</svg>'''
    return _wrap("dg-rb_footsep", "Foot separation at touchdown", body,
                 "A lab-free window onto hip extension and elasticity - it improves only when those do.")


def d_nu_plantbased():
    body = _SVG.format(h=348, tid="nu_plantbased", label="Haem versus non-haem iron absorption, the other nutrients a plant-based plan must cover, and the low energy availability risk") + '''
<rect x="8" y="8" width="300" height="254" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="20" y="26" fill="var(--text-dim)">IRON - THE HEADLINE RISK</text>
<text x="24" y="46" fill="var(--text)">haem iron (animal foods)</text>
<rect x="24" y="52" width="264" height="14" rx="3" fill="var(--theme-accent)" fill-opacity="0.45"/>
<text x="24" y="86" fill="var(--text)">non-haem iron (plants)</text>
<rect x="24" y="92" width="86" height="14" rx="3" fill="var(--theme-accent)" fill-opacity="0.45"/>
<text x="118" y="103" fill="var(--text-dim)">far less bioavailable</text>
<text x="24" y="122" fill="var(--text-dimmer)">relative absorption, schematic and not to scale</text>
<text x="24" y="148" font-weight="700" fill="var(--text)">AT THE SAME MEAL</text>
<circle cx="30" cy="164" r="6" fill="var(--good)"/>
<text x="44" y="168" fill="var(--text)">vitamin C RAISES non-haem uptake</text>
<circle cx="30" cy="186" r="6" fill="var(--bad)"/>
<text x="44" y="190" fill="var(--text)">tea, coffee, calcium INHIBIT it</text>
<text x="24" y="216" fill="var(--text-dim)">Deficiency impairs endurance well before</text>
<text x="24" y="230" fill="var(--text-dim)">anaemia appears - screen symptomatic</text>
<text x="24" y="244" fill="var(--text-dim)">athletes, do not wait for haemoglobin to fall.</text>
<rect x="320" y="8" width="372" height="254" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="332" y="26" fill="var(--text-dim)">THE OTHER GAPS TO PLAN FOR</text>
<text x="332" y="52" font-weight="700" fill="var(--bad)">B12</text>
<text x="440" y="52" fill="var(--text)">supplement or fortified foods -</text>
<text x="440" y="66" fill="var(--text-dim)">non-negotiable for vegans</text>
<text x="332" y="90" font-weight="700" fill="var(--text)">PROTEIN</text>
<text x="440" y="90" fill="var(--text)">higher total intake; lower in leucine,</text>
<text x="440" y="104" fill="var(--text-dim)">less digestible - pair legumes with grains</text>
<text x="332" y="128" font-weight="700" fill="var(--text)">OMEGA-3</text>
<text x="440" y="128" fill="var(--text)">plant ALA converts poorly to EPA/DHA</text>
<text x="440" y="142" fill="var(--text-dim)">an algae supplement is the practical route</text>
<text x="332" y="166" font-weight="700" fill="var(--text)">CALCIUM + D</text>
<text x="440" y="166" fill="var(--text)">bone health alongside running volume</text>
<text x="440" y="180" fill="var(--text-dim)">fortified plant milks cover most cases</text>
<text x="332" y="204" font-weight="700" fill="var(--text)">ZINC + IODINE</text>
<text x="440" y="204" fill="var(--text)">frequently under-consumed; iodine</text>
<text x="440" y="218" fill="var(--text-dim)">especially where iodised salt is not used</text>
<line x1="332" y1="228" x2="680" y2="228" stroke="var(--border)"/>
<text x="332" y="242" font-weight="700" fill="var(--good)">NOT A GAP -</text>
<text x="332" y="256" font-weight="700" fill="var(--good)">AN OPPORTUNITY</text>
<text x="440" y="242" fill="var(--text)">CREATINE / BETA-ALANINE stores tend to be</text>
<text x="440" y="256" fill="var(--text-dim)">lower, so a larger relative benefit than in omnivores</text>
<rect x="8" y="270" width="430" height="74" rx="6" fill="var(--warn)" fill-opacity="0.10" stroke="var(--warn)"/>
<text x="22" y="292" font-weight="700" fill="var(--text)">THE QUIET PROBLEM</text>
<text x="22" y="312" fill="var(--text-dim)">High fibre and high food volume make it hard to eat enough energy -</text>
<text x="22" y="330" fill="var(--text-dim)">a route into low energy availability that looks like discipline.</text>
<rect x="452" y="270" width="240" height="74" rx="6" fill="var(--theme-accent)" fill-opacity="0.10" stroke="var(--theme-accent)"/>
<text x="466" y="292" font-weight="700" fill="var(--text)">REFER EARLY</text>
<text x="466" y="312" fill="var(--text-dim)">Dietitian for a new or struggling</text>
<text x="466" y="330" fill="var(--text-dim)">athlete; screen iron, B12, vit D.</text>
</svg>'''
    return _wrap("dg-nu_plantbased", "The eight gaps a plant-based plan must close", body,
                 "Plant-based works when it is planned - iron is the performance risk, B12 the non-negotiable.")


def d_sm_longevity():
    body = _SVG.format(h=348, tid="sm_longevity", label="A graded inverse curve of all-cause mortality risk against cardiorespiratory fitness, beside the health case for the format and the risks that scale with how it is done") + '''
<rect x="8" y="8" width="344" height="248" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="20" y="26" fill="var(--text-dim)">THE DOSE-RESPONSE IS GRADED, NOT FLAT</text>
<rect x="48" y="40" width="102" height="174" fill="var(--good)" fill-opacity="0.14"/>
<line x1="44" y1="214" x2="344" y2="214" stroke="var(--border)" stroke-width="2"/>
<line x1="44" y1="36" x2="44" y2="214" stroke="var(--border)" stroke-width="2"/>
<path d="M48,54 C86,58 112,140 156,160 C210,184 268,196 336,200"
      fill="none" stroke="var(--theme-accent)" stroke-width="3" stroke-linecap="round"/>
<circle cx="60" cy="66" r="6" fill="var(--good)"/>
<text x="76" y="62" fill="var(--text)">deconditioned beginner:</text>
<text x="76" y="76" fill="var(--text)">the biggest gain is here</text>
<circle cx="300" cy="197" r="6" fill="var(--text-dim)"/>
<text x="290" y="186" text-anchor="end" fill="var(--text-dim)">chasing a 5-min PB:</text>
<text x="290" y="172" text-anchor="end" fill="var(--text-dim)">smallest marginal gain</text>
<text x="26" y="125" text-anchor="middle" fill="var(--text-dim)" transform="rotate(-90 26 125)">all-cause mortality risk</text>
<text x="194" y="234" text-anchor="middle" fill="var(--text-dim)">cardiorespiratory fitness, rising</text>
<text x="20" y="250" fill="var(--text-dimmer)">Schematic shape of a graded inverse association.</text>
<rect x="364" y="8" width="328" height="248" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="376" y="26" fill="var(--text-dim)">WHY THE FORMAT IS A HEALTH DOSE</text>
<rect x="376" y="36" width="304" height="26" rx="6" fill="var(--theme-accent)" fill-opacity="0.20" stroke="var(--theme-accent)"/>
<text x="388" y="53" font-weight="700" fill="var(--text)">CARDIORESPIRATORY FITNESS</text>
<rect x="376" y="68" width="304" height="26" rx="6" fill="var(--theme-accent)" fill-opacity="0.20" stroke="var(--theme-accent)"/>
<text x="388" y="85" font-weight="700" fill="var(--text)">MUSCULAR STRENGTH</text>
<text x="376" y="112" fill="var(--text-dim)">Each is independently associated with lower</text>
<text x="376" y="126" fill="var(--text-dim)">all-cause mortality - and HYROX trains both.</text>
<rect x="376" y="140" width="56" height="22" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="404" y="155" text-anchor="middle" fill="var(--text-dim)">carry</text>
<rect x="438" y="140" width="56" height="22" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="466" y="155" text-anchor="middle" fill="var(--text-dim)">lunge</text>
<rect x="500" y="140" width="56" height="22" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="528" y="155" text-anchor="middle" fill="var(--text-dim)">push</text>
<rect x="562" y="140" width="56" height="22" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="590" y="155" text-anchor="middle" fill="var(--text-dim)">pull</text>
<rect x="624" y="140" width="56" height="22" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="652" y="155" text-anchor="middle" fill="var(--text-dim)">sit-stand</text>
<path d="M528,166 L528,180" stroke="var(--text-dim)" fill="none"/>
<path d="M523,178 L533,178 L528,184 Z" fill="var(--text-dim)"/>
<text x="528" y="198" text-anchor="middle" font-weight="700" fill="var(--text)">later-life independence</text>
<text x="376" y="220" fill="var(--text-dim)">Weight-bearing and resistance load keep bone</text>
<text x="376" y="234" fill="var(--text-dim)">mineral density up; the community keeps</text>
<text x="376" y="248" fill="var(--text-dim)">adherence up, and adherence decides outcomes.</text>
<rect x="8" y="260" width="684" height="46" rx="6" fill="var(--warn)" fill-opacity="0.10" stroke="var(--warn)"/>
<text x="22" y="277" font-weight="700" fill="var(--text)">RISKS SCALE WITH HOW IT IS DONE</text>
<text x="22" y="291" fill="var(--text-dim)">rapid load progression drives overuse injury / chasing performance drives RED-S and overtraining</text>
<text x="22" y="303" fill="var(--text-dim)">event-day cardiac events, though rare, cluster in older participants with undetected disease</text>
<rect x="8" y="310" width="684" height="34" rx="6" fill="var(--bad)" fill-opacity="0.12" stroke="var(--bad)"/>
<circle cx="26" cy="327" r="6" fill="var(--bad)"/>
<text x="42" y="331" fill="var(--text)">Screen older or previously inactive athletes. Chest pain, breathlessness or syncope on exertion - assess first, always.</text>
</svg>'''
    return _wrap("dg-sm_longevity", "Where the health return actually sits", body,
                 "Most clients are training for another twenty years, not a PB - protect the return by protecting them.")


def d_mp_neurodiversity():
    body = _SVG.format(h=348, tid="mp_neurodiversity", label="Ambiguous instructions contrasted with explicit ones, and the coaching adjustments that support neurodivergent athletes") + '''
<rect x="8" y="8" width="336" height="68" rx="6" fill="var(--bad)" fill-opacity="0.12" stroke="var(--bad)"/>
<text x="20" y="28" font-weight="700" fill="var(--bad)">AMBIGUOUS</text>
<text x="20" y="48" font-size="12" fill="var(--text)">just go a few rounds and</text>
<text x="20" y="64" font-size="12" fill="var(--text)">see how you feel</text>
<path d="M348,36 L356,42 L348,48 Z" fill="var(--text-dim)"/>
<rect x="364" y="8" width="328" height="68" rx="6" fill="var(--good)" fill-opacity="0.12" stroke="var(--good)"/>
<text x="376" y="28" font-weight="700" fill="var(--good)">LITERAL, SPECIFIC, SEQUENCED</text>
<text x="376" y="48" font-size="12" fill="var(--text)">three rounds: 10 wall balls,</text>
<text x="376" y="64" font-size="12" fill="var(--text)">200 m run, rest 90 seconds</text>
<rect x="8" y="86" width="336" height="170" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="20" y="106" font-weight="700" fill="var(--theme-accent)">REDUCE COGNITIVE LOAD</text>
<text x="20" y="128" fill="var(--text)">instructions that are literal, specific, sequenced</text>
<text x="20" y="150" fill="var(--text)">more than one channel - written or demonstrated</text>
<text x="20" y="164" fill="var(--text-dim)">as well as spoken; processing preferences differ</text>
<text x="20" y="186" fill="var(--text)">advance notice of any change to session, venue</text>
<text x="20" y="200" fill="var(--text-dim)">or timing - unannounced change is a big stressor</text>
<text x="20" y="222" fill="var(--text)">discrete chunks with a defined start and end</text>
<text x="20" y="244" fill="var(--text)">structure and scaffolding, never nagging: executive</text>
<text x="20" y="258" fill="var(--text-dim)">function is not effort and not motivation</text>
<rect x="364" y="86" width="328" height="170" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="376" y="106" font-weight="700" fill="var(--theme-accent)">REDUCE SENSORY LOAD</text>
<text x="376" y="128" fill="var(--text)">noise, echo, crowding, lighting and heat are real</text>
<text x="376" y="142" fill="var(--text-dim)">performance variables at a HYROX venue</text>
<text x="376" y="164" fill="var(--text)">plan arrival timing and warm-up location</text>
<text x="376" y="186" fill="var(--text)">consider ear defenders or noise-cancelling</text>
<text x="376" y="200" fill="var(--text-dim)">headphones</text>
<text x="376" y="222" fill="var(--text)">watch for masking - an athlete coping visibly</text>
<text x="376" y="236" fill="var(--text-dim)">well may still be depleting, and it hides distress</text>
<text x="376" y="258" fill="var(--text-dimmer)">Inclusive design mostly helps the whole group.</text>
<rect x="8" y="266" width="222" height="78" rx="6" fill="var(--surface)" stroke="var(--warn)"/>
<text x="20" y="286" font-weight="700" fill="var(--warn)">HYPERFOCUS</text>
<text x="20" y="304" fill="var(--text-dim)">drives exceptional consistency</text>
<text x="20" y="320" fill="var(--text-dim)">and also overrides fatigue:</text>
<text x="20" y="336" fill="var(--text-dim)">build explicit STOP RULES</text>
<rect x="239" y="266" width="222" height="78" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="251" y="286" font-weight="700" fill="var(--text)">ASK, DO NOT ASSUME</text>
<text x="251" y="304" fill="var(--text-dim)">self-reported accommodations</text>
<text x="251" y="320" fill="var(--text-dim)">beat any guess from a label.</text>
<text x="251" y="336" fill="var(--text-dim)">Use the athlete&#39;s own words.</text>
<rect x="470" y="266" width="222" height="78" rx="6" fill="var(--surface)" stroke="var(--bad)"/>
<text x="482" y="286" font-weight="700" fill="var(--bad)">SCOPE</text>
<text x="482" y="304" fill="var(--text-dim)">Coaches do not diagnose -</text>
<text x="482" y="320" fill="var(--text-dim)">accommodate, adjust, refer.</text>
<text x="482" y="336" fill="var(--text-dim)">Never disclose without consent.</text>
</svg>'''
    return _wrap("dg-mp_neurodiversity", "Design the environment, not the athlete", body,
                 "Accommodation and environment design - never deficit correction, and never diagnosis.")


def d_cm_communication():
    body = _SVG.format(h=348, tid="cm_communication", label="Where a cue points - external versus internal focus - and the feedback schedules that fade it as the skill consolidates") + '''
<style>
.cm_communication-flow{stroke-dasharray:10 6;animation:cm_communication-flow 2.6s linear infinite}
@keyframes cm_communication-flow{to{stroke-dashoffset:-32}}
@media (prefers-reduced-motion:reduce){.cm_communication-flow{animation:none;stroke-dasharray:none}}
</style>
<rect x="8" y="8" width="340" height="188" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="20" y="26" fill="var(--text-dim)">WHERE THE CUE POINTS</text>
<line x1="24" y1="150" x2="330" y2="150" stroke="var(--border)" stroke-width="2"/>
<rect x="26" y="106" width="8" height="44" fill="var(--theme-accent)" fill-opacity="0.5"/>
<text x="52" y="100" fill="var(--theme-accent)" font-weight="700">the far wall</text>
<rect x="96" y="120" width="44" height="30" rx="3" fill="var(--surface)" stroke="var(--text-dim)" stroke-width="2"/>
<g stroke="var(--text-dim)" stroke-width="3" stroke-linecap="round" fill="none">
<path d="M176,108 L158,84"/>
<path d="M176,108 L200,128 L212,150"/>
<path d="M176,108 L192,132 L176,150"/>
<path d="M158,84 L146,104 L142,124"/>
</g>
<circle cx="150" cy="74" r="9" fill="var(--text-dim)"/>
<path d="M92,133 L40,133" stroke="var(--theme-accent)" stroke-width="2.5" fill="none" class="dg-anim cm_communication-flow"/>
<path d="M46,128 L36,133 L46,138 Z" fill="var(--theme-accent)"/>
<path d="M232,72 L200,120" stroke="var(--bad)" stroke-width="2" stroke-dasharray="4 4" fill="none"/>
<circle cx="198" cy="124" r="4" fill="var(--bad)"/>
<text x="238" y="70" fill="var(--bad)" font-weight="700">INTERNAL</text>
<text x="20" y="170" fill="var(--text)">INTERNAL "drive through your quads" - a body part</text>
<text x="20" y="188" fill="var(--text)">EXTERNAL "push the far wall away" - an effect on the world</text>
<rect x="364" y="8" width="328" height="188" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="376" y="26" fill="var(--text-dim)">TWO KINDS OF FEEDBACK</text>
<text x="376" y="48" font-weight="700" fill="var(--text)">KR - knowledge of RESULTS</text>
<text x="376" y="62" fill="var(--text-dim)">the split, the reps, the distance</text>
<text x="376" y="76" fill="var(--text-dimmer)">usually free in HYROX: clock, erg monitor</text>
<text x="376" y="98" font-weight="700" fill="var(--text)">KP - knowledge of PERFORMANCE</text>
<text x="376" y="112" fill="var(--text-dim)">how it was produced: kinematics, sequencing</text>
<text x="376" y="126" fill="var(--theme-accent)">this is where the coach adds most value</text>
<text x="376" y="142" font-weight="700" fill="var(--text)">FADE IT (guidance hypothesis)</text>
<line x1="384" y1="182" x2="522" y2="182" stroke="var(--border)"/>
<rect x="384" y="150" width="34" height="32" fill="var(--theme-accent)" fill-opacity="0.45"/>
<rect x="432" y="166" width="34" height="16" fill="var(--theme-accent)" fill-opacity="0.45"/>
<rect x="480" y="174" width="34" height="8" fill="var(--theme-accent)" fill-opacity="0.45"/>
<text x="401" y="193" text-anchor="middle" fill="var(--text-dimmer)">100%</text>
<text x="449" y="193" text-anchor="middle" fill="var(--text-dimmer)">50%</text>
<text x="497" y="193" text-anchor="middle" fill="var(--text-dimmer)">25%</text>
<text x="530" y="162" fill="var(--text-dim)">high frequency raises</text>
<text x="530" y="176" fill="var(--text-dim)">acute performance and</text>
<text x="530" y="190" fill="var(--text-dim)">can impair retention</text>
<rect x="8" y="206" width="340" height="60" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="20" y="224" font-weight="700" fill="var(--text)">CONSTRAINED-ACTION HYPOTHESIS</text>
<text x="20" y="240" fill="var(--text-dim)">an internal focus imposes conscious control and disrupts</text>
<text x="20" y="256" fill="var(--text-dim)">automatic, self-organising motor processes - leading</text>
<text x="20" y="270" fill="var(--text-dim)">explanation, not a proven mechanism</text>
<rect x="364" y="206" width="328" height="60" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="376" y="224" font-weight="700" fill="var(--text)">OTHER FADING SCHEDULES</text>
<text x="376" y="240" fill="var(--text-dim)">summary / average, bandwidth (speak only when error</text>
<text x="376" y="256" fill="var(--text-dim)">exceeds tolerance), self-controlled (the athlete asks)</text>
<text x="14" y="292" fill="var(--text)">ONE cue per set, a handful of words, one focus at a time - information processing degrades under fatigue.</text>
<text x="14" y="312" fill="var(--text)">AUTONOMY-SUPPORTIVE: meaningful choice, a rationale, "you can..." - not "you must...".</text>
<text x="14" y="332" fill="var(--text)">LATE-RACE: one pre-agreed ANCHOR cue, rehearsed as self-talk - in a HYROX race the coach is not alongside.</text>
</svg>'''
    return _wrap("dg-cm_communication", "Where the cue points, and when to stop giving it", body,
                 "Coaching language is a motor-learning intervention: aim it outward, then fade it.")


def _hp_stations_row(cy, name, demand, split, cost, note):
    seg = ""
    if cost < 0:
        seg = ('<text x="444" y="%d" fill="var(--text-dim)">--</text>' % (cy + 4))
    else:
        for i in range(3):
            fill = "var(--theme-accent)" if i < cost else "var(--border)"
            seg += ('<rect x="%d" y="%d" width="26" height="10" rx="2" fill="%s"/>'
                    % (444 + i * 30, cy - 1, fill))
    return (
        '<text x="16" y="%d" fill="var(--theme-accent)">1 km</text>'
        '<text x="52" y="%d" font-size="11.5" fill="var(--text)">%s</text>'
        '<text x="208" y="%d" fill="var(--text-dim)">%s</text>'
        '<text x="342" y="%d" fill="var(--text)">%s</text>'
        '%s'
        '<text x="542" y="%d" fill="var(--text-dim)">%s</text>'
        % (cy + 4, cy + 4, name, cy + 4, demand, cy + 4, split, seg, cy + 4, note))


def d_hp_stations():
    rows = (
        (84, "SkiErg 1000 m", "lats, triceps, trunk", "4:00-5:00", 1, "low leg cost, early HR spike"),
        (118, "Sled push 50 m", "high-force leg drive", "1:00-3:00+", 3, "commonly the top disruptor"),
        (152, "Sled pull 50 m", "upper back and grip", "1:30-3:00", 2, "grip carries to the carry"),
        (186, "Burpee broad jump 80 m", "whole body, eccentric", "3:00-5:00", 3, "among the worst, with push"),
        (220, "Row 1000 m", "legs-back-arms drive", "3:45-4:30", 2, "concentric, non-impact"),
        (254, "Farmers carry 200 m", "grip, forearms, trunk", "1:30-2:15", 1, "least disruptive, not rest"),
        (288, "Sandbag lunges 100 m", "loaded unilateral range", "--", 3, "cramps, choppy final run"),
        (322, "Wall balls, 100 reps", "squat to front press", "4:00-7:00", -1, "the race ends here"),
    )
    body = _SVG.format(h=348, tid="hp_stations", label="A table of the eight stations with dominant demand, typical split, and a three-block scale for the cost each imposes on the next run")
    body += ('<text x="14" y="20" fill="var(--text-dim)">Fixed order: 8 runs of 1 km alternating with 8 stations. '
             'Aerobic overall - most stations sit at or above threshold.</text>')
    body += ('<text x="14" y="36" fill="var(--text-dim)">Roxzone (15 traverses) commonly 4-8 min for age-groupers, '
             'less for elites. Splits below are broad approximations.</text>')
    body += ('<text x="52" y="60" fill="var(--text-dimmer)">STATION</text>'
             '<text x="208" y="60" fill="var(--text-dimmer)">DOMINANT DEMAND</text>'
             '<text x="342" y="60" fill="var(--text-dimmer)">TYPICAL SPLIT</text>'
             '<text x="444" y="60" fill="var(--text-dimmer)">TYPICAL COST TO THE NEXT RUN</text>'
             '<text x="444" y="48" fill="var(--text-dimmer)">1 block = low cost, 3 = the top disruptors</text>'
             '<line x1="14" y1="64" x2="690" y2="64" stroke="var(--border)"/>'
             '<line x1="44" y1="70" x2="44" y2="332" stroke="var(--border)"/>')
    for cy, name, demand, split, cost, note in rows:
        body += _hp_stations_row(cy, name, demand, split, cost, note)
    body += ('<text x="14" y="345" fill="var(--text-dimmer)">-- = no typical split given for the lunges. '
             'Loads and standards vary by division and season - check the current rulebook.</text>')
    body += "</svg>"
    return _wrap("dg-hp_stations", "Eight ways to tax one aerobic engine", body,
                 "The real cost of a station is often paid on the kilometre that follows, not on its own clock.")


def d_mock_decisions():
    body = _SVG.format(h=350, tid="mock_decisions", label="Four plausible options filtered first by the safest defensible answer and then by individualisation, beside a verified panel and a working-assumption panel") + '''
<rect x="8" y="8" width="344" height="304" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="20" y="26" fill="var(--text-dim)">FOUR PLAUSIBLE OPTIONS</text>
<rect x="22" y="34" width="152" height="26" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="98" y="51" text-anchor="middle" fill="var(--text-dim)">looks right</text>
<rect x="186" y="34" width="152" height="26" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="262" y="51" text-anchor="middle" fill="var(--text-dim)">also looks right</text>
<rect x="22" y="66" width="152" height="26" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="98" y="83" text-anchor="middle" fill="var(--text-dim)">technically true</text>
<rect x="186" y="66" width="152" height="26" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="262" y="83" text-anchor="middle" fill="var(--text-dim)">what a coach would say</text>
<path d="M180,96 L180,112" stroke="var(--text-dim)" fill="none"/>
<path d="M175,110 L185,110 L180,118 Z" fill="var(--text-dim)"/>
<rect x="22" y="122" width="316" height="46" rx="6" fill="var(--theme-accent)" fill-opacity="0.14" stroke="var(--theme-accent)"/>
<text x="34" y="140" font-weight="700" fill="var(--text)">FILTER 1 - THE SAFEST DEFENSIBLE ANSWER</text>
<text x="34" y="158" fill="var(--text-dim)">refer out of scope / reduce load / protect the athlete</text>
<path d="M180,172 L180,184" stroke="var(--text-dim)" fill="none"/>
<path d="M175,182 L185,182 L180,190 Z" fill="var(--text-dim)"/>
<rect x="60" y="194" width="110" height="26" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="115" y="211" text-anchor="middle" fill="var(--text)">survivor A</text>
<rect x="192" y="194" width="110" height="26" rx="5" fill="var(--surface)" stroke="var(--border)"/>
<text x="247" y="211" text-anchor="middle" fill="var(--text)">survivor B</text>
<path d="M180,224 L180,236" stroke="var(--text-dim)" fill="none"/>
<path d="M175,234 L185,234 L180,242 Z" fill="var(--text-dim)"/>
<rect x="22" y="246" width="316" height="30" rx="6" fill="var(--theme-accent)" fill-opacity="0.14" stroke="var(--theme-accent)"/>
<text x="34" y="266" font-weight="700" fill="var(--text)">FILTER 2 - the one that INDIVIDUALISES</text>
<path d="M180,280 L180,290" stroke="var(--text-dim)" fill="none"/>
<path d="M175,288 L185,288 L180,296 Z" fill="var(--text-dim)"/>
<rect x="98" y="286" width="164" height="22" rx="6" fill="var(--theme-accent)"/>
<text x="180" y="301" text-anchor="middle" font-weight="700" fill="var(--bg)">CREDITED ANSWER</text>
<rect x="364" y="8" width="328" height="152" rx="8" fill="var(--good)" fill-opacity="0.08" stroke="var(--good)"/>
<circle cx="378" cy="24" r="6" fill="var(--good)"/>
<text x="394" y="28" font-weight="700" fill="var(--text)">VERIFIED</text>
<text x="376" y="52" fill="var(--text)">digital-only, self-paced, English-only</text>
<text x="376" y="72" fill="var(--text)">delivered on the HYROX365 LMS</text>
<text x="376" y="92" fill="var(--text)">Level 1 is the prerequisite</text>
<text x="376" y="112" fill="var(--text)">ten published, structured modules</text>
<text x="376" y="132" fill="var(--text)">navigation is strictly linear</text>
<text x="376" y="152" fill="var(--text-dimmer)">so you can never preview a quiz</text>
<rect x="364" y="170" width="328" height="142" rx="8" fill="var(--warn)" fill-opacity="0.08" stroke="var(--warn)"/>
<circle cx="378" cy="186" r="6" fill="var(--warn)"/>
<text x="394" y="190" font-weight="700" fill="var(--text)">WORKING ASSUMPTION - not published</text>
<text x="376" y="214" fill="var(--text)">about 40 hours: the LMS runtimes totalled by hand</text>
<text x="376" y="234" fill="var(--text)">a multiple-choice quiz after each module</text>
<text x="376" y="254" fill="var(--text)">roughly 10-20 questions, 80% pass mark</text>
<text x="376" y="274" fill="var(--text)">unlimited retakes, unchanged question set</text>
<text x="376" y="296" fill="var(--text-dimmer)">the last three observed first-hand on the Foundation</text>
<text x="376" y="308" fill="var(--text-dimmer)">Course; the 40 h is the Level 2 runtimes totalled by hand</text>
<text x="14" y="332" fill="var(--text)">Bank named numbers, frameworks and expert-specific claims as you FIRST watch each module - you cannot go back for them.</text>
<text x="14" y="346" fill="var(--text-dim)">Final week: work the spaced-repetition due queue. Re-watching whole modules is the lowest-yield use of the last week.</text>
</svg>'''
    return _wrap("dg-mock_decisions", "How to pick when every option looks right", body,
                 "The credited answer protects the athlete first, then individualises - and format claims stay assumptions.")


DIAGRAMS = {
    "hp_levels": d_hp_levels,
    "hp_movelib": d_hp_movelib,
    "st_framework": d_st_framework,
    "mp_pressure_sim": d_mp_pressure_sim,
    "rb_compromised_tech": d_rb_compromised_tech,
    "pe_load_mgmt": d_pe_load_mgmt,
    "pc_individualize": d_pc_individualize,
    "rb_footsep": d_rb_footsep,
    "nu_plantbased": d_nu_plantbased,
    "sm_longevity": d_sm_longevity,
    "mp_neurodiversity": d_mp_neurodiversity,
    "cm_communication": d_cm_communication,
    "hp_stations": d_hp_stations,
    "mock_decisions": d_mock_decisions,
}
