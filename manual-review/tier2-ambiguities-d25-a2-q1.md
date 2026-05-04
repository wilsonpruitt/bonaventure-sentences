# Tier-2 ambiguities — bon-sent-I-d25-a2-q1

Source: pt2 raw lines 2413–2679; pt2 PDF (doctorisseraphic12bona.pdf) pages 31–34 = printed pages 441–444.

## PDF / printed page offset (verified)

The pt2 PDF doctorisseraphic12bona.pdf has only 468 pages and contains Vol I distinctions ~24 onward through later books (it is *not* the same offset as pt1). Direct verification by extracting PDF pages:

- PDF page 11 → printed page 421 (DIST. XXIV. ART. I. QUAEST. I.)
- PDF page 32 → printed page 442 (DIST. XXV. ART. II. QUAEST. I.)
- PDF page 200 → printed page 610 (SENTENT. LIB. 4)

Therefore for this chunk: **PDF page = printed page − 410**.
- printed 441 → PDF 31
- printed 442 → PDF 32
- printed 443 → PDF 33
- printed 444 → PDF 34

The sibling chunk d25-a1-q1 (currently recorded as `pdf_pages: [537, 538, 539, 540]`) and d25-littera (`[534, 535, 536]`) carry the pt1-PDF offset of +102 and are therefore wrong for the pt2 PDF. Not corrected here per the instruction not to touch other chunk files.

## Resolved ambiguities (no `[?]` flags emitted in chunk body)

- **OCR `Concedenda3` (raw line 2554)** → resolved to **`Concedendae`**. The high-resolution PDF image clearly shows "Concedendae⁶" with the footnote-marker spacing for fn 6 (Cod. V *subiicit quae probant*); the OCR `3` was misread of `e⁶`.
- **OCR `per,sonaTO^` (raw line 2578)** → resolved to **`personam`** (no footnote marker on this word; the apparatus marker `^` is artifactual OCR garble; fn 18 attaches to the immediately following clause `ut praedictum est`, where the high-res image shows the actual marker).
- **OCR `praedictum est',`** → confirmed as `praedictum est` followed by footnote marker `⁷` (now renumbered fn 18 in this chunk).
- **OCR `decima nona °`** → confirmed as `decima nona` + footnote marker (fn 6 in this chunk; corresponds to footer entry "Lit. Magistri, c. 7. seqq.").
- **OCR `aequivocum ^` (right column line 2481)** → confirmed as `aequivocum` + marker for fn 8 (footer entry "Sic plerique codd.; Vat. cum cod. cc *aequivocatio*…").
- **OCR `Damascenus "` (right column line 2486)** → confirmed as `Damascenus` + marker for fn 9 (footer entry "Libr. I. *de Fide orthod.* c. 8…").
- **OCR `harum '°`** → confirmed as `harum` + marker for fn 10 (footer entry "A Vat. abest *harum*…").
- **OCR `animal est "`** → confirmed as `animal est` + marker for fn 11 (footer entry "Vat. cum cod. cc *dicitur animal esse*").
- **OCR `humanitas^`** → confirmed as `humanitas` + fn marker (footer entry on p.443 "Aliqui codd. ut F G I R S V cum ed. 1 *humanitatis*").
- **OCR `comparatione '^`** → confirmed `comparatione` + fn marker (footer "Vat. praeter fidem mss. et ed. 1 *operatione*").
- **OCR `Non °`** → confirmed `Non` + fn marker (footer "Vat. adiicit *enim*").
- **OCR `distinctione '`** → confirmed `distinctione` + fn marker (footer "Cod. Y *definitione*; cod. T *distinctione vel definitione*").
- **OCR `habitudinis '`** → confirmed `habitudinis` + fn marker (footer "Auctoritate cod. T adiecimus verba *similitudinem habitudinis*…").
- **OCR `substantiam'`** → confirmed `substantiam` + fn marker (footer "Mutilam lectionem Vat., quae verba *dicitur secundum substantiam* omittit…").
- **OCR `unitatem '`** in p.444 first paragraph → confirmed `unitatem` + fn marker (footer "A nostris codd. et ed. 1 abest *et*").
- **Scholion `nominis^`** → confirmed `nominis` + fn marker (footer "Cfr. supra d. 6. p. II. q. 1.").
- **OCR running heads `DIST. XXV. .\RT.` / `DIST. XXV. ART. II.`** → silently corrected.

## Header / opener structure

- The line range `2413–2445` covers the ARTICULUS II header (line 2413), the article subtitle "*De communitate nominis persona.*" (line 2415), and the two-question opener (lines 2419–2422), all printed on the bottom of p. 441.
- Footnotes 1–5 appearing in the p. 441 footer (raw lines 2426–2439) belong to the **previous chunk** (d25-a1-q2 solut.) and are intentionally excluded.
- Page 442 (raw line 2447) opens with "QUAESTIO I." and the question subtitle on line 2453.
- Page 444 (raw line 2637) carries the tail of resp. ad 4, the SCHOLION (lines 2646 ff.), then immediately QUAESTIO II opens at line 2680.

## Footnote count

- p. 442 footer: 11 entries → fns 1–11
- p. 443 footer: 8 entries → fns 12–19 (renumbered from local 1–8)
- p. 444 footer: 2 entries belong to this chunk → fns 20–21 (renumbered from local 1–2). Local fns 3–5 on p. 444 belong to QUAESTIO II and are excluded.

Total: **21 footnotes**, all paired in Latin and English bodies, all with **La.** and **En.** entries.

No `[?]` markers emitted in the chunk body; every garble was resolvable from the high-resolution PDF image of pt2 pp. 31–34.
