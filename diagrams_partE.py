# -*- coding: utf-8 -*-
"""Bespoke lesson diagrams - batch E."""


def _wrap(did, title, body, caption=""):
    cap = f'<div class="w-hint">{caption}</div>' if caption else ""
    return (f'<div class="widget diagram" id="{did}">'
            f'<div class="w-head"><span class="w-icon">&#9672;</span><span class="w-title">{title}</span></div>'
            f'<div class="w-body">{body}</div>{cap}</div>')


# Reduced-motion guard. Disables the animation only, never the static geometry
# inside the animated group - the same rule the other modules use. CSS cannot stop
# SMIL on its own, so the rule has to reach the <animate*> elements themselves.
_RM = ('<style>@media (prefers-reduced-motion: reduce){'
       '.dg-anim animate,.dg-anim animateMotion,.dg-anim animateTransform{display:none}}'
       '</style>')


def d_of_testmatrix():
    return _wrap("dg-of_testmatrix", "Five bike-erg tests, ranked by the stress they impose", '''<svg viewBox="0 0 700 356" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Five off-feet tests ordered by stress, with the pool of permitted athletes shrinking as stress rises">''' + _RM + '''
<text x="26" y="20" font-size="12" fill="var(--text-dim)">pool of athletes permitted</text>
<text x="520" y="20" font-size="12" fill="var(--text-dim)">stress the test imposes &#8594;</text>
<polygon points="26,30 674,46 674,64 26,78" fill="var(--theme-accent)" opacity="0.15"/>
<text x="36" y="58" font-size="12" fill="var(--text)">every athlete</text>
<text x="300" y="58" font-size="12" fill="var(--text)">experienced pro</text>
<text x="536" y="60" font-size="12" fill="var(--text)">pro + supervised</text>
<g class="dg-anim"><line x1="26" y1="28" x2="26" y2="250" stroke="var(--theme-accent)" stroke-width="2" opacity="0.35"><animate attributeName="x1" values="40;660;40" dur="14s" repeatCount="indefinite"/><animate attributeName="x2" values="40;660;40" dur="14s" repeatCount="indefinite"/></line></g>
<text x="122" y="92" font-size="11" fill="var(--text-dimmer)" text-anchor="middle">AEROBIC</text>
<text x="240" y="92" font-size="11" fill="var(--text-dimmer)" text-anchor="middle">POWER</text>
<text x="358" y="92" font-size="11" fill="var(--text-dimmer)" text-anchor="middle">AEROBIC</text>
<text x="476" y="92" font-size="11" fill="var(--text-dimmer)" text-anchor="middle">AEROBIC</text>
<text x="594" y="92" font-size="11" fill="var(--text-dimmer)" text-anchor="middle">POWER</text>
<rect x="72" y="216" width="100" height="30" rx="3" fill="var(--good)" opacity="0.55"/>
<rect x="190" y="202" width="100" height="44" rx="3" fill="var(--good)" opacity="0.55"/>
<rect x="308" y="160" width="100" height="86" rx="3" fill="var(--warn)" opacity="0.55"/>
<rect x="426" y="136" width="100" height="110" rx="3" fill="var(--warn)" opacity="0.55"/>
<rect x="544" y="116" width="100" height="130" rx="3" fill="var(--bad)" opacity="0.55"/>
<text x="122" y="210" font-size="11" fill="var(--text)" text-anchor="middle">ALL ATHLETES</text>
<text x="240" y="196" font-size="11" fill="var(--text)" text-anchor="middle">ALL DIVISIONS</text>
<text x="358" y="154" font-size="11" fill="var(--text)" text-anchor="middle">PRO, SUPERVISED</text>
<text x="476" y="130" font-size="11" fill="var(--text)" text-anchor="middle">PRO, SUPERVISED</text>
<text x="594" y="110" font-size="11" fill="var(--text)" text-anchor="middle">PRO ONLY, RARELY</text>
<line x1="26" y1="246" x2="674" y2="246" stroke="var(--border)" stroke-width="1.5"/>
<text x="122" y="264" font-size="12" fill="var(--text)" text-anchor="middle">Submaximal<tspan x="122" dy="14">health ramp</tspan></text>
<text x="240" y="264" font-size="12" fill="var(--text)" text-anchor="middle">6-second<tspan x="240" dy="14">peak power</tspan></text>
<text x="358" y="264" font-size="12" fill="var(--text)" text-anchor="middle">3-minute<tspan x="358" dy="14">confirmation</tspan></text>
<text x="476" y="264" font-size="12" fill="var(--text)" text-anchor="middle">Maximal<tspan x="476" dy="14">ramp</tspan></text>
<text x="594" y="264" font-size="12" fill="var(--text)" text-anchor="middle">30-second<tspan x="594" dy="14">power test</tspan></text>
<text x="122" y="296" font-size="11" fill="var(--text-dim)" text-anchor="middle">8-12 min ramp<tspan x="122" dy="12">stop at RPE 7/10</tspan><tspan x="122" dy="12">or 85% HRmax</tspan></text>
<text x="240" y="296" font-size="11" fill="var(--text-dim)" text-anchor="middle">peak W and W/kg<tspan x="240" dy="12">strong: ~130 rpm</tspan><tspan x="240" dy="12">peaks 140-150+</tspan></text>
<text x="358" y="296" font-size="11" fill="var(--text-dim)" text-anchor="middle">3 min at a known<tspan x="358" dy="12">MMP, 90-110 rpm</tspan><tspan x="358" dy="12">confirms the zones</tspan></text>
<text x="476" y="296" font-size="11" fill="var(--text-dim)" text-anchor="middle">ramp to failure<tspan x="476" dy="12">true MMP + max HR</tspan><tspan x="476" dy="12">medical clearance</tspan></text>
<text x="594" y="296" font-size="11" fill="var(--text-dim)" text-anchor="middle">adds the fatigue<tspan x="594" dy="12">factor; greatest</tspan><tspan x="594" dy="12">whole-body stress</tspan></text>
<line x1="26" y1="336" x2="674" y2="336" stroke="var(--border)" stroke-width="1"/>
<text x="26" y="352" font-size="11" fill="var(--text-dim)">outputs feed forward: MMP &#8594; power + HR zones &#183; CRF percentile &#183; sprint work 2 levels below test resistance</text>
</svg>''', "Risk, not curiosity, picks the test: everyone starts on the submaximal ramp and the permitted pool narrows as stress climbs.")


