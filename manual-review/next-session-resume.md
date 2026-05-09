# Next-session resume — Wave 9b Tier B

Drafted 2026-05-09 at end of the session that shipped Wave 5 + Wave 9b
Tier A. Paste the block below into the next session.

---

Resume Bonaventure Vol I cleanup — Wave 9b Tier B. Last session shipped
3 commits closing Wave 5 + Wave 9b Tier A. HEAD is `1473c68`. Working
tree should be clean.

## Confirm starting state

1. `git log --oneline -5` → top should be:
   ```
   1473c68 Wave 9b Tier A: 8 of 9 chunks dispositioned …
   98feb05 Wave 9b: status-string downgrade on 23 chunks …
   6fa6b43 Task 9 wave 5: d3-p1-dubia / d3-p2-a1-q3 / d3-p2-dubia apparatus rebuilt …
   ```
2. `python3.11 tools/audit-paraphrase.py 2>&1 | tail -1` → `critical: 0  high: 1`
   (the 1 high is `d11-divisio`, pre-existing, not your problem)
3. `python3.11 tools/audit-formatting.py 2>&1 | grep -c "missing required keys"` → 0
4. `grep -l "Phase C Tier 2 apparatus-incomplete" vol1/*.md | wc -l` → 14
   (the 14 Tier B chunks; status string still says `apparatus-incomplete —`
   from commit `98feb05`)
5. `df -h ~ | tail -1` → check free space

## Read FIRST (in this order)

1. `manual-review/wave9b-tier-b-resume.md` — the Tier B queue with line
   bounds, raw-counts, and per-chunk expected entry counts. The 14-chunk
   table is your work list.
2. `manual-review/d1-d4-tier2-promotion-log.md` Lessons 7–11 — full
   disposition history. **Lessons 10 and 11 are critical for Tier B**:
   - Lesson 10: apparatus heuristic OVERCOUNTS on Scholion-heavy chunks
     and *littera* chunks (two-stream apparatus + Lombard chapter
     rubrics). Don't pad apparatus to chase the audit number; eyes-on
     the printed-page footer.
   - Lesson 11: body undercoverage is a separate failure mode from
     apparatus undercoverage. Apparatus rebuild prompts MUST include a
     body-paraphrase guard step.
3. `CLAUDE.md` lines 109–264 — Tier-2 verification workflow has Lesson
   9 baked into item 5. Skim if cold.
4. `manual-review/d1-d11-pdf-supplement-resolution-log.md` lessons 1–6 —
   older but ambient discipline.

## Tier B scope (14 chunks)

All currently carry `transcription_status: "Phase C Tier 2 apparatus-incomplete — …"`
(downgraded in commit `98feb05`). Each chunk's apparatus needs eyes-on
disposition: **rebuild** OR **overcount-accept**.

Eight are *littera* / d.8 family chunks: `d8-littera`, `d27-littera`,
`d28-littera`, `d31-littera`, `d32-littera`, `d33-littera`, `d8-p1-a1-q1`,
`d8-p1-a1-q2`, `d8-p1-a2-q2` was already done in Tier A so skip — wait
that was Wave 9b Tier A. Tier B's d.8 family: `d8-littera`,
`d8-p1-a1-q1`, `d8-p1-a1-q2`, `d8-p2-a1-q2`. Per Lesson 9-reinforcement,
*littera* chunks at audit diff +20 to +35 are likely OVERCOUNT-only
(two-stream apparatus + chapter rubrics). Wave 9b Tier A's `d37-littera`
was a metadata-only disposition (32 → 32). Expect a similar pattern on
most Tier B littera chunks — but **verify each, don't assume**.

Six are quaestio chunks: `d39-a1-q1`, `d37-p2-a1-q1`, `d7-a1-q2`,
`d8-p1-a1-q2`, `d8-p2-a1-q2`, `d38-a1-q1`, `d38-a2-q1`. These are more
likely real undercoverage.

## Suggested wave dispatch (5 rounds × 3 parallel)

The 6-agent hard cap (`feedback_acta-usage.md`) gives headroom; 3
parallel keeps the 8GB Mac comfortable. Group by complexity, validate
prompt on small quaestiones first.

**Wave 1 (small quaestiones; validate prompt):**
- `d8-p1-a1-q1` (raw=31, chunk=10, +21)
- `d38-a1-q1` (raw=31, chunk=11, +20)
- `d38-a2-q1` (raw=30, chunk=10, +20)

