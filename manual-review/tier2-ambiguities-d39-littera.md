# Tier-2 ambiguities — bon-sent-I-d39-littera

OCR source: `raw/bonaventure_vol1_pt2_raw.txt` lines 26377–26535. Printed pp. 682–683 (Quaracchi 1882, Vol. I).

## Open `[?]` flags

- **Apparatus [^2] tail (codd. D / E variants)**: The OCR footer band on p. 682 collapses two adjacent notes into the same physical paragraph (the *De Trin.* chapter/numbering note + a *Cod. D minui / Cod. E minui vel mutari* variant). The body anchor [^1] in line 26389 is on *mutari*, and the footer's first numbered note (`Vat. cum edd. 2, 3 sub.`) is the variant for *sub* vs *mutari*; the *Cod. D minui / Cod. E minui vel mutari* fragment that immediately follows in the OCR is most naturally a continuation of that same variant cluster, but in the OCR's column order it appears under what reads as the second (n. 2 = Cap. 13. n. 22.) footnote. I have folded the cod. D / cod. E fragment into [^2] following the OCR's printed sequencing; if eyes-on the printed page shows it should attach to [^1] (variants on *mutari*), [^1]'s English will need the cod. D / cod. E sentence appended and the paragraph removed from [^2]'s tail. Resolve at next d.31–d.40 polish-pass with 600 dpi PDF.

## Resolved silently (OCR cleanup)

- `llrum` → *Utrum* (Cap. I title, line 26384) — initial U misread as ll.
- `Augnstinus` → *Augustinus* (line 26417).
- `decirao` → *decimo* (line 26417).
- `Hieronyinus` → *Hieronymus* (line 26473).
- `Habacuc''` → *Habacuc* (line 26473) — apostrophes are footnote-marker glyphs, dropped from body.
- `Apostoius''` → *Apostolus* (line 26494).
- `Numquid` ← OCR `Niimquid` (line 26493).
- `pluviam` ← OCR `pliwiam` (line 26505).
- `culicum` ← OCR `culicura` (line 26506).
- `momenta singula` ← OCR `momenta sin-/gula,.immo` (lines 26508–26509) — collapsed line break, removed stray period.
- `vel mutari` (cap. III title) — OCR Cap. I title fragment "vel aliquo modo mutari" preserved as printed.
- Cap. I lacks a printed `Cap. I.` label in the OCR, but the structural sequence (II, III, IV are labelled) and the running heads make Cap. I unambiguous; label supplied in the chunk.

## Frontmatter correction made

- `printed_pages` was `[660, 661]` (pre-translation scaffolding placeholder); corrected to `[682, 683]` based on running-head positions: line 26365 = SENTENTIARUM LIB. I (closes preceding p. 681), line 26377 = DISTINCTIO XXXIX (opens p. 682), line 26470 = DISTINCTIO XXXIX running head (= top of p. 683), line 26531 = SENTENTIARUM LIB. I (closes p. 683), line 26536 = COMMENTARIUS IN DISTINCTIONEM XXXIX (Bonaventure, p. 683 footer or p. 684 top). PDF offset for pt2 = printed − 410, so pdf_pages = [272, 273].
