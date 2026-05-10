# Wave 9b Tier C — resume document

Created 2026-05-09 at the close of Wave 9b Tier B. **CAMPAIGN CLOSED
2026-05-10** — see "Pivot 2026-05-10" section at the top before reading
the rest of this file.

## Pivot 2026-05-10 — d.1-d.10 verify-each campaign abandoned, moved to d.31+ rechunk pipeline

### What happened

Wave A1 + A2 of the d.1-d.10 residual re-verification campaign ran 6
chunks total (after the d6-a1-q2 spot-check that opened the campaign).
Result: **0 ACCEPT / 2 REBUILD / 3 BODY-PARAPHRASED / 1 HALT.**

| Wave | Chunk | Banded | Disposition |
|---|---|---|---|
| Spot | d6-a1-q2 | +5 | REBUILD (7→21) |
| A1 | d7-a1-q4 | +15 | BODY-PARAPHRASED (obj 1 wholly paraphrased; 3 fabricated [^N]) |
| A1 | d8-p2-a1-q1 | +15 | REBUILD (7→23) |
| A1 | d5-a2-q1 | +13 | BODY-PARAPHRASED (Respondeo truncated; "Ad 1...Ad 4" replies fabricated) |
| A2 | d2-a1-q4 | +11 | HALT — body has 3 missing paragraphs, prior "body verified solid 2026-05-09" claim was wrong |
| A2 | d7-a1-q3 | +9 | BODY-PARAPHRASED (Replies 1-2 paraphrased) |
| A2 | d8-p2-dubia | +9 | REBUILD (6→21) |

**7 of 7 chunks needed work. Zero overcount-only.** Pattern is
structural, not edge-case: fabricated `[^N]` cross-refs, fabricated
"Ad 1...Ad 4" reply blocks, paraphrased objections, silently elided
body paragraphs, misplaced page markers, bad footer numerals, bad
`printed_pages` frontmatter (d7-a1-q4: 143-144 should be 142-143-144).

### Why we stopped

Each verification pass surfaced issues the prior pass didn't catch:

- d6 spot-check found apparatus rot.
- d6 rebuild surfaced page-marker rot, body-elision rot, footer-numeral rot.
- Wave A1 surfaced fabricated reply blocks.
- Wave A2 surfaced 3 missing body paragraphs in a chunk that was
  supposedly diff-checked against the PDF the day before.

The audit tools we built (banded detector, triage estimator) measure
narrower phenomena than the actual rot. Verification cost approached
rebuild cost AND verification was unreliable (d2-a1-q4 prior verification
was wrong). Each wave expanded scope rather than closing it.

User signal 2026-05-10: *"The churn of verification has sucked up twice
as much usage as the d.31+ method and it doesn't feel like we are closer
to resolution. Each wave flags new issues."*

### What replaces it

**d.1-d.10 moves into the d.31+ rechunk pipeline.** Same method that
shipped d.34-d.40 in one push 2026-05-07: re-chunk from raw OCR,
parallel translation waves, Tier-2 promote.

Concretely:

- **Keep as Tier-2 confirmed** (rebuilt 2026-05-10, real work):
  - `d6-a1-q2` (committed 2026-05-10, commit `c748e0d`)
  - `d8-p2-a1-q1` (Wave A1 rebuild — see commit alongside this doc)
  - `d8-p2-dubia` (Wave A2 rebuild — see commit alongside this doc)
- **Keep as Tier-2 confirmed** (zero-apparatus, audited clean
  2026-05-10): `d1-commentary`, `d10-commentary`, `d5-divisio`.
  These have honest `has_apparatus: false` frontmatter.
- **Keep flagged** (already demoted to `apparatus-incomplete +
  body-paraphrased`, deferred to body-paraphrase initiative):
  `d2-a1-q4`, `d4-a1-q4`, `d5-a1-q1`, `d5-a2-q1`, `d7-a1-q2`,
  `d7-a1-q3`, `d7-a1-q4`. These need body rebuild from raw OCR; in
  the new strategy the rebuild IS the rechunk.
