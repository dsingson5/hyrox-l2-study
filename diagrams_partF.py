# -*- coding: utf-8 -*-
"""Bespoke lesson diagrams - batch F."""


def _wrap(did, title, body, caption=""):
    cap = f'<div class="w-hint">{caption}</div>' if caption else ""
    return (f'<div class="widget diagram" id="{did}">'
            f'<div class="w-head"><span class="w-icon">' + chr(9672) + f'</span><span class="w-title">{title}</span></div>'
            f'<div class="w-body">{body}</div>{cap}</div>')


# Shared snippet: reduced-motion guard for SMIL groups. It disables the animation
# only, never the static geometry inside the animated group - the same rule the other
# modules use. CSS cannot stop SMIL on its own, so it has to reach the <animate*>
# elements themselves, and it is scoped so it cannot blank another diagram's group.
_RM = ('<style>@media (prefers-reduced-motion: reduce){'
       '.dg-anim animate,.dg-anim animateMotion,.dg-anim animateTransform{display:none}}'
       '</style>')


# ---------------------------------------------------------------- day 122
def d_of_decisiontree():
    return _wrap(
        "dg-of_decisiontree",
        "Off-feet: the order of the questions",
        '''<svg viewBox="0 0 700 356" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px;display:block" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="A six-step off-feet decision ladder from availability through objective to modality, beside cards comparing the bike, the rower and SkiErg, and the curved treadmill">
''' + _RM + '''
<line x1="13" y1="26" x2="13" y2="255" stroke="var(--border)" stroke-width="2"/>
<g class="dg-anim"><circle cx="13" cy="31" r="5.5" fill="var(--theme-accent)"><animate attributeName="cy" values="31;75;119;163;207;251;31" dur="12s" repeatCount="indefinite" calcMode="discrete"/></circle></g>

<rect x="26" y="12" width="292" height="38" rx="7" fill="var(--surface)" stroke="var(--border)"/>
<circle cx="46" cy="31" r="11" fill="var(--theme-accent)"/><text x="46" y="35" font-size="12" font-weight="700" fill="var(--bg)" text-anchor="middle">1</text>
<text x="64" y="28" font-size="12" font-weight="600" fill="var(--text)">Is running available today?</text>
<text x="64" y="43" font-size="11" fill="var(--text-dim)">triage / impact-load budget / bone-stress history</text>
<path d="M168 52 l4 4 l4 -4" fill="none" stroke="var(--text-dimmer)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>

<rect x="26" y="56" width="292" height="38" rx="7" fill="var(--surface)" stroke="var(--border)"/>
<circle cx="46" cy="75" r="11" fill="var(--theme-accent)"/><text x="46" y="79" font-size="12" font-weight="700" fill="var(--bg)" text-anchor="middle">2</text>
<text x="64" y="72" font-size="12" font-weight="600" fill="var(--text)">What quality is this session buying?</text>
<text x="64" y="87" font-size="11" fill="var(--text-dim)">Z2 volume, threshold, VO2 or sprint power</text>
<path d="M168 96 l4 4 l4 -4" fill="none" stroke="var(--text-dimmer)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>

<rect x="26" y="100" width="292" height="38" rx="7" fill="var(--surface)" stroke="var(--theme-accent)" stroke-width="1.8"/>
<circle cx="46" cy="119" r="11" fill="var(--theme-accent)"/><text x="46" y="123" font-size="12" font-weight="700" fill="var(--bg)" text-anchor="middle">3</text>
<text x="64" y="116" font-size="12" font-weight="600" fill="var(--text)">Which modality fits?</text>
<text x="64" y="131" font-size="11" fill="var(--text-dim)">the THIRD question, never the first</text>
<path d="M168 140 l4 4 l4 -4" fill="none" stroke="var(--text-dimmer)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>

<rect x="26" y="144" width="292" height="38" rx="7" fill="var(--surface)" stroke="var(--border)"/>
<circle cx="46" cy="163" r="11" fill="var(--theme-accent)"/><text x="46" y="167" font-size="12" font-weight="700" fill="var(--bg)" text-anchor="middle">4</text>
<text x="64" y="160" font-size="12" font-weight="600" fill="var(--text)">Convert the dose</text>
<text x="64" y="175" font-size="11" fill="var(--text-dim)">by duration and RPE - never by distance</text>
<path d="M168 184 l4 4 l4 -4" fill="none" stroke="var(--text-dimmer)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>

<rect x="26" y="188" width="292" height="38" rx="7" fill="var(--surface)" stroke="var(--border)"/>
<circle cx="46" cy="207" r="11" fill="var(--theme-accent)"/><text x="46" y="211" font-size="12" font-weight="700" fill="var(--bg)" text-anchor="middle">5</text>
<text x="64" y="204" font-size="12" font-weight="600" fill="var(--text)">Schedule the route back</text>
<text x="64" y="219" font-size="11" fill="var(--text-dim)">short easy runs return, erg volume stays up</text>
<path d="M168 228 l4 4 l4 -4" fill="none" stroke="var(--text-dimmer)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>

<rect x="26" y="232" width="292" height="38" rx="7" fill="var(--surface)" stroke="var(--border)"/>
<circle cx="46" cy="251" r="11" fill="var(--theme-accent)"/><text x="46" y="255" font-size="12" font-weight="700" fill="var(--bg)" text-anchor="middle">6</text>
<text x="64" y="248" font-size="12" font-weight="600" fill="var(--text)">Verify the transfer</text>
<text x="64" y="263" font-size="11" fill="var(--text-dim)">run economy and compromised running</text>

<path d="M322 119 H330 V139 H336" fill="none" stroke="var(--text-dim)" stroke-width="1.4"/>
<path d="M334 135 l7 4 l-7 4 z" fill="var(--text-dim)"/>

<rect x="344" y="12" width="348" height="78" rx="7" fill="var(--surface)" stroke="var(--border)"/>
<rect x="344" y="12" width="4" height="78" rx="2" fill="var(--theme-accent)"/>
<text x="358" y="32" font-size="12" font-weight="700" fill="var(--theme-accent)">BIKE - the default</text>
<text x="358" y="50" font-size="11" fill="var(--text)">no impact, no skill gate: quality holds deep in fatigue</text>
<text x="358" y="66" font-size="11" fill="var(--text)">watts are the most precisely dosed intensity available</text>
<text x="358" y="82" font-size="11" fill="var(--text-dim)">weakness: no bike in a HYROX - transfer is central only</text>

<rect x="344" y="100" width="348" height="78" rx="7" fill="var(--surface)" stroke="var(--border)"/>
<rect x="344" y="100" width="4" height="78" rx="2" fill="var(--good)"/>
<text x="358" y="120" font-size="12" font-weight="700" fill="var(--good)">ROWER / SKIERG - the specific ones</text>
<text x="358" y="138" font-size="11" fill="var(--text)">they ARE the race: SkiErg first station, rower fifth</text>
<text x="358" y="154" font-size="11" fill="var(--text)">trunk, lats, grip, hinge - minutes double as rehearsal</text>
<text x="358" y="170" font-size="11" fill="var(--text-dim)">skill-gated: novice or deeply fatigued, quality collapses</text>

<rect x="344" y="188" width="348" height="78" rx="7" fill="var(--surface)" stroke="var(--border)"/>
<rect x="344" y="188" width="4" height="78" rx="2" fill="var(--bad)"/>
<text x="358" y="208" font-size="12" font-weight="700" fill="var(--bad)">CURVED TREADMILL - not off-feet at all</text>
<text x="358" y="226" font-size="11" fill="var(--text)">up to speed almost instantly: a sprint and high-HR tool</text>
<text x="358" y="242" font-size="11" fill="var(--text)">but it is running, constant uphill: calf, Achilles, shin</text>
<text x="358" y="258" font-size="11" fill="var(--text-dim)">sprint branch only - never the injury branch</text>

<line x1="12" y1="280" x2="692" y2="280" stroke="var(--border)"/>
<text x="12" y="294" font-size="11" font-weight="600" fill="var(--text)">The official one-page tree is benchmark-first: benchmarked? -&gt; risk-stratify -&gt;</text>
<text x="12" y="307" font-size="11" font-weight="600" fill="var(--text)">submaximal test -&gt; power profile -&gt; plan? -&gt; 4 branches</text>
<text x="12" y="323" font-size="11" fill="var(--text-dim)">general CRF -&gt; 12-week plans by fitness percentile: 0-30 beginner 1 / 31-50 beginner 2 / 51-70 intermediate / above 70 advanced</text>
<text x="12" y="336" font-size="11" fill="var(--text-dim)">return from injury -&gt; pedal effectiveness around 75, left-right deficit under 10 pct, before impact work rebuilds</text>
<text x="12" y="349" font-size="11" fill="var(--text-dim)">aerobic power -&gt; Z1-Z6 as pct of max minute power and max HR | sprint -&gt; 120-130 rpm, 2 levels down; 6-s check, 15 pct drop = fatigue</text>
</svg>''',
        "Availability, then objective, then the machine - equipment preference must never pick the objective.")


