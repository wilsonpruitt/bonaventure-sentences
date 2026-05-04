# Tier-2 ambiguities — bon-sent-I-d26-littera

Source: `raw/bonaventure_vol1_pt2_raw.txt` lines 3114–3217 (printed pp.449–450; PDF pp.39–40 per −410 offset).

## Boundary surprise

The skeleton's `line_start: 3114` only covers the **tail** of Lombard's d.26 littera (caps IV in fine through VIII opening on pp.449–450). Caps I–IV opening live on **pp.447–448** (raw lines ~2945–3110, embedded mid-d.25-commentarius column-flow), and were NOT auto-chunked into any littera file. Per task instructions ("boundaries verified") I held to the explicit 3114–3217 range; the d.26 caps I–IV-opening Lombard text remains an unassigned gap that should later be either prepended to this chunk or split into a `bon-sent-I-d26-littera-part1.md`.

Tail boundary at 3217 cleanly precedes the COMMENTARIUS IN DISTINCTIONEM XXVI rubric at line 3218 (followed by the *Iam de proprietatibus personarum videamus* opener and DIVISIO TEXTUS at 3221–3224); these ~7 lines were dropped per CLAUDE.md convention.

## Apparatus marker placement (approximate)

The p.449 footnote band (raw lines 3188–3196) yields 10 entries, reflowed col-A (notes 1–5) then col-B (notes 6–10). Marker positions in OCR are partially preserved (`'`, `^`, `°`, `"`, etc.), but cross-page references and column reflow make exact body-anchors uncertain for several entries:

- **[^2]** ("Cap. VI. n. 12. — Supra Vat. et edd. 1, 4, 6 omittunt *et* post *Patris, sed*"). Placed at the "scriptum est" Deut anchor inside the Cap. V Augustine quote, but the variant *et post Patris, sed* is not present verbatim in any nearby Cap. V phrase. The "Supra" ("above") suggests a variant on a phrase earlier on the page or carried from p.448. → **Resolve later**: cross-check against Aug. *de Trin.* VI.12 critical text; may belong inside the Aug. de Trin. quote in Cap. V at "Patrem nostrum" or further up the column.

- **[^7]** ("Cap. II. n. 12") — placed at "iam diximus nec iterare piget, *quia*..." inside the Cap. VI Aug. quote, which references *de Trin.* book V cap. II n.12. Marker position in OCR is `'` between Latin words on raw line 3132 col B; reasonable but not certain.

