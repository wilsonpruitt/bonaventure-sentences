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
