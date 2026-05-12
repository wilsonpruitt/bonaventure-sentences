# Tier-2 ambiguities — d.36 divisio

(2026-05-07) No `[?]` flags inserted. OCR was clean for this chunk; the four apparatus footnotes parse unambiguously, and the divisio body matches the standard Quaracchi divisio template (cf. d.35-divisio).

Notes:
- Footnote 2 OCR garble `Pro 'rfic/to'` corrected silently to `Pro dicitur` based on the variant context (PQV substitute *est* for the verb anchored to it in the body, which is *dicitur*).
- ART. II preamble (raw lines 20507–20520) rolled into divisio per task brief; a2-q1 already starts at line 20546 (QUAESTIO I header), so no overlap.
- printed_pages corrected from scaffolding `[617]` to `[619, 622]` (619 = COMMENTARIUS / DIVISIO TEXTUS / TRACTATIO; 622 = ARTICULUS II preamble). PDF offset pt2 = printed − 410 → [209, 212].

(2026-05-12, Wave 9b apparatus-rebuild dispatch) Re-verified raw OCR per-page footer walk. Result: NO new entries to add. Audit raw=52 vs chunk=4 (+48) is bounds-noise OVERCOUNT (Lesson 10), not undercoverage.
- p. 619 footer band (raw lines 20229-20231): 4 entries — all present and verbatim-faithful in chunk as [^1]-[^4].
- p. 620 footer band (raw ~20303-20330): belongs to d36-a1-q1 (lines 20242-20414); fully covered in that chunk's apparatus (14 entries).
- p. 621 footer band (raw ~20422-20443): also belongs to d36-a1-q1.
- p. 622 footer band (raw lines 20522-20534): belongs to d36-a1-q2; fully covered in that chunk's apparatus. The p. 622 content rolled into THIS chunk (lines 20507-20520) is only the ARTICULUS II preamble, which carries no apparatus anchors of its own.
- Status string promoted from `apparatus-incomplete` to `complete` with explicit per-page distribution + OVERCOUNT note. No body or apparatus content edits — apparatus rebuild not warranted. Metadata-only disposition per Wave 9b Tier A precedent (d37-littera 2026-05-09).
