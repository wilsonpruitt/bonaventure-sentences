# d.31 scaffolds sweep audit log — 2026-05-08

Scope: `vol1/bon-sent-I-d31-{littera, p1-divisio, p1-dubia, p2-divisio, p2-dubia}.md` (the multi-pars scaffolds; the question chunks `p1-a1-q{1-3}` and `p2-a{1-2}-q{1-3}` are out of scope for this sweep).

Goal: verify chunk bounds, diff Latin against pt2 raw OCR, diff/build apparatus, never invent Latin or fabricate apparatus.

Source: `raw/bonaventure_vol1_pt2_raw.txt`. Pt2 PDF offset = printed − 410.

Context: d.31 was polished 2026-05-07 ([?]-flag pass for d.31–d.40, logged in `manual-review/d31-d40-polish-resolution-log.md`) but not body-diffed against raw OCR. This sweep closes the gap.

## Per-chunk verdicts

### bon-sent-I-d31-littera.md — PASS (no changes)

- **Bounds**: frontmatter `line_start: 11190, line_end: 11540`.
  - `DISTINCTIO XXXI.` at OCR line 11190 — chunk head correct.
  - `DISTINCTIO XXXI. P. U.` running head at line 11391 = page-break running head between pp. 529 and 530, mid-littera.
  - Body terminates before `COMMENTARIUS IN DISTINCTIONEM XXXI.` (Bonaventure commentary) at line 11541 = next chunk's start.
  - Bounds correctly capture Lombard's full d.31 littera spanning Pars I caps I–IV plus Pars II caps V–VI with the internal Pars II heading at the page-break.
- **Latin body**: verbatim against OCR after standard de-interleave + silent OCR fixes. Lombard's text matches OCR through Cap. VI. Augustine *de Trin.* citations (Cap. I [^2][^3], Cap. II [^7], Cap. IV [^15][^21]) and Hilary *de Synodis* notulae (Cap. II [^8], Cap. III [^14], Cap. IV [^20]) pull cleanly from the appropriate raw lines.
- **Apparatus**: 21 entries. Spot-checked against OCR footer bands:
  - p. 529 footer (raw 11240–11268): [^1]–[^5] match verbatim. [^4] (`Auctoritate omnium codd. et ed. 1 (5 in margine) posuimus propter naturae unitatem indisparitas pro naturalis unitas et identitas...`) matches OCR exactly. [^5] (`Haec definitio sumta est ex Hilario (de Synodis n. 73)... Quidam dicunt, quod haec nomina aequalis, similis tantum remotive accipiuntur...`) verbatim match.
  - p. 530 footer: [^6]–[^10] confirmed (Hilarius *Prop. I. n. 13*, etc.).
  - p. 531 footer: [^11]–[^14] confirmed.
  - p. 532 deferred footer-of-p.532 entries: [^15]–[^21] confirmed via raw OCR line 12042–12044 (`1. Cor. 13, 12. Vulgata...`, `Cap. 5. n. 5, nonnullis omissis vel additis`, etc.).
- **[^19] honest declaration**: chunk explicitly flags `[^19]` as "OCR-noise marker preserved here for chunk-numbering consistency". Verified: raw OCR line 11457 places the marker `'` on the **second** `qui` in `qui ' dicunt, Patrem fuisse passum` (= [^18] *quia* variant), not on the first `qui est Filius` (where [^19] sits in the chunk body). The chunk's transparent disclosure matches the actual OCR/PDF state. NO fabrication.
- **English**: literal, paragraph-for-paragraph parallel to Latin. Scholastic formulae preserved. Quotation-mark conversion `«…»` → `"…"`.
- **transcription_status**: dated 2026-05-06, descriptive, accurate. No update needed.
- **Verdict**: clean. No edits.

### bon-sent-I-d31-p1-divisio.md — PASS (no changes)

- **Bounds**: frontmatter `line_start: 11541, line_end: 11594`.
  - `COMMENTARIUS IN DISTINCTIONEM XXXI.` at line 11541 (immediately after littera ends).
  - `DIVISIO TEXTUS.` at line 11554.
  - `TRACTATIO QUAESTIONUM.` at line 11583.
  - `ARTICULUS UNICUS` at line 11595 = next chunk (p1-a1-q1) start.
  - Bounds clean.
- **Latin body**: verbatim against OCR. The COMMENTARIUS opener, Pars I subheading + signification subhead, Lombard incipit (`Praeterea considerari oportet...`), full DIVISIO TEXTUS paragraph, and TRACTATIO listing of three questions all match OCR.
- **Apparatus**: `has_apparatus: false`. Chunk body has zero `[^N]` markers. Apparatus section honestly declares: "[No apparatus in this divisio. The three numbered footnotes printed at the foot of p. 532 belong to the d.31 littera (continuations of the Hilarius notulae from the preceding pages) and are extracted with that chunk.]" Verified by inspecting OCR — the p.532 footer notes are correctly captured in the d.31-littera chunk's [^15]–[^21], not duplicated here.
- **English**: literal, parallel to Latin, including the bracketed Lombard incipit citation in italics.
- **transcription_status**: dated 2026-05-06, accurate.
- **Verdict**: clean. No edits.

