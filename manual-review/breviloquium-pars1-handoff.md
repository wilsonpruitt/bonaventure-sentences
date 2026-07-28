# Breviloquium Pars I — session handoff (c6–c9 + Pars I gate)

**Written 2026-07-28. Self-contained: hand a session THIS FILE plus the repo's
`CLAUDE.md` § "VOL V" and it has everything it needs.** The format reference is
`vol5/bon-brev-p1-c5.md` — read it before writing anything.

---

## State

**Done, committed, and pushed** (`origin/master` = `5929494`): Breviloquium
Pars I capitula **I–V**, printed pp.210–214, **37 apparatus entries**, build
**1938/1938**. Pages 210–214 are fully owned and contiguous.

**Remaining in Pars I** — 4 chunks:

| Chunk | Cap. | Title (printed) | Pages | Split(s) |
|---|---|---|---|---|
| `bon-brev-p1-c6` | VI | *De unitate divinae naturae in multiplicitate appropriatorum* | 214–215 | 1397 / **1163** |
| `bon-brev-p1-c7` | VII | *De omnipotentia Dei* | 215–216 | 1163 / **1385** |
| `bon-brev-p1-c8` | VIII | *De Dei sapientia, praedestinatione et praescientia* | 216–217 | 1385 / **1180** |
| `bon-brev-p1-c9` | IX | *De voluntate Dei et providentia* | 217–218 | 1180 / **1377** |

Page ranges are from the volume's own index (raw L93780–93790) and are a
**starting hypothesis, not a boundary** — set every real boundary from the
`Cap. N.` heading visible in a band (see Rule 2 below). Pars I ends on p.218;
`PARS II` opens p.219 (verified by pdftotext on pdf 294/295).

**Also available any time, independent of the capitula:** the **Prologue**,
pp.201–208 → `bon-brev-prol` (intro) + `bon-brev-prol-s1..s6` (`section: 1..6`,
`division: 0`, `type: prologus`). The capitula table on pp.209–210 top is
editorial and is NOT chunked.

---

## Already prepared for you — do not redo

- **450 dpi page images exist** for pp.215–218 at `raw/vision/vol5/p-2NN.png`
  (gitignored, regenerable via `tools/extract-pages.py --volume vol5`).
  Extraction is slow (~1–2 min/page); it is already done.
- **Column bands are generated** at `/tmp/colcrop/vol5-p2NN-{L,R}-{0,1,2}.png`
  for pp.215–218, using the measured splits in the table above. `/tmp` may be
  cleared between sessions — if the bands are gone, regenerate with
  `python3.11 tools/colcrop.py vol5 <page> <split> 3 1.8` using the **splits in
  the table**, which are already measured. Do not re-measure unless you go past
  p.218.
- **Gutter splits are measured** for every remaining Pars I page. Running
  series: 210=1350, 211=1175, 212=1335, 213=1126, 214=1397, 215=1163,
  216=1385, 217=1180, 218=1377. Parity alternates (odd ≈1126–1180, even
  ≈1335–1397) **but each cluster drifts**, so past p.218 always measure.
- **`tools/check-vol5-apparatus.py` exists** and replaces the audit that is
  blind to Vol V (see "Verification" below).

---

## c6's incoming hand-off (from c5's Notes — do not re-derive)

**Apparatus.** p.214 footer **n. 9** belongs to c6. It is anchored on
*appropriatio Hilarii*. Verbatim:

> **La.** Libr. II. de Trin. n. 1. Cfr. I. Sent. d. 31. p. II. a. 1. q. 3. De aliis appropriationibus vide ibid. a. 2. q. 3; d. 34. q. 4. et d. 3. p. I. dub. 3. et 4. — Superius pro *sacra Scriptura* plures codd. *Scriptura divina*, K *sacra fides*, M S legunt *appropriatorum docet Scriptura*. Subinde pro *omnibus* R *tribus*.

**Body.** Cap. VI opens in p.214's **right** column and breaks at the column
foot. c6's `printed_pages` must begin at **214**. The inherited run is:

> Tertio vero de pluralitate *appropriatorum* hoc docet sacra Scriptura esse tenendum, quod licet omnia essentialia omnibus personis aequaliter et indifferenter conveniant; tamen Patri dicitur appropriari *unitas*, Filio *veritas*, Spiritui sancto *bonitas*. — Et iuxta hanc sumitur secunda appropriatio Hilarii[^p214-9], scilicet « *aeternitas* in Patre, *species* in Imagine, *usus* in Munere ». — Iuxta hanc sumitur tertia, scilicet in

Marginalia on that run (trim from body, log in Notes): "Appropriatio prima." ·
"Secunda." · "Tertia."

---

## Per-chunk recipe

1. **Read the bands in reading order** — left column top→bottom (`L-0`, `L-1`,
   `L-2`), then right column (`R-0`, `R-1`, `R-2`). Bands overlap deliberately.
2. **Find the chunk's true end**: the next `Cap. N.` heading *in a band*.
3. **Lead with the incoming hand-off**, then read this chunk's own footers.
4. **Reassemble every runover** (Rule 1) before writing the apparatus.
5. **Write the file** on the `bon-brev-p1-c5.md` pattern: frontmatter (`work:
   breviloquium`, `division: 1`, `capitulum: N`, `type: capitulum`, both
   titles, `printed_pages`, `pdf_pages` = printed+76, `source`,
   `has_scholion: false`, `has_apparatus: true`, a `transcription_status`
   recording the splits used), then `## Latin` (with `<!-- page N -->` at each
   page start), `## English`, `## Apparatus`, `## Notes`.
