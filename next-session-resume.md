# Next session — **d.12 promotion: 6/9 done**. Begin d12-a2-q2.

**d.1–d.11 COMPLETE = 139 chunks. d.12 promotion: 6/9 done**
(d12-littera, d12-divisio, d12-a1-q1, d12-a1-q2, d12-a1-q3, d12-a2-q1).
Build: 556 translated, 878 quaestio routes.
Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com since 2026-05-23; per
"deploy after each decade ships" rule, the next live ship is at
end-of-d.20.

## d.12 chunk inventory

| chunk | lines | wc_la | status |
|---|---|---|---|
| `d12-littera`  | 20609–20739 (eff.) | 1128 | Tier 2 (2026-05-23) |
| `d12-divisio`  | 20733–20776 (eff.) |  432 | Tier 2 (2026-05-23) |
| `d12-a1-q1`    | 20780–20931 (eff.) | 2094 | Tier 2 (2026-05-23) |
| `d12-a1-q2`    | 20932–21186 | 3687 | Tier 2 (2026-05-23) |
| `d12-a1-q3`    | 21187–21396 | 3087 | Tier 2 (2026-05-23) |
| `d12-a2-q1`    | 21397–21552 (eff., incl. ART II opener) | 1822 | Tier 2 (2026-05-24) |
| `d12-a2-q2`    | 21553–21646 |  ~   | skeleton — **NEXT** |
| `d12-a2-q3`    | 21647–21744 |  ~   | skeleton |
| `d12-dubia`    | 21745–21841 | 1332 | skeleton |

## What to do this session

**Promote `d12-a2-q2`** — d.12 Article II, Quaestio II: per the
audit-apparatus-count heuristic the raw range 21553–21646 has ~13
footer entries; expect body to span p.304 R lower → p.305 (and
possibly into p.306). The opening line on p.304 R is "QUAESTIO II.
*Utrum materia prima producta sit in die, an ante omnem diem.*" with
"Secundo quaeritur de informi materia quantum..." beginning the body.

1. Generate crops for p.305 (and p.306 if needed):
   `python3.11 tools/extract-pages.py --volume vol2 --pages 305-306 --dpi 450`
   then `python3.11 tools/colcrop.py vol2 305 1660 3 1.8` (and 306).
   p.304 crops already cached at /tmp/colcrop/vol2-p304-*.png.
2. Body Latin base from IA djvu OCR raw 21553–21646 + reconcile
   against PDF column bands.
3. Apparatus: walk every numbered footer entry per printed page. p.304
   already shows footers 1–8 anchoring in a2-q2's body (Genesis,
   Cap. 1.1, Cap. 8, Loan., Epist. 1 Tim., etc. — see p.304 R-2 crop).
4. Three audits + smoke build, then two-commit rhythm (chunk +
   content.json; this resume note → **d12-a2-q3**).

After d12-a2-q2, continue d.12 in order: a2-q3 → dubia.

## Tooling status

- 450 dpi PDF crops cached for pp.274–304 at `/tmp/colcrop/vol2-p*`.
  Generate p.305+ as needed.
- Manual-rescue chunks created earlier (d.11–d.20 boundary sweep):
  d18-dubia, d19-littera, d13-a1-q2, d16-a1-q2, d14-p2-divisio,
  d14-p2-a1-q3, d14-p1-a2-q1/q2, d14-p1-a3-q1/q2. All skeleton
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
