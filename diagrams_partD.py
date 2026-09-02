# -*- coding: utf-8 -*-
"""Bespoke lesson diagrams - batch D."""

# One reduced-motion rule for the whole module: it disables the animation, never the
# static geometry inside the animated group. CSS cannot stop SMIL on its own, so the
# rule has to reach the <animate*> elements themselves.
_RM = ('<style>@media (prefers-reduced-motion: reduce){'
       '.dg-anim animate,.dg-anim animateMotion,.dg-anim animateTransform{display:none}}'
       '</style>')


def _open(h, label):
    # fill/stroke defaults are declared so an undefined colour token can never fall
    # back to the SVG initial black (fill) or none (stroke).
    return ('<svg viewBox="0 0 700 %d" preserveAspectRatio="xMidYMid meet" '
            'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s" '
            'font-family="ui-sans-serif, system-ui, Segoe UI, Roboto, sans-serif" '
            'font-size="11" fill="var(--text)" stroke="none" '
            'style="width:100%%;height:auto;max-height:360px;display:block">' % (h, label)) + _RM


def _wrap(did, title, body, caption=""):
    cap = f'<div class="w-hint">{caption}</div>' if caption else ""
    return (f'<div class="widget diagram" id="{did}">'
            f'<div class="w-head"><span class="w-icon">&#9672;</span><span class="w-title">{title}</span></div>'
            f'<div class="w-body">{body}</div>{cap}</div>')


def d_bm_techmodels():
    body = _open(310, "A filmed treadmill stride broken into right contact, flight and left contact by frame count, with the left-right asymmetry checked against a 10 percent working limit") + '''
<defs><marker id="bm_techmodels-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker></defs>
<rect x="20" y="6" width="196" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="118" y="26" text-anchor="middle" font-size="12" fill="var(--text)">1 &#183; Phases</text>
<text x="228" y="26" text-anchor="middle" font-size="13" fill="var(--text-dim)">&#8594;</text>
<rect x="238" y="6" width="196" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="336" y="26" text-anchor="middle" font-size="12" fill="var(--text)">2 &#183; Description</text>
<text x="446" y="26" text-anchor="middle" font-size="13" fill="var(--text-dim)">&#8594;</text>
<rect x="456" y="6" width="196" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="554" y="26" text-anchor="middle" font-size="12" fill="var(--text)">3 &#183; Attributes</text>
<text x="118" y="52" text-anchor="middle" font-size="11" fill="var(--text-dim)">the movement, split up</text>
<text x="336" y="52" text-anchor="middle" font-size="11" fill="var(--text-dim)">what to look for on video</text>
<text x="554" y="52" text-anchor="middle" font-size="11" fill="var(--text-dim)">what to train when cueing fails</text>
<text x="20" y="78" font-size="12" fill="var(--text-dim)">DIY protocol: film one treadmill speed at 240 fps, then count frames</text>
<text x="266" y="94" text-anchor="middle" font-size="11" fill="var(--text)">step time = 100 frames = 0.417 s</text>
<path d="M94 100 L94 106 M94 103 L437 103 M437 100 L437 106" fill="none" stroke="var(--text-dim)" stroke-width="1"/>
<rect x="94" y="112" width="206" height="28" rx="3" fill="var(--theme-accent)" opacity="0.85"/>
<rect x="300" y="112" width="137" height="28" rx="3" fill="none" stroke="var(--text-dim)" stroke-width="1.5" stroke-dasharray="5 4"/>
<rect x="437" y="112" width="189" height="28" rx="3" fill="var(--good)" opacity="0.85"/>
<g class="dg-anim"><line x1="94" y1="106" x2="94" y2="152" stroke="var(--good)" stroke-width="2"><animateTransform attributeName="transform" type="translate" values="0 0;532 0" dur="10s" repeatCount="1" fill="freeze"/></line></g>
<line x1="60" y1="146" x2="670" y2="146" stroke="var(--border)" stroke-width="1.5"/>
<path d="M94 146 L94 152 M300 146 L300 152 M437 146 L437 152 M626 146 L626 152" fill="none" stroke="var(--text-dim)" stroke-width="1"/>
<text x="94" y="166" text-anchor="middle" font-size="11" fill="var(--text-dim)">frame 100</text>
<text x="300" y="166" text-anchor="middle" font-size="11" fill="var(--text-dim)">160</text>
<text x="437" y="166" text-anchor="middle" font-size="11" fill="var(--text-dim)">200</text>
<text x="626" y="166" text-anchor="middle" font-size="11" fill="var(--text-dim)">255</text>
<text x="197" y="188" text-anchor="middle" font-size="11.5" fill="var(--text)">R contact 0.250 s</text>
<text x="368" y="188" text-anchor="middle" font-size="11.5" fill="var(--text)">flight 0.167 s</text>
<text x="531" y="188" text-anchor="middle" font-size="11.5" fill="var(--text)">L contact 0.229 s</text>
<line x1="20" y1="204" x2="680" y2="204" stroke="var(--border)" stroke-width="1"/>
<text x="20" y="226" font-size="12" fill="var(--text)">Left&#8211;right asymmetry, computed per metric</text>
<text x="198" y="252" text-anchor="middle" font-size="11" fill="var(--text)">8.4%</text>
<rect x="30" y="258" width="300" height="12" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<rect x="30" y="258" width="168" height="12" rx="6" fill="var(--theme-accent)" opacity="0.85"/>
<line x1="230" y1="252" x2="230" y2="276" stroke="var(--warn)" stroke-width="2"/>
<text x="230" y="290" text-anchor="middle" font-size="11" fill="var(--text-dim)">10% working limit</text>
<text x="30" y="304" font-size="11" fill="var(--text-dim)">(0.250 &#8722; 0.229) &#247; 0.250 &#215; 100 = 8.4%</text>
<rect x="390" y="214" width="290" height="82" rx="8" fill="var(--surface)" stroke="var(--border)"/>
<text x="404" y="236" font-size="12" fill="var(--text)">Leakage &#8212; the unifying fault</text>
<text x="404" y="256" font-size="11" fill="var(--text-dim)">a joint travels through its range while</text>
<text x="404" y="272" font-size="11" fill="var(--text-dim)">the implement gains no force</text>
<text x="404" y="288" font-size="11" fill="var(--text-dim)">(SkiErg hips drop; rowing seat slips)</text>
</svg>'''
    return _wrap("dg-bm_techmodels", "Building a technical model from video",
                 body,
                 "At 240 fps every interval is (frame difference) &#247; 240; average five contacts per side and keep each left&#8211;right gap under 10%.")


