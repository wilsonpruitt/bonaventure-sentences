# Tier-2 ambiguities — d.39 dubia

Scope: DUB I–IV (raw lines 27875–27966 of `bonaventure_vol1_pt2_raw.txt`, printed p. 698).

No inline `[?]` flags were placed in `vol1/bon-sent-I-d39-dubia.md`. The OCR was clean enough on this page, and 600dpi PDF spot-checks (`/tmp/d39-dubia-p683-273.png` initially, then the correct `/tmp/d39-dubia-p697-288.png` for printed p. 698) resolved the few uncertain readings:

- **Frontmatter correction.** Pre-translation frontmatter had `printed_pages: [683]`. PDF eyes-on shows DUB I–IV occupy printed p. **698** (PDF pt2 page 288); DUB V–VI continue on printed p. 699. Corrected to `[698]` / `pdf_pages: [288]`. (Task scope explicitly limits this chunk to lines 27875–27966 = DUB I–IV; DUB V–VI on p. 699 are not yet captured here. Flag for follow-up if a fuller d.39-dubia chunk is desired.)
- **Footnote 9 anchor.** Apparatus reads "Vat. cum pluribus codd. *sic*." Anchor placed at "et sic[^9] incipit Deus scire" (DUB IV respondeo), where Quaracchi italicises *sic* as the lemma. The OCR garbled the surrounding glyph as "sicut '" — resolved against PDF.
- **Footnote 5 anchor.** Apparatus is a bare "Vide Alex. Hal." cross-reference for DUB II as a whole. Quaracchi places it at the end of DUB II respondeo, after "in divina essentia"; that placement preserved.

No unresolved `[?]` flags remain in DUB I–IV.

## 2026-05-07 extension — DUB V + DUB VI (raw lines ~27969–28023, printed pp. 699–700)

The chunk was extended on 2026-05-07 to absorb DUB V (`Item quaeritur de hoc quod dicit: Nec potest noviter vel ex tempore velle aliquid…`) and DUB VI (`…specialem curam habet de rationalibus…`), which the original auto-chunker boundary at line 27966 had cut off. Frontmatter updated: `line_end` 27966 → 28023; `printed_pages` [698] → [698, 699, 700]; `pdf_pages` [288] → [288, 289, 290]; apparatus count 9 → 15.

Open `[?]` flags introduced by the extension (DUB V apparatus is the most heavily fragmented section of OCR on this two-column page; the apparatus column splits across both columns and intercalates DUB I–IV's notes 1–4 with DUB V's notes 1–4, so glyph-level reconstruction is uncertain in places):

- **bon-sent-I-d39-dubia, DUB V apparatus [^10] (`Vat., post velle posita virgula, pro hic substituit hoc`)**: OCR reads `pro hoc substituit hic`; sense-direction is reversed by the corruption pattern between *hic*/*hoc*. Currently rendered with the substitution flagged (`pro *hic* substituit *hoc*[?]`). → Resolve against 600dpi PDF p. 699 column-bottom.
- **bon-sent-I-d39-dubia, DUB V apparatus [^10] tail (`Librarii … hic pro hoc legisse, valde [?]`)**: OCR truncates the closing clause (after `valde`) where the page-bottom column wraps. Currently rendered with `[?]` placeholder. → Resolve against 600dpi PDF p. 699 column-bottom.
- **bon-sent-I-d39-dubia, DUB V apparatus [^13] (`Vat. fuit. [?]`)**: Two adjacent apparatus notes in the OCR both read `Vat. fuit`. Provisionally split between [^11] and [^13]; the second may belong to a different lemma not yet identified. → Resolve against 600dpi PDF p. 699.
- **bon-sent-I-d39-dubia, DUB V Latin body, footnote-12 placement on `ordinationem ipsius effectus`**: OCR shows a backslash (`\`) marker at `velle hoc \ duo dico`; placed [^12] at the next "ordinationem" token instead, on the strength of the apparatus content. May need adjustment to the earlier position. → Resolve against 600dpi PDF p. 699.

These do not block Tier-2 status of DUB I–IV (which remain clean); they are scoped to the DUB V/VI extension and will be cleared in the d.31–d.40 polish-pass after d.40 ships.
