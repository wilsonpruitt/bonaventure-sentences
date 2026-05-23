# Next session — Vol II d.11 in progress, **d11-a2-q2 next**.

**d.1–d.10 COMPLETE = 130 chunks. d.11 promotion: 5/9 done**
(d11-divisio + d11-a1-q1 + d11-a1-q2 + d11-a1-q3 + d11-a2-q1). Build:
546 translated, 878 quaestio routes. Vol II d.1–d.10 LIVE on
bonaventure.wrootpress.com since 2026-05-23; deploy after each decade
ships.

## d.11 chunk inventory + Tier-2 progress

| chunk | lines | wc_la | status |
|---|---|---|---|
| `d11-littera`  | 19518–19627 | 1483 | skeleton |
| `d11-divisio`  | 19629–19657 |  268 | Tier 2 (2026-05-23) |
| `d11-a1-q1`    | 19658–19835 | 2333 | Tier 2 (2026-05-23) |
| `d11-a1-q2`    | 19836–19927 | 1078 | Tier 2 (2026-05-23) |
| `d11-a1-q3`    | 19928–20037 | 1430 | Tier 2 (2026-05-23) |
| `d11-a2-q1`    | 20050–20245 | 2244 | Tier 2 (2026-05-23) |
| `d11-a2-q2`    | 20246–20353 | 1354 | skeleton — **NEXT** |
| `d11-a2-q3`    | 20354–20531 | 2231 | skeleton |
| `d11-dubia`    | 20532–20645 | 1470 | skeleton |

## What to do this session

**Promote `d11-a2-q2`** (printed pp.285–?).
Title: *Utrum Angelo custodienti amplificetur gaudium ex
beatificatione custoditi* (Whether joy is increased for the guarding
Angel from the beatification of the one in his custody).

Body opens cleanly on p.285 immediately after the SCHOLION block that
closed d11-a2-q1: "*Secundo quaeritur, utrum ex beatificatione
custoditi Angelo custodienti amplificetur gaudium. Et quod sic,
videtur:*" — then objections 1–6 already visible in cached crops.

1. Extract/colcrop pp.286, 287 (and 288 if needed):
   `python3.11 tools/extract-pages.py --volume vol2 --pages 286,287,288
   --dpi 450 && for p in 286 287 288; do python3.11 tools/colcrop.py
   vol2 $p; done`. p.285 crops already cached at `/tmp/colcrop/vol2-p285-*`.
2. **Page 285 footers belonging to this chunk:** numbered notes 1–8+ on
   p.285 anchor at objections 1ff in the QUAEST. II body — read the
   p.285 R-1 column-band footer block carefully and split per anchor.
   d11-a2-q1 captured nothing from p.285's footer block (SCHOLION I+II
   carry no numbered Quaracchi notes), so all of p.285's numbered
   footers belong to this chunk. Incoming boundary CLEAN.
3. **Continuous [^N] numbering for a2-q2:** start at [^1] for p.285
   footer ¹ (the Luke 15 *Gaudium est Angelis Dei* citation already
   visible in the L-1 band).
4. Marginal labels likely present (*Ad oppositum.*, *Sed contra.*,
   *Pro parte negativa.*, *Fundamenta.*, *Conclusio.*, *Solutio
   oppositorum.*, etc.). Preserve inline italic per Vol II convention.
5. Document incoming + outgoing boundary CLEAN status in `## Notes`.
6. Three audits + smoke build, then two-commit rhythm (chunk +
   content.json; this resume note → d11-a2-q3).

## Tooling status

- 450 dpi PDF crops cached for pp.275–285 at `/tmp/colcrop/vol2-p*`
  and `raw/vision/vol2/p-hires-*.png`. p.286+ extraction pending.
- Manual-rescue chunks created earlier session (d.11–d.20 boundary
  sweep): d18-dubia, d19-littera, d13-a1-q2, d16-a1-q2,
  d14-p2-divisio, d14-p2-a1-q3, d14-p1-a2-q1/q2, d14-p1-a3-q1/q2.
  All are skeleton Tier-1; promote in normal Vol II cadence.
- Pre-promotion boundary sweep log:
  `manual-review/d11-d20-boundary-sweep-audit.md` — all blockers
  cleared 2026-05-23.

## Open project-wide TODOs

- **Next decade polish-blocker fires after d.20.** Three-pass cadence;
  `manual-review/d11-d20-polish-resolution-log.md` will be the log.
- **Vol I site copy** still hardcodes "Volume I" in
  `site/src/app/page.tsx:47,57` — update when Vol II has enough real
  chunks to surface in landing copy.

## Convention reminders

- "keep going" = continue chunk-by-chunk, committing each, no check-ins
  (cf. [[feedback_bonaventure-bucket-e-autopilot]]).
- Tier-2 = literal, not paraphrase, incl. scholia/apparatus.
- Marginal labels (*Ad oppositum.*, *Fundamenta.*, *Ratio …*,
  *Solutio …*, *Notandum.*, *Alia solutio.*, etc.) are preserved inline
  per Vol II convention, NOT promoted to headings.
- Backup before any rebuild: `cp <chunk>.md _backup-<chunk>-pre-<reason>-<YYYYMMDD>/`.
- Vol II offset: `pdf = printed + 22`. Trust running-head text, never
  the OCR'd digits.

Prior session-by-session vol2 history (sessions 1–77) is trimmed per
Wilson's request 2026-05-22; the per-decade resolution logs and chunk
`## Notes` are the durable record. Backup of the pre-trim resume is at
`_backup-resume-pre-trim-20260522.md` if you need to walk back.