def d_hp_pacing():
    body = _open(320, "The race model as the sum of run, station and roxzone budgets, above two run-split shapes across the eight runs: a fading positive split and an even one") + '''
<rect x="20" y="28" width="170" height="36" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="105" y="51" text-anchor="middle" font-size="12" fill="var(--text)">&#931; 8 run splits</text>
<text x="200" y="52" text-anchor="middle" font-size="14" fill="var(--text-dim)">+</text>
<rect x="212" y="28" width="170" height="36" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="297" y="51" text-anchor="middle" font-size="12" fill="var(--text)">&#931; 8 station splits</text>
<text x="392" y="52" text-anchor="middle" font-size="14" fill="var(--text-dim)">+</text>
<rect x="404" y="28" width="150" height="36" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="479" y="51" text-anchor="middle" font-size="12" fill="var(--text)">roxzone 4&#8211;8 min</text>
<text x="564" y="52" text-anchor="middle" font-size="14" fill="var(--text-dim)">=</text>
<rect x="578" y="28" width="102" height="36" rx="6" fill="var(--theme-accent)"/>
<text x="629" y="51" text-anchor="middle" font-size="12" fill="var(--bg)">FINISH</text>
<text x="20" y="86" font-size="11.5" fill="var(--text-dim)">15 changeovers, not 8: 8 run&#8594;station plus 7 station&#8594;run (wall balls end at the finish line)</text>
<line x1="70" y1="110" x2="70" y2="262" stroke="var(--border)" stroke-width="1.5"/>
<line x1="70" y1="262" x2="665" y2="262" stroke="var(--border)" stroke-width="1.5"/>
<text x="62" y="118" text-anchor="end" font-size="11" fill="var(--text-dim)">slower</text>
<text x="62" y="262" text-anchor="end" font-size="11" fill="var(--text-dim)">faster</text>
<path d="M70 250 L154 224 L238 208 L322 190 L406 172 L490 158 L574 144 L658 132" fill="none" stroke="var(--bad)" stroke-width="2.5" stroke-dasharray="6 4"/>
<path id="hp_pacing-even" d="M70 214 L154 216 L238 216 L322 215 L406 216 L490 218 L574 222 L658 226" fill="none" stroke="var(--good)" stroke-width="2.5"/>
<g class="dg-anim"><circle r="4" fill="var(--good)"><animateMotion dur="9s" repeatCount="indefinite" path="M70 214 L154 216 L238 216 L322 215 L406 216 L490 218 L574 222 L658 226"/></circle></g>
<path d="M148 162 L84 244" fill="none" stroke="var(--bad)" stroke-width="1" stroke-dasharray="3 3"/><circle cx="70" cy="250" r="3.5" fill="var(--bad)"/><text x="80" y="140" font-size="11" fill="var(--text)">Run 1 is usually the fastest split</text>
<text x="80" y="156" font-size="11" fill="var(--text-dim)">&#8212; the honest baseline is runs 2&#8211;3</text>
<line x1="418" y1="236" x2="442" y2="236" stroke="var(--bad)" stroke-width="2.5" stroke-dasharray="6 4"/>
<text x="450" y="240" font-size="11" fill="var(--text-dim)">positive split (fade)</text>
<line x1="418" y1="252" x2="442" y2="252" stroke="var(--good)" stroke-width="2.5"/>
<text x="450" y="256" font-size="11" fill="var(--text-dim)">even to slight negative</text>
<text x="70" y="278" text-anchor="middle" font-size="11" fill="var(--text-dim)">R1</text>
<text x="154" y="278" text-anchor="middle" font-size="11" fill="var(--text-dim)">R2</text>
<text x="238" y="278" text-anchor="middle" font-size="11" fill="var(--text-dim)">R3</text>
<text x="322" y="278" text-anchor="middle" font-size="11" fill="var(--text-dim)">R4</text>
<text x="406" y="278" text-anchor="middle" font-size="11" fill="var(--text-dim)">R5</text>
<text x="490" y="278" text-anchor="middle" font-size="11" fill="var(--text-dim)">R6</text>
<text x="574" y="278" text-anchor="middle" font-size="11" fill="var(--text-dim)">R7</text>
<text x="658" y="278" text-anchor="middle" font-size="11" fill="var(--text-dim)">R8</text>
<path d="M238 292 L238 286 M238 292 L406 292 M406 292 L406 286" fill="none" stroke="var(--warn)" stroke-width="1.5"/>
<text x="322" y="308" text-anchor="middle" font-size="11" fill="var(--text)">sled push, sled pull and burpees (stations 2, 3, 4) surface here</text>
</svg>'''
    return _wrap("dg-hp_pacing", "The race model and the run-split shape",
                 body,
                 "Model all three ledgers or the prediction is wrong; time banked on run 1 is repaid at a worse rate on runs 3&#8211;5.")


def d_st_carry():
    body = _open(322, "Farmers carry drawn as a held stack with short steps, with the trunk working isometrically against the offset load") + '''
<defs><marker id="st_carry-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker></defs>
<text x="20" y="20" font-size="12" fill="var(--text-dim)">Anti-lateral flexion under an offset load</text>
<line x1="175" y1="36" x2="175" y2="250" stroke="var(--text-dimmer)" stroke-width="1" stroke-dasharray="4 4"/>
<circle cx="175" cy="56" r="12" fill="none" stroke="var(--text)" stroke-width="2"/>
<rect x="147" y="78" width="56" height="50" rx="10" fill="var(--surface-2)" stroke="var(--theme-accent)" stroke-width="2"/>
<line x1="175" y1="128" x2="175" y2="152" stroke="var(--text)" stroke-width="2"/>
<rect x="147" y="152" width="56" height="18" rx="5" fill="var(--surface-2)" stroke="var(--theme-accent)" stroke-width="2"/>
<line x1="149" y1="84" x2="130" y2="196" stroke="var(--text)" stroke-width="2"/>
<line x1="201" y1="84" x2="220" y2="196" stroke="var(--text)" stroke-width="2"/>
<rect x="114" y="196" width="32" height="38" rx="4" fill="var(--surface-2)" stroke="var(--text-dim)"/>
<rect x="204" y="196" width="32" height="38" rx="4" fill="var(--surface-2)" stroke="var(--text-dim)"/>
<line x1="130" y1="236" x2="130" y2="248" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#st_carry-ah)"/>
<line x1="220" y1="236" x2="220" y2="248" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#st_carry-ah)"/>
<path d="M209 88 q20 12 6 28" fill="none" stroke="var(--warn)" stroke-width="1.6" marker-end="url(#st_carry-ah)"/>
<path d="M141 88 q-20 12 -6 28" fill="none" stroke="var(--warn)" stroke-width="1.6" marker-end="url(#st_carry-ah)"/>
<text x="240" y="100" font-size="11" fill="var(--text-dim)">rib cage</text>
<text x="240" y="166" font-size="11" fill="var(--text-dim)">pelvis</text>
<text x="110" y="222" text-anchor="end" font-size="11" fill="var(--text-dim)">load</text>
<text x="244" y="222" font-size="11" fill="var(--text-dim)">load</text>
<text x="20" y="70" font-size="11" fill="var(--text-dim)">scapulae held down</text>
<line x1="118" y1="66" x2="143" y2="82" stroke="var(--text-dimmer)" stroke-width="1"/>
<text x="20" y="272" font-size="11.5" fill="var(--text)">Obliques, QL and deep stabilisers hold isometrically.</text>
<text x="20" y="290" font-size="11" fill="var(--text-dim)">Any deviation costs energy and disrupts gait.</text>
<text x="20" y="308" font-size="11" fill="var(--text-dim)">Neutral spine, slight thoracic extension, head still.</text>
<line x1="345" y1="20" x2="345" y2="310" stroke="var(--border)" stroke-width="1"/>
<text x="360" y="20" font-size="12" fill="var(--text-dim)">Centre-of-mass sway vs step length</text>
<text x="360" y="46" font-size="11.5" fill="var(--text)">long strides &#8212; more sway, more variability</text>
<line x1="370" y1="84" x2="634" y2="84" stroke="var(--text-dimmer)" stroke-width="1" stroke-dasharray="3 3"/>
<path id="st_carry-w1" d="M370 84 q44 -40 88 0 t88 0 t88 0" fill="none" stroke="var(--warn)" stroke-width="2.2"/>
<g class="dg-anim"><circle r="3.5" fill="var(--warn)"><animateMotion dur="6s" repeatCount="indefinite" path="M370 84 q44 -40 88 0 t88 0 t88 0"/></circle></g>
<text x="360" y="130" font-size="11.5" fill="var(--text)">compressed march &#8212; short controlled steps</text>
<line x1="370" y1="164" x2="634" y2="164" stroke="var(--text-dimmer)" stroke-width="1" stroke-dasharray="3 3"/>
<path id="st_carry-w2" d="M370 164 q22 -12 44 0 t44 0 t44 0 t44 0 t44 0 t44 0" fill="none" stroke="var(--good)" stroke-width="2.2"/>
<g class="dg-anim"><circle r="3.5" fill="var(--good)"><animateMotion dur="6s" repeatCount="indefinite" path="M370 164 q22 -12 44 0 t44 0 t44 0 t44 0 t44 0 t44 0"/></circle></g>
<text x="360" y="206" font-size="12" fill="var(--text-dim)">Which should fail first</text>
<rect x="360" y="218" width="130" height="32" rx="6" fill="var(--surface-2)" stroke="var(--good)"/>
<text x="425" y="238" text-anchor="middle" font-size="11" fill="var(--text)">postural control</text>
<line x1="496" y1="234" x2="522" y2="234" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#st_carry-ah)"/>
<rect x="528" y="218" width="130" height="32" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="593" y="238" text-anchor="middle" font-size="11" fill="var(--text)">grip</text>
<text x="360" y="274" font-size="11" fill="var(--text)">Grip first means the station is grip-capped.</text>
<text x="360" y="292" font-size="11" fill="var(--text-dim)">Grip is often inhibited upstream: shoulder</text>
<text x="360" y="308" font-size="11" fill="var(--text-dim)">girdle, lat, and the thumb (opponens).</text>
</svg>'''
    return _wrap("dg-st_carry", "Farmers carry: hold the stack, shorten the step",
                 body,
                 "The trunk works isometrically against an offset load; short steps cut sway, and posture should give out before grip does.")