**Wave 2 (mid quaestiones):**
- `d8-p1-a1-q2` (raw=34, chunk=11, +23)
- `d8-p2-a1-q2` (raw=31, chunk=8, +23)
- `d7-a1-q2` (raw=31, chunk=7, +24)

**Wave 3 (larger quaestiones + first littera):**
- `d39-a1-q1` (raw=40, chunk=13, +27)
- `d37-p2-a1-q1` (raw=38, chunk=13, +25)
- `d8-littera` (raw=42, chunk=14, +28) — first littera; expect
  overcount-only

**Wave 4 (littera batch 1):**
- `d27-littera` (raw=40, chunk=17, +23)
- `d28-littera` (raw=36, chunk=15, +21)
- `d32-littera` (raw=36, chunk=15, +21)

**Wave 5 (littera batch 2):**
- `d31-littera` (raw=43, chunk=21, +22)
- `d33-littera` (raw=41, chunk=19, +22)

(14 total; wave 5 has 2 chunks. Adjust grouping if findings change pace.)

## Per-agent prompt template

Reuse the Wave 9b Tier A template — last session's transcript has the
text for `d27-p1-a1-q2` and `d37-littera` agents which both worked
cleanly. Key elements every prompt needs:

1. **Permission test FIRST** — write 4-byte test file in
   `manual-review/_perm_test_<chunk-id>.md`; `rm` on success; STOP if
   denied. (Project-scope `.claude/settings.json` was added in commit
   `6fa6b43` — should already work.)
2. **Anti-self-throttle** — push to ground-truth count from the printed
   page footer; do NOT use heuristic raw-count as stopping target.
3. **Required reading list** — CLAUDE.md 109–264, d1-d4-tier2-promotion-log
   Lessons 7–11, the chunk file itself.
4. **Heuristic-skepticism block** — quote both Lesson 9 (UNDERCOUNT bias
   from OCR garbles) and Lesson 10 (OVERCOUNT bias from Scholion / numbered
   argument openers / lettered series) explicitly. For littera chunks,
   add: "Lombard chapter rubrics + two-stream apparatus convention typically
   inflate the audit by ~30 entries; expect overcount-only metadata
   disposition unless body anchors lack matching defs."
5. **Body-paraphrase guard** (Lesson 11) — spot-check chunk Latin against
   printed Quaracchi for omitted clusters BEFORE placing apparatus
   markers. If body-paraphrase clusters found:
   - Place apparatus entries you can faithfully anchor.
   - Document missing-body-content clusters in
     `manual-review/tier2-ambiguities-<chunk-id>.md` with raw line
     ranges.
   - Status string variant: `Phase C Tier 2 apparatus-rebuilt-body-paraphrased —`
     (NOT `complete —`).
6. **Per-page recipe** — Quaracchi restarts numbering each printed page;
   render every numbered footer entry; mirror anchors in Latin and
   English bodies at OCR-confirmed superscript positions.
7. **Format** — `[^N]: **La.** <Latin>\n    **En.** <English>` (4-space
   indent on **En.**; period after **La**); codex sigla verbatim;
   scripture in Vulgate numbering Latin-side; `[?]` for ambiguous + log
   to `manual-review/tier2-ambiguities-<chunk-id>.md`.
8. **Status string update** on success: replace `apparatus-incomplete —`
   prefix with `complete —` (or `apparatus-rebuilt-body-paraphrased —`
   variant) plus full disposition narrative including per-page
   distribution and any [?] flags.
9. **Audits per chunk** — paraphrase + formatting + apparatus-count
   filtered to the chunk's distinctio.
10. **Report back** — entry count before/after, per-page distribution,
    body-guard result, anchor counts L/E, `[?]` count + log location,
    audit deltas, judgment calls.

## Don't re-trigger known traps

- **Don't quote the heuristic raw-count to the agent as a target.**
  Lesson 9 / Wave-5 trap: agents WILL match the number and stop, even
  when their own walk sees more. Quote *only* "expected ~10 entries per
  printed page" and the page count.
- **Don't assume body is sound.** Lesson 11 / d5-a1-q1 trap: Wave 9b
  Tier B chunks have the same parent-Tier-1 lineage as d5-a1-q1; some
  may have body paraphrase too.
