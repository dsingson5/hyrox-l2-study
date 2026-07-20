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

61 lessons: days 1–51 walk the 13 official modules; days 52–53 add the two
Module 1 topics the original pass missed (reflective practice / growth mindset,
holistic athlete development); days 54–59 are cross-module exam-synthesis days;
days 60–61 are mock assessments (a full athlete case study, then hard scenarios
plus exam-day strategy).

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
