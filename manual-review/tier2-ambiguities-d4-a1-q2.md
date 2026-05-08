# Tier-2 ambiguities — bon-sent-I-d4-a1-q2

Rebuild date: 2026-05-08. Raw OCR lines 23974–24227 in `raw/bonaventure_vol1_raw.txt`. Promoted from "first-pass vision re-OCR reconciled" to canonical Tier 2.

## `[?]` flags inline

| Location | OCR | Currently rendered | Note |
|---|---|---|---|
| Apparatus fn 2 (Latin) | `(auTS)` | `(αὐτῷ [?])` | OCR garbled the Greek; printed text needs eyes-on PDF to confirm exact accenting / breathing of *autōi*. |
| Apparatus fn 16 (Latin) | `(oxuteu?)` | `(σκυτεύς [?])` | OCR garbled the Greek transliteration; printed text needs eyes-on PDF to confirm spelling of *skuteus*. |

Both Greek glosses are best-effort reconstructions from the OCR's Latin transliteration; verify against the print before publication.

## Silent OCR corrections

| OCR | Restored | Basis |
|---|---|---|
| `QU.ESTIO II.` | `QUAESTIO II.` | Standard heading garble (cf. d.1, d.2) |
| `Deuni` | `Deum` | Standard `m → ni` glyph confusion at end of word |
| `Deus genuil alium Deum` | `Deus genuit alium Deum` | `t → l` confusion in CONCLUSIO heading |
| `aiietas` | `alietas` | `l → i` confusion |
| `distinctio-nem` (line break) | `distinctionem` | line-wrapped word |
| `suhstantive` | `substantive` | `b → h` confusion |
| `ut^` | `ut` | OCR superscript marker bleed; `,` between `substantive` and `ut` is the apparatus break, not part of text |
| `(1 verbum simpli( / ctionem` | `verbum simpliciter importans distinctionem` | OCR mangled the line; reconstruction is the standard Quaracchi formula and matches surrounding context (`Et ex hoc est, quod non sequitur ad verbum simpliciter importans distinctionem; et sic patet primum`). |
| `IVIaximinum` | `Maximinum` | OCR letter-cluster confusion |
| `loannem` / `loannes` | `Ioannem` / `Ioannes` | Standard `I → l` substitution |
| `recipiunlur` | `recipiuntur` | `t → l` confusion |
| `omitlunt` | `omittunt` | doubled-letter OCR error |
| `omiltunt` | `omittunt` | same |
| `subiecium` | `subiectum` | `t → i` confusion |
| `substantimm` | `substantivum` | OCR letter-pile confusion |
| `dicil` | `dicit` | `t → l` confusion |
| `nnus` | `unus` | `u → n` doubled |
| `flne` | `fine` | `i → l` confusion |
| `n. II` | `n. 11` | OCR Roman-numeral / arabic confusion in fn 13; Tract. 14, n. 11 of Augustine's *In Joannem*. |
| `sumtum` | `sumtum` | preserved as-is (Quaracchi orthography for *sumptum*) |
| `aT'tiuni` | `artium` | OCR ligature break |
| `pajulo` | `paulo` | OCR letter-cluster |
| `simpli(`/`(c.   4.)` punctuation | normalized | column-break artifacts; meaning unambiguous |

## Paraphrase departures fixed (vs prior "first-pass vision" version)

The prior chunk was AI-translated rather than transcribed. Pass-2 corrections:

1. **Footnote-anchor for fn 4 was misplaced** in the Latin and English bodies. Prior: `*alius* est terminus masculini generis[^4]; sed terminus masculini generis stat pro persona`. OCR places the apparatus marker `*` between *generis* and *stat* in the SECOND occurrence (`sed terminus masculini generis * stat pro persona`), and the apparatus entry itself glosses the variant `qui loco sed terminus masculini generis`, confirming. Marker moved to: `... terminus masculini generis; sed terminus masculini generis[^4] stat pro persona ...`. Mirrored in English body.

2. **Apparatus delimiter format** — prior used non-canonical `**La** — ` ... `<br>` ... `**En** — ` (with em-dash and `<br>` break). Corpus standard since d.10 (and required by `build-content.mjs` parser per CLAUDE.md) is `**La.**` (period) + newline + 5-space-indented `**En.**`. All 17 entries reformatted; no content shortened.

3. **Aristotle citation form modernized in fn 2 and fn 16.** Prior: `Arist., De Anima II, text. 47 (c. 4)` and `Arist., Periherm. II, c. 2 (c. 11)`. OCR-verbatim Quaracchi form: `Aristot., II. de Anima, text. 47. (c. 4.)` and `Aristot., II. Periherm. c. 2. (c. 11.)`. Restored to OCR form per "Latin verbatim from OCR, not paraphrase" rule. English unchanged (citations modernize naturally in translation).

4. **fn 1 English** — prior translated `in Proslogio` as "*in the* Proslogion" (italic + article). Restored to `*in* Proslogio` matching the Latin's italic on the preposition+title pair, since the apparatus gloss is about the false attribution string, not the work itself.

5. **fn 13 punctuation** — restored Quaracchi's terminal periods after numerals (`c. 2. in fine; et super Ioannem, c. 3. Tract. 14. n. 11`). Body number `II` → `11` (corrected OCR Roman/arabic).

6. **fn 16 cross-reference** — restored Quaracchi's `d. 2. q. 1. ad 1.` form. English-side comma form (`d. 2, q. 1, ad 1`) preserved as natural translation.

## Structural anomalies

- The Respondeo's last sentence comes through OCR as `Et ex hoc est, quod non sequitur ad / (1 verbum simpli( / ctionem ; et sic patet primum.` — the leading `(1` and the parenthetical-glyph spray are scanner-bleed from the marginal note `(1` (i.e. `1.` indent marker for the Respondeo's numbered solutions). Reading: `Et ex hoc est, quod non sequitur ad verbum simpliciter importans distinctionem; et sic patet primum.` Standard Quaracchi formula; not flagged `[?]`.
- **Implicit Ad 1.** The Respondeo's final `et sic patet primum` ("and thus the first is clear") substitutes for an explicit `Ad 1.` reply. This is a Bonaventuran convention; documented in Notes.
- Marginal Quaracchi side-notes interleaved through OCR (`Fundameaui.`, `opinio ob-`, `Reprobatur.`, `conciusio.`, `Reeuia communis`, `Alia regula`, `Tres species vocabulorum in divinis`, `solutio ad obiecta`) are editorial gloss-tags, not Bonaventure text; trimmed per OCR-cleanup rules.
- Scholion header `CHOLIOE` (line 24205) is OCR garble of `SCHOLION`.
