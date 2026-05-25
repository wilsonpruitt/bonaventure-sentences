# Next session — **d.14-p1 littera/divisio/a1-q1 DONE.** Begin `d14-p1-a1-q2`.

**d.1–d.13 COMPLETE + d.14-p1 {littera, divisio, a1-q1} = 160 chunks.** Build: 571 translated, 878 quaestio routes.
Vol II d.1–d.10 LIVE on bonaventure.wrootpress.com since 2026-05-23; per
"deploy after each decade ships" rule, the next live ship is at
end-of-d.20.

## Last session (2026-05-24)

Three d.14 chunks promoted Tier-2 in a single session:
- `d14-p1-littera` — Lombard Caps. I–X, pp.333–335, 1,003 Lat words, 13
  apparatus, three `[?]` *Dubium N.* numeral flags.
- `d14-p1-divisio` — Commentarius opener, p.335 R col, 303 Lat words,
  0 apparatus (p.335 R-footer NOTA belongs to a1-q1).
- `d14-p1-a1-q1` — *Utrum caelum crystallinum sit de natura aquae,*
  pp.335–338, 2,095 Lat words, 21 apparatus across pp.335–337 footers
  (p.338 R-footer belongs to a1-q2), 3-section scholion, 1 `[?]` flag
  on Scholion II Alex. Hal. citation.

Build: 568 → 571 translated.

## d.14 chunk inventory (in semantic order)

Remaining d.14 chunks to promote, in order:

- **`d14-p1-a1-q2`** — NEXT. *An firmamentum sit idem cum ignis
  elemento* (or similar — running head opens on p.338 R-2 immediately
  below q1's Scholion III). Likely runs from p.338 R into p.339 L
  through p.341 (running head for `DIST. XIV. P. I. ART. II. QUAEST. I.`
  appears at line 24123 → p.341). Watch: q1's p.338 R-footer notes
  (Gen 1,2; Gen 1,6; Homil. 3 in Hexaëm.; Vat. *ergo si ipse*) anchor
  here per the cross-chunk footer-split convention — pick them up as
  [^1]–[^4] of q2.
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

**Promote `d14-p1-a1-q2`.** Raw range begins near line 23979 (QUAESTIO
II running head on p.339). Page span p.338 R bottom → p.341 top. Per
Vol II recipe, generate PDF crops for pp.339–341 (p.338 crops already
cached), reset Latin column-by-column, translate, build apparatus.

**Cross-chunk footer-split watch:** the p.338 R-footer notes (Gen 1,2;
Gen 1,6; Homil. 3 in Hexaëm.; Vat. *ergo si ipse*) — flagged in
`d14-p1-a1-q1` Notes — are body-anchored on q2's affirmative-arg side
and SHOULD be picked up here as q2's [^1]–[^4].

The two p.333 Bonaventure-side variant footers from `d14-p1-littera`
Notes (*Vat. … quando*; *Art. 2. q. 2. — Cfr. etiam supra d. I. p. I.
dub. 1...*) remain parked — the "Art. 2. q. 2." cross-reference clearly
belongs to `d14-p1-a2-q2`. The "Vat. … quando" has no obvious anchor in
d.14 — may belong elsewhere or be a stray variant note.

## Tooling status

- 450 dpi PDF crops cached for pp. 274–338 at `/tmp/colcrop/vol2-p*`.
  Generate p.339+ as needed.
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

From `d14-p1-a1-q1`:
4. Scholion II at `Alex. Hal., S. p. II. q. 50. m. 1.[?]` — stray glyph
   (likely `1.` or `n. 1.`) before em-dash to `Scot.` at 450 dpi.

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
