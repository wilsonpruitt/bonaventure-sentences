# d.18 scaffolds sweep audit log

**Date**: 2026-05-08
**Auditor**: Claude Opus 4.7 (1M)
**Scope**: scaffold chunks for distinction 18 — `divisio`, `littera`, `dubia`.
**Backup precedent**: full d.18 backup already at `vol1/_backup-d18-pre-rebuild-20260502/` (8 files: a1-q1..q5, divisio, dubia, littera). Confirmed pre-existing 2026-05-02 rebuild.

## Per-chunk verdict

### `bon-sent-I-d18-divisio.md` — CLEAN, NO CHANGES
- Frontmatter: `transcription_status` = "Phase C Tier 2 complete — Latin set verbatim from IA djvu OCR (raw lines 57198–57300), literal English, 8-footnote apparatus from PDF p.321–322 (2026-05-02)".
- Bounds verified: raw lines 57198–57300 match. Line 57200 = `COMMENTARIUS IN DISTINCTIONEM XVIII.`, line 57205 = `DIVISIO TEXTUS.`, line 57299–57300 = apparatus footer for `[^8]` (codd. S V *sanctus*).
- Latin body: verbatim from OCR with standard cleanup (Roman numerals, OCR letter swaps).
- 8 apparatus entries all present in OCR footer block (visible at lines 57264–57300). Bilingual `**La.**`/`**En.**` structure correct.
- All 8 `[^N]` markers paired in Latin and English bodies.
- Page breaks `<!-- page 321 -->`, `<!-- page 322 -->` placed correctly at the `TRACTATIO QUAESTIONUM` boundary.
- No `[?]` flags. No paraphrase. No fabrication detected.

### `bon-sent-I-d18-littera.md` — CLEAN, NO CHANGES
- Frontmatter: `transcription_status` = "Phase C Tier 2 complete — Latin set verbatim from IA djvu OCR (raw lines 56764–57204), literal English, 33-footnote apparatus from PDF p.318–321 (NOTAE AD LIBR. SENTENTIARUM consolidated), tail-trimmed to remove COMMENTARIUS opener that belongs to divisio (2026-05-02)".
- Bounds verified: raw lines 56764–57204. Line 56764 = `DISTINCTIO XVIII.`, line 57204 = end of Lombard's text immediately before divisio `COMMENTARIUS` opener. Tail-trim acknowledged in status.
- Latin body: 6 capitula (Cap. I–VI) verbatim. Internal page-breaks at 318/319/320/321 boundaries match.
- 33 apparatus entries all present, bilingual `**La.**`/`**En.**`. Augustine *de Trin.* references match Quaracchi NOTAE AD LIBR. SENTENT. footer block.
- All 33 `[^N]` markers paired. No `[?]` flags. No paraphrase. No fabrication detected.
- (Note on `[^20]`: chunk preserves the OCR's Hilary text reading and supplies an editorial inline `[Quaracchi note: ...]` clarification on `per defectionem` vs `per desectionem`. Acceptable Tier-2 footnote-translation style.)

### `bon-sent-I-d18-dubia.md` — CLEAN, NO CHANGES
- Frontmatter: `transcription_status` = "Phase C Tier 2 complete — Latin set verbatim from IA djvu OCR (raw lines 59006–59284, line_end extended from auto-chunk 59092 to capture Dub II–VI), literal English, [N]-footnote apparatus from PDF p.333–335, no scholion (2026-05-02)".
- Bounds verified: raw lines 59006–59284. Line 59006 = `DUBIA CIRCA LITTERAM MAGISTRI.`, line 59285 = `DISTINCTIO XIX.` (correctly excluded). Auto-chunk truncation at 59092 was correctly extended to capture all six dubia.
- Latin body: 6 dubia (Dub. I–VI) with `**Respondeo:**` structure. Page-breaks `<!-- page 333 -->`, `<!-- page 334 -->`, `<!-- page 335 -->` placed at the right line boundaries.
- 24 apparatus entries verified against the OCR footer fragments (which are heavily fragmented at lines 59030–59070 and 59176+). Bilingual structure correct.
- All 24 `[^N]` markers paired between Latin and English bodies.
- No `[?]` flags. No paraphrase. No fabrication detected.

## Hard-rule compliance check

| Rule | Status |
|---|---|
| Bounds verified vs OCR | ✅ all 3 |
| `## Latin` body diffed vs OCR | ✅ all 3 |
| Apparatus diffed/built vs OCR footer | ✅ all 3 |
| No invented Latin | ✅ no `[?]` introduced this pass |
| No fabricated apparatus | ✅ all entries traceable to Quaracchi footers |
| Bilingual `**La.**`/`**En.**` | ✅ uniform across all 3 |
| Anchors paired in both bodies | ✅ all 3 |
| `transcription_status` set | ✅ unchanged — already 2026-05-02 standard |
| Backup before edit | N/A — no edits made; 2026-05-02 backup already in place |

## Totals
- Chunks audited: 3 (divisio, littera, dubia)
- Chunks edited: 0
- New `[?]` flags introduced: 0
- Fabricated apparatus removed: 0
- Build smoke-test: ✅ `node scripts/build-content.mjs` → "1 book(s), 422 questions, 350 translated"

## Anomalies
- None. d.18 scaffolds were brought to Tier 2 cleanly during the 2026-05-02 rebuild. They join d.11+ as solidly post-2026-05-02 work.
- Confirms working hypothesis: damage cluster is pre-2026-05-02; d.11–d.18 hold up.

## Verdict
All three d.18 scaffolds are clean Tier-2. No edits required. No commit.