def d_pc_doubles():
    return _wrap(
        "dg-pc_doubles",
        "Doubles: what halves, what does not",
        '''<svg viewBox="0 0 700 346" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px;display:block" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="A doubles race strip showing which segments halve and which do not, with a changeover-cost panel and per-athlete comparison against the individual race">
''' + _RM + '''
<text x="14" y="20" font-size="12" font-weight="700" fill="var(--text)">Per athlete, against the individual race</text>
<text x="14" y="36" font-size="11" fill="var(--text-dimmer)">relative, schematic - no scale implied</text>
<rect x="14" y="44" width="12" height="10" fill="var(--text-dimmer)"/><text x="32" y="53" font-size="11" fill="var(--text-dim)">individual</text>
<rect x="108" y="44" width="12" height="10" fill="var(--theme-accent)"/><text x="126" y="53" font-size="11" fill="var(--text-dim)">doubles</text>

<line x1="22" y1="250" x2="336" y2="250" stroke="var(--border)" stroke-width="1.5"/>
<rect x="48" y="140" width="24" height="110" fill="var(--text-dimmer)" opacity="0.55"/>
<rect x="80" y="140" width="24" height="110" fill="var(--theme-accent)"/>
<text x="76" y="268" font-size="11.5" font-weight="600" fill="var(--text)" text-anchor="middle">running</text>
<text x="76" y="283" font-size="11" fill="var(--good)" text-anchor="middle">8 km - unchanged</text>
<text x="76" y="297" font-size="11" fill="var(--text-dim)" text-anchor="middle">both run every metre</text>

<rect x="152" y="140" width="24" height="110" fill="var(--text-dimmer)" opacity="0.55"/>
<rect x="184" y="195" width="24" height="55" fill="var(--theme-accent)"/>
<text x="180" y="268" font-size="11.5" font-weight="600" fill="var(--text)" text-anchor="middle">station volume</text>
<text x="180" y="283" font-size="11" fill="var(--warn)" text-anchor="middle">roughly halves</text>
<text x="180" y="297" font-size="11" fill="var(--text-dim)" text-anchor="middle">work is shared</text>

<rect x="256" y="180" width="24" height="70" fill="var(--text-dimmer)" opacity="0.55"/>
<rect x="288" y="132" width="24" height="118" fill="var(--theme-accent)"/>
<path d="M300 124 l0 -14 M296 116 l4 -6 l4 6" fill="none" stroke="var(--good)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="284" y="268" font-size="11.5" font-weight="600" fill="var(--text)" text-anchor="middle">station intensity</text>
<text x="284" y="283" font-size="11" fill="var(--good)" text-anchor="middle">rises sharply</text>
<text x="284" y="297" font-size="11" fill="var(--text-dim)" text-anchor="middle">bursts with recovery</text>

<text x="14" y="322" font-size="11" fill="var(--text)">So the profile shifts toward repeated high-intensity work and fast</text>
<text x="14" y="337" font-size="11" fill="var(--text)">recovery, not sustained moderate strength-endurance.</text>

<line x1="348" y1="10" x2="348" y2="336" stroke="var(--border)"/>

<text x="364" y="20" font-size="12" font-weight="700" fill="var(--text)">Every changeover costs time</text>
<text x="364" y="46" font-size="11" fill="var(--text-dim)">two big blocks</text>
<g class="dg-anim">
  <rect x="364" y="54" width="96" height="22" rx="3" fill="var(--theme-accent)"><animate attributeName="opacity" values="1;1;0.3;0.3;1" dur="7s" repeatCount="indefinite"/></rect>
  <rect x="460" y="54" width="96" height="22" rx="3" fill="var(--theme-accent)"><animate attributeName="opacity" values="0.3;0.3;1;1;0.3" dur="7s" repeatCount="indefinite"/></rect>
</g>
<rect x="364" y="54" width="192" height="22" rx="3" fill="none" stroke="var(--border)"/>
<path d="M460 50 v30" stroke="var(--warn)" stroke-width="2" fill="none"/>
<text x="562" y="69" font-size="11" fill="var(--text-dim)">1 swap</text>

<text x="364" y="106" font-size="11" fill="var(--text-dim)">many small alternations</text>
<rect x="364" y="114" width="234" height="22" rx="3" fill="var(--theme-accent)" opacity="0.35"/>
<rect x="364" y="114" width="234" height="22" rx="3" fill="none" stroke="var(--border)"/>
<path d="M396 110 v30 M428 110 v30 M460 110 v30 M492 110 v30 M524 110 v30" stroke="var(--warn)" stroke-width="1.6" fill="none"/>
<path d="M556 110 v30" stroke="var(--border)" stroke-dasharray="3 3" fill="none"/>
<rect x="556" y="114" width="42" height="22" fill="var(--bad)" opacity="0.28"/>
<text x="602" y="129" font-size="11" fill="var(--bad)">added</text>
<text x="364" y="154" font-size="11" fill="var(--text-dim)">Fewer, larger blocks are usually faster - unless fatigue forces it.</text>

<text x="364" y="184" font-size="11" fill="var(--text)">Pace-match first. The pair runs at the slower partner's</text>
<text x="364" y="199" font-size="11" fill="var(--text)">sustainable pace, so a mismatched faster partner under-works</text>
<text x="364" y="214" font-size="11" fill="var(--text)">for 8 km while the slower one runs over threshold.</text>
<text x="364" y="236" font-size="11" fill="var(--text)">Split asymmetrically where strengths differ: give the stronger</text>
<text x="364" y="251" font-size="11" fill="var(--text)">partner more sled push and pull - sled time is highly</text>
<text x="364" y="266" font-size="11" fill="var(--text)">sensitive to absolute strength.</text>
<text x="364" y="288" font-size="11" fill="var(--text)">Agree every split and the fallback in advance. Wall balls are</text>
<text x="364" y="303" font-size="11" fill="var(--text)">where pairs unravel: set the swap trigger as a rep count,</text>
<text x="364" y="318" font-size="11" fill="var(--text)">not a feeling. Calls stay short - complex talk fails at race pace.</text>
<text x="364" y="337" font-size="11" fill="var(--warn)">Early runs feel easy because stations were shared. That is the trap.</text>
</svg>''',
        "Running volume is untouched; only station work halves - and its intensity climbs.")


# ---------------------------------------------------------------- day 110
def d_st_wallball():
    return _wrap(
        "dg-st_wallball",
        "Wall balls: legs project, posture fails",
        '''<svg viewBox="0 5 700 360" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px;display:block" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Triple extension driving the wall-ball throw, the same athlete at rep 10 and rep 80 showing the postural failure, and the qualities to train">
''' + _RM + '''
<text x="12" y="20" font-size="12" font-weight="700" fill="var(--text)">Where the throw comes from</text>
<line x1="20" y1="300" x2="248" y2="300" stroke="var(--border)" stroke-width="2"/>
<line x1="150" y1="52" x2="242" y2="52" stroke="var(--text-dim)" stroke-width="3"/>
<text x="196" y="44" font-size="11" fill="var(--text-dim)" text-anchor="middle">target</text>

<path d="M76 300 L86 250 L100 202 L110 150" fill="none" stroke="var(--text)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="116" cy="136" r="11" fill="none" stroke="var(--text)" stroke-width="2.5"/>
<path d="M110 150 L132 170 L142 148" fill="none" stroke="var(--text)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="150" cy="130" r="13" fill="none" stroke="var(--theme-accent)" stroke-width="2.5"/>
<path d="M158 118 Q182 74 196 58" fill="none" stroke="var(--theme-accent)" stroke-width="1.6" stroke-dasharray="4 4"/>

<circle cx="76" cy="298" r="5" fill="var(--theme-accent)"/>
<circle cx="86" cy="250" r="5" fill="var(--theme-accent)"/>
<circle cx="100" cy="202" r="5" fill="var(--theme-accent)"/>
<text x="66" y="302" font-size="11" fill="var(--text-dim)" text-anchor="end">ankle</text>
<text x="76" y="254" font-size="11" fill="var(--text-dim)" text-anchor="end">knee</text>
<text x="90" y="206" font-size="11" fill="var(--text-dim)" text-anchor="end">hip</text>

<g class="dg-anim"><circle r="4.5" fill="var(--good)"><animateMotion path="M76 298 L86 250 L100 202 L110 150 L132 170 L150 130" dur="3.6s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;1;0" dur="3.6s" repeatCount="indefinite"/></circle></g>

<path d="M40 292 V186" fill="none" stroke="var(--theme-accent)" stroke-width="2.5"/>
<path d="M34 194 l6 -10 l6 10 z" fill="var(--theme-accent)"/>
<text x="28" y="250" font-size="11" font-weight="600" fill="var(--theme-accent)" text-anchor="middle" transform="rotate(-90 28 250)">triple extension</text>

<line x1="264" y1="14" x2="264" y2="300" stroke="var(--border)"/>

<text x="278" y="20" font-size="12" font-weight="700" fill="var(--text)">The fatigue failure is postural</text>
<path d="M320 240 L320 150" fill="none" stroke="var(--good)" stroke-width="3.5" stroke-linecap="round"/>
<circle cx="320" cy="134" r="10" fill="none" stroke="var(--text)" stroke-width="2.5"/>
<path d="M320 162 L300 158 L306 138 M320 162 L340 158 L334 138" fill="none" stroke="var(--good)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="320" cy="120" r="10" fill="none" stroke="var(--theme-accent)" stroke-width="2.5"/>
<text x="320" y="262" font-size="11" font-weight="600" fill="var(--good)" text-anchor="middle">rep 10</text>
<text x="320" y="277" font-size="11" fill="var(--text-dim)" text-anchor="middle">braced trunk,</text>
<text x="320" y="291" font-size="11" fill="var(--text-dim)" text-anchor="middle">elbows high</text>

<path d="M352 196 h22" stroke="var(--text-dim)" stroke-width="1.6" fill="none"/><path d="M372 192 l8 4 l-8 4 z" fill="var(--text-dim)"/>
<text x="363" y="184" font-size="11" fill="var(--text-dim)" text-anchor="middle">80</text>

<path d="M402 240 Q398 190 414 156" fill="none" stroke="var(--bad)" stroke-width="3.5" stroke-linecap="round"/>
<circle cx="424" cy="146" r="10" fill="none" stroke="var(--text)" stroke-width="2.5"/>
<path d="M412 160 L392 176 L400 186 M412 160 L430 176 L422 186" fill="none" stroke="var(--bad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="394" cy="124" r="10" fill="none" stroke="var(--theme-accent)" stroke-width="2.5" opacity="0.6"/>
<text x="408" y="262" font-size="11" font-weight="600" fill="var(--bad)" text-anchor="middle">rep 80</text>
<text x="408" y="277" font-size="11" fill="var(--text-dim)" text-anchor="middle">upper back rounds,</text>
<text x="408" y="291" font-size="11" fill="var(--text-dim)" text-anchor="middle">elbows drop forward</text>

<line x1="470" y1="14" x2="470" y2="300" stroke="var(--border)"/>

<text x="484" y="20" font-size="12" font-weight="700" fill="var(--text)">What to train</text>
<rect x="484" y="32" width="4" height="42" rx="2" fill="var(--theme-accent)"/>
<text x="496" y="46" font-size="11.5" font-weight="600" fill="var(--text)">Upper-back strength endurance</text>
<text x="496" y="61" font-size="11" fill="var(--text-dim)">scap depressions, prone Y-raises,</text>
<text x="496" y="74" font-size="11" fill="var(--text-dim)">cable face pulls - decisive over 100 reps</text>

<rect x="484" y="86" width="4" height="42" rx="2" fill="var(--theme-accent)"/>
<text x="496" y="100" font-size="11.5" font-weight="600" fill="var(--text)">Squat endurance</text>
<text x="496" y="115" font-size="11" fill="var(--text-dim)">barbell front squats; goblet squats with</text>
<text x="496" y="128" font-size="11" fill="var(--text-dim)">dumbbell or kettlebell for mechanics</text>

<rect x="484" y="140" width="4" height="42" rx="2" fill="var(--theme-accent)"/>
<text x="496" y="154" font-size="11.5" font-weight="600" fill="var(--text)">Trunk bracing</text>
<text x="496" y="169" font-size="11" fill="var(--text-dim)">front planks with a reach and loaded</text>
<text x="496" y="182" font-size="11" fill="var(--text-dim)">front carries - stops forward flexion</text>

<rect x="484" y="194" width="4" height="42" rx="2" fill="var(--theme-accent)"/>
<text x="496" y="208" font-size="11.5" font-weight="600" fill="var(--text)">Shoulder endurance</text>
<text x="496" y="223" font-size="11" fill="var(--text-dim)">barbell or dumbbell push press, heavier,</text>
<text x="496" y="236" font-size="11" fill="var(--text-dim)">in the plane the throw uses</text>

<rect x="484" y="248" width="4" height="42" rx="2" fill="var(--good)"/>
<text x="496" y="262" font-size="11.5" font-weight="600" fill="var(--good)">Shoulder-girdle mobility</text>
<text x="496" y="277" font-size="11" fill="var(--text-dim)">the physio lens: the single fastest route</text>
<text x="496" y="290" font-size="11" fill="var(--text-dim)">to a better wall ball; thoracic, hip next</text>

<line x1="12" y1="308" x2="688" y2="308" stroke="var(--border)"/>
<text x="12" y="322" font-size="11" fill="var(--text)">Triple extension of hips, knees and ankles drives the throw; force then passes proximal to distal through torso, shoulders and arms.</text>
<text x="12" y="335" font-size="11" fill="var(--text)">The arms guide the ball. Muscling it with the shoulders fatigues fast and makes trajectory inconsistent. Store elastic recoil on the descent.</text>
<text x="12" y="348" font-size="11" fill="var(--text)">Descend to regulation depth with a stiff trunk and neutral lumbar spine; flexion at the bottom leaks force and adds spinal load.</text>
<text x="12" y="361" font-size="11" fill="var(--text-dimmer)">Compact mesomorph: fast cycling on hip drive, avoid a high arc. Tall ectomorph: less throw height, but long levers to control.</text>
</svg>''',
        "The legs project the ball; the upper back is what gives way first.")