### bon-sent-I-d31-p1-dubia.md — PASS (no changes)

- **Bounds**: frontmatter `line_start: 12053, line_end: 12092`.
  - `DUBIA CIRCA LITTERAM MAGISTRL` (OCR garble for MAGISTRI) at line 12053.
  - DUB I at line 12056 (col-A); DUB II at line 12072 (col-A); DUB III at line 12070 (col-B — two-column OCR interleave puts DUB III before DUB II in linear OCR).
  - Body for DUB III ends ~line 12089 (`quae supra ostensae sunt`).
  - `COMMENTARIUS IN DISTINCTIONEM XXXI.` Pars II opener at line 12093 = next chunk start.
- **Latin body**: 3 dubia (DUB I–III) verbatim from OCR after de-interleave. Body markers `nona '` (DUB I, on `decima, nona`) at OCR 12060 and `sibi ^ similis` (DUB II) at OCR 12074 are honestly stripped (the OCR carries them, but no parseable apparatus footer for p. 540 is captured in the OCR sweep). Marginal gloss `Differentia triplex` and `Aiii` (mis-OCR for `Alii`) stripped per Quaracchi-marginalia convention.
- **Apparatus**: `has_apparatus: false`. Chunk Apparatus block honestly declares no extractable footer band for p. 540's d.31-portion of the dubia, and explicitly notes that the lone OCR-visible footer note `1 Cap. 1. seqq. — Mo,\ pio est cod. T` on p. 540 (raw line 12125) belongs to the Pars II Commentarius/Divisio block that begins immediately after this dubia chunk — not to this chunk. Verified: line 12125 is inside p2-divisio bounds (12093–12162), and the note IS captured as p2-divisio's [^1]. NO duplication, NO fabrication.
- **Notes block**: documents (1) the body-marker on `differt a se Deo` corresponds to printed fn 7 (`Cod. W adiicit Deo`), tracked in the d.31–d.40 polish-resolution log; (2) marginal-gloss strip-out provenance.
- **English**: literal, parallel to Latin. Scholastic formulae preserved.
- **transcription_status**: dated 2026-05-06, accurate.
- **Verdict**: clean. No edits.

### bon-sent-I-d31-p2-divisio.md — PASS (no changes)

- **Bounds**: frontmatter `line_start: 12093, line_end: 12162`.
  - `COMMENTARIUS IN DISTINCTIONEM XXXI.` (Pars II opener) at line 12093.
  - `Pars II.` subheading; Lombard incipit `Non est hic praetermittendum, quod vir illustris Hilarius`.
  - `DIVISIO TEXTUS.` at line 12108; spans across page-break to p. 541.
  - `TRACTATIO QUAESTIONUM.` at line 12149; lists 2 articles + 3 sub-questions for art. 1.
  - `ARTICULUS I.` at line 12163 = next chunk (p2-a1-q1) start.
- **Latin body**: verbatim against OCR. Cross-page DIVISIO TEXTUS body reflowed cleanly from the two-column raw lines. The page-break `<!-- page 541 -->` placed at the correct paragraph boundary. The TRACTATIO listing matches OCR (raw 12149–12162) word-for-word.
- **Apparatus**: 1 entry, [^1] = `Cap. 1. seqq. — Mox pro est cod. T.` Verified against OCR line 12125: `1 Cap. 1. seqq. — Mo,\ pio esl cod. T` (silent OCR fix `Mo,\ pio esl` → `Mox pro est`). The `**En.**` rendering ("Lombard, *Sentences* Bk. I, d. 31, c. 1 and following. — Just below, for *est* codex T [reads otherwise]") is a literal expansion plus translator gloss; faithful to the Latin. NO fabrication.
- **Notes block**: notes that TRACTATIO QUAESTIONUM here lists only the 3 questions of Art. I; the 3 questions of Art. II are introduced separately at the article-2 boundary (raw c. line 12823) per multi-article distinction pattern. Confirms the chunk does not under-extract.
- **English**: literal, parallel to Latin.
- **transcription_status**: dated 2026-05-06, accurate.
- **Verdict**: clean. No edits.

### bon-sent-I-d31-p2-dubia.md — PASS (no changes)

- **Bounds**: frontmatter `line_start: 13273, line_end: 13569`.
  - `DUBIA CIRCA LITTERAM MAGISTRL` at line 13273.
  - DUB I at 13277, DUB II missing direct heading marker (col-B interleave), DUB III at 13379, DUB IV at 13322 (col-B), DUB V at 13458 (col-B), DUB VI at 13420 (col-B), DUB VII at 13468 (col-B), DUB VIII at 13557. All 8 dubia present in chunk body.
  - DUB VIII body terminates at line 13568 (`unitatem habeant in essentia.`).
  - `DISTINCTIO XXXII.` running head at line 13570; chunk correctly stops at 13569.
