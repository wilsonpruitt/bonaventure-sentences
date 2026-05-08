# d.28 Scaffolds Sweep Audit Log

Audit date: **2026-05-08**.
Source of truth: `raw/bonaventure_vol1_pt2_raw.txt` (IA djvu OCR, pt2).
Pt2 PDF offset: `pdf_page = printed_page − 410`.

## Scope

Sweep audit of the three "scaffold-style" chunks of d.28 — `divisio`, `littera`, `dubia` — to catch silent paraphrase, Vat-variant inversion, fabricated apparatus, body omissions, or anchor leakage that may have survived the d.27–d.30 polish-blocker pass on 2026-05-06.

The four quaestio chunks (`a1-q1` … `a1-q4`) are not in scope of this sweep — they were the focus of the polish pass logged in `d27-d30-polish-resolution-log.md`.

## Per-chunk verdicts

### `bon-sent-I-d28-divisio.md` — CLEAN

- Bounds: frontmatter `line_start: 7778, line_end: 7863` matches OCR — `COMMENTARIUS IN DISTINCTIONEM XXVIII` at raw 7778, divisio body 7791–7829, `TRACTATIO QUAESTIONUM` 7834–7844, page-bottom NOTAE 7849–7853. Verified.
- Latin body: matches OCR verbatim after de-interleaving the two-column page-bottom layout. Marker positions for `[^1]`–`[^4]` correspond to OCR anchors at *elucescunt*, *Tertio*, *determinat*, *huius partis*.
- Apparatus: 4/4 entries faithful to raw OCR (Aristot. *Elench.* + *de Caelo*; Vat. addition `Adiungens…`; codd. PQW *solvit*; Vat. suppression of `Sciendum quoque…`). No fabrication detected.
- English body: literal, parallel paragraph structure preserved.
- No edit needed.

### `bon-sent-I-d28-littera.md` — FIX APPLIED

- Bounds: 7590–7777 (Lombard's text, capp. I–VII, pp. 493–494). Verified against raw `DISTINCTIO XXVIII` heading at 7590 and Bonaventure-pt2 commentary boundary at 7778.
- Latin body: matches OCR (after Quaracchi two-column reflow). Cap. headings, Augustine and Hilary quotation strings, and Ambrose excerpt all verbatim.
- **Finding (silent omission)**: chunk skipped p. 494 footnote 3 (Quaracchi page-internal numbering: `Cap. 2. n. 3.` — the Augustine *de Trinitate* VII source citation for the `«Id dici accipiamus…»` block-quote). Raw OCR line 7725 carries an OCR-rendered footnote anchor (`'`) at `Augustinus in septimo libro de Trinitate'`. Chunk had no `[^N]` anchor at this body position and dropped the apparatus entry; subsequent p. 494 footnotes were correctly numbered as if the entry never existed.
- **Resolution**: inserted apparatus entry as new `[^9]` (`Cap. 2, n. 3.` / "Chapter 2, n. 3."); added body anchor `[^9]` at *septimo libro de Trinitate* in both Latin and English; renumbered prior `[^9]`–`[^14]` body anchors and apparatus defs to `[^10]`–`[^15]`. Apparatus header range note updated from `[^7]–[^14]` to `[^7]–[^15]`. Backup placed at `vol1/_backup-d28-littera-pre-rebuild-20260508/bon-sent-I-d28-littera.md`. Frontmatter `transcription_status` extended with 2026-05-08 sweep note.
- Other apparatus entries (`[^1]`–`[^8]`, `[^10]`–`[^15]`): all verbatim against raw OCR. No fabrication.
- No `[?]` flags introduced.

### `bon-sent-I-d28-dubia.md` — CLEAN

- Bounds: frontmatter `line_start: 8662, line_end: 8848`. Verified — `DUB. I` at 8662, `DUBIA` running head at 8758, Dubia-V close near 8830, page footer / DISTINCTIO XXIX at 8849. Apparatus footers at 8726–8752 (p. 504) and 8836–8842 (p. 505).
- Latin body: 5 dubia (DUB. I–V) match OCR verbatim after two-column de-interleave.
- Apparatus: 17/17 entries verified against raw OCR. The polish-log correction `negativum` (vs OCR `negalumn` at line 8838) is in place at `[^13]`. No fabricated entries; no Vat-variant inversions detected.
- English body: literal; anchors mirror Latin.
- No edit needed.

## Totals

- Chunks audited: 3 (divisio, littera, dubia).
- Clean: 2 (divisio, dubia).
- Fixed: 1 (littera — one missing apparatus entry restored, body anchors added, six subsequent footnote numbers shifted).
- New `[?]` flags: 0.
- Backups created: 1 (`_backup-d28-littera-pre-rebuild-20260508/`).
- Build smoke-test: `node scripts/build-content.mjs` → `Built content.json: 1 book(s), 422 questions, 350 translated`. Clean parse.

## Anomalies / observations

- **`d28-littera` apparatus omission survived the 2026-05-06 polish pass.** The 25-flag inventory in `d27-d30-polish-resolution-log.md` did not catch this because the missing entry left no `[?]` marker — it was a silent body-anchor + apparatus drop. The d.31–d.40 polish cadence and the corpus formatting audit only verify *pairing* (every `[^N]:` def has matching body anchors) and *frontmatter completeness*; they cannot detect apparatus entries that the chunk never claimed. Worth folding "compare apparatus entry count against page-bottom NOTAE band line count" into a future audit script if cheap.
- The Quaracchi page-internal footnote re-numbering (each printed page restarts at `1`) creates a recurring opportunity for off-by-one drops at page boundaries when chunks span two printed pages. d28-littera straddles pp. 493–494 and the OCR drops the visual `'`/`²`/`³` glyph distinction between an in-body marker and a footnote-band index, which is exactly where this entry slipped.

## Commit status

No commits made. Edits and audit log staged in working tree.