# ----------------------------------------------------------------- day 93
def d_rb_injury_cause():
    return _wrap(
        "dg-rb_injury_cause",
        "Load outrunning capacity",
        '''<svg viewBox="0 10 700 356" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px;display:block" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="A slowly rising capacity curve crossed by a fast-changing load line at the point injury appears, beside the strongest modifiable risk factors and the non-mechanical ones">
''' + _RM + '''
<line x1="46" y1="26" x2="46" y2="250" stroke="var(--border)" stroke-width="1.5"/>
<line x1="46" y1="250" x2="384" y2="250" stroke="var(--border)" stroke-width="1.5"/>
<text x="24" y="140" font-size="11" fill="var(--text-dim)" text-anchor="middle" transform="rotate(-90 24 140)">load / capacity</text>
<text x="384" y="266" font-size="11" fill="var(--text-dim)" text-anchor="end">time</text>

<path d="M46 206 C120 199 200 187 260 177 C312 168 352 160 388 154" fill="none" stroke="var(--good)" stroke-width="2.6"/>
<path d="M46 232 L86 224 L126 230 L166 218 L206 224 L246 210 L286 214 L306 172 L326 120 L346 138 L366 128 L388 134" fill="none" stroke="var(--theme-accent)" stroke-width="2.4" stroke-linejoin="round"/>

<circle cx="313" cy="158" r="6" fill="none" stroke="var(--bad)" stroke-width="2.4"/>
<g class="dg-anim"><circle cx="313" cy="158" r="6" fill="none" stroke="var(--bad)" stroke-width="2"><animate attributeName="r" values="6;16" dur="2.8s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.75;0" dur="2.8s" repeatCount="indefinite"/></circle></g>
<path d="M228 72 L306 150" stroke="var(--text-dimmer)" stroke-width="1.2" fill="none"/>
<text x="96" y="62" font-size="11.5" font-weight="600" fill="var(--bad)">demand outruns capacity: injury appears</text>
<text x="96" y="76" font-size="11" fill="var(--text-dim)">at whichever structure has the least reserve</text>

<rect x="52" y="278" width="12" height="4" fill="var(--good)"/><text x="70" y="285" font-size="11" fill="var(--text-dim)">capacity adapts slowly</text>
<rect x="216" y="278" width="12" height="4" fill="var(--theme-accent)"/><text x="234" y="285" font-size="11" fill="var(--text-dim)">load can change fast</text>
<path d="M306 250 v8" stroke="var(--warn)" stroke-width="2" fill="none"/>
<text x="14" y="306" font-size="11" fill="var(--warn)">the spike: a volume jump, a new surface or gradient, a new shoe</text>
<text x="14" y="322" font-size="11" fill="var(--text-dim)">Technique work is a legitimate adjunct where a fault concentrates</text>
<text x="14" y="335" font-size="11" fill="var(--text-dim)">load - it does not substitute for sane load progression.</text>
<text x="14" y="350" font-size="11" fill="var(--text-dimmer)">HYROX: runs land on legs pre-loaded by sled push, pull and lunges.</text>

<line x1="392" y1="10" x2="392" y2="364" stroke="var(--border)"/>

<text x="404" y="24" font-size="12" font-weight="700" fill="var(--good)">Strongest modifiable</text>
<text x="404" y="41" font-size="11" fill="var(--text)">training load history: how much, how fast it</text>
<text x="404" y="54" font-size="11" fill="var(--text)">changed, what the tissue was used to</text>
<text x="404" y="70" font-size="11" fill="var(--text)">previous injury is the most consistent</text>
<text x="404" y="83" font-size="11" fill="var(--text)">predictor - address the deficits it left</text>

<text x="404" y="106" font-size="12" font-weight="700" fill="var(--warn)">Where load lands, not whether</text>
<text x="404" y="123" font-size="11" fill="var(--text)">footstrike does not reliably predict injury:</text>
<text x="404" y="136" font-size="11" fill="var(--text)">forefoot loads calf and Achilles, rearfoot</text>
<text x="404" y="149" font-size="11" fill="var(--text)">the knee - a shift of load, not a cure</text>
<text x="404" y="165" font-size="11" fill="var(--text)">pronation is poorly supported and a weak</text>
<text x="404" y="178" font-size="11" fill="var(--text)">basis for prescribing footwear</text>
<text x="404" y="194" font-size="11" fill="var(--text)">low cadence with overstride raises per-step</text>
<text x="404" y="207" font-size="11" fill="var(--text)">load; a modest cadence rise unloads the</text>
<text x="404" y="220" font-size="11" fill="var(--text)">knee but adds demand elsewhere</text>
<text x="404" y="236" font-size="11" fill="var(--text)">high loading rate and braking impulse bias</text>
<text x="404" y="249" font-size="11" fill="var(--text)">toward bone stress, tibial especially</text>
<text x="404" y="265" font-size="11" fill="var(--text)">reduced hip extension and glute drive push</text>
<text x="404" y="278" font-size="11" fill="var(--text)">propulsion onto hamstrings and calf</text>

<text x="404" y="293" font-size="12" font-weight="700" fill="var(--text-dim)">Non-mechanical</text>
<text x="404" y="310" font-size="11" fill="var(--text)">energy availability, sleep and stress set</text>
<text x="404" y="323" font-size="11" fill="var(--text)">adaptation capacity - the same load is</text>
<text x="404" y="336" font-size="11" fill="var(--text)">riskier in an under-fuelled athlete</text>
<text x="404" y="349" font-size="11" fill="var(--bad)">bone stress with menstrual disturbance or</text>
<text x="404" y="362" font-size="11" fill="var(--bad)">restrictive eating warrants medical referral</text>
</svg>''',
        "Injury is a load-management failure first - history and rate of change beat any single kinematic variable.")


# ------------------------------------------------------------------ day 5
def d_sm_monitoring():
    return _wrap(
        "dg-sm_monitoring",
        "Prescribe external, adapt from internal",
        '''<svg viewBox="0 0 700 360" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px;display:block" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="External load prescribed into an athlete and internal load read back out, with the simple arithmetic and the rule that baselines beat absolutes">
''' + _RM + '''
<rect x="14" y="18" width="190" height="82" rx="8" fill="var(--surface)" stroke="var(--border)"/>
<text x="24" y="38" font-size="11.5" font-weight="700" fill="var(--theme-accent)">EXTERNAL LOAD</text>
<text x="24" y="54" font-size="11" fill="var(--text-dim)">what you prescribe</text>
<text x="24" y="74" font-size="11" fill="var(--text)">km run, sled metres, reps,</text>
<text x="24" y="88" font-size="11" fill="var(--text)">kilos, watts</text>

<rect x="252" y="18" width="190" height="82" rx="8" fill="var(--surface)" stroke="var(--border)"/>
<text x="262" y="38" font-size="11.5" font-weight="700" fill="var(--text)">THIS ATHLETE, TODAY</text>
<text x="262" y="54" font-size="11" fill="var(--text-dim)">what changes the landing</text>
<text x="262" y="74" font-size="11" fill="var(--text)">sleep, heat, fuelling,</text>
<text x="262" y="88" font-size="11" fill="var(--text)">life stress</text>

<rect x="490" y="18" width="190" height="82" rx="8" fill="var(--surface)" stroke="var(--border)"/>
<text x="500" y="38" font-size="11.5" font-weight="700" fill="var(--good)">INTERNAL LOAD</text>
<text x="500" y="54" font-size="11" fill="var(--text-dim)">what you measure</text>
<text x="500" y="74" font-size="11" fill="var(--text)">HR-derived load, sRPE,</text>
<text x="500" y="88" font-size="11" fill="var(--text)">perceived strain</text>

<g class="dg-anim">
  <g><path d="M208 59 H238" stroke="var(--text-dim)" stroke-width="2" fill="none"/><path d="M236 54 l9 5 l-9 5 z" fill="var(--text-dim)"/><animate attributeName="opacity" values="1;0.25;0.25;1" dur="6s" repeatCount="indefinite"/></g>
  <g><path d="M446 59 H476" stroke="var(--text-dim)" stroke-width="2" fill="none"/><path d="M474 54 l9 5 l-9 5 z" fill="var(--text-dim)"/><animate attributeName="opacity" values="0.25;1;0.25;0.25" dur="6s" repeatCount="indefinite"/></g>
  <g><path d="M585 104 V126 H109 V104" fill="none" stroke="var(--text-dim)" stroke-width="2"/><path d="M104 106 l5 -9 l5 9 z" fill="var(--text-dim)"/><animate attributeName="opacity" values="0.25;0.25;1;0.25" dur="6s" repeatCount="indefinite"/></g>
</g>
<text x="347" y="142" font-size="11" fill="var(--text)" text-anchor="middle">Adapt the next prescription from the RELATIONSHIP between them - not from either number alone.</text>

<line x1="352" y1="156" x2="352" y2="300" stroke="var(--border)"/>

<text x="14" y="172" font-size="12" font-weight="700" fill="var(--text)">The cheap arithmetic</text>
<text x="14" y="192" font-size="11" fill="var(--text)">sRPE = RPE (0-10 CR10) x session minutes, in AU</text>
<text x="14" y="207" font-size="11" fill="var(--text-dim)">rate it around 30 min after the session, 10-15 min at minimum,</text>
<text x="14" y="221" font-size="11" fill="var(--text-dim)">so the last hard interval does not dominate the rating</text>
<text x="14" y="240" font-size="11" fill="var(--text)">weekly load = the sum of daily sRPE</text>
<text x="14" y="255" font-size="11" fill="var(--text)">monotony = weekly mean / SD of daily loads</text>
<text x="14" y="269" font-size="11" fill="var(--text-dim)">typically 1-2; above about 2 is the usual flag. High load with</text>
<text x="14" y="283" font-size="11" fill="var(--text-dim)">high monotony (no easy days) is a heuristic, not a predictor.</text>
<text x="14" y="300" font-size="11" fill="var(--text)">strain = weekly load x monotony</text>

<text x="366" y="172" font-size="12" font-weight="700" fill="var(--text)">Baselines, never absolutes</text>
<text x="366" y="192" font-size="11" fill="var(--text)">HRV: log RMSSD or lnRMSSD in standard conditions - same time,</text>
<text x="366" y="206" font-size="11" fill="var(--text)">posture, breathing, device, before caffeine. Judge against the</text>
<text x="366" y="220" font-size="11" fill="var(--text)">athlete's own 7-day rolling mean and SD.</text>
<text x="366" y="238" font-size="11" fill="var(--text)">Signal = the rolling mean drifting outside normal range, or a</text>
<text x="366" y="252" font-size="11" fill="var(--text)">suppressed mean with rising SD. One low morning is expected.</text>
<text x="366" y="270" font-size="11" fill="var(--text)">Resting HR up roughly 5-10 bpm over several days, with HRV</text>
<text x="366" y="284" font-size="11" fill="var(--text)">and wellness down, is a prompt to investigate, not a diagnosis.</text>
<text x="366" y="300" font-size="11" fill="var(--bad)">ACWR = 7-day / 28-day: cut-offs are NOT validated. Direction only.</text>

<rect x="14" y="312" width="158" height="42" rx="6" fill="var(--surface)" stroke="var(--good)"/>
<text x="24" y="329" font-size="11" font-weight="600" fill="var(--good)">1 verify</text>
<text x="24" y="345" font-size="11" fill="var(--text-dim)">real? multi-day? confirmed?</text>
<path d="M176 328 l8 5 l-8 5 z" fill="var(--text-dim)"/>
<rect x="188" y="312" width="158" height="42" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="198" y="329" font-size="11" font-weight="600" fill="var(--text)">2 fix the cheap causes</text>
<text x="198" y="345" font-size="11" fill="var(--text-dim)">sleep, fuel, fluid, life stress</text>
<path d="M350 328 l8 5 l-8 5 z" fill="var(--text-dim)"/>
<rect x="362" y="312" width="158" height="42" rx="6" fill="var(--surface)" stroke="var(--warn)"/>
<text x="372" y="329" font-size="11" font-weight="600" fill="var(--warn)">3 modify</text>
<text x="372" y="345" font-size="11" fill="var(--text-dim)">intensity first, then volume</text>
<path d="M524 328 l8 5 l-8 5 z" fill="var(--text-dim)"/>
<rect x="536" y="312" width="156" height="42" rx="6" fill="var(--surface)" stroke="var(--bad)"/>
<text x="546" y="329" font-size="11" font-weight="600" fill="var(--bad)">4 refer</text>
<text x="546" y="345" font-size="11" fill="var(--text-dim)">fever, chest, pain, ED, mood</text>
</svg>''',
        "Trends against the athlete's own baseline decide - and never use the data punitively, or honest reporting stops.")