def d_mp_raceday():
    body = _open(336, "The race split into sixteen chunks each with its own finish line, the attention dial between associative and dissociative, and the four-step refocus script after a bad station") + '''
<defs><marker id="mp_raceday-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker></defs>
<text x="20" y="14" font-size="11.5" fill="var(--text-dim)">Segmentation: 8 runs + 8 stations = 16 chunks, each with its own finish line</text>
<rect x="20" y="22" width="38" height="22" rx="4" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="39" y="37" text-anchor="middle" font-size="11" fill="var(--text-dim)">R1</text>
<rect x="61.3" y="22" width="38" height="22" rx="4" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="80.3" y="37" text-anchor="middle" font-size="11" fill="var(--text)">S1</text>
<rect x="102.6" y="22" width="38" height="22" rx="4" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="121.6" y="37" text-anchor="middle" font-size="11" fill="var(--text-dim)">R2</text>
<rect x="143.9" y="22" width="38" height="22" rx="4" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="162.9" y="37" text-anchor="middle" font-size="11" fill="var(--text)">S2</text>
<rect x="185.2" y="22" width="38" height="22" rx="4" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="204.2" y="37" text-anchor="middle" font-size="11" fill="var(--text-dim)">R3</text>
<rect x="226.5" y="22" width="38" height="22" rx="4" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="245.5" y="37" text-anchor="middle" font-size="11" fill="var(--text)">S3</text>
<rect x="267.8" y="22" width="38" height="22" rx="4" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="286.8" y="37" text-anchor="middle" font-size="11" fill="var(--text-dim)">R4</text>
<rect x="309.1" y="22" width="38" height="22" rx="4" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="328.1" y="37" text-anchor="middle" font-size="11" fill="var(--text)">S4</text>
<rect x="350.4" y="22" width="38" height="22" rx="4" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="369.4" y="37" text-anchor="middle" font-size="11" fill="var(--text-dim)">R5</text>
<rect x="391.7" y="22" width="38" height="22" rx="4" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="410.7" y="37" text-anchor="middle" font-size="11" fill="var(--text)">S5</text>
<rect x="433" y="22" width="38" height="22" rx="4" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="452" y="37" text-anchor="middle" font-size="11" fill="var(--text-dim)">R6</text>
<rect x="474.3" y="22" width="38" height="22" rx="4" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="493.3" y="37" text-anchor="middle" font-size="11" fill="var(--text)">S6</text>
<rect x="515.6" y="22" width="38" height="22" rx="4" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="534.6" y="37" text-anchor="middle" font-size="11" fill="var(--text-dim)">R7</text>
<rect x="556.9" y="22" width="38" height="22" rx="4" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="575.9" y="37" text-anchor="middle" font-size="11" fill="var(--text)">S7</text>
<rect x="598.2" y="22" width="38" height="22" rx="4" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="617.2" y="37" text-anchor="middle" font-size="11" fill="var(--text-dim)">R8</text>
<rect x="639.5" y="22" width="38" height="22" rx="4" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="658.5" y="37" text-anchor="middle" font-size="11" fill="var(--text)">S8</text>
<text x="20" y="72" font-size="12" fill="var(--text-dim)">Attention is a dial, not a switch</text>
<path d="M88 210 A92 92 0 0 1 272 210" fill="none" stroke="var(--border)" stroke-width="10" stroke-linecap="round"/>
<path d="M88 210 A92 92 0 0 1 180 118" fill="none" stroke="var(--theme-accent)" stroke-width="10" stroke-linecap="round" opacity="0.55"/>
<g class="dg-anim"><line x1="180" y1="210" x2="180" y2="128" stroke="var(--text)" stroke-width="2.5" stroke-linecap="round"><animateTransform attributeName="transform" type="rotate" values="-62 180 210;62 180 210;-62 180 210" dur="9s" repeatCount="indefinite" calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1" keyTimes="0;0.5;1"/></line></g>
<circle cx="180" cy="210" r="5" fill="var(--theme-accent)"/>
<text x="88" y="232" text-anchor="middle" font-size="11.5" fill="var(--text)">ASSOCIATIVE</text>
<text x="88" y="250" text-anchor="middle" font-size="11" fill="var(--text-dim)">breath, cadence,</text>
<text x="88" y="266" text-anchor="middle" font-size="11" fill="var(--text-dim)">split, technique</text>
<text x="272" y="232" text-anchor="middle" font-size="11.5" fill="var(--text)">DISSOCIATIVE</text>
<text x="272" y="250" text-anchor="middle" font-size="11" fill="var(--text-dim)">counting, mantra,</text>
<text x="272" y="266" text-anchor="middle" font-size="11" fill="var(--text-dim)">scenery, rhythm</text>
<line x1="340" y1="60" x2="340" y2="290" stroke="var(--border)" stroke-width="1"/>
<text x="360" y="72" font-size="12" fill="var(--text-dim)">After a bad station: the refocus script</text>
<rect x="360" y="86" width="300" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="374" y="106" font-size="11" fill="var(--text)">1 &#183; Acknowledge (1&#8211;2 s)</text>
<line x1="378" y1="118" x2="378" y2="130" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#mp_raceday-ah)"/>
<rect x="360" y="132" width="300" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="374" y="152" font-size="11" fill="var(--text)">2 &#183; Physical reset: exhale, posture</text>
<line x1="378" y1="164" x2="378" y2="176" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#mp_raceday-ah)"/>
<rect x="360" y="178" width="300" height="30" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="374" y="198" font-size="11" fill="var(--text)">3 &#183; One process cue</text>
<line x1="378" y1="210" x2="378" y2="222" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#mp_raceday-ah)"/>
<rect x="360" y="224" width="300" height="30" rx="6" fill="var(--surface-2)" stroke="var(--theme-accent)"/>
<text x="374" y="244" font-size="11" fill="var(--text)">4 &#183; Attention forward to the next chunk</text>
<text x="360" y="276" font-size="11" fill="var(--text-dim)">No in-race score-keeping: one loss stays one loss.</text>
<text x="20" y="306" font-size="11.5" fill="var(--text)">Associate when the task can go wrong: sled, burpee broad jump, wall-ball depth, roxzone.</text>
<text x="20" y="326" font-size="11.5" fill="var(--text)">Dissociate when output is locked and discomfort is the only problem.</text>
</svg>'''
    return _wrap("dg-mp_raceday", "Race day: the attention dial and the reset",
                 body,
                 "Chunk the race into 16 finish lines, turn the dial to suit the task, and rehearse the reset &#8212; race rules ban headphones, so every dissociation cue is internal.")


def d_st_burpee():
    body = _open(322, "The burpee broad jump drawn as a recycled landing-to-jump rhythm rather than a reset, with the cost of a longer jump") + '''
<defs><marker id="st_burpee-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker></defs>
<text x="20" y="20" font-size="12" fill="var(--text-dim)">One repetition: where the energy goes</text>
<line x1="30" y1="232" x2="430" y2="232" stroke="var(--border)" stroke-width="2"/>
<path d="M60 232 Q155 112 250 232" fill="none" stroke="var(--warn)" stroke-width="2" stroke-dasharray="6 4"/>
<text x="155" y="138" text-anchor="middle" font-size="11" fill="var(--text-dim)">excess vertical oscillation = wasted energy</text>
<path d="M60 232 Q155 182 250 232" fill="none" stroke="var(--theme-accent)" stroke-width="2.5"/>
<g class="dg-anim"><circle r="4.5" fill="var(--theme-accent)"><animateMotion dur="3.6s" repeatCount="indefinite" path="M60 232 Q155 182 250 232"/></circle></g>
<text x="155" y="222" text-anchor="middle" font-size="11" fill="var(--text)">flat and forward</text>
<circle cx="60" cy="232" r="4" fill="var(--text)"/>
<text x="60" y="254" text-anchor="middle" font-size="11" fill="var(--text)">take-off</text>
<text x="60" y="270" text-anchor="middle" font-size="11" fill="var(--text-dim)">hip-dominant</text>
<circle cx="250" cy="232" r="4" fill="var(--text)"/>
<text x="250" y="254" text-anchor="middle" font-size="11" fill="var(--text)">landing</text>
<text x="250" y="270" text-anchor="middle" font-size="11" fill="var(--text-dim)">hip + knee + ankle</text>
<line x1="264" y1="232" x2="342" y2="232" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#st_burpee-ah)"/>
<text x="303" y="224" text-anchor="middle" font-size="11" fill="var(--text)">recycle</text>
<rect x="348" y="216" width="78" height="32" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="387" y="236" text-anchor="middle" font-size="11" fill="var(--text)">next rep</text>
<text x="20" y="294" font-size="11" fill="var(--text-dim)">Energy recycling: carry the landing into the next jump, do not reset.</text>
<text x="20" y="312" font-size="11" fill="var(--text-dim)">Each landing preloads lower- and upper-body tendons.</text>
<line x1="440" y1="20" x2="440" y2="312" stroke="var(--border)" stroke-width="1"/>
<text x="458" y="20" font-size="12" fill="var(--text-dim)">Longer jump: the trade-off</text>
<text x="458" y="48" font-size="11" fill="var(--good)">&#8595; reps to cover the distance</text>
<text x="458" y="70" font-size="11" fill="var(--text)">&#8593; explosive power required</text>
<text x="458" y="92" font-size="11" fill="var(--text)">&#8593; heart-rate spike</text>
<text x="458" y="114" font-size="11" fill="var(--text)">&#8593; eccentric landing load</text>
<rect x="458" y="132" width="222" height="72" rx="8" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="470" y="154" font-size="11" fill="var(--text)">So train the absorbers:</text>
<text x="470" y="172" font-size="11" fill="var(--text-dim)">heavy controlled squats,</text>
<text x="470" y="190" font-size="11" fill="var(--text-dim)">plus plyometrics for elasticity</text>
<text x="458" y="230" font-size="11.5" fill="var(--text-dim)">Safety</text>
<rect x="458" y="240" width="222" height="26" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="470" y="257" font-size="11" fill="var(--text)">neutral wrist alignment</text>
<rect x="458" y="274" width="222" height="26" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="470" y="291" font-size="11" fill="var(--text)">control spinal flexion down</text>
</svg>'''
    return _wrap("dg-st_burpee", "Burpee broad jump: recycle, do not reset",
                 body,
                 "Elastic athletes turn each landing into the next jump; a longer jump buys fewer reps at the price of power, heart rate and eccentric load.")