- **Don't pad apparatus to satisfy the heuristic when ground-truth is
  lower.** Lesson 10 / d35-a1-q1 + d37-littera trap. Especially on
  *littera* chunks (two-stream apparatus convention inflates by ~30) and
  Scholion-heavy chunks (italicized work-citations match the regex).
- **Don't commit autonomously.** Pattern from this session: each Tier
  closes with one commit summarizing dispositions across all chunks
  in that tier. Triple-audit first.

## After Tier B closes

**Tier C** (37 chunks at audit diff +5 to +19) — see
`manual-review/wave9b-tier-b-resume.md` "After Tier B" section. Many
are likely heuristic noise (Lesson 10 case); eyes-on triage first to
avoid 37 unnecessary rebuilds.

**Outstanding initiatives (separate from Tier B/C):**

- **`d36-divisio` deferred** — frontmatter line_start/line_end
  (20165–20520, 355 lines) span non-contiguous content; chunk's actual
  scope is ~80 lines (status string says "20165–20231 + 20507–20520").
  Need either (a) tighten line bounds to the actual contiguous range
  with a separate chunk for the back-half, or (b) extend chunk schema
  to support multi-range coverage and update the audit to slice across
  segments.
- **d5-a1-q1 body rebuild** — apparatus done (24 entries) but body
  itself is paraphrased (3 omitted clusters). Logged in
  `manual-review/tier2-ambiguities-d5-a1-q1.md`.
- **Body-paraphrase corpus audit** (Lesson 11 follow-up) — write a tool
  that compares chunk Latin body length per printed-page against raw OCR
  per-page line counts; flag chunks where chunk body is < ~70% of OCR
  body length, suggesting paragraph drops. d5-a1-q1's pattern is the
  template.
- **d.41+ chunking still blocked** by polish discipline
  (`feedback_bonaventure-guard-rail-discipline.md`).

## Session pace estimate

- 3 parallel agents per wave; ~10–15 min wall-clock per wave foreground.
- 5 waves × 15 min = ~75 min of agent dispatch.
- Plus ~30 min for status-string fixups, log updates, audits, commits.
- **One full session for Tier B is realistic** if waves go cleanly.
- Two sessions if Lesson-11 body-paraphrase findings surface mid-wave
  (each one pauses dispatch for triage and a status-string variant).

## Triple-audit before commit

```bash
cd ~/bonaventure-sentences
python3.11 tools/audit-paraphrase.py 2>&1 | tail -3
python3.11 tools/audit-headers.py 2>&1 | tail -10
python3.11 tools/audit-apparatus-count.py --min-d 1 --max-d 40 --min-diff 20 2>&1 | tail -30
```

All Tier B chunks should drop out of the apparatus-incomplete list at
session close. Any remaining +20 to +35 flags should be either (a)
overcount-accepted with explicit ambiguities-log disposition, or (b)
deferred to Tier C with a recorded reason.

## Mid-session refresh

If context starts compressing, re-read this file rather than re-deriving
the plan from scratch.

---

## Why these specific pointers

- **Audit baselines** — confirm nothing regressed between sessions; the
  14 apparatus-incomplete chunks are *expected*.
- **Lessons 10 + 11 first** — they're new this session and apply
  directly. Older lessons are ambient discipline.
- **Wave-1 small validation** — last session's Wave 5 first pass missed
  the per-page-restart conventions until I caught it pre-commit; small
  validation now means catching prompt drift early.
- **`d8-littera` placed in wave 3** — it's the first littera dispatched;
  its disposition (likely overcount-only per Lesson 9 reinforcement)
  sets the pattern for waves 4–5.
- **"Don't commit autonomously"** — every tier in Wave 9b has surfaced
  a new finding that warranted user input. Trust the pattern.

## Files of interest

- `manual-review/wave9b-tier-b-resume.md` — full Tier B queue
- `manual-review/d1-d4-tier2-promotion-log.md` — disposition history +
  Lessons 7–11
- `tools/audit-apparatus-count.py` — hardened heuristic (Lesson 9
  comment block at top)
- `tools/wave9b-status-downgrade.py` — idempotent status-string
  downgrader (run once last session; usable as template if more chunks
  surface from Tier C eyes-on)
- `vol1/_backup-*/` — historical pre-rebuild snapshots; none from
  Wave-9b waves (rebuilds were direct)
