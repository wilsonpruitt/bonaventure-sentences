# d.35 dubia — Tier-2 ambiguities

Source: `vol1/bon-sent-I-d35-dubia.md`. OCR raw lines 19688–19945 of `raw/bonaventure_vol1_pt2_raw.txt`.

## Flagged

- **bon-sent-I-d35-dubia, DUB. VI Respondeo**: OCR reads `quia ^Dupies` (with marginal gloss `Duplex ratio`) at the start of the response. The OCR garbles the running gloss into the body. Currently rendered: *quia duplici ratione[?]: actu cognoscit...* → Resolve by 600dpi PDF eyes-on at p. 616 (PDF p. 206) to confirm whether *duplici ratione* is body text or a marginal/scholion gloss; the parallel "ex hac duplici causa" at the end of the same paragraph supports keeping it.

- **bon-sent-I-d35-dubia, page numbering**: OCR shows running head `DIST. XXXV. DUBIA. 613` mid-flow at raw line ~19773 (preview line 86), implying the dubia begin on printed p. 613, not p. 614 as originally framed in this chunk's frontmatter. Updated `printed_pages` to [613, 614, 615, 616]; `pdf_pages` to [203, 204, 205, 206]. (Note: pt2 PDF offset is printed − 410, so 613 → 203, 616 → 206.) → ACCEPT pending PDF check.

- **bon-sent-I-d35-dubia, DUB. III Respondeo, "Vel sic..."**: OCR at this point is heavily garbled: `Vel sic: aut ' dicit cognitionem simplicem ... per rationem nobilissimam. Primo modo scientia, secundo modo sapientia.` Rendering preserves OCR but the doubled "scientia / sapientia" pair (after the prior speculatio/affectio split) reads as a parallel re-statement; cf. apparatus note ⁹ (Vat. addit *per appropriationem*) which suggests minor variant. → ACCEPT.

- **bon-sent-I-d35-dubia, DUB. IV apparatus alignment**: footnote anchors [^10]–[^15] in DUB IV are placed at semantically appropriate points (et bene, sex generum, Boethii de Trin., Magister, praecessionem, calumniam) but the OCR's superscript markers in the 2-column layout were partially illegible; spacing inferred from semantic + apparatus content. → ACCEPT pending PDF check.

- **bon-sent-I-d35-dubia, DUB. II Respondeo, "potentiae"**: OCR shows `potentiae".` with stray quote — Quaracchi italicizes *potentiae* here as the term being defined. Rendered as plain *potentiae* italicized. → ACCEPT.
