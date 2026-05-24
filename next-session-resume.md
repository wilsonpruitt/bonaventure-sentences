# Next session — **d.12 promotion: 8/9 done**. Begin d12-dubia.

**d.1–d.11 COMPLETE = 139 chunks. d.12 promotion: 8/9 done**
(d12-littera, d12-divisio, d12-a1-q1, d12-a1-q2, d12-a1-q3, d12-a2-q1, d12-a2-q2, d12-a2-q3).
Build: 558 translated, 878 quaestio routes.
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
| `d12-a2-q2`    | 21553–21646 | 1021 | Tier 2 (2026-05-24) |
| `d12-a2-q3`    | 21647–21744 | 1326 | Tier 2 (2026-05-24) |
| `d12-dubia`    | 21745–21841 | 1332 | skeleton — **NEXT** |

## What to do this session

**Promote `d12-dubia`** — d.12 DUBIA CIRCA LITTERAM MAGISTRI. Opens
on p.306 R lower with "DUB. I. In parte ista sunt dubitationes circa
litteram, et primo quaeritur de hoc quod dicit, quod materiam quatuor
elementorum nomine terrae appellavit Moyses…" and bleeds onto p.307+.
Audit-apparatus-count heuristic shows raw=9 footer entries.

1. p.306 crops already cached at /tmp/colcrop/vol2-p306-*.png. Generate
   p.307+ as the body runs:
   `python3.11 tools/extract-pages.py --volume vol2 --pages 307-309 --dpi 450`
   then `for p in 307 308 309; do python3.11 tools/colcrop.py vol2 $p 1660 3 1.8; done`.
2. Body Latin base from IA djvu OCR raw 21745–21841 (+ any bleed past
   line 21841 — extend the range as needed) reconciled against PDF
   column bands.
3. Apparatus: p.306 footers **9 and 10** (Libr. I. de Sacram. p. I. c. 6;
   Gen. 1, 2) are anchored in the dubia text on p.306 R bottom and were
   **reserved for this chunk** — pick them up at the head of the chunk's
   apparatus numbering. Continue with p.307+ footer per-page numbering.
4. Three audits + smoke build, then two-commit rhythm (chunk +
   content.json; this resume note → **d13-littera** to open d.13 gate).

After d12-dubia, **d.13 gate opens.** The d.10 polish-blocker has been
closed; the next polish-blocker is d.20.

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
