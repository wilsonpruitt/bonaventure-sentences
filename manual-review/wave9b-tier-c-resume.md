# Wave 9b Tier C — resume document

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
