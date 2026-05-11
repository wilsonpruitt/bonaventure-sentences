# Next session — d.1-d.10 polish (PDF eyes-on)

Created 2026-05-10 at the close of the 16-wave d.1-d.10 rechunk pipeline.
All 79 cohort chunks force-rebuilt from raw OCR. Deployed to
https://bonaventure.wrootpress.com same day.

## Status at handoff

- 0 cohort flags remaining (verify: `grep -l "Wave 9b residual" vol1/*.md | wc -l` → 0)
- Last commit: `437b6f5` (Wave 16 FINAL)
- Build: 414 chunks / 350 translated
- d.1 through d.40 are now all Tier-2

## What's left — three buckets

### Bucket 1 — PDF eyes-on resolution for ~250 [?] flags + 9 OCR-band dropouts

The 16-wave rebuild surfaced ambiguities the agents could not resolve
from IA djvu OCR alone. These need 600dpi PDF reads.

**OCR-band dropouts (entire footer block missing from IA djvu OCR
for that page)** — high priority:

| Chunk | Page | Status |
|---|---|---|
| d1-a3-q2 | p.42 | 3 [?] body markers, no footer |
| d2-a1-q2 | p.54 | Agent already recovered 7 entries from PDF in Wave 4 |
| d3-littera | p.66 | 3 [?] body markers, no footer |
| d3-p2-a1-q2 | p.84 | Agent already recovered 3 entries from PDF in Wave 14 |
| d5-a2-q2 | p.118 | 6 [?] body markers, no footer |
| d6-a1-q3 | p.130 | 7 [?] body markers, no footer |
| d7-divisio | p.134 | ~10 unanchored footer entries |
| d8-p2-a1-q4 | p.174 | OCR p.174 footer block elided; marker `⁵` preserved with [?] |
| d10-littera | p.193 | 11 [?] on p.193 tail (heavy scan damage) |

**Process** for each:
1. Extract at 600dpi: `python3.11 tools/extract-pages.py --volume vol1 --pages N --dpi 600`
2. Read the footer band visually and reconcile with the chunk's apparatus
3. Either fill the `[?]` flags in apparatus or replace them with the real
   footer entries (matching body marker positions)

**Remaining ~250 [?] flags** are mostly small (single-word OCR garbles,
ambiguous codex sigla, truncated lemmas). Spot-check by chunk via the
per-chunk ambiguities logs at `manual-review/tier2-ambiguities-d{N}-*.md`.

### Bucket 2 — Convention cleanups (low priority)

Renumbering / consolidation cleanups noted during rebuild:

- **sub-key markers** to remove (replace with sequential integer keys):
  - `d4-dubia` — uses `[^1b]`, `[^p106-N]`, `[^p107-N]` (33 entries total)
  - `d4-a1-q2` — uses `[^4b]`, `[^6b]`
- **entry-merging to expand** (the strict convention is 1:1 with raw OCR
  footer notes, not consolidated by shared body anchor):
  - `d6-littera` — 11 entries consolidated from 19 raw footer notes
  - `d3-divisio` — main-footer + NOTAE merged by shared anchor
- **marker reposition**:
  - `d7-littera` — `[^17]`/`[^18]`/`[^19]` positions appear scrambled
    (apparatus content suggests [^17] → *scilicet*, [^18] → *qua possit
    esse Filius*, [^19] → *esse* within that phrase). Currently [^17]
    sits where [^18]/[^19] belong.

Parser tolerates all these — chunks render and parse cleanly. These
are correctness/consistency cleanups, not blockers.

### Bucket 3 — Body-paraphrase backlog (separate initiative)

7 chunks already demoted to `apparatus-incomplete + body-paraphrased`
during the verify-each campaign before the pivot. Their body Latin is
paraphrased, not verbatim from OCR — needs full body rebuild:

- d2-a1-q4, d4-a1-q4, d5-a1-q1, d5-a2-q1, d7-a1-q2, d7-a1-q3, d7-a1-q4

These weren't part of the rechunk pipeline cohort (already flagged
differently). Process: same per-chunk recipe from CLAUDE.md, but the
trigger is body length < ~70% of raw OCR per-page line counts. Build
the audit tool (Lesson 11 followup) before starting, or just rebuild
all 7 directly.

## How to start the next session

1. Read this file. Pick a bucket.
2. **For PDF eyes-on (Bucket 1)**: tackle 1-2 OCR-band dropouts per
   session. They are small surface area but require visual PDF reading.
3. **For convention cleanups (Bucket 2)**: 1-session bulk job. Could
   be dispatched as a single agent per chunk.
4. **For body-paraphrase (Bucket 3)**: 7 chunks via parallel agents,
   same cadence as the rechunk pipeline. Estimate 1-2 waves.

## What NOT to do

- ❌ Don't re-verify or re-rebuild the 79 cohort chunks unless something
  specific surfaces a regression. The pipeline closed clean.
- ❌ Don't trust IA djvu OCR for the pages in Bucket 1's dropout list.
  PDF is authoritative for those specific pages.
- ❌ Don't expand entry-merging or sub-keys further in new chunks. The
  convention is sequential integer keys, one entry per raw OCR footer
  note.

## d.41+ is unblocked

After polish completes (or in parallel), d.41+ chunking + Tier-2
promotion can resume. d.40 closed the polish cadence; the next polish-
blocker is d.50.

## Confirm starting state next session

```bash
cd /Users/wilsonpruitt/bonaventure-sentences
git log --oneline -5
# expect:
#   437b6f5 d.1-d.10 rechunk pipeline Wave 16 (FINAL): d.8 pars II + d.8 p1-dubia
#   a9fdaf4 d.1-d.10 rechunk pipeline Wave 15: d.8 pars I + littera
#   38437a5 d.1-d.10 rechunk pipeline Wave 14: d.3 pars II finish
#   0477181 d.1-d.10 rechunk pipeline Wave 13: d.3 pars I + p2-a1-q1
#   a111dbb d.1-d.10 rechunk pipeline Wave 12: d.1 finish + d.3 scaffolds

git status  # clean

grep -l "Wave 9b residual re-verification campaign" vol1/*.md | wc -l
# expect: 0

python3.11 tools/audit-paraphrase.py 2>&1 | tail -1
# expect: critical: 0  high: 1 (pre-existing d11-divisio)
```
