# d.21 scaffolds sweep audit (2026-05-08)

## Scope correction

Task description listed three chunks (`divisio`, `littera`, `dubia`). The actual d.21 chunk inventory in `vol1/` is **seven** files:

- `bon-sent-I-d21-littera.md`
- `bon-sent-I-d21-divisio.md`
- `bon-sent-I-d21-a1-q1.md`
- `bon-sent-I-d21-a1-q2.md`
- `bon-sent-I-d21-a2-q1.md`
- `bon-sent-I-d21-a2-q2.md`
- `bon-sent-I-d21-dubia.md`

Per task scope, only the three named chunks were audited in this pass. All seven chunks were rebuilt 2026-05-03 (one day after the d.11+ wave that holds up clean) with per-chunk ambiguity logs already on file in `manual-review/tier2-ambiguities-d21-*.md`. A pre-existing `_backup-d21-pre-rebuild-20260503/` directory already contains the prior versions of all seven chunks; the 2026-05-03 promotion was the original Tier-2 build, so no fresh `_backup-d21-{chunk}-pre-rebuild-20260508/` was needed.

## Per-chunk audit results

| Chunk | Bounds (raw OCR) | Latin↔OCR | Apparatus | Markers paired (LA/EN/defs) | [?] flags | Status string | Verdict |
|---|---|---|---|---|---|---|---|
| littera | 65462–65647 ✓ (DISTINCTIO XXI heading at 65462; ends at "loeis occurrit." before COMMENTARIUS at 65648) | verbatim, spot-checked Cap. I opening + Cap. III ("non inde separatur Pater[?]") | 15 entries (pp.377–378 NOTAE AD LIBR. SENTENTIARUM) | 15 / 15 / 15 | 2 (Pater[?] and the chunk's documented head-trim boundary note) — already logged | Tier 2 complete 2026-05-03 | HOLDS |
| divisio | 65648–65753 ✓ (COMMENTARIUS opener through "Secundo, si vere addatur a parte praedicati.") | verbatim | 5 entries (p.378–379 NOTAE AD COMMENTARIUM) | 5 / 5 / 5 | 0 | Tier 2 complete 2026-05-03 | HOLDS |
| dubia | 66956–67092 ✓ (DUBIA CIRCA LITTERAM MAGISTRI through last "subversionem audientium" before SENTENTIARUM running head + DISTINCTIO XXII at 67093) | verbatim, spot-checked DUB. I, II, III openers and responses | 14 entries (p.386 apparatus) | 14 / 14 / 14 | 0 | Tier 2 complete 2026-05-03 | HOLDS |

## Totals (3 audited chunks)

- 3 / 3 chunks Tier-2 complete
- 34 apparatus entries total, all bilingual (`**La.**` / `**En.**`)
- All footnote markers paired exactly across Latin body, English body, and apparatus defs
- 2 `[?]` flags total, both in `littera`, already documented in `tier2-ambiguities-d21-littera.md` (one inline `Pater[?]` re: spurious OCR comma in Augustine quotation; one is a boundary note, not an in-text flag)
- Inter-chunk OCR boundaries verified clean at every transition (DISTINCTIO XXI heading at 65462; COMMENTARIUS IN DISTINCTIONEM XXI at 65648; DUBIA at 66956; DISTINCTIO XXII at 67093)
- Build smoke-test: `cd site && node scripts/build-content.mjs` → "Built content.json: 1 book(s), 422 questions, 350 translated" (clean parse)

## Anomalies / observations

1. **Task scope undercount**: task description named 3 chunks; corpus has 7. The four `a*-q*` chunks were not audited in this pass per scope; they hold ambiguity logs from 2026-05-03 and are not flagged in any prior audit.
2. **No rebuild needed**: the three audited chunks are not damaged scaffolds. They are fully translated Tier-2 work from 2026-05-03 with verbatim OCR Latin, full bilingual apparatus, and matched marker pairing. Rebuilding would be redundant and would orphan existing `tier2-ambiguities-d21-{divisio,littera,dubia}.md` logs.
3. **No 2026-05-08 backups created**: per workflow, backups only happen when substantive edits land. No edits were necessary. The pre-existing `_backup-d21-pre-rebuild-20260503/` already preserves the prior versions.
4. **No `transcription_status` date bump to 2026-05-08**: workflow says bump only on substantive edits. Audit-only sweeps don't touch the status string.
5. **Marker-pairing regex caveat**: an early naïve check (`\[\^(\d+)\](?!:)`) under-counts body anchors when an anchor is followed by a colon used as punctuation (e.g. `de hac locutione[^2]:`). The corrected check (excluding only line-start `[^N]:` definitions) confirms full pairing on all three chunks. Worth porting back into `tools/audit-formatting.py` if not already there; otherwise future audits will produce false negatives on chunks like d.21 divisio.
6. The 2 `[?]` situations in `littera` are: (a) genuine OCR comma ambiguity in an Augustine quotation, sense unambiguous, reading retained verbatim — accept-as-flagged, no PDF resolution needed; (b) a boundary-trim explanation (not an in-text flag), already part of the chunk's documented chunk-bounds rationale.

## Conclusion

d.21 (the three audited chunks: littera, divisio, dubia) ships as-is. No edits, no rebuilds, no commit needed.
