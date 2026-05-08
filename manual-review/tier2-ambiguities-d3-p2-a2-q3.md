# Tier-2 ambiguities — bon-sent-I-d3-p2-a2-q3

Rebuild date: 2026-05-08. Raw OCR lines 22914–23053 in `raw/bonaventure_vol1_raw.txt`. Print verification: 600-dpi vision pages `raw/vision/vol1/p-092.png`, `raw/vision/vol1/p-093.png`.

## Inline `[?]` flags

1. **Reply heading "1. 2." (printed p. 93, right column, ~mid-column).**
   The Quaracchi print has the heading "1. 2." over the combined reply on *amor*. The Scholion remarks that Bonaventure "secundum et tertium breviter solvit", i.e. he answers the second and third *Sed contra* objections. So the printed numerals "1. 2." disagree with the editor's own reading. This is plausibly a Quaracchi typesetting slip (or an inherited tag from an earlier edition). Preserved verbatim in Latin and English; flagged `[?]` so future readers know not to treat the numerals as authoritative.

2. **Apparatus `[^4]` — "Cod. I Y hic addunt *bene* et cum subnexis cohaerenter *in anima*."**
   The footnote prints two italic lemma additions, *bene* and *in anima*, with an unitalicized editorial parenthetical "et cum subnexis cohaerenter" between them. Most natural reading: codd. I and Y here add the word *bene* (after *mentem*) and — coherently with the following clause "et per *notitiam* in anima notitiam in Deo" — place the words *in anima* in this earlier slot as well. The English renders this reading literally and flags `[?]` because the exact scope of "bene" vs "in anima" as separate additions cannot be fully resolved from print alone.

## Silent OCR corrections

| OCR | Restored | Basis |
|---|---|---|
| `QU^STIO    III.` | `QUAESTIO III.` | Standard `^/A` and `S/E` glyph confusion in heading |
| `estorigo` | `est origo` | Word-break OCR loss |
| `ali uno` | `ab uno` | Standard `b/li` glyph confusion |
| `cuni` | `cum` | Standard `m/ni` confusion |
| `siue distiuctione` | `sine distinctione` | Standard `n/u` confusion in lower-case |
| `notilia` | `notitia` | Standard `t/l` confusion |
| `vei` | `vel` | Standard `i/l` confusion at line end |
| `flde` | `fide` | Standard `fl/fi` ligature confusion |
| `habelur` | `habetur` | Standard `t/l` confusion |
| `Trinitalem` | `Trinitatem` | Standard `t/l` confusion |
| `pro nega- siue` (marginal note) | dropped | Marginal gloss "Pro negativa" — editorial marginalia, not Bonaventure's text |
| `'p.^/'«` (marginal note) | dropped | Marginal gloss; not body text |
| `conciosio 2.` / `conoiusio 3.` (marginal) | dropped | Editorial scholion-tags `Conclusio 2`, `Conclusio 3` printed in margins, not body |
| `'  p.^/'«` (margin) | dropped | Marginal note |
| `1.2.` (heading) | `1. 2.` | Standard space-loss in heading |

## Print-restored content (OCR garbled)

The OCR rendered the column-break of the Respondeo as

> "per hanc trinita- / [blank] / est attribuendo"

The 600-dpi print clearly reads

> "per hanc trinita- (col break) -tem **contingit cognoscere Trinitatem in Deo, et hoc est** attribuendo ea quae..."

Restored verbatim from the print.

## Apparatus correction

The previous chunk's apparatus included an entry "Cod. Z addit *quod non valet*…" attached to "Ad illud quod obiicitur de amore" in this Q. III. That apparatus footnote is in fact entry №2 of the **p. 91** footer and comments on Q. II's "Ad illud quod obiicitur de ratione Augustini" (raw line 22855). Removed from this chunk.

The previous chunk was missing apparatus footnote №4 of the p. 93 footer ("Cod. I Y hic addunt *bene* et cum subnexis cohaerenter *in anima*"), which keys off *mentem* in the Respondeo. Restored.

Final apparatus count: 6 entries, matching the six numbered footnotes at the foot of p. 93.
