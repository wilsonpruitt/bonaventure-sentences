# d.8 Scaffolds Sweep-Audit Resolution Log

Audit date: **2026-05-08**. Source of truth: `raw/bonaventure_vol1_raw.txt` (Internet Archive djvu OCR of Quaracchi 1882, Tomus I, pt. 1).

d.8 is a multi-pars distinction (Pars I = veritas + immutabilitas; Pars II = simplicitas), so it has 5 scaffold chunks: a single shared `littera` covering both partes, plus per-pars `divisio` + `dubia`.

## OCR line-range verification (frontmatter `line_start` / `line_end`)

| Chunk | Frontmatter | Verified | Verdict |
|---|---|---|---|
| d8-littera | 31017–31495 | matches Lombard text on pp. 147–149 (Cap. I–VIII), incl. footer notes | OK |
| d8-p1-divisio | 31496–31619 | matches `COMMENTARIUS IN DISTINCTIONEM VIII / Pars I / Divisio textus / Tractatio Quaestionum`; spans pp. 149–150 | OK |
| d8-p1-dubia | 33452–33786 | matches `DUB. I` through `DUB. X` on pp. 161–165 | OK |
| d8-p2-divisio | 33787–33899 | matches `COMMENTARIUS / Pars II / Divisio textus / Tractatio Quaestionum`; pp. 165–166 | OK |
| d8-p2-dubia | 35295–35560 | matches `DUB. I` through `DUB. VI` on pp. 175–176 | OK |

Pt2 PDF offset is irrelevant here (all pt1).

## Per-chunk verdicts

### d8-littera — CLEAN ✅

Lombard's text + 14-fn apparatus. Body matches OCR (lines 31017–31495) verbatim allowing for OCR-artifact silent corrections (e.g. `procoditur`, `homo` glyph fixes, italics restoration on Quaracchi formulae). All 14 apparatus entries trace to authentic OCR footer notes on pp. 147–149 (Vat./codd. textual variants on the Hieronymus *ad Marcellam* / *ad Damasum* attribution; Hilary *de Trin.* VII n. 11; the Augustine *de Trin.* V c. 2 n. 3 collation; the John 16:13 *est/etiam* variant; Augustine *contra Maximinum* II c. 12 n. 1; the *de Trin.* VI c. 6 n. 8 collation; the *de Trin.* VII c. 4–5 collation). Anchor positions match OCR marker positions. **No fixes applied**; promoted to Tier 2 string already canonical (2026-04-13).

### d8-p1-divisio — REBUILD APPLIED ⚠️

Two distinct problems both fixed:

**1. Body: missing paragraph.** Chunk's `## Latin` body terminated at *"...quae ponitur quarto capitulo: Eademque sola proprie ac vere simplex est etc."* (OCR line 31537), then jumped to `### Tractatio Quaestionum`. The intervening paragraph (OCR lines 31589–31599, beginning *"Item prima pars habet duas partes, quia primo attribuit Deo proprietatem veritatis..."*) — which carries the second-level subdivision of the *prima pars* into its own two parts (proprietas veritatis + removal of doubt, then unchangeableness sub-part assignment + Apostle confirmation) — was silently dropped. **Restored**, with `<!-- page 150 -->` page break inserted at correct OCR boundary. English translation of restored paragraph added in parallel.

**2. Apparatus: fully fabricated (3 of 3 entries).** The original 3 apparatus entries were AI-style cross-reference glosses:
- `[^1]`: *"Cfr. supra d. 2, Divisio textus, et d. 3, p. I, Divisio textus..."* — not in OCR.
- `[^2]`: *"Cfr. I Sent. d. 19, Comm., ubi S. Bonav. fusius de aequalitate personarum..."* — not in OCR.
- `[^3]`: *"Tertium capitulum Magistri hic refertur ad Cap. II litterae Magistri..."* — not in OCR.

`grep "Cfr. supra d. 2" raw/bonaventure_vol1_raw.txt` returns nothing. The actual Quaracchi *NOTAE AD COMMENTARIUM* footer for the divisio (OCR lines 31568–31580) contains 4 authentic notes about textual variants (`Magister/istius/utraque`; `unitate pro virtute`; alternate chapter-division standard with Vat. *ibi* read; *et haec* vs *quae*). These have been substituted in place of the fabricated cross-references, with body anchors moved to the words they reference (`determinat Magister`; `virtute`; `tertio capitulo`; `quarto capitulo`).

Backup of pre-rebuild file: `vol1/_backup-d8-p1-divisio-pre-rebuild-20260508/`.