- **[^8]** ("Codd. ABDE et edd. 1, 2, 3, 7 *quia*. Etiam alibi Magister particula *quia* utitur pro *quod*"). Variant *quia*/*quod*. Placed at the conjunction in "Et est sciendum, quod cum Pater vel Filius dicitur spiritus" (Cap. VI tail) on the assumption Magister wrote *quia* and editions corrected to *quod*; the codex cluster ABDE supports the original *quia*.

- **[^9]** ("Codd. D E hic incipiunt d. XXVII"). Codex-layout note about where D, E begin distinction XXVII. Placed adjacent to the Cap. VII title as the most semantically plausible spot (since codex breaks usually fall at chapter boundaries); could equally belong at the head of Cap. VIII.

## Scribal / OCR garbles silently corrected

- `proprietalis` → `proprietatis`
- `signiflcatione` → `significatione`
- `honio` → `homio` → `homo`
- `fllius` → `filius` (passim)
- `anlequam` → `antequam`
- `estfilius,nascibilitatis` → `est filius, nascibilitatis`
- `eins` → `eius`
- `generatioue` → `generatione`
- `dicilur` → `dicitur` (passim)
- `Trinilas` → `Trinitas`
- `paier` → `pater`
- `factura` → kept as `factura` (Lombard's word for "made-thing")
- `lotius` → `totius`
- `lorte` → `forte`
- `enini` → `enim`
- `Audilsrael, Dominm Deustum` → `Audi Israel, Dominus Deus tuus`
- `(st` → `est`
- `ulique` → `utique`
- `Palrem` → `Patrem`
- `pei- fldem` → `per fidem`
- `lesum` → `Iesum`
- `conflteraur` → `confitemur`
- `ostcnsum esl` → `ostensum est`
- `naMis` → `natus`
- `jyroprielate` → `proprietate`
- `nunciipatione` → `nuncupatione`
- `donimi` → `donum`
- `alla` → `alia`
- `sinl` → `sint`
- `aelerna` → `aeterna`
- `relalive` → `relative` (passim)
- `apparetin` → `apparet in`
- `inef-fabilis` (line break) → `ineffabilis`
- `forlasse` → `forlasse` (kept; this is *fortasse* but rendered *forlasse* in ed. — flag below)
- `Nani` → `Nam`
- `disiunctim` → `disiunctim` (kept)
- `Trinilas` → `Trinitas`
- `scriplum` → `scriptum`
- `etDeiis` → `et Deus`
- `Patei-` → `Pater`
- `Spiritm sancti vcl Doni` → `Spiritus sancti vel Doni`
- `(lonum` → `donum`
- `Augusiinns. gustiuus Uoruni` → `Augustinus huius` (marginal label `Augustinus.` was inline; Quaracchi has marginal note "Augustinus")
- `vicissira` → `vicissim`
- `treni` → `trem` (in `Patrem`)
- `fdius` → `filius`
- `sancli` → `sancti`
- `invenialur` → `inveniatur`
- `donim` → `donum`
- `dotii` → `doni`
- `dommi` → `donum`
- `aelerno` → `aeterno`
- `ti donator` → `et donator`
- `licct` → `licet`
- `respon-deat` → `respondeat`
- `palrem` → `patrem`
- `usitalum` → `usitatum`

## Genuine `[?]` flags

None inserted in body. All readings sufficiently disambiguated by context.

## Notes

- Marginal-gloss labels (`Augustinns.`, `Differaut`, `Hilarius.`, `in Augustin`) appearing inline in OCR were trimmed as editorial marginalia, per CLAUDE.md OCR cleanup rules.
- The Cap. V section heading (Cap. V. *Quod homo dicitur filius Trinitatis, et Trinitas pater*) had OCR fragmenting "Trinitas pater" across columns — recovered cleanly.

---

## 2026-05-04 head-fix update

The boundary gap flagged in the "Boundary surprise" section above has been **resolved**. Caps I–IV opening (raw lines 2945–3113, pp. 447–448) prepended to this chunk via two-column deinterleaving of the IA djvu OCR. New `line_start: 2945`, `printed_pages: [447, 448, 449, 450]`, `pdf_pages: [37, 38, 39, 40]`. Apparatus renumbered consecutively 1–22 (was 1–10); 12 new entries added from p. 447 col-B and p. 448 footers (4 from p. 447 col-B; 5 from p. 448 col-A; 3 from p. 448 col-B). Existing notes 1–10 became 13–22.

### Apparatus marker placement (pp. 447–448, approximate)

- **[^1]** (Hieronymus, Epist. 15) anchored at *Damasum Papam* in Cap. I; OCR marker `'` is on the right column at line 2987 footer, body anchor inferred from quote opening.
- **[^2]** (II Cor. 11:14) anchored at *transfigurat enim se angelus satanae in Angelum lucis* — direct scriptural allusion, anchor unambiguous.
- **[^3]** (Solummodo ed. 2 repetuntur) anchored at *quae ideo a nobis repetitur* in Cap. II head; the note refers to ed. 2's repetition of *ut cordi nostro tenacius infigantur*. Plausible but approximate.
- **[^4]** (Cap. 1. n. 6 / c. 2. n. 7) anchored at *in libro de Fide ad Petrum* in Cap. II; covers both adjacent Augustine quotes.
- **[^5]** (Excepta ed. 8 ... *spiratio*) anchored at *paternitas, filiatio, spiratio* — direct word match.
- **[^6]** (Cap. 5. n. 6; *Unde Augustinus* variant) anchored at *in quinto libro de Trinitate* in Cap. III opening.
- **[^7]** (Solummodo Vat. *dixerit*) anchored at *desineret* in the Aug. quote — the *dixerit* variant likely refers to a verb earlier in the sequence; precise anchor uncertain.
- **[^8]** (Num. 23; Sequens locus ibid. n. 15) anchored at *in duodecimo libro de Trinitate* in Cap. III tail; the note covers both Hilarius quotes there.
- **[^9]** (Psalm. 81, 6) anchored at *Filii Excelsi omnes* — direct scripture.
- **[^10]** (Exod. 4, 22) anchored at *Filius meus primogenitus Israel* — direct scripture. (OCR has *Exod. i, 22*; the printed Vulgate ref is normally Exodus 4:22; preserved as 4:22 silently fixing a likely OCR misread of `4` as `i`.)
- **[^11]** (A sola Vat. omittitur *filii Dei*) anchored at *fiunt enim filii Dei, non nascuntur filii Dei* — direct word match.
- **[^12]** (Num. 13; Hilarius variants) anchored at *in duodecimo libro de Trinitate* of Cap. IV's Hilary quote. (OCR fragment showed `Num. 1` in col-B — likely *Num. 13*; harmonized silently.)

### Scribal / OCR garbles silently corrected (new content, pp. 447–448)

- `DISTJNGTIO` → `DISTINCTIO`
- `Suflficiat` → `Sufficiat`
- `confltetur` → `confitetur`
- `dissenliunt` → `dissentiunt`
- `placel` → `placet`
- `raihi` → `mihi`
- `veuenum` → `venenum`
- `raelle` → `melle`
- `tra.nsfigurat` → `transfigurat`
- `alioquiu` → `alioquin`
- `ti'es` → `tres`
- `traclatu` / `traclatu` → `tractatu`
- `conimemoraviraus` → `commemoravimus`
- `hyposlasis` → `hypostasis` (passim)
- `seducerent` preserved
- `signiflcatio` → `significatio`
- `efflagilant` → `efflagitant`
- `subsistenles` → `subsistentes`
- `liypostasim` / `hyposlasim` → `hypostasim`
- `traclatu` → `tractatu`
- `sullicit` → `sufficit`
- `Auslin` / `Auguslinus` → `Augustinus`
- `Filinm` → `Filium`
- `triumpersonarum` → `trium personarum`
- `signiflcavit` → `significavit`
- `genilus ex Deo` → `genitus ex Deo`
- `flunl` / `flunt` → `fiunt`
- `Ililarius` → `Hilarius`
- `dislinguit` → `distinguit`
- `oslendens` → `ostendens`
- `iracundiac` → `iracundiae`
- `appellalioties` → `appellationes`
- `relaliones` → `relationes`
- `accidenta-les` (line break) → `accidentales`
- `imnnitabili-ter` (line break) → `immutabiliter`
- `incomrautabile` → `incommutabile`
- `seinper` → `semper`
- `propriiim` → `proprium`

### Editorial marginalia stripped (pp. 447–448)

Marginal labels `Hieronymus.`, `Augustinus.`, `Auaii^^^` (an OCR garble of an editorial marginal at line 2974), `Augi`, `Hilarius.`, `Auguslinus.`, `^"^''"`-style noise (right-margin artefacts e.g. line 3019), `dum accidens` running-fragment artefacts, the running header `448  SENTENTIARUM LIB. I.` at line 3000, and the page-breaking running header `DISTINCTIO XXVI.   449` at line 3114 were all dropped per CLAUDE.md OCR cleanup rules.

### Genuine `[?]` flags

None inserted. All readings sufficiently disambiguated by context.

## Post-fix corrections (2026-05-04, Wilson + Claude)

After head-fix agent run, manual review caught and corrected the following:

- **[^10]**: agent wrote `Exod. 4, 22` / `Exodus 4:22`. OCR (raw line 3089) has `Exod. i, 22` — roman numeral i = 1. **Corrected to `Exod. 1, 22` / `Exodus 1:22`.** Discipline note: agent appears to have made a contextual guess rather than a roman-numeral read.

- **[^12]**: agent reflowed `Num. 1` (col-B start, raw 3097) with `2. et 1 3` (col-B continuation, raw 3098) as `Num. 13` and shifted `12 et 13` into the editions list (`edd. 2, 3, 7, 8 et 12 et 13`). Correct reflow: `Num. 12 et 13; in quo textu solummodo edd. 2, 3, 7, 8 post *Vero* addunt *Deo*`. **Corrected.** Editions cited = 4 (2, 3, 7, 8), not 6.

- **`Num.` rendered as biblical "Number(s)"** in English for entries [^8], [^12], [^16], [^17]. In Quaracchi's NOTAE apparatus `Num.` = `numerus` = paragraph/section number of the cited authority (consistent with `n. 15`, `n. 13` used elsewhere in the same entries). **Corrected all four entries to render `Num.` as `n.`** in English (e.g., "n. 23" not "Number 23").
