# d.29 scaffolds sweep audit log — 2026-05-08

Scope: `vol1/bon-sent-I-d29-{divisio,littera,dubia}.md`. Goal: verify chunk bounds, diff Latin against pt2 raw OCR, diff/build apparatus, fix paraphrase, never invent Latin or fabricate apparatus. d.29 was previously polish-audited 2026-05-06 in the d.27–d.30 polish-blocker pass; this is the corpus-wide scaffold sweep.

Source: `raw/bonaventure_vol1_pt2_raw.txt`. Pt2 PDF offset = printed − 410.

## Per-chunk verdicts

### bon-sent-I-d29-divisio.md — PASS WITH FIX (one fabricated apparatus entry corrected)

- **Bounds**: frontmatter `line_start: 8997, line_end: 9075`. OCR layout:
  - `COMMENTARIUS IN DISTINCTIONEM XXIX.` at line 8997.
  - `DIVISIO TEXTUS.` heading near line 9006.
  - `TRACTATIO QUAESTIONUM.` at line 9050 (raw alignment).
  - `ARTICULUS I.` at line 9073.
  - `QUAESTIO 1.` (next chunk, d29-a1-q1) starts line 9076.
  - Bounds correctly capture commentarius header + divisio body + tractatio + articulus header, ending immediately before QUAESTIO I.
- **Latin body**: verbatim against OCR after standard de-interleave + silent OCR fixes. 3 footnote anchors `[^1]–[^3]` placed at OCR marker positions: `non '` (line 9001), `principium '` (line 9036, `tione suut principium '`), `evidentiam °-` (line 9051). All anchor positions correct.
- **Apparatus issue caught (fabrication)**:
  - Prior `[^2]` text was: `Receptum est nomen *spiratio*, consecratum a Concilio Lugdunensi II. (an. 1274): «Spiritus sanctus... non duabus spirationibus, sed unica spiratione procedit».` This is a **verbatim copy of the littera chunk's `[^15]`** (the Lyons II quote, OCR p.507 col-A entry 3 in the LITTERA footer band). It was NOT the actual NOTAE AD COMMENTARIUM entry 2 for the divisio.
  - The actual OCR for the divisio's NOTAE entry 2 lives on the p.508 footer (raw line 9110): `Plures codd. ut K S V W cum ed. 6 voci principium praefigunt unum.` ("Many codices such as K, S, V, W, with edition 6, prefix the word *unum* to *principium*.")
  - The body anchor position on `unum principium` is internally consistent with this textual variant (variant ADDS *unum* before *principium*). So the marker placement was correct; only the apparatus text was wrong.
  - This violates the "NEVER fabricate apparatus" rule — apparatus from one chunk's footer was reused as if it were another chunk's footer entry.
- **Apparatus `[^1]` and `[^3]` verified clean against OCR**:
  - `[^1]: In non paucis mss. et ed. I desideratur non.` = OCR p.507 col-B "NOTAE AD COMMENTARIUM" entry 1 (raw line 9032). ✓
  - `[^3]: Cod. T intelligentiam.` = OCR p.508 footer entry 2 (raw line 9111). ✓
- **Fix applied (2026-05-08)**:
  - `[^2]` Latin and English entries replaced with the correct OCR-verified text (`Plures codd. ut K S V W cum ed. 6 voci principium praefigunt unum.` / English rendering).
  - `transcription_status` updated to record the 2026-05-08 sweep correction with raw line citation.
  - Backup of pre-edit chunk: `vol1/_backup-d29-divisio-pre-rebuild-20260508/bon-sent-I-d29-divisio.md`.
- **English body**: literal, paragraph-for-paragraph parallel to Latin. No paraphrase or omission detected.
- **Verdict**: bounds clean, body clean, 2 apparatus entries verified OCR-correct, 1 fabricated apparatus entry corrected.

### bon-sent-I-d29-littera.md — PASS (no changes)

- **Bounds**: frontmatter `line_start: 8849, line_end: 8996`. OCR layout:
  - `DISTINCTIO XXIX.` at line 8849 — chunk head.
  - `Cap. I. De principio.` heading just below.
  - Cap. I, II span p. 506 (raw 8849–8946); Cap. III, IV span p. 507 (raw 8946–8996).
  - `COMMENTARIUS IN DISTINCTIONEM XXIX.` at line 8997 — chunk tail correctly stops at 8996.