def d_hp_roxzone():
    return _wrap("dg-hp_roxzone", "15 traverses: where the roxzone minutes go", '''<svg viewBox="0 0 700 348" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Race strip of eight runs alternating with eight stations, showing fifteen transition traverses">''' + _RM + '''
<text x="26" y="20" font-size="12" fill="var(--text-dim)">8 runs alternate with 8 stations &#8212; the clock never stops in between</text>
<g>
<rect x="30" y="34" width="34" height="26" rx="4" fill="none" stroke="var(--text-dim)" stroke-width="1.5"/>
<rect x="70" y="34" width="34" height="26" rx="4" fill="var(--theme-accent)" opacity="0.30"/>
<rect x="110" y="34" width="34" height="26" rx="4" fill="none" stroke="var(--text-dim)" stroke-width="1.5"/>
<rect x="150" y="34" width="34" height="26" rx="4" fill="var(--theme-accent)" opacity="0.30"/>
<rect x="190" y="34" width="34" height="26" rx="4" fill="none" stroke="var(--text-dim)" stroke-width="1.5"/>
<rect x="230" y="34" width="34" height="26" rx="4" fill="var(--theme-accent)" opacity="0.30"/>
<rect x="270" y="34" width="34" height="26" rx="4" fill="none" stroke="var(--text-dim)" stroke-width="1.5"/>
<rect x="310" y="34" width="34" height="26" rx="4" fill="var(--theme-accent)" opacity="0.30"/>
<rect x="350" y="34" width="34" height="26" rx="4" fill="none" stroke="var(--text-dim)" stroke-width="1.5"/>
<rect x="390" y="34" width="34" height="26" rx="4" fill="var(--theme-accent)" opacity="0.30"/>
<rect x="430" y="34" width="34" height="26" rx="4" fill="none" stroke="var(--text-dim)" stroke-width="1.5"/>
<rect x="470" y="34" width="34" height="26" rx="4" fill="var(--theme-accent)" opacity="0.30"/>
<rect x="510" y="34" width="34" height="26" rx="4" fill="none" stroke="var(--text-dim)" stroke-width="1.5"/>
<rect x="550" y="34" width="34" height="26" rx="4" fill="var(--theme-accent)" opacity="0.30"/>
<rect x="590" y="34" width="34" height="26" rx="4" fill="none" stroke="var(--text-dim)" stroke-width="1.5"/>
<rect x="630" y="34" width="34" height="26" rx="4" fill="var(--theme-accent)" opacity="0.30"/>
</g>
<g stroke="var(--warn)" stroke-width="3" stroke-linecap="round">
<line x1="66" y1="47" x2="68" y2="47"/><line x1="106" y1="47" x2="108" y2="47"/><line x1="146" y1="47" x2="148" y2="47"/>
<line x1="186" y1="47" x2="188" y2="47"/><line x1="226" y1="47" x2="228" y2="47"/><line x1="266" y1="47" x2="268" y2="47"/>
<line x1="306" y1="47" x2="308" y2="47"/><line x1="346" y1="47" x2="348" y2="47"/><line x1="386" y1="47" x2="388" y2="47"/>
<line x1="426" y1="47" x2="428" y2="47"/><line x1="466" y1="47" x2="468" y2="47"/><line x1="506" y1="47" x2="508" y2="47"/>
<line x1="546" y1="47" x2="548" y2="47"/><line x1="586" y1="47" x2="588" y2="47"/><line x1="626" y1="47" x2="628" y2="47"/>
</g>
<g class="dg-anim"><circle r="4" fill="var(--theme-accent)"><animateMotion path="M47,47 L647,47" dur="12s" repeatCount="indefinite"/></circle></g>
<text x="30" y="76" font-size="11" fill="var(--text-dim)">1 km run (outline)</text>
<text x="180" y="76" font-size="11" fill="var(--text-dim)">station (filled)</text>
<text x="300" y="76" font-size="11" fill="var(--warn)">| = one roxzone traverse: 8 in + 7 out = 15</text>
<text x="560" y="24" font-size="11" fill="var(--text-dim)">ends on wall balls</text>
<line x1="647" y1="28" x2="647" y2="34" stroke="var(--text-dim)" stroke-width="1"/>
<text x="560" y="90" font-size="11" fill="var(--text-dimmer)">no exit transition after it</text>
<rect x="26" y="100" width="648" height="36" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="42" y="123" font-size="13" fill="var(--text)">roxzone time &#8776; total time &#8722; (run time + station work time) &#8212; and HYROX reports it as its own split</text>
<text x="26" y="164" font-size="12" fill="var(--text-dim)">typical spread (venue-dependent field norms, not standards)</text>
<line x1="150" y1="248" x2="674" y2="248" stroke="var(--border)"/>
<text x="26" y="192" font-size="12" fill="var(--text)">elite</text>
<text x="26" y="216" font-size="12" fill="var(--text)">age-grouper</text>
<text x="26" y="240" font-size="12" fill="var(--text)">novice / mid-pack</text>
<rect x="270" y="180" width="80" height="14" rx="3" fill="var(--good)" opacity="0.6"/>
<rect x="350" y="204" width="120" height="14" rx="3" fill="var(--warn)" opacity="0.6"/>
<rect x="470" y="228" width="160" height="14" rx="3" fill="var(--bad)" opacity="0.6"/>
<text x="358" y="192" font-size="11" fill="var(--text-dim)">3-5 min</text>
<text x="478" y="216" font-size="11" fill="var(--text-dim)">5-8 min</text>
<text x="638" y="240" font-size="11" fill="var(--text-dim)">8-12+ min</text>
<line x1="150" y1="248" x2="150" y2="254" stroke="var(--border)"/><line x1="350" y1="248" x2="350" y2="254" stroke="var(--border)"/><line x1="550" y1="248" x2="550" y2="254" stroke="var(--border)"/>
<text x="150" y="264" font-size="11" fill="var(--text-dimmer)" text-anchor="middle">0</text>
<text x="350" y="264" font-size="11" fill="var(--text-dimmer)" text-anchor="middle">5 min</text>
<text x="550" y="264" font-size="11" fill="var(--text-dimmer)" text-anchor="middle">10 min</text>
<rect x="26" y="276" width="648" height="60" rx="6" fill="var(--theme-accent)" opacity="0.10"/>
<text x="42" y="300" font-size="13" fill="var(--text)">15 s saved per traverse &#215; 15 traverses = 225 s &#8776; 3:45</text>
<text x="42" y="318" font-size="11" fill="var(--text-dim)">bought with rehearsal and pre-set decision rules, not aerobic adaptation. The leaks: walking instead of<tspan x="42" dy="12">jogging, the chalk ritual, kit-fiddling, lane hunting, standing recovery, misreading the station set-up</tspan></text>
</svg>''', "Roxzone is a measured split, not dead time: fifteen traverses mean a 15-second habit is worth nearly four minutes.")


def d_st_row():
    return _wrap("dg-st_row", "The rowing chain, the fault that breaks it, and the late-race knee", '''<svg viewBox="0 0 700 346" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Kinetic sequence legs to hips to trunk to arms, the early-arm fault chain, and knee valgus versus knees tracking out">''' + _RM + '''
<text x="26" y="20" font-size="12" fill="var(--text-dim)">kinetic sequence &#8212; large proximal groups initiate, distal segments finish</text>
<rect x="26" y="32" width="389" height="40" rx="5" fill="var(--theme-accent)" opacity="0.32"/>
<rect x="415" y="32" width="259" height="40" rx="5" fill="var(--theme-accent)" opacity="0.12"/>
<line x1="415" y1="32" x2="415" y2="72" stroke="var(--surface)" stroke-width="2"/>
<line x1="501" y1="34" x2="501" y2="70" stroke="var(--text-dimmer)" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="588" y1="34" x2="588" y2="70" stroke="var(--text-dimmer)" stroke-width="1" stroke-dasharray="3 3"/>
<text x="220" y="57" font-size="13" fill="var(--text)" text-anchor="middle">LEGS &#8212; about 60% of stroke effort</text>
<text x="458" y="57" font-size="12" fill="var(--text)" text-anchor="middle">hips</text>
<text x="544" y="57" font-size="12" fill="var(--text)" text-anchor="middle">trunk</text>
<text x="631" y="57" font-size="12" fill="var(--text)" text-anchor="middle">arms</text>
<g class="dg-anim"><rect x="26" y="32" width="26" height="40" rx="5" fill="var(--theme-accent)" opacity="0.5"><animate attributeName="x" values="26;648;26" dur="9s" repeatCount="indefinite" calcMode="spline" keySplines="0.3 0 0.7 1;0.3 0 0.7 1" keyTimes="0;0.55;1"/></rect></g>
<text x="26" y="90" font-size="11" fill="var(--text-dimmer)">drive order runs left to right; reach is maximised at the catch WITHOUT losing trunk stiffness</text>
<rect x="26" y="102" width="200" height="44" rx="6" fill="none" stroke="var(--bad)" stroke-width="1.5"/>
<text x="126" y="122" font-size="12" fill="var(--text)" text-anchor="middle">FAULT: arms flex early<tspan x="126" dy="15">(order broken)</tspan></text>
<line x1="230" y1="124" x2="266" y2="124" stroke="var(--bad)" stroke-width="2" marker-end="url(#st_row-ar)"/>
<defs><marker id="st_row-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--bad)"/></marker></defs>
<text x="274" y="115" font-size="12" fill="var(--text)">stroke shortens</text>
<text x="274" y="131" font-size="12" fill="var(--text)">peak force drops</text>
<text x="274" y="147" font-size="12" fill="var(--text)">metabolic cost rises &#8212; small muscles doing large-muscle work</text>
<line x1="26" y1="160" x2="674" y2="160" stroke="var(--border)"/>
<text x="26" y="180" font-size="12" fill="var(--text-dim)">the station&#8217;s signature late-race fault: knee tracking under fatigue</text>
<g stroke-width="4" fill="none" stroke-linecap="round">
<line x1="90" y1="200" x2="118" y2="248" stroke="var(--bad)"/><line x1="118" y1="248" x2="96" y2="296" stroke="var(--bad)"/>
<line x1="190" y1="200" x2="162" y2="248" stroke="var(--bad)"/><line x1="162" y1="248" x2="184" y2="296" stroke="var(--bad)"/>
<line x1="430" y1="200" x2="418" y2="248" stroke="var(--good)"/><line x1="418" y1="248" x2="414" y2="296" stroke="var(--good)"/>
<line x1="510" y1="200" x2="522" y2="248" stroke="var(--good)"/><line x1="522" y1="248" x2="526" y2="296" stroke="var(--good)"/>
</g>
<line x1="86" y1="298" x2="194" y2="298" stroke="var(--border)" stroke-width="2"/>
<line x1="408" y1="298" x2="532" y2="298" stroke="var(--border)" stroke-width="2"/>
<text x="140" y="316" font-size="12" fill="var(--text)" text-anchor="middle">knee valgus &#8212; knees cave in</text>
<text x="140" y="332" font-size="11" fill="var(--text-dim)" text-anchor="middle">glute medius under-active or quad-dominant</text>
<text x="470" y="316" font-size="12" fill="var(--text)" text-anchor="middle">cue: knees track out over the toes</text>
<text x="470" y="332" font-size="11" fill="var(--text-dim)" text-anchor="middle">band walks, clamshells, monster walks; hip thrusts</text>
<text x="228" y="212" font-size="11" fill="var(--text-dim)">the row arrives LATE in</text>
<text x="228" y="228" font-size="11" fill="var(--text-dim)">the race, so fatigue alone</text>
<text x="228" y="244" font-size="11" fill="var(--text-dim)">produces valgus even in</text>
<text x="228" y="260" font-size="11" fill="var(--text-dim)">athletes with strong glutes</text>
<text x="228" y="284" font-size="11" fill="var(--text-dimmer)">rhythm: hold the drive-to-recovery</text>
<text x="228" y="298" font-size="11" fill="var(--text-dimmer)">ratio &#8212; rushing recovery raises HR</text>
</svg>''', "Legs lead and carry roughly 60% of the stroke; flexing the arms early or letting the knees cave costs force and oxygen, not just style.")


