# Tier-2 ambiguities — bon-sent-I-d19-p1-dubia (2026-05-03)

## Resolution of the missing-Dub-VI/VII/VIII question
The user-prompt flagged that Dubs VI, VII, VIII appeared missing from a coarse grep of the OCR. They are present but very heavily garbled in the IA djvu OCR:
- raw line 61771: `DrB.  Vl.` → DUB. VI.
- raw line 61791: `DiiB.  VII.` → DUB. VII.
- raw line 61808: `Din.  VIIl.` → DUB. VIII.

All 11 dubia (I–XI) are present in the chunk and have been transcribed.

## Page-boundary correction
The header in the user prompt said pp.349–353 / PDF 451–455. Verification by `pdftotext`:
- p.350 (PDF 452) starts the dubia section ("DUBIA CIRCA LITTERAM MAGISTRI" + DUB. I).
- pp.349 / PDF 451 belong to q4 + scholion (not dubia).

Corrected `printed_pages: [350, 351, 352, 353]` and `pdf_pages: [452, 453, 454, 455]`.

## Footnote-attribution decision (p.350)
On printed p.350, footnotes 1–4 in the printed apparatus actually anchor in the q4 column-1 continuation of the previous chunk (they reference *consubstantialem*, *post Unde*, etc., which are q4 vocabulary). Only printed-fn 5 (`Vide supra pag. 342. nota 6.`) belongs to Dub I — anchored at *difficilior*. So Dub I has just one apparatus entry in this chunk (`[^1]`). The OCR mark `"` on `similitudinem"` was treated as italic-end / typographic, not a footnote anchor (consistent with Dub I context having only the single anchored variant note).

## `[?]` flags inline
1. **Footnote [^32], Latin**: rendered `*et*, quae[?] in Vat. deest.` — The OCR (raw l.448–449) breaks the Quaracchi note off mid-sentence at `quae` due to the page-bottom OCR artifact (`S. Bonav. — Tom. I.` running line). The full printed apparatus on PDF p.353 reads `quae in Vat. deest.` — preserved as a `[?]` because the OCR cut and the printed glyph cannot be 100 % verified without page-image confirmation. Reading `quae in Vat. deest` is high-confidence.

## Silent OCR fixes (representative; not all enumerated)
- `suhstantia` → `substantia`; `qitan-litate` → `quantitate`; `aho` → `alio`; `coaeternita- tem` → `coaeternitatem`; `inteUigendi` → `intelligendi`; `nuUa` → `nulla`; `In re-latione` → `In relatione`; `aetemita-tem` → `aeternitatem`; `infmitum` → `infinitum`; `comistit` → `consistit`; `iden` → `ideo`; `expoiiit` → `exponit`; `illnd` → `illud`; `siuiile` → `simile`; `Eiempiom` → `Exemplum`; `npex.` → (gloss; dropped); `inintelligibile` → `inintelligibile` (kept as in OCR — Bonaventure's contracted form `inintelligibile`); `lonui` → `loqui`; `intcHectus` → `intellectus`; `ahquid` → `aliquid`; `ahud` → `aliud`; `inflnitus` → `infinitus`; `a,ppreliendente` → `apprehendente`; `siCdeSrliwinr` (marginal gloss) dropped; `genei'at` → `generat`; `fllium` → `filium`; `perfeetum` → `perfectum`; `receptioncTn` → `receptionem`; `restaurationera` → `restaurationem`; `duplicein` → `duplicem`; `essemli` → `essendi`; `excliidat` → `excludat`; `Fdio` → `Filio`; `bed` → `Sed`; `msi` → `nisi`; `coniunclionem` → `coniunctionem`; `simiiitudinem` → `similitudinem`; `indiflerentem` → `indifferentem`; `cratura-rum` → `creaturarum`; `iitteram` → `litteram`; `subiun-git` → `subiungit`; `corimiunem` → `communem`; `naiu-ram` → `naturam`; `pjuribus` → `pluribus`; `Degeneratio` (margin gloss) dropped; `dissimilitudinera` → `dissimilitudinem`. Marginal gloss tags (e.g. `Eiempiom npex.`, `intcHecms compreliori- ens.`, `iripimiei.`, `iu diciiur sitio /(/ ant`, `Solutio quorundam.`, `Alia solutio.`, `Degeneratio in tribus modis.`) were stripped per CLAUDE.md `OCR cleanup rules`.

## Apparatus translation notes
- Where the apparatus quotes a Latin codex variant in italic, the English version retains the variant in italic and only translates the surrounding scholarly framing.
- `Enarratio in Psalm.` (fn [^15]) was translated literally including the long Augustine quotation.
- Cross-references (`d. 3. p. I. q. 1. ad 1`; `II. Sent. d. 24. p. I. a. 2. q. 4`; etc.) preserved in expanded form.