- **Discard body + apparatus on the remaining ~76 chunks**, keep
  filenames + frontmatter scope. Replace body Latin / body English /
  apparatus from raw OCR using the d.31+ method.
- **Cohort flag stays in place** for the 76 unverified chunks until
  rechunk replaces them. No demotion tool needed.

### What NOT to do (anti-patterns from the campaign)

- ❌ Don't dispatch Wave A3-A5. The cohort is being rebuilt; verifying
  individual chunks before discarding their content is wasted work.
- ❌ Don't run the d.1-d.10 banded triage. Same reason.
- ❌ Don't trust prior "body verified" claims on d.1-d.10 chunks
  (d2-a1-q4 demonstrated the verification was unreliable).
- ❌ Don't try to repair chunks in place. The corruption is structural
  (LLM-fabricated content rather than transcription); repair surface
  area is worse than rebuild surface area.

### Files surviving the pivot

- `tools/audit-apparatus-count-banded.py` — useful for future Tier-2
  verification on chunks built via the d.31+ method. Keep.
- `tools/add-d1-d10-cohort-flag.py` — `--undo` mode strips flag from a
  single chunk; rechunk pipeline can call this as it promotes each
  chunk to fresh Tier-2.
- `manual-review/wave9b-tier-c-triage-banded.md` — keep as historical
  record of the heuristic's limits.
- `manual-review/d1-d4-tier2-promotion-log.md` — Lessons 7-11 still
  load-bearing for future Tier-2 work.
- `_backup-d8-p2-a1-q1-pre-rebuild-20260510/`,
  `_backup-d8-p2-dubia-pre-rebuild-20260510/` — pre-rebuild snapshots
  for diff reference.

### Outstanding outside-d.1-d.10 items (still real)