# ----------------------------------------------------------------- day 49
def d_pc_testing():
    return _wrap(
        "dg-pc_testing",
        "A battery in four layers",
        '''<svg viewBox="0 0 700 356" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px;display:block" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="A test battery in four layers gated by whether a decision hangs on the result, with retest cadence, the noise floor and the read-out">
<text x="14" y="22" font-size="11" fill="var(--text)">Validity: it measures the quality you claim.  Reliability: it repeats.  Specificity: it resembles the race.</text>
<text x="14" y="38" font-size="11" fill="var(--text-dim)">Standardise warm-up, footwear, time of day, sled surface and load, the prior 24-48 h, fuelling, caffeine.</text>
<text x="14" y="52" font-size="11" fill="var(--text-dim)">Uncontrolled sled friction makes sled times from different venues close to useless.</text>
<line x1="14" y1="62" x2="686" y2="62" stroke="var(--border)"/>

<rect x="14" y="78" width="100" height="32" rx="6" fill="var(--surface)" stroke="var(--bad)"/>
<text x="64" y="99" font-size="11.5" font-weight="600" fill="var(--bad)" text-anchor="middle">drop the test</text>
<path d="M172 94 H126" stroke="var(--text-dim)" stroke-width="1.6" fill="none"/><path d="M124 89 l-9 5 l9 5 z" fill="var(--text-dim)"/>
<text x="148" y="86" font-size="11" fill="var(--text-dim)" text-anchor="middle">no</text>

<rect x="176" y="76" width="258" height="36" rx="8" fill="var(--theme-accent)"/>
<text x="305" y="99" font-size="12" font-weight="700" fill="var(--bg)" text-anchor="middle">Does a decision hang on the result?</text>
<path d="M305 114 V128" stroke="var(--text-dim)" stroke-width="1.6" fill="none"/><path d="M300 126 l5 9 l5 -9 z" fill="var(--text-dim)"/>
<text x="316" y="127" font-size="11" fill="var(--text-dim)">yes</text>

<rect x="14" y="140" width="420" height="48" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<rect x="14" y="140" width="4" height="48" rx="2" fill="var(--theme-accent)"/>
<text x="28" y="157" font-size="11.5" font-weight="700" fill="var(--text)">1  Aerobic anchor</text>
<text x="28" y="172" font-size="11" fill="var(--text-dim)">about 30 min steady TT, or a lab lactate / ventilatory test, for the threshold estimate</text>
<text x="28" y="184" font-size="11" fill="var(--text-dim)">a 5 km TT is a pace anchor - but most race it ABOVE threshold, so it is not one</text>

<rect x="14" y="194" width="420" height="46" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<rect x="14" y="194" width="4" height="46" rx="2" fill="var(--theme-accent)"/>
<text x="28" y="211" font-size="11.5" font-weight="700" fill="var(--text)">2  Race-transfer anchor</text>
<text x="28" y="225" font-size="11" fill="var(--text-dim)">4 x (1 km run + 1 station), race order, race intent - beats any isolated station PB</text>
<text x="28" y="237" font-size="11" fill="var(--text-dim)">a half-sim costs far less recovery than a full one and yields most of the information</text>

<rect x="14" y="246" width="420" height="48" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<rect x="14" y="246" width="4" height="48" rx="2" fill="var(--theme-accent)"/>
<text x="28" y="263" font-size="11.5" font-weight="700" fill="var(--text)">3  Station benchmarks, at the athlete's own division loads</text>
<text x="28" y="278" font-size="11" fill="var(--text-dim)">1000 m SkiErg / 1000 m Row / 50 m sled push / 50 m sled pull, fixed load</text>
<text x="28" y="290" font-size="11" fill="var(--text-dim)">80 m burpee broad jump / 200 m farmers / 100 m sandbag lunge / 100 wall balls</text>

<rect x="14" y="300" width="420" height="48" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<rect x="14" y="300" width="4" height="48" rx="2" fill="var(--theme-accent)"/>
<text x="28" y="317" font-size="11.5" font-weight="700" fill="var(--text)">4  Strength and durability markers</text>
<text x="28" y="332" font-size="11" fill="var(--text-dim)">heavy sled-push proxy, trap-bar or squat 3-5RM, front-rack hold, grip work</text>
<text x="28" y="344" font-size="11" fill="var(--text-dim)">(a farmers hold at race load past a minute is a practical target, not a cut-off)</text>

<line x1="448" y1="70" x2="448" y2="350" stroke="var(--border)"/>

<text x="460" y="88" font-size="11.5" font-weight="700" fill="var(--text)">Retest cadence</text>
<text x="460" y="104" font-size="11" fill="var(--text-dim)">the full battery every 6-12 weeks, at block</text>
<text x="460" y="117" font-size="11" fill="var(--text-dim)">boundaries. Cheap monitors - submax HR,</text>
<text x="460" y="130" font-size="11" fill="var(--text-dim)">RPE at a fixed pace - weekly. Retesting a</text>
<text x="460" y="143" font-size="11" fill="var(--text-dim)">slow quality fortnightly buries the signal.</text>

<text x="460" y="170" font-size="11.5" font-weight="700" fill="var(--warn)">The noise floor</text>
<text x="460" y="186" font-size="11" fill="var(--text-dim)">call a change real only above the test's</text>
<text x="460" y="199" font-size="11" fill="var(--text-dim)">typical error: on the order of 1-2 pct for</text>
<text x="460" y="212" font-size="11" fill="var(--text-dim)">a well-practised erg TT, and often several</text>
<text x="460" y="225" font-size="11" fill="var(--text-dim)">pct for sled, burpee and sim tests.</text>
<text x="460" y="238" font-size="11" fill="var(--text-dim)">Establish your own from repeat trials.</text>

<text x="460" y="265" font-size="11.5" font-weight="700" fill="var(--good)">The read-out</text>
<text x="460" y="281" font-size="11" fill="var(--text-dim)">compromised-running index = fresh 1 km</text>
<text x="460" y="294" font-size="11" fill="var(--text-dim)">pace vs the average 1 km inside the</text>
<text x="460" y="307" font-size="11" fill="var(--text-dim)">couplet. A widening gap is a durability or</text>
<text x="460" y="320" font-size="11" fill="var(--text-dim)">station-economy limiter, not raw speed.</text>
<text x="460" y="336" font-size="11" fill="var(--text)">1-2 full sims per build, clear of race week.</text>
<text x="460" y="349" font-size="11" fill="var(--text)">Time the roxzone as its own variable.</text>
</svg>''',
        "No decision, no test - and any change smaller than the typical error is noise, not adaptation.")


