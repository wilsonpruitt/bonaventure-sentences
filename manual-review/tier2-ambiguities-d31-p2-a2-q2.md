# d.31 p.2 a.2 q.2 — Tier-2 ambiguities (2026-05-06)

Chunk: `vol1/bon-sent-I-d31-p2-a2-q2.md`
Raw range: `raw/bonaventure_vol1_pt2_raw.txt` lines 12964–13131
Printed pp. 546–548 (PDF pp. 136–138).

## Inline `[?]` flags

1. **Scholion I, "quae conformitas[?] potest esse triplex"**: OCR reads `quac conformiias neutra potest esse triplex`. The token `neutra` is suspect (`neutra` = "neither" makes no syntactic sense after `quae conformitas`); plausibly a printer's gloss or an OCR mangle of e.g. `vero` or another adverb. Currently rendered with `[?]` and the suspect token elided. → Resolve via 600dpi PDF eyes-on of p. 548 SCHOLION when next decade-polish pass runs.

2. **Scholion II, "B. Alberto, hic a. 13[?]"**: OCR fragment reads `tractatur tantum a li. Alberlo, hic a. 1.S` — the article number is unclear (`1.S` could be `13`, `1, 5`, `1, 8`, etc., or `a. 1, S` as in `§`). Currently rendered as `a. 13[?]`. → Resolve via 600dpi PDF eyes-on of p. 548 SCHOLION.

3. **Apparatus ^11 (Aristot. Metaph. text 8 Arabic-Latin), trailing "...cum...»[?]"**: OCR truncates the Arabic-Latin gloss mid-sentence at the page-548 footer (`cum,` then page break). The continuation almost certainly runs onto p. 549 (next chunk's footnotes). Currently terminated with `cum...»[?]`. → Resolve by checking pt2 raw lines 13131+ during d.32 work, or by 600dpi PDF eyes-on.

## Notes on Latin reconstruction

- Q.II content begins in raw pt2 only at line 13050 (after a page-break running head `DIST. XXXI. P. II. ART. II. QUAEST. II. 547`). Lines 12964–13049 are page-546 OCR for Q.I solutio + Q.I scholion (already published in q1). The chunk's frontmatter `line_start: 12964` is preserved per task instructions, but the Q.II body proper draws from lines 13050–13131.
- Page-546 OCR footnotes 5, 6, 7 (the `«` glyph numbered 6, the `'` numbered 7) were recognized as belonging to Q.I body text on p. 546 (in q1's already-shipped Conclusio + Solutiones); they are NOT included here. Footnote 8 of the page-546 group (`Vers. 8.`) is Q.II's first footnote (cites 1 Cor 3:8 for *Qui plantat et qui rigat unum sunt*) and is rendered here as `[^1]`.
- Two-column OCR was reflowed; running heads `DIST. XXXI. P. II. ART. II. QUAEST. II.` and `SENTENTIARUM LIB. I.` dropped at page boundaries, replaced with `<!-- page N -->` HTML comments at 546→547 and 547→548.
- Page break 546→547 placed between Fundamentum 1 (last line on p. 546) and Fundamentum 2 (first column of p. 547), per OCR layout.
- Page break 547→548 placed mid-Solutio-3 ("quia etsi | concordant in fine propinquo"), per the explicit `S48 SENTRNTiARUM LIB. I.` running-head break.