def d_rb_braking():
    return _wrap("dg-rb_braking", "Overstride, braking impulse and the levers that actually work", '''<svg viewBox="0 0 700 356" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Overstriding foot far ahead of centre of mass producing large braking, versus contact nearer the centre of mass">
<defs><marker id="rb_braking-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--bad)"/></marker>
<marker id="rb_braking-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--good)"/></marker></defs>
<text x="26" y="20" font-size="12" fill="var(--text-dim)">braking impulse scales with the horizontal distance from foot contact to the centre of mass</text>
<line x1="26" y1="180" x2="330" y2="180" stroke="var(--border)" stroke-width="2"/>
<line x1="370" y1="180" x2="674" y2="180" stroke="var(--border)" stroke-width="2"/>
<circle cx="120" cy="86" r="9" fill="var(--theme-accent)"/>
<text x="96" y="70" font-size="11" fill="var(--text-dim)">centre of mass</text>
<line x1="120" y1="95" x2="120" y2="180" stroke="var(--text-dimmer)" stroke-width="1" stroke-dasharray="4 3"/>
<line x1="120" y1="96" x2="228" y2="176" stroke="var(--bad)" stroke-width="4" stroke-linecap="round"/>
<line x1="120" y1="128" x2="228" y2="176" stroke="var(--bad)" stroke-width="1" stroke-dasharray="3 3" opacity="0.6"/>
<text x="182" y="120" font-size="11" fill="var(--bad)">extended knee = strut</text>
<line x1="222" y1="164" x2="150" y2="164" stroke="var(--bad)" stroke-width="3" marker-end="url(#rb_braking-b)"/>
<text x="150" y="156" font-size="12" fill="var(--text)">large braking force</text>
<line x1="120" y1="196" x2="228" y2="196" stroke="var(--text-dim)" stroke-width="1"/>
<line x1="120" y1="191" x2="120" y2="201" stroke="var(--text-dim)"/><line x1="228" y1="191" x2="228" y2="201" stroke="var(--text-dim)"/>
<text x="174" y="212" font-size="12" fill="var(--text)" text-anchor="middle">large distance</text>
<text x="174" y="228" font-size="12" fill="var(--bad)" text-anchor="middle">OVERSTRIDE</text>
<circle cx="470" cy="86" r="9" fill="var(--theme-accent)"/>
<line x1="470" y1="95" x2="470" y2="180" stroke="var(--text-dimmer)" stroke-width="1" stroke-dasharray="4 3"/>
<line x1="470" y1="96" x2="508" y2="140" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/>
<line x1="508" y1="140" x2="512" y2="176" stroke="var(--good)" stroke-width="4" stroke-linecap="round"/>
<text x="524" y="120" font-size="11" fill="var(--good)">flexed knee absorbs</text>
<line x1="506" y1="164" x2="474" y2="164" stroke="var(--good)" stroke-width="3" marker-end="url(#rb_braking-g)"/>
<text x="524" y="160" font-size="12" fill="var(--text)">small braking force</text>
<line x1="470" y1="196" x2="512" y2="196" stroke="var(--text-dim)" stroke-width="1"/>
<line x1="470" y1="191" x2="470" y2="201" stroke="var(--text-dim)"/><line x1="512" y1="191" x2="512" y2="201" stroke="var(--text-dim)"/>
<text x="491" y="212" font-size="12" fill="var(--text)" text-anchor="middle">small distance</text>
<text x="491" y="228" font-size="12" fill="var(--good)" text-anchor="middle">CONTACT NEARER THE COM</text>
<path d="M34 176 L48 176 L56 138 L64 166 L92 166" fill="none" stroke="var(--bad)" stroke-width="2"/>
<text x="26" y="102" font-size="11" fill="var(--text-dim)">sharp impact peak,</text>
<text x="26" y="116" font-size="11" fill="var(--text-dim)">high loading rate</text>
<text x="26" y="130" font-size="11" fill="var(--text-dimmer)">(tibial stress risk)</text>
<path d="M384 176 L398 176 L412 152 L430 164 L448 164" fill="none" stroke="var(--good)" stroke-width="2"/>
<text x="376" y="140" font-size="11" fill="var(--text-dim)">blunted peak</text>
<line x1="26" y1="242" x2="674" y2="242" stroke="var(--border)"/>
<text x="26" y="262" font-size="12" fill="var(--text-dim)">the reliable levers &#8212; all indirect</text>
<rect x="26" y="272" width="200" height="46" rx="6" fill="var(--theme-accent)" opacity="0.12"/>
<rect x="240" y="272" width="200" height="46" rx="6" fill="var(--theme-accent)" opacity="0.12"/>
<rect x="454" y="272" width="220" height="46" rx="6" fill="var(--theme-accent)" opacity="0.12"/>
<text x="126" y="292" font-size="12" fill="var(--text)" text-anchor="middle">raise cadence 5-10%<tspan x="126" dy="15">most reliable single change</tspan></text>
<text x="340" y="292" font-size="12" fill="var(--text)" text-anchor="middle">small lean from the ANKLES<tspan x="340" dy="15">not a bend at the waist</tspan></text>
<text x="564" y="292" font-size="12" fill="var(--text)" text-anchor="middle">improve hip extension<tspan x="564" dy="15">stride length found behind</tspan></text>
<text x="26" y="334" font-size="12" fill="var(--bad)">Do NOT cue foot placement &#8212; &#8220;land under yourself&#8221; makes athletes reach, then pull back.</text>
<text x="26" y="350" font-size="11" fill="var(--text-dim)">Small changes only; fatigue drives overstride, so the compromised run after the sled is the risk window.</text>
</svg>''', "Braking is set by how far ahead of the centre of mass the foot lands - fix it with cadence, ankle lean and hip extension, never by aiming the foot.")