6. **`## Notes` must carry**: provenance + splits used; page span with the
   positive evidence that fixed it; apparatus count and where each note came
   from; every runover reassembled; the **hand-off forwarded** to the next
   chunk (quote both any leftover note *and* any inherited body text verbatim);
   marginalia in body order; readings settled off the bands. No literal `[^`
   token anywhere in Notes prose — it breaks the pairing check.
7. **Verify**: `python3.11 tools/check-vol5-apparatus.py` then
   `cd site && node scripts/build-content.mjs`. The build count must rise by
   exactly 1 per chunk (1938 → 1939 → 1940 → 1941 → 1942).
8. **Commit one chunk at a time**, message naming pages, entry count, build
   number, and any new method finding. Then update `next-session-resume.md`
   to point at the following chunk. Do **not** push or deploy — both are
   protected and need Wilson's explicit per-action OK.

---

## The four rules that carry the quality bar

1. **Runovers are the norm — four in the first five chunks.** A footer's last
   entry frequently continues as an **unnumbered** block at the head of the
   next footer: across the gutter (p.211 n.4, p.213 n.4), across a **page**
   boundary (p.212 n.7), or breaking **mid-word** (p.214 n.5, `...ubi de ap-`
   → `paritione...`). **Treat every footer's last entry as presumed incomplete
   until you locate its continuation or positively exclude one.** A
   column-order read that stops at the left footer's end will silently truncate
   these.
2. **The running head names a page's LAST capitulum, not its first.** p.211
   heads `PARS I. C. III.` although Cap. II occupies its left column. Never set
   a boundary from a running head; find the `Cap. N.` heading in the band.
3. **Footnote numbering restarts on every printed page** — hence page-qualified
   labels (`[^p215-3]`). Never use bare numbers: two pages' n.1 would collide
   into one definition and an entry would vanish at render.
4. **The raw OCR has NO footnote numerals** — Vol V's OCR renders every
   superscript as `^ ' " *`. Anchor *positions* survive in the raw and are
   useful; numbers and footer openers do not. **All apparatus comes off the
   bands.** Corollary: the raw's silence about a page's footer means nothing.

Two smaller ones worth keeping: Quaracchi's serif **`1` prints like `4`**
(`120`→"420", `11`→"41") — cross-check any digit against a second occurrence or
against content (p.214 n.5's `Ioan. 1, 32` was settled by knowing the dove
belongs to John 1). And Quaracchi's spellings **`transsumtive`, `assumtum`,
`assumtionem`** (single *m*, no *p*) are correct as printed — do not normalize.

---

## Verification

```bash
python3.11 tools/check-vol5-apparatus.py     # pairing + duplicates + ownership
cd site && node scripts/build-content.mjs    # must be +1 per chunk
```

`check-vol5-apparatus.py` reports a printed page's notes as `PENDING` when its
top note(s) are legitimately forwarded to a chunk that isn't written yet, and
as `GAP` when a note in the interior of the range is owned by nobody. **A GAP
is the failure mode that cost Vol IV three entire footer registers** — never
commit past one. Its `KNOWN_TOTALS` map holds each page's true note count as
established by an eyes-on band read; **add p.215–218 to that map as you read
them**, so a later dropout is caught automatically.

Note that `audit-apparatus-count.py` is **blind to Vol V** and always will be
until it grows a symbol-glyph mode — do not trust its diff column here. The
other two audits (`audit-paraphrase.py`, `audit-headers.py`) also do not yet
support `--volume 5`, and `seam-screen.py` / `audit-style-formatting.py` parse
`bon-sent-…` ids and will silently skip `bon-brev-…` files. **Extending them is
a prerequisite for the Pars I gate, not for the chunks.**

---

## The Pars I gate (fires when c9 lands)

⚠ **Cadence revised 2026-07-28 — this is a SHAKEDOWN gate, not one of seven.**
The pilot's "one gate per pars" is superseded by CLAUDE.md § "Polish-gate
cadence for Vols V–X": gates fire on **~100 printed pages**, on **every work
boundary**, and on **one shakedown ~15–25 pp into each new work**. This gate is
trigger 3. The Breviloquium gets **two** gates total — this one and a closing
gate at p.291. Also: **pass 2 below is decoupled and runs every commit**, not
here; only passes 1, 3 and 4 are gate work.

When c9 closes, run the passes over the prologue + Pars I before starting Pars II:

1. **Flag resolution** — walk every `[?]` in `vol5/` (currently **zero** across
   all 16 chunks) and every parked ambiguity in the chunks' `## Notes`; resolve at 600
   dpi (`pdftoppm -r 600 -f <pdf> -l <pdf> -png raw/doctorisseraphic05bona.pdf
   raw/vision/vol5/p-hires-<printed>-r600`, pdf = printed + 76) or formally
   ACCEPT-ILLEGIBLE with a reason. Log to
   `manual-review/breviloquium-pars1-polish-resolution-log.md`.
2. **Style/formatting audit — NOT gate work any more; run it every commit.**
   Extending the tooling to Vol V (see Verification) is still a prerequisite,
   and is the one piece of real work this gate carries. Once extended, wire it
   into the per-chunk verification step beside `build-content.mjs`. Running it
   only at gates is what let `polish-style-scan.py` sit hardcoded to
   `DIRS=["vol1","vol2"]` through all of Vol III and Vol IV, making every
   "Pass 2 CLEAN" in those logs false.
3. **Boundary sweep** — every chunk boundary that falls inside a printed page,
   checked from both ends: the receiving chunk's opening must be grammatically
   continuous with the prior chunk's close, and the shared page's footer must
   be fully accounted for across the two. Vol V's own multiplier: confirm every
   runover was joined, not truncated.
4. **Disk cleanup** — `rm -f raw/vision/vol5/*.png /tmp/colcrop/vol5-*`
   (regenerable; ~3.5 MB per page). Wilson's machine has run as low as 7.9 GB
   free, so do not skip this.
