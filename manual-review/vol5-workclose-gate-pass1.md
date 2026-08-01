# Breviloquium work-close gate — Pass 1 (`[?]` flag resolution)

**Gate scope:** the Breviloquium in full (Vol V, printed pp. 201–291, 79 chunks in
`vol5/`), fired **unconditionally at the work boundary** per CLAUDE.md § "Polish-gate
cadence for Vols V–X", trigger 2. This is the work's second and closing gate; the Pars I
shakedown gate (`breviloquium-pars1-polish-resolution-log.md`) was the first, and its
format is followed here.

Run 2026-08-01. **Pass 1 only** — pass 2 (style scan) is decoupled and has run every
commit, reported CLEAN; passes 3 and 4 are not this agent's.

**Method.** Every reading below was **re-derived at 600 dpi**, an escalation the earlier
reads did not use (they stopped at 450 dpi / 11×):
`pdftoppm -r 600 -f <pdf> -l <pdf> -png raw/doctorisseraphic05bona.pdf raw/vision/vol5/p-hires-<printed>-r600`,
offset `pdf = printed + 76` (271→347, 272→348, 282→358). Pages were read as column bands
via `tools/colcrop.py` on a `vol5hires` mirror of the 600 dpi leaves, never as a full-page
extract, and single word-pairs were cropped tight and upscaled 8–12× on top of that.
**No reading below rests on a glyph alone**: each is settled by an independent agreement —
a corpus-wide parallel of Quaracchi's own formula, a book's chapter count, or the plate's
own second occurrence of the same word.

**Working set: three standing `[?]` flags.** All three resolve, and **all three resolve
the same way — the reading is CERTAIN and the text is WRONG.** None is
accepted-illegible; none is emended.

---

## Flag 1 — `bon-brev-p6-c7`, p. 271 n. 2 · `E F G H minus, aptae ponunt et`

**Owned by `bon-brev-p6-c6`** (which raised it), re-reached without disposition by
`bon-brev-p6-c7`, and forwarded unchanged through `p6-c8` and `p6-c11`. The entry stands
in p. 271's **left** footer block, second note:

> `² Pro videlicet, quod edd. et pauci codd. omittunt, E F G H / minus, aptae ponunt et. Inferius pro incredulis D P substituunt infidelibus.`

**As it stands in the chunk:** transcribed exactly as printed, English rendering the sense
the grammar requires, flagged because *aptae* agrees with nothing in the sentence.

**Evidence gathered.**

- **600 dpi, p. 271 left column, footer band (`n=14`, band L-11, 2×), then a tight crop of
  the word-pair at 12×.** The plate prints `minus,` — a true comma with a descending tail,
  not a speck — then `aptae`, five sorts, **a-p-t-a-e**, the `a` before the final `e`
  carrying an unmistakable round bowl and right stem. There is no ligature, no broken
  sort, and no ink loss anywhere near it. **More dpi did not change the reading; it made
  it certain.**
- **The siglum run re-derived in the same pass** (tight crop at 12×): `E F G H`. The final
  sort is two uprights with top and bottom serifs and a partly-inked crossbar; **one
  upright is never `H`, two can be**, and the run's alphabetical order (E, F, G, →H)
  admits nothing else. **The sigla were never the problem and they stand.**
- **The independent agreement — Quaracchi's own formula, corpus-wide.** `minus apte` is
  the edition's standing apparatus phrase and it occurs **21 times across the Vols I–IV
  raws** (`grep -oiE "minus a[pnu][tl]e"`: vol1 pt2 4, vol2 2, vol3 6, vol4 9), e.g.
  `cum pluribus codd. minus apte hoc`, `…ris et edd. minus apte purificans`,
  `aliis minus apte catechumeno`. **In none of them is there a comma, and in none of them
  is the adverb spelled `aptae`.** The Vol V raw's own `minus, aplae` reproduces the
  plate's comma faithfully — it is the plate's, not the OCR's.

**DISPOSITION — PLATE-DEFECT (resolved; the reading is certain, the text is wrong).**
The 1891 plate prints `minus, aptae` where Quaracchi's own invariable formula, attested
21× elsewhere in the corpus, is `minus apte`; **both the comma and the `-ae` are
compositor's faults in one word-pair.** The Latin stays exactly as printed and the English
keeps the sense the grammar requires. **Quaracchi is not emended.** This takes the same
shape as p. 280 n. 6's `homo non separe` (`bon-brev-p6-c13`) — a determinate reading of a
defective plate — and, like it, is now CLOSED and must not be resurrected downstream.
**No chunk edit.**

---

## Flag 2 — `bon-brev-p6-c7`, p. 272 n. 6 · `Respicitur Col. 6, 12.`

