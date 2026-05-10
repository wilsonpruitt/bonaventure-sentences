# Next-session resume — Wave 9b Tier C

Drafted 2026-05-09 at end of the session that shipped Wave 9b Tier B.
HEAD is `8ca85a3`. Working tree should be clean. Paste the block below
into the next session.

---

Resume Bonaventure Vol I cleanup — Wave 9b Tier C planning. Last session
shipped Tier B (commit `8ca85a3`, 14 of 14 chunks dispositioned: 8
rebuilt, 6 overcount-accepted) plus a Tier C triage tool.

## Confirm starting state

1. `git log --oneline -3` → top should be:
   ```
   <commit> Tier C triage tool + resume docs       # most recent commit
   8ca85a3 Wave 9b Tier B: 14 of 14 chunks …
   714c257 Update next-session-resume.md for Wave 9b Tier B
   ```
2. `git status` → clean
3. `python3.11 tools/audit-paraphrase.py 2>&1 | tail -1` → `critical: 0
   high: 1` (pre-existing d11-divisio)
4. `grep -l "Phase C Tier 2 apparatus-incomplete" vol1/*.md` → 1 file:
   `vol1/bon-sent-I-d36-divisio.md` (deferred — not Tier C)
5. `df -h ~ | tail -1` → check free space

## Read FIRST (in this order)

1. `manual-review/wave9b-tier-c-resume.md` — Tier C scope is **154
   chunks**, not 37 as the prior estimate said. The triage estimator
   under-counts Lesson-10 noise. Sample-validate before mass-dispatch.
2. `manual-review/wave9b-tier-c-triage.md` — full triage table (auto-
   generated). Buckets A=2 / B=78 / C=74.
3. `manual-review/d1-d4-tier2-promotion-log.md` — Lessons 7–11. Tier B
   added new precedents at the bottom (d8-littera real undercoverage as
   a counterexample to the "littera is always overcount-only" assumed
   pattern; d7-a1-q2 body-paraphrase + Scholion fabrication as a
   second Lesson-11 case after d5-a1-q1).
4. `CLAUDE.md` lines 109–264 — Tier-2 verification workflow.

## Suggested next-session sequence

The Tier C triage hit-rate is unknown. The key first move is **NOT**
mass dispatch. Instead:

1. **Sample-validate 10 chunks** (5 from Bucket B, 5 from Bucket C).
   Pick mixed types: 2 littera + 2 quaestio + 1 divisio per bucket. For
   each, do a per-page eyes-on footer walk against raw OCR. Record:
   ground-truth count, overcount-only vs real-undercoverage,
   noise-estimator gap. This is ~1 hour of work.
2. **Tune the triage noise estimator** based on findings. Add missing
   contributors (numbered argument openers, Scholion-internal
   enumerations, two-stream apparatus on littera, OCR column-break
   garbles). Re-run triage. The fix should collapse B+C significantly.
3. **OR: build a per-page footer-band detector** if the simple noise
   subtraction can't reach reliable accuracy. Detect page-break markers
   in the OCR and count footers only within the bottom band of each
   printed page.
4. **Then dispatch waves** of 3 parallel agents on the smaller real-
   undercoverage subset (estimate: 20–40 chunks corpus-wide once the
   estimator is honest).

Per-chunk dispatch prompts: reuse the Tier B template (which validated
across 14 dispositions). Add Lesson-11 body-paraphrase guard to every
prompt as standard. Per-chunk wall-clock ~5–15 min depending on type.

## Mid-session refresh

If context starts compressing, re-read the Tier C resume doc rather than
re-deriving the plan.

## Outstanding initiatives (separate from Tier C)

- **`d36-divisio` frontmatter bounds** — multi-range coverage; audit
  raw=52 counts footers from intervening chunks. Tighten bounds or
  extend schema.
- **`d7-a1-q2` and `d5-a1-q1` body rebuilds** — both
  `apparatus-rebuilt-body-paraphrased`. Body itself paraphrased.
  Apparatus done; body rebuild is its own initiative.
- **Body-paraphrase corpus audit** (Lesson 11 follow-up) — tool
  comparing chunk Latin body length per printed-page against raw OCR
  per-page line counts; flag chunks where chunk body < ~70% of OCR.
- **d.41+ chunking** blocked by polish discipline.

## Triple-audit before commit (every Tier C wave)

```bash
cd ~/bonaventure-sentences
python3.11 tools/audit-paraphrase.py 2>&1 | tail -3
python3.11 tools/audit-headers.py 2>&1 | tail -10
python3.11 tools/audit-apparatus-count.py --min-d 1 --max-d 40 --min-diff 5 2>&1 | tail -30
```

Each Tier C wave should drop its dispositioned chunks out of the audit's
flag column (or out of the table if the noise estimator improvements
re-rank them below the threshold).

---

## Why these specific pointers

- **Sample-validate first** — Tier B's 6/14 OVERCOUNT-ACCEPT rate
  predicts Tier C will be even higher (smaller diffs = more noise-
  dominated). Mass dispatch wastes most of its work.
- **Re-read the triage resume** — context compression matters here;
  the scope is 4× larger than the Tier B doc said.
- **Add Lesson-11 guard to every prompt** — d7-a1-q2 was the second
  body-paraphrase case in 22 dispositions across Tiers A+B (~9% rate);
  high enough to expect Tier C will surface more.

## Files of interest

- `tools/triage-apparatus-count.py` — Tier C triage tool (this session)
- `manual-review/wave9b-tier-c-resume.md` — Tier C plan
- `manual-review/wave9b-tier-c-triage.md` — auto-generated triage table
- `manual-review/wave9b-tier-b-resume.md` — Tier B queue (now closed,
  preserved for reference)
- `manual-review/d1-d4-tier2-promotion-log.md` — Lessons 7–11 + Tier A/B
  full disposition history
