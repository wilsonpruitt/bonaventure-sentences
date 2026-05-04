# Tier-2 Ambiguities — bon-sent-I-d25-a2-q2

Source: `raw/bonaventure_vol1_pt2_raw.txt` lines 2680–2772 (printed pp. 444–445; PDF pp. 546–547 in `raw/doctorisseraphic12bona.pdf`).

Promoted to Tier 2 on 2026-05-03. PDF offset +102 (pdf_page = printed_page + 102) confirmed against sibling pt2 chunks `bon-sent-I-d25-a1-q1.md` (435/537), `bon-sent-I-d25-littera.md` (432–434/534–536), and `bon-sent-I-d24-littera.md` (418–419/520–521). The earlier `bon-sent-I-d25-divisio.md` records `pdf_pages: [24, 25]` which is wrong and should be `[536, 537]` — flagged for separate cleanup, not touched in this pass.

## OCR garbles silently corrected

- "QUAESTIO 11." (centered title heading at line 2680) → `QUAESTIO II.`
- "Utruin" → `Utrum` (printed Latin standard).
- "dictuni" / "crealis" → `dictum` / `creatis` (title line).
- "univocura" → `univocum`; "uihil" → `nihil`; "Contba" → `Contra`; "et^" / "in genere ^" / "persona ^" / "ad res°" / "analogice '" / "et cum^" / "analogum^" — all marker-position garbles where the OCR rendered the superscript footnote digit as an apostrophe, caret, degree sign, or stray digit. Resolved by mapping to consecutive `[^N]` markers.
- "ahquid" / "incommnnicabililate" / "communitas habitudi-" / "univocaiio" / "communitas habitudinis" — typesetter ligature/spacing artifacts; corrected silently.
- "Qaacstio in-" (gutter marginal) → `*(Quaestio incidens.)*` rendered inline as an italicized parenthetical label, matching the pattern established in `bon-sent-I-d25-a1-q1.md` for printed marginal headings.
- "Ad opposi-" (marginal) → omitted as gutter label that does not correspond to a body sentence; the *Contra* arguments are introduced by the bold **Contra:** marker only.
- "Fandamenu." (marginal at *Contra* arg 1) → `*(Fundamenta.)*` (matches printed *fundamenta* convention).
- "DistincUo." (marginal at "Sed attendendum") → `*(Distinctio.)*`.
- "soiuiio op-" (marginal at solution 1) → `*(Solutio oppositorum.)*`.
- "conciusiod" / "conciusio 2" / "conciusio 3" / "conciusio 4" (marginals) → `*(Conclusio 1.)*` etc.
- "SOHOLIOK" → `SCHOLION`.
- "DDBIA CIRCA LITTERAM MAGISTRI." at line 2770 = boundary marker for next chunk; not included.
- "DIST. XXV. ART. II. QUAEST. II. ... 448" (line 2726, running head): the `448` is OCR error for **445**; printed page numbers 444 (preceding, line 2637) and 446 (following, line 2818) confirm the page-445 placement of the running head. Used as `<!-- page 445 -->` boundary in the chunk.
- Scholion II citation list: "S^6" → `36`; "S6" → `36`; "33" reading verified against analogous citation patterns; "^gid. R." → `Aegid. R.` (Aegidius Romanus); "Ilenr. Gand." → `Henr. Gand.`; "lum" → `tum`; "unicocum" → `univocum`; "persome" → `personae`; "conimune" → `commune`; "di/fert" → `differt`; ".4d" → `Ad`; ", a. 4. a. 1." → `m. 4. a. 1.` (Alex. Hal. citation form: pars . membrum . articulus).

## Marginal labels rendered inline

The OCR shows printed marginal headings ("Ad opposi[tum]", "Fundamenta", "Quaestio incidens", "conclusio 1–4", "Distinctio", "Solutio oppositorum") set in the gutter alongside the body. These are rendered as italicized parenthetical labels (`*(Conclusio 1.)*` etc.) in both Latin and English, immediately preceding (or following, where the OCR placement and the printed marginal align) the paragraph they describe — same convention as `bon-sent-I-d25-a1-q1.md`.

## Footnote anchor positioning

- p. 444 has 5 footnote markers in the body (numbered 1–5 here):
  - [^1] at *et* in arg. 2 («reperitur et[^1] in creatura»).
  - [^2] at *in genere* in *Contra* 2.
  - [^3] at *persona* in *Quaestio incidens* 4 («de quo per prius dicatur *persona*[^3]»).
  - [^4] at *prius* in the *Respondeo* opening («sicut visum est prius[^4]»).
  - [^5] at *res* in the *Distinctio* on the right column («per comparationem ad res[^5] diversorum generum»).
  These match exactly the five entries in the p. 444 footer apparatus block (raw lines 2723–2725).
- p. 445 has 3 further body markers (numbered 6–8 here):
  - [^6] at *analogice* in the second *Conclusio* on the left column («ideo analogice[^6] et aequaliter»).
  - [^7] at *cum* in the *Solutio ad 3* on the right column («et cum[^7] alia ratio distinguendi»).
  - [^8] at the closing *analogum* in the *Solutio ad 3* («sed solum analogum[^8]»).

## p. 445 apparatus footer — MISSING from OCR

Critical gap. The p. 445 footer apparatus block, which should contain entries for body markers 6–8, is **not present** in the IA djvu OCR of pt2 between the body text (raw line 2751) and the SCHOLION header (raw line 2754). The OCR appears to have absorbed or skipped that printed footer block entirely (a known artifact when the SCHOLION begins very near the page bottom and the columns reflow).

Action taken in this pass:
- All three apparatus entries `[^6]`, `[^7]`, `[^8]` are inserted with `[?]` flags and a note that the entry was not preserved in the OCR.
- Body markers are kept in the chunk so the apparatus parser remains balanced (5 + 3 = 8 footnotes, all present in both Latin and English bodies and in the apparatus block).

Resolve later by:
- Visually inspecting `raw/doctorisseraphic12bona.pdf` p. 547 (printed p. 445) bottom margin — request a manual extraction of the page image (`pdftoppm -f 547 -l 547 -r 300`).
- Or by cross-checking against another scan of the Quaracchi pt2 (e.g., a higher-resolution IA mirror) for the missing footer text.

## Cross-references

- Sibling chunk `bon-sent-I-d25-a2-q1.md` is still `auto-chunked 2026-04-18` (skeleton). When that chunk is promoted, its p. 443 → p. 444 boundary will need to align with this chunk's beginning at raw line 2680.
- Sibling chunk `bon-sent-I-d25-divisio.md` carries an incorrect `pdf_pages: [24, 25]` (should be `[536, 537]` for printed pp. 434–435); flagged here, not modified in this pass.
