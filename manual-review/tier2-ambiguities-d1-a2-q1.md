# Tier-2 ambiguities — d.1, a.2, q. unica (*Utrum frui sit actus voluntatis*)

## 2026-05-10 from-scratch rebuild (d.1-d.10 rechunk pipeline)

Latin re-set verbatim from raw IA djvu OCR (`raw/bonaventure_vol1_raw.txt`, lines 14178-14534). Fresh literal English translation. Apparatus rebuilt per CLAUDE.md "every numbered Quaracchi footer entry in the raw range, page by page" — 31 entries total (p. 35 = 8, p. 36 = 14, p. 37 = 9).

### Marker mapping

- p. 35 body anchors: [^1] (after *amore inhaerere etc.*, OCR raw line 14198), [^2] (after *in sequenti*, line 14207). Footnotes 3-8 of p. 35 attach to text above this chunk's start (the prior chunk's tail visible at lines 14211-14220 carries those anchors) but are still rendered in full to preserve the printed-page footer block.
- p. 36 body anchors: [^9]-[^22] mapped to OCR raw lines 14259, 14263, 14270, 14285, 14288, 14292, 14295, 14305, 14318, 14320, 14329, 14347, 14351, 14353.
- p. 37 body anchors: [^23]-[^31] mapped to OCR raw lines 14428, 14432, 14436, 14439, 14440, 14456, 14460, 14467, 14473.

### Silent OCR corrections (per CLAUDE.md "OCR cleanup rules")

- `tttiMj` (line 14183) → *utibili*.
- `/"rtti` (line 14184) → *frui*.
- `fnd` (line 14200) → *frui*.
- `deflnitionibus` (line 14206) → *definitionibus*.
- `deflnit` (line 14329) → *definit*.
- `deflnitur` (lines 14331, 14336, 14352, etc.) → *definitur*.
- `f7-ui` (line 14267) → *frui*.
- `prop?7'e` (line 14334) → *proprie*.
- `propriissime` (line 14339) preserved as-is.
- `notifieatione` (line 14423) → *notificatione*.
- `consimili` (line 14398) preserved.
- `fldem`, `flde` (multiple) → *fidem*, *fide*.
- `flnis` (line 14476) → *finis*.
- `flne` (line 14497) → *fine*.
- `coniugitur` / `coniunctur` variants resolved to *coniungitur* where Quaracchi syntax demands.
- `(t descen-` (line 14561) → opening quotation mark before `descendit omne meritum hominis` (Quaracchi guillemets).
- `«` and `»` preserved as-is per CLAUDE.md.
- The half-page-bleed marginal `Ad opposi-/torum` glosses (lines 14276, 14438) and `condusio 1/2`, `oppositorum.`, `soiutio op-`, `Tres modi`, `Nonappro-`, `goimio ai-`, `patct tertia quaestio`, `opinioquo-`, etc. running-head fragments are trimmed as Quaracchi marginalia, not Bonaventure's body.

### [?] flags

None in body. One semi-ambiguous spot:

- **line 14336, `et"` between *delectationem* and *hoc modo definitur*.** OCR shows a stray quote-mark glyph here. Treated as OCR noise rather than as a footnote anchor: the 14 footer entries on p. 36 are exhausted by the 14 unambiguous anchors at lines 14259, 14263, 14270, 14285, 14288, 14292, 14295, 14305, 14318, 14320, 14329, 14347, 14351, 14353. Resolution: silently dropped. → Verify against 600-dpi PDF in the next d.1-d.10 polish pass.

### Apparatus-side notes

- The p. 35 footer block raw lines 14211-14220 are the tail of a footnote belonging to the prior chunk (a. 1 q. 4); not rendered here.
- Page-36 footer [^22] ("Vat. cum cod. cc, mutata interpunctione...") is anchored to *Tamen* at line 14353 — verified by the footer's own gloss *posito cum pro Tamen*.
- Page-37 footer [^26] (Augustine *de Trin.* XV) and [^27] (Anselm *de Concordia*) preserve the Quaracchi book/chapter compactness in the English rendering.

## Prior (2026-05-07) log entries

Preserved below for cross-reference; the 2026-05-10 from-scratch rebuild supersedes the earlier 23-entry apparatus with a fuller 31-entry per-page rendering per the CLAUDE.md guidance.

- The 2026-05-07 pass rendered only the apparatus entries with anchors inside this chunk (23 total), counting only footer items 7-8 of p. 35.
- The 2026-05-10 pass renders every numbered Quaracchi footer entry in the OCR raw range, page by page, including p. 35 footer items 1-6 whose anchors fall above this chunk's start in the same printed-page footer block.
