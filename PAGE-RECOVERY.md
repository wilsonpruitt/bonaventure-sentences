# Vol I page recovery — 33 missing printed pages

> **Wilson's ruling, 2026-08-24: go through every page in order, one at a time, and deal with
> whatever is on it. No triage-by-type, no "easy ones first", no skipping a page because it looks
> awkward.** An earlier pass sorted these into "dropped mid-chunk" vs "between chunks" vs "the
> 249–255 run"; that sort is deliberately NOT the work order, because sorting by expected
> difficulty is how pages get avoided. **Work ascending by printed page number. Every page gets
> opened.**

## What these are

33 printed pages inside Vol I's own range that no chunk carries. **Every one was confirmed
(2026-08-24) to be an ordinary two-column text page with a footnote band** — not a blank, plate,
half-title or index. They are missing content. Confirmed by hand so far: **p. 104 is a *dubia***
(Wilson), **p. 854** carries body + `CONCLUSIO` + `SCHOLION` + footer band, **p. 249** is a full
`ARTICULUS`/`QUAESTIO` opening. `p. 710` was reported as having **no** footer band — the only one,
worth attention when you reach it.

Expect anything: dubia, littera, divisio, scholion, an article opening, a page that is mostly
apparatus. **The type is discovered at the page, not predicted before it.**

## Per-page procedure

For each page, in ascending order:

1. **Open the plate.** Local, already fetched, full resolution:
   `raw/vision/vol1/pagegaps/p<N>.jpg` (gitignored; regenerate with the URL in the table).
2. **Read the running head** — confirm you have the right page, and note the unit it names
   (`DIST. XIV. ART. II. QUAEST. I.` etc.).
3. **Find the raw OCR.** The window is in the table below; the OCR is the transcription source
   (it beats reading the plate — see repo `CLAUDE.md`). Vol I pt 1 =
   `raw/bonaventure_vol1_raw.txt`, pt 2 = `raw/bonaventure_vol1_pt2_raw.txt`.
4. **First ask: is this page's text ALREADY in the corpus, just unmarked?** Some of these are
   not missing transcription at all — the text sits inside a neighbouring chunk which simply
   never emitted a `<!-- page N -->` marker and left N out of its `printed_pages`. **Confirmed
   case: p. 526.** Its whole footer band is already present as `bon-sent-I-d30-a1-q3`'s `[^1s]`–
   `[^8s]` Scholion apparatus; nothing needs translating, the frontmatter is just wrong.
   *How to check:* grep the corpus for a distinctive phrase you can see on the plate. **A narrow
   raw-line window is a hint** — where the neighbours' recorded bounds nearly touch there is no
   room for untranscribed text. Narrow (<40 lines) on this list: **104, 155, 244, 387, 526, 558,
   718**. Treat that as a hint to check, never as an answer: open the page and confirm either way.
   If it is already there → fix the page marker + `printed_pages`, tick, move on.
5. **Otherwise decide where the page belongs** — into an existing neighbouring chunk, or a new
   chunk. Both neighbours are named in the table. Record the decision in the ledger even when
   obvious.
6. **Transcribe to Tier 2** per the standing per-chunk recipe in `CLAUDE.md` (Latin verbatim from
   OCR, literal English, full apparatus from the footer band, `[?]` on anything ambiguous).
7. **Update the owning chunk's `printed_pages` frontmatter.** This is how the page got lost.
8. **Tick the ledger row** and record what the page turned out to be, and which of the two
   outcomes it was (marker-only fix, or real transcription).

## ⛔ Rules that are not negotiable on this job

- **Every digit is read from the full-resolution plate, by you.** Do NOT delegate any digit —
  page numbers, `nota` numbers, chapter numbers — to a cheap model. Measured 2026-08-24: a Haiku
  fleet misread **12.5%** of *large* running-head page numbers, four of five errors being `5`→`3`
  — the same class that put sixteen wrong cross-references into this corpus. Cheap models may
  answer "is something there?" and nothing finer. See `AUDIT-QUEUE.md`.
