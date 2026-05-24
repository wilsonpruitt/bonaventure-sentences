# Next session — **d.13 COMPLETE.** Begin d.14 (pars-1, then pars-2 manual-rescue chunks).

**d.1–d.13 COMPLETE = 157 chunks.** Build: 568 translated, 878 quaestio routes.
Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com since 2026-05-23; per
"deploy after each decade ships" rule, the next live ship is at
end-of-d.20.

## d.13 close-out (2026-05-24)

All nine d.13 chunks Tier-2 complete: `d13-littera`, `d13-divisio`,
`d13-a1-q1`, `d13-a1-q2`, `d13-a2-q1`, `d13-a2-q2`, `d13-a3-q1`,
`d13-a3-q2`, `d13-dubia`. All three Vol II audits clean for d.13
(paraphrase 0 critical / 0 high; apparatus-count 0 flags; headers
3/3 ART, 4/6 QUAEST, 2/4 DUB — no LOSS flag).

## d.14 chunk inventory (next)

d.14 has multi-pars structure (PARS I + PARS II); the auto-chunker
created `d14-p1-*` and `d14-p2-*` chunks per the manual-rescue plan.
Per the boundary-sweep audit (`manual-review/d11-d20-boundary-sweep-audit.md`):
the manual-rescue chunks still in skeleton are `d14-p1-a2-q1`,
`d14-p1-a2-q2`, `d14-p1-a3-q1`, `d14-p1-a3-q2`, `d14-p2-divisio`,
`d14-p2-a1-q3` — plus the normal d.14 skeletons created by the
auto-chunker.

`ls vol2/bon-sent-II-d14-*` will show the full d.14 chunk set; start
by promoting `d14-littera` (Lombard's text for distinction XIV) per
Vol II cadence, then walk pars 1 → pars 2 chunk-by-chunk.

## What to do this session

**Promote `d14-littera`** — the next quaestio in cadence. Per the Vol II
recipe, find printed-page span from chunk frontmatter, extract +
column-band crop, then reconstruct body + apparatus column-by-column.

After d14-littera: walk d.14 chunks in semantic order (divisio → p1
articles → p2 divisio → p2 articles → dubia if any).

## Tooling status

- 450 dpi PDF crops cached for pp.274–333 at `/tmp/colcrop/vol2-p*`.
  Generate p.334+ as needed.
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