- **Latin body**: 8 dubia (I–VIII) all present, verbatim from OCR after standard de-interleave + silent OCR fixes. Marginal-gloss-style inline `*[Ratio 1]*`, `*[Ratio 2]*`, `*[Quid sit ars]*`, `*[Defenditur ratio Hilarii]*`, etc. preserved as Quaracchi inline glosses (not stripped — these are different from the column-edge marginalia conventionally stripped, since they are narratively integrated). Per project convention this is acceptable; no body invention.
- **Apparatus — 8 entries verified**:
  - [^1] `Cod. bb hunc.` = OCR line 13305 footnote 8 ✓
  - [^2] `Cod. T omittit relationem. secundum. Mox pro quae...` = OCR line 13306–13308 footnote 9 ✓
  - [^3] `Codd. dd ee omittunt qui est. Mox pro etiam est Vat. esset etiam.` = OCR p.550 footer fn 5 ✓
  - [^4] `Multi codd. indistincta, sed infra...` = OCR p.550 footer fn 7 ✓
  - [^5] `Aristot., VI. Topic. c. 3. (c. 4.), ubi et hanc rationem addit...` = OCR p.550 footer fn 8 ✓
  - [^6] `Nostra lectio, quae plurimorum codd. et ed. 1 auctoritate fulcitur...` = OCR p.550 footer fn 9 ✓
  - [^7] `Vide hic in lit. Magistri, c. 3. notula. — Pro ubi codd. cum ed. 1 quia...` = OCR line 13586–13593 (footer of p.552 col-A) ✓
  - [^8] `Pro substantiam fere omnes codd. cum edd. 1, 2, 3 consonantiam; perperam...` = OCR line 13586–13594 (footer of p.552 fn `*` = 2) ✓
- **Bound nit (non-blocking)**: the p.552 footer band carrying [^7] and [^8] is at OCR lines 13586–13602, technically past `line_end: 13569`. The chunk's body-end-only bound is consistent with the d.26 audit precedent (bounds = body-end; apparatus pulled from page footers regardless). NOT a fabrication or extraction error — the apparatus content IS faithfully sourced. The remaining 2 footnotes in that p.552 footer band (footnotes 3 and 4: `Vat. nec non plurimi codd. hic valde incongrue subiiciunt sicut...` and `Complures codd., inter quos G H S cum ed. I quin.`) anchor to the d.32 col-B body content that begins at raw line 13570, so they correctly belong to the d.32 next chunks, not this one.
- **English**: literal, parallel to Latin. Scholastic formulae and inline gloss markers preserved. Block quotations (e.g., the `«principium totius deitatis»` in DUB VI) carried over as italicized inline quotations in English.
- **transcription_status**: dated 2026-05-06, accurate.
- **Verdict**: clean. No edits.

## Totals

- 5 chunks audited.
- 5 PASS (0 with fix).
- 0 chunks reverted to skeleton.
- 0 paraphrase issues found in body Latin or English.
- 0 invented Latin in body.
- 0 fabricated apparatus entries.
- 0 missing apparatus entries (all OCR-visible footer notes are accounted for).
- Backups: none required (no edits made).

## Anomalies

- **p.540 dubia footer band absent from OCR sweep.** Standard for printed Quaracchi (the page footer printer-marks are present, but ABBYY OCR did not emit them as a parseable column). Body footnote markers exist at OCR positions (e.g. `decima, nona '`, `sibi ^ similis`); chunk handles this honestly via `has_apparatus: false` + Notes-block disclosure of the p.540 fn 7 (`Cod. W adiicit Deo`) tracked in `d31-d40-polish-resolution-log.md`. Same defect pattern as d.26 p. 464 footer.
- **[^19] in d.31-littera is an OCR-noise marker preserved for chunk-numbering consistency.** Already disclosed in the chunk transparently with PDF-confirmed reasoning; not a fabrication.
- **No bound, paraphrase, or anchor mismatches** in any of the 5 chunks. The 2026-05-07 polish pass (decade-cadence, d.31–d.40, [?]-flag resolution log) successfully cleared d.31 in body and apparatus.
- **Vat-variant inversions, body omissions, line-bound leakage**: zero detected.

## Open follow-ups (not blockers)

- Eyes-on-PDF read of `doctorisseraphic12bona.pdf` p. 130 (printed p. 540) to formally extract the p.540 d.31 dubia footer band (≥ 7 footnotes including `Cod. W adiicit Deo`). Already tracked in `d31-d40-polish-resolution-log.md`. Not blocking d.32+ work.

## Smoke-test

- `cd site && node scripts/build-content.mjs` →
  ```
  Built content.json: 1 book(s), 422 questions, 350 translated
  ```
- Build clean; chunk counts and parses unchanged.
