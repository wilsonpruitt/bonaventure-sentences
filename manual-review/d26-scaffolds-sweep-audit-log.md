# d.26 scaffolds sweep audit log — 2026-05-08

Scope: `vol1/bon-sent-I-d26-{divisio,littera,dubia}.md`. Goal: verify chunk bounds, diff Latin against pt2 raw OCR, diff/build apparatus, fix paraphrase, never invent Latin or fabricate apparatus.

Source: `raw/bonaventure_vol1_pt2_raw.txt`. Pt2 PDF offset = printed − 410.

## Per-chunk verdicts

### bon-sent-I-d26-divisio.md — PASS (no changes)

- **Bounds**: frontmatter `line_start: 3219, line_end: 3274`. OCR layout:
  - `COMMENTARIUS IN DISTINCTIONEM XXVI.` at line 3218.
  - `DIVISIO TEXTUS.` at line 3224.
  - Body runs 3227–3258.
  - `NOTAE AT COMMENTARITJM.` (= NOTAE AD COMMENTARIUM) footer at line 3267.
  - Notes 1–4 on lines 3269–3270 (col-A) and 3264–3266 + 3267–3268 (col-B / interleaved).
  - `DIST. XXVI. ART. UNICUS QUAEST. I.` (next chunk) at line 3276.
  - Bounds correctly capture body + apparatus, ending before next chunk's running head.
- **Latin body**: verbatim against OCR after standard de-interleave + silent OCR fixes (`midtipliciter` → `multipliciter`, `subhstantiam` → `substantiam`, `aelernaliter` → `aeternaliter`, `temporahter` → `temporaliter`, etc.). All 4 footnote anchors `[^1]–[^4]` placed at the OCR marker positions (`egit '`, `communiter '`, `capitula °`, `auctoritate ^`).
- **Apparatus**: 4 entries match OCR p. 451 footer (and bottom-of-page-450 spillover) verbatim. Bilingual `**La.**` / `**En.**` structure preserved. No fabrication.
- **English**: literal, paragraph-for-paragraph parallel to Latin.
- **transcription_status**: dated 2026-05-04, descriptive, accurate. No update needed.
- **Verdict**: clean. No edits.

### bon-sent-I-d26-littera.md — PASS (no changes)

- **Bounds**: frontmatter `line_start: 2945, line_end: 3217`.
  - `DISTJNGTIO XXVI.` (OCR garble for DISTINCTIO XXVI) at line 2945 — chunk head.
  - Lombard caps I–IV span pp. 447–448 (raw 2945–3110); caps V–VIII span pp. 449–450 (raw 3114–3215).
  - `COMMENTARIUS IN DISTINCTIONEM XXVI.` at line 3218 — chunk tail correctly stops at 3217.
  - The 2026-05-04 head-clip (recorded in transcription_status) is intact: caps I–IV opening present and verbatim from OCR.
- **Latin body**: 8 chapters fully present, verbatim against OCR. Cap headings (`Cap. I.` through `Cap. VIII.`) preserved. Italic title-rubrics intact. Augustine + Hilary + Jerome quoted text reflowed cleanly from two-column OCR.
- **Apparatus**: 22 entries reflowed from p. 447 (footer A1–A2 + col-B implicit), p. 448 (col-A 1–5 + col-B 6, 7, 8), p. 449 (col-A 1–3 + col-B 4, 5, 6, 7), p. 450 (col-A 1, col-B). Spot-checked entries [^5] (*spiratio*), [^6] (Cap. 5. n. 6), [^7] (*dixerit*), [^8] (Num. 23), [^9] (Psalm 81:6), [^10] (Exod. 1:22), [^11] (*A sola Vat. omittit filii Dei*), [^12] (Num. 12 et 13) — all verbatim against OCR with bilingual `**La.**`/`**En.**` structure. No fabrication detected.
- **Anchors**: `[^1]–[^22]` matched between Latin body, English body, and apparatus definitions. Approximate-anchor-position notes on [^3], [^14], [^19], [^20], [^21] retained per the existing `manual-review/tier2-ambiguities-d26-littera.md`.
- **English**: literal, parallel paragraph-for-paragraph; quotation-mark conversion `«…»` → `"…"`. Hilary, Augustine, Jerome quotations preserved as block embedded text per Quaracchi typography.
- **transcription_status**: dated 2026-05-04 (Phase C Tier 2 + head-clip fix). Already polished; no update needed.
- **Verdict**: clean. No edits.

### bon-sent-I-d26-dubia.md — PASS WITH FIX (one apparatus entry corrected)

