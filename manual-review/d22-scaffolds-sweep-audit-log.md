# d.22 scaffolds sweep audit log (2026-05-08)

Scope: `vol1/bon-sent-I-d22-{divisio,littera,dubia}.md`. The three chunks were last rebuilt 2026-05-03 (backup at `vol1/_backup-d22-pre-rebuild-20260503/`). Today's sweep diffed each chunk's `## Latin` body and apparatus against `raw/bonaventure_vol1_raw.txt` (IA djvu OCR) line-for-line and verified anchor positions against OCR-marker positions. Pre-edit copies saved to `vol1/_backup-d22-{divisio,littera,dubia}-pre-rebuild-20260508/`.

## Per-chunk verdict

### `bon-sent-I-d22-divisio.md` — PASS
- Bounds 67263–67356 verified tight: line 67255 is the `COMMENTARIUS IN DISTINCTIONEM XXII` opener (correctly excluded), 67263 is the `DIVISIO TEXTUS` heading (included), 67357 starts `ARTICULUS UNICUS` of a1-q1 (correctly excluded).
- Latin body matches OCR verbatim after standard ligature/letter cleanup. All seven apparatus entries match raw lines 67328–67348 (NOTAE AD COMMENTARIUM block).
- Footnote anchors agree with OCR-marker positions where present (`determinat¹`, `Divisionum²`, `secundo capitulo³`, `partes⁴`, `uno⁵`, `aut⁶`, `aliquo⁷`).
- No edits.

### `bon-sent-I-d22-littera.md` — PASS
- Bounds 67093–67254 verified tight: 67093 is the `DISTINCTIO XXII` heading; 67255 starts the `COMMENTARIUS` chunk handled by divisio.
- Latin body matches OCR verbatim. All eight apparatus entries (notes 1–6 from p.388 footer at raw lines 67199–67227, notes 7–8 carry over to divisio's footer block immediately above) verified.
- Anchor positions agree with OCR.
- No edits.

### `bon-sent-I-d22-dubia.md` — CORRECTED (3 substantive edits)
Bounds 68815–69042 verified. The five-rules-block-as-appendix structural decision is the right call (printed p. 400 sets it as a free-standing centered heading, not a numbered DUB.). Three substantive issues found and fixed:

1. **DUB. II base text was the Vatican variant, not Quaracchi's base text.**
   - Raw OCR line 68878: `defieit` (clearly OCR garble for *deficit*).
   - Apparatus note 8 (raw line 68964): `Vat. absque auctoritate mss. et edd. 1, 2, 3 differt …` — i.e. *Vat reads* `differt` *against* mss and edd. 1–3. By Quaracchi convention this means the editorial base text retains the mss reading, here `deficit`.
   - The 2026-05-03 rebuild silently substituted the Vatican variant `differt` into the body (see prior ambiguities log line 38: `defieit → differt`), which inverted the base-text/variant relationship.
   - Fix: restored `deficit` in Latin body; English now "falls short" rather than "differs"; apparatus note 8 English clarified that `differt` is the Vatican variant *in place of* `deficit`.

2. **`[^18]` anchor was placed at end of clause; OCR has the marker mid-clause at `vel`.**
   - Raw OCR line 68930: `nisi omnipotens sit adiectivum vel¹¹ adiective retentum.` — marker between `vel` and `adiective`, not after `retentum`.
   - Apparatus note 18 (raw 11) reports two variants jointly: Vat reads `et` (replacing `vel`) and `tentum` (for `retentum`). Anchoring at the first cited variant (`vel`) follows the project convention.
   - Fix: moved `[^18]` from `retentum[^18]` to `vel[^18]`. English mirrors the shift.

3. **DUB. IV word order at note 22 was wrong (and inconsistent with OCR base text).**
   - Raw OCR line 68954: `dicendum, quod est esse maius¹⁵ dupliciter`.
   - Apparatus note 22 (raw 15) says Vat (and one other codex) wrongly omit `esse`; cod. T reads `quod esse maius dicitur dupliciter`. The Quaracchi base text retains both `est` and `esse` in the OCR-printed order: `quod est esse maius dupliciter`.
   - The 2026-05-03 rebuild rewrote this as `quod esse maius est dupliciter`, which matches neither the OCR base text nor any cited variant.
   - Fix: restored `quod est esse maius` (Latin) and adjusted the English clause for the correct sense (*being greater* is taken in two ways).

`transcription_status` updated with the date-stamp of these three corrections.

## Anomalies / open items

- The 2026-05-03 ambiguities log noted `defieit → differt` as a "silent OCR fix" with rationale "per apparatus note 8: Vat. reading is *differt*; OCR conflated." That rationale was the wrong direction: the Vat reading in an apparatus is the variant, not the base. Worth a project-owner note in case other chunks made the same inversion. The `bonaventure-decade-polish` cadence (d.21–d.30 polish pass, status TBD per `MEMORY.md`) is the natural place for a corpus-wide spot-check on `Vat. … X loco/pro Y` apparatus entries.
- DUB. I `[^4]` and `[^5]` continue to share a single underlying apparatus entry (the entry covers two anchor positions, "hic et paulo infra post *personis*"). That dual-anchoring is documented in the ambiguities log and is left as-is.
- No new `[?]` flags were raised; raw OCR resolved every reading examined.

## Build smoke-test

`cd site && node scripts/build-content.mjs` — see end of session output.
