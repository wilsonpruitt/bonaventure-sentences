# d.23 scaffolds sweep audit (2026-05-08)

## Scope

Per task instruction: three named chunks only — `divisio`, `littera`, `dubia`. The full d.23 chunk inventory in `vol1/` also contains six question chunks (`a1-q1`, `a1-q2`, `a1-q3`, `a2-q1`, `a2-q2`, `a2-q3`), each with its own `tier2-ambiguities-d23-*.md` log. Those quaestio chunks are out of scope here.

The dubia chunk is the only d.23 chunk that crosses the pt1/pt2 boundary; its frontmatter carries both `line_start`/`line_end` (pt1) and `line_start_pt2`/`line_end_pt2` (pt2) extension fields.

All three target chunks were promoted to Tier 2 on 2026-05-03 (divisio + littera) and 2026-05-04 (dubia stitch-in of pt2 continuation). All three predate the cluster of suspect rebuilds the user flagged as resolved by the 2026-05-02 wave — d.11+ rebuilds confirmed elsewhere as holding.

## Per-chunk audit results

| Chunk | Bounds | Latin ↔ OCR | Apparatus | Markers (La / En / defs) | [?] flags | Status string | Verdict |
|---|---|---|---|---|---|---|---|
| divisio | 69438–69502 ✓ (COMMENTARIUS opener through end of TRACTATIO QUAESTIONUM list, before ARTICULUS I at 69505) | verbatim, OCR garbles silently corrected per per-chunk log; commentary subtitle and Lombard opener dropped per d.20/d.22 convention | 6 entries from pp. 404–405 footer (OCR notes 1, 2, 3, 4, 5, 6) | 6 / 6 / 6 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| littera | 69043–69437 ✓ (DISTINCTIO XXIII opener through end of cap. VI, trim before COMMENTARIUS at 69438) | verbatim; Cap. I and Cap. II headings restored from inference (OCR drop) per d.22 convention; three p. 402 page-bottom footnotes correctly suppressed (they belong to d.22 commentary) | 27 entries consolidated from three NOTAE AD LIBR. SENTENTIARUM blocks (pp. 402, 403, 404) | 27 / 27 / 27 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| dubia | pt1 71288–71373 ✓ + pt2 60–141 ✓ (DUBIA opener through end of DUB. IV body and full p. 417 footer apparatus, excluding pt2 lines 1–29 IA/title-page furniture, 142–160 AD LECTOREM editorial notice, 161+ d.24 territory) | verbatim across both raw files; pt2 two-column reflow (col-A-then-col-B) handled cleanly for both body and footer apparatus | 14 entries: 6 from p. 416 footer (printed nn. 3–8; nn. 1–2 anchor in preceding quaestio chunk) + 8 from p. 417 footer (printed nn. 1–8) | 14 / 14 / 14 | 1 (`ad ipsam[?] veritatem` at the pt1/pt2 seam — pt1 OCR has masculine `ipsum`, grammar requires feminine `ipsam` agreeing with `veritatem`; logged) | Tier 2 complete 2026-05-04 | HOLDS |

## Totals

- 3 / 3 chunks Tier-2 complete
- 47 apparatus entries total (6 + 27 + 14), all bilingual `**La.**` / `**En.**`, no fabrication
- All footnote markers paired exactly across Latin body, English body, and apparatus defs (verified by uniq-count: 3 occurrences per `[^N]` in each chunk; descriptive prose mentions in the apparatus blockquote and `## Notes` section in dubia are not anchors)
- 1 inline `[?]` flag (dubia, `ad ipsam[?] veritatem`) — already documented in `manual-review/tier2-ambiguities-d23-dubia.md` § (d)
- 1 silently-resolved historical correction (Jerome `Ep. 15 ad Damasum` adopted over OCR `Ep. 13` — canonical letter on the hypostasis controversy; logged under `manual-review/tier2-ambiguities-d23-dubia.md` § Apparatus renumbering with explicit owner-flag)
- Inter-chunk OCR boundaries verified clean: DISTINCTIO XXIII at 69043, COMMENTARIUS at 69438, ARTICULUS I at 69505 (pt1); page header at pt2 60, AD LECTOREM at pt2 147, DISTINCTIO XXIV at pt2 161
- Build smoke-test: `node scripts/build-content.mjs` → "Built content.json: 1 book(s), 422 questions, 350 translated" (clean parse, no warnings)

## Anomalies / observations

- **pt2 boundary handling — clean.** The dubia chunk is the first chunk in vol. I to stitch pt1 and pt2 in a single unit. The frontmatter encodes both line ranges (`line_start`/`line_end` for pt1, `line_start_pt2`/`line_end_pt2` for pt2). The body re-flows the pt2 two-column layout into linear order col-A-then-col-B for both prose and apparatus footer; semantic continuity at the seam (`Potest enim esse comparatio entis ad ipsum [pt1] veritatem [pt2]…`) confirms the column split. The `## Notes` trailing section in the chunk file documents the stitch in-band so a future reviewer doesn't have to reconstruct the boundary work from the raw files. Recommend keeping the `## Notes` section in d.23 dubia as the project's reference template for any future cross-volume-pt stitch chunks.
- **Jerome citation `Ep. 15` vs OCR `Ep. 13`.** The pt1 OCR at line 71350 reads `Epist. 13. ad Damasum, n. i` (Roman 4 misread). The chunk publishes `Epist. 15.` — historically correct (Jerome's letter to Damasus on the hypostasis controversy is *Ep.* 15, CSEL 54). The per-chunk ambiguity log calls this out with explicit owner-revertible language. No action; verdict HOLDS.
- **No fabricated apparatus.** Every one of the 47 entries traces to a specific OCR footnote line range. Renumbering maps from OCR-symbol order to consecutive `[^N]` are documented per chunk.
- **No paraphrase residue.** All three Latin bodies are verbatim from OCR (with documented silent corrections); all three English bodies are literal, paragraph-for-paragraph translations consistent with the d.11+ Tier-2 standard.
- **No unflagged `[?]` ambiguities** introduced by this audit — the existing per-chunk logs already document the only flagged item.
- **No backups created.** No substantive edits made; `vol1/_backup-d23-{chunk}-pre-rebuild-20260508/` directories were not needed. The pre-existing `_backup-d23-pre-rebuild-20260503/` remains untouched.

## Verdict

All three d.23 scaffold chunks (divisio, littera, dubia) HOLD as Tier-2 complete. The dubia pt1/pt2 stitch is the most structurally novel artifact in the d.23 set and is verified clean.