# ----------------------------------------------------------------- day 88
def d_rb_hip():
    return _wrap(
        "dg-rb_hip",
        "The usable stride is behind you",
        '''<svg viewBox="0 10 700 356" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px;display:block" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="A runner shown propelling behind the centre of mass versus reaching in front of it, beside the compensation chain that follows restricted hip extension">
''' + _RM + '''
<rect x="22" y="200" width="174" height="82" fill="var(--good)" opacity="0.12"/>
<rect x="196" y="200" width="174" height="82" fill="var(--bad)" opacity="0.12"/>
<line x1="22" y1="282" x2="372" y2="282" stroke="var(--border)" stroke-width="2"/>
<line x1="196" y1="112" x2="196" y2="288" stroke="var(--text-dim)" stroke-width="1.4" stroke-dasharray="5 4"/>
<text x="196" y="104" font-size="11" fill="var(--text-dim)" text-anchor="middle">centre of mass</text>
<text x="108" y="194" font-size="11.5" font-weight="700" fill="var(--good)" text-anchor="middle">BEHIND = propulsion</text>
<text x="284" y="194" font-size="11.5" font-weight="700" fill="var(--bad)" text-anchor="middle">IN FRONT = braking</text>

<path d="M196 196 L204 146" fill="none" stroke="var(--text)" stroke-width="3.5" stroke-linecap="round"/>
<circle cx="208" cy="132" r="11" fill="none" stroke="var(--text)" stroke-width="2.5"/>
<path d="M204 146 L182 166 L198 180" fill="none" stroke="var(--text)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M204 146 L230 162 L216 182" fill="none" stroke="var(--text)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M196 196 L158 228 L128 260" fill="none" stroke="var(--good)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M196 196 L228 232 L246 256" fill="none" stroke="var(--text)" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M204 176 A 34 34 0 0 1 168 208" fill="none" stroke="var(--good)" stroke-width="1.8" stroke-dasharray="3 3"/>
<text x="160" y="164" font-size="11" fill="var(--good)" text-anchor="end">hip extension</text>
<path d="M154 166 L182 186" stroke="var(--text-dimmer)" stroke-width="1" fill="none"/>

<g class="dg-anim">
  <path d="M124 262 L92 278" fill="none" stroke="var(--good)" stroke-width="3.2" stroke-linecap="round"><animate attributeName="opacity" values="1;0.35;1" dur="3.4s" repeatCount="indefinite"/></path>
  <path d="M96 270 l-10 9 l12 3 z" fill="var(--good)"><animate attributeName="opacity" values="1;0.35;1" dur="3.4s" repeatCount="indefinite"/></path>
</g>
<text x="22" y="300" font-size="11" fill="var(--good)">push the ground back and down in late stance</text>
<path d="M248 258 L272 270" stroke="var(--bad)" stroke-width="2.4" stroke-linecap="round" fill="none"/>
<path d="M266 262 l10 9 l-12 3 z" fill="var(--bad)"/>
<text x="282" y="272" font-size="11" fill="var(--bad)">reach = brake</text>

<line x1="384" y1="14" x2="384" y2="300" stroke="var(--border)"/>

<text x="396" y="24" font-size="12" font-weight="700" fill="var(--text)">The compensation chain</text>
<rect x="396" y="32" width="292" height="28" rx="6" fill="var(--surface)" stroke="var(--warn)"/>
<text x="406" y="51" font-size="11.5" fill="var(--text)">restricted hip extension</text>
<path d="M537 62 l5 8 l5 -8" fill="none" stroke="var(--text-dimmer)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="396" y="74" width="292" height="28" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="406" y="93" font-size="11.5" fill="var(--text)">anterior pelvic tilt</text>
<path d="M537 104 l5 8 l5 -8" fill="none" stroke="var(--text-dimmer)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="396" y="116" width="292" height="28" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="406" y="135" font-size="11.5" fill="var(--text)">lumbar extension fakes the range</text>
<path d="M537 146 l5 8 l5 -8" fill="none" stroke="var(--text-dimmer)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="396" y="158" width="292" height="28" rx="6" fill="var(--surface)" stroke="var(--bad)"/>
<text x="406" y="177" font-size="11.5" fill="var(--text)">no propulsive gain, added spinal load</text>

<text x="396" y="206" font-size="11" fill="var(--warn)">Glutes under-contribute, so hamstrings and calf</text>
<text x="396" y="219" font-size="11" fill="var(--warn)">take the propulsive demand - strain risk in both.</text>
<text x="396" y="238" font-size="11" fill="var(--text)">Assess with a Thomas test or a half-kneeling</text>
<text x="396" y="251" font-size="11" fill="var(--text)">check; watch for lumbar extension substituting</text>
<text x="396" y="264" font-size="11" fill="var(--text)">for hip extension.</text>
<text x="396" y="283" font-size="11" fill="var(--text)">HYROX compounds it: sled push, sled pull and</text>
<text x="396" y="296" font-size="11" fill="var(--text)">lunges shorten the flexors before every run.</text>

<line x1="14" y1="308" x2="686" y2="308" stroke="var(--border)"/>
<text x="14" y="322" font-size="11" fill="var(--text)">Restoring range rarely changes running on its own: load it - hip thrusts, full-range split squats, single-leg RDLs, A-marches.</text>
<text x="14" y="335" font-size="11" fill="var(--text)">Cue the push - 'drive the ground back behind you' - not 'lengthen your stride', which buys the overstride you meant to remove.</text>
<text x="14" y="348" font-size="11" fill="var(--text)">A slight forward lean from the ankles preserves the extension window; sitting back into the hips closes it.</text>
<text x="14" y="361" font-size="11" fill="var(--text-dimmer)">Expect a longer stride at the SAME cadence, and the biggest gains in the back half, where extension range collapses first.</text>
</svg>''',
        "Cue the push, not the reach: propulsion is force applied behind the centre of mass.")


# ----------------------------------------------------------------- day 94
def d_nu_working():
    return _wrap(
        "dg-nu_working",
        "Nutrition: the scope line",
        '''<svg viewBox="0 0 700 348" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px;display:block" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="The nutrition scope line: what a coach may guide on, what must be referred, the red flags that trigger referral, and where the real work sits">
<line x1="350" y1="12" x2="350" y2="180" stroke="var(--text-dim)" stroke-width="2.5"/>
<text x="20" y="26" font-size="12.5" font-weight="700" fill="var(--good)">IN SCOPE - the coach</text>
<text x="20" y="50" font-size="11.5" fill="var(--text)">general, evidence-based performance nutrition</text>
<text x="20" y="70" font-size="11.5" fill="var(--text)">fuelling around sessions, and hydration</text>
<text x="20" y="90" font-size="11.5" fill="var(--text)">practical race-day strategy</text>
<text x="20" y="110" font-size="11.5" fill="var(--text)">food-quality basics</text>
<text x="20" y="130" font-size="11.5" fill="var(--text)">a food and training log across a normal week</text>
<text x="20" y="150" font-size="11.5" fill="var(--text)">one or two specific, negotiated changes</text>
<path d="M20 38 h300" stroke="var(--good)" stroke-width="2" opacity="0.5" fill="none"/>

<text x="366" y="26" font-size="12.5" font-weight="700" fill="var(--bad)">OUT OF SCOPE - refer</text>
<text x="366" y="50" font-size="11.5" fill="var(--text)">individualised medical nutrition therapy</text>
<text x="366" y="70" font-size="11.5" fill="var(--text)">clinical meal prescription for a diagnosis</text>
<text x="366" y="90" font-size="11.5" fill="var(--text)">eating-disorder treatment</text>
<text x="366" y="110" font-size="11.5" fill="var(--text)">supplements prescribed for medical purposes</text>
<path d="M366 38 h300" stroke="var(--bad)" stroke-width="2" opacity="0.5" fill="none"/>
<text x="366" y="140" font-size="11.5" font-weight="600" fill="var(--text)">Build the referral network before you need it:</text>
<text x="366" y="158" font-size="11.5" fill="var(--text-dim)">dietitian, physician, and a clinician experienced</text>
<text x="366" y="172" font-size="11.5" fill="var(--text-dim)">in disordered eating.</text>

<rect x="14" y="192" width="326" height="148" rx="8" fill="var(--surface)" stroke="var(--bad)"/>
<text x="26" y="212" font-size="12" font-weight="700" fill="var(--bad)">Red flags: refer, do not adjust</text>
<text x="26" y="232" font-size="11" fill="var(--text)">restriction  /  food secrecy  /  rigid rules</text>
<text x="26" y="248" font-size="11" fill="var(--text)">weight preoccupation  /  unexplained fatigue</text>
<text x="26" y="264" font-size="11" fill="var(--text)">menstrual disturbance  /  recurrent bone injury</text>
<text x="26" y="280" font-size="11" fill="var(--text)">gastrointestinal symptoms</text>
<text x="26" y="302" font-size="11" fill="var(--text-dim)">Avoid routine body-composition measurement without</text>
<text x="26" y="316" font-size="11" fill="var(--text-dim)">a clear purpose and a plan for the result - it is a</text>
<text x="26" y="330" font-size="11" fill="var(--text-dim)">common trigger for restriction.</text>

<rect x="354" y="192" width="332" height="148" rx="8" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="366" y="212" font-size="12" font-weight="700" fill="var(--theme-accent)">Where the work actually is</text>
<text x="366" y="232" font-size="11" fill="var(--text)">The failure is implementation, not knowledge. Most</text>
<text x="366" y="246" font-size="11" fill="var(--text)">athletes already know roughly what to do.</text>
<text x="366" y="266" font-size="11" fill="var(--text)">Anchor a change to a session - carbohydrate in the</text>
<text x="366" y="280" font-size="11" fill="var(--text)">two hours before the key session - so it is concrete.</text>
<text x="366" y="300" font-size="11" fill="var(--text)">Budget, cooking skill, shift work, family, culture and</text>
<text x="366" y="314" font-size="11" fill="var(--text)">travel decide adherence more than optimality does.</text>
<text x="366" y="330" font-size="11" fill="var(--text-dim)">No moralising language. Evaluate before adding another.</text>
</svg>''',
        "Guidance in, therapy out - and red flags trigger a referral, never a dietary adjustment.")


