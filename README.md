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

119 lessons. Days 1-51 walk the 13 official modules; days 52-53 add the two
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

Days 111-113 (authored later, from remaining course media) cover a periodisation-models
critique, metabolic pathways and skill in the high-performance athlete. An earlier
111-119 block of gap-close lessons was overwritten when those days were renumbered;
two of them — Module 6 supplements and the Module 4 5 Level System — have since been
restored at new day numbers.

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

Gap audit status (Aug 2026, revised): a block of gap-close lessons authored for days
111-119 was lost when those day slots were renumbered for new content. **Re-opened
gaps:** Module 7.3 test matrix and decision tree; Module 4's safety/efficacy/efficiency;
Module 3's how-to-utilise-testing-data; Module 8's double peaking; Module 7.1's
categorization of skills; Module 7.2's differences in running. Module 6 supplements and
the Module 4 5 Level System have been restored. Drafts of the rest are in the git
history at commits 1cea6c9, 9b35296 and 2487b12 if they are wanted back.

**Verified from source (Aug 2026).** Sections that were previously unverifiable have been
transcribed from audio David supplied, and the lessons rewritten from the actual course
material:

* Module 2 *Anti-Doping WADA* — day 101 now carries the race-day chaperone and continuity
  procedure from the Elite Athlete Briefing slides.
* Module 4 *5 Level System* — **the earlier version was wrong.** It reconstructed the system
  as a movement-competence ladder. It is a population/division ladder (novice, beginner,
  open, pro, elite) scored across four categories, with an athlete graded at their lowest
  category. Rewritten and restored.
* Module 4 *Interference Effect* and *Building Power* — days 42 and 37 now carry the
  practitioners' material, including a corrected session-separation figure (3-4 h plus a
  meal, against the 6 h convention previously recorded).

Still a reconstruction: Module 7.2's *Differences in Running*, one of the lessons lost from
the 111-119 block.

Numeric thresholds for the 5 Level System's four categories live in a separate *HYROX
Fitness Level Guidelines* page inside that section, which could not be extracted.