def d_mp_routines():
    body = _open(330, "Pre-race and in-race routines that cut decision load, beside a training journal loop that turns scattered sessions into patterns") + '''
<defs><marker id="mp_routines-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker></defs>
<text x="20" y="20" font-size="12" fill="var(--text-dim)">Three routines worth building</text>
<rect x="20" y="30" width="310" height="46" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="34" y="50" font-size="11.5" fill="var(--text)">PRE-RACE</text>
<text x="34" y="68" font-size="11" fill="var(--text-dim)">nutrition, warm-up, kit, activation, cues</text>
<rect x="20" y="84" width="310" height="46" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="34" y="104" font-size="11.5" fill="var(--text)">PRE-STATION</text>
<text x="34" y="122" font-size="11" fill="var(--text-dim)">a breath, a grip check, a cue word</text>
<rect x="20" y="138" width="310" height="46" rx="8" fill="var(--surface-2)" stroke="var(--theme-accent)" stroke-width="2"/>
<text x="34" y="158" font-size="11.5" fill="var(--text)">POST-ERROR RESET</text>
<text x="34" y="176" font-size="11" fill="var(--text-dim)">the highest-value routine in HYROX</text>
<rect x="20" y="198" width="72" height="26" rx="13" fill="var(--surface)" stroke="var(--border)"/>
<text x="56" y="215" text-anchor="middle" font-size="11" fill="var(--text)">short</text>
<rect x="99" y="198" width="72" height="26" rx="13" fill="var(--surface)" stroke="var(--border)"/>
<text x="135" y="215" text-anchor="middle" font-size="11" fill="var(--text)">portable</text>
<rect x="178" y="198" width="72" height="26" rx="13" fill="var(--surface)" stroke="var(--border)"/>
<text x="214" y="215" text-anchor="middle" font-size="11" fill="var(--text)">controllable</text>
<rect x="257" y="198" width="72" height="26" rx="13" fill="var(--surface)" stroke="var(--border)"/>
<text x="293" y="215" text-anchor="middle" font-size="11" fill="var(--text)">rehearsed</text>
<text x="20" y="250" font-size="11" fill="var(--text)">Rehearsed under fatigue, or it is not a routine.</text>
<text x="20" y="276" font-size="11" fill="var(--text-dim)">A routine has a functional mechanism.</text>
<text x="20" y="294" font-size="11" fill="var(--text-dim)">A superstition credits an unrelated act and</text>
<text x="20" y="310" font-size="11" fill="var(--text-dim)">creates anxiety the moment it is broken.</text>
<line x1="345" y1="16" x2="345" y2="314" stroke="var(--border)" stroke-width="1"/>
<text x="360" y="20" font-size="12" fill="var(--text-dim)">The journal loop</text>
<rect x="360" y="30" width="290" height="38" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="374" y="54" font-size="11" fill="var(--text)">Objective: session, splits, load</text>
<line x1="382" y1="70" x2="382" y2="82" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#mp_routines-ah)"/>
<rect x="360" y="84" width="290" height="38" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="374" y="108" font-size="11" fill="var(--text)">Subjective: RPE, mood, sleep, stress</text>
<line x1="382" y1="124" x2="382" y2="136" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#mp_routines-ah)"/>
<rect x="360" y="138" width="290" height="38" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="374" y="162" font-size="11" fill="var(--text)">Patterns emerge across weeks</text>
<line x1="382" y1="178" x2="382" y2="190" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#mp_routines-ah)"/>
<rect x="360" y="192" width="290" height="38" rx="8" fill="var(--surface)" stroke="var(--theme-accent)" stroke-width="2"/>
<text x="374" y="216" font-size="11" fill="var(--text)">3 &#215; 3: learned / done well / improve</text>
<g class="dg-anim"><path d="M652 211 L674 211 L674 49 L654 49" fill="none" stroke="var(--theme-accent)" stroke-width="2" stroke-dasharray="6 6" marker-end="url(#mp_routines-ah)"><animate attributeName="stroke-dashoffset" values="24;0" dur="2.2s" repeatCount="indefinite"/></path></g>
<text x="360" y="254" font-size="11" fill="var(--text-dim)">Reflection-on-action gradually sharpens</text>
<text x="360" y="270" font-size="11" fill="var(--text-dim)">reflection-in-action.</text>
<text x="360" y="294" font-size="11" fill="var(--text-dim)">Memory for subjective states is biased by</text>
<text x="360" y="310" font-size="11" fill="var(--text-dim)">the most recent session. Coaches log too.</text>
</svg>'''
    return _wrap("dg-mp_routines", "Routines that hold, journals that compound",
                 body,
                 "Routines cut decision load when working memory is degraded; the journal turns scattered sessions into patterns you can act on.")


def d_sk_motor_learning():
    body = _open(336, "The cognitive, associative and autonomous stages with automation rising as attention cost falls, beside blocked versus random practice and the fatigue rule") + '''
<text x="40" y="22" font-size="11" fill="var(--text-dim)">A continuum, not thresholds &#8212; the autonomous stage takes extensive practice</text>
<g class="dg-anim"><path d="M54 30 L66 30 L60 40 Z" fill="var(--theme-accent)"><animateTransform attributeName="transform" type="translate" values="0 0;580 0" dur="16s" repeatCount="1" fill="freeze"/></path></g>
<rect x="40" y="44" width="620" height="26" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<line x1="246.7" y1="44" x2="246.7" y2="70" stroke="var(--border)"/>
<line x1="453.3" y1="44" x2="453.3" y2="70" stroke="var(--border)"/>
<text x="143" y="62" text-anchor="middle" font-size="11.5" fill="var(--text)">COGNITIVE</text>
<text x="350" y="62" text-anchor="middle" font-size="11.5" fill="var(--text)">ASSOCIATIVE</text>
<text x="557" y="62" text-anchor="middle" font-size="11.5" fill="var(--text)">AUTONOMOUS</text>
<text x="143" y="88" text-anchor="middle" font-size="11" fill="var(--text-dim)">large errors, heavy attention</text>
<text x="350" y="88" text-anchor="middle" font-size="11" fill="var(--text-dim)">errors shrink, self-detection</text>
<text x="557" y="88" text-anchor="middle" font-size="11" fill="var(--text-dim)">automatic, attention freed</text>
<line x1="60" y1="106" x2="60" y2="204" stroke="var(--border)" stroke-width="1.5"/>
<text x="52" y="114" text-anchor="end" font-size="11" fill="var(--text-dim)">high</text>
<text x="52" y="204" text-anchor="end" font-size="11" fill="var(--text-dim)">low</text>
<path d="M60 196 C200 180 380 130 600 116" fill="none" stroke="var(--theme-accent)" stroke-width="2.5"/>
<text x="606" y="119" font-size="11" fill="var(--text)">automation</text>
<path d="M60 116 C200 132 380 182 600 196" fill="none" stroke="var(--warn)" stroke-width="2.5"/>
<text x="606" y="199" font-size="11" fill="var(--text)">attention cost</text>
<path d="M60 132 C200 152 380 168 600 172" fill="none" stroke="var(--text-dim)" stroke-width="2" stroke-dasharray="5 4"/>
<text x="606" y="168" font-size="11" fill="var(--text-dim)">variability</text>
<text x="40" y="240" font-size="12" fill="var(--text-dim)">Practice design</text>
<rect x="40" y="250" width="300" height="32" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="54" y="270" font-size="11" fill="var(--text)">Blocked / constant: &#8593; today, &#8595; retention</text>
<rect x="40" y="288" width="300" height="32" rx="6" fill="var(--surface-2)" stroke="var(--theme-accent)"/>
<text x="54" y="308" font-size="11" fill="var(--text)">Random / variable: &#8595; today, &#8593; retention</text>
<text x="40" y="332" font-size="11" fill="var(--text-dim)">contextual interference &#8212; true novices start blocked</text>
<line x1="358" y1="222" x2="358" y2="332" stroke="var(--border)" stroke-width="1"/>
<text x="378" y="240" font-size="12" fill="var(--text-dim)">The fatigue rule</text>
<text x="378" y="264" font-size="11" fill="var(--text)">Acquire technique fresh, early in the session.</text>
<text x="378" y="284" font-size="11" fill="var(--text)">Stress-test an acquired skill fatigued, later.</text>
<text x="378" y="310" font-size="11" fill="var(--text-dim)">Fatigue lowers proprioception, force control</text>
<text x="378" y="326" font-size="11" fill="var(--text-dim)">and the athlete&#8217;s own error detection.</text>
</svg>'''
    return _wrap("dg-sk_motor_learning", "Stages, practice design and the fatigue rule",
                 body,
                 "Learning is what survives a delayed retention test &#8212; the practice that feels worst in the session is usually the one that retains.")


