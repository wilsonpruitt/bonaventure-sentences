# Next session — **d.13 promotion: 6/9 done.** Begin d13-a3-q1.

**d.1–d.12 COMPLETE = 148 chunks. d.13 promotion: 6/9 done** (d13-littera, d13-divisio, d13-a1-q1, d13-a1-q2, d13-a2-q1, d13-a2-q2).
Build: 565 translated, 878 quaestio routes.
Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com since 2026-05-23; per
"deploy after each decade ships" rule, the next live ship is at
end-of-d.20.

## d.13 chunk inventory

| chunk | lines | wc_la | status |
|---|---|---|---|
| `d13-littera`  | 21842–21990 | 1941 | Tier 2 (2026-05-24) |
| `d13-divisio`  | 21996–22048 |  585 | Tier 2 (2026-05-24) |
| `d13-a1-q1`    | 22053–22247 | 2728 | Tier 2 (2026-05-24) |
| `d13-a1-q2`    | 22248–22436 | 2628 | Tier 2 (2026-05-24) |
| `d13-a2-q1`    | 22445–22585 | 2099 | Tier 2 (2026-05-24) |
| `d13-a2-q2`    | 22586–22883 | 4659 | Tier 2 (2026-05-24) |
| `d13-a3-q1`    | 22894–23121 | 3127 | skeleton — **NEXT** |
| `d13-a3-q2`    | 23122–23351 | 3358 | skeleton |
| `d13-dubia`    | 23352–23549 | 2861 | skeleton |

## What to do this session

**Promote `d13-a3-q1`** — d.13 Article III, Quaestio I:
*Utrum lumen, quod exit a corpore luminoso, sit corpus.* Opens **p.323
L mid** immediately below d13-a2-q2 scholion II.6 — under the centred
"ARTICULUS III." banner with rubric *De lucis effectu et irradiatione*
and the Article opener (*Consequenter quaeritur de lucis effectu et
irradiatione. Et circa hoc quaeruntur duo. Primo… Secundo…*) per the
Vol II convention. Raw lines 22894–23121, ~3127 words. Apparatus-count
heuristic raw=25 — moderate. Body likely spans p.323 lower → p.325.

1. Extract + crop p.324–p.325 (p.323 already cached):
   `python3.11 tools/extract-pages.py --volume vol2 --pages 324-325 --dpi 450`
   then `for p in 324 325; do python3.11 tools/colcrop.py vol2 $p 1660 3 1.8; done`.
2. Body Latin base from IA djvu OCR raw 22894–23121 reconciled against
   PDF column bands. Watch the column-shattered Respondeo per Vol II
   Override.
3. Apparatus: walk every numbered footer per printed page.
4. Three audits + smoke build, then two-commit rhythm (chunk +
   content.json; this resume note → **d13-a3-q2**).

After d13-a3-q1: d13-a3-q2 → d13-dubia. Then d.14 gate opens (caution:
d.14 has multi-pars structure; the chunker created d14-p1-* and
d14-p2-* chunks per the manual-rescue plan).

## Tooling status

- 450 dpi PDF crops cached for pp.274–323 at `/tmp/colcrop/vol2-p*`.
  Generate p.324+ as needed.
- Manual-rescue chunks (d.11–d.20 boundary sweep) still skeleton:
  d16-a1-q2, d18-dubia, d19-littera, d14-p2-divisio, d14-p2-a1-q3,
  d14-p1-a2-q1/q2, d14-p1-a3-q1/q2. Promote in normal Vol II cadence.
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
