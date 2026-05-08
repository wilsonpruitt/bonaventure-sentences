# d.24 scaffolds sweep audit (2026-05-08)

## Scope

Per task framing and prior memory ("d.24 has NO dubia"), this sweep targets the two non-quaestio chunks in `vol1/`:

- `bon-sent-I-d24-divisio.md`
- `bon-sent-I-d24-littera.md`

The six d.24 quaestio chunks (`a1-q1`, `a1-q2`, `a2-q1`, `a2-q2`, `a3-q1`, `a3-q2`) are NOT in scope for this sweep.

d.24 is the first distinction whose source is `raw/bonaventure_vol1_pt2_raw.txt` (printed p. 418 onward; pt2 PDF offset = printed − 410). Both chunks were originally promoted to Tier 2 on 2026-05-03; this sweep verifies bounds, content, apparatus, and marker pairing before the d.21–d.30 polish-blocker pass and confirms no rebuild is needed.

No prior `_backup-d24-*` directory exists; the 2026-05-03 build was the original Tier-2 build. Since no substantive edits were made in this sweep (HOLDS verdicts), no backup directory is created.

## Per-chunk audit results

| Chunk | Source | Bounds | Latin↔OCR | Apparatus | Markers paired (La/En/defs) | [?] flags | Status string | Verdict |
|---|---|---|---|---|---|---|---|---|
| divisio | pt2 raw | 300–354 ✓ (DIVISIO TEXTUS at ~301 → end of TRACTATIO QUAESTIONUM before SENTENTIARUM LIB. I / ARTICULUS I) | verbatim from OCR; 2-column layout collapsed; COMMENTARIUS rubric + opener (raw 291–299) intentionally dropped per convention | 4 entries from NOTAE AD COMMENTARIUM (printed p.419 right column) | 4 / 4 / 4 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| littera | pt2 raw | 166–290 ✓ (DISTINCTIO XXIV / Cap. unicum heading → end of Lombard cap. unicum on p.419 left column, before COMMENTARIUS opener at line 291) | verbatim; 2-column layout collapsed; Quaracchi marginalia (Quid dicit unus Deus, Quae tres personae, Explicit littera) suppressed; page break correctly placed at "distin- / ctio" | 16 entries consolidated from two NOTAE AD LIBR. SENTENTIARUM blocks (11 on p.418 footer, 5 on p.419-left footer) | 16 / 16 / 16 | 0 | Tier 2 complete 2026-05-03 | HOLDS |

## Totals

- 2 / 2 chunks Tier-2 complete; both HOLD without rebuild
- 20 apparatus entries total, all bilingual (`**La.**` / `**En.**`) with blank line between
- All footnote markers paired exactly across Latin body, English body, and apparatus defs (4+4+4 for divisio, 16+16+16 for littera)
- 0 `[?]` flags in either chunk; no per-chunk ambiguity logs needed for this sweep
- pt1/pt2 boundary: confirmed pt2 is the correct source — d.24 begins on printed p.418, which falls in pt2 (pt2 PDF offset = printed − 410, so printed 418 = pt2 PDF page 8); pt1 raw was not consulted and is not relevant for d.24
- Build smoke-test: `node scripts/build-content.mjs` → "Built content.json: 1 book(s), 422 questions, 350 translated" (clean parse)

## Anomalies / observations

- **First pt2 distinction:** d.24 is the first distinction whose chunks draw entirely from `raw/bonaventure_vol1_pt2_raw.txt`. The source-line citations in both chunks' `transcription_status` and `source` frontmatter correctly identify pt2; no pt1 leakage detected.
- **Apparatus split across two NOTAE blocks:** the littera apparatus has 11 entries footed on p.418 and 5 entries footed on p.419 left column (since the littera continues onto p.419 before the COMMENTARIUS rubric). The chunk's apparatus introduction note documents this split clearly; verified the p.419-left fns (12–16) match the raw OCR block at line 254ff (`Id est, de Fide ad Gratianum`, `Edd. 2,5 addunt Deus trinus vel`, `Dist. XXIII. c. 6`, `Non invenimus in editionibus Isidori`, `Sola Vat. numeralem`).
- **NOTAE AD COMMENTARIUM is on the same printed page (p.419 right column)** as the divisio body and the tail of the littera. The chunk authors correctly partitioned: littera apparatus pulls from NOTAE AD LIBR. SENTENTIARUM (left footer block); divisio apparatus pulls from NOTAE AD COMMENTARIUM (right footer block). No cross-contamination.
- **No rebuild necessary** — both chunks were authored under the disciplined 2026-05-03 regimen with bilingual apparatus already in place; nothing in the d.11+ damage cluster (pre-2026-05-02) applies here.