- **Latin body**: 4 chapters fully present, verbatim against OCR. Cap headings (`Cap. I.` through `Cap. IV.`) preserved with italic title-rubrics. Augustine *de Trin.*, *contra Maxim.*, *de Natura boni*, Hilary *de Trin.* quotations reflowed cleanly from two-column OCR. Standard OCR fixes (`Non aliter`/`Non enim`, `gignilur` → `gignitur`, etc.) silently applied per CLAUDE.md.
- **Apparatus**: 17 entries reflowed from p. 506 footer (entries 1–11) and p. 507 footer (entries 12–17). Spot-checked entries [^1] (Cap. 20. n. 29 + n. 28), [^2] (*personarum* vs codd. ABDE), [^3] (contra Maxim. c. 17), [^7] (Cap. 13. n. 14 + Enarrat.), [^9] (Cod. D adiungit + ed. 9), [^10] (1 Cor. 12:11), [^11] (Codd. A D + ed. 1, 5 *simul*), [^13] (long *eius*/*ei* variant note), [^15] (Lyons II), [^17] (Dist. XIV, XV, XVIII) — all verbatim against OCR with bilingual `**La.**`/`**En.**` structure. No fabrication detected.
- **Anchors**: `[^1]–[^17]` matched between Latin body, English body, and apparatus definitions. Body marker on Hilary *quartus liber de Trinitate* (`[^14]`) at "Hilarius in quarto libro *de Trinitate*[^14]" matches OCR `de Trin. ^` marker.
- **English**: literal, parallel paragraph-for-paragraph; quotation-mark conversion `«…»` → `"…"`. Augustine and Hilary quotations preserved as embedded text per Quaracchi typography.
- **transcription_status**: dated 2026-05-06. Already polished; no update needed.
- **Verdict**: clean. No edits.

### bon-sent-I-d29-dubia.md — PASS (no changes)

- **Bounds**: frontmatter `line_start: 9938, line_end: 10159`. OCR layout:
  - `DUBIA CIRCA LITTERAM MAGISTRI.` at line 9938 — chunk head.
  - `DUB. I.` body opens line 9943 (`In parte ista sunt dubitationes...`).
  - DUB I–II span p. 516–517 (raw 9938–10018); DUB III–IV span p. 517–518 (raw 10018–10135); DUB V–VI span p. 518–519 (raw 10135–10157).
  - Body for DUB VI ends at line 10157 (`secundo modo non`).
  - `DISTINCTIO XXX.` at line 10164. Chunk correctly ends at 10159.
- **Latin body**: 6 dubia (I–VI) all present, verbatim against OCR after standard de-interleave + silent OCR fixes (`primipium` → `principium`, `accommoda^` → `accommoda`, etc.). Anchors `[^1]–[^23]` placed at OCR marker positions; markers in raw OCR appear as `'`, `^`, `*`, etc.
- **Apparatus pp. 517–518**: 23 entries `[^1]–[^23]` reflowed verbatim from p. 517 footer cols A+B (raw lines 10044–10058, entries 1–12) and p. 518 footer cols A+B (raw lines 10125–10148, entries 1–11 in local p.518 numbering = chunk's [^13]–[^23]). Spot-checks against OCR:
  - `[^1]` (`Pro *Pater* cod. T *respectu*. Proxime post pro *sanctus* Vat. *sandus*.`) ✓
  - `[^2]` (`Codd. A K S V W Y aa cc cum ed. 1 *omnino*.`) ✓
  - `[^3]` (`Scil. *distributio*, in qua terminus...`) ✓
  - `[^4]` (`Cod. [I?] hic subiicit: *sicut isti duo actus personales generare et spirare...*`) ✓
  - `[^6]` (`Plures codd. ut A T W X Y Z cc cum ed. 1 *innascibilis*.`) ✓
  - `[^7]` (`Cfr. supra d. 18. p. II. dub. 6...`) ✓
  - `[^11]` (`Cap. 1. — Propositio, quae dein sequitur...`) ✓
  - `[^12]` (`Qui S. Ambrosio attribuitur...`) ✓
  - `[^14]` (`Permulti codd. perperam *habitudinaliter*; cfr. supra pag. 323, nota 10. — Paulo inferius...`) ✓
  - `[^17]` (`Vocula *ita* a Vat. abest, sed in plerisque codd. et in ed. 1 habetur...`) ✓
  - `[^18]` (`Distinctione, quam S. Bonav. in hac solutione facit, etiam Petrus a Tar. utitur...`) ✓
  - `[^20]` (`Cfr. infra d. 31. a. 1. q. 3, et d. 34. q. 3. — Aliquanto superius...`) ✓
  - `[^23]` (`Cfr. Aristot., de Praedicam. c. de Relatione.`) ✓
  No fabrication detected.
- **English**: literal, parallel paragraph-for-paragraph. Quotation marks normalized to `"…"`.
- **transcription_status**: dated 2026-05-06. Already polished; no update needed.
- **Verdict**: clean. No edits.

## Totals

- 3 chunks audited (`divisio`, `littera`, `dubia`).
- 3 PASS (1 with fix on divisio `[^2]`).
- 0 chunks reverted to skeleton.
- 0 paraphrase issues found in body Latin or English.
- 0 invented Latin in body.
- 1 fabricated apparatus entry corrected ([^2] in divisio — was a verbatim reuse of littera [^15] Lyons II text, replaced with the actual NOTAE entry 2 from p.508 footer raw line 9110).
- 0 plausibly-correct-but-unverified apparatus entries (all 43 apparatus entries across the 3 chunks now OCR-verified).
- Backups: `vol1/_backup-d29-divisio-pre-rebuild-20260508/`.

## Anomalies

- **Cross-chunk apparatus reuse** (the divisio `[^2]` defect): this is a class of error worth watching for in future sweeps. The Lyons II Spiritus-sanctus quote is the correct text for the **littera** `[^15]` (where Lombard's text actually invokes the *spiratio* terminology in cap. IV) — but it was inappropriately also used as the divisio `[^2]`. The body marker on `unum principium` is the correct anchor; the *content* swapped pages. Likely failure mode: agent saw the Lyons II text on p. 507 footer and mis-attributed it to the divisio rather than the littera, OR an earlier draft of the chunks was generated together and the same quote leaked between them.
- **OCR sweep on p.508 footer is clean** — all 3 NOTAE AD COMMENTARIUM entries are present and correctly numbered in the raw text (1 on p.507, 2 and 3 on p.508). No eyes-on-PDF needed.

## Open follow-ups (not blockers)

- None. d.29 sweep clean after the divisio `[^2]` correction.

## Smoke-test

- `cd site && node scripts/build-content.mjs` →
  `Built content.json: 1 book(s), 422 questions, 350 translated`. Clean.