# ----------------------------------------------------------------- day 99
def d_sm_neuro():
    return _wrap(
        "dg-sm_neuro",
        "The control loop, and what degrades it",
        '''<svg viewBox="0 0 700 354" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px;display:block" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="The sense, integrate and act control loop, what degrades each stage under fatigue, and what that implies for injury clustering and prevention">
''' + _RM + '''
<rect x="14" y="14" width="200" height="90" rx="8" fill="var(--surface)" stroke="var(--border)"/>
<text x="26" y="34" font-size="11.5" font-weight="700" fill="var(--theme-accent)">SENSE</text>
<text x="26" y="52" font-size="11" fill="var(--text)">muscle spindles - length, velocity</text>
<text x="26" y="68" font-size="11" fill="var(--text)">Golgi tendon organs - tension</text>
<text x="26" y="84" font-size="11" fill="var(--text)">joint receptors</text>
<text x="26" y="98" font-size="11" fill="var(--text-dim)">plus vestibular and visual input</text>

<rect x="252" y="14" width="176" height="90" rx="8" fill="var(--surface)" stroke="var(--border)"/>
<text x="264" y="34" font-size="11.5" font-weight="700" fill="var(--theme-accent)">INTEGRATE</text>
<text x="264" y="54" font-size="11" fill="var(--text)">central processing</text>
<text x="264" y="72" font-size="11" fill="var(--text-dim)">the speed and quality of</text>
<text x="264" y="86" font-size="11" fill="var(--text-dim)">the decision decide whether</text>
<text x="264" y="100" font-size="11" fill="var(--text-dim)">the movement is organised</text>

<rect x="466" y="14" width="220" height="90" rx="8" fill="var(--surface)" stroke="var(--border)"/>
<text x="478" y="34" font-size="11.5" font-weight="700" fill="var(--theme-accent)">ACT</text>
<text x="478" y="54" font-size="11" fill="var(--good)">feedforward: pre-activates muscle</text>
<text x="478" y="68" font-size="11" fill="var(--good)">before the load arrives</text>
<text x="478" y="86" font-size="11" fill="var(--warn)">feedback: corrects afterwards -</text>
<text x="478" y="100" font-size="11" fill="var(--warn)">too slow for high-speed events</text>

<g class="dg-anim">
  <g><path d="M218 58 H244" stroke="var(--text-dim)" stroke-width="2" fill="none"/><path d="M242 53 l9 5 l-9 5 z" fill="var(--text-dim)"/><animate attributeName="opacity" values="1;0.25;0.25;1" dur="5.4s" repeatCount="indefinite"/></g>
  <g><path d="M432 58 H458" stroke="var(--text-dim)" stroke-width="2" fill="none"/><path d="M456 53 l9 5 l-9 5 z" fill="var(--text-dim)"/><animate attributeName="opacity" values="0.25;1;0.25;0.25" dur="5.4s" repeatCount="indefinite"/></g>
  <g><path d="M576 108 V132 H114 V110" fill="none" stroke="var(--text-dim)" stroke-width="2"/><path d="M109 112 l5 -9 l5 9 z" fill="var(--text-dim)"/><animate attributeName="opacity" values="0.25;0.25;1;0.25" dur="5.4s" repeatCount="indefinite"/></g>
</g>
<text x="345" y="148" font-size="11" fill="var(--text)" text-anchor="middle">Injury risk = tissue capacity AND the quality of this loop in the moment.</text>

<path d="M92 200 V166" stroke="var(--warn)" stroke-width="1.8" fill="none"/><path d="M87 170 l5 -9 l5 9 z" fill="var(--warn)"/>
<path d="M258 200 V166" stroke="var(--warn)" stroke-width="1.8" fill="none"/><path d="M253 170 l5 -9 l5 9 z" fill="var(--warn)"/>
<path d="M424 200 V166" stroke="var(--warn)" stroke-width="1.8" fill="none"/><path d="M419 170 l5 -9 l5 9 z" fill="var(--warn)"/>
<path d="M594 200 V166" stroke="var(--warn)" stroke-width="1.8" fill="none"/><path d="M589 170 l5 -9 l5 9 z" fill="var(--warn)"/>

<rect x="14" y="200" width="156" height="54" rx="6" fill="var(--surface)" stroke="var(--warn)"/>
<text x="24" y="217" font-size="11.5" font-weight="600" fill="var(--warn)">fatigue</text>
<text x="24" y="232" font-size="11" fill="var(--text-dim)">slower reaction, blunted</text>
<text x="24" y="246" font-size="11" fill="var(--text-dim)">proprioception, altered firing</text>

<rect x="180" y="200" width="156" height="54" rx="6" fill="var(--surface)" stroke="var(--warn)"/>
<text x="190" y="217" font-size="11.5" font-weight="600" fill="var(--warn)">cognitive load</text>
<text x="190" y="232" font-size="11" fill="var(--text-dim)">distraction leaves less</text>
<text x="190" y="246" font-size="11" fill="var(--text-dim)">attention for movement</text>

<rect x="346" y="200" width="156" height="54" rx="6" fill="var(--surface)" stroke="var(--warn)"/>
<text x="356" y="217" font-size="11.5" font-weight="600" fill="var(--warn)">pain</text>
<text x="356" y="232" font-size="11" fill="var(--text-dim)">alters motor control even</text>
<text x="356" y="246" font-size="11" fill="var(--text-dim)">once the tissue has healed</text>

<rect x="512" y="200" width="174" height="54" rx="6" fill="var(--surface)" stroke="var(--warn)"/>
<text x="522" y="217" font-size="11.5" font-weight="600" fill="var(--warn)">previous injury</text>
<text x="522" y="232" font-size="11" fill="var(--text-dim)">degrades proprioceptive acuity</text>
<text x="522" y="246" font-size="11" fill="var(--text-dim)">and alters the motor pattern</text>

<text x="14" y="282" font-size="12" font-weight="700" fill="var(--bad)">So injuries cluster</text>
<text x="14" y="300" font-size="11" fill="var(--text)">late in sessions and late in races, in unpredictable</text>
<text x="14" y="314" font-size="11" fill="var(--text)">environments, and in athletes with a history.</text>
<text x="14" y="334" font-size="11" fill="var(--text)">In HYROX the compromised-running transition off a</text>
<text x="14" y="348" font-size="11" fill="var(--text)">station is the highest-risk control moment of the race.</text>

<line x1="352" y1="266" x2="352" y2="352" stroke="var(--border)"/>
<text x="368" y="282" font-size="12" font-weight="700" fill="var(--good)">So prevention must</text>
<text x="368" y="300" font-size="11" fill="var(--text)">combine strength, plyometrics, balance and agility -</text>
<text x="368" y="314" font-size="11" fill="var(--text)">multi-component programmes beat single-mode ones</text>
<text x="368" y="334" font-size="11" fill="var(--text)">include reactive, unanticipated cues, be rehearsed under</text>
<text x="368" y="348" font-size="11" fill="var(--text)">fatigue, and use progressive exposure, not avoidance</text>
</svg>''',
        "A clean, fresh, pre-planned screen can pass the athlete who fails on run 8.")


# ----------------------------------------------------------------- day 82
def d_mp_sdt():
    return _wrap(
        "dg-mp_sdt",
        "Three needs move one continuum",
        '''<svg viewBox="0 0 700 350" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px;display:block" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Autonomy, competence and relatedness feeding one motivation continuum from amotivation to intrinsic, with the fragile and persistent bands marked">
''' + _RM + '''
<circle cx="112" cy="52" r="38" fill="none" stroke="var(--theme-accent)" stroke-width="2.5"/>
<text x="112" y="56" font-size="11.5" font-weight="700" fill="var(--text)" text-anchor="middle">AUTONOMY</text>
<text x="112" y="108" font-size="11" fill="var(--text-dim)" text-anchor="middle">volition and ownership:</text>
<text x="112" y="122" font-size="11" fill="var(--text-dim)" text-anchor="middle">meaningful choice, rationale</text>

<circle cx="350" cy="52" r="38" fill="none" stroke="var(--theme-accent)" stroke-width="2.5"/>
<text x="350" y="56" font-size="11.5" font-weight="700" fill="var(--text)" text-anchor="middle">COMPETENCE</text>
<text x="350" y="108" font-size="11" fill="var(--text-dim)" text-anchor="middle">visible, attributable progress:</text>
<text x="350" y="122" font-size="11" fill="var(--text-dim)" text-anchor="middle">benchmarks, splits, process goals</text>

<circle cx="588" cy="52" r="38" fill="none" stroke="var(--theme-accent)" stroke-width="2.5"/>
<text x="588" y="56" font-size="11.5" font-weight="700" fill="var(--text)" text-anchor="middle">RELATEDNESS</text>
<text x="588" y="108" font-size="11" fill="var(--text-dim)" text-anchor="middle">connection and belonging:</text>
<text x="588" y="122" font-size="11" fill="var(--text-dim)" text-anchor="middle">group sessions are programming</text>

<path d="M112 132 V144 H588 V132 M350 132 V144" fill="none" stroke="var(--border)" stroke-width="1.4"/>
<text x="350" y="160" font-size="11" fill="var(--text-dim)" text-anchor="middle">a need-supportive environment satisfies all three, and moves the athlete rightward</text>

<rect x="14" y="176" width="112" height="34" rx="4" fill="var(--surface)" stroke="var(--border)"/>
<rect x="126" y="176" width="112" height="34" rx="0" fill="var(--surface)" stroke="var(--border)"/>
<rect x="238" y="176" width="112" height="34" rx="0" fill="var(--surface)" stroke="var(--border)"/>
<rect x="350" y="176" width="112" height="34" rx="0" fill="var(--surface)" stroke="var(--border)"/>
<rect x="462" y="176" width="112" height="34" rx="0" fill="var(--surface)" stroke="var(--border)"/>
<rect x="574" y="176" width="112" height="34" rx="4" fill="var(--surface)" stroke="var(--border)"/>
<text x="70" y="198" font-size="11" fill="var(--text)" text-anchor="middle">amotivation</text>
<text x="182" y="198" font-size="11" fill="var(--text)" text-anchor="middle">external</text>
<text x="294" y="198" font-size="11" fill="var(--text)" text-anchor="middle">introjected</text>
<text x="406" y="198" font-size="11" fill="var(--text)" text-anchor="middle">identified</text>
<text x="518" y="198" font-size="11" fill="var(--text)" text-anchor="middle">integrated</text>
<text x="630" y="198" font-size="11" fill="var(--text)" text-anchor="middle">intrinsic</text>

<g class="dg-anim">
  <path d="M177 165 l7 9 l7 -9 z" fill="var(--theme-accent)">
    <animateTransform attributeName="transform" type="translate" values="0 0;0 0;336 0;336 0;0 0" dur="9s" repeatCount="indefinite" calcMode="spline" keyTimes="0;0.18;0.5;0.78;1" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1"/>
  </path>
</g>

<rect x="14" y="214" width="336" height="4" fill="var(--warn)"/>
<rect x="350" y="214" width="336" height="4" fill="var(--good)"/>
<text x="14" y="234" font-size="11" font-weight="600" fill="var(--warn)">fragile - collapses under adversity</text>
<text x="686" y="234" font-size="11" font-weight="600" fill="var(--good)" text-anchor="end">persists through setbacks</text>

<path d="M14 258 H286" stroke="var(--good)" stroke-width="2.5" fill="none"/><path d="M284 252 l10 6 l-10 6 z" fill="var(--good)"/>
<text x="304" y="254" font-size="11" fill="var(--text)">need-supportive: offer meaningful choice, explain the</text>
<text x="304" y="268" font-size="11" fill="var(--text)">rationale, acknowledge their perspective, give informational</text>
<text x="304" y="282" font-size="11" fill="var(--text)">rather than controlling feedback</text>

<path d="M286 300 H14" stroke="var(--bad)" stroke-width="2.5" fill="none"/><path d="M16 294 l-10 6 l10 6 z" fill="var(--bad)"/>
<text x="304" y="300" font-size="11" fill="var(--text)">need-thwarting: controlling language, conditional regard,</text>
<text x="304" y="314" font-size="11" fill="var(--text)">guilt induction, public comparison between athletes</text>

<text x="14" y="330" font-size="11" fill="var(--warn)">Introjected regulation - guilt, shame, ego protection - looks like great commitment and precedes burnout.</text>
<text x="14" y="346" font-size="11" fill="var(--text-dim)">Mastery climate (improvement, effort) beats ego climate. Autonomy is cheap: a choice between two acceptable sessions.</text>
</svg>''',
        "Ask why an athlete trains: obligation and other people's expectations mark the fragile end of the continuum.")