Raised by `bon-brev-p6-c7`, which owns p. 272 nn. 1–7. The entry opens the second note of
p. 272's **right** footer block (n. 5 having run over the gutter above it):

> `⁶ Respicitur Col. 6, 12. — Praecedens sententia, quae etiam paulo inferius recurrit, est Magistri Sent., II. Sent. d. XXX. c. 9. …`

**As it stands in the chunk:** transcribed and translated exactly as printed
(`Reference is had to Col. 6:12.`).

**Evidence gathered.**

- **600 dpi, p. 272 right column, footer bands (`n=14`, bands R-11 and R-12, 2×), then a
  tight crop of `Col. 6, 12.` at 10×.** The abbreviation is **C-o-l-period** — three
  sorts, no possibility of `Eph.` or `Coloss.` — followed by `6`, comma, `12`, period.
  The `6` shows the closed lower bowl and rising terminal of a true 6 (not a `5`, which in
  this face carries a flat top bar and no ascender, and not an `8`); the `12` is a serifed
  upright `1` with a footed base plus a `2`. **Every digit is individually legible.**
- **The independent agreement is a COUNT, the same species that settled `text. 84`→`81`
  (Physics I has 83 texts): the Epistle to the Colossians has FOUR chapters.** `Col. 6`
  cannot exist. The citation is not ambiguous; it is impossible.
- **The sense fixes the intended target.** The anchor is `redigit etiam in diabolicam
  servitutem et in potestatem principis tenebrarum`, and **Ephes. 6:12** reads *adversus
  principes et potestates, adversus mundi rectores tenebrarum harum* — supplying both of
  the anchor's nouns (*potestatem*, *principis*, *tenebrarum*) in one verse, at exactly
  the chapter and verse the plate prints. Checked directly against the words the body
  prints, per the gate brief.
- **The plate's own control.** Two entries below, n. 7 uses **the same three sorts** for a
  genuine `Col. 1, 13: Qui eripuit nos de potestate tenebrarum…` — read on the same band.
  So `Col.` is what the case held; the fault is the book name, not the digits.
- **Independent machine corroboration, not used as authority but recorded:**
  `index/citations.tsv:19179` carries
  `bon-brev-p6-c7 … apparatus:p272-6 … Col. 6, 12 → Col 6:12 … chapter-out-of-range`,
  and `manual-review/citation-qa-report.md:12` the same. **★ This QA line is EXPECTED, not
  a defect in the chunk** — it is the flagged plate reading being detected, on the same
  commit that raised it, exactly as CLAUDE.md § "Polish-gate cadence" describes. It must
  not be "fixed" and must not be counted against the chunk.

**DISPOSITION — PLATE-DEFECT (resolved; the reading is certain, the citation is wrong).**
The plate prints `Col. 6, 12`; the sense and the verse both require **Ephes. 6:12**. The
Latin and the English stay exactly as printed. **The emendation to `Ephes.` would be ours
and not the edition's, and is not made.** `build-citations.py` will keep flagging the line
for as long as the transcription is faithful, which is the correct behaviour.
**No chunk edit.**

---

## Flag 3 — `bon-brev-p7-c2`, p. 282 n. 4 · lemma `purgatis` against the body's `expurgatis`

Raised by `bon-brev-p7-c2`, which owns p. 282 nn. 3–7. n. 4 straddles p. 282's gutter; the
lemma stands in the **unnumbered continuation at the head of the right footer block**:

> `Pro quibus sufficienter purgatis P a quibus sufficienter purgati, et pro reliquiis S sordibus; post corporali 1 addit eis.`

**As it stands in the chunk:** both readings transcribed exactly as printed — body
`expurgatis`, footer lemma `purgatis` — with the discrepancy flagged, not repaired.

**Evidence gathered.**

- **600 dpi, p. 282 right column, top band (`n=14`, band R-0, 2×) — the BODY.** The first
  line of the right column reads `sufficienter expurgatis, immediate evolant et intro-`.
  **The `ex` is fully inked and unambiguous**, and the mid-sentence break from the left
  column (`…reliquiis peccatorum; quibus` / `sufficienter expurgatis`) is a clean word
  boundary, so the prefix cannot have been carried over or split.
- **600 dpi, same column, footer band R-11 (2×), then a tight crop of the lemma at 8×.**
  The lemma prints, in italic, `quibus sufficienter purgatis` — **and the gap between
  *sufficienter* and *purgatis* is a full word-space, not a broken or bleached `ex`.**
  No ink loss, no worn sort: the prefix is simply not in the forme.
- **The independent agreement is internal to the note, and it is the note's own logic.**
  A Quaracchi `Pro X … Y` entry quotes the **adopted** text as its lemma; here the adopted
  text is four sorts longer than the lemma that quotes it. And the variant the entry
  reports, P's `a quibus sufficienter purgati`, is likewise prefix-less — so the
  compositor's eye was on the un-prefixed stem across the whole entry.
