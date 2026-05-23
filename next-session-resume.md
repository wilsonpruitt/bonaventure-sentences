# Next session — Vol II d.11 in progress, **d11-a2-q1 next**.

**d.1–d.10 COMPLETE = 130 chunks. d.11 promotion: 4/9 done**
(d11-divisio + d11-a1-q1 + d11-a1-q2 + d11-a1-q3). Build: 545 translated,
878 quaestio routes. Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com
since 2026-05-23; deploy after each decade ships.

## d.11 chunk inventory + Tier-2 progress

| chunk | lines | wc_la | status |
|---|---|---|---|
| `d11-littera`  | 19518–19627 | 1483 | skeleton |
| `d11-divisio`  | 19629–19657 |  268 | Tier 2 (2026-05-23) |
| `d11-a1-q1`    | 19658–19835 | 2333 | Tier 2 (2026-05-23) |
| `d11-a1-q2`    | 19836–19927 | 1078 | Tier 2 (2026-05-23) |
| `d11-a1-q3`    | 19928–20037 | 1430 | Tier 2 (2026-05-23) |
| `d11-a2-q1`    | 20050–20245 | 2244 | skeleton — **NEXT** |
| `d11-a2-q2`    | 20246–20353 | 1354 | skeleton |
| `d11-a2-q3`    | 20354–20531 | 2231 | skeleton |
| `d11-dubia`    | 20532–20645 | 1470 | skeleton |

## What to do this session

**Promote `d11-a2-q1`** (printed pp.282–?; need ~3 pages).
Title: *Utrum Angelus subtrahat ab homine custodiae beneficium
propter obstinationem* (Whether the Angel withdraws the benefit of
custody from man on account of obstinacy).

This chunk per Vol II convention folds in the ARTICULUS II opener:
"*De eis quae angelicae custodiae sunt annexa.* Consequenter
quaeritur de secundo articulo, scilicet de annexis angelicae
custodiae, et circa hoc quaeruntur tria. Primo quaeritur, utrum
Angelus propter nostram obstinationem subtrahat custodiae
beneficium. — Secundo quaeritur, utrum ex nostra beatificatione
accrescat ei novum gaudium. — Tertio quaeritur, utrum Angelus
custodiens ex damnatione custoditi incurrat aliquod detrimentum."

1. Extract/colcrop pp.283, 284 (and 285 if needed):
   `python3.11 tools/extract-pages.py --volume vol2 --pages 283,284,285
   --dpi 450 && for p in 283 284 285; do python3.11 tools/colcrop.py
   vol2 $p; done`. p.282 crops already at `/tmp/colcrop/vol2-p282-*`.
2. **Page 282 reserved footers carried INTO this chunk per
   cross-chunk page-footer split discipline:**
   - footer ² (`Cod. 1 Angelo custode amplificetur gaudium, sicut
     infra in principio quaest. secundae ponitur.`) → anchors at
     `gaudium²` in the ARTICULUS II divisio.
   - footer ³ (`Vers. 9. — Glossa, quae in hoc et in seq. arg.
     allegatur, est ex Origene, hom. 21. in Ieremiam, n. 12.`) →
     anchors at `Ieremiae quinquagesimo primo³` in obj 1.
   - footer ⁴ (`Locutio obfirmare faciem legitur Lev. 17, 10; Ez.
     4, 3.`) → anchors at `obstinationem⁴` at end of obj 2.
   - d11-a1-q3 already captured p.282 footer ¹; incoming boundary
     into a2-q1 is CLEAN.
3. **Continuous [^N] numbering for a2-q1:** start at [^1] for p.282
   footer ². The three reserved p.282 footers (², ³, ⁴) become
   `[^1]–[^3]`; p.283+ footers continue from `[^4]`.
4. Marginal labels likely present (*Ad oppositum.*, *Fundamenta.*,
   *Solutio oppositorum.*, etc.). Preserve inline italic.
5. Document incoming + outgoing boundary CLEAN status in `## Notes`.
6. Three audits + smoke build, then two-commit rhythm (chunk +
   content.json; this resume note → d11-a2-q2).

## Tooling status

- 450 dpi PDF crops cached for pp.275–282 at `/tmp/colcrop/vol2-p*`
  and `raw/vision/vol2/p-hires-*.png`. p.283+ extraction pending.
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