# ----------------------------------------------------------------- day 51
def d_pc_cases():
    return _wrap(
        "dg-pc_cases",
        "Archetype, limiter, lever",
        '''<svg viewBox="0 0 700 350" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px;display:block" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="Three athlete archetypes mapped to their rate-limiter and the single lever that follows from it">
<rect x="14" y="10" width="128" height="28" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="78" y="29" font-size="11.5" fill="var(--text)" text-anchor="middle">run time</text>
<rect x="150" y="10" width="128" height="28" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="214" y="29" font-size="11.5" fill="var(--text)" text-anchor="middle">station time</text>
<rect x="286" y="10" width="128" height="28" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="350" y="29" font-size="11.5" fill="var(--text)" text-anchor="middle">roxzone time</text>
<path d="M422 24 H448" stroke="var(--text-dim)" stroke-width="1.8" fill="none"/><path d="M446 19 l9 5 l-9 5 z" fill="var(--text-dim)"/>
<text x="462" y="21" font-size="11" fill="var(--text)">split the race first - the biggest</text>
<text x="462" y="34" font-size="11" fill="var(--text)">addressable loss is the target</text>

<text x="20" y="58" font-size="11" font-weight="700" fill="var(--text-dimmer)">ARCHETYPE</text>
<text x="206" y="58" font-size="11" font-weight="700" fill="var(--text-dimmer)">RATE-LIMITER</text>
<text x="340" y="58" font-size="11" font-weight="700" fill="var(--text-dimmer)">THE LEVER</text>
<line x1="14" y1="64" x2="686" y2="64" stroke="var(--border)"/>

<rect x="14" y="68" width="672" height="66" fill="var(--surface)"/>
<text x="20" y="90" font-size="11.5" font-weight="600" fill="var(--text)">Strong but slow</text>
<text x="206" y="90" font-size="11.5" fill="var(--warn)">aerobic ceiling</text>
<text x="340" y="86" font-size="11" fill="var(--text)">raise easy-run volume and add threshold work; hold strength at</text>
<text x="340" y="100" font-size="11" fill="var(--text)">maintenance - 1-2 quality sessions a week with intensity kept high -</text>
<text x="340" y="114" font-size="11" fill="var(--text)">so it does not detrain while the engine is built.</text>

<rect x="14" y="136" width="672" height="66" fill="var(--surface-2)"/>
<text x="20" y="158" font-size="11.5" font-weight="600" fill="var(--text)">Runner fails on sleds</text>
<text x="206" y="158" font-size="11.5" fill="var(--warn)">force deficit</text>
<text x="340" y="154" font-size="11" fill="var(--text)">heavy squat, leg press and hip hinge, plus prowler intervals at or near</text>
<text x="340" y="168" font-size="11" fill="var(--text)">race load. Coach technique before load: low body angle, short choppy</text>
<text x="340" y="182" font-size="11" fill="var(--text)">steps, do not stop - every restart re-pays static friction. Sleds are</text>
<text x="340" y="196" font-size="11" fill="var(--text)">brutal too - this is a strength emphasis, not a claim about cardio.</text>

<rect x="14" y="204" width="672" height="66" fill="var(--surface)"/>
<text x="20" y="226" font-size="11.5" font-weight="600" fill="var(--text)">The recurring calf</text>
<text x="206" y="226" font-size="11.5" fill="var(--warn)">load tolerance,</text>
<text x="206" y="240" font-size="11.5" fill="var(--warn)">not flexibility</text>
<text x="340" y="222" font-size="11" fill="var(--text)">progressive calf loading, straight- and bent-knee, heavy and slow; a sane</text>
<text x="340" y="236" font-size="11" fill="var(--text)">run-volume progression; and review eccentric exposure from lunges and</text>
<text x="340" y="250" font-size="11" fill="var(--text)">wall balls. Rule out footwear change, prior injury, sleep and fuelling</text>
<text x="340" y="264" font-size="11" fill="var(--text)">before assuming pure load error.</text>

<rect x="14" y="272" width="672" height="66" fill="var(--surface-2)"/>
<text x="20" y="294" font-size="11.5" font-weight="600" fill="var(--text)">First race, peaking</text>
<text x="206" y="294" font-size="11.5" fill="var(--warn)">execution,</text>
<text x="206" y="308" font-size="11.5" fill="var(--warn)">not fitness</text>
<text x="340" y="290" font-size="11" fill="var(--text)">roughly a 1-2 week taper: volume down about 40-60 pct with intensity</text>
<text x="340" y="304" font-size="11" fill="var(--text)">largely retained. Rehearse pacing, transitions, fuelling and wall-ball set</text>
<text x="340" y="318" font-size="11" fill="var(--text)">sizes - pre-plan them (25/25/20/15/15) rather than going to failure.</text>
<text x="340" y="332" font-size="11" fill="var(--text)">The first kilometre must feel restrained; hard early is paid in runs 5-8.</text>
</svg>''',
        "Archetypes are a triage hypothesis, not a diagnosis - re-test the same metric in 4-8 weeks before intensifying.")


# ----------------------------------------------------------------- day 13
def d_hp_format():
    return _wrap(
        "dg-hp_format",
        "The fixed sixteen segments",
        '''<svg viewBox="0 0 700 360" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px;display:block" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="The fixed HYROX sequence of sixteen linked segments, eight runs alternating with eight named stations, plus roxzone transitions">
''' + _RM + '''
<text x="12" y="20" font-size="11" fill="var(--text)">Fixed order, never varies. A 1 km run precedes every station: 8 km of running, plus roxzone transit on top.</text>
<path d="M18 34 l6 6 l-6 6 l-6 -6 z" fill="var(--warn)"/>
<text x="30" y="44" font-size="11" fill="var(--text-dim)">roxzone - the transition corridor; its time is inside the official result, commonly around 5-10 min but venue-dependent.</text>

<path d="M12 96 H676 C692 96 692 150 676 150 H26 C10 150 10 206 26 206 H688" fill="none" stroke="var(--border)" stroke-width="1.6" stroke-dasharray="5 4"/>

<rect x="16" y="70" width="54" height="52" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="43" y="91" font-size="11" font-weight="600" fill="var(--text)" text-anchor="middle">RUN</text><text x="43" y="106" font-size="11" fill="var(--text-dim)" text-anchor="middle">1 km</text>
<path d="M74 90 l6 6 l-6 6 l-6 -6 z" fill="var(--warn)"/>
<rect x="78" y="70" width="96" height="52" rx="6" fill="var(--theme-accent)" opacity="0.16"/>
<rect x="78" y="70" width="96" height="52" rx="6" fill="none" stroke="var(--theme-accent)"/>
<text x="126" y="91" font-size="11.5" font-weight="700" fill="var(--text)" text-anchor="middle">SKIERG</text><text x="126" y="107" font-size="11" fill="var(--text-dim)" text-anchor="middle">1000 m</text>

<rect x="186" y="70" width="54" height="52" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="213" y="91" font-size="11" font-weight="600" fill="var(--text)" text-anchor="middle">RUN</text><text x="213" y="106" font-size="11" fill="var(--text-dim)" text-anchor="middle">1 km</text>
<path d="M244 90 l6 6 l-6 6 l-6 -6 z" fill="var(--warn)"/>
<rect x="248" y="70" width="96" height="52" rx="6" fill="var(--theme-accent)" opacity="0.16"/>
<rect x="248" y="70" width="96" height="52" rx="6" fill="none" stroke="var(--theme-accent)"/>
<text x="296" y="91" font-size="11.5" font-weight="700" fill="var(--text)" text-anchor="middle">SLED PUSH</text><text x="296" y="107" font-size="11" fill="var(--text-dim)" text-anchor="middle">50 m = 4 x 12.5</text>

<rect x="356" y="70" width="54" height="52" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="383" y="91" font-size="11" font-weight="600" fill="var(--text)" text-anchor="middle">RUN</text><text x="383" y="106" font-size="11" fill="var(--text-dim)" text-anchor="middle">1 km</text>
<path d="M414 90 l6 6 l-6 6 l-6 -6 z" fill="var(--warn)"/>
<rect x="418" y="70" width="96" height="52" rx="6" fill="var(--theme-accent)" opacity="0.16"/>
<rect x="418" y="70" width="96" height="52" rx="6" fill="none" stroke="var(--theme-accent)"/>
<text x="466" y="91" font-size="11.5" font-weight="700" fill="var(--text)" text-anchor="middle">SLED PULL</text><text x="466" y="107" font-size="11" fill="var(--text-dim)" text-anchor="middle">50 m = 4 x 12.5</text>

<rect x="526" y="70" width="54" height="52" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="553" y="91" font-size="11" font-weight="600" fill="var(--text)" text-anchor="middle">RUN</text><text x="553" y="106" font-size="11" fill="var(--text-dim)" text-anchor="middle">1 km</text>
<path d="M584 90 l6 6 l-6 6 l-6 -6 z" fill="var(--warn)"/>
<rect x="588" y="70" width="96" height="52" rx="6" fill="var(--theme-accent)" opacity="0.16"/>
<rect x="588" y="70" width="96" height="52" rx="6" fill="none" stroke="var(--theme-accent)"/>
<text x="636" y="91" font-size="11.5" font-weight="700" fill="var(--text)" text-anchor="middle">BURPEE BJ</text><text x="636" y="107" font-size="11" fill="var(--text-dim)" text-anchor="middle">80 m</text>

<rect x="16" y="180" width="54" height="52" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="43" y="201" font-size="11" font-weight="600" fill="var(--text)" text-anchor="middle">RUN</text><text x="43" y="216" font-size="11" fill="var(--text-dim)" text-anchor="middle">1 km</text>
<path d="M74 200 l6 6 l-6 6 l-6 -6 z" fill="var(--warn)"/>
<rect x="78" y="180" width="96" height="52" rx="6" fill="var(--theme-accent)" opacity="0.16"/>
<rect x="78" y="180" width="96" height="52" rx="6" fill="none" stroke="var(--theme-accent)"/>
<text x="126" y="201" font-size="11.5" font-weight="700" fill="var(--text)" text-anchor="middle">ROW</text><text x="126" y="217" font-size="11" fill="var(--text-dim)" text-anchor="middle">1000 m</text>

<rect x="186" y="180" width="54" height="52" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="213" y="201" font-size="11" font-weight="600" fill="var(--text)" text-anchor="middle">RUN</text><text x="213" y="216" font-size="11" fill="var(--text-dim)" text-anchor="middle">1 km</text>
<path d="M244 200 l6 6 l-6 6 l-6 -6 z" fill="var(--warn)"/>
<rect x="248" y="180" width="96" height="52" rx="6" fill="var(--theme-accent)" opacity="0.16"/>
<rect x="248" y="180" width="96" height="52" rx="6" fill="none" stroke="var(--theme-accent)"/>
<text x="296" y="201" font-size="11.5" font-weight="700" fill="var(--text)" text-anchor="middle">FARMERS</text><text x="296" y="217" font-size="11" fill="var(--text-dim)" text-anchor="middle">200 m</text>

<rect x="356" y="180" width="54" height="52" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="383" y="201" font-size="11" font-weight="600" fill="var(--text)" text-anchor="middle">RUN</text><text x="383" y="216" font-size="11" fill="var(--text-dim)" text-anchor="middle">1 km</text>
<path d="M414 200 l6 6 l-6 6 l-6 -6 z" fill="var(--warn)"/>
<rect x="418" y="180" width="96" height="52" rx="6" fill="var(--theme-accent)" opacity="0.16"/>
<rect x="418" y="180" width="96" height="52" rx="6" fill="none" stroke="var(--theme-accent)"/>
<text x="466" y="201" font-size="11.5" font-weight="700" fill="var(--text)" text-anchor="middle">SANDBAG</text><text x="466" y="217" font-size="11" fill="var(--text-dim)" text-anchor="middle">lunges, 100 m</text>

<rect x="526" y="180" width="54" height="52" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="553" y="201" font-size="11" font-weight="600" fill="var(--text)" text-anchor="middle">RUN</text><text x="553" y="216" font-size="11" fill="var(--text-dim)" text-anchor="middle">1 km</text>
<path d="M584 200 l6 6 l-6 6 l-6 -6 z" fill="var(--warn)"/>
<rect x="588" y="180" width="96" height="52" rx="6" fill="var(--theme-accent)" opacity="0.16"/>
<rect x="588" y="180" width="96" height="52" rx="6" fill="none" stroke="var(--theme-accent)"/>
<text x="636" y="201" font-size="11.5" font-weight="700" fill="var(--text)" text-anchor="middle">WALL BALLS</text><text x="636" y="217" font-size="11" fill="var(--text-dim)" text-anchor="middle">100 reps</text>

<g class="dg-anim"><circle r="5" fill="var(--good)"><animateMotion path="M12 96 H676 C692 96 692 150 676 150 H26 C10 150 10 206 26 206 H688" dur="18s" repeatCount="1" fill="freeze"/></circle></g>

<rect x="12" y="246" width="330" height="106" rx="8" fill="var(--surface)" stroke="var(--border)"/>
<text x="24" y="264" font-size="11.5" font-weight="700" fill="var(--theme-accent)">Divisions change load, not the sequence</text>
<text x="24" y="281" font-size="11" fill="var(--text)">Pro: heavier sled push, sled pull, farmers, sandbag and</text>
<text x="24" y="294" font-size="11" fill="var(--text)">wall ball. SkiErg, Row and burpee broad jump unchanged,</text>
<text x="24" y="307" font-size="11" fill="var(--text)">as are all distances and reps. Entry is open, no qualifier.</text>
<text x="24" y="323" font-size="11" fill="var(--text)">Doubles: both run all 8 km, station work shared and totals</text>
<text x="24" y="336" font-size="11" fill="var(--text)">one athlete's worth. Relay: four athletes, two rounds each.</text>
<text x="24" y="349" font-size="11" fill="var(--text-dim)">Age groups: about 5-year bands, for rankings, not for load.</text>

<rect x="354" y="246" width="334" height="106" rx="8" fill="var(--surface)" stroke="var(--border)"/>
<text x="366" y="264" font-size="11.5" font-weight="700" fill="var(--bad)">It is judged - technique is a performance variable</text>
<text x="366" y="281" font-size="11" fill="var(--text)">A rep below standard is a no-rep and must be redone;</text>
<text x="366" y="294" font-size="11" fill="var(--text)">infractions can escalate to a time penalty in a penalty area.</text>
<text x="366" y="310" font-size="11" fill="var(--text)">Faults: incomplete hip or knee extension, ball missing the</text>
<text x="366" y="323" font-size="11" fill="var(--text)">target, sandbag off the shoulders, handles dropped rather</text>
<text x="366" y="336" font-size="11" fill="var(--text)">than set down, sled not crossing the line, non-continuous</text>
<text x="366" y="349" font-size="11" fill="var(--text)">burpee, or a jump that is not a two-foot take-off.</text>

<text x="12" y="58" font-size="11" fill="var(--warn)">Exam trap: wall balls are 100 reps in EVERY individual division (mixed doubles uses 75) - only ball weight and target height change.</text>
</svg>''',
        "Sixteen linked segments plus roxzone, not eight runs and eight workouts - the station dictates the run that follows.")


