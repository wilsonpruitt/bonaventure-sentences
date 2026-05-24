# Next session — **d.12 COMPLETE (9/9). d.13 gate OPEN.** Begin d13-littera.

**d.1–d.12 COMPLETE = 148 chunks.**
Build: 559 translated, 878 quaestio routes.
Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com since 2026-05-23; per
"deploy after each decade ships" rule, the next live ship is at
end-of-d.20.

## d.13 chunk inventory

| chunk | lines | wc_la | status |
|---|---|---|---|
| `d13-littera`  | 21842–21990 | 1941 | skeleton — **NEXT** |
| `d13-divisio`  | 21996–22048 |  585 | skeleton |
| `d13-a1-q1`    | 22053–22247 | 2728 | skeleton |
| `d13-a1-q2`    | 22248–22436 | 2628 | skeleton (manual-rescue) |
| `d13-a2-q1`    | 22445–22585 | 2099 | skeleton |
| `d13-a2-q2`    | 22586–22883 | 4659 | skeleton |
| `d13-a3-q1`    | 22894–23121 | 3127 | skeleton |
| `d13-a3-q2`    | 23122–23351 | 3358 | skeleton |
| `d13-dubia`    | 23352–23549 | 2861 | skeleton |

## What to do this session

**Promote `d13-littera`** — d.13 Lombard text (CAP. I–VII), De generali
informatione materiae per formam communem lucis. Opens p.308 R lower
("DISTINCTIO XIII. Cap. I. De primo distinctionis opere. Prima autem
distinctionis operatio fuit formatio lucis…") and runs through pp.309–
310. ~1941 words of Latin; substantial Lombard chapter — likely a
one-session job per Vol II littera convention.

1. Generate PDF crops:
   `python3.11 tools/extract-pages.py --volume vol2 --pages 308-311 --dpi 450`
   then `for p in 308 309 310 311; do python3.11 tools/colcrop.py vol2 $p 1660 3 1.8; done`
   (p.308 crops already cached; p.309 onwards new). Note p.308 R is
   shared between `d12-dubia` (upper) and this chunk (lower starting
   from "DISTINCTIO XIII." banner).
2. Body Latin base from IA djvu OCR raw 21842–21990 reconciled
   against PDF column bands. The chunker stops at line 21990 but the
   Lombard text continues — extend if needed; the next semantic break
   is the "COMMENTARIUS IN DISTINCTIONEM XIII." banner on p.310 (raw
   ~21996, owned by `d13-divisio`).
3. Apparatus: Lombard littera apparatus uses "NOTAE AD LIBR.
   SENTENTIARUM" footer block (distinct from Bonaventure's "NOTAE AD
   COMMENTARIUM"). p.308 R footer 6 is owned by `d12-dubia`; p.308
   "NOTAE AD LIBR. SENTENTIARUM" notes 1–4 onwards are this chunk's.
   Per-page numbering restarts. Use the `d11-littera` and `d12-littera`
   Notes blocks as templates for the littera-apparatus convention.
4. Three audits + smoke build, then two-commit rhythm (chunk +
   content.json; this resume note → **d13-divisio**).

After d13-littera: d13-divisio → d13-a1-q1 → d13-a1-q2 (manual-rescue)
→ d13-a2-q1 → d13-a2-q2 → d13-a3-q1 → d13-a3-q2 → d13-dubia. Then
d.14 gate opens (caution: d.14 has multi-pars structure; the chunker
created d14-p1-* and d14-p2-* chunks per the manual-rescue plan).

## Tooling status

- 450 dpi PDF crops cached for pp.274–308 at `/tmp/colcrop/vol2-p*`.
  Generate p.309+ as needed.
- Manual-rescue chunks (d.11–d.20 boundary sweep) still skeleton: d13-a1-q2,
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