def d_nu_hydration():
    body = _open(336, "The hydration window with exercise-associated hyponatraemia on one side and dehydration on the other, and the sweat-rate arithmetic between them") + '''
<text x="115" y="50" text-anchor="middle" font-size="11.5" fill="var(--text)">EAH</text>
<text x="330" y="50" text-anchor="middle" font-size="11.5" fill="var(--text)">EUHYDRATION</text>
<text x="565" y="50" text-anchor="middle" font-size="11.5" fill="var(--text)">HYPOHYDRATION</text>
<rect x="40" y="58" width="150" height="30" rx="4" fill="var(--surface-2)" stroke="var(--bad)" stroke-width="2"/>
<rect x="190" y="58" width="280" height="30" fill="var(--surface-2)" stroke="var(--theme-accent)" stroke-width="2"/>
<g class="dg-anim"><rect x="194" y="62" width="272" height="22" fill="var(--theme-accent)" opacity="0.18"><animate attributeName="opacity" values="0.10;0.28;0.10" dur="7s" repeatCount="indefinite"/></rect></g>
<rect x="470" y="58" width="190" height="30" rx="4" fill="var(--surface-2)" stroke="var(--warn)" stroke-width="2"/>
<text x="115" y="106" text-anchor="middle" font-size="11" fill="var(--text-dim)">over-drinking</text>
<text x="115" y="122" text-anchor="middle" font-size="11" fill="var(--text-dim)">serum Na &lt; 135 mmol/L</text>
<text x="330" y="106" text-anchor="middle" font-size="11" fill="var(--text-dim)">the start-line target</text>
<text x="565" y="106" text-anchor="middle" font-size="11" fill="var(--text-dim)">&#8805; 2% body-mass loss</text>
<text x="565" y="122" text-anchor="middle" font-size="11" fill="var(--text-dim)">&#8595; plasma volume, &#8593; HR, &#8593; RPE, &#8593; core temp</text>
<text x="40" y="152" font-size="11.5" fill="var(--text)">sweat rate (L/h) = (pre-BM &#8722; post-BM + fluid in &#8722; urine out) &#247; hours</text>
<text x="40" y="172" font-size="11" fill="var(--text-dim)">1 kg body mass &#8776; 1 L fluid &#183; typical 0.5&#8211;2.0 L/h &#183; sweat Na 20&#8211;80 mmol/L</text>
<rect x="30" y="188" width="206" height="110" rx="8" fill="var(--surface)" stroke="var(--border)"/>
<text x="42" y="210" font-size="11.5" fill="var(--text)">BEFORE</text>
<text x="42" y="232" font-size="11" fill="var(--text-dim)">5&#8211;7 mL/kg, &#8805; 4 h out</text>
<text x="42" y="250" font-size="11" fill="var(--text-dim)">+3&#8211;5 mL/kg ~2 h out if dark</text>
<text x="42" y="268" font-size="11" fill="var(--text-dim)">200&#8211;300 mL near the start</text>
<text x="42" y="286" font-size="11" fill="var(--text-dim)">aim for pale-yellow urine</text>
<rect x="247" y="188" width="206" height="110" rx="8" fill="var(--surface)" stroke="var(--theme-accent)"/>
<text x="259" y="210" font-size="11.5" fill="var(--text)">DURING</text>
<text x="259" y="232" font-size="11" fill="var(--text-dim)">0.4&#8211;0.8 L/h, toward sweat rate</text>
<text x="259" y="250" font-size="11" fill="var(--text-dim)">never above measured sweat rate</text>
<text x="259" y="268" font-size="11" fill="var(--text-dim)">sports drink Na 10&#8211;25 mmol/L</text>
<text x="259" y="286" font-size="11" fill="var(--text-dim)">high-Na formulas 30&#8211;50+ mmol/L</text>
<rect x="464" y="188" width="206" height="110" rx="8" fill="var(--surface)" stroke="var(--border)"/>
<text x="476" y="210" font-size="11.5" fill="var(--text)">AFTER</text>
<text x="476" y="232" font-size="11" fill="var(--text-dim)">125&#8211;150% of the deficit</text>
<text x="476" y="250" font-size="11" fill="var(--text-dim)">over 2&#8211;4 h, with sodium</text>
<text x="476" y="268" font-size="11" fill="var(--text-dim)">sodium drives retention</text>
<text x="476" y="286" font-size="11" fill="var(--text-dim)">plain water &#8594; diuresis</text>
<text x="30" y="322" font-size="11" fill="var(--text-dim)">Indoor venues are humid, crowded and still: do not plan from cool-gym training data.</text>
</svg>'''
    return _wrap("dg-nu_hydration", "The hydration window: two ways to get it wrong",
                 body,
                 "Measure, do not assume: 2% body-mass loss is a planning guideline, and the opposite error &#8212; volumes of plain water &#8212; is hyponatraemia.")


