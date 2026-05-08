# d.17 scaffolds sweep audit log (2026-05-08)

Sweep covering all 13 chunks of distinction 17 (multi-pars):

```
bon-sent-I-d17-littera.md
bon-sent-I-d17-p1-divisio.md
bon-sent-I-d17-p1-a1-q1.md
bon-sent-I-d17-p1-a1-q2.md
bon-sent-I-d17-p1-a1-q3.md
bon-sent-I-d17-p1-a1-q4.md
bon-sent-I-d17-p1-dubia.md
bon-sent-I-d17-p2-divisio.md
bon-sent-I-d17-p2-a1-q1.md
bon-sent-I-d17-p2-a1-q2.md
bon-sent-I-d17-p2-a1-q3.md
bon-sent-I-d17-p2-a1-q4.md
bon-sent-I-d17-p2-dubia.md
```

The task brief listed 5 chunks (`littera, p1-divisio, p1-dubia, p2-divisio, p2-dubia`); the actual repository carries 13 d.17 chunks (the 8 quaestiones in addition to the 5 named). All 13 were audited.

Methodology: per-chunk verify line bounds against `raw/bonaventure_vol1_raw.txt`; spot-check Latin body against the OCR slice; spot-check apparatus entries against the `NOTAE AD COMMENTARIUM` blocks; verify Latin/English/Apparatus anchor parity programmatically (`/tmp/d17_anchor_audit_v2.py`); inspect for `[?]` flags and confirm they are logged.

A pre-existing partial backup directory `vol1/_backup-d17-pre-rebuild-20260502/` covers the p2 q1–q4 + p2-dubia chunks from the prior 2026-05-02 wave. No new substantive edits were made on 2026-05-08, so no `_backup-d17-*-pre-rebuild-20260508/` directory was created.

Build smoke-test: `cd site && node scripts/build-content.mjs` → `Built content.json: 1 book(s), 422 questions, 350 translated`. Clean.

## Boundary chain (verified contiguous against raw OCR)

| Chunk | Range | Start line evidence | End line evidence |
|---|---|---|---|
| littera | 51999–52651 | L51999 `DISTINGTIO XVII.` (CAP. I opens) | L52651 blank before `COMMENTARIUS IN DISTINCTIONEM XVII.` at 52652 |
| p1-divisio | 52652–52771 | L52652 `COMMENTARIUS IN DISTINCTIONEM XVII.` | L52771 blank before `ARTICULUS UNICUS` at 52772 |
| p1-a1-q1 | 52776–53400 | L52776 `QUAESTIO I.` | L53400 blank before `QUAESTIO II.` at 53401 |
| p1-a1-q2 | 53401–53714 | L53401 `QUAESTIO II.` | L53714 blank before `QU.ESTIO III.` (OCR garble) at 53715 |
| p1-a1-q3 | 53715–54017 | L53715 `gl!.\ESTIO [11.` (= `QUAESTIO III`, OCR garble) | L54017 blank before `QUAESTIO IV.` at 54018 |
| p1-a1-q4 | 54018–54528 | L54018 `QUAESTIO IV.` | L54528 blank before `DUBIA r.IRCA LITTER.VM M.UJISTRI.` at 54529 |
| p1-dubia | 54529–54959 | L54529 `DUBIA CIRCA LITTERAM MAGISTRI.` | L54959 — `Pars II.` at 54960 (running head transition) |
| p2-divisio | 54967–55018 | L54967 `DIVISIO TEXTUS.` | L55018 blank before `ARTICULUS UNICUS.` at 55019 |
| p2-a1-q1 | 55022–55480 | L55022 `QUAESTIO I.` | L55480 blank before `QLWESTIO 11.` (OCR garble) at 55481 |
| p2-a1-q2 | 55481–55906 | L55481 `QLWESTIO 11.` (= QUAESTIO II) | L55906 blank before `QUAESTIO III.` at 55907 |
| p2-a1-q3 | 55907–56281 | L55907 `QUAESTIO III.` | L56281 blank before `QUAESTIO IV.` at 56282 |
| p2-a1-q4 | 56282–56634 | L56282 `QUAESTIO IV.` | L56634 blank before `DrB. L` at 56635 |
| p2-dubia | 56635–56763 | L56635 `DrB. L` (= DUB. I) | L56763 blank before `DISTINCTIO XVIII.` at 56764 |

