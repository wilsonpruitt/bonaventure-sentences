# d.19 scaffolds sweep audit log (2026-05-08)

Sweep auditor: scaffold-only chunks (`littera`, `p1-divisio`, `p1-dubia`, `p2-divisio`, `p2-dubia`). The four `pN-a1-qN` quaestio chunks are full quaestiones and were out of scope for this sweep.

All five scaffolds were rebuilt 2026-05-03 (existing backup at `vol1/_backup-d19-pre-rebuild-20260503/`). This sweep verifies whether the 2026-05-03 rebuilds hold up against the **wave 1+2 damage cluster** (pre-2026-05-02 paraphrase / fabricated apparatus). Verdict: they hold up. One mechanical formatting fix landed.

## Per-chunk verdict

| chunk | bounds | Latin (OCR) | Apparatus | anchor parity | [?] flags | verdict |
|---|---|---|---|---|---|---|
| `bon-sent-I-d19-littera.md` | OCR 59285–60178 confirmed (start `DISTINCTIO XIX`, end `noii superel magnitudino`) | verbatim from raw OCR with vision-OCR fallback for damaged p.336 | 56 entries, full **La.**/**En.** structure, all anchors covered | La 56 == En 56 == Apparatus 56 | 3 inline `[?]` (logged in `tier2-ambiguities-d19-littera.md`, 64 lines) | HOLDS |
| `bon-sent-I-d19-p1-divisio.md` | OCR 60181–60281 confirmed (start `COMMENTARIUS IN DISTINCTIONEM XIX`, end `cum circumincessione`) | clean | 7 entries, full **La.**/**En.** | La/En/Ap = 7/7/7 | 0 | HOLDS |
| `bon-sent-I-d19-p1-dubia.md` | OCR 61568–62049 confirmed (start `DUB. 1.`, end `non sit ibi plus`) | clean (Dub I–XI) | 37 entries, full **La.**/**En.** | La/En/Ap = 37/37/37 | 0 | HOLDS (with one minor formatting fix — see below) |
| `bon-sent-I-d19-p2-divisio.md` | OCR 62050–62184 confirmed (start `COMMENTARIUS IN DISTINCTIONEM XIX`, end after `secundum numerum`) | clean | 10 entries, full **La.**/**En.** | La/En/Ap = 10/10/10 | 0 | HOLDS |
| `bon-sent-I-d19-p2-dubia.md` | OCR 63762–63917 confirmed (start `DUB. 1.` of pars-2 dubia, end after `corporeis plus … in una`) | clean (Dub I–IV) | 19 entries, full **La.**/**En.** | La/En/Ap = 19/19/19 | 0 | HOLDS |

## Per-pars findings

### Pars 1 (printed pp. 341–353; chunks: littera covers Lombard pp. 335–341, then p1-divisio, then four quaestiones, then p1-dubia)
- Wave-1+2 damage check: no fabricated Latin, no missing apparatus, no paraphrased apparatus entries. All 100 apparatus entries across the three scaffolds (`littera` 56 + `p1-divisio` 7 + `p1-dubia` 37) follow `**La.** … **En.** …` structure.
- Inline `[?]` flags only in `littera` (3 occurrences) — all genuinely ambiguous OCR garbles (e.g. `magnitudine[?]` p.335; `distinguantur[?]` / `personae[?]` p.339), already logged in `tier2-ambiguities-d19-littera.md`.
- **One real defect found and fixed**: `p1-dubia` had English-section page-break parity gap. Latin section had `<!-- page 350 -->` and `<!-- page 351 -->` markers (plus 352 and 353 mid-paragraph); English section had only 352 and 353 (missing 350 at top, 351 between Dub I question and `**I respond:**`). Added the two missing English markers at parallel positions. Backup at `vol1/_backup-d19-p1-dubia-pre-rebuild-20260508/`. `transcription_status` updated with the 2026-05-08 amendment.

### Pars 2 (printed pp. 354–366; chunks: p2-divisio, four quaestiones, p2-dubia)
- Wave-1+2 damage check: clean. All 29 apparatus entries (`p2-divisio` 10 + `p2-dubia` 19) follow bilingual structure.
- No `[?]` flags in either scaffold.
- No missing page breaks.

## Totals

- **Scaffolds audited**: 5
- **Verdicts**: 5 HOLD (no rebuild needed)
- **Mechanical fixes landed**: 1 (English page-break parity in `p1-dubia`)
- **Substantive backups created this sweep**: 1 (`_backup-d19-p1-dubia-pre-rebuild-20260508/`)
- **Apparatus entries verified**: 129 (56 + 7 + 37 + 10 + 19), all bilingual `**La.**/**En.**`
- **`[?]` flags inline**: 3 (all in littera, all logged)
- **Build smoke-test**: clean (`Built content.json: 1 book(s), 422 questions, 350 translated`)

## Anomalies / curiosities (not defects)

- `littera` apparatus entry `[^4]` contains an embedded inline editorial gloss using `[^[?]:` syntax inside the `**En.**` line. This is unusual but parses cleanly (the bracket form only triggers a footnote def when at column 0). Left as-is; no risk to build or rendering. If the renderer gets pickier later, escape the inner bracket pair.
- All scaffold chunks except `littera` follow the same "page-breaks in Latin section only" convention used in d.17 / d.18 scaffolds. Now that `p1-dubia` has been brought into per-section parity, only `littera` and `p1-dubia` have page-breaks in both languages; the three `divisio` and `p2-dubia` chunks place page-breaks only in Latin (corpus-consistent for short scaffolds that fit on ≤ 2 pages).

## OCR slice spot-checks

| chunk | start line | start text | end line | end text |
|---|---|---|---|---|
| littera | 59285 | `DISTINCTIO XIX.` | 60178 | `superel magnitudino.` |
| p1-divisio | 60181 | `COMMENTARIUS m M8TINCTI0NEM XIX.` | 60281 | `cum circumincessione.` |
| p1-dubia | 61568 | `DUB. 1.` | 62049 | `tas in suhstantia faciat identitatem,` (start) / `quamvis non sit ibi plus` (end at 62049 confirmed) |
| p2-divisio | 62050 | `COMMENTARIUS IN DISTINCTIONEM XIX.` | 62184 | (after the four-question listing) |
| p2-dubia | 63762 | `DUB. 1.` (pars 2) | 63917 | `non sit ibi plus` |

All slice bounds match chunk content.