- **Bounds**: frontmatter `line_start: 4355, line_end: 4587`.
  - `DUBIA CIRC\ LITTERAM MAGISTRL` (OCR for DUBIA CIRCA LITTERAM MAGISTRI) at line 4355 — head correct.
  - `DUB. I.` at line 4358 (OCR `DuB. L`); DUB II–X follow in raw 4396, 4358-col-B, 4374, 4395-col-B, 4495, 4495-col-B (Dub VII), 4508, 4572, 4572-col-B.
  - Body for DUB X ends at line 4585 (`secundo modo dicitur ab aeterno.`).
  - `DISTINCTIO XXVII.` at line 4588. Chunk correctly ends at 4587.
- **Latin body**: 10 dubia (I–X) all present, verbatim against OCR after standard de-interleave + silent OCR fixes (recorded in `tier2-ambiguities-d26-dubia.md`). Anchors `[^1]–[^23]` placed at OCR marker positions; markers in raw OCR appear as `'`, `^`, `*`, etc.
- **Apparatus pp. 462–463**: 21 entries `[^1]–[^21]` reflowed verbatim from p. 462 footer (raw 4438 ff.) and p. 463 footer (raw 4528–4557). Spot-checks against OCR confirm content (Aristotle/Porphyry on accidents, Boethius, John 8:44 anchor [^17], etc.). No fabrication.
- **Apparatus p. 464**: **OCR sweep does not capture a footer band on p. 464.** The body OCR line 4585 is followed immediately by line 4587 → 4588 `DISTINCTIO XXVII.` heading. No `* Vers.` / `* Aristot.` numbered footnotes between. Body markers for [^22] (line 4579, `simul natura'`) and [^23] (line 4583, `sic et^`) are present, so footnotes do exist on p. 464 — but the OCR sweep missed the footer block.
- **Issue caught (2026-05-04 reconstruction defect)**:
  - Prior [^22] reconstruction = `Aristot., de Praedicam. c. de Relatione.` Plausible (verbatim duplicate of [^19]'s Aristotle citation, fitting the *simul natura* tag). But unverified.
  - Prior [^23] reconstruction = **verbatim copy of [^17]** (`Vers. 44. — Paulo superius post secundo modo cod. V repetit dicitur. — Hoc dubium solvit etiam B. Albert., hic a. 15; S. Thom., hic circa lit.`). [^17] is the John 8:44 / "in John 8 the Lord says sinners have devil for father" footnote in DUB VI. It cannot also be the [^23] footnote on DUB X's `sic et donum`. This is fabricated apparatus content (parroted from [^17]) — violates the "NEVER fabricate apparatus" rule. Trailing `[?]` was the only acknowledgment.
- **Fix applied (2026-05-08)**:
  - [^22] retained but explicitly `[?]`-flagged with reconstruction-pending-verification note (rather than appearing as a settled entry).
  - [^23] reverted to honest `[?]`-flagged stub describing what is known (body marker on `sic et`, footer absent from OCR sweep, eyes-on-PDF needed).
  - `transcription_status` updated to record the 2026-05-08 sweep correction.
  - `manual-review/tier2-ambiguities-d26-dubia.md` updated with the correction note.
  - Backup of pre-edit chunk: `vol1/_backup-d26-dubia-pre-rebuild-20260508/bon-sent-I-d26-dubia.md`.
- **Verdict**: bounds clean, body clean (21 verified entries), 1 fabricated apparatus entry corrected, 1 plausibly-correct-but-unverified entry transparently flagged.

## Totals

- 3 chunks audited.
- 3 PASS (1 with fix).
- 0 chunks reverted to skeleton.
- 0 paraphrase issues found in body Latin or English.
- 0 invented Latin in body.
- 1 fabricated apparatus entry corrected ([^23] in dubia).
- 1 plausibly-correct apparatus entry retained but transparently `[?]`-flagged ([^22] in dubia).
- Backups: `vol1/_backup-d26-dubia-pre-rebuild-20260508/`.

## Anomalies

- **OCR sweep missed p. 464 footer band entirely.** This is the only place in d.26 where the IA djvu OCR text fails (footer is present on the printed page, just not captured by the OCR pass). 2 footnotes ([^22], [^23]) genuinely need eyes-on-PDF (pdf p. 54, printed p. 464) for resolution. Dispatch with the standard `pdftoppm -r 600 -f 54 -l 54` on `raw/doctorisseraphic12bona.pdf` (or via `tools/extract-pages.py --volume vol1 --pages 464`).
- **No bound, paraphrase, or anchor mismatches** in any of the 3 chunks. The 2026-05-04 polish pass (decade-cadence, d.21–d.30) successfully cleared d.26 in all but the noted [^23] regression.

## Open follow-ups (not blockers)

- Eyes-on-PDF read of `doctorisseraphic12bona.pdf` p. 54 (printed p. 464) to resolve [^22] (likely confirms Aristotle *Categories* c. *de Relatione*, 7b15 *simul natura*) and [^23] (unknown content; body marker is on `sic et donum` conjunction, suggesting variant reading). Tracked in `manual-review/tier2-ambiguities-d26-dubia.md`.

## Smoke-test

- `cd site && node scripts/build-content.mjs` — see report tail.
