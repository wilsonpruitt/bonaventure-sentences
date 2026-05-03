# d.22 dubia ambiguities

## Structural decision: QUINQUE REGULAE DE NOMINIBUS DIVINIS placement (priority: project-owner review)

The Quaracchi edition (Tomus I, p. 400) prints the block headed **QUINQUE REGULAE DE NOMINIBUS DIVINIS** as a centered, free-standing heading sitting between DUB. II and DUB. III. The dubia numbering itself runs I → II → III → IV without skipping a slot for the rules block.

PDF inspection (printed p. 400) confirms:
- `DUB. II.` is clearly labeled (OCR `DlfB. 11.` → `DUB. II.`).
- The QUINQUE REGULAE heading is typeset like a section heading, **not** like a dubium label (no `DUB.` prefix, no Roman numeral).
- `DUB. III.` follows immediately after the rules-block paragraph and continues the dubia sequence.

**Decision taken:** rendered as a separately-titled appendix-style subsection under `### Quinque Regulae de Nominibus Divinis`, not promoted to "DUB. II.5" or merged into DUB. II. Rationale: the printed edition treats it as a distinct rule-listing appendix to DUB. II rather than as a fresh dubitatio, and silently relabeling editorial structure would distort what the Quaracchi editors chose to set apart.

(Note: the original chunk-dispatcher prompt suggested DUB. II might be missing — that was a misreading of the OCR `DlfB. 11.` glyph cluster. DUB. II is in fact present and clearly numbered.)

## Footnote anchor positions

The Quaracchi apparatus for this chunk uses the standard apparatus-glyph sequence (`'`, `2`, `3`, `*`, `5`, `«`, etc.), but the OCR preserved only a few of the in-body marker glyphs. Anchors were placed by content-matching the apparatus entry to the variant it discusses:

- DUB. I — note 1 anchors at `quoniam`; note 2 at `trimembris` (cod. X variant about the immediate-members reading); note 3 at `divisiones` (Dist. 28 cross-reference); note 4 at `substantiae` (first occurrence of the mss-vs-Vat. *vel* split); note 5 at `personis ... vel` (second occurrence of the same vel/non-vel apparatus entry — entry actually shared with note 4 in the Quaracchi printing, but a marker is needed at both anchor positions); note 6 at `et ita` (Vat. omits *Et*, *ista* vs *ita*).
- DUB. II — note 7 at `Bernardus`; note 8 at `differt` (Vat. silent variant `differt` vs `deficit`); note 9 at `sed`; note 10 at `et` before `ideo`; note 11 at `quasi`.
- Quinque Regulae — note 12 at `de Trinitate`; note 13 at `quinque`; note 14 at `substantiam` (after the second rule); note 15 at `hoc` (final sentence about *missus*).
- DUB. III — notes 16–20 placed at OCR-marker positions (`dicamus`, `et ideo`, `retentum`, `Grammaticus`, `vel idem`).
- DUB. IV — notes 21 (`vel maior`) and 22 (`esse maius est`) on p. 400; notes 23 (`Deo autem`), 24 (`habet`), 25 (`per essentiam`) on the page-401 continuation.

Notes 4 and 5 cite the **same Quaracchi apparatus entry** (a single entry that explicitly mentions two anchor positions: "hic et paulo infra post *personis*"). To preserve marker-pairing and let the reader find the relevant variant at both anchor points, both markers point to the same apparatus text; note 5's English explicitly cross-references note 4. If the project owner prefers a different convention, this is the place to revise.

## Silent OCR fixes (no `[?]` flags raised)

- `esl → est` (multiple)
- `aul → aut`
- `sufficierites → sufficientes`
- `quoniam'` (apparatus marker glyph adjacent to word) → `quoniam` + `[^N]`
- `7>'m«to → Trinitas`
- `etita^ → et ita` + `[^N]`
- `DlfB. 11. → DUB. II.`
- `RESPONDt:o → Respondeo`
- `defieit → differt` (per apparatus note 8: Vat. reading is *differt*; OCR conflated)
- `coUectivo → collectivo`
- `nuUo → nullo`
- `iraportat → importat`
- `Sci-endum → Sciendum`
- `igilur → igitur`
- `fro-prie → proprie`
- `(iivinis → divinis`
- `cilur → citur` (`dicilur → dicitur`)
- `secunduin → secundum` (multiple)
- `oinne → omne`
- `ftum → dictum`
- `mme → mine` (`nomine`)
- `Quartaesiha.e( → Quarta est haec`
- `liis → his`
- `dica-mus° → dicamus` + `[^N]`
- `signiflcat → significat`
- `omnipotem → omnipotens`
- `noinen → nomen`
- `^foundu` (DUB. IV continuation) — dropped as a marginal-gloss bleed (`Fundamentum 2dae solutionis`); not a body word
- `mme → nomine`
- `participium '" → participium` + `[^N]`
- `vel " → vel` + `[^N]`
- `Grammaticus '% → Grammaticus` + `[^N]`
- `vel " idem → vel idem` + `[^N]`
- `albior vel maior " → albior vel maior` + `[^N]`
- `esse maius'^ → esse maius est` (the Quaracchi text per apparatus note 22 is *esse maius est dupliciter*; Vat. drops *est* — reading restored from the apparatus consensus)
- `subiecti at-tenditur → attenditur`
- `forraae → formae`
- `tanien → tamen`
- `essenliam → essentiam`
- `denominare per essenliam → denominare per essentiam`
- `excellit → excellit` (preserved)
- `participalione → participatione`

## Apparatus-side OCR fixes (silent)

Standard ligature/letter-substitution cleanup throughout the apparatus block: `ct → et`, `siibsiiwimus → substituimus`, `avtem → autem`, `loeo → loco`, `tainen → tamen`, `qmntum → quantum`, `dwendum → Dicendum`, `simiUtudo → similitudo`, `cilialione → conciliatione`, `praedicla → praedicta`, `slanllam → stantiam`, `addlt → addit`, `omittltur → omittitur`, `Va( → Vat`, `cd → ed`, `iit → ut`, `dlcimus / Dlclmus → dicimus`, `sic → sic`, `pio → pro`, `personls → personis`, `subslantia → substantia`, `peip-eram → perperam`, `singuiariter → singulariter`, `oinnia → omnia`, `Funda → (marginal gloss, dropped)`, etc.

No `[?]` flags raised in this chunk — all OCR garbles resolved by context + apparatus consensus.
