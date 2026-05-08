# d.3 Littera — Tier-2 ambiguities log

Created 2026-05-08 during Tier-2 promotion of `vol1/bon-sent-I-d3-littera.md`.

## OCR-derived flags

- **bon-sent-I-d3-littera, p. 62, footnote 2 (anchor `[^2]` after "*Apostolus dixit*").** OCR source (raw lines 18357–18358) yields only the fragment `'  Codd.  CDE  et` followed by blank lines; the full apparatus entry is truncated. The anchor was preserved in body and the apparatus entry left as a labelled fragment with `[?]`. → Resolve by eyes-on extraction of Quaracchi I, p. 62, footer note 2 (PDF p. 164 at ≥ 400 dpi).

- **bon-sent-I-d3-littera, p. 66, all four apparatus entries.** OCR source (raw lines 18841–18874) contains body text only; the COMMENTARIUS heading begins immediately at line 18876 with no intervening footer block. Four body anchors are flagged inline as `[?]` (instead of `[^N]`) at:
  1. "*credamus*" — after "in libro nono *de Trinitate*" (cit. Aug., *De Trin.* IX, prob. c. 1, n. 1, but unverified)
  2. "*Una est natura*" — after "in libro *de Fide ad Petrum*" (Pseudo-Aug. = Fulgentius, *De Fide ad Petrum* c. 1)
  3. End of "*Trinitatem*" — page-end source citation
  4. "*Nulla res est, quae se ipsam gignat*" — Aug., *De Trin.* I.1.1 (likely)

  → Resolve by eyes-on extraction of Quaracchi I, p. 66 (PDF p. 168 at ≥ 400 dpi). Likely 4–6 footer entries, mostly source citations.

- **bon-sent-I-d3-littera, p. 65, footnote 4 (apparatus body).** OCR yields the editorial gloss `... stricte dici non possunt esse unius Dei, sed sunt unius Dei ...` — the second "*unius Dei*" is suspicious; the antithesis the editor is constructing requires "*unus Deus*" (nominative). Rendered as "*unus Deus* [?]" in the En. with bracket-flag. → Resolve from PDF: confirm whether printed reads *unius Dei* (and editor's argument is opaque) or *unus Deus*.

## Structural notes

- The page-62 opening of Cap. I ("Apostolus namque ait..." through "...ad unitatem Deitatis pertinent monstrandam") was MISSING from the prior Tier-1 chunk. It has been added per OCR (raw lines 18267–18338). The chunk now correctly spans printed pages 62–66 instead of 63–66. Frontmatter `printed_pages` and `pdf_pages` updated accordingly.

- Bonaventure's *Divisio Textus* (raw lines 18887ff.) confirms that Pars I has two sub-parts: "In prima ostendit Unitatem, in secunda Trinitatem, ibi: *Nunc restat ostendere*." The chunk's Cap. I therefore comprises BOTH the unity-section (page 62) and the trinity-section (pages 62–63) joined as a single capitulum in the printed Quaracchi text.

- The OCR shows no explicit `Cap. I.` heading in the printed text (the marginal label `Cap. I.` was dropped by OCR margin-stripping). Cap. III is explicit (raw line 18623) and Cap. II / Cap. IV rubrics are present without numerical headings. Chapter numbering as printed reconstructed by structural inference; → confirm against PDF if discrepancy emerges.
