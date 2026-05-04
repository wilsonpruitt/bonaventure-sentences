# Tier-2 ambiguities — bon-sent-I-d24-a1-q1

Source: `raw/bonaventure_vol1_pt2_raw.txt` lines 355–686. Printed pp. 420–422.

No `[?]` flags raised in the chunk. The chunk is technically clean of unresolved Latin readings; the OCR garbles below were silently corrected per CLAUDE.md §"OCR cleanup rules" (resolved unambiguously by context, the parallel Quaracchi printing conventions, and cross-checking against the in-OCR running heads).

## Silent corrections of OCR garbles (logged for transparency)

- `Pliilosophus` → `Philosophus` (printer-ligature corruption; multiple occurrences)
- `Melapliysicara` → `Metaphysicam`
- `principiura`, `principiurn` → `principium`
- `coraplementum`, `compleraentum` → `complementum`
- `unimi` → `unum`
- `unnra` → `unum`
- `numerura` → `numerum`
- `secundura`, `dicendura` → `secundum`, `dicendum`
- `raagis`, `mss. raagis` → `magis`
- `Iterum *` body marker for "neither relatively" objection retained as `[^5]` (citation to *Categories*).
- `liaec`, `liabet`, `liabeantur` → `haec`, `habet`, `habeantur` (initial-h confusion)
- `lioc`, `lioc est` → `hoc`, `hoc est`
- `mnlta` → `multa`
- `dicitw` (footer ¶) → `dicitur` (in apparatus quotation about *Unitas autem in substantia*)
- `notiflcari`, `notificari` retained → `notificari`
- `multi-tiidinem`, `multitiidinem` → `multitudinem`
- `relaUva`, `relaUve`, `relaUvorum`, `posiUve`, `posiUvum`, `acUveritas` patterns → `relativa`, `relative`, `relativorum`, `positive`, `positivum` (the OCR systematically substitutes `U` for `ti` in the scholion)
- `ponilur` → `ponitur`
- `connumerabilis` retained as in OCR
- `respe-ctus` line break joined → `respectus`
- `ductum`, `eflicitur` → `ducatur`, `efficitur`
- `definUio`, `deflnitio` → `definitio`
- `intenUo`, `intenUi` → `intentio`, `intenti`
- `disposiUo`, `disposiUonem` → `dispositio`, `dispositionem`
- `conUnuum`, `conUnuitate` → `continuum`, `continuitate`
- `posiUUvae`, `posiUvae` → `positivae`
- `commenU` retained with parenthetical gloss `(commentatoris)` per OCR
- `videatur ^` body marker resolved to `[^15]` mapping to `Vat. cum solo recentiore codd. cc habeatur` (the variant `videatur` vs. `habeatur`)
- Greek snippet in fn 13 (`καὶ τῆς στερήσεως πρότερον ἡ κατάφασις`) reconstructed from OCR garble `y.aX t^? cT6p:^a£M? TipoTEpov ?] xaiitfaais (affirmatio)`. Confidence: high (Aristotle, *De Caelo* II.3, standard text).
- Footer markers `'`, `^`, `*`, `°`, `"`, `‘» ` mapped to numbered apparatus by content rather than by glyph, since OCR scrambles the marker glyphs unsystematically across the two-column footers. Mapping decisions:
  - `et illa constituit "` → fn 14 (`Sub hoc respectu Dionys… Non enim est multitudo non participans uno`) on grounds that the Dionysius cite supports objection 4's "one is preserved in many" claim.
  - `privative dicitur ^` (respondeo, ad rationem intelligendi) → fn 17 (Aristot. X *Metaph.* text 9, *Dicitur autem ex contrario ipsum unum*) — fits the via-posteriora epistemic claim.
  - `eorum opposita privative` → fn 18 (Aristot. text 1, *Item unius quidem est… idem, simile et aequale*) — direct match to identitas/aequalitas/similitudo triple.
  - `sic dicit positionem` → fn 19 (Aug., *Vis ipsa formae commendatur nomine unitatis*) — direct match form-confers-unity.
  - `aliquando privative etiam secundum rem` → fn 20 (`In Vat. desideratur etiam`) — textual variant on *etiam*.

## Notes for future verification

- OCR pages 420–422 use a heavy two-column body with two-column footnote footers; marker glyphs are degraded. A re-OCR or PDF cross-check would harden the marker-to-footer mapping above.
- The Magister-Lombard reference "in littera" at the start of the *Respondeo* is verified against d. 24 *littera* in pt2 (separate chunk).
- `concernit tempus` final line has the implicit subject change (intellect concerns time when it understands divisible/distinct things). Translation preserves Bonaventure's elliptical phrasing.