**Body paraphrase departures fixed**: 1 (missing-paragraph restoration). **Fabricated apparatus entries replaced**: 3.

### d8-p1-dubia — CLEAN ✅ (light apparatus surplus, not fabrication)

Body matches OCR (lines 33452–33786) verbatim. Section structure (DUB. I–X) intact. The chunk has 10 apparatus entries; OCR has ~19 footer footnotes spread across pp. 161–164. All 10 chunk entries trace to authentic OCR notes:

- `[^1]` (Aristotle *Praedicam.* + grammatici/logici) → OCR fn 5 line 33529–33534 ✓
- `[^2]` (Vat. *non* addition; St. Thomas) → OCR fn 6 line 33537–33548 ✓
- `[^3]` (August. XII *Civ. Dei* c. 15 n. 2) → OCR fn 2 line 33658 ✓
- `[^4]` (Anselm *Monolog.* c. 28 + *Proslog.* cc. 20, 22) → OCR fn 6 line 33679 ✓
- `[^5]` (August. *Genesi ad lit.* I cc. 2, 3, nn. 9, 10 + *contra Ep. Manichaei* c. 40 n. 46) → OCR fn 8 line 33684–33685 ✓
- `[^6]` (De Hieronymo + Scotus I Sent. d. 9) → OCR fn 13 line 33698–33700 ✓
- `[^7]` (August. I *de Trin.* c. 1 n. 3) → not a separate OCR footer note but a cross-reference Bonaventure himself supplies in body; legitimate
- `[^8]` (Iac. 1, 17 cite) → biblical reference, legitimate
- `[^9]` (Alex. Hal. + S. Thom. cross-refs) → OCR fn 7 line 33681–33682 ✓
- `[^10]` (II Sent. d. 2 cross-ref) → OCR fn 5 line 33667–33675 (paraphrased editorial note about creature possibility / *prius et posterius*) ✓

OCR additionally has ~9 minor footer notes (`Vat. cum cod. cc addit Ad quod`; `Aliqui codd. ut F T dd repetunt esse`; `Plurimi codd. omittunt est`; `Plures mss. cum ed. 1 e converso`; `Cod. T vermi`; `Hoc est res aeviterna`; `Supple: non noscere`; `Vat. praeter fidem mss. et ed. 1 etiam`; `Subaudi: creatura`; `Plurimis codd. obnitentibus, Vat. praemittit debere`; `Ex mss. et edd. 1, 2, 3 supplevimus tunc`; `Substituimus fide antiquorum mss. et ed. 1 masculinitate pro masculino genere`) — these are mostly micro-collation variants that the chunk legitimately consolidates or omits per the d.10+ corpus convention (drop pure-orthography codd. comparisons, retain doctrinal/citation notes). Acceptable.

`transcription_status` retained as canonical (2026-04-13). **No fixes applied.**

### d8-p2-divisio — CLEAN ✅

Body matches OCR (lines 33787–33899). Two apparatus entries, both authentic:

- `[^1]` (NOTAE divisio textus partis II in codd. hoc loco ponitur...) → OCR fn 8 line 33840–33842 ✓
- `[^2]` (Fide omnium mss. et ed. 1 restituimus *in parte ista*) → OCR fn 3 line 33968–33969 ✓

The chunk's `[^1]` is anchored at the `### Divisio Textus` heading — supportable, since the OCR footnote concerns the placement of this very block. The `[^2]` is anchored at *"in parte ista"* in the Tractatio — exact OCR position.

OCR has additional footer notes (Bernard *de Gratia*; *Verba Augustini supra in lit. Magistri c. 2*; *Vat. cum cod. cc alio pro illo*; etc.) that the chunk does not represent — these are micro-variants on the body of the divisio, legitimately omitted.

`transcription_status` retained as canonical (2026-04-13). **No fixes applied.**

### d8-p2-dubia — 1 fix applied

Body matches OCR (lines 35295–35560). 6-dubium structure intact (DUB. I–VI; OCR drops the literal "DUB." word from heading II–III, putting only `II.` and `III.` on their own lines, which the chunk normalizes — acceptable).