def d_st_lunge():
    return _wrap("dg-st_lunge", "Sandbag lunges: the two faults that empty the legs", '''<svg viewBox="0 0 700 352" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Set-up sequence, tightrope versus parallel-line stance seen from above, and front-leg-only versus bilateral drive">
<defs><marker id="st_lunge-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker>
<marker id="st_lunge-bad" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--bad)"/></marker>
<marker id="st_lunge-good" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--good)"/></marker></defs>
<text x="26" y="18" font-size="12" fill="var(--text-dim)">station 7 of 8 &#8212; one 1 km run and 100 wall balls still to come, so the legs matter more than the split</text>
<rect x="26" y="28" width="146" height="34" rx="5" fill="var(--theme-accent)" opacity="0.12"/>
<rect x="192" y="28" width="146" height="34" rx="5" fill="var(--theme-accent)" opacity="0.12"/>
<rect x="358" y="28" width="146" height="34" rx="5" fill="var(--theme-accent)" opacity="0.12"/>
<rect x="524" y="28" width="150" height="34" rx="5" fill="var(--theme-accent)" opacity="0.12"/>
<text x="99" y="49" font-size="12" fill="var(--text)" text-anchor="middle">grip the handles</text>
<text x="265" y="49" font-size="12" fill="var(--text)" text-anchor="middle">clean to front rack</text>
<text x="431" y="49" font-size="12" fill="var(--text)" text-anchor="middle">overhead on shoulders</text>
<text x="599" y="49" font-size="12" fill="var(--text)" text-anchor="middle">hold it for 100 m</text>
<line x1="174" y1="45" x2="190" y2="45" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#st_lunge-a)"/>
<line x1="340" y1="45" x2="356" y2="45" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#st_lunge-a)"/>
<line x1="506" y1="45" x2="522" y2="45" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#st_lunge-a)"/>
<text x="26" y="78" font-size="11" fill="var(--text-dimmer)">handles: outside, inner-outside or closest inside &#8212; practise the clean and the overhead transition</text>
<text x="26" y="92" font-size="11" fill="var(--text-dimmer)">overhead needs shoulder and thoracic mobility, or the athlete compensates through the lumbar spine</text>
<line x1="345" y1="100" x2="345" y2="292" stroke="var(--border)"/>
<text x="26" y="110" font-size="12" fill="var(--text)">FAULT 1 &#8212; foot placement (from above)</text>
<line x1="96" y1="124" x2="96" y2="222" stroke="var(--bad)" stroke-width="1" stroke-dasharray="4 3"/>
<rect x="88" y="130" width="16" height="24" rx="7" fill="var(--bad)" opacity="0.55"/>
<rect x="88" y="166" width="16" height="24" rx="7" fill="var(--bad)" opacity="0.55"/>
<rect x="88" y="202" width="16" height="24" rx="7" fill="var(--bad)" opacity="0.55"/>
<text x="96" y="244" font-size="12" fill="var(--text)" text-anchor="middle">tightrope walk</text>
<text x="96" y="260" font-size="11" fill="var(--text-dim)" text-anchor="middle">one line, no lateral</text>
<text x="96" y="272" font-size="11" fill="var(--text-dim)" text-anchor="middle">stability</text>
<line x1="216" y1="124" x2="216" y2="222" stroke="var(--good)" stroke-width="1" stroke-dasharray="4 3"/>
<line x1="264" y1="124" x2="264" y2="222" stroke="var(--good)" stroke-width="1" stroke-dasharray="4 3"/>
<rect x="208" y="130" width="16" height="24" rx="7" fill="var(--good)" opacity="0.55"/>
<rect x="256" y="166" width="16" height="24" rx="7" fill="var(--good)" opacity="0.55"/>
<rect x="208" y="202" width="16" height="24" rx="7" fill="var(--good)" opacity="0.55"/>
<line x1="216" y1="122" x2="264" y2="122" stroke="var(--text-dim)" stroke-width="1"/>
<text x="272" y="126" font-size="11" fill="var(--text-dim)">squat width</text>
<text x="240" y="244" font-size="12" fill="var(--text)" text-anchor="middle">parallel lines</text>
<text x="240" y="260" font-size="11" fill="var(--text-dim)" text-anchor="middle">two tracks, moving</text>
<text x="240" y="272" font-size="11" fill="var(--text-dim)" text-anchor="middle">forward on them</text>
<text x="366" y="110" font-size="12" fill="var(--text)">FAULT 2 &#8212; standing up (the costly one)</text>
<line x1="380" y1="226" x2="510" y2="226" stroke="var(--border)" stroke-width="2"/>
<rect x="470" y="216" width="26" height="10" rx="3" fill="var(--bad)" opacity="0.55"/>
<rect x="392" y="216" width="26" height="10" rx="3" fill="var(--text-dimmer)" opacity="0.45"/>
<line x1="483" y1="214" x2="483" y2="150" stroke="var(--bad)" stroke-width="5" marker-end="url(#st_lunge-bad)"/>
<text x="366" y="200" font-size="11" fill="var(--text-dimmer)">back leg</text>
<text x="366" y="212" font-size="11" fill="var(--text-dimmer)">passive</text>
<text x="440" y="140" font-size="12" fill="var(--text)" text-anchor="middle">front leg only</text>
<line x1="540" y1="226" x2="670" y2="226" stroke="var(--border)" stroke-width="2"/>
<rect x="630" y="216" width="26" height="10" rx="3" fill="var(--good)" opacity="0.55"/>
<rect x="552" y="216" width="26" height="10" rx="3" fill="var(--good)" opacity="0.55"/>
<line x1="643" y1="214" x2="643" y2="164" stroke="var(--good)" stroke-width="4" marker-end="url(#st_lunge-good)"/>
<line x1="562" y1="214" x2="580" y2="168" stroke="var(--good)" stroke-width="4" marker-end="url(#st_lunge-good)"/>
<text x="604" y="136" font-size="12" fill="var(--text)" text-anchor="middle">drive with BOTH feet,</text>
<text x="604" y="150" font-size="12" fill="var(--text)" text-anchor="middle">then push off the back leg</text>
<text x="366" y="256" font-size="11" fill="var(--bad)">front leg only: bag + body weight on ONE quad, rep after rep</text>
<text x="366" y="272" font-size="11" fill="var(--good)">both feet: load shared, and full extension every rep</text>
<line x1="26" y1="296" x2="674" y2="296" stroke="var(--border)"/>
<text x="26" y="314" font-size="12" fill="var(--text)">Breathing is the limiter &#8594; feet together at the top, take a beat. Going for time &#8594; step-through.</text>
<text x="26" y="334" font-size="12" fill="var(--warn)">Overload the front quad and you pay on the final run and at the wall balls &#8212; a coupled pair.</text>
</svg>''', "Feet on two parallel tracks and both legs driving out of every rep: this station is judged by what is left in the legs afterwards.")


def d_hp_profiling():
    return _wrap("dg-hp_profiling", "Profiling by rank gap, not by raw time", '''<svg viewBox="0 0 700 350" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Three athlete profiles plotted as run rank versus station rank within the same division">
<text x="26" y="18" font-size="12" fill="var(--text)">the limiter shows up as a GAP between segment ranks, never as a raw time</text>
<text x="26" y="34" font-size="11" fill="var(--text-dim)">rank each segment by percentile inside your own division and field &#8212; that normalises course, conditions and field depth</text>
<line x1="180" y1="56" x2="660" y2="56" stroke="var(--border)" stroke-width="1.5"/>
<text x="180" y="50" font-size="11" fill="var(--text-dimmer)">ranks poorly</text>
<text x="660" y="50" font-size="11" fill="var(--text-dimmer)" text-anchor="end">ranks well</text>
<line x1="180" y1="52" x2="180" y2="60" stroke="var(--border)"/><line x1="660" y1="52" x2="660" y2="60" stroke="var(--border)"/>
<text x="26" y="76" font-size="12" fill="var(--text)">Endurance-</text><text x="26" y="90" font-size="12" fill="var(--text)">dominant</text>
<line x1="240" y1="80" x2="600" y2="80" stroke="var(--warn)" stroke-width="2" stroke-dasharray="5 4"/>
<rect x="232" y="72" width="16" height="16" rx="3" fill="var(--bad)"/>
<circle cx="600" cy="80" r="8" fill="var(--good)"/>
<text x="216" y="106" font-size="11" fill="var(--text-dim)">stations</text>
<text x="600" y="106" font-size="11" fill="var(--text-dim)" text-anchor="middle">runs</text>
<text x="280" y="106" font-size="11" fill="var(--text-dimmer)">sleds the usual outlier; low relative strength</text>
<text x="26" y="140" font-size="12" fill="var(--text)">Strength-</text><text x="26" y="154" font-size="12" fill="var(--text)">dominant</text>
<line x1="248" y1="144" x2="592" y2="144" stroke="var(--warn)" stroke-width="2" stroke-dasharray="5 4"/>
<circle cx="248" cy="144" r="8" fill="var(--bad)"/>
<rect x="584" y="136" width="16" height="16" rx="3" fill="var(--good)"/>
<text x="248" y="170" font-size="11" fill="var(--text-dim)" text-anchor="middle">runs</text>
<text x="568" y="170" font-size="11" fill="var(--text-dim)">stations</text>
<text x="286" y="170" font-size="11" fill="var(--text-dimmer)">runs fade late; long roxzone spent recovering</text>
<text x="26" y="208" font-size="12" fill="var(--text)">Balanced</text>
<line x1="470" y1="204" x2="512" y2="204" stroke="var(--good)" stroke-width="2"/>
<circle cx="470" cy="204" r="8" fill="var(--good)"/>
<rect x="504" y="196" width="16" height="16" rx="3" fill="var(--good)"/>
<text x="120" y="208" font-size="11" fill="var(--text-dimmer)">within a few points of the athlete&#8217;s own average</text>
<text x="26" y="228" font-size="11" fill="var(--text-dim)">&#8594; then gains come from roxzone, pacing discipline and station technique, not from one big physical hole</text>
<line x1="26" y1="242" x2="674" y2="242" stroke="var(--border)"/>
<rect x="26" y="250" width="330" height="58" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="40" y="270" font-size="12" fill="var(--text)">run-split drift =</text>
<text x="40" y="286" font-size="12" fill="var(--text)">(mean runs 5-8 &#8722; mean runs 1-4) &#247; mean runs 1-4</text>
<text x="40" y="302" font-size="11" fill="var(--text-dim)">no validated cut-off; roughly 8-10% is a practical flag</text>
<rect x="370" y="250" width="304" height="58" rx="6" fill="var(--theme-accent)" opacity="0.12"/>
<text x="384" y="270" font-size="12" fill="var(--text)">bias training to the limiter, and hold the</text>
<text x="384" y="286" font-size="12" fill="var(--text)">dominant quality at 1-2 sessions a week</text>
<text x="384" y="302" font-size="11" fill="var(--text-dim)">re-profile each block: training moves the limiter</text>
<text x="26" y="326" font-size="11" fill="var(--text-dim)">Confirm with gym testing &#8212; fresh run benchmark, compromised-run repeats, relative strength, unbroken capacity, grip.</text>
<text x="26" y="342" font-size="11" fill="var(--text-dim)">One race distorts easily, and grip alone can be the limiter while looking like a conditioning problem.</text>
</svg>''', "Rank the runs against the stations inside your own division: the size and direction of the gap names the limiter.")