- **Both readings were re-read at 600 dpi in the same pass, so the discrepancy is not an
  artefact of two different resolutions** — which is what the 450 dpi / 4.6× reads could
  not exclude.

**DISPOSITION — PLATE-DEFECT (resolved; both readings are certain, the plate is internally
inconsistent).** The body's `expurgatis` and the footer's lemma `purgatis` are each
definitively read at 600 dpi and they disagree; the fault is Quaracchi's, in the lemma,
which drops the prefix of the text it quotes. **Neither is emended and neither is
harmonised to the other** — the chunk already prints both exactly as the plate does, which
is the correct treatment. **No chunk edit.**

---

## Recorded but deliberately NOT flagged — confirmed still correctly unflagged

These three were reviewed for the gate and **need no resolution; each is confirmed to
remain correctly unflagged, and none may be "fixed."**

1. **p. 283's right-column faded scan streak (`bon-brev-p7-c3`) — CORRECTLY UNFLAGGED.**
   Six body words in a narrow vertical band are partly bleached **in the scan, not in the
   plate**: `haec`, `misericordiae`, `quo`, `praesentiam`, `est`, `beneficia`. `p7-c3`
   re-read them at 4.6× and again at **7.0×**, which recovered no further ink — **the loss
   is photographic, not resolution-limited, so escalating this gate to 600 dpi would
   recover nothing either and was not attempted.** Every one of the six has a
   **determinate** reading from the surviving letters plus the grammar (*haec suffragia
   valere* is the acc.-and-inf. governed by *disposuit*; *misericordiae* is required by
   *dulcedinem*; *in quo* by *sacrificium*; *praesentiam* shows `pr…entiam`; *est*
   completes *hinc est*), and the raw reproduces the scan's own damage rather than
   contradicting it. **A determinate reading is not an ambiguity — no `[?]` is owed.**
2. **p. 284's `de Cura pro mortuis agenda` (`bon-brev-p7-c3`) — CORRECTLY UNFLAGGED.**
   The received title of Augustine's work is *De cura pro mortuis gerenda*; the plate
   prints `agenda`, the form is Bonaventure's, the sense is unaffected, and **Quaracchi's
   own footnote to it (`Cap. 2. n. 4.`) resolves to the right work**, so nothing is
   ambiguous and nothing dangles. **Transcribed as printed. This is a note that no one
   should "fix," not a flag.**
3. **`bon-brev-p6-c8`'s dangling `tom. I. pag. 155` (`apparatus:p273-6`) — NOT A CHUNK
   DEFECT.** `index/citations.tsv:19189` and `citation-qa-report.md:13` report it as
   `dangling` / "no chunk owns printed page 155 of tom. 1". The reference is **GALLAND's
   *Bibliotheca veterum Patrum*** — the entry reads `…et apud Galland. Biblioth. (tom. I.
   pag. 155, c. 4.)` — **not tom. I of the Quaracchi opera**, which is the only sequence
   the citation parser can resolve. **A parser limitation, and the transcription is
   right.** Every digit of that entry was band-settled by `p6-c8` (`pag. 745`, `pag. 155`,
   `tom. XI.`, `§ 4`, `c. 4.`, and `(11. Nov.)` fixed externally by St Martin's feast).

---

## Disposition

**Pass 1 CLOSED. Three flags in, three flags resolved, zero accepted-illegible, zero
chunk edits, zero emendations.**

All three turned out to be the same finding: **at 600 dpi the reading is certain and the
plate is wrong.** That is a resolution, not a failure to resolve — the ambiguity these
flags recorded was in *our reading*, and it is gone; what remains is a defect in
Quaracchi's forme, which the transcription is obliged to preserve. **All three convert
from standing `[?]` to documented PLATE-DEFECT dispositions and are now CLOSED**, joining
p. 280 n. 6's `homo non separe`. **They must not be resurrected by downstream chunks, and
the `Col. 6, 12` QA line must not be counted as a defect for as long as the transcription
stays faithful.**

Because no resolution required a chunk edit, **no chunk was touched and the five
verification scripts were not run** (they are gated on an edit; pass 2 and
`build-citations.py` run every commit regardless, and the citation artefacts consulted
above are the current ones).

**Nothing carried forward from pass 1.** Passes 3 (boundary sweep) and 4 (disk cleanup)
are outside this agent's scope. The 600 dpi leaves written for this pass live at
`raw/vision/vol5/p-hires-{271,272,282}-r600-*.png` (gitignored, ~5 MB each) and are
regenerable — **hand them to pass 4's cleanup.**
