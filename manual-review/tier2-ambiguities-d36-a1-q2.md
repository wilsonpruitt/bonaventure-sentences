# Tier-2 ambiguities — d.36 a.1 q.2

Logged 2026-05-07 during Tier-2 promotion of `vol1/bon-sent-I-d36-a1-q2.md` from raw lines 20415–20505 of `raw/bonaventure_vol1_pt2_raw.txt`.

## Inline `[?]` flags

- **bon-sent-I-d36-a1-q2, fundamentum 1 (page 621)**: OCR ends fund. 1 mid-clause at "si ergo hoc est commune tribus..." — the printed text on page 621 truncates at the bottom of the right column with no continuation captured by OCR. Currently rendered "...si ergo hoc[^2] est commune tribus[?]..." → Resolve via 600dpi PDF eyes-on of pt.2 PDF p. 211 (printed 621): the missing continuation likely reads "...tribus personis, ergo non est dicendum, quod sint ratione personae" or similar implicit negation. Defer to next polish-blocker decade audit.

- **bon-sent-I-d36-a1-q2, scholion I**: OCR garbles "II p.-m-cis" / "11 p.-m-cis" at line 20502–20494: "non invenimus discussam, nisi 11 p.-m-cis, nempe a Scoto..." — the OCR's "11 p.-m-cis" appears to be a corrupted reading of "*paucis*" ("by few [authors]") or "*a paucis*". Currently rendered "II[?] p[?]m[?]cis[?]" with "by a few[?]" in English. → Resolve via 600dpi PDF: most likely "*a paucis*". Defer to polish-blocker.

- **bon-sent-I-d36-a1-q2, [^7]**: OCR has "post *quod sunt* cod. [blank space] non incongrue addit *in Deo*" — the codex letter is missing in OCR (line 20526 just has "cod.    non incongrue"). Currently rendered "codex [?]". → Resolve via 600dpi PDF.

## Marker-position notes

- [^1] anchor placed after "videtur" (per fn-text "Codd. aa bb subiiciunt *omnino*", which adds *omnino* most naturally to *videtur* rather than to *hoc*). OCR positioned the apostrophe glyph after "hoc" but the grammatical fit favors *videtur*. If next polish pass disagrees, swap [^1] to "hoc[^1]" and renumber.

- [^2] is the OCR-anchored apostrophe `'` after "hoc" in line 20430. The footnote text "Verba *illud quod est in aliquo* desiderantur" actually relates to fund. 2 ("est in aliquo est in illo"); placement here follows OCR position rather than referential fit. Decade-polish to verify.

## Status

13 apparatus entries (7 from page 621 + 6 from page 622, but body uses 9 unique markers since page-621 fns 4–7 reference page-622 text). Footnotes 4–7 of page 621 OCR block were absorbed into the page-622 numbering (3, 5, 6, 7 → mapped to body markers [^3], [^5], [^6], [^7], [^8]) for parser cleanliness. Verify mapping during polish-blocker.
