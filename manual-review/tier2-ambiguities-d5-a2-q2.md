# d.5 a.2 q.2 — Tier-2 ambiguities (2026-05-10 d.1-d.10 rechunk pipeline rebuild)

## Page-118 footer block missing from OCR

The IA djvu OCR for raw lines 26786-26998 contains the full p.117 footer block (7 entries, lines 26871-26900) but does NOT contain a separate p.118 footer block. The body of p.118 (raw lines 26906-26972, plus scholion 26975-26996) contains 6 footnote-anchor markers (apostrophes and carets) which require apparatus entries that are not in the raw OCR. The next visible footer block in the OCR (lines 27021-27046) belongs to p.119 (DUBIA section), not p.118.

Six `[?]` placeholders have been inserted as `[^8]` through `[^13]`, anchored at the OCR marker positions. Each placeholder records the body location and OCR line of its anchor.

- **d5-a2-q2, body Respondeo `propagationem...plurium`** (raw line 26910): apostrophe marker after *plurium*. → `[^8]` placeholder. Resolve via 600dpi PDF read of printed p.118 footer.
- **d5-a2-q2, body Ad 1 `naturam communem`** (raw line 26928): apostrophe marker after *naturam*. → `[^9]` placeholder. Resolve via PDF.
- **d5-a2-q2, body Ad 2 `ostensum est`** (raw line 26941): apostrophe marker after *ostensum est*. Likely cross-reference to d. 4, q. 4 or to d. 5, a. 2, q. 1. → `[^10]` placeholder. Resolve via PDF.
- **d5-a2-q2, body Ad 2 (alia solutio) `distinguitur in suppositis`** (raw line 26953): apostrophe marker after *distinguitur*. → `[^11]` placeholder. Resolve via PDF.
- **d5-a2-q2, body Ad 3 `substantiam facit communem`** (raw line 26960): caret marker after *communem*. → `[^12]` placeholder. Resolve via PDF.
- **d5-a2-q2, body Ad 4 `datio dicit auctoritatem`** (raw line 26970): caret marker after *datio*. → `[^13]` placeholder. Resolve via PDF.

## Genuinely ambiguous OCR readings

None this rebuild — every footer entry that is present in the OCR (entries 1-7 for p.117) parsed cleanly. The gap is a structural OCR omission of the p.118 footer band, not in-line OCR garble.

## Body fidelity vs. prior chunk

The 2026-04-13 chunk had paraphrased Latin in places and only 5 apparatus entries (an English-curated subset). The Latin body has been re-set verbatim from the IA djvu OCR. Notable differences from prior chunk:

- Title: *substantia sive essentia* → *substantia sive essentia divina* (per OCR line 26789).
- Contra-2: restored *appropriandi et individuandi* (prior had only *appropriandi*).
- Conclusio: restored *Essentia divina per generationem communicatur, quia per generationem fit, ut sit in pluribus una* (prior had a paraphrased "verissime substantia vel essentia..." form lifted from later in the Respondeo).
- Respondeo: restored *sed tamen actu communicatur per propagationem plurium* (prior had collapsed this clause into the modern editorial reconstruction "but its being actually communicated in many is only through that which multiplies or pluralizes the supposits").
- Ad 2 (alia solutio): restored *Sed quaedam natura est, quae distinguitur in suppositis... in divina solum communicandi* (prior chunk dropped this entire closing distinction).