def d_sk_practice_design():
    return _wrap("dg-sk_practice_design", "Blocked vs random: practice-day score is not learning", '''<svg viewBox="0 0 700 352" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Blocked and random practice schedules and their crossing acquisition and retention curves">
<text x="26" y="18" font-size="12" fill="var(--text-dim)">how you SCHEDULE practice, at equal volume</text>
<text x="26" y="44" font-size="12" fill="var(--text)">BLOCKED</text>
<g font-size="12" fill="var(--text)" text-anchor="middle">
<rect x="26" y="54" width="22" height="22" rx="4" fill="var(--theme-accent)" opacity="0.30"/><text x="37" y="70">A</text>
<rect x="52" y="54" width="22" height="22" rx="4" fill="var(--theme-accent)" opacity="0.30"/><text x="63" y="70">A</text>
<rect x="78" y="54" width="22" height="22" rx="4" fill="var(--theme-accent)" opacity="0.30"/><text x="89" y="70">A</text>
<rect x="112" y="54" width="22" height="22" rx="4" fill="var(--theme-accent)" opacity="0.30"/><text x="123" y="70">B</text>
<rect x="138" y="54" width="22" height="22" rx="4" fill="var(--theme-accent)" opacity="0.30"/><text x="149" y="70">B</text>
<rect x="164" y="54" width="22" height="22" rx="4" fill="var(--theme-accent)" opacity="0.30"/><text x="175" y="70">B</text>
<rect x="198" y="54" width="22" height="22" rx="4" fill="var(--theme-accent)" opacity="0.30"/><text x="209" y="70">C</text>
<rect x="224" y="54" width="22" height="22" rx="4" fill="var(--theme-accent)" opacity="0.30"/><text x="235" y="70">C</text>
<rect x="250" y="54" width="22" height="22" rx="4" fill="var(--theme-accent)" opacity="0.30"/><text x="261" y="70">C</text>
</g>
<text x="26" y="96" font-size="11" fill="var(--text-dim)">feels good in the session, fades by the retention test</text>
<text x="26" y="124" font-size="12" fill="var(--text)">RANDOM / INTERLEAVED</text>
<g font-size="12" fill="var(--text)" text-anchor="middle">
<rect x="26" y="134" width="22" height="22" rx="4" fill="var(--good)" opacity="0.30"/><text x="37" y="150">A</text>
<rect x="52" y="134" width="22" height="22" rx="4" fill="var(--good)" opacity="0.30"/><text x="63" y="150">B</text>
<rect x="78" y="134" width="22" height="22" rx="4" fill="var(--good)" opacity="0.30"/><text x="89" y="150">C</text>
<rect x="112" y="134" width="22" height="22" rx="4" fill="var(--good)" opacity="0.30"/><text x="123" y="150">B</text>
<rect x="138" y="134" width="22" height="22" rx="4" fill="var(--good)" opacity="0.30"/><text x="149" y="150">C</text>
<rect x="164" y="134" width="22" height="22" rx="4" fill="var(--good)" opacity="0.30"/><text x="175" y="150">A</text>
<rect x="198" y="134" width="22" height="22" rx="4" fill="var(--good)" opacity="0.30"/><text x="209" y="150">C</text>
<rect x="224" y="134" width="22" height="22" rx="4" fill="var(--good)" opacity="0.30"/><text x="235" y="150">A</text>
<rect x="250" y="134" width="22" height="22" rx="4" fill="var(--good)" opacity="0.30"/><text x="261" y="150">B</text>
</g>
<text x="26" y="176" font-size="11" fill="var(--text-dim)">feels worse in the session, holds at the retention test</text>
<text x="26" y="196" font-size="11" fill="var(--text-dimmer)">random is PLANNED &#8212; only the athlete&#8217;s expectancy is randomised</text>
<line x1="320" y1="40" x2="320" y2="212" stroke="var(--border)"/>
<line x1="400" y1="180" x2="400" y2="46" stroke="var(--border)" stroke-width="1.5"/>
<line x1="400" y1="180" x2="650" y2="180" stroke="var(--border)" stroke-width="1.5"/>
<text x="382" y="46" font-size="11" fill="var(--text-dim)" text-anchor="end">high</text>
<text x="382" y="176" font-size="11" fill="var(--text-dim)" text-anchor="end">low</text>
<text x="370" y="112" font-size="11" fill="var(--text-dim)" text-anchor="middle" transform="rotate(-90 370 112)">performance</text>
<text x="424" y="196" font-size="11" fill="var(--text-dim)">practice day</text>
<text x="640" y="196" font-size="11" fill="var(--text-dim)" text-anchor="end">delayed retention</text>
<text x="640" y="208" font-size="11" fill="var(--text-dim)" text-anchor="end">+ transfer test</text>
<line x1="430" y1="66" x2="620" y2="140" stroke="var(--theme-accent)" stroke-width="2.5"/>
<line x1="430" y1="140" x2="620" y2="66" stroke="var(--good)" stroke-width="2.5"/>
<circle cx="430" cy="66" r="4" fill="var(--theme-accent)"/><circle cx="620" cy="140" r="4" fill="var(--theme-accent)"/>
<circle cx="430" cy="140" r="4" fill="var(--good)"/><circle cx="620" cy="66" r="4" fill="var(--good)"/>
<text x="628" y="144" font-size="11" fill="var(--text)">blocked</text>
<text x="628" y="62" font-size="11" fill="var(--text)">random</text>
<text x="410" y="230" font-size="11" fill="var(--text-dimmer)">contextual interference &#8212; mechanism still contested</text>
<line x1="26" y1="244" x2="674" y2="244" stroke="var(--border)"/>
<text x="26" y="264" font-size="12" fill="var(--text)">blocked</text>
<line x1="82" y1="260" x2="112" y2="260" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#sk_practice_design-a)"/>
<defs><marker id="sk_practice_design-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker></defs>
<text x="118" y="264" font-size="12" fill="var(--text)">serial</text>
<line x1="156" y1="260" x2="186" y2="260" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#sk_practice_design-a)"/>
<text x="192" y="264" font-size="12" fill="var(--text)">random</text>
<text x="248" y="264" font-size="11" fill="var(--text-dim)">as competence rises &#8212; weak or reversed in novices and on very complex skills</text>
<rect x="26" y="280" width="320" height="60" rx="6" fill="var(--good)" opacity="0.12"/>
<text x="38" y="298" font-size="12" fill="var(--text)">VARY what genuinely differs on race day</text>
<text x="38" y="314" font-size="11" fill="var(--text-dim)">sled load, floor friction under the sled, sandbag shape</text>
<text x="38" y="330" font-size="11" fill="var(--text-dim)">and placement, rope thickness, footwear and surface</text>
<rect x="356" y="280" width="318" height="60" rx="6" fill="var(--bad)" opacity="0.12"/>
<text x="368" y="298" font-size="12" fill="var(--text)">NEVER vary the movement standard</text>
<text x="368" y="314" font-size="11" fill="var(--text-dim)">wall-ball target height is fixed by division &#8212; train it at</text>
<text x="368" y="330" font-size="11" fill="var(--text-dim)">spec, and gate fatigued practice: stop when form breaks</text>
</svg>''', "Judge a schedule by the delayed retention test, not the session score - and step blocked to serial to random as competence rises.")


def d_nu_postcomp():
    return _wrap("dg-nu_postcomp", "Post-race refuelling: urgency is set by the next effort", '''<svg viewBox="0 0 700 352" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Decision fork on time to the next hard effort, with rapid refuelling targets on one branch and daily totals on the other">
<defs><marker id="nu_postcomp-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker></defs>
<text x="26" y="18" font-size="12" fill="var(--text-dim)">four recovery targets after a race</text>
<g font-size="11" fill="var(--text)" text-anchor="middle">
<rect x="26" y="26" width="152" height="26" rx="13" fill="var(--theme-accent)" opacity="0.14"/><text x="102" y="43">glycogen resynthesis</text>
<rect x="190" y="26" width="152" height="26" rx="13" fill="var(--theme-accent)" opacity="0.14"/><text x="266" y="43">muscle repair</text>
<rect x="354" y="26" width="152" height="26" rx="13" fill="var(--theme-accent)" opacity="0.14"/><text x="430" y="43">fluid + electrolytes</text>
<rect x="518" y="26" width="156" height="26" rx="13" fill="var(--theme-accent)" opacity="0.14"/><text x="596" y="43" text-anchor="middle">immune + energy status</text>
</g>
<rect x="220" y="64" width="260" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="350" y="84" font-size="13" fill="var(--text)" text-anchor="middle">when is the next hard effort?</text>
<path d="M240 94 L240 112 L170 112 L170 128" fill="none" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#nu_postcomp-a)"/>
<path d="M460 94 L460 112 L530 112 L530 128" fill="none" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#nu_postcomp-a)"/>
<text x="170" y="108" font-size="12" fill="var(--warn)" text-anchor="end">within ~24 h</text>
<text x="540" y="108" font-size="12" fill="var(--good)">a week or more</text>
<rect x="26" y="132" width="314" height="118" rx="8" fill="var(--warn)" opacity="0.12"/>
<text x="40" y="152" font-size="12" fill="var(--text)">TIMING GENUINELY MATTERS</text>
<text x="40" y="174" font-size="12" fill="var(--text)">carbohydrate 1.0-1.2 g/kg/h for the first</text>
<text x="40" y="188" font-size="12" fill="var(--text)">several hours</text>
<text x="40" y="208" font-size="12" fill="var(--text)">protein 0.3-0.4 g/kg per serving</text>
<text x="40" y="228" font-size="12" fill="var(--text)">fluid 125-150% of the deficit, WITH sodium</text>
<text x="40" y="244" font-size="11" fill="var(--text-dim)">appetite is suppressed &#8212; go liquid in the first hour</text>
<rect x="360" y="132" width="314" height="118" rx="8" fill="var(--good)" opacity="0.12"/>
<text x="374" y="152" font-size="12" fill="var(--text)">TOTALS MATTER, NOT THE CLOCK</text>
<text x="374" y="174" font-size="12" fill="var(--text)">total DAILY carbohydrate dominates the</text>
<text x="374" y="188" font-size="12" fill="var(--text)">timing of the first feed</text>
<text x="374" y="208" font-size="12" fill="var(--text)">total daily protein dominates too</text>
<text x="374" y="228" font-size="12" fill="var(--text)">the 30-minute window is largely irrelevant</text>
<text x="374" y="244" font-size="11" fill="var(--text-dim)">return to normal eating patterns quickly</text>
<line x1="26" y1="264" x2="674" y2="264" stroke="var(--border)"/>
<text x="26" y="280" font-size="12" fill="var(--bad)">the two self-inflicted delays</text>
<text x="26" y="298" font-size="12" fill="var(--text)">ALCOHOL &#8212; impairs glycogen resynthesis, muscle protein synthesis and rehydration, and wrecks sleep</text>
<text x="26" y="314" font-size="12" fill="var(--text)">ENERGY RESTRICTION &#8212; &#8220;earning&#8221; a rest week by eating less blocks repair and immunity</text>
<text x="26" y="334" font-size="11" fill="var(--text-dim)">Plain water after a big sweat loss promotes diuresis and delays rehydration.</text>
<text x="26" y="348" font-size="11" fill="var(--text-dim)">Eccentric stations &#8212; lunges, wall balls, sled deceleration &#8212; lengthen the repair timeline.</text>
</svg>''', "The anabolic window only matters when the next hard effort is close; otherwise daily totals, sodium with the fluid, and no alcohol do the work.")


