# Breviloquium Pars I polish gate — resolution log

**Gate scope:** prologue (`bon-brev-prol`, `-s1`…`-s6`) + Pars I (`bon-brev-p1-c1`…`c9`),
16 chunks, printed pp. 201–208 + 210–218. This is the shakedown gate per the revised
Vols V–X cadence (CLAUDE.md § "Polish-gate cadence for Vols V–X") — the first structural
seam of the first work in the volume.

Run 2026-07-28 (Sonnet), continuing from the 2026-07-28 pilot/build session.

## Pass 1 — `[?]` flag resolution

**Nothing to resolve.** Every one of the 16 chunks' `## Notes` carries the literal
sentence "No `[?]` flags" (verified via `grep -F '[?]'`, which matches only that
confirming sentence in each file, not an actual unresolved marker). Zero ambiguities
across the gate.

## Pass 2 — style/formatting audit (full corpus, decoupled — runs every commit)

`polish-style-scan.py` and `audit-style-formatting.py` report their findings across
`vol1`–`vol5`; the 14 outstanding issues are **all pre-existing, all outside Vol V**
(see item 2 of `NEXT-SESSION-QUEUE.md`). Vol V contributes zero flags to either scan.

## Pass 3 — cross-chunk boundary integrity sweep

`seam-screen.py --volume 5`: **14 mid-page boundaries, 0 tail-not-terminal suspects.**
Every boundary's tail clause is grammatically complete and its head opens a new
sentence — no cascade-merge signature anywhere in the gate.

`check-vol5-apparatus.py`: **16 chunks, 130 apparatus entries**, La/En counts matching
on every chunk, and all 17 printed pages (201–208, 210–218) show continuous 1..N
footer ownership with no gaps and no double-claims. `All checks passed.`

Runover joins (10 of 16 chunks carry at least one) are already documented per-chunk in
each file's `## Notes`, per the method rules frozen in `next-session-resume.md`.

**0b (from the queue) also verified in this pass:** `bon-brev-prol-s6`'s heading-anchor
case (`[^p207-4]` inside the `### § 6` title) renders correctly in the browser —
Playwright snapshot of `/browse/5/d/0/q/bon-brev-prol-s6` shows the `<h3>` splitting
into two emphasis spans with the footnote `<sup><a href="#fn-p207-4">4</a></sup>`
between them, in both the Latin and English columns, and the apparatus list resolves
`#fn-p207-4` to a proper La/En entry. No reader-regex defect; no chunk edit needed.

## Pass 4 — disk cleanup

`raw/vision/vol5/*.png` deleted (56 MB reclaimed, confirmed with Wilson first since
it's a deletion). `/tmp/colcrop/vol5-*` was already empty. Both are fully regenerable
from the gitignored PDF via `tools/extract-pages.py` + `tools/colcrop.py`.

## Disposition

**Gate CLOSED.** All four passes clean; nothing carried forward. Next front is
**Pars II, opening printed p.219** — nothing forwarded from p.218's footer, so the
first Pars II chunk starts clean. Gutters for p.219+ are not yet measured; measure
per page per the established parity-alternation caution.
