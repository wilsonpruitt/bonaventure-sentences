# Next session — Vol II d.11 in progress, **d11-a1-q3 next**.

**d.1–d.10 COMPLETE = 130 chunks. d.11 promotion: 3/9 done**
(d11-divisio + d11-a1-q1 + d11-a1-q2). Build: 544 translated, 878 quaestio routes.
Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com since 2026-05-23;
deploy after each decade ships.

## d.11 chunk inventory + Tier-2 progress

| chunk | lines | wc_la | status |
|---|---|---|---|
| `d11-littera`  | 19518–19627 | 1483 | skeleton |
| `d11-divisio`  | 19629–19657 |  268 | Tier 2 (2026-05-23) |
| `d11-a1-q1`    | 19658–19835 | 2333 | Tier 2 (2026-05-23) |
| `d11-a1-q2`    | 19836–19927 | 1078 | **Tier 2 (2026-05-23)** |
| `d11-a1-q3`    | 19928–20037 | 1430 | skeleton — **NEXT** |
| `d11-a2-q1`    | 20050–20245 | 2244 | skeleton |
| `d11-a2-q2`    | 20246–20353 | 1354 | skeleton |
| `d11-a2-q3`    | 20354–20531 | 2231 | skeleton |
| `d11-dubia`    | 20532–20645 | 1470 | skeleton |

## What to do this session

**Promote `d11-a1-q3`** (printed p.280 right column → p.281+).
Title: *Utrum Christus habuerit Angelum custodem* (Whether Christ
had a guardian Angel).

1. Extract/colcrop p.281 (and p.282 if needed):
   `python3.11 tools/extract-pages.py --volume vol2 --pages 281,282
   --dpi 450 && python3.11 tools/colcrop.py vol2 281 && python3.11
   tools/colcrop.py vol2 282`. p.280 crops already exist from this
   session at `/tmp/colcrop/vol2-p280-{L,R}-{0..2}.png`.
2. **Page 280 reserved footers carried INTO this chunk by q3 per
   cross-chunk page-footer split discipline:**
   - The q3 body opens on p.280 right column with "QUAESTIO III.
     *Utrum Christus habuerit Angelum custodem*. Tertio quaeritur,
     utrum aliquis Angelus deputatus fuerit ad custodiam Christi…"
     followed by objections containing markers `Psalmi⁶`,
     `confortans eum⁷`, and `bonum⁸` (the Eccli. 33,15 cite).
   - Footers on p.280 that anchor in q3 (not q2): footer ⁶
     (`Psalm. 90, 11. — Glossam vide apud Augustinum in hunc
     locum, serm. 2.`), ⁷ (`Vers. 43. — Bedae verba sunt ex
     Comment. ipsius super hunc locum, et in textu originali
     legitur: In documento ergo utriusque naturae ei Angeli
     ministrasse… describitur.`), ⁸ (`Hebr. 2, 9: Eum autem, qui
     modico quam Angeli minoratus est, videmus Iesum, propter
     passionem mortis etc.`), ⁹ (`Eccli. 33, 15. — Sequens textus
     est Matth. 4, 1.`).
   - q2 already captured p.280 footers 1–5 (`perdere¹`,
     `commoveri²`, `peccatum³` (end of Ad 3), `homo⁴`,
     `multiplicare⁵`); incoming boundary into q3 is CLEAN.
3. **Continuous [^N] numbering for q3:** start at [^1] for the
   first footer that q3 anchors. The four reserved p.280 footers
   (⁶, ⁷, ⁸, ⁹) become `[^1]–[^4]`; p.281 footers continue from
   `[^5]`.
4. Marginal labels likely present (cf. q1/q2 pattern: *Ad
   oppositum.*, *Fundamenta.*, *Solutio oppositorum.*, etc.).
   Preserve inline italic.
5. Document incoming + outgoing boundary CLEAN status in `## Notes`.
6. Three audits + smoke build, then two-commit rhythm (chunk +
   content.json; this resume note → d11-a2-q1).

## Tooling status

- 450 dpi PDF crops cached for pp.275–280 at `/tmp/colcrop/vol2-p*`
  and `raw/vision/vol2/p-hires-*.png`. p.281+ extraction pending.
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