def d_sm_illness():
    return _wrap("dg-sm_illness", "The neck check, and the one sign that overrides it", '''<svg viewBox="0 0 700 352" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Neck check decision rule with systemic symptoms overriding, and the fever to myocarditis chain">
<defs><marker id="sm_illness-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker>
<marker id="sm_illness-bad" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--bad)"/></marker></defs>
<text x="26" y="18" font-size="12" fill="var(--text-dim)">the neck check &#8212; a practical heuristic, read from the top down</text>
<rect x="26" y="28" width="300" height="62" rx="8" fill="var(--good)" opacity="0.12"/>
<text x="40" y="48" font-size="12" fill="var(--text)">ABOVE the neck only</text>
<text x="40" y="66" font-size="11" fill="var(--text-dim)">mild sore throat, nasal congestion,</text>
<text x="40" y="80" font-size="11" fill="var(--text-dim)">sneezing &#8212; and no fever</text>
<line x1="26" y1="100" x2="326" y2="100" stroke="var(--text)" stroke-width="2" stroke-dasharray="8 5"/>
<text x="330" y="104" font-size="11" fill="var(--text-dim)">the neck line</text>
<rect x="26" y="110" width="300" height="62" rx="8" fill="var(--bad)" opacity="0.12"/>
<text x="40" y="130" font-size="12" fill="var(--text)">BELOW the neck</text>
<text x="40" y="148" font-size="11" fill="var(--text-dim)">productive cough, chest tightness,</text>
<text x="40" y="162" font-size="11" fill="var(--text-dim)">breathlessness, vomiting or diarrhoea</text>
<line x1="180" y1="90" x2="180" y2="106" stroke="var(--good)" stroke-width="0"/>
<path d="M330 58 L364 58" fill="none" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#sm_illness-a)"/>
<path d="M330 140 L364 140" fill="none" stroke="var(--bad)" stroke-width="1.5" marker-end="url(#sm_illness-bad)"/>
<text x="372" y="50" font-size="12" fill="var(--good)">train reduced, and review daily</text>
<text x="372" y="66" font-size="11" fill="var(--text-dim)">cut intensity and volume FIRST, reassess</text>
<text x="372" y="80" font-size="11" fill="var(--text-dim)">daily &#8212; do not push through to the plan</text>
<text x="372" y="136" font-size="12" fill="var(--bad)">DO NOT TRAIN</text>
<text x="372" y="154" font-size="11" fill="var(--text-dim)">exertional red flags &#8212; chest pain,</text>
<text x="372" y="168" font-size="11" fill="var(--text-dim)">palpitations, syncope &#8212; need assessment</text>
<rect x="26" y="184" width="648" height="46" rx="8" fill="var(--bad)" opacity="0.16"/>
<text x="40" y="204" font-size="12" fill="var(--text)">ANY SYSTEMIC SIGN OVERRIDES THE CHECK &#8212; fever, muscle aches, unusual fatigue, swollen glands: STOP,</text>
<text x="40" y="220" font-size="12" fill="var(--text)">wherever the local symptoms sit. Fever is an absolute contraindication and no athlete races with it.</text>
<text x="26" y="250" font-size="11" fill="var(--text-dim)">why fever is absolute &#8212; it is the sign that the illness is systemic</text>
<rect x="26" y="256" width="354" height="30" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="203" y="275" font-size="11" fill="var(--text)" text-anchor="middle">training through a systemic viral illness (fever)</text>
<line x1="382" y1="271" x2="404" y2="271" stroke="var(--bad)" stroke-width="1.5" marker-end="url(#sm_illness-bad)"/>
<rect x="408" y="256" width="120" height="30" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="468" y="275" font-size="11" fill="var(--text)" text-anchor="middle">myocarditis</text>
<line x1="530" y1="271" x2="552" y2="271" stroke="var(--bad)" stroke-width="1.5" marker-end="url(#sm_illness-bad)"/>
<rect x="556" y="256" width="118" height="30" rx="5" fill="var(--bad)" opacity="0.18"/>
<text x="615" y="271" font-size="11" fill="var(--text)" text-anchor="middle">rare, but a cause of</text>
<text x="615" y="283" font-size="11" fill="var(--text)" text-anchor="middle">sudden cardiac death</text>
<line x1="26" y1="300" x2="674" y2="300" stroke="var(--border)"/>
<text x="26" y="316" font-size="12" fill="var(--text)">GRADED RETURN: fever-free and symptom-free first, then a progressive rebuild.</text>
<text x="26" y="332" font-size="11" fill="var(--text)">Allow as many easy days as days missed, longer after fever; a high HR at easy pace means you rushed it.</text>
<text x="26" y="346" font-size="11" fill="var(--text-dim)">Prevention: sleep, energy availability, hygiene, no shared bottles. Check OTC remedies for restricted substances.</text>
</svg>''', "Above the neck and no fever buys a reduced session; below the neck or any systemic sign stops it - and fever is absolute, because of myocarditis.")


