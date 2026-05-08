# d.25 scaffolds sweep audit (2026-05-08)

## Scope correction

Task description listed three chunks (`divisio`, `littera`, `dubia`). The actual d.25 chunk inventory in `vol1/` is **seven** files — same shape as d.20:

- `bon-sent-I-d25-littera.md`
- `bon-sent-I-d25-divisio.md`
- `bon-sent-I-d25-a1-q1.md`
- `bon-sent-I-d25-a1-q2.md`
- `bon-sent-I-d25-a2-q1.md`
- `bon-sent-I-d25-a2-q2.md`
- `bon-sent-I-d25-dubia.md`

All seven were rebuilt 2026-05-03 in the same regimen as the d.11+ wave (wave was 2026-05-02; d.25 followed a day later). Per-chunk ambiguity logs already exist (7 files: `tier2-ambiguities-d25-{littera,divisio,a1-q1,a1-q2,a2-q1,a2-q2,dubia}.md`). Two backup directories present from the 2026-05-03 build (`vol1/_backup-d25-pre-rebuild-20260503/` and `vol1/_backup-d25-a2-q1-pre-rebuild-20260503/`); not new from this sweep.

## Per-chunk audit results

| Chunk | Bounds | Latin↔OCR | Apparatus | Markers paired (La/En/defs) | [?] flags | Status string | Verdict |
|---|---|---|---|---|---|---|---|
| littera | 1430–1722 ✓ (DISTINCTIO XXV at 1430 → before COMMENTARIUS at 1723) | verbatim | 24 entries from three NOTAE blocks pp. 432–434, page-432-top spillover from d.24 commentarius correctly suppressed | 24 / 24 / 24 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| divisio | 1731–1827 ✓ (DIVISIO TEXTUS at 1731 → before ARTICULUS I at 1828) | verbatim, two-column reflow clean | 3 entries from p.434 NOTAE AD COMMENTARIUM | 3 / 3 / 3 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| a1-q1 | 1828–2178 ✓ (ARTICULUS I at 1828 → before QUAESTIO II at 2179) | verbatim, ARTICULUS I + QUAESTIO I headers + scholion (I–III) included | 27 entries renumbered 1–27 from four footer blocks (p.435 fns 1–6, p.436 fns 7–16, p.437 fns 17–24, p.438 fns 25–27) | 27 / 27 / 27 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| a1-q2 | 2179–2412 ✓ (QUAESTIO II at 2179 → before ARTICULUS II at 2413) | verbatim, scholion (I–II) translated literally | 17 entries renumbered 1–17 from three footer blocks (p.439 fns 1–6, p.440 fns 7–13, p.441 fns 14–17) | 17 / 17 / 17 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| a2-q1 | 2413–2679 ✓ (ARTICULUS II at 2413 → before QUAESTIO II at 2680) | verbatim, ARTICULUS II header + 2-question opener + QUAESTIO I included | 21 entries renumbered 1–21 from three footer blocks (p.442 fns 1–11, p.443 fns 12–19, p.444 fns 20–21; p.441 has no fns belonging to this chunk) | 21 / 21 / 21 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| a2-q2 | 2680–2772 ✓ (QUAESTIO II at 2680 → before DUBIA at 2773) | verbatim, scholion (I–II) literal | 5 OCR-preserved entries from p.444 footer + 3 placeholder `[?]` entries (markers 6–8) where p.445 footer block was lost in pt2 OCR (already documented) | 8 / 8 / 8 | 3 (markers 6, 7, 8 — apparatus only) | Tier 2 complete 2026-05-03 | HOLDS |
| dubia | 2773–2943 ✓ (DUBIA CIRCA LITTERAM MAGISTRI at 2770/header, body opens 2773 → before DISTINCTIO XXVI at 2945; tail tightened 2026-05-04 from 2999 → 2943 to exclude d.26 littera caps I–IV head) | verbatim, 4 dubia I–IV | 20 entries from 2-column footers pp. 445–447 col-A (col-B p.447 belongs to d.26) | 20 / 20 / 20 | 0 | Tier 2 complete 2026-05-03 (boundary patch 2026-05-04) | HOLDS |

## Totals

- 7 / 7 chunks Tier-2 complete
- 120 apparatus entries total (24 + 3 + 27 + 17 + 21 + 8 + 20), all bilingual `**La.**` / `**En.**` except the 3 documented OCR-loss placeholders in a2-q2
- All footnote markers paired exactly across Latin body, English body, and apparatus defs
- 3 `[?]` flags total, all in `a2-q2` apparatus entries 6–8 — already documented in `manual-review/tier2-ambiguities-d25-a2-q2.md` as awaiting visual extraction of pt2 PDF p. 547 (printed p. 445) bottom margin
- Inter-chunk OCR boundaries verified clean at every transition (DISTINCTIO XXV, COMMENTARIUS, DIVISIO TEXTUS, ARTICULUS I, QUAESTIO II of art. 1, ARTICULUS II, QUAESTIO I/II of art. 2, DUBIA, DISTINCTIO XXVI)
- Build smoke-test: `cd site && node scripts/build-content.mjs` → "Built content.json: 1 book(s), 422 questions, 350 translated" (clean parse, identical to d.20 sweep result)

## Anomalies / observations

1. **Task scope undercount**: task description named 3 chunks; corpus has 7. No work done on phantom files. (Same shape as d.20 sweep; expected for any distinction with two articles + two questions per article.)
2. **No rebuild needed**: the d.25 chunks are not damaged scaffolds; they are fully translated Tier-2 work from 2026-05-03 (with one boundary patch on dubia 2026-05-04) and pass the same gates the d.11+ wave passed.
3. **No backups created this sweep**: the two `_backup-d25-*-pre-rebuild-20260503/` dirs are from the 2026-05-03 build itself, not from this audit. No edits were necessary today.
4. **No `transcription_status` date bump to 2026-05-08**: per workflow, status only bumps on substantive edits. Audit-only sweeps leave status untouched.
5. **a2-q2 [?] flags are honest OCR-loss markers**, not ambiguities about Latin readings. The pt2 djvu OCR truncated the p. 445 footer block; the chunk preserves balanced markers (5 OCR + 3 stub) so the parser stays clean. Resolution requires visual extraction from pt2 PDF p. 547 bottom margin and is already in the manual-review queue.
6. **Stale ambiguity-log claim about pdf offset**: `tier2-ambiguities-d25-a2-q2.md` says the divisio's `pdf_pages: [24, 25]` is "wrong, should be [536, 537]" using a +102 offset assumption. That is itself wrong: the pt2 PDF is `doctorisseraphic12bona.pdf` (not pt1), and per CLAUDE.md and the divisio chunk's own `source` line, **pt2 offset = printed − 410**, so printed 434/435 → PDF 24/25 is correct. All seven d.25 chunks use the correct pt2 offset. No edit needed; the stale ambiguity-log note is non-load-bearing (didn't trigger any chunk change).
7. **dubia "Notes" tail line still cites raw lines 2773–2999**, but `line_end: 2943` and the status string both record the 2026-05-04 boundary tightening. The Notes paragraph is descriptive, not bookkeeping; the authoritative bounds in frontmatter are correct. Mechanical to fix if desired, not a Tier-2 blocker.

## Conclusion

d.25 ships as-is. No edits, no rebuilds, no commit. Build clean.
