# Next session — Vol II d.11 almost done, **d11-littera next (final d.11 chunk).**

**d.1–d.10 COMPLETE = 130 chunks. d.11 promotion: 8/9 done**
(d11-divisio + d11-a1-q1 + d11-a1-q2 + d11-a1-q3 + d11-a2-q1 +
d11-a2-q2 + d11-a2-q3 + d11-dubia). Build: 549 translated, 878
quaestio routes. Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com
since 2026-05-23; deploy after each decade ships.

## d.11 chunk inventory + Tier-2 progress

| chunk | lines | wc_la | status |
|---|---|---|---|
| `d11-littera`  | 19518–19627 | 1483 | skeleton — **NEXT** |
| `d11-divisio`  | 19629–19657 |  268 | Tier 2 (2026-05-23) |
| `d11-a1-q1`    | 19658–19835 | 2333 | Tier 2 (2026-05-23) |
| `d11-a1-q2`    | 19836–19927 | 1078 | Tier 2 (2026-05-23) |
| `d11-a1-q3`    | 19928–20037 | 1430 | Tier 2 (2026-05-23) |
| `d11-a2-q1`    | 20050–20245 | 2244 | Tier 2 (2026-05-23) |
| `d11-a2-q2`    | 20246–20353 | 1354 | Tier 2 (2026-05-23) |
| `d11-a2-q3`    | 20354–20531 | 2231 | Tier 2 (2026-05-23) |
| `d11-dubia`    | 20532–20645 | 1470 | Tier 2 (2026-05-23) |

## What to do this session

**Promote `d11-littera`** — Peter Lombard's text for d.11, the closing
chunk of d.11. Standard littera chunk per `vol1/bon-sent-I-d8-littera.md`
template: Latin verbatim from Quaracchi's Lombard printing (top-band
small-type body on the d.11 opening pages), parallel literal English,
apparatus from the `NOTAE AD LIBR. SENTENTIARUM` footer block on the
relevant pages.

Lombard's d.11 covers angelic custody (the source for Bonaventure's
a.1+a.2) and the question of angelic advance in cognition (Dub.II
source) — capit. 1–3.

1. Identify the printed-page range for d.11 Lombard text. The
   `bon-sent-II-d11-littera.md` frontmatter currently says skeleton;
   verify printed-pages by walking back from d.11 a.1 opening
   (printed p. ~270, pdf p. ~292) — Lombard's text always precedes
   the commentary.
2. Extract + colcrop those pages at 450 dpi; Lombard's small-type
   appears at the TOP of each page in a single band above the
   Bonaventure commentary, with `NOTAE AD LIBR. SENTENTIARUM`
   footnotes in the bottom band (separate from Bonaventure-body
   footnotes).
3. Three audits + smoke build, then two-commit rhythm (chunk +
   content.json; this resume note → **d12-divisio** to open d.12).

After d11-littera, **d.11 is complete and ready to deploy.** Per the
"deploy after each decade ships" rule, d.11 alone does not trigger
a deploy — wait for the decade ship at end-of-d.20. Continue into
d.12 next.

## Tooling status

- 450 dpi PDF crops cached for pp.275–290 at `/tmp/colcrop/vol2-p*`
  and `raw/vision/vol2/p-hires-*.png`.
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
