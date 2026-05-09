# Tier-2 ambiguities: d.8 p.1 a.2 q.2 (Wave 9b Tier A apparatus rebuild, 2026-05-09)

Apparatus rebuilt from raw OCR `bonaventure_vol1_raw.txt` lines 32878–33451 covering printed pages 158–161 of *Opera Omnia* tom. I. Quaracchi restarts footnote numbering on each printed page; this chunk's body draws from p.158 footnotes 11–13 (preceding footnotes 1–10 belong to the prior a.2-q.1 tail), p.159 fns 1–16, p.160 fns 1–9 (plus tail of p.159 fn 16), and p.161 fns 1–10. Total this chunk = 38 entries.

## `[?]` flags

**`[^6]` — p.159 footer entry 3 ("Cap. 1. in fine.")**
This bare cross-reference appears between Gregor. *Moral.* (fn 2) and Rom. 8 (fn 4) on p.159 footer-block. It carries no quoted lemma so its body anchor is not unambiguous from the OCR alone. The most likely target is the implicit Damascenus *de Fide orth.* I.3 reference (sharpening the chapter reference of p.158 fn 13 to "c. 1 in fine" — but Quaracchi's own fn 13 already gives "c. 3"). Alternative: it may attach to argument 3's "huius" / "huiusmodi" gloss. Currently anchored at the close of argument 3 (after "*ergo etc.*" of arg 3) and rendered with a `[?]` flag in the En. line. Resolve by checking 600dpi PDF p.159 footer-block alignment against body marker spacing.

## Notes on counting

`tools/audit-apparatus-count.py` heuristic flagged this chunk with diff `+41` (raw=53, chunk=12). Page-by-page walk yields 38 real footer entries belonging to this chunk's body. Heuristic over-counts here (typical 10–15% noise range) — 38 is the ground-truth count from eyes-on raw walk per CLAUDE.md Lesson 9.

## Body-paraphrase guard

Result: body sound. Spot-checked variant-note targets (codd. tendit on Damascenus quote line; "ubi hoc" on argument 2; "a non esse" on argument 7; "actum" in epilogus; "obiicit" on Ad 9) — all corresponding Latin phrases present in chunk body. No orphan apparatus clusters; no missing body content found.
