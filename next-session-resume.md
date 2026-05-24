# Next session — **d.11 COMPLETE**. Begin d.12 with `d12-littera`.

**d.1–d.11 COMPLETE = 139 chunks.** Build: 550 translated, 878
quaestio routes. Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com
since 2026-05-23; per "deploy after each decade ships" rule, the
next live ship is at end-of-d.20.

## d.12 chunk inventory (all skeleton)

| chunk | lines | wc_la | status |
|---|---|---|---|
| `d12-littera`  | 20646–20732 | 1128 | skeleton — **NEXT** |
| `d12-divisio`  | 20740–20779 |  404 | skeleton |
| `d12-a1-q1`    | 20784–20931 |  ~   | skeleton |
| `d12-a1-q2`    | 20932–21186 |  ~   | skeleton |
| `d12-a1-q3`    | 21187–21396 |  ~   | skeleton |
| `d12-a2-q1`    | 21405–21552 |  ~   | skeleton |
| `d12-a2-q2`    | 21553–21646 |  ~   | skeleton |
| `d12-a2-q3`    | 21647–21744 |  ~   | skeleton |
| `d12-dubia`    | 21745–21841 | 1332 | skeleton |

## What to do this session

**Promote `d12-littera`** — Peter Lombard's text for d.12, the opening
chunk of d.12. Lombard begins on p.290 R-bottom with `DISTINCTIO XII.
Cap. I.` (*De distinctione operum sex dierum*) — see the closing
notes of d11-dubia which confirms the p.290 outgoing boundary is
clean. Lombard's d.12 covers the distinction of the six days' works
and the dispute between the simultaneous-creation view (Augustine)
and the per-intervalla view (Gregory, Jerome, Bede); expect Cap.
I–III on pp.290–292ish.

1. Identify the printed-page range. The auto-chunker assigned raw
   lines 20646–20732 — walk that range to find `Cap.` markers and
   page-footer page-numbers, then set `printed_pages` and `pdf_pages`
   in the frontmatter (offset `pdf = printed + 22`).
2. Extract + colcrop the relevant pages at 450 dpi. P.290 crops are
   already cached at `/tmp/colcrop/vol2-p290-*`; you'll need p.291
   (already cached) and possibly p.292.
3. Body Latin from IA djvu OCR (cleaner than column-band reads for
   Lombard text, which is single-band at the top of each page);
   cross-check against PDF only for garbles. Lombard-side NOTAE
   appears as `NOTAE AD LIBR. SENTENTIARUM` block at the page foot,
   *separate* from Bonaventure-body NOTAE.
4. Note that p.290's Lombard-side n.2 (*Libr. I. de Gen. ad lit.*) and
   the rest of the NOTAE AD LIBR. SENTENTIARUM block on p.290 belong
   to d12-littera (NOT to d11-dubia or d.12 commentary). The
   Bonaventure-body footers n.1 (*Ita codd. F…universales*) on
   p.290 anchor in d12-littera at *quatuor elementorum¹*.
5. Three audits + smoke build, then two-commit rhythm (chunk +
   content.json; this resume note → **d12-divisio**).

After d12-littera, continue d.12 in the usual order: divisio → a1-q1
→ a1-q2 → a1-q3 → a2-q1 → a2-q2 → a2-q3 → dubia.

## Tooling status

- 450 dpi PDF crops cached for pp.274–290 at `/tmp/colcrop/vol2-p*`
  and pp.291 cached. Generate p.292+ as needed.
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
