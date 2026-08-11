# HYROX Level 2 — "Mastering Performance" study site

A spaced-repetition study site covering the 13 modules of the HYROX Academy
Level 2 *Mastering Performance* certification.

**Live:** https://dsingson5.github.io/hyrox-l2-study/

- One lesson per day, FSRS-scheduled review, self-graded retrieval questions.
- `modules.html` lists every lesson — all unlocked, work at any pace.
- Regenerate: `python generate_daily.py` (or `--day N` for a specific day).
- A GitHub Action rebuilds the day's page at 00:05 Manila; past day 61 the
  generator rotates Deep Review through the training-relevant lessons.

### Curriculum

110 lessons. Days 1-51 walk the 13 official modules; days 52-53 add the two
Module 1 topics the original pass missed (reflective practice / growth mindset,
holistic athlete development); days 54-59 are cross-module exam-synthesis days;
days 60-61 are mock assessments; days 62-75 deepen Modules 4, 5, 7.1 and 7.2.
Days 76-101 close the gaps found by auditing the site against the official
course section list: Module 10's six athlete populations (76-81), Module 9's
expanded mental-performance sections (82-87), Module 7.2's running-biomechanics
sections (88-93), Module 6's remaining nutrition sections (94-97) and Module 2's
remaining sports-medicine sections (98-101).

Days 102-110 are the real Module 7.4: an introduction to the module's three
expert lenses (biomechanics / physiotherapy / strength & conditioning) followed
by a deep dive on each of the eight stations, including the burpee broad jump,
which previously had no dedicated lesson anywhere on the site.

**Correction, Aug 2026:** days 37-39 (`pe_strength`, `pe_screening`,
`pe_load_mgmt`) were originally filed under Module 7.4 on the assumption that
7.4 was a strength-and-prehab module. It is not — it is the per-station deep
dive. Those three lessons are good content and have been re-filed under
Modules 4 and 2 respectively; their `topic_id`s are unchanged so existing FSRS
review state is preserved.

Domains: `CM` coaching & individualisation · `SM` sports medicine & injury ·
`BM` biomechanics & technique · `PH` physiology & nutrition ·
`PG` performance pillars & programming. Question interleaving is weighted by
each domain's share of the curriculum (kept in sync between
`generate_daily.py` and `app.js`).

### Content note
These are **original study notes** written from the module list and from
established sport-science knowledge. They are not a reproduction of HYROX
Academy course material. Assessment-format details are inferred from public
sources about the same platform's other courses and are flagged as unverified
in the lessons that mention them.

Known remaining gaps (audited Aug 2026, not yet authored): Module 7.3 Test Matrix
and Decision Tree; Module 4's 5 Level System and Safety / Efficacy / Efficiency;
Module 3's How to Utilise Testing Data; Module 8's Double Peaking specifics;
Module 7.1 Categorization of Skills; Module 6 Supplements (partially covered by
day 26); Module 7.2 Differences in Running.

