# d.38 littera — Tier 2 ambiguities log

Created 2026-05-07 during Tier-2 promotion of `vol1/bon-sent-I-d38-littera.md`.

## OCR-flagged ambiguities

**bon-sent-I-d38-littera, Cap. I, Origenes citation block**: OCR shows `non notetur ibi causa nisi sine qua non, fleret`. Reading reconstructed as `non notetur ibi causa nisi sine qua non fieret` — i.e. "no cause is noted there save a *sine qua non*" (a necessary condition without which it would not happen). [?] flagged inline once for the punctuation/syntax of the trailing clause; sense is clear, but the exact Quaracchi punctuation around `sine qua non, fieret` may differ from what the OCR delivers (the comma may be spurious column-rule).

**bon-sent-I-d38-littera, Cap. I, mid-page on `nec aliter scivit creata quam creanda`**: OCR clean; no flag.

**bon-sent-I-d38-littera, Cap. I, Augustine's *De Trinitate* book number**: OCR reads "in decimo quinto libro de Trinitate" (book XV) and then later "Idem quoque in sexto libro" (= book VI of De Trin.). Both citations preserved verbatim; Quaracchi apparatus (note 3 of OCR footer) cites cap. 13 n. 22 for the first and cap. 10 n. 11 for the second. Not flagged — sense is clear.

**bon-sent-I-d38-littera, Cap. II, `aut aliter potest fieri, quam Deus praescivit, aut non aliter`**: OCR has `aut aliter potest fleri` (fleri = fieri, standard OCR garble for `fi`). Silently corrected to *fieri* throughout (likewise *flunt*→*fiunt*, *flat*→*fiat*, *fl-*→*fi-*) per CLAUDE.md OCR cleanup rules. Not flagged.

**bon-sent-I-d38-littera, Cap. II tail, `non esset^ praescitum`**: OCR has a stray `^` glyph (carrot from broken footnote anchor or column-rule). Read as plain `non esset praescitum`. [?] flagged inline once at the spot, since a real footnote anchor may have been dropped here. Resolution requires PDF eyes-on; deferred.

## 2026-05-08 sweep audit (re-audit since 2026-05-07 promotion)

**Marker `[^2]` placement corrected.** OCR (raw line ~24863) shows the footnote-2 superscript (rendered as `%`) directly after `praeteritis`: `praeteritis % sed etiam de praesenlibus et futuris ,`. Original chunk had the marker mis-placed after `futuris` in both Latin and English bodies. The apparatus 2 entry's `Ita in codd. ABE et edd. 1, 6, in aliis non bene *futuris*` is a textual variant *anchored on `praeteritis`* (some manuscripts incorrectly read `futuris` for `praeteritis` here). Marker repositioned to after `praeteritis` in both Latin and English. Apparatus text unchanged; transcription_status updated.

**Marker `[^6]` position checked.** OCR: `et ex creaturis penderet praescientia ' Creatoris,` — the `'` glyph (= footnote 6) sits *between* `praescientia` and `Creatoris`, not after `penderet`. Chunk currently anchors `[^6]` after `penderet`, which is where the apparatus's `dependeret pro penderet` variant logically applies. Retained on logical grounds; flagged here for PDF-resolution at next polish-blocker if a literal-OCR-position policy is preferred. NOT moved.

**Marker `[^4]` position confirmed.** OCR shows `Unde in Ecclesiastico *` with `*` = footnote 4 immediately after `Ecclesiastico`. Chunk matches. ✓

**Body silent-dropout check (DUB-V-style).** Walked Cap. I body line by line against raw lines 24851–25042; no missing clauses detected. Walked Cap. II body against raw lines 25043–25069; no missing clauses detected. The "supra praetaxatum est" / "His enim duobus modis" passage on transitions between p.667 and p.668 is intact.

## Apparatus footnote anchors

The Quaracchi footer for these two pages (printed pp. 667–668) carries 8 numbered notes plus the Vulgate citation header note for Sap. 7, 24. They are renumbered consecutively 1–8 in this chunk. The OCR shows them in a two-column footer band at lines 24898–24910 (page 667 footer) and 25024–25037 (page 668 footer); both blocks were transcribed in full. No notes were dropped.
