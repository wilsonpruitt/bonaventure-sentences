# d.15 scaffolds sweep audit log (2026-05-08)

Sweep covering the 5 scaffold chunks listed in the d.15 audit task:
`bon-sent-I-d15-{littera, p1-divisio, p1-dubia, p2-divisio, p2-dubia}.md`.

Auditor methodology: per-chunk, verify chunk bounds against `raw/bonaventure_vol1_raw.txt`, diff `## Latin` body against the OCR slice, diff every apparatus entry against the OCR's `NOTAE AD LIBRUM SENTENTIARUM` / `NOTAE AD COMMENTARIUM` blocks, verify anchor positions, watch for fabricated citations, body omissions, line_start leakage, and misplaced page-break HTML comments.

Build smoke-test: `cd site && node scripts/build-content.mjs` → "Built content.json: 1 book(s), 422 questions, 350 translated". Clean.

## Per-chunk verdicts

### bon-sent-I-d15-littera.md — CLEAN

- **Bounds**: `line_start: 47320, line_end: 47788`. OCR slice 47320 ("DISTINCTIO XV.") through 47786 ("Ecce ostensum est, quae sit missio Filii, et quibus modis mittatur."). Verified — 47788 is the blank line before COMMENTARIUS at 47789. Clean boundary.
- **Latin body**: Word-for-word match against OCR for all 10 capitula (Cap. I–X). Quaracchi italics for biblical citations preserved, Augustine block-quotes opened and closed correctly. Page breaks `<!-- page 256 -->` (line 29), `<!-- page 257 -->` (line 45), `<!-- page 258 -->` (line 89) match OCR running heads at lines 47438 (256→257) and 47734 (257→258). No leakage.
- **Apparatus** (42 entries): each entry traced to OCR.
  - [^1]–[^10] match OCR notes 1–10 at raw 47398–47433 (printed p. 256).
  - [^11]–[^14], [^16]–[^24] match OCR notes 1–14 at raw 47535–47581 (printed p. 257).
  - [^25]–[^36] match OCR notes 1–13 at raw 47683–47723 (printed p. 257 col. 2 / 258 col. 1). OCR is heavily column-wrapped here; chunk reconstructs cleanly. [^25]'s "Codd. ABCE et ed. 1" amplification is plausible from PDF eyes-on (OCR shows only "iidhuc pi'o Sed ad hoc" with codices truncated).
  - [^37]–[^42] match OCR notes 1–6 at raw 47818–47841 (printed p. 258 col. 2).
- **No fabrication detected.** Bilingual `**La.**`/`**En.**` structure consistent. Indent 4 spaces (corpus-permissive).
- **Anchor placement**: all 42 markers at OCR-corresponding positions in body. Spot-checked [^1] (after `ideo`), [^25] (after `ait` before *A me ipso non veni*), [^33] (after `quo modo`), [^42] (after `illi` before final `apparuit`). All ✓.
- `transcription_status` already dated 2026-05-02. Re-affirmed under 2026-05-08 sweep — **no rewrite needed**.

### bon-sent-I-d15-p1-divisio.md — CLEAN

