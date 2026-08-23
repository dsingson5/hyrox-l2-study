# -*- coding: utf-8 -*-
"""Rebuild modules.html — the browse-all index — from curriculum.json.

modules.html used to be hand-edited, so every batch of new lessons got appended
as its own heading at the end. That left Module 5 appearing seven times and the
index ordered by authoring date rather than by course structure. This script
regenerates it from scratch instead:

  * one heading per module, in official course order (1 -> 10, then the
    non-module exam-prep groups),
  * lessons ordered WITHIN each module by day number, which is the order their
    sections were authored and therefore the course-section order,
  * no dates and no day numbers on the rows — just the section position inside
    its module. The dated filename stays in the href because that is the actual
    page path.

Run after any change to data/curriculum.json:  python build_modules.py
"""
import json
import datetime as dt
from html import escape
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
SITE_VERSION = "v3.3"

# Official course order. Anything in curriculum.json whose chapter is not
# listed here is appended afterwards in first-appearance order, so a new
# chapter can never be silently dropped from the index.
MODULE_ORDER = [
    "Module 1", "Module 2", "Module 3", "Module 4", "Module 5", "Module 6",
    "Module 7.1", "Module 7.2", "Module 7.3", "Module 7.4",
    "Module 8", "Module 9", "Module 10",
    "Exam synthesis", "Mock assessment",
]

SUBTITLE = {
    "Module 1":   "The Coaching Mindset",
    "Module 2":   "Sports Medicine: Optimizing Health, Recovery &amp; Performance",
    "Module 3":   "Biomechanics",
    "Module 4":   "HYROX Performance Pillars",
    "Module 5":   "Exercise Physiology",
    "Module 6":   "Nutrition",
    "Module 7.1": "Embedding Skills in Athletes for HYROX Performance",
    "Module 7.2": "Running Biomechanics and Technique for HYROX Performance",
    "Module 7.3": "Off-Feet Conditioning",
    "Module 7.4": "Performance Enhancement and Injury &mdash; station deep dives",
    "Module 8":   "Mastering Periodization in HYROX",
    "Module 9":   "Mental Performance",
    "Module 10":  "Personalized Performance Coaching",
    "Exam synthesis":  "High-yield cross-module review",
    "Mock assessment": "Certification dry runs",
}

HEAD = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>HYROX L2 — all modules</title><style>
:root{--bg:#0b0e14;--surface:#121722;--border:#232b3a;--text:#e6ebf5;--dim:#9ba3b4;--accent:#5ec8ff}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:15px/1.55 -apple-system,Segoe UI,Roboto,sans-serif;padding:28px 18px 70px}
.wrap{max-width:820px;margin:0 auto}h1{font-size:22px;margin:0 0 6px}
.sub{color:var(--dim);font-size:13px;margin-bottom:22px}
.mod{font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:var(--accent);margin:26px 0 10px;font-weight:700}
.mod span{display:block;text-transform:none;letter-spacing:0;color:var(--dim);font-size:13px;font-weight:500;margin-top:3px}
.mod em{font-style:normal;color:var(--dim);font-weight:500;letter-spacing:0;text-transform:none;font-size:11px;float:right;padding-top:2px}
.lrow{display:flex;align-items:center;gap:12px;padding:11px 14px;background:var(--surface);border:1px solid var(--border);border-radius:10px;margin-bottom:7px;text-decoration:none;color:var(--text)}
.lrow:hover{border-color:var(--accent)}
.ld{font-size:11px;color:var(--dim);min-width:26px;text-align:right;font-variant-numeric:tabular-nums}
.lt{flex:1;font-weight:600;font-size:14px}
.lq{font-size:11px;color:var(--dim)}
a.back{display:inline-block;margin-bottom:16px;color:var(--accent);text-decoration:none;font-size:13px}
</style></head><body><div class="wrap">
<a class="back" href="index.html">&larr; Today's lesson</a>
<h1>Level 2 &mdash; Mastering Performance</h1>
"""


def main():
    cur = json.loads((ROOT / "data" / "curriculum.json").read_text(encoding="utf-8"))
    qs = json.loads((ROOT / "data" / "questions.json").read_text(encoding="utf-8"))
    lessons = cur["lessons"]
    start = dt.date.fromisoformat(cur["meta"]["start_date"])

    # group by chapter, preserving day order inside each
    groups = {}
    for n in sorted(lessons, key=int):
        groups.setdefault(lessons[n]["chapter"], []).append(int(n))

    ordered = [c for c in MODULE_ORDER if c in groups]
    extra = [c for c in groups if c not in MODULE_ORDER]
    if extra:
        print("NOTE: chapters not in MODULE_ORDER, appended at end:", extra)
    ordered += extra

    body = []
    total = 0
    for chapter in ordered:
        days = groups[chapter]
        sub = SUBTITLE.get(chapter, "")
        body.append(
            f'<h2 class="mod">{escape(chapter)}'
            f'<em>{len(days)} lesson{"s" if len(days) != 1 else ""}</em>'
            f'<span>{sub}</span></h2>'
        )
        for i, day in enumerate(days, 1):
            l = lessons[str(day)]
            iso = (start + dt.timedelta(days=day - 1)).isoformat()
            nq = len(qs.get(l["topic_id"], []))
            body.append(
                f'<a class="lrow" href="daily/hyrox_{iso}.html">'
                f'<span class="ld">{i}</span>'
                f'<span class="lt">{escape(l["title"])}</span>'
                f'<span class="lq">{nq} Q</span></a>'
            )
            total += 1

    stamp = dt.datetime.now(ZoneInfo("Asia/Manila")).strftime("%b %d, %Y %H:%M")
    head = HEAD + (
        f'<div id="build-stamp" style="font-size:10px;color:var(--dim);opacity:.75;'
        f'margin:-2px 0 4px">site {SITE_VERSION} &middot; updated {stamp} Manila</div>\n'
        f'<div class="sub">All {total} lessons, ordered by module and by section within each '
        f'module &mdash; first module first, last module last. Every lesson is unlocked '
        f'&mdash; work at whatever pace you want.</div>\n'
    )

    out = head + "<!-- exam-prep:start -->" + "".join(body) + \
        "<!-- exam-prep:end -->\n</div></body></html>\n"
    (ROOT / "modules.html").write_text(out, encoding="utf-8")

    print(f"modules.html rebuilt: {total} lessons in {len(ordered)} groups")
    for chapter in ordered:
        print(f"   {chapter:18s} {len(groups[chapter]):3d}")


if __name__ == "__main__":
    main()