def d_sm_injuries():
    body = _open(344, "A jagged applied-load line crossing a slowly rising tissue-capacity curve at the point injury appears, beside intrinsic and extrinsic risk factors") + '''
<text x="40" y="22" font-size="12" fill="var(--text-dim)">Load-tolerance mismatch</text>
<text x="60" y="40" font-size="11" fill="var(--text-dim)">load / tissue capacity</text>
<line x1="60" y1="46" x2="60" y2="250" stroke="var(--border)" stroke-width="1.5"/>
<line x1="60" y1="250" x2="380" y2="250" stroke="var(--border)" stroke-width="1.5"/>
<path d="M60 238 C140 224 240 194 372 176" fill="none" stroke="var(--good)" stroke-width="2.5"/>
<path d="M60 246 L104 230 L148 236 L192 216 L236 206 L272 150 L306 166 L344 112 L372 124" fill="none" stroke="var(--theme-accent)" stroke-width="2"/>
<g class="dg-anim"><circle cx="240" cy="197" r="6" fill="var(--bad)"><animate attributeName="r" values="5;8;5" dur="3.4s" repeatCount="indefinite"/></circle></g>
<line x1="244" y1="192" x2="266" y2="104" stroke="var(--text-dimmer)" stroke-width="1"/>
<text x="252" y="76" font-size="11" fill="var(--text)">injury: applied load crosses</text>
<text x="252" y="92" font-size="11" fill="var(--text)">the capacity actually built</text>
<text x="60" y="270" font-size="11" fill="var(--text-dim)">training weeks &#8594;</text>
<line x1="190" y1="266" x2="214" y2="266" stroke="var(--good)" stroke-width="2.5"/>
<text x="220" y="270" font-size="11" fill="var(--text-dim)">capacity</text>
<line x1="290" y1="266" x2="314" y2="266" stroke="var(--theme-accent)" stroke-width="2"/>
<text x="320" y="270" font-size="11" fill="var(--text-dim)">load</text>
<line x1="396" y1="16" x2="396" y2="278" stroke="var(--border)" stroke-width="1"/>
<text x="414" y="22" font-size="12" fill="var(--text-dim)">Risk factors</text>
<text x="414" y="48" font-size="11.5" fill="var(--text)">INTRINSIC</text>
<text x="414" y="68" font-size="11" fill="var(--text-dim)">prior injury, same site (strongest)</text>
<text x="414" y="86" font-size="11" fill="var(--text-dim)">age, mobility limits, asymmetry</text>
<text x="414" y="104" font-size="11" fill="var(--text-dim)">running mechanics</text>
<text x="414" y="122" font-size="11" fill="var(--text-dim)">sleep, energy availability (RED-S)</text>
<text x="414" y="152" font-size="11.5" fill="var(--text)">EXTRINSIC</text>
<text x="414" y="172" font-size="11" fill="var(--text-dim)">weekly volume and its rate of change</text>
<text x="414" y="190" font-size="11" fill="var(--text-dim)">sled load, floor friction</text>
<text x="414" y="208" font-size="11" fill="var(--text-dim)">footwear, surface</text>
<text x="414" y="226" font-size="11" fill="var(--text-dim)">race density, coaching quality</text>
<rect x="410" y="240" width="270" height="34" rx="6" fill="var(--surface-2)" stroke="var(--theme-accent)"/>
<text x="422" y="261" font-size="11" fill="var(--text)">Change ONE variable at a time.</text>
<line x1="40" y1="290" x2="680" y2="290" stroke="var(--border)" stroke-width="1"/>
<text x="40" y="310" font-size="11" fill="var(--text-dim)">Achilles/calf &#8212; sled push, running, burpee rebounds</text>
<text x="40" y="330" font-size="11" fill="var(--text-dim)">Knee &#8212; sandbag lunges, wall-ball squat volume</text>
<text x="380" y="310" font-size="11" fill="var(--text-dim)">Lumbar &#8212; sled-pull hinge, ski/row collapse</text>
<text x="380" y="330" font-size="11" fill="var(--text-dim)">Shoulder &#8212; wall balls overhead, chest-to-floor</text>
</svg>'''
    return _wrap("dg-sm_injuries", "Why HYROX injuries are overuse injuries",
                 body,
                 "Injury sits where applied load crosses the capacity the tissue has actually built &#8212; and prior injury at the same site is the most consistent predictor.")


def d_mp_winners():
    body = _open(320, "The controllables an athlete can narrow attention onto, arousal read as readiness, and the evidence loop that builds earned confidence") + '''
<defs><marker id="mp_winners-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker></defs>
<circle cx="170" cy="160" r="118" fill="none" stroke="var(--text-dimmer)" stroke-width="1.5" stroke-dasharray="5 5"/>
<circle cx="170" cy="160" r="66" fill="var(--surface-2)" stroke="var(--theme-accent)" stroke-width="2"/>
<text x="170" y="122" text-anchor="middle" font-size="11.5" fill="var(--text)">CONTROLLABLES</text>
<text x="170" y="144" text-anchor="middle" font-size="11" fill="var(--text-dim)">effort, attention</text>
<text x="170" y="162" text-anchor="middle" font-size="11" fill="var(--text-dim)">technique, pacing</text>
<text x="170" y="180" text-anchor="middle" font-size="11" fill="var(--text-dim)">routine, response</text>
<text x="170" y="64" text-anchor="middle" font-size="11" fill="var(--text-dim)">results</text>
<text x="170" y="258" text-anchor="middle" font-size="11" fill="var(--text-dim)">conditions</text>
<text x="78" y="164" text-anchor="middle" font-size="11" fill="var(--text-dim)">rivals</text>
<text x="262" y="164" text-anchor="middle" font-size="11" fill="var(--text-dim)">friction</text>
<text x="20" y="302" font-size="11" fill="var(--text-dim)">Attention spent outside the inner circle is wasted.</text>
<line x1="330" y1="16" x2="330" y2="308" stroke="var(--border)" stroke-width="1"/>
<text x="350" y="22" font-size="12" fill="var(--text-dim)">Same arousal, two readings</text>
<rect x="350" y="40" width="140" height="36" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="420" y="63" text-anchor="middle" font-size="11" fill="var(--text)">arousal at the gun</text>
<path d="M494 52 L534 40" fill="none" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#mp_winners-ah)"/>
<path d="M494 64 L534 88" fill="none" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#mp_winners-ah)"/>
<rect x="540" y="24" width="146" height="32" rx="6" fill="var(--surface-2)" stroke="var(--good)" stroke-width="2"/>
<text x="613" y="45" text-anchor="middle" font-size="11" fill="var(--text)">read as READY</text>
<rect x="540" y="74" width="146" height="32" rx="6" fill="var(--surface-2)" stroke="var(--bad)" stroke-width="2"/>
<text x="613" y="95" text-anchor="middle" font-size="11" fill="var(--text)">read as DANGER</text>
<text x="350" y="130" font-size="11" fill="var(--text-dim)">Challenge appraisal enhances; threat appraisal degrades.</text>
<text x="350" y="164" font-size="12" fill="var(--text-dim)">Confidence is an output, not an input</text>
<rect x="350" y="176" width="196" height="28" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="362" y="195" font-size="11" fill="var(--text)">completed hard sessions</text>
<rect x="350" y="212" width="196" height="28" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="362" y="231" font-size="11" fill="var(--text)">benchmark improvements</text>
<rect x="350" y="248" width="196" height="28" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="362" y="267" font-size="11" fill="var(--text)">rehearsed race scenarios</text>
<g class="dg-anim"><path d="M550 190 L566 190 L566 226 M550 226 L566 226 M550 262 L566 262 L566 226 M566 226 L586 226" fill="none" stroke="var(--theme-accent)" stroke-width="2" stroke-dasharray="5 5" marker-end="url(#mp_winners-ah)"><animate attributeName="stroke-dashoffset" values="20;0" dur="2s" repeatCount="indefinite"/></path></g>
<rect x="592" y="208" width="94" height="36" rx="6" fill="var(--theme-accent)"/>
<text x="639" y="231" text-anchor="middle" font-size="11.5" fill="var(--bg)">CONFIDENCE</text>
<text x="350" y="302" font-size="11" fill="var(--text-dim)">Built in training under fatigue, not summoned on race day.</text>
</svg>'''
    return _wrap("dg-mp_winners", "Controllables, appraisal and earned confidence",
                 body,
                 "The winner&#8217;s mindset is a set of trainable habits: narrow attention to the controllables, read arousal as readiness, and let evidence build the confidence.")