- **A page that is mostly apparatus is still a page.** Do not skip the footer band because the
  body is four lines (p. 526 is exactly this: it carries `bon-sent-I-d30-a1-q3`'s entire Scholion
  apparatus band, which is why that chunk's frontmatter is wrong).
- **Do not renumber or re-anchor a neighbouring chunk's existing apparatus** to make a page fit.
  If the seam looks wrong, flag it and stop; that is a separate ruling.
- **Five cross-references point into these gaps** — p. 215 (×3), p. 131, p. 718. When you reach
  those pages, check that the referenced `nota` actually exists there, and say so in the ledger.
  The three p. 215 refs agree with one another, which argues those digits are right.
- **Push and deploy stay protected.** Commit per page or per small batch; do not push.

## Ledger — work top to bottom

`raw lines` = window in that part's raw OCR file, between the neighbours' recorded bounds.
`leaf` = archive.org leaf: pt 1 `doctorisseraphic11bona`, pt 2 `doctorisseraphic12bona`,
URL `https://archive.org/download/<ident>/page/<leaf>.jpg`.

| ✓ | page | part | raw lines | previous chunk | next chunk | leaf |
|:-:|-----:|:----:|-----------|----------------|------------|------|
| ☐ | **104** | pt1 | `24625–24634` | `bon-sent-I-d4-a1-q4 (pp.102-103)` | `bon-sent-I-d4-dubia (pp.105-107)` | `n205` |
| ☐ | **131** | pt1 | `28639–28913` | `bon-sent-I-d6-a1-q3 (pp.129-130)` | `bon-sent-I-d7-littera (pp.132-133)` | `n232` |
| ☐ | **145** | pt1 | `30738–31017` | `bon-sent-I-d7-a1-q4 (pp.142-144)` | `bon-sent-I-d8-littera (pp.147-149)` | `n246` |
| ☐ | **147** | pt1 | `31015–31496` | `bon-sent-I-d7-dubia (pp.145-146)` | `bon-sent-I-d8-p1-divisio (pp.149-150)` | `n248` |
| ☐ | **155** | pt1 | `32575–32576` | `bon-sent-I-d8-p1-a1-q2 (pp.152-154)` | `bon-sent-I-d8-p1-a2-q1 (pp.156-158)` | `n256` |
| ☐ | **162** | pt1 | `33451–33787` | `bon-sent-I-d8-p1-a2-q2 (pp.158-161)` | `bon-sent-I-d8-p2-divisio (pp.165-166)` | `n263` |
| ☐ | **210** | pt1 | `40497–41341` | `bon-sent-I-d11-littera (pp.207-208)` | `bon-sent-I-d11-a1-q2 (pp.214-216)` | `n311` |
| ☐ | **215** | pt1 | `41340–41693` | `bon-sent-I-d11-a1-q1 (pp.209-213)` | `bon-sent-I-d11-dubia (pp.217-218)` | `n316` |
| ☐ | **216** | pt1 | `41340–41693` | `bon-sent-I-d11-a1-q1 (pp.209-213)` | `bon-sent-I-d11-dubia (pp.217-218)` | `n317` |
| ☐ | **222** | pt1 | `42339–42567` | `bon-sent-I-d12-a1-q1 (pp.220-221)` | `bon-sent-I-d12-a1-q3 (pp.223-224)` | `n323` |
| ☐ | **228** | pt1 | `43304–43446` | `bon-sent-I-d12-dubia (pp.226-227)` | `bon-sent-I-d13-littera (pp.229-229)` | `n329` |
| ☐ | **244** | pt1 | `45750–45755` | `bon-sent-I-d14-divisio (pp.242-243)` | `bon-sent-I-d14-a1-q1 (pp.245-247)` | `n345` |
| ☐ | **249** | pt1 | `46333–47320` | `bon-sent-I-d14-a1-q2 (pp.247-248)` | `bon-sent-I-d15-littera (pp.256-258)` | `n350` |
| ☐ | **250** | pt1 | `46333–47320` | `bon-sent-I-d14-a1-q2 (pp.247-248)` | `bon-sent-I-d15-littera (pp.256-258)` | `n351` |
| ☐ | **251** | pt1 | `46333–47320` | `bon-sent-I-d14-a1-q2 (pp.247-248)` | `bon-sent-I-d15-littera (pp.256-258)` | `n352` |
| ☐ | **252** | pt1 | `46333–47320` | `bon-sent-I-d14-a1-q2 (pp.247-248)` | `bon-sent-I-d15-littera (pp.256-258)` | `n353` |
| ☐ | **253** | pt1 | `46333–47320` | `bon-sent-I-d14-a1-q2 (pp.247-248)` | `bon-sent-I-d15-littera (pp.256-258)` | `n354` |
| ☐ | **254** | pt1 | `46333–47320` | `bon-sent-I-d14-a1-q2 (pp.247-248)` | `bon-sent-I-d15-littera (pp.256-258)` | `n355` |
| ☐ | **255** | pt1 | `46333–47320` | `bon-sent-I-d14-a1-q2 (pp.247-248)` | `bon-sent-I-d15-littera (pp.256-258)` | `n356` |
| ☐ | **269** | pt1 | `49414–49508` | `bon-sent-I-d15-p1-dubia (pp.266-268)` | `bon-sent-I-d15-p2-a1-q1 (pp.270-271)` | `n370` |
| ☐ | **292** | pt1 | `52651–53401` | `bon-sent-I-d17-littera (pp.287-291)` | `bon-sent-I-d17-p1-a1-q2 (pp.296-298)` | `n393` |
| ☐ | **305** | pt1 | `54528–54967` | `bon-sent-I-d17-p1-a1-q4 (pp.301-303)` | `bon-sent-I-d17-p2-divisio (pp.307-307)` | `n406` |
| ☐ | **387** | pt1 | `67092–67093` | `bon-sent-I-d21-dubia (pp.386-386)` | `bon-sent-I-d22-littera (pp.388-389)` | `n488` |
| ☐ | **526** | pt2 | `10975–10976` | `bon-sent-I-d30-a1-q3 (pp.524-525)` | `bon-sent-I-d30-dubia (pp.527-529)` | `n115` |
| ☐ | **558** | pt2 | `14246–14247` | `bon-sent-I-d32-a1-q1 (pp.555-557)` | `bon-sent-I-d32-a1-q2 (pp.559-561)` | `n147` |
| ☐ | **586** | pt2 | `16969–17309` | `bon-sent-I-d34-divisio (pp.585-585)` | `bon-sent-I-d34-a1-q2 (pp.588-591)` | `n175` |
| ☐ | **589** | pt2 | `17308–17543` | `bon-sent-I-d34-a1-q1 (pp.585-588)` | `bon-sent-I-d34-a1-q3 (pp.591-592)` | `n178` |
| ☐ | **603** | pt2 | `18308–18858` | `bon-sent-I-d35-divisio (pp.599-599)` | `bon-sent-I-d35-a1-q2 (pp.605-607)` | `n192` |
| ☐ | **604** | pt2 | `18308–18858` | `bon-sent-I-d35-divisio (pp.599-599)` | `bon-sent-I-d35-a1-q2 (pp.605-607)` | `n193` |
| ☐ | **677** | pt2 | `25983–26274` | `bon-sent-I-d38-a2-q1 (pp.673-676)` | `bon-sent-I-d38-dubia (pp.680-682)` | `n266` |
| ☐ | **710** | pt2 | `28648–29096` | `bon-sent-I-d40-a1-q2 (pp.704-705)` | `bon-sent-I-d40-a2-q2 (pp.711-713)` | `n299` |
| ☐ | **718** | pt2 | `29864–29883` | `bon-sent-I-d40-a4-q1 (pp.716-717)` | `bon-sent-I-d40-a4-q2 (pp.719-722)` | `n307` |
| ☐ | **854** | pt2 | `43202–43367` | `bon-sent-I-d48-a1-q1 (pp.851-853)` | `bon-sent-I-d48-a2-q1 (pp.855-856)` | `n443` |

## Notes as you go

Record per page: what the page turned out to be, which chunk absorbed it (or the new chunk id),
any `[?]` left open, and anything that looked like a further seam defect. Append below.

---

### p. 104 — (Wilson, 2026-08-24: it is a *dubia*.) Not yet transcribed.