All bounds verified clean. No leakage; the chain runs unbroken from the d.17 littera through the p2 dubia.

## Apparatus parity (programmatic)

Anchor-parity script `/tmp/d17_anchor_audit_v2.py` matches `[^N]` body anchors (Latin and English) to `[^N]:` apparatus definitions. All 13 chunks: perfect parity, no missing-anchor or orphaned-def cases.

| Chunk | Latin anchors | English anchors | Apparatus defs |
|---|---|---|---|
| littera | 61 | 61 | 61 |
| p1-divisio | 5 | 5 | 5 |
| p1-a1-q1 | 41 | 41 | 41 |
| p1-a1-q2 | 22 | 22 | 22 |
| p1-a1-q3 | 19 | 19 | 19 |
| p1-a1-q4 | 21 | 21 | 21 |
| p1-dubia | 40 | 40 | 40 |
| p2-divisio | 4 | 4 | 4 |
| p2-a1-q1 | 25 | 25 | 25 |
| p2-a1-q2 | 35 | 35 | 35 |
| p2-a1-q3 | 30 | 30 | 30 |
| p2-a1-q4 | 26 | 26 | 26 |
| p2-dubia | 10 | 10 | 10 |
| **TOTAL** | **339** | **339** | **339** |

Bilingual `**La.**` / `**En.**` structure consistent across every entry. No fabricated apparatus detected on spot-checks (entries [^1]–[^10] of p1-a1-q1 traced verbatim to OCR raw 52828–52844 and surrounding; entries [^1]–[^8] of p2-a1-q1 traced to OCR raw 55052–55612; entries [^1]–[^10] of p1-a1-q3 traced to OCR raw 53785+ apparatus block; littera entries [^1]–[^61] are the same set audited and confirmed clean during the 2026-05-02 wave).

## Per-chunk verdicts

### bon-sent-I-d17-littera.md — CLEAN

- Bounds 51999–52651 verified — opens at `DISTINGTIO XVII. Pars 1.` and closes at the final apparatus continuation before `COMMENTARIUS IN DISTINCTIONEM XVII.`. Apparatus blockquote intro on line 155 (one extra `**La.**` count comes from this single intro paragraph; the 61 actual entries match `transcription_status`).
- 61 entries, all paired (La/En), all body-anchored both Latin and English. Fresh 2026-05-02 rebuild holds up.
- No `[?]` flags. No new edits.

### bon-sent-I-d17-p1-divisio.md — CLEAN

- Bounds 52652–52771. Latin body matches OCR for the prefatory rubric, sub-part listing, and 4-question TRACTATIO QUAESTIONUM listing.
- 5 NOTAE entries; all body-anchored.

### bon-sent-I-d17-p1-a1-q1.md — CLEAN (with stale `transcription_status` count)

- Bounds 52776–53400. Q I, "Utrum praeter caritatem increatam poni debeat habitus caritatis creatus."
- File contains 41 apparatus entries (all paired, body-anchored). `transcription_status` reports "32 entries". This is a stale count string only — the apparatus content itself is correct and traceable to OCR. Disposition: leave as-is (cosmetic frontmatter drift, not load-bearing; build pipeline does not parse the count). Flagged here for the record. **Do not alter without re-counting.**
- No `[?]` flags.

### bon-sent-I-d17-p1-a1-q2.md — CLEAN

- Bounds 53401–53714. Q II, "Utrum caritas diligenda sit ex caritate."
- 22 entries paired and anchored. `transcription_status` count matches.

### bon-sent-I-d17-p1-a1-q3.md — CLEAN

- Bounds 53715–54017. Q III, "Utrum quis certitudinaliter scire possit, se esse in caritate."
- 19 entries paired and anchored. `transcription_status` count matches.

### bon-sent-I-d17-p1-a1-q4.md — CLEAN

- Bounds 54018–54528. Q IV, "Utrum caritas in universali sit cognoscibilis etiam a non habente eam."
- 21 entries paired and anchored. `transcription_status` count matches.

### bon-sent-I-d17-p1-dubia.md — CLEAN