- `d36-divisio` frontmatter bounds bug (line range 20165-20520 spans
  non-contiguous content; chunk's actual scope ~80 lines). Tighten
  line bounds OR extend chunk schema for multi-range coverage. NOT
  d.1-d.10; outlives this pivot.
- d.41+ chunking still blocked by polish discipline
  (`feedback_bonaventure-guard-rail-discipline.md`).
- Body-paraphrase corpus audit tool (Lesson 11 follow-up) — chunk
  Latin body length per printed-page vs raw OCR per-page line counts;
  flag chunks < ~70%. Low priority now that d.1-d.10 is moving to
  rebuild rather than detection.

### Confirm starting state (next session)

```bash
cd /Users/wilsonpruitt/bonaventure-sentences
git log --oneline -3
# expect (after pivot commit):
#   <hash> Wave 9b campaign closed: pivot d.1-d.10 to d.31+ rechunk pipeline
#   4b5cbf8 d.1-d.10 Wave 9b residual campaign: pre-campaign cohort flag
#   c748e0d Rebuild d6-a1-q2 apparatus 7 -> 21 entries

git status  # clean

# Cohort flag still on the 76 unverified chunks:
grep -l "Wave 9b residual re-verification campaign" vol1/*.md | wc -l
# expect: ~76 (84 minus the chunks the campaign edited 2026-05-10)
```

### First move next session

Open the d.31+ rechunk playbook (start with d.34-d.40 commit history as
template — see memory `bonaventure-sentences.md`). Pick a wave size of
2-3 distinctions, parallel-translate, Tier-2 promote. Don't open this
file again unless something below the pivot section is needed for
historical context.

----

## (Historical record — Wave 9b Tier C dispatch + sample-validate. Above pivot supersedes.)

Created 2026-05-09 at the close of Wave 9b Tier B. **Updated 2026-05-10**
after sample-validate (10 chunks) + per-page footer-band detector built.
This is the queue for the next session.

## 2026-05-10 update — sample-validate + banded detector

### Sample-validate findings (10/10)

5 chunks from Bucket B + 5 from Bucket C, eyes-on PDF footer walks:

| Bucket | OVERCOUNT-ONLY | SMALL-UNDER | OTHER | LARGE-UNDER |
|---|---|---|---|---|
| B (5) | 3 | 1 | 1 | 0 |
| C (5) | 4 | 1 | 0 | 0 |
| **Total** | **7** | **2** | **1** | **0** |

Zero of 10 samples are real-LARGE-undercoverage. Sample agents
under-reported gap sizes (claimed 1-4 missing for what was actually
7-13 missing); future sample agents need explicit instruction to
verify ALL apparatus entries against raw OCR per page, not spot-check.

3 real-fix items dispositioned in commit `d49548e`:

- **`d35-divisio`** — pages corrected 600→599 / 190→189; missing
  [^5] (Cod. V *autem*) backfilled. Now 5 entries, Tier 2 complete.
- **`d4-a1-q4`** — fabricated [^7] removed; demoted to
  `apparatus-incomplete + body-paraphrased` (joins d5-a1-q1 / d7-a1-q2
  pattern). 7 of 13 ground-truth footers missing; body Sed-contra +
  Respondeo paraphrased; Scholion III missing.
- **`d2-a1-q4`** — body solid (PDF-supplement diff-checked
  2026-05-09), but ENTIRE p.57 footer band (11 entries) absent.
  Demoted to `apparatus-incomplete (body verified)`.

### Banded detector (`tools/audit-apparatus-count-banded.py`)

Built 2026-05-10. Page-section partition + footer-band scoping
eliminates two dominant noise sources from the original audit:
body-objection numerals outside the band, and intra-entry numerals
inside long multi-clause apparatus entries.

Validation against 10 sample chunks (ground-truth from sample-validate):
banded count is within ±3 of ground truth on 8/10. Two failures: chunks
that are FULLY shared (e.g. `d29-divisio` straddling distinction
boundary at p.507/508) — detector has no chunk-portion attribution.

**Re-bucketing impact (d.1–d.40, 350 chunks audited):**

| Banded diff | orig audit | banded audit |
|---|---|---|
| ≤ 0 | 127 | 218 |
| 1-2 | 45 | 46 |
| 3-5 | 54 | 37 |
| 6-10 | 69 | 33 |
| 11-19 | 44 | 14 |
| ≥ 20 | 11 | 2 |

Suspect count (banded > 5) = **49 chunks**. Filtering 4 skeletons
(chunk_app = 0: d27-p2-divisio, d5-divisio, d40-divisio + 1 more)
leaves **45 candidates** for eyes-on. Most are divisios/small
quaestios at distinction boundaries (shared-page noise persists).
Real-undercoverage candidates (large chunks with multi-page spans,
banded diff > 8): ~8-10 chunks including `d27-littera` (+21),
`d35-a1-q1` (+14, 6-page span), `d33-littera` (+14), `d28-littera`
(+14), `d37-p2-a1-q1` (+14), `d39-a1-q1` (+13), `d31-p2-a1-q1` (+11),
`d34-a1-q1` (+10). Full table at
`manual-review/wave9b-tier-c-triage-banded.md`.

### Real-undercoverage dispatch — done 2026-05-10

9 candidates dispatched in 3 waves of 3, with tightened "walk every
apparatus entry per page from raw OCR" prompts. Outcome:

| Wave | Chunks | Banded diff | Verdict |
|---|---|---|---|
| 1 | d27-littera (+21), d35-a1-q1 (+14), d33-littera (+14) | +49 | 3/3 ACCEPT |
| 2 | d28-littera (+14), d37-p2-a1-q1 (+14), d39-a1-q1 (+13) | +41 | 3/3 ACCEPT |
| 3 | d31-p2-a1-q1 (+11), d34-a1-q1 (+10), d8-p1-a2-q2 (+8) | +29 | 3/3 ACCEPT |

**9/9 OVERCOUNT-ACCEPT. Zero rebuilds. Zero body-paraphrase finds.**

Across the 9 chunks, banded inflation traced uniformly to:
- Italicized work citations inside multi-clause apparatus entries
  (e.g. *de Trinitate*, *Topic.*, *S. Thom. S. I. q. ...*)
- Lombard chapter rubrics inside littera entries (Cap. I, Cap. II...)
- Scholion lemma citations (Alex. Hal., Greg. Ariminens., Mastrius...)
- Em-dash-joined micro-notes correctly bundled in chunk's `[^N]:` defs
- Shared-page boundary contamination (d8-p1-a2-q2: p.158 fns 1-10
  belong to prior chunk)
- OCR-garbled superscript markers caught by the hardened regex

Status strings updated in 8 chunks; d8-p1-a2-q2 disposition logged in
this resume doc + commit message (no chunk edit needed — Tier-2
already documented per-page mapping).

### Tier C status

**Tier C closed for the +5 to +21 banded-diff suspect set.** Bucket
collapse summary:

| Stage | Suspect chunks |
|---|---|
| Pre-banded triage | 124 (orig diff > 5) |
| Post-banded triage | 49 (banded diff > 5) |
| Post-skeleton-filter | ~45 |
| Post-Wave-9b-Tier-C-dispatch (top 9) | 36 remaining at banded +5 to +10 |

The remaining 36 are mostly small divisios + quaestio openers at
distinction boundaries. Wave 9b Tier C precedent strongly suggests
these will batch-accept with a 3-4 chunk spot-check confirming the
shared-page-boundary pattern. Not blocking d.41+ chunking.

### Open follow-ups

1. **Body-paraphrase corpus audit** (Lesson 11) — separate initiative
   for d4-a1-q4 / d5-a1-q1 / d7-a1-q2 / d2-a1-q4 (apparatus side
   already deferred). Build a tool comparing chunk Latin body length
   per page against raw OCR per-page line counts; flag chunks
   < ~70%.
2. **Spot-check the residual 36** (banded +5 to +10) — pick 3-4 from
   different pdf_page geometries (single-page divisio, 2-page
   quaestio opener, 3-page mid-distinction quaestio) and confirm the
   shared-page-noise pattern. If confirmed, batch-accept; if any
   surprise, expand.
3. **d.41+ chunking** — UNBLOCKED for chunking work as of 2026-05-10.
   Re-chunking + Tier-2 promotion can resume.
4. **`d36-divisio` frontmatter bounds** — outstanding from earlier
   notes; line range 20165–20520 (355 lines) spans non-contiguous
   content; chunk's actual scope ~80 lines. Tighten line bounds OR
   extend chunk schema for multi-range coverage.

----

## Context — Tier B is closed

Tier B (14 chunks at audit diff +20 to +29) closed in commit `8ca85a3`.
Outcome: 8 REBUILD / 6 OVERCOUNT-ACCEPT.

Two new findings carry into Tier C planning:

1. **Lesson 11 surfaced again** on `d7-a1-q2` (body paraphrase + Scholion
   I/II partly fabricated). Status = `apparatus-rebuilt-body-paraphrased`.
   Body rebuild deferred to a corpus-wide initiative.
2. **Littera disposition is per-chunk, not uniform.** `d8-littera` was
   real undercoverage (14→32) — counterexample to `d37-littera` Tier A's
   metadata-only pattern. Don't assume.

## Tier C is BIGGER than the resume doc estimated

The Tier B resume doc said "37 chunks at +5 to +19." The actual count
(d.1–d.40, Tier-2-complete chunks only, audit diff in that range) is
**154 chunks** — a 4× scope error.

Triage script (`tools/triage-apparatus-count.py`) buckets by
adjusted-diff = audit_diff − Lesson-10 noise (chapter rubrics + Scholion
headers + italicized work-citations + lettered series):

  - **Bucket A (metadata-only candidate, adjusted ≤ 2):**  2 chunks
  - **Bucket B (small undercoverage, adjusted 3–8):**     78 chunks
  - **Bucket C (large undercoverage, adjusted > 8):**     74 chunks

Full table: `manual-review/wave9b-tier-c-triage.md`.

## CRITICAL: the triage noise estimator is under-counting

The two Wave 9b Tier A REBUILDs that ended up overcount-only —
`d27-p1-a1-q2` (raw=57 vs ground-truth=48) and `d35-a1-q1` (raw=49 vs
ground-truth=15) — both reappear in Tier C as Bucket B (`d27-p1-a1-q2`
adj=5; `d35-a1-q1` adj would also be Bucket-B-or-C if rerun). They are
already-resolved cases. Their post-rebuild diff is residual heuristic
noise, not real undercoverage.

This means a sizable share of Buckets B and C are likely
already-resolved overcount cases that the noise estimator doesn't catch.
**The triage is advisory; eyes-on per chunk is still required before
dispatch.** Specific known undercounts in the noise estimator:

  - Two-stream apparatus on littera (Lesson 9 reinforcement) — adds ~30
    per littera, only the chapter-rubric component is subtracted.
  - Numbered argument openers in body (`1. Auctoritate`, `2. Item`) —
    not subtracted at all; can be 5–15 per quaestio.
  - Scholion-internal numbered enumerations (`1.`, `2.`, `3.`) — not
    subtracted.
  - OCR-garbled column-break markers — match the regex but aren't
    footers.

A real fix would be to count footers ONLY within the printed-page footer
band (after a column break, before the next page header). That requires
finding page-break markers in the OCR. **Not done yet** — the existing
triage is the cheaper first pass.

## Suggested first move (next session)

**Don't dispatch 78 + 74 = 152 disposition agents.** That would burn
~25 hours of wall-clock and most of it would be re-doing overcount-only
metadata updates.

Instead:

1. **Sample-validate the triage on 10 chunks** (5 from B, 5 from C).
   Pick a mix of types: 2 littera, 2 quaestio, 1 divisio per bucket.
   Eyes-on per-page footer walk for each. Record:
   - actual ground-truth count
   - whether it's overcount-only or real undercoverage
   - what the noise estimator missed
2. **Decide based on hit rate:**
   - If ≥70% of Bucket B and ≥50% of Bucket C are already-resolved
     overcount-only: tune the noise estimator (add the missing
     contributors above) and re-bucket. The fixed estimator should
     collapse B+C dramatically.
   - If real undercoverage rates are high: build a per-page footer-band
     detector to count more accurately. Then re-bucket.
   - If both: do both, in that order.
3. **Only after re-bucketing** dispatch agents in waves of 3, like Tier B.
   The high-value targets will be a much smaller subset (estimate: 20–40
   real-undercoverage chunks corpus-wide).

## d.1-d.10 Wave 9b residual re-verification campaign (opened 2026-05-10)

### Why

The Wave 9b Tier C residual spot-check (4 of 36 chunks at banded +5 to
+10) found 1/4 = `d6-a1-q2` had real undercoverage: only 7 of 21
ground-truth apparatus entries. All 14 textual-variant notes
(`Vat. cum cod. cc...`, `iste pro ille`, etc.) were silently dropped
during initial Tier-2 promotion. Audits did NOT flag this — banded
under-counts variant openers, paraphrase audit doesn't smell variant
entries.

The d6 rebuild then surfaced 3 MORE issues that no audit caught:
- `<!-- page 128 -->` marker placed before Conclusio but the actual
  page break is mid-Respondeo
- Silently elided sentence in body (`Pater vult, se esse Deum...`)
- Old [^1] cited Hilary `de Synodis n.58`; raw OCR is `n.88, XXIV`

This is a pattern. The d.1-d.10 cohort was promoted before the
locked-in apparatus standard + audit guard rails. False-confidence
"Phase C Tier 2 complete" labels are unreliable.

Outcome of strategic decision (2026-05-10): bounded reset on d.1-d.10
**only**. d.11+ stays as-is (Tier B + Tier C dispatches confirm it
holds up).

### Scope

89 d.1-d.10 chunks total:
- 84 "Phase C Tier 2 complete" claims (cohort-flagged 2026-05-10)
- 4 already demoted to `apparatus-incomplete + body-paraphrased`
  (d2-a1-q4 / d4-a1-q4 / d5-a1-q1 / d7-a1-q2 — handled by separate
  body-paraphrase initiative)
- 1 skeleton (d3-p2-divisio)

3 zero-apparatus chunks (d1-commentary, d10-commentary, d5-divisio)
audited 2026-05-10 — all legitimately apparatus-free
(`has_apparatus: false` in frontmatter, honest status strings). NOT
mislabeled skeletons.

### Pre-campaign state (commit `4b5cbf8`, 2026-05-10)

84 chunks now carry `[d.1-d.10 Wave 9b residual re-verification
campaign 2026-05-10 — apparatus completeness pending]` appended to
`transcription_status`. Tool: `tools/add-d1-d10-cohort-flag.py`
(reversible via `--undo`). Site keeps serving the chunks unchanged.

### Wave A — 13 chunks at banded > +5 (queued)

Highest-risk cohort: most-likely undercoverage per d6 pattern.
Excluded 4 from raw 17-chunk list: d5-divisio (legit apparatus-free),
d6-a1-q2 (already rebuilt 2026-05-10), d4-a1-q4 + d5-a1-q1 (already
demoted to body-paraphrase backlog).

Dispatch order (highest banded first):

| Wave | Chunks |
|---|---|
| A1 | d7-a1-q4 (+15), d8-p2-a1-q1 (+15), d5-a2-q1 (+13) |
| A2 | d2-a1-q4 (+11) [already in backlog], d7-a1-q3 (+9), d8-p2-dubia (+9) |
| A3 | d5-a1-q2 (+8), d8-p1-a2-q2 (+8), d8-p1-dubia (+7) |
| A4 | d8-p2-a1-q4 (+7), d6-a1-q1 (+6), d8-p1-a2-q1 (+6) |
| A5 | d8-p2-divisio (+6) |

Note: d2-a1-q4 is already in body-paraphrase backlog; can either skip
in Wave A or roll its apparatus rebuild forward separately. Net: 12-13
chunks needing dispatch.

### Wave A agent prompt — lessons-encoded template

After d6's three-extra-issues finding, Wave A prompts MUST include
all of:

1. **Walk every entry per page from raw OCR** (per CLAUDE.md):
   render every numbered Quaracchi footer entry, page by page;
   ~10/page is normal. Cross-reference each ground-truth entry against
   chunk's `[^N]:` defs. PRESENT/MISSING/MIS-ANCHORED/FABRICATED.
   Include BOTH auctoritas-citations AND textual-variant notes.
2. **Verify page-break markers** (`<!-- page N -->`) against raw OCR.
   The d6 chunk had its `<!-- page 128 -->` marker placed before
   Conclusio but the real break was mid-Respondeo. Find the
   running-head transition in raw OCR and place the marker there.
3. **Body sanity check for silent elisions** — does chunk Latin body
   contain every sentence the raw OCR has in the chunk's line range?
   Spot-check by sampling 3-5 paragraphs from raw vs chunk body.
4. **Verify footer numerals against raw OCR** — d6's [^1] cited
   Hilary n.58 but raw OCR was n.88. Compare every Roman/Arabic numeral
   in chunk apparatus against raw.
5. **Body paraphrase check (Lesson 11)** — proportional length, no
   obvious paraphrase. Demote rather than rebuild if body paraphrased.

Disposition categories (4 outcomes, not 3):
- BODY-PARAPHRASED → demote to `apparatus-incomplete + body-paraphrased`,
  defer to body-paraphrase corpus initiative.
- BODY-OK + APPARATUS-INCOMPLETE → REBUILD apparatus (and any
  page-break / footer-citation fixes). Update status string.
- BODY-OK + APPARATUS-COMPLETE → OVERCOUNT-ACCEPT, strip cohort flag,
  document overcount source in status.
- SURPRISE → halt rebuild, report finding, ask for direction.

Critical: prompts MUST tell agent to update status string to remove
the cohort flag if disposition is OVERCOUNT-ACCEPT or REBUILD-COMPLETE.
Otherwise the chunk stays flagged as pending forever.

### Wave B — 20 medium-risk chunks (banded +1 to +5)

Run after Wave A pattern emerges. Strategy: spot-check 5 from
diverse types (1 littera, 1 dubia, 2 quaestio, 1 divisio); if all
clean, batch-strip cohort flag with explanation; if any fail,
expand to full Wave B dispatch.

### Wave C — 52 low-risk chunks (banded ≤ 0)

Banded under-counts; chunks claim more entries than heuristic finds.
Most likely clean. Spot-check 5 across types; batch-accept if clean,
else expand.

### Open questions for next session

- Roll d2-a1-q4 apparatus rebuild into Wave A2, or keep separate
  (it's in the body-paraphrase backlog already; body verified solid).
- After Wave A: if the rebuild rate is much higher than 50%, consider
  upgrading Wave B from spot-check-then-batch to full dispatch.
- The d36-divisio frontmatter bounds bug (line range 20165-20520
  spans non-contiguous content) is still open — outside d.1-d.10
  scope, but tracked in this resume doc.

### Files of interest for next session

- `tools/audit-apparatus-count-banded.py` — banded detector. Use
  `--chunk d{N}-...` per chunk for post-rebuild verification.
- `tools/add-d1-d10-cohort-flag.py` — `--undo` strips cohort flag
  from a single chunk if needed.
- `manual-review/wave9b-tier-c-triage-banded.md` — full d.1-d.40
  banded re-bucket table.
- `manual-review/d1-d4-tier2-promotion-log.md` — Lessons 7-11.
- `_backup-d6-pre-rebuild-20260510/` — d6-a1-q2 pre-rebuild backup
  for diff reference (showing what a "Phase C Tier 2 complete" chunk
  could look like before discovering it was 7-of-21).
- `CLAUDE.md` — Tier-2 verification workflow (canonical).

### Confirm starting state (next session)

```bash
cd /Users/wilsonpruitt/bonaventure-sentences
git log --oneline -5
# expect:
#   4b5cbf8 d.1-d.10 Wave 9b residual campaign: pre-campaign cohort flag
#   c748e0d Rebuild d6-a1-q2 apparatus 7 -> 21 entries
#   28f514c Wave 9b Tier C: 9 candidates dispositioned 9/9 OVERCOUNT-ACCEPT
#   c265d46 Wave 9b Tier C: per-page footer-band detector
#   d49548e Wave 9b Tier C sample-validate: 3 real-fix items dispositioned

git status  # clean

grep -l "Wave 9b residual re-verification campaign" vol1/*.md | wc -l
# expect: 84

python3.11 tools/audit-paraphrase.py 2>&1 | tail -1
# expect: critical: 0  high: 1
```

----

## Outstanding initiatives (not Tier C)

These were surfaced during Tier B and remain open:

- **`d36-divisio` frontmatter bounds** — line range 20165–20520 (355
  lines) spans non-contiguous content; chunk's actual scope is ~80
  lines. Audit raw=52 counts footer entries from intervening chunks.
  Tighten line bounds OR extend chunk schema for multi-range coverage.
- **`d7-a1-q2` and `d5-a1-q1` body rebuilds** — both have
  `apparatus-rebuilt-body-paraphrased` status. Body itself is paraphrased
  (3 omitted clusters in d5; 6+ in d7 + Scholion I/II fabrication).
  Apparatus done; body rebuild from raw OCR is its own initiative.
- **Body-paraphrase corpus audit** (Lesson 11 follow-up) — write a tool
  comparing chunk Latin body length per printed-page against raw OCR
  per-page line counts; flag chunks where chunk body is < ~70% of OCR.
  d5-a1-q1 + d7-a1-q2 are the template patterns. Once Tier C closes (or
  before, if scope dictates), run this audit.
- **d.41+ chunking** still blocked by polish discipline
  (`feedback_bonaventure-guard-rail-discipline.md`).

## Files of interest

- `tools/triage-apparatus-count.py` — the triage tool (new this session).
  Adjust the noise estimator if a sample-validate run shows under-count.
- `manual-review/wave9b-tier-c-triage.md` — full 154-row triage table.
- `manual-review/d1-d4-tier2-promotion-log.md` — Lessons 7–11.
- `tools/audit-apparatus-count.py` — the underlying audit (already
  hardened, see Lesson 9).

## Confirm starting state (next session)

```bash
git log --oneline -3              # top should be 8ca85a3 (Tier B close)
git status                         # clean
python3.11 tools/audit-paraphrase.py 2>&1 | tail -1
                                  # critical: 0  high: 1 (pre-existing d11-divisio)
grep -l "Phase C Tier 2 apparatus-incomplete" vol1/*.md
                                  # should be 1: just d36-divisio (deferred)
```
