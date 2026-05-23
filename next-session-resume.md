# Next session — Vol II d.11 in progress, **d11-a1-q2 next**.

**d.1–d.10 COMPLETE = 130 chunks. d.11 promotion: 2/9 done**
(d11-divisio + d11-a1-q1). Build: 543 translated, 878 quaestio routes.
Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com since 2026-05-23;
deploy after each decade ships.

## d.11 chunk inventory + Tier-2 progress

| chunk | lines | wc_la | status |
|---|---|---|---|
| `d11-littera`  | 19518–19627 | 1483 | skeleton |
| `d11-divisio`  | 19629–19657 |  268 | Tier 2 (2026-05-23) |
| `d11-a1-q1`    | 19658–19835 | 2333 | **Tier 2 (2026-05-23)** |
| `d11-a1-q2`    | 19836–19927 | 1078 | skeleton — **NEXT** |
| `d11-a1-q3`    | 19928–20037 | 1430 | skeleton |
| `d11-a2-q1`    | 20050–20245 | 2244 | skeleton |
| `d11-a2-q2`    | 20246–20353 | 1354 | skeleton |
| `d11-a2-q3`    | 20354–20531 | 2231 | skeleton |
| `d11-dubia`    | 20532–20645 | 1470 | skeleton |

## What to do this session

**Promote `d11-a1-q2`** (printed p.279, PDF 301; possibly bleeding to
p.280). Title: *Utrum competens fuerit, Angelum deputari ad custodiam
hominis conditi.* (i.e. integral, pre-fall man).

1. Extract/colcrop p.280 if not done
   (`python3.11 tools/extract-pages.py --volume vol2 --pages 280
   --dpi 450 && python3.11 tools/colcrop.py vol2 280`). p.279 crops
   already exist from this session.
2. **Page 279 reserved footers (carried by this chunk per cross-chunk
   page-footer split discipline):**
   - ¹ *Vide infra d. XXIV. lit. Magistri, c. 2. et XXV. c. 6.*
     (anchors body opener at *defectus*¹)
   - ² *Cfr. supra pag. 45, nota 5. — Cod. cc et ed. 1 per peccatum.*
     (anchors *peccatum*²)
   - ³ *Vers. 10. — Verba Hieronymi sunt etiam in lit. Magistri, c. 1.*
     (anchors *Angeli eorum*³)
   These were noted in d11-a1-q1 promotion notes; pick them up at
   the top of this chunk's apparatus.
3. **Continuous [^N] numbering:** start at [^1] for p.279 footer ¹;
   work through p.279 then any p.280 footers. Quaracchi restarts
   numbering each page but the chunk's [^N] is continuous.
4. Marginal labels probably present (cf. d11-a1-q1 used Fundamenta /
   Ad oppositum / Ratio* / Solutio* / Notandum). Preserve inline italic.
5. Document incoming + outgoing boundary CLEAN status in `## Notes`.
6. Three audits + smoke build, then two-commit rhythm (chunk +
   content.json; this resume note → d11-a1-q3).

## Tooling status

- 450 dpi PDF crops cached for pp.275–280 at `/tmp/colcrop/vol2-p*`
  and `raw/vision/vol2/p-hires-*.png`.
- Manual-rescue chunks created this session (d.11–d.20 boundary sweep):
  d18-dubia, d19-littera, d13-a1-q2, d16-a1-q2, d14-p2-divisio,
  d14-p2-a1-q3, d14-p1-a2-q1/q2, d14-p1-a3-q1/q2. All are skeleton
  Tier-1; promote in normal Vol II cadence.
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