- Bounds 54529–54959. Six DUBIA over the Lombard text of pars I.
- 40 entries paired and anchored. The frontmatter notes the auto-chunker boundary fix (extension from 54577 → 54959); confirmed the extended range matches OCR through `Pars II.` at 54960.

### bon-sent-I-d17-p2-divisio.md — CLEAN

- Bounds 54967–55018. Pars II preface + DIVISIO TEXTUS + 4-question TRACTATIO listing.
- 4 NOTAE entries paired and anchored. `transcription_status` count matches.

### bon-sent-I-d17-p2-a1-q1.md — CLEAN (with stale `transcription_status` count)

- Bounds 55022–55480. Q I, "Utrum caritas secundum substantiam augeri possit."
- File contains 25 apparatus entries; `transcription_status` reports "12 entries". Same stale-count case as p1-a1-q1. Verified no fabrication: entries [^1] (Augustine *Epist.* 189), [^3] (Aristotle *de Gener. et Corrupt.*), [^6] (Gilbert *de Sex princ.*) all map to OCR raw 55052+ apparatus block. **Do not alter without re-counting.**
- No `[?]` flags. (`tier2-ambiguities-d17p2-q1.md` already exists from the 2026-05-02 wave.)

### bon-sent-I-d17-p2-a1-q2.md — CLEAN

- Bounds 55481–55906. Q II, "Quomodo caritas augeatur."
- 35 entries paired and anchored. `transcription_status` count matches.

### bon-sent-I-d17-p2-a1-q3.md — CLEAN (1 flagged ambiguity, already logged)

- Bounds 55907–56281. Q III, "Utrum caritas possit diminui."
- 30 entries paired and anchored.
- One `[?]` flag in apparatus [^18] (`In corp. praeced. n. [?]`) — already documented in `manual-review/tier2-ambiguities-d17p2-q3.md`. No further action this sweep.

### bon-sent-I-d17-p2-a1-q4.md — CLEAN

- Bounds 56282–56634. Q IV, "Utrum caritas terminum habeat in augmento."
- 26 entries paired and anchored. `transcription_status` count matches.

### bon-sent-I-d17-p2-dubia.md — CLEAN

- Bounds 56635–56763. Six DUBIA over the Lombard text of pars II, ending at `DISTINCTIO XVIII.` boundary.
- 10 entries paired and anchored. `transcription_status` count matches.

## Anomalies / non-load-bearing notes

1. **Stale entry counts in two `transcription_status` strings**: p1-a1-q1 reports "32 entries" (actual: 41); p2-a1-q1 reports "12 entries" (actual: 25). Apparatus content itself is verified clean; counts in the status string drifted out of date during the 2026-05-02 rebuild. Not edited under this sweep (per "commit nothing" instruction). Flag for the next polish-decade pass to refresh.

2. **OCR garbles in QUAESTIO heading lines** (`QU.ESTIO III.`, `QLWESTIO 11.`, `gl!.\ESTIO [11.`): correctly silently corrected in chunks per CLAUDE.md guidance; flagged here as a pattern observation, not a defect.

3. **Backup directory naming**: `vol1/_backup-d17-pre-rebuild-20260502/` covers only the p2 quaestiones + p2-dubia. The p1 quaestiones + littera + p1-dubia + p1-divisio + p2-divisio rebuild artifacts from 2026-05-02 are not in that directory; if a future rollback is ever needed for those, git history at the 2026-05-02 commit would be the source. No action required this sweep.

## Totals

- Chunks audited: **13 / 13**
- Chunks clean: **13 / 13**
- Substantive edits made: **0** (per "commit nothing" instruction; status-string drift logged but not corrected)
- New `[?]` flags introduced: **0**
- New ambiguity logs created: **0** (existing d17p2 logs cover the only outstanding `[?]`)
- Apparatus entries verified: **339** (perfect Latin/English/def parity)
- Build smoke-test: **PASS** (`Built content.json: 1 book(s), 422 questions, 350 translated`)

d.17 holds up cleanly under the 2026-05-08 re-sweep, consistent with the auditor's prior expectation that post-2026-05-02 fresh rebuilds (d.11+ window) are uniformly clean. No rebuild work needed.
