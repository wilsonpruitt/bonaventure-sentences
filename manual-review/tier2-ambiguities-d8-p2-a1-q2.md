# Tier-2 ambiguities — bon-sent-I-d8-p2-a1-q2

Logged during Wave 9b Tier B disposition, 2026-05-09. Apparatus rebuild from raw OCR pt1 lines 34190–34634 (printed pp. 168–170); 27 footer entries.

## [?] flags

**chunk-id, [^17] (p. 169, fn 9)**: OCR reads `Aliqui codd. ut H T cum edd. i, 4, 5 habeai.` The verb `habeai` is OCR for `habent`, but the entry truncates without the variant text (no `loco X` clause). Likely the entry indicates that codd. HT with edd. 1, 4, 5 read something other than the Vatican here, but the variant reading itself is OCR-dropped. Currently rendered: "Some codices, such as H and T, with editions 1, 4, and 5, read *habent* [?]." → Resolve with: PDF p. 271 (raw/doctorisseraphic11bona.pdf) eyes-on at 600 dpi to recover the dropped tail; until then keep as-is with [?] flag. Adjacent fn 10 (`Nonnulli codd. ut H I aa bb addunt sic`) suggests fn 9 is in the same vicinity of variant addition/omission near "alii" / "secunda" of *Una compositio est ex partibus essentialibus; et haec est in omnibus per se entibus; alia est…*.

**chunk-id, [^23] (p. 169, fn 15)**: OCR reads `Id est substantia completa, cui opponitur accidcns. — Paulo infra fide plurium mss. ut H T aa bb ee el ed. ) post iterum posuimus omne loco esse; codd. aa bb habent omne` — the entry truncates mid-clause after `habent omne`. The complete entry should specify what codd. aa bb actually have *omne* in place of (likely *esse*) and what the ms tradition's reading was. Currently rendered with [?] tail. → Resolve with: PDF p. 271 eyes-on at 600 dpi to read the bottom of the footer band where the OCR drops; the entry continues onto a few more words before fn 16 begins. Until then keep [?].

## Notes

- Per-page footer walk yields 8 + 15 + 4 = **27 entries**. Hardened audit script reports raw=31 (diff +4 against 27). The +4 overcount-only is consistent with Lesson 10: the chunk's body has lettered series (a)/(b)/(c) twice and the scholion has Roman-numeral sections I–V; these match `[\W_]{1,3}\s+[A-Z]` and inflate the heuristic. **NOT real undercoverage** — the chunk's prior 8-entry apparatus was real undercoverage; the rebuilt 27-entry apparatus is full coverage.
- Body anchor for [^6] in the original chunk (now [^9]/[^10] split) was mis-anchored: chunk had `[^6]` at `per se entibus` but its content (the *accidentium pro actionum* variant from p. 169 fn 1) belonged at `actionum`. Now [^9] is correctly at `actionum` and [^10] is correctly at `per se entibus` (p. 169 fn 2). Verified against raw OCR marker spacing (`actionum '` vs `entibus °-`).
- Body and English translation passed paraphrase guard: chunk Latin body covers all clusters present in raw OCR pt1 lines 34190–34634 (fund. 1–4, contra 1–4, conclusio, two privation modes with three-fold compositions and three-fold differences, epilogus, alius modus, ad 1, ad 2/3/4 with concluding *omne simplicissimum est absolutissimum*). No paraphrase or omitted clusters.
