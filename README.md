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

124 lessons. Days 1-51 walk the 13 official modules; days 52-53 add the two
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

Days 123-124 add Module 8 section 3, **Athlete Monitoring**, which had no coverage
anywhere on the site: the testing battery (5 km run, AMRAP 7 burpees + 1 km row, "Karen",
sled push to failure, rep-max squat endurance, NIRS 5-1-5, the WOD-Science functional ramp
test with IMU power analysis, the compromised running fatigue test) and both example test
weeks; then the profiling logic that turns those results into a periodization model —
strength-biased vs endurance-biased novices, the delivery-limited vs utilisation-limited
distinction and its opposite interval prescriptions, the spider diagram with goal-based
versus elite-based scaling, and the note that HYROX-specific normative values do not yet
exist so coaches must build their own.

Gap audit status (Aug 2026, closed): **all identified course-section gaps are authored.**
The seven lessons lost when days 111-113 were renumbered over the 111-119 block have been
restored from git history at days 116-122, byte-identical to the reviewed originals.

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
* Module 5 *Muscle Physiology*, *Thermoregulation & Hydration* and *Exercise Adaptations* —
  days 64, 68, 69 and 71 now carry the source material. Day 64 was audited against the
  section and found correct; it gains the HYROX strength-curve mapping and a note that the
  course itself uses the loose 'isometric is maximum force' phrasing, which describes the
  shortening branch only.

Still a reconstruction: Module 7.2's *Differences in Running* (day 122), restored with its
unverified flag intact.

Numeric thresholds for the 5 Level System's four categories live in a separate *HYROX
Fitness Level Guidelines* page inside that section, which could not be extracted.