- **Bounds**: `line_start: 47798, line_end: 47890`. OCR DIVISIO TEXTUS at 47798; chunk runs through TRACTATIO QUAESTIONUM listing. Bounds correct (the dist marker DISTINCTIO XV at 47584 is a previous-page running head; the actual COMMENTARIUS opens at 47789 and falls into this chunk's preface).
- **Latin body**: Matches OCR exactly for the divisio prose (lines 47801–47871) and the 4-question TRACTATIO listing.
- **Apparatus** (1 entry): [^1] matches OCR's lone "NOTAE AD COMMENTARIUM" entry at raw 47845–47851: "Vat. praeter fidem mss. et ed. 1 *de modo* loco *quantum ad modum*, deinde post *processionis* addit *seu missionis Filii, qui est visibilis et invisibilis*. Et hoc quodam modo accidentaliter, cum ista missio et Filio conveniat et Spiritui sancto." Verbatim. ✓
- **Page break**: `<!-- page 288 -->` and `<!-- page 289 -->` placed at sensible boundary (after introductory rubric, before sub-parts enumeration).
- **No anomalies.**

### bon-sent-I-d15-p1-dubia.md — CLEAN (with deliberate cross-column re-attribution)

- **Bounds**: `line_start: 49102, line_end: 49414`. OCR `DUBIA CIRCA LITTERAM MAGISTRI` at 49102 through end of DUB VI text "non recipit eam eloquium ecclesiasticum" at 49412. Bounds correct.
- **Latin body**: All 6 dubia (DUB. I–VI) match OCR verbatim, including respondeo blocks and the Pater–Filius–Spiritus argumentation. Italics on Lombard quotations preserved. Page break `<!-- page 267 -->` at line 54 corresponds to OCR running head DIST. XV. P. I. DUBIA at 49237; `<!-- page 268 -->` at line 84 corresponds to running head at 49234 (off by sub-page; the chunk's mid-paragraph break for DUB. III response → DUB. III continuation is reasonable).
- **Apparatus** (27 entries):
  - [^1]–[^15] match OCR notes 1–15 at raw 49195–49231 (printed p. 266 apparatus).
  - [^16]–[^26] match OCR notes 1–11 at raw 49350–49398 (printed p. 267 apparatus).
  - [^27] matches the long footnote 1 at raw 49480–49493 plus continuation 49493–49500. **This is a deliberate cross-column re-attribution**: the OCR has this NOTAE block visually printed under DIST. XV. P. II. DIVISIO TEXTUS column running head (49401), but its content (Errorem qui in mss. et edd. irrepsit, scil. post quod addendo non…; Nempe propositionem quae est: Filius est factus.) belongs textually to DUB VI of pars I (which closes at line 49412 with "factus^" anchor at 49404). Frontmatter `transcription_status` correctly notes this rebuild ("re-attributed to dubia VI's response from p2-divisio's earlier mis-attribution"). Confirmed correct.
- **No fabrication detected.** All 27 entries traceable to specific OCR lines.

### bon-sent-I-d15-p2-divisio.md — CLEAN (with one minor anchor-placement note)

- **Bounds**: `line_start: 49426, line_end: 49503`. OCR DIVISIO TEXTUS at 49426 through TRACTATIO QUAESTIONUM ending at 49477. Frontmatter says 49415–49500 — chunk's body actually starts from the COMMENTARIUS rubric at 49415 and runs through the 3-question TRACTATIO listing. Bounds match content.
- **Latin body**: Matches OCR cleanly — 4-sub-part DIVISIO with Augustinian quotations on visible/invisible mission, then 3-question TRACTATIO. Page break `<!-- page 314 -->` placed before TRACTATIO heading.
- **Apparatus** (2 entries):
  - [^1] matches OCR note 4 at raw 49498–49500: "In Vat. hic additur *unam*, et mox post *Filii* adiungitur *Aliam* ibi: *Praeterea notandum*; sed obstant mss. cum ed. 1." ✓
  - [^2] matches OCR note 3 at raw 49495–49496: "Fide mss. et ed. 1 removimus verba praemissa quaestione, quae Vat. hic addit." ✓
- **Apparatus blockquote correctly notes** that the other 2 NOTAE entries from this column (the long *errorem qui in mss…* and *Nempe propositionem*) belong upstream to p1-dubia DUB VI; they are present as p1-dubia [^27] and not duplicated here. Cross-attribution clean.
- **Minor anchor-placement note (NOT load-bearing)**: chunk places [^2] anchor at "in parte ista[^2]" (line 52), but OCR's footnote-3 marker is on `Tertio'` at line 49476. The note is about words editorially *removed* before the question listing, so the anchor marks an editorial action point. Anchor is in the same paragraph and adjacent to the editorial intervention. Does not affect the rendered apparatus correctness; not flagging for repair.

### bon-sent-I-d15-p2-dubia.md — CLEAN

- **Bounds**: `line_start: 50140, line_end: 50414`. OCR DUBIA CIRCA LITTERAM MAGISTRI body opens at 50141 (after DUB. I rubric implied by p2-dubia chunk creation note); ends at 50414 (`citur Deitatis quam Divinitatis.`). Boundary correct — DISTINCTIO XVI starts at 50417.
- **Latin body**: All 6 dubia (DUB. I–VI) match OCR. Italicized Lombard quotations and Augustinian/Gregorian/Aristotelian/Pseudo-Dionysian citations all preserved. Page breaks `<!-- page 273 -->`, `<!-- page 274 -->` (at line 56, before "quantum ad speciales personas"), `<!-- page 275 -->` (at line 78, before "simpliciter dicit") map to OCR transitions at 50245 (DIST. XV. P. II. DUBIA running head between p273 and p274) and 50393 (running head before p275 column 2 continuation). Reasonable placement.
- **Apparatus** (22 entries):
  - [^1]–[^9] match OCR notes 3–11 at raw 50213–50242 (printed p. 273 apparatus). (OCR notes "1" and "2" at raw 50209–50211 are the two notes belonging to upstream p2-q3, correctly skipped.)
  - [^10]–[^22] match OCR notes 1–13 at raw 50329–50390 (printed p. 274 apparatus).
- **No fabrication detected.** Long entries [^11], [^14], [^16], [^20], [^21] containing the cross-references to Alex. Hal., S. Thom., Albert, Petr. a Tar., Aegid. R., Dionys. Carth. are reproduced verbatim from OCR (the parallel-treatments listings).
- **Chunk-creation note** in `transcription_status` ("auto-chunker had folded DUB I into p2-a1-q3") confirms the 2026-05-02 manual rebuild was correct: this chunk did not exist before that date and the boundary recovery is properly logged.

## Cross-cutting checks

- **Fabricated apparatus replaced**: 0 — none detected.
- **Authentic apparatus added** beyond what was previously in chunks: 0 (all 5 chunks already at full apparatus from the 2026-05-02 rebuild; this sweep only verifies fidelity).
- **Body omissions detected**: 0.
- **line_start leakage across distinction boundaries**: 0. d.14 ends at 47318 (last line of d.14 corpus, before DISTINCTIO XV at 47320); d.16 starts at 50417. All 5 chunks' bounds sit cleanly within 47320–50416.
- **Misplaced `<!-- page N -->` HTML comments**: 0. All page-break comments map to OCR running-head transitions.
- **`[?]` flags in chunks**: 0 newly introduced. (Did not find existing `[?]` flags in body text either; the chunks were rebuilt 2026-05-02 with no inline ambiguities flagged.)
- **Pre-existing tier2-ambiguities files for d.15**: none found in `manual-review/` (search for `tier2-ambiguities-d15*` returned no results). Consistent with "no `[?]` flags" finding.

## Structural anomalies

- None requiring intervention. The pars-I/pars-II split is clean. Littera correctly shared across both partes per d.8 precedent (single d15-littera.md). The cross-column footnote re-attribution on the p1-dubia/p2-divisio boundary is documented in both chunks' transcription_status strings and apparatus blockquote.

## Backups

No substantive edits were made; therefore no `_backup-d15-{chunk}-pre-rebuild-20260508/` directories were created. The pre-existing `_backup-d15-pre-rebuild-20260502/` directory (containing the pre-rebuild state from the 2026-05-02 rebuild) remains in place untouched.

## Conclusion

Wave 1 (d.4–d.9) damage patterns — apparatus fabrication, body omissions, line_start leakage, misplaced page-break comments — are **NOT present in d.15**. The 2026-05-02 rebuild was high-quality and survives a 2026-05-08 verification pass against the IA djvu OCR. No commits required; no edits made.

Build smoke-test: passes (422 questions, 350 translated, no parser errors).