def d_pc_highperf():
    body = _open(330, "Adaptation per unit of stimulus falling from novice to elite, with a narrowing window between productive overload and non-functional overreaching") + '''
<text x="40" y="22" font-size="12" fill="var(--text-dim)">Diminishing returns</text>
<text x="64" y="40" font-size="11" fill="var(--text-dim)">adaptation per unit of stimulus</text>
<line x1="64" y1="46" x2="64" y2="252" stroke="var(--border)" stroke-width="1.5"/>
<line x1="64" y1="252" x2="380" y2="252" stroke="var(--border)" stroke-width="1.5"/>
<path d="M70 62 C160 142 250 196 372 222 L372 246 C250 236 160 204 70 124 Z" fill="var(--theme-accent)" opacity="0.15"/>
<path d="M70 92 C160 172 250 216 372 234" fill="none" stroke="var(--theme-accent)" stroke-width="2.5"/>
<g class="dg-anim"><circle r="4.5" fill="var(--theme-accent)"><animateMotion dur="11s" repeatCount="indefinite" path="M70 92 C160 172 250 216 372 234"/></circle></g>
<text x="196" y="140" font-size="11" fill="var(--text)">the window between</text>
<text x="196" y="156" font-size="11" fill="var(--text)">productive overload and</text>
<text x="196" y="172" font-size="11" fill="var(--text)">non-functional overreaching</text>
<line x1="300" y1="180" x2="336" y2="222" stroke="var(--text-dimmer)" stroke-width="1"/>
<text x="64" y="272" font-size="11" fill="var(--text-dim)">novice &#8594; elite (training status)</text>
<text x="40" y="298" font-size="11" fill="var(--text-dim)">A year of 2% improvement is an excellent outcome.</text>
<text x="40" y="316" font-size="11" fill="var(--text-dim)">Progression is measured across seasons, not blocks.</text>
<line x1="396" y1="16" x2="396" y2="320" stroke="var(--border)" stroke-width="1"/>
<text x="414" y="22" font-size="12" fill="var(--text-dim)">Where the leverage is</text>
<rect x="414" y="34" width="34" height="30" rx="5" fill="var(--theme-accent)"/>
<text x="431" y="54" text-anchor="middle" font-size="11.5" fill="var(--bg)">K</text>
<rect x="453" y="34" width="34" height="30" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="470" y="54" text-anchor="middle" font-size="11.5" fill="var(--text-dim)">&#183;</text>
<rect x="492" y="34" width="34" height="30" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="509" y="54" text-anchor="middle" font-size="11.5" fill="var(--text-dim)">&#183;</text>
<rect x="531" y="34" width="34" height="30" rx="5" fill="var(--theme-accent)"/>
<text x="548" y="54" text-anchor="middle" font-size="11.5" fill="var(--bg)">K</text>
<rect x="570" y="34" width="34" height="30" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="587" y="54" text-anchor="middle" font-size="11.5" fill="var(--text-dim)">&#183;</text>
<rect x="609" y="34" width="34" height="30" rx="5" fill="var(--theme-accent)"/>
<text x="626" y="54" text-anchor="middle" font-size="11.5" fill="var(--bg)">K</text>
<rect x="648" y="34" width="34" height="30" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="665" y="54" text-anchor="middle" font-size="11.5" fill="var(--text-dim)">&#183;</text>
<text x="414" y="84" font-size="11" fill="var(--text-dim)">K = the 2&#8211;3 sessions that drive the block.</text>
<text x="414" y="100" font-size="11" fill="var(--text-dim)">Everything else exists to protect them.</text>
<text x="414" y="128" font-size="11" fill="var(--text-dim)">Polarised / pyramidal distribution</text>
<rect x="414" y="136" width="216" height="24" rx="4" fill="var(--surface-2)" stroke="var(--border)"/>
<rect x="634" y="136" width="48" height="24" rx="4" fill="var(--theme-accent)"/>
<text x="522" y="176" text-anchor="middle" font-size="11" fill="var(--text-dim)">easy volume (most)</text>
<text x="655" y="176" text-anchor="middle" font-size="11" fill="var(--text-dim)">hard (little)</text>
<text x="414" y="204" font-size="11" fill="var(--text)">1&#8211;2 qualities per block; three gives three</text>
<text x="414" y="220" font-size="11" fill="var(--text)">mediocre outcomes.</text>
<text x="414" y="244" font-size="11" fill="var(--text-dim)">Interference matters MORE near both ceilings.</text>
<text x="414" y="268" font-size="11" fill="var(--text-dim)">Monitor: sRPE, HRV trend, pace at fixed HR,</text>
<text x="414" y="284" font-size="11" fill="var(--text-dim)">and a repeated benchmark session.</text>
<text x="414" y="308" font-size="11" fill="var(--text)">Availability = planned sessions completed.</text>
</svg>'''
    return _wrap("dg-pc_highperf", "The elite problem: smaller gains, narrower window",
                 body,
                 "Near the ceiling the stimulus must be bigger and better aimed for a smaller return, so the coach protects the few sessions that actually produce it.")


def d_cm_reflection():
    body = _open(344, "The reflective coaching loop running from session to what, so-what and now-what, and back into the next session plan") + '''
<defs><marker id="cm_reflection-ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="var(--text-dim)"/></marker></defs>
<text x="20" y="24" font-size="12" fill="var(--text-dim)">Reflection-in-action &#8212; live, inside the session</text>
<rect x="20" y="34" width="470" height="50" rx="8" fill="var(--surface-2)" stroke="var(--theme-accent)" stroke-width="2"/>
<text x="255" y="56" text-anchor="middle" font-size="11.5" fill="var(--text)">THE SESSION</text>
<text x="255" y="74" text-anchor="middle" font-size="11" fill="var(--text-dim)">swap a cue, cap the sled load, cut an interval</text>
<line x1="510" y1="60" x2="530" y2="60" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#cm_reflection-ah)"/>
<text x="536" y="56" font-size="11" fill="var(--text-dim)">live</text>
<text x="536" y="72" font-size="11" fill="var(--text-dim)">adjustments</text>
<line x1="120" y1="86" x2="120" y2="112" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#cm_reflection-ah)"/>
<text x="20" y="110" font-size="12" fill="var(--text-dim)">Reflection-on-action &#8212; Rolfe, after it ends</text>
<rect x="20" y="120" width="200" height="44" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="120" y="147" text-anchor="middle" font-size="11.5" fill="var(--text)">What happened?</text>
<line x1="224" y1="142" x2="236" y2="142" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#cm_reflection-ah)"/>
<rect x="240" y="120" width="200" height="44" rx="8" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="340" y="147" text-anchor="middle" font-size="11.5" fill="var(--text)">So what does it mean?</text>
<line x1="444" y1="142" x2="456" y2="142" stroke="var(--text-dim)" stroke-width="1.5" marker-end="url(#cm_reflection-ah)"/>
<rect x="460" y="120" width="200" height="44" rx="8" fill="var(--surface-2)" stroke="var(--theme-accent)" stroke-width="2"/>
<text x="560" y="147" text-anchor="middle" font-size="11.5" fill="var(--text)">Now what will I do?</text>
<g class="dg-anim"><path d="M560 166 L560 192 L8 192 L8 59 L16 59" fill="none" stroke="var(--theme-accent)" stroke-width="2" stroke-dasharray="6 6" marker-end="url(#cm_reflection-ah)"><animate attributeName="stroke-dashoffset" values="24;0" dur="2.4s" repeatCount="indefinite"/></path></g>
<text x="300" y="186" text-anchor="middle" font-size="11" fill="var(--text)">a written now-what, carried into the next session plan</text>
<text x="20" y="214" font-size="12" fill="var(--text-dim)">Four inputs to the review</text>
<rect x="20" y="222" width="155" height="30" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="97" y="242" text-anchor="middle" font-size="11" fill="var(--text)">session logs</text>
<rect x="187" y="222" width="155" height="30" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="264" y="242" text-anchor="middle" font-size="11" fill="var(--text)">filmed station work</text>
<rect x="354" y="222" width="155" height="30" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="431" y="242" text-anchor="middle" font-size="11" fill="var(--text)">peer observation</text>
<rect x="521" y="222" width="155" height="30" rx="6" fill="var(--surface)" stroke="var(--border)"/>
<text x="598" y="242" text-anchor="middle" font-size="11" fill="var(--text)">athlete feedback</text>
<text x="20" y="282" font-size="11.5" fill="var(--text)">GROWTH</text>
<text x="20" y="300" font-size="11" fill="var(--text-dim)">praise process and strategy; not-yet language;</text>
<text x="20" y="316" font-size="11" fill="var(--text-dim)">a DNF or a bad split is information</text>
<text x="380" y="282" font-size="11.5" fill="var(--text)">FIXED</text>
<text x="380" y="300" font-size="11" fill="var(--text-dim)">praise talent &#8594; risk-averse, fragile</text>
<text x="380" y="316" font-size="11" fill="var(--text-dim)">correction is heard as criticism</text>
<text x="20" y="338" font-size="11" fill="var(--text-dimmer)">Big events (race, injury) &#8594; Gibbs: description, feelings, evaluation, analysis, conclusion, action plan</text>
</svg>'''
    return _wrap("dg-cm_reflection", "The reflective coach&#8217;s loop",
                 body,
                 "A reflection only changes practice when it ends in a written now-what that reaches the next session plan &#8212; and growth mindset is not toxic positivity.")


