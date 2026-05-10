# Tier-2 ambiguities — bon-sent-I-d1-a1-q1

Rebuild date: 2026-05-10 (d.1-d.10 rechunk pipeline from-scratch). Raw OCR lines 13383–13668 in `raw/bonaventure_vol1_raw.txt`.

## Inline `[?]` flags

| Location | OCR | Currently rendered | Resolve with |
|---|---|---|---|
| Scholion p.32 — opening | `' niiliiiui scholasdci siitis conscntiiiiU.` | `Plurimi[?] scholastici satis consentiunt` | Eyes-on 600dpi PDF p.32 footer. Reading is highly confident from context (typical Quaracchi scholion opener) but glyphs are badly garbled. |
| Scholion p.32 | `'l !i. in tiiic.` | `[hic][?] q. in fine` | Garble of "hic q. in fine" or similar Scotus locus formula. PDF eyes-on needed for exact wording. |
| Scholion p.32 | `nicharil. a Metl.` | `[Richard. a Med.][?]` (Richard of Mediavilla) | OCR-garbled author abbreviation; standard scholastic doxology context confirms Richard of Mediavilla but glyph-level Latin abbreviation is illegible. PDF eyes-on. |
| Scholion p.32 | `R., hic a. 1. piincipalis q. 3.` | `[...][?], hic a. 1 principalis q. 3` | Author abbreviation lost in OCR (only trailing "R." survived); likely "Petrus de Tarantasia" or similar. PDF eyes-on. |
| Scholion p.32 | `hic q. 1.` after Dionys. Carth. listing, separate clause | `[...][?] hic q. 1` | Author of trailing clause lost in OCR; clause continues "qui doctrinam S. Bonavent. breviter repetit". PDF eyes-on. |
| Apparatus [^7] p.30 fn 7 | `Comment. in Rhetor. Ciceronis, 1. c.` (split lines 13477–13483) | `Comment. in Rhetor. Ciceronis, l. c. [?]` | OCR break across lines 13477–13483 fragmented the citation; "1. c." is plausibly "loc. cit." but ed./section number lost. PDF eyes-on. |

## Silent OCR corrections (standard)

| OCR | Restored | Basis |
|---|---|---|
| `QU.ESTIO I.` | `Quaestio I.` | Standard heading garble |
| `oninis` | `omnis` | Standard `n/m` confusion |
| `Fnndamcni.-i.boniis ^` | `bonus[^2]` | Marginal-gloss bleed (*Fundamenta* margin); `boniis` for `bonus` standard double-`i`/`u` |
| `voluntalis` | `voluntatis` | Standard `t/l` confusion |
| `u^uni` | `usum` | Standard `s` glyph garble |
| `veiit` | `velit` | Standard `i/l` confusion |
| `ehci-tus` | `elicitus` | Standard line-break with `h/l` confusion |
| `scilicel^` | `scilicet` | Standard `t/l` |
| `vohmtatis` | `voluntatis` | Standard `m/un` |
| `quietativum` | `quietativum` | OK |
| `divlditur` | `dividitur` | Standard `i/l` |
| `coUrd.` | `contra` | Standard `nt/U` confusion |
| `A'enerit` | `venerit` | Standard `v/A'` glyph |
| `inuhipli-cis` / `mulhpUcis` | `multiplicis` | Standard `lt/h` confusion |
| `lo-quendo` (split) | `loquendo` | Line break |
| `soimioop-posiiorum` (marginal) | "Solutio oppositorum" — marginalia, not body | Marginal gloss bleed |
| `obiicitur` | `obiicitur` | OK (medieval orthography) |
| `aiiquid`, `aiiud`, `aiio` | `aliquid`, `aliud`, `alio` | Standard `l/i` confusion |
| `ahquid`, `ahud` | `aliquid`, `aliud` | Standard `li/h` ligature confusion |
| `conciusio %` (marginal) | "Conclusio" — marginalia, not body | Marginal gloss bleed |
| `Auyustinus` | `Augustinus` | Standard `g/y` |
| `dkii` (in apparatus [^22]) | `dicit` | Standard `c/k` and dropped `t` |
| `Boetliium` | `Boethium` | Standard `h/li` ligature |
| `tlieologica` | `theologica` | Standard `h/li` ligature |
| `eirca` | `circa` | Standard `c/e` |
| `Vietorini` | `Victorini` | Standard `c/e` |
| `definilio ums` | `definitio usus` | Standard cluster garble |
| `praenotatis` | `praenotatis` | OK |
| `exercitaiionis` | `exercitationis` | Standard `t/i` |
| `conlinuatio` | `continuatio` | Standard `t/l` |
| `c. 2S.` | `c. 28.` | Standard `8/S` digit-letter confusion |
| `habitm` | `habitus` | Standard cluster garble |
| `relattie` | `relatae` | Standard glyph garble |
| `venetit` | `venerit` | Standard `r/t` |
| `commuimsime` | `communissime` | Standard `n/m`/`ss` cluster |
| `polentiae` | `potentiae` | Standard `t/l` |
| `tritms` | `tribus` | Standard `b/tm` |
| `duolms` | `duobus` | Standard `b/lm` |
| `manifeste` | `manifeste` | OK |
| `propriissime` | `propriissime` | OK |
| `vohmtatis` / `votetafe` | `voluntatis` | Standard double-garble |