def d_mp_threat():
    return _wrap("dg-mp_threat", "Threat appraisal to race-day failure, and the two ways back", '''<svg viewBox="0 4 700 356" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Causal chain from threat appraisal through arousal, narrowed attention and shrunken working memory to typical race failures, with down-regulation and attention tools">
<defs><marker id="mp_threat-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker></defs>
<text x="26" y="18" font-size="12" fill="var(--text-dim)">three brain functions under pressure: threat appraisal &#183; attentional allocation &#183; executive control</text>
<rect x="26" y="28" width="120" height="90" rx="8" fill="var(--bad)" opacity="0.14"/>
<text x="86" y="66" font-size="12" fill="var(--text)" text-anchor="middle">threat</text>
<text x="86" y="82" font-size="12" fill="var(--text)" text-anchor="middle">appraisal</text>
<line x1="150" y1="73" x2="176" y2="73" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#mp_threat-a)"/>
<rect x="182" y="28" width="196" height="26" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="280" y="46" font-size="12" fill="var(--text)" text-anchor="middle">sympathetic arousal rises</text>
<rect x="182" y="60" width="196" height="26" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="280" y="78" font-size="12" fill="var(--text)" text-anchor="middle">attention narrows</text>
<rect x="182" y="92" width="196" height="26" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="280" y="110" font-size="12" fill="var(--text)" text-anchor="middle">working memory shrinks</text>
<line x1="382" y1="73" x2="408" y2="73" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#mp_threat-a)"/>
<rect x="414" y="28" width="260" height="90" rx="8" fill="var(--bad)" opacity="0.10"/>
<text x="428" y="46" font-size="11" fill="var(--text)">going out too hard</text>
<text x="428" y="62" font-size="11" fill="var(--text)">forgetting the pacing plan</text>
<text x="428" y="78" font-size="11" fill="var(--text)">fixating on a competitor</text>
<text x="428" y="94" font-size="11" fill="var(--text)">over-gripping already-automatic technique</text>
<text x="428" y="112" font-size="11" fill="var(--text-dim)">rehearsed routines survive; complex plans do not</text>
<line x1="26" y1="132" x2="674" y2="132" stroke="var(--border)"/>
<text x="26" y="150" font-size="12" fill="var(--text)">1. DOWN-REGULATE THE PHYSIOLOGY</text>
<rect x="26" y="158" width="300" height="22" rx="11" fill="var(--good)" opacity="0.14"/>
<text x="40" y="173" font-size="11" fill="var(--text)">breathe with the belly, not chest and shoulders</text>
<rect x="26" y="184" width="300" height="22" rx="11" fill="var(--good)" opacity="0.14"/>
<text x="40" y="199" font-size="11" fill="var(--text)">make the exhale longer than the inhale</text>
<rect x="26" y="210" width="300" height="22" rx="11" fill="var(--good)" opacity="0.14"/>
<text x="40" y="225" font-size="11" fill="var(--text)">box breathing: in 4, hold 4, out 4, hold 4</text>
<rect x="26" y="236" width="300" height="22" rx="11" fill="var(--good)" opacity="0.14"/>
<text x="40" y="251" font-size="11" fill="var(--text)">body scan: soften tension by just 5-10%</text>
<text x="26" y="274" font-size="11" fill="var(--text-dim)">&#8220;Relax&#8221; often backfires; a countable protocol also occupies attention.</text>
<text x="350" y="150" font-size="12" fill="var(--text)">2. REDIRECT ATTENTION</text>
<text x="364" y="172" font-size="11" fill="var(--text)">a pre-rehearsed cue word, or a physical anchor</text>
<text x="364" y="188" font-size="11" fill="var(--text)">(a touch of the wrist, eyes to a fixed point)</text>
<text x="364" y="210" font-size="11" fill="var(--text)">keep focus EXTERNAL and task-relevant</text>
<text x="364" y="232" font-size="11" fill="var(--text)">reappraise: &#8220;this racing heart means I am ready&#8221;</text>
<text x="364" y="248" font-size="11" fill="var(--text-dim)">&#8212; suppression tends to raise arousal instead</text>
<text x="364" y="274" font-size="11" fill="var(--text-dim)">Not all arousal is bad: aim for the athlete&#8217;s own zone.</text>
<line x1="26" y1="286" x2="674" y2="286" stroke="var(--border)"/>
<path d="M40 342 C74 342 84 310 122 310 C160 310 170 342 204 342" fill="none" stroke="var(--theme-accent)" stroke-width="2"/>
<rect x="98" y="304" width="48" height="38" fill="var(--good)" opacity="0.18"/>
<text x="122" y="302" font-size="11" fill="var(--text)" text-anchor="middle">optimal zone</text>
<text x="34" y="322" font-size="11" fill="var(--text-dim)" text-anchor="middle" transform="rotate(-90 34 322)">performance</text>
<text x="48" y="356" font-size="11" fill="var(--text-dim)">low</text>
<text x="196" y="356" font-size="11" fill="var(--text-dim)">high arousal</text>
<text x="278" y="310" font-size="12" fill="var(--warn)">Some athletes need UP-regulation before a race, not calming.</text>
<text x="278" y="330" font-size="12" fill="var(--warn)">These are trained skills, not an emergency umbrella opened the night</text>
<text x="278" y="346" font-size="12" fill="var(--warn)">before a race &#8212; rehearse them under fatigue and mild pressure.</text>
</svg>''', "Pressure narrows attention and shrinks working memory, so lengthen the exhale to drop arousal and let one rehearsed cue carry the plan.")


def d_pc_adapted():
    return _wrap("dg-pc_adapted", "Substitute the movement, keep the training intent", '''<svg viewBox="0 0 700 356" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Table mapping each HYROX station to the training intent that must survive a substitution, beside the population-specific medical considerations">
<defs><marker id="pc_adapted-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--theme-accent)"/></marker></defs>
<text x="26" y="18" font-size="12" fill="var(--text-dim)">classify by FUNCTION, not diagnosis &#8212; the same label can mean entirely different capacities</text>
<text x="26" y="40" font-size="11" fill="var(--text-dimmer)">STATION</text>
<text x="200" y="40" font-size="11" fill="var(--text-dimmer)">THE INTENT THAT MUST SURVIVE THE SUBSTITUTION</text>
<line x1="26" y1="46" x2="674" y2="46" stroke="var(--border)"/>
<g font-size="11">
<text x="26" y="64" fill="var(--text)">SkiErg / Row</text><text x="200" y="64" fill="var(--text-dim)">upper-body and trunk aerobic-strength endurance</text>
<text x="26" y="86" fill="var(--text)">Sleds</text><text x="200" y="86" fill="var(--text-dim)">heavy horizontal push and pull strength-endurance</text>
<text x="26" y="108" fill="var(--text)">Burpee broad jump</text><text x="200" y="108" fill="var(--text-dim)">whole-body cyclical power with a floor transition</text>
<text x="26" y="130" fill="var(--text)">Farmers carry</text><text x="200" y="130" fill="var(--text-dim)">grip and trunk stiffness under load</text>
<text x="26" y="152" fill="var(--text)">Sandbag lunges</text><text x="200" y="152" fill="var(--text-dim)">unilateral leg endurance</text>
<text x="26" y="174" fill="var(--text)">Wall balls</text><text x="200" y="174" fill="var(--text-dim)">repeated squat-to-overhead local muscular endurance</text>
</g>
<line x1="26" y1="184" x2="674" y2="184" stroke="var(--border)"/>
<text x="26" y="202" font-size="11" fill="var(--text)">substitute freely, but match the energy system, the muscular demand and the duration</text>
<line x1="500" y1="198" x2="530" y2="198" stroke="var(--theme-accent)" stroke-width="1.5" marker-end="url(#pc_adapted-a)"/>
<text x="538" y="202" font-size="11" fill="var(--text-dim)">intent preserved</text>
<rect x="26" y="212" width="648" height="34" rx="6" fill="var(--warn)" opacity="0.14"/>
<text x="40" y="234" font-size="12" fill="var(--text)">The commonest failure is not unsafe programming &#8212; it is LOW EXPECTATION: adapted athletes are under-loaded.</text>
<rect x="26" y="256" width="648" height="46" rx="6" fill="var(--bad)" opacity="0.14"/>
<text x="40" y="274" font-size="11" fill="var(--text)">AUTONOMIC DYSREFLEXIA (spinal cord injury around T6 and above): pounding headache, flushing, sweating above</text>
<text x="40" y="292" font-size="11" fill="var(--text)">the lesion, bradycardia. Stop &#183; sit upright &#183; remove the trigger &#183; get help. Boosting is prohibited and dangerous.</text>
<text x="26" y="320" font-size="11" fill="var(--text-dim)">Thermoregulation is impaired below the lesion &#8212; plan cooling, shorter heat exposure and frequent fluid access.</text>
<text x="26" y="334" font-size="11" fill="var(--text-dim)">Wheelchair shoulders: balance pushing with posterior-chain and scapular work; guard skin and pressure points.</text>
<text x="26" y="348" font-size="11" fill="var(--text-dim)">Visual impairment: verbal and tactile cues, a fixed layout. Socket tolerance caps volume. Refer early.</text>
</svg>''', "Adapted coaching keeps each station's physiological intent and lets the movement change - and the usual error is expecting too little, not too much.")