Apparatus: 6 entries, 5 trace cleanly:
- `[^1]` (Aristotle *Poster.* I c. 10) → OCR fn 4 line 35351–35352 ✓
- `[^2]` (Aristotle *Poster.* I c. 2) → OCR fn 5 line 35361 ✓
- `[^3]` (Boethius *de Trin.* c. 2) → OCR fn 2 line 35461 ✓
- `[^4]` (Aristotle IV *Topic.* c. 2 + Petrus Hispanus) → OCR fn 3 line 35464 ✓
- `[^6]` (Axioma scholasticum *ex duobus entibus actu nihil fit*) → built-up gloss; matches body `*"ex duobus entibus actu nihil fit"*` axiom but no separate OCR footnote covers it (OCR line 35544 has the axiom inline). Not strictly an OCR footer note, but a legitimate editorial note on the axiom; left as-is.

**Fix applied to `[^5]`:** Chunk cited *"August., V de Trin. c. 1, n. 2"* — but OCR raw line 35485 reads *"Lib. V. de Trin. c. 8. n. 9"* and continues with a substantial editorial note (lines 35485–35503) about the scope of Dub IV (translation of generic names to divine things, not whether God is in a genus), citing S. Thom., Alex. Hal., B. Albert., Petrus a Tarentaise, and explicating the holy Doctor's two-part position. The chunk had compressed this into a short St. Thomas excerpt and (more troublingly) misreported the chapter/section as c. 1 n. 2. Replaced with verbatim OCR Latin and literal English. Pre-edit `[^5]` content saved to `vol1/_backup-d8-p2-dubia-pre-rebuild-20260508/bon-sent-I-d8-p2-dubia-fn5-original.md`.

OCR has additional micro-variant footer notes (`Codd. V X secundum`; `Hoc est, per eminentiam`; `Vat. praeter fidem mss. et ed. 1 haec`; `Cod. V hic addit haec`; `Vat. contra mss. et ed. 1 Deum`; `Ed. 1 addit substantia`; `Vat. contra plurimos codd. Quia si`; `Postulantibus antiquioribus mss. et ed. 1, substituimus volunt loco voluerunt`) not represented in chunk — legitimately omitted micro-collation per corpus convention.

`transcription_status` updated to reflect 2026-05-08 sweep + correction.

## Totals

| Chunk | Body fixes | Apparatus fixes | Status |
|---|---|---|---|
| d8-littera | 0 | 0 | clean |
| d8-p1-divisio | 1 (missing paragraph restored) | 3 fabricated → replaced | rebuilt |
| d8-p1-dubia | 0 | 0 | clean |
| d8-p2-divisio | 0 | 0 | clean |
| d8-p2-dubia | 0 | 1 (chapter/note correction) | minor fix |
| **Totals** | **1** | **4** | — |

## Anomalies / per-pars structural findings

- **d.8 multi-pars architecture is intact**: separate `p1-divisio` + `p2-divisio` files exist (no legacy single `d8-divisio.md` duplicate — the d.8 polish pass had already caught and removed any vestigial duplicate, per the polish-cadence audit logged on 2026-05-06).
- The d.8 `littera` is shared across both partes (one chunk covering Cap. I–VIII of Lombard's text on pp. 147–149) — correct per project's rule that *"Littera Magistri for any multi-chapter distinction should be its own big Tier-2 chunk, separate from the Bonaventure commentary"* (CLAUDE.md, "Re-chunking before translating", item 6).
- **d8-p1-divisio is the worst offender** in this sweep — silent paragraph drop + 3-of-3 fabricated apparatus entries reproducing exactly the pattern caught in d.1 (cross-reference glosses substituting for genuine Quaracchi NOTAE). Pattern continues to be: shorter, structurally lighter chunks (divisio, dubia) are highest-risk for fabrication, because their authentic OCR apparatus is sparse, making it easier for an AI pass to "fill in" plausible-looking glosses.
- d8-p1-dubia and d8-p2-dubia, by contrast, came out **largely clean** — they had been built more carefully. Their apparatus surveys real OCR footer notes (with one chapter-number error on p2-dubia[^5]).
- **No `[?]` flags introduced** — all readings either traced to OCR cleanly or were OCR-artifact corrections per CLAUDE.md silent-correction rules.

## Files touched

- `vol1/bon-sent-I-d8-p1-divisio.md` — full rebuild (body restoration + apparatus replacement)
- `vol1/bon-sent-I-d8-p2-dubia.md` — `[^5]` and `transcription_status` corrected
- `vol1/_backup-d8-p1-divisio-pre-rebuild-20260508/bon-sent-I-d8-p1-divisio.md` — pre-rebuild backup
- `vol1/_backup-d8-p2-dubia-pre-rebuild-20260508/bon-sent-I-d8-p2-dubia-fn5-original.md` — diff record for the surgical edit
