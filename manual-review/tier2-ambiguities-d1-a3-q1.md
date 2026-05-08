# Tier-2 ambiguities — `bon-sent-I-d1-a3-q1`

Logged at the 2026-05-07 promotion from "first-pass vision re-OCR reconciled" to Tier 2.

Source: `raw/bonaventure_vol1_raw.txt` lines 14580–14818 (printed pp. 38–39 = PDF pp. 140–141).

## Anchor placements not visually confirmed at hi-res

These were placed by lemma-reasoning against the apparatus content, not by direct match to marker glyphs (which the IA djvu OCR represents as `'`, `^`, `°`, `*`, etc., often inconsistently, and which sit at small point size in the printed page).

- **bon-sent-I-d1-a3-q1, Ad 1 (p. 39):** `[^11]` placed at *quia unum factum est propter alterum* — apparatus says *Cod. X hic repetit unum*. Plausible but not glyph-confirmed.
- **bon-sent-I-d1-a3-q1, Ad 1 (p. 39):** `[^12]` placed at *ubi est sensus* — apparatus says *Codd. W X Z adiungunt ibi, et mox cod. A post sequitur repetit delectatio*. The "ibi" addition fits at *ubi est sensus [ibi]*; the *delectatio* repetition would anchor a few words later. One-mark-for-two-lemmata is plausible Quaracchi practice but not confirmed.
- **bon-sent-I-d1-a3-q1, Ad 2 (p. 39):** `[^13]` and `[^14]` placed adjacent at *non tristatur in excellenti[^13][^14]*. The OCR shows two glyphs at this spot but their order is not reliably distinguishable. `[^13]` is the manuscript-variant footnote (Cod. X *etiam*, aa/bb *spiritualis*, A C G I L S T U W omit *in*, R/ff *ab*, bb *ex*); `[^14]` is the De Anima cross-reference (II.123/143; III.4/7). The De Anima reference may actually anchor a few sentences earlier (at *non est simile de intelligere et sentire* or at the end of the *Ex parte virtutis apprehensivae* paragraph) rather than at *excellenti*; small-point glyphs in the OCR cannot resolve this.

## Resolution

Either RESOLVE with a 600 dpi PDF eyes-on pass, or formally ACCEPT-ILLEGIBLE. To be folded into the next decade-polish pass alongside any d.1–d.10 anchor-position residuals when those are run.

## Other notes

- The chunk's prior `[^17]` merged two distinct apparatus entries from the OCR. Now split as `[^17]` (Cod. cc *scilicet quantum* pro *secundum quod*, anchoring at *secundum quod* in Ad 3) and `[^18]` (Codd. F et I *qui*, cod. T *quia*, anchoring at *quae* in *ultimo fini, quae maxime habet finiendi rationem*). No `[?]` on this — the lemmata are clear from the apparatus text itself.

- No Latin was invented and no English was paraphrased to "recover" from OCR difficulty. The Latin body matches the IA djvu OCR verbatim modulo standard OCR-substitution corrections (`flni → fini`, `flniendi → finiendi`, `inflnitum → infinitum`, `partieipationem → participationem`, `colhgitur → colligitur`, `immateriahs → immaterialis`, etc.) where context makes the intent unambiguous.
