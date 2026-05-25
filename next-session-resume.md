# Next session — **d.14-p1-littera DONE.** Begin `d14-p1-divisio` (Bonaventure's commentary opens).

**d.1–d.13 COMPLETE + d.14-p1-littera = 158 chunks.** Build: 569 translated, 878 quaestio routes.
Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com since 2026-05-23; per
"deploy after each decade ships" rule, the next live ship is at
end-of-d.20.

## Last session (2026-05-24)

`d14-p1-littera` promoted Tier-2 — Lombard's *Sententiae* II d. XIV Caps.
I–X spanning the Pars I → Pars II transition (printed pp. 333–335 = PDF
355–357). 1,003 Lat words; 13 apparatus entries renumbered continuously
across three printed pages. Latin re-set column-by-column from 450 dpi
PDF column-bands. Three `[?]` flags on marginal *Dubium N.* numerals,
preserved as printed pending the d.11–d.20 polish-blocker 600 dpi pass.

## d.14 chunk inventory (in semantic order)

Remaining d.14 chunks to promote, in order:

- **`d14-p1-divisio`** — NEXT. The COMMENTARIUS IN DISTINCTIONEM XIV.
  opener begins at raw line ~23706 (immediately after the littera ends
  at `…quarta die facta sunt.`). Per Vol II convention, this chunk holds
  the COMMENTARIUS header + *De productione insensibilium continentium.*
  subtitle + lemma + DIVISIO TEXTUS + TRACTATIO QUAESTIONUM + (per Vol II
  d.1 sessions 8/10/11 lock) the short ARTICULUS I opener (`Circa primum
  quaeruntur duo… Primo quaeritur de natura caeli crystallini. Secundo
  de natura caeli firmamenti.`) — but does NOT include `Circa primum sic
  proceditur` (that is the q1 opener).
- `d14-p1-a1-q1` — *Utrum caelum crystallinum sit de natura aquae.*
  Opens at the bottom of p.336 with `Circa primum sic proceditur…`;
  large quaestio with two-column Respondeo.
- `d14-p1-a1-q2`
- `d14-p1-a2-q1` *(manual-rescue chunk per boundary-sweep audit)*
- `d14-p1-a2-q2` *(manual-rescue)*
- `d14-p1-a3-q1` *(manual-rescue)*
- `d14-p1-a3-q2` *(manual-rescue)*
- `d14-p1-dubia`
- `d14-p2-divisio` *(manual-rescue)*
- `d14-p2-a1-q1`
- `d14-p2-a1-q2`
- `d14-p2-a1-q3` *(manual-rescue)*
- `d14-p2-a2-q1`
- `d14-p2-a2-q2`
- `d14-p2-a2-q3`
- `d14-p2-dubia`

## What to do this session

**Promote `d14-p1-divisio`.** Raw range begins at line ~23706. Per the
Vol II recipe, find the chunk's frontmatter line range and printed-page
span (likely pp. 335–336 = PDF 357–358 — text begins mid-p.335 right
column under `COMMENTARIUS IN DISTINCTIONEM XIV.`). Generate PDF crops if
not cached (`/tmp/colcrop/vol2-p{335,336}-*.png` may already exist for
p.335 from the last session; verify p.336).

**Cross-chunk footer-split watch:** the two p.333 Bonaventure-side
variant footers above the NOTAE divider (*Vat. cum uno alteroque cod.
quando.* and *Art. 2. q. 2. — Cfr. etiam supra d. I. p. I. dub. 1...*)
are anchored on the Commentarius side of p.333. They likely belong to
this `d14-p1-divisio` chunk or to `d14-p1-a1-q1`. Read the body anchors
and assign correctly per the Vol II cross-chunk footer-split convention.

## Tooling status

- 450 dpi PDF crops cached for pp. 274–335 at `/tmp/colcrop/vol2-p*`.
  Generate p.336+ as needed.
- Manual-rescue chunks (d.11–d.20 boundary sweep) still skeleton:
  d16-a1-q2, d18-dubia, d19-littera, d14-p2-divisio, d14-p2-a1-q3,
  d14-p1-a2-q1/q2, d14-p1-a3-q1/q2. Promote in normal Vol II cadence.
- Pre-promotion boundary sweep log:
  `manual-review/d11-d20-boundary-sweep-audit.md` — all blockers
  cleared 2026-05-23.

## Open `[?]` flags (parked for d.11–d.20 polish-blocker)

From `d14-p1-littera`:
1. Cap. IX marginal *Dubium 3.* vs *Dubium 1.* (Pars II reset
   ambiguity) — `[?]` flag in chunk + Notes block.
2. Cap. X marginal *Dubium 1.* vs *Dubium 4.* (gutter-crushed digit).
3. Cap. VII Pars II reset of Dubium numbering — preserved as printed.

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
  *Solutio …*, *Notandum.*, *Alia solutio.*, *Dubium N.*, etc.) are
  preserved inline per Vol II convention, NOT promoted to headings.
- Backup before any rebuild: `cp <chunk>.md _backup-<chunk>-pre-<reason>-<YYYYMMDD>/`.
- Vol II offset: `pdf = printed + 22`. Trust running-head text, never
  the OCR'd digits.

Prior session-by-session vol2 history (sessions 1–77) is trimmed per
Wilson's request 2026-05-22; the per-decade resolution logs and chunk
`## Notes` are the durable record. Backup of the pre-trim resume is at
`_backup-resume-pre-trim-20260522.md` if you need to walk back.