def d_cm_athletedev():
    return _wrap("dg-cm_athletedev", "One recovery budget, and the culture that keeps people in", '''<svg viewBox="0 0 700 352" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Five life stressors drawing on a single recovery budget, the four retention levers, and the culture red flags">
<defs><marker id="cm_athletedev-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="var(--warn)"/></marker></defs>
<text x="26" y="18" font-size="12" fill="var(--text-dim)">the biopsychosocial lens: biological, psychological and social factors interact &#8212; fitness metrics alone predict less</text>
<g font-size="11" fill="var(--text)" text-anchor="middle">
<rect x="26" y="34" width="112" height="26" rx="6" fill="var(--surface-2)" stroke="var(--border)"/><text x="82" y="51">training</text>
<rect x="152" y="34" width="112" height="26" rx="6" fill="var(--surface-2)" stroke="var(--border)"/><text x="208" y="51">work</text>
<rect x="278" y="34" width="112" height="26" rx="6" fill="var(--surface-2)" stroke="var(--border)"/><text x="334" y="51">family</text>
<rect x="404" y="34" width="112" height="26" rx="6" fill="var(--surface-2)" stroke="var(--border)"/><text x="460" y="51">finances</text>
<rect x="530" y="34" width="144" height="26" rx="6" fill="var(--surface-2)" stroke="var(--border)"/><text x="602" y="51">poor sleep</text>
</g>
<g stroke="var(--warn)" stroke-width="1.5" marker-end="url(#cm_athletedev-a)">
<line x1="82" y1="62" x2="82" y2="94"/><line x1="208" y1="62" x2="208" y2="94"/><line x1="334" y1="62" x2="334" y2="94"/>
<line x1="460" y1="62" x2="460" y2="94"/><line x1="602" y1="62" x2="602" y2="94"/>
</g>
<rect x="26" y="100" width="648" height="34" rx="6" fill="var(--theme-accent)" opacity="0.16"/>
<text x="350" y="122" font-size="13" fill="var(--text)" text-anchor="middle">ONE finite recovery budget (allostatic load)</text>
<text x="26" y="152" font-size="12" fill="var(--text)">A heavy life-stress week is a programming input: cut weekly training load by roughly 20-30%,</text>
<text x="26" y="168" font-size="12" fill="var(--text)">agreed with the athlete in advance. It is a practical heuristic, not a published model.</text>
<line x1="26" y1="182" x2="674" y2="182" stroke="var(--border)"/>
<text x="26" y="200" font-size="12" fill="var(--text)">FOUR RETENTION LEVERS</text>
<g font-size="11" fill="var(--text)" text-anchor="middle">
<rect x="26" y="210" width="150" height="28" rx="14" fill="var(--good)" opacity="0.16"/><text x="101" y="228">belonging</text>
<rect x="190" y="210" width="150" height="28" rx="14" fill="var(--good)" opacity="0.16"/><text x="265" y="228">visible progress</text>
<rect x="354" y="210" width="150" height="28" rx="14" fill="var(--good)" opacity="0.16"/><text x="429" y="228">shared effort</text>
<rect x="518" y="210" width="156" height="28" rx="14" fill="var(--good)" opacity="0.16"/><text x="596" y="228">celebration rituals</text>
</g>
<text x="26" y="256" font-size="11" fill="var(--text-dim)">belonging feeds RELATEDNESS and visible progress feeds COMPETENCE (self-determination theory).</text>
<text x="26" y="272" font-size="11" fill="var(--text-dim)">Athlete education multiplies the coach: knowing why a session exists, athletes self-regulate when you are away.</text>
<line x1="26" y1="284" x2="674" y2="284" stroke="var(--border)"/>
<rect x="26" y="292" width="318" height="52" rx="6" fill="var(--bad)" opacity="0.12"/>
<text x="38" y="310" font-size="12" fill="var(--text)">CULTURE RED FLAGS</text>
<text x="38" y="326" font-size="11" fill="var(--text-dim)">a leaderboard-only culture keeps the fast and</text>
<text x="38" y="338" font-size="11" fill="var(--text-dim)">quietly loses everyone else; overtraining as a badge</text>
<rect x="356" y="292" width="318" height="52" rx="6" fill="var(--theme-accent)" opacity="0.12"/>
<text x="368" y="310" font-size="12" fill="var(--text)">MULTI-YEAR PROJECTS</text>
<text x="368" y="326" font-size="11" fill="var(--text-dim)">aerobic base, strength reserve, station skill floors</text>
<text x="368" y="338" font-size="11" fill="var(--text-dim)">&#8212; race-to-race planning systematically undermines them</text>
</svg>''', "Work, family, finances and sleep draw on the same budget as training, so a heavy life week is a planned 20-30% load cut, not a failure of discipline.")


def d_xs_periodization():
    return _wrap("dg-xs_periodization", "Macrocycle, taper and the interference effect", '''<svg viewBox="0 4 700 356" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Four-phase HYROX macrocycle, a taper panel showing volume cut with intensity held, and the interference effect conditions">
<text x="26" y="18" font-size="12" fill="var(--text-dim)">a practical HYROX macrocycle &#8212; structure beats no structure, and adherence outweighs the model</text>
<rect x="26" y="28" width="180" height="34" rx="5" fill="var(--theme-accent)" opacity="0.14"/>
<rect x="212" y="28" width="180" height="34" rx="5" fill="var(--theme-accent)" opacity="0.22"/>
<rect x="398" y="28" width="180" height="34" rx="5" fill="var(--theme-accent)" opacity="0.32"/>
<rect x="584" y="28" width="90" height="34" rx="5" fill="var(--theme-accent)" opacity="0.10"/>
<g font-size="12" fill="var(--text)" text-anchor="middle">
<text x="116" y="49">general prep</text><text x="302" y="49">specific prep</text><text x="488" y="49">competition</text><text x="629" y="49">transition</text>
</g>
<g font-size="11" fill="var(--text-dim)" text-anchor="middle">
<text x="116" y="78">maximal strength</text><text x="116" y="90">+ aerobic base</text>
<text x="302" y="78">station endurance +</text><text x="302" y="90">compromised running</text>
<text x="488" y="78">race simulations</text><text x="488" y="90">then the taper</text>
</g>
<line x1="26" y1="104" x2="674" y2="104" stroke="var(--border)"/>
<text x="26" y="122" font-size="12" fill="var(--text)">THE TAPER</text>
<line x1="60" y1="212" x2="60" y2="134" stroke="var(--border)" stroke-width="1.5"/>
<line x1="60" y1="212" x2="320" y2="212" stroke="var(--border)" stroke-width="1.5"/>
<line x1="60" y1="179" x2="320" y2="179" stroke="var(--border)" stroke-dasharray="3 4"/>
<text x="56" y="150" font-size="11" fill="var(--text-dimmer)" text-anchor="end">100%</text>
<text x="56" y="183" font-size="11" fill="var(--text-dimmer)" text-anchor="end">50%</text>
<text x="56" y="216" font-size="11" fill="var(--text-dimmer)" text-anchor="end">0</text>
<path d="M70 141 L310 141" fill="none" stroke="var(--good)" stroke-width="2.5" stroke-dasharray="6 4"/>
<path d="M70 146 L150 146 L230 176 L310 179" fill="none" stroke="var(--theme-accent)" stroke-width="2.5"/>
<text x="70" y="206" font-size="11" fill="var(--theme-accent)">volume &#8722;40-60% of the peak week</text>
<text x="306" y="159" font-size="11" fill="var(--good)" text-anchor="end">intensity held</text>
<text x="66" y="228" font-size="11" fill="var(--text-dim)">cut over the last 1-2 weeks before an A race</text>
<text x="66" y="242" font-size="11" fill="var(--text-dim)">intensity AND frequency held; typical gain 1-3%</text>
<text x="26" y="258" font-size="11" fill="var(--bad)">commonest error: cutting INTENSITY,</text>
<text x="26" y="270" font-size="11" fill="var(--bad)">not volume &#8212; race sharpness then fades</text>
<line x1="340" y1="112" x2="340" y2="268" stroke="var(--border)"/>
<text x="356" y="122" font-size="12" fill="var(--text)">THE INTERFERENCE EFFECT</text>
<text x="356" y="140" font-size="11" fill="var(--text-dim)">endurance blunts strength and hypertrophy &#8212; the molecular</text>
<text x="356" y="152" font-size="11" fill="var(--text-dim)">story is plausible but not settled. It bites most when:</text>
<text x="356" y="172" font-size="11" fill="var(--text)">endurance volume is high</text>
<text x="356" y="188" font-size="11" fill="var(--text)">same-muscle endurance runs straight before lifting</text>
<text x="356" y="204" font-size="11" fill="var(--text)">the key lifting is done glycogen-depleted</text>
<text x="356" y="226" font-size="11" fill="var(--good)">manage it: lift first when strength is the priority &#183; separate</text>
<text x="356" y="238" font-size="11" fill="var(--good)">sessions by roughly six hours &#183; move volume off-feet</text>
<text x="356" y="258" font-size="11" fill="var(--text-dim)">&#8212; do not avoid concurrent training, sequence it</text>
<line x1="26" y1="276" x2="674" y2="276" stroke="var(--border)"/>
<rect x="26" y="284" width="318" height="52" rx="6" fill="var(--warn)" opacity="0.16"/>
<text x="38" y="304" font-size="12" fill="var(--text)">Polarised ~80/20 is an INTENSITY DISTRIBUTION,</text>
<text x="38" y="326" font-size="12" fill="var(--text)">not a periodization model &#8212; a classic exam trap.</text>
<text x="356" y="298" font-size="11" fill="var(--text)">A race: full taper &#183; B: 3-7 day mini-taper &#183; C: train through</text>
<text x="356" y="314" font-size="11" fill="var(--text-dim)">Strength decays over weeks, so low-volume weekly touches</text>
<text x="356" y="326" font-size="11" fill="var(--text-dim)">at moderate-to-high intensity hold it between races.</text>
<text x="26" y="344" font-size="11" fill="var(--text-dim)">Linear: volume &#8594; intensity across long phases. Block: one quality per mesocycle (accumulation, transmutation,</text>
<text x="26" y="356" font-size="11" fill="var(--text-dim)">realisation) held by residual effects. DUP: varies within the week, which suits concurrent-demand HYROX.</text>
</svg>''', "Cut taper VOLUME by 40-60% and hold intensity - and remember polarised describes the intensity mix, never the sequence of phases.")


DIAGRAMS = {
    "of_testmatrix": d_of_testmatrix,
    "hp_roxzone": d_hp_roxzone,
    "st_row": d_st_row,
    "rb_braking": d_rb_braking,
    "st_lunge": d_st_lunge,
    "hp_profiling": d_hp_profiling,
    "sk_practice_design": d_sk_practice_design,
    "nu_postcomp": d_nu_postcomp,
    "sm_illness": d_sm_illness,
    "mp_threat": d_mp_threat,
    "pc_adapted": d_pc_adapted,
    "cm_athletedev": d_cm_athletedev,
    "xs_periodization": d_xs_periodization,
}
