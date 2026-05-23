# Next session — Vol II d.11 in progress, **d11-a1-q1 next**.

**d.1–d.10 COMPLETE = 130 chunks. d.11 promotion underway: 1/9
(d11-divisio).** Build: 542 translated (876 quaestio routes total).
Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com since 2026-05-23;
deploy after each decade ships (or sooner at Wilson's discretion).

## d.11 chunk inventory (auto-chunked baseline)

| chunk | lines | wc_la | status |
|---|---|---|---|
| `d11-littera`     | 19518–19627 | 1483 | skeleton |
| `d11-divisio`     | 19629–19657 |  268 | **Tier 2 (2026-05-23 — this session)** |
| `d11-a1-q1`       | 19662–19835 | 2326 | skeleton — **NEXT** |
| `d11-a1-q2`       | 19836–19927 | 1078 | skeleton |
| `d11-a1-q3`       | 19928–20037 | 1430 | skeleton |
| `d11-a2-q1`       | 20050–20245 | 2244 | skeleton |
| `d11-a2-q2`       | 20246–20353 | 1354 | skeleton |
| `d11-a2-q3`       | 20354–20531 | 2231 | skeleton |
| `d11-dubia`       | 20532–20645 | 1470 | skeleton |

Article I = guardianship (q1 fallen man, q2 integral man, q3 Christ).
Article II = annexa (Article 1 of the second principal part — running
heads at lines 20233 `DIST. XI. ART. H. QUAEST. 11.` and 20368
`DIST. XI. ART. II. QUAEST. III.`; a2-q1 boundaries to be verified
against running heads before promotion).

## What to do this session

**Promote `d11-a1-q1`** (printed pp.276–280, PDF 298–302). Per the
locked Vol II workflow (see CLAUDE.md "Vol II Override"):

1. Pages already extracted at 450 dpi: `raw/vision/vol2/p-hires-276.png`
   exists; extract 277–280 if not present
   (`python3.11 tools/extract-pages.py --volume vol2 --pages 277-280 --dpi 450`)
   then `python3.11 tools/colcrop.py vol2 <p>` per page.
2. **Page 276 reserved footers:** ² *Cfr. infra d. 25. p. II. q. 4.
   seq. — Quod Deus nihil facit frustra, dicit Aristot., I. de Caelo
   et mundo, text. 32. (c. 4.).* anchors at `violentari²` in the *Ad
   oppositum* block; ³ *Luc. 22, 27.* anchors at `qui ministrat³` in
   the third *Ad oppositum* argument. These are documented in the
   d11-divisio Notes — pick them up at the top of a1-q1 footer
   numbering (renumber the receiving chunk's apparatus continuously
   starting at [^1] for page 276 footer ², [^2] for footer ³, then
   page 277 footer ¹ becomes [^3], etc. — Quaracchi numbering restarts
   each page, but the chunk's [^N] is continuous).
3. **Article opener folds in:** `ARTICULUS I. — Circa Angelorum
   custodiam. — QUAESTIO I. — Utrum Angeli debuerint deputari ad
   custodiam hominis lapsi.` opens at the bottom of p.276 below
   TRACTATIO QUAESTIONUM. Marginal label *Ad oppositum.* visible on
   p.276 left margin next to the first *ostenditur* opener — preserve
   inline in italics per Vol II convention.
4. **Cascade-damaged respondeo expected.** ~2300 words spanning ~5
   printed pages = a full solo session.
5. Document incoming + outgoing boundary CLEAN status in `## Notes`
   at promotion time (the d.10 / d11-divisio convention).
6. Before commit: three audits (`--volume 2 --min-d 11 --max-d 11`)
   + `cd site && node scripts/build-content.mjs`.
7. Two-commit rhythm: (1) chunk work + content.json, (2) update this
   resume note for the next session.

## Open project-wide TODOs

- **Next decade polish-blocker fires after d.20.** Same three-pass
  cadence; `manual-review/d11-d20-polish-resolution-log.md` will be
  the log.
- **Vol I site copy** still hardcodes "Volume I" in
  `site/src/app/page.tsx:47,57` — update when Vol II has enough real
  chunks to surface in landing copy.

## Convention reminders

- "keep going" = continue chunk-by-chunk, committing each, no check-ins
  (cf. [[feedback_bonaventure-bucket-e-autopilot]]).
- Tier-2 = literal, not paraphrase, incl. scholia/apparatus.
- Marginal labels (`*Ad oppositum.*`, `*Fundamenta.*`, `*Conclusio.*`,
  `*Solutio.*`, etc.) are preserved inline per Vol II convention, NOT
  promoted to headings.
- Backup before any rebuild: `cp <chunk>.md _backup-<chunk>-pre-<reason>-<YYYYMMDD>/`.
- Vol II offset: `pdf = printed + 22`. Trust running-head text, never
  the OCR'd digits.

Prior session-by-session vol2 history (sessions 1–77) is trimmed per
Wilson's request 2026-05-22; the per-decade resolution logs and chunk
`## Notes` are the durable record. Backup of the pre-trim resume is at
`_backup-resume-pre-trim-20260522.md` if you need to walk back.