# ----------------------------------------------------------------- day 60
def d_mock_case():
    return _wrap(
        "dg-mock_case",
        "Ana: profile to plan",
        '''<svg viewBox="0 0 700 350" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;max-height:360px;display:block" xmlns="http://www.w3.org/2000/svg" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="11" fill="var(--text)" stroke="none" role="img" aria-label="A worked case: Ana's profile, a twelve-week plan in three four-week blocks, a pacing estimate, low-burden monitoring and the red-flag rule">
<rect x="12" y="10" width="272" height="330" rx="10" fill="var(--surface)" stroke="var(--border)"/>
<text x="26" y="32" font-size="14" font-weight="700" fill="var(--theme-accent)">ANA</text>
<text x="70" y="32" font-size="11" fill="var(--text-dim)">38 - women's open - first HYROX</text>
<line x1="26" y1="42" x2="270" y2="42" stroke="var(--border)"/>

<rect x="26" y="54" width="4" height="44" rx="2" fill="var(--good)"/>
<text x="40" y="68" font-size="11.5" font-weight="600" fill="var(--text)">5 km in 21:40 (4:20/km)</text>
<text x="40" y="83" font-size="11" fill="var(--text-dim)">a clear strength - so the ceiling</text>
<text x="40" y="95" font-size="11" fill="var(--text-dim)">on her race time sits elsewhere</text>

<rect x="26" y="108" width="4" height="44" rx="2" fill="var(--good)"/>
<text x="40" y="122" font-size="11.5" font-weight="600" fill="var(--text)">Deadlift 120 kg</text>
<text x="40" y="137" font-size="11" fill="var(--text-dim)">force already covers open sled</text>
<text x="40" y="149" font-size="11" fill="var(--text-dim)">and lunge demands: maintain</text>

<rect x="26" y="162" width="4" height="58" rx="2" fill="var(--bad)"/>
<text x="40" y="176" font-size="11.5" font-weight="600" fill="var(--bad)">Wall balls break down early</text>
<text x="40" y="191" font-size="11" fill="var(--text-dim)">100 reps, 4 kg, 2.70 m target -</text>
<text x="40" y="203" font-size="11" fill="var(--text-dim)">the most-limiting station, and it</text>
<text x="40" y="215" font-size="11" fill="var(--text-dim)">closes the race under max fatigue</text>

<rect x="26" y="230" width="4" height="44" rx="2" fill="var(--warn)"/>
<text x="40" y="244" font-size="11.5" font-weight="600" fill="var(--warn)">Achilles niggle history</text>
<text x="40" y="259" font-size="11" fill="var(--text-dim)">every run progression is gated by</text>
<text x="40" y="271" font-size="11" fill="var(--text-dim)">tendon tolerance, not by fitness</text>

<rect x="26" y="284" width="4" height="46" rx="2" fill="var(--warn)"/>
<text x="40" y="298" font-size="11.5" font-weight="600" fill="var(--warn)">5 h a week, two young children</text>
<text x="40" y="313" font-size="11" fill="var(--text-dim)">about 4 sessions: minimum effective</text>
<text x="40" y="325" font-size="11" fill="var(--text-dim)">dose, no quality trained twice, and</text>
<text x="40" y="337" font-size="11" fill="var(--text-dim)">one designated droppable session</text>

<text x="298" y="24" font-size="12" font-weight="700" fill="var(--text)">Twelve weeks, three four-week blocks</text>
<rect x="298" y="30" width="129" height="52" rx="4" fill="var(--theme-accent)" opacity="0.16"/>
<rect x="298" y="30" width="129" height="52" rx="4" fill="none" stroke="var(--theme-accent)"/>
<text x="362" y="48" font-size="11" font-weight="600" fill="var(--text)" text-anchor="middle">1 general prep</text>
<text x="362" y="63" font-size="11" fill="var(--text-dim)" text-anchor="middle">tendon base and</text>
<text x="362" y="76" font-size="11" fill="var(--text-dim)" text-anchor="middle">wall-ball skill</text>
<rect x="429" y="30" width="129" height="52" rx="4" fill="var(--theme-accent)" opacity="0.16"/>
<rect x="429" y="30" width="129" height="52" rx="4" fill="none" stroke="var(--theme-accent)"/>
<text x="493" y="48" font-size="11" font-weight="600" fill="var(--text)" text-anchor="middle">2 HYROX-specific</text>
<text x="493" y="63" font-size="11" fill="var(--text-dim)" text-anchor="middle">compromised running,</text>
<text x="493" y="76" font-size="11" fill="var(--text-dim)" text-anchor="middle">station pairings</text>
<rect x="560" y="30" width="128" height="52" rx="4" fill="var(--theme-accent)" opacity="0.16"/>
<rect x="560" y="30" width="128" height="52" rx="4" fill="none" stroke="var(--theme-accent)"/>
<text x="624" y="48" font-size="11" font-weight="600" fill="var(--text)" text-anchor="middle">3 sharpen</text>
<text x="624" y="63" font-size="11" fill="var(--text-dim)" text-anchor="middle">and taper</text>
<text x="298" y="92" font-size="11" fill="var(--text-dimmer)">week 0</text>
<text x="429" y="92" font-size="11" fill="var(--text-dimmer)" text-anchor="middle">4</text>
<text x="560" y="92" font-size="11" fill="var(--text-dimmer)" text-anchor="middle">8</text>
<text x="688" y="92" font-size="11" fill="var(--text-dimmer)" text-anchor="end">12</text>
<text x="298" y="108" font-size="11" fill="var(--text-dim)">Tendon capacity first: it raises the ceiling on the run volume that follows.</text>

<rect x="298" y="120" width="390" height="66" rx="8" fill="var(--surface)" stroke="var(--border)"/>
<text x="310" y="138" font-size="11.5" font-weight="700" fill="var(--theme-accent)">Pacing estimate</text>
<text x="310" y="155" font-size="11" fill="var(--text)">fresh 4:20/km, plus the taught 30-60 s/km race penalty, gives about</text>
<text x="310" y="168" font-size="11" fill="var(--text)">4:50-5:20/km. A rule of thumb, not a law - and the fast end is</text>
<text x="310" y="181" font-size="11" fill="var(--text)">defensible, because running is her clear strength.</text>

<rect x="298" y="194" width="390" height="58" rx="8" fill="var(--surface)" stroke="var(--border)"/>
<text x="310" y="212" font-size="11.5" font-weight="700" fill="var(--theme-accent)">Monitoring, kept low-burden</text>
<text x="310" y="229" font-size="11" fill="var(--text)">session RPE plus a three-item morning traffic light. Daily HRV is</text>
<text x="310" y="244" font-size="11" fill="var(--text)">skipped: broken parent sleep makes it noisy and prone to false alarms.</text>

<rect x="298" y="260" width="390" height="56" rx="8" fill="var(--surface)" stroke="var(--bad)"/>
<text x="310" y="278" font-size="11.5" font-weight="700" fill="var(--bad)">The red-flag rule</text>
<text x="310" y="295" font-size="11" fill="var(--text)">Achilles morning stiffness lasting beyond roughly 24 hours, or pain</text>
<text x="310" y="309" font-size="11" fill="var(--text)">that changes her gait, triggers an immediate cut to running load.</text>

<text x="298" y="329" font-size="11" fill="var(--text-dim)">The exam skill this case trains: state the decision plus its justification</text>
<text x="298" y="342" font-size="11" fill="var(--text-dim)">in two sentences. Grade the reasoning, not the phrasing.</text>
</svg>''',
        "Strengths get maintained, the limiter gets the budget, and the tendon gates every run progression.")


DIAGRAMS = {
    "of_decisiontree": d_of_decisiontree,
    "pc_doubles": d_pc_doubles,
    "st_wallball": d_st_wallball,
    "rb_injury_cause": d_rb_injury_cause,
    "sm_monitoring": d_sm_monitoring,
    "pc_testing": d_pc_testing,
    "rb_hip": d_rb_hip,
    "nu_working": d_nu_working,
    "sm_neuro": d_sm_neuro,
    "mp_sdt": d_mp_sdt,
    "pc_cases": d_pc_cases,
    "hp_format": d_hp_format,
    "mock_case": d_mock_case,
}
