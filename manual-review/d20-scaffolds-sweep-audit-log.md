# d.20 scaffolds sweep audit (2026-05-08)

## Scope correction

Task description listed three chunks (`divisio`, `littera`, `dubia`). The actual d.20 chunk inventory in `vol1/` is **seven** files:

- `bon-sent-I-d20-littera.md`
- `bon-sent-I-d20-divisio.md`
- `bon-sent-I-d20-a1-q1.md`
- `bon-sent-I-d20-a1-q2.md`
- `bon-sent-I-d20-a2-q1.md`
- `bon-sent-I-d20-a2-q2.md`
- `bon-sent-I-d20-dubia.md`

All seven were rebuilt 2026-05-03 in the same regimen as the d.11+ wave the user noted as holding up (wave was 2026-05-02; d.20 followed one day later). Per-chunk ambiguity logs already exist in `manual-review/tier2-ambiguities-d20-*.md` (7 files).

No prior `_backup-d20-*` directory exists; the 2026-05-03 rebuild was the original Tier-2 build, not a re-rebuild.

## Per-chunk audit results

| Chunk | Bounds | Latin↔OCR | Apparatus | Markers paired (La/En/defs) | [?] flags | Status string | Verdict |
|---|---|---|---|---|---|---|---|
| littera | 63918–64133 ✓ (DISTINCTIO XX → before COMMENTARIUS at 64135) | verbatim | 13 entries, ends correctly at OCR fn 10 "Scilicet in hac et praecedente dist." | 13 / 13 / 13 | 2 (ab illo[?]) — logged | Tier 2 complete 2026-05-03 | HOLDS |
| divisio | 64135–64190 ✓ (COMMENTARIUS opener through last "intensionem potentiae") | verbatim | 6 entries from p.368 footer | 6 / 6 / 6 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| a1-q1 | 64195–64463 ✓ (ARTICULUS I / QUAESTIO I → before QUAESTIO II) | verbatim, spot-checked openers and 4 obj./4 contra | 15 entries (3 from p.368 + 12 from p.369) | 15 / 15 / 15 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| a1-q2 | 64464–64639 ✓ (QUAESTIO II → before ARTICULUS II at 64640) | verbatim, scholion vision-verified per status string | 16 entries (pp.370–371) | 16 / 16 / 16 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| a2-q1 | 64640–64923 ✓ (ARTICULUS II opener → before QUAESTIO II at 64924) | verbatim | 17 entries (pp.371–373) | 17 / 17 / 17 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| a2-q2 | 64924–65229 ✓ (QUAESTIO II → before DUBIA at 65230) | verbatim | 29 entries (pp.373–375) | 29 / 29 / 29 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| dubia | 65230–65461 ✓ (DUBIA opener → before DISTINCTIO XXI) | verbatim | 17 entries (p.375 7–9, p.376 1–12, p.377 1–2) | 17 / 17 / 17 | 2 (melior[?] in fn 15) — logged | Tier 2 complete 2026-05-03 | HOLDS |

## Totals

- 7 / 7 chunks Tier-2 complete
- 113 apparatus entries total, all bilingual (`**La.**` / `**En.**`)
- All footnote markers paired exactly across Latin body, English body, and apparatus defs
- 4 `[?]` flags total, both already documented in per-chunk ambiguity logs
- Inter-chunk OCR boundaries verified clean at every transition (DISTINCTIO XX, COMMENTARIUS, ARTICULUS I, QUAESTIO II of art. 1, ARTICULUS II, QUAESTIO II of art. 2, DUBIA, end-of-d.20)
- Build smoke-test: `node scripts/build-content.mjs` → "Built content.json: 1 book(s), 422 questions, 350 translated" (clean parse)

## Anomalies / observations

1. **Task scope undercount**: task description named 3 chunks; corpus has 7. No work done on phantom files.
2. **No rebuild needed**: the d.20 chunks were not damaged scaffolds; they are fully translated Tier-2 work from 2026-05-03 and pass the same gates the d.11+ wave passed. Treating them as scaffolds-to-rebuild would have been redundant work and would have orphaned the existing `tier2-ambiguities-d20-*.md` logs.
3. **No backups created**: per workflow, backups are only made when substantive edits happen. No edits were necessary.
4. **No `transcription_status` date bump to 2026-05-08**: the workflow says to bump only on substantive edits. Audit-only sweeps don't touch the status.
5. The two `[?]` flags (littera "ab illo[?]", dubia "*melior*[?]" in fn 15) are both genuine OCR-illegible spots already documented; resolution requires PL 192 / cleaner Quaracchi copy, deferred per existing log notes.

## Conclusion

d.20 ships as-is. No edits, no rebuilds, no commit needed.