def d_xs_racecraft():
    body = _open(326, "The fixed station order with a demand fingerprint for each station, and the three budgets that add up to finish time") + '''
<text x="20" y="24" font-size="11.5" fill="var(--text-dim)">Fixed order: each run is followed by its station; wall balls end at the finish line</text>
<g class="dg-anim"><path d="M24 40 L36 40 L30 50 Z" fill="var(--theme-accent)"><animateTransform attributeName="transform" type="translate" values="0 0;624 0" dur="18s" repeatCount="1" fill="freeze"/></path></g>
<rect x="20" y="70" width="22" height="52" rx="4" fill="none" stroke="var(--border)"/>
<text x="31" y="100" text-anchor="middle" font-size="11" fill="var(--text-dim)">R1</text>
<text x="70.5" y="62" text-anchor="middle" font-size="11" fill="var(--text-dimmer)">1</text>
<rect x="44.5" y="70" width="52" height="52" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<rect x="44.5" y="70" width="52" height="5" fill="var(--theme-accent)"/>
<text x="70.5" y="102" text-anchor="middle" font-size="11" fill="var(--text)">SkiErg</text>
<rect x="99" y="70" width="22" height="52" rx="4" fill="none" stroke="var(--border)"/>
<text x="110" y="100" text-anchor="middle" font-size="11" fill="var(--text-dim)">R2</text>
<text x="149.5" y="62" text-anchor="middle" font-size="11" fill="var(--text-dimmer)">2</text>
<rect x="123.5" y="70" width="52" height="52" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<rect x="123.5" y="70" width="52" height="5" fill="var(--good)"/>
<text x="149.5" y="98" text-anchor="middle" font-size="11" fill="var(--text)">Sled</text>
<text x="149.5" y="114" text-anchor="middle" font-size="11" fill="var(--text)">Push</text>
<rect x="178" y="70" width="22" height="52" rx="4" fill="none" stroke="var(--border)"/>
<text x="189" y="100" text-anchor="middle" font-size="11" fill="var(--text-dim)">R3</text>
<text x="228.5" y="62" text-anchor="middle" font-size="11" fill="var(--text-dimmer)">3</text>
<rect x="202.5" y="70" width="52" height="52" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<rect x="202.5" y="70" width="52" height="5" fill="var(--good)"/>
<text x="228.5" y="98" text-anchor="middle" font-size="11" fill="var(--text)">Sled</text>
<text x="228.5" y="114" text-anchor="middle" font-size="11" fill="var(--text)">Pull</text>
<rect x="257" y="70" width="22" height="52" rx="4" fill="none" stroke="var(--border)"/>
<text x="268" y="100" text-anchor="middle" font-size="11" fill="var(--text-dim)">R4</text>
<text x="307.5" y="62" text-anchor="middle" font-size="11" fill="var(--text-dimmer)">4</text>
<rect x="281.5" y="70" width="52" height="52" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<rect x="281.5" y="70" width="52" height="5" fill="var(--warn)"/>
<text x="307.5" y="98" text-anchor="middle" font-size="11" fill="var(--text)">Burpee</text>
<text x="307.5" y="114" text-anchor="middle" font-size="11" fill="var(--text)">Broad J</text>
<rect x="336" y="70" width="22" height="52" rx="4" fill="none" stroke="var(--border)"/>
<text x="347" y="100" text-anchor="middle" font-size="11" fill="var(--text-dim)">R5</text>
<text x="386.5" y="62" text-anchor="middle" font-size="11" fill="var(--text-dimmer)">5</text>
<rect x="360.5" y="70" width="52" height="52" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<rect x="360.5" y="70" width="52" height="5" fill="var(--theme-accent)"/>
<text x="386.5" y="102" text-anchor="middle" font-size="11" fill="var(--text)">Row</text>
<rect x="415" y="70" width="22" height="52" rx="4" fill="none" stroke="var(--border)"/>
<text x="426" y="100" text-anchor="middle" font-size="11" fill="var(--text-dim)">R6</text>
<text x="465.5" y="62" text-anchor="middle" font-size="11" fill="var(--text-dimmer)">6</text>
<rect x="439.5" y="70" width="52" height="52" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<rect x="439.5" y="70" width="52" height="5" fill="var(--good)"/>
<text x="465.5" y="98" text-anchor="middle" font-size="11" fill="var(--text)">Farmers</text>
<text x="465.5" y="114" text-anchor="middle" font-size="11" fill="var(--text)">Carry</text>
<rect x="494" y="70" width="22" height="52" rx="4" fill="none" stroke="var(--border)"/>
<text x="505" y="100" text-anchor="middle" font-size="11" fill="var(--text-dim)">R7</text>
<text x="544.5" y="62" text-anchor="middle" font-size="11" fill="var(--text-dimmer)">7</text>
<rect x="518.5" y="70" width="52" height="52" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<rect x="518.5" y="70" width="52" height="5" fill="var(--good)"/>
<text x="544.5" y="98" text-anchor="middle" font-size="11" fill="var(--text)">Sandbag</text>
<text x="544.5" y="114" text-anchor="middle" font-size="11" fill="var(--text)">Lunges</text>
<rect x="573" y="70" width="22" height="52" rx="4" fill="none" stroke="var(--border)"/>
<text x="584" y="100" text-anchor="middle" font-size="11" fill="var(--text-dim)">R8</text>
<text x="623.5" y="62" text-anchor="middle" font-size="11" fill="var(--text-dimmer)">8</text>
<rect x="597.5" y="70" width="52" height="52" rx="5" fill="var(--surface-2)" stroke="var(--border)"/>
<rect x="597.5" y="70" width="52" height="5" fill="var(--warn)"/>
<text x="623.5" y="98" text-anchor="middle" font-size="11" fill="var(--text)">Wall</text>
<text x="623.5" y="114" text-anchor="middle" font-size="11" fill="var(--text)">Balls</text>
<rect x="654" y="70" width="40" height="52" rx="5" fill="var(--theme-accent)"/>
<text x="674" y="100" text-anchor="middle" font-size="11" fill="var(--bg)">FIN</text>
<rect x="20" y="140" width="16" height="10" fill="var(--theme-accent)"/>
<text x="42" y="149" font-size="11" fill="var(--text-dim)">engine &#8212; paceable, low failure risk</text>
<rect x="250" y="140" width="16" height="10" fill="var(--good)"/>
<text x="272" y="149" font-size="11" fill="var(--text-dim)">strength-endurance</text>
<rect x="390" y="140" width="16" height="10" fill="var(--warn)"/>
<text x="412" y="149" font-size="11" fill="var(--text-dim)">rep integrity &#8212; failure sets live here</text>
<text x="20" y="180" font-size="12" fill="var(--text-dim)">Race-model arithmetic</text>
<rect x="20" y="190" width="150" height="36" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="95" y="213" text-anchor="middle" font-size="11" fill="var(--text)">run budget</text>
<text x="182" y="214" text-anchor="middle" font-size="14" fill="var(--text-dim)">+</text>
<rect x="194" y="190" width="150" height="36" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="269" y="213" text-anchor="middle" font-size="11" fill="var(--text)">station budget</text>
<text x="356" y="214" text-anchor="middle" font-size="14" fill="var(--text-dim)">+</text>
<rect x="368" y="190" width="150" height="36" rx="6" fill="var(--surface-2)" stroke="var(--border)"/>
<text x="443" y="213" text-anchor="middle" font-size="11" fill="var(--text)">roxzone budget</text>
<text x="530" y="214" text-anchor="middle" font-size="14" fill="var(--text-dim)">=</text>
<rect x="542" y="190" width="138" height="36" rx="6" fill="var(--theme-accent)"/>
<text x="611" y="213" text-anchor="middle" font-size="11.5" fill="var(--bg)">TARGET TIME</text>
<text x="20" y="252" font-size="11" fill="var(--text)">Roxzone is the cheapest time on course: roughly 4&#8211;6 min well-drilled versus 8+ unpractised</text>
<text x="20" y="268" font-size="11" fill="var(--text-dim)">&#8212; it answers to rehearsal and logistics, not to added fitness.</text>
<text x="20" y="296" font-size="11" fill="var(--text-dim)">First-run discipline: even to slightly</text>
<text x="20" y="312" font-size="11" fill="var(--text-dim)">negative splits across the eight runs.</text>
<text x="370" y="296" font-size="11" fill="var(--text-dim)">Runner profile bleeds on sleds, lunges,</text>
<text x="370" y="312" font-size="11" fill="var(--text-dim)">carries; strength profile on the late runs.</text>
</svg>'''
    return _wrap("dg-xs_racecraft", "Race order, demand fingerprints and the three budgets",
                 body,
                 "Total time = run + station + roxzone; know each station&#8217;s fingerprint and buy the cheapest minutes first.")


DIAGRAMS = {
    "bm_techmodels": d_bm_techmodels,
    "hp_pacing": d_hp_pacing,
    "st_carry": d_st_carry,
    "mp_raceday": d_mp_raceday,
    "st_burpee": d_st_burpee,
    "mp_routines": d_mp_routines,
    "sk_motor_learning": d_sk_motor_learning,
    "nu_hydration": d_nu_hydration,
    "sm_injuries": d_sm_injuries,
    "mp_winners": d_mp_winners,
    "pc_highperf": d_pc_highperf,
    "cm_reflection": d_cm_reflection,
    "xs_racecraft": d_xs_racecraft,
}
