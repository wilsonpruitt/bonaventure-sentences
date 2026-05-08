# Tier-2 ambiguities — d.1, a.2, q. unica (*Utrum frui sit actus voluntatis*)

Promotion from "first-pass vision" to Tier 2 on 2026-05-07. Latin re-set verbatim from raw IA djvu OCR (`raw/bonaventure_vol1_raw.txt`, lines 14178–14534).

## Status

No `[?]` flags were inserted in the chunk body itself. The OCR for these three pages (pp. 35–37) is clean enough that every word of Bonaventure's body text and of the Scholion could be transcribed without inventing Latin.

The few places where the OCR was visibly corrupted are routine and were silently corrected per the CLAUDE.md "OCR cleanup rules":

- `tttiMj` (line 14183) → *utibili* (Quaracchi has *uti* and *utibili* in immediate parallel; *utibili* is the only word that fits both syntax and the doctrinal pair *uti / utibile*).
- `/"rtti` (line 14184) → *frui*.
- `fnd` (line 14200) → *frui*.
- `f7-ui` (line 14267), `7-ui` (line 14304) → *frui* / *frui*.
- `prop?7'e` (line 14334) → *proprie*.
- Foot-note marker glyphs (single quote / asterisk / caret / superscript digits) → numbered `[^N]` markers in OCR-attested positions.

## Apparatus-side cleanups (no `[?]` left in the chunk)

- The page-35 footer block (raw lines 14211–14253) contains a continuation footnote from the *previous* question (a.1, q.4: *versitatem in finem cum delectatione…*) followed by footnotes 1–8 of page 35. Of those, only footnotes 7 ("*Vide lit. Magistri, c. 2.*") and 8 ("*Cfr. lit. Magistri, c. 2.*") attach to anchors inside this chunk. They become the chunk's [^1] and [^2] respectively.
- The page-36 footer (raw lines 14356–14413) supplies the chunk's [^3]–[^14].
- The page-37 footer (raw lines 14537–14574) supplies the chunk's [^15]–[^23].
- Footnote-anchor placement in the body follows the OCR's visible spacing, e.g. `fruitione  delectamur  ^` → `fruitione delectamur[^4]`.

## Anomalies worth recording (resolved, not flagged)

1. **Augustine, *De Trin.* X reference numbering.** OCR p. 35 footer (footnote 8 of that page → chunk [^2]) gives `Cfr. lit. Magistri, c. 2.` with no further Augustine reference; the Vatican-style reference *De Trin. X, c. 11, n. 17* is supplied in the apparatus from the parallel passage cited later in the Scholion's *De Trin.* citations and from the standard Maurist numbering. No textual conjecture; only a bibliographic completion.

2. **Two distinct Vatican-edition variants on the *frui non definitur per…* paragraph.** Footnote [^14] flags the Vatican's *resolutio* / *consuevit* / *dilectionis* triplet, and [^15] flags a separate Vatican repunctuation that fuses the question with the answer ("*delectationis, cum haec quaestio fundata sit super falsum*"). Both are standard Quaracchi notes, transcribed verbatim from OCR.

3. **The Scholion's *Caietano* parenthetical.** OCR has `(ad S. I. II. q. 1. a. 1.)`; this expands to "on Cajetan's commentary on Aquinas, *Summa theol.* I–II, q. 1, a. 1." The English Scholion renders it tersely as "on *S.[umma]* I–II, q. 1, a. 1" without the bracketed `theol.` to preserve the Quaracchi compactness.

## Open items for a future polish pass

None. Chunk is ready for the d.1–d.10 cleanup track.
