# *Quaestiones disputatae de scientia Christi* — mini-pilot scouting

Work 2 of Vol V. Slug `scientia-christi`, book id **8**. Scouted 2026-08-31, immediately after
the *De decem praeceptis* work-close gate closed, pushed and deployed. **The first
*quaestio disputata* in Vol V — and the genre the corpus already knows best**, because the
Sentences quaestio in Vols I–IV has exactly this shape. The three reportatio conventions
(Summarium, collatio-as-chunk) do **not** port; the Sentences conventions do.

English title: **"Disputed Questions on the Knowledge of Christ."**

---

## Structure — verified on the plate, not inferred

| Fact | How it was fixed |
|---|---|
| **p. 1 half-title, and it covers ALL THREE QD** | Plate read at full page. Prints `SERAPHICI DOCTORIS / SANCTI BONAVENTURAE / QUAESTIONES DISPUTATAE / DE SCIENTIA CHRISTI, DE MYSTERIO SS. TRINITATIS, / DE PERFECTIONE EVANGELICA`. Foot carries `S. Bonav. — Tom. V.` ⭐ **This is a THREE-WORK half-title** — see the consequence below. |
| **p. 2 MEASURED BLANK** | **0.0013 %** dark px at the `< 160` threshold — the cleanest blank verso Vol V has measured (*decem praeceptis* 0.047 %, *septem donis* 0.084 %). |
| **Body opens p. 3** | Plate: `QUAESTIONES DISPUTATAE` in small caps, `DE SCIENTIA CHRISTI` in large caps, an ornamental rule, then `QUAESTIO I.`, the italic subtitle, and ¶ 1. |
| **SEVEN quaestiones, I–VII, and NO articuli** | Volume index (raw L93588–L93610) lists exactly seven, each a bare `QUAEST. N` with a single *Utrum…* title and one page number. ⭐ **Confirmed negatively on the band: a grep for `ARTICULUS`/`ARTIGULUS` over the whole work returns ZERO.** Contrast *de mysterio Trinitatis* directly below it in the same index, whose every question divides into `Art. I` / `Art. II`. |
| **NO scholia, anywhere in the work** | Grep for `SCHOLION` over the band returns zero, and the index lists none. ⭐ Quaracchi's editorial matter in this work goes into the **footer register** instead — see p. 43 n. 3 below. |
| **Work ends p. 43** | Plate read. ⛔ **There is NO `EXPLICIUNT` colophon** — see below. |
| **p. 44 MEASURED BLANK** | **0.0008 %** dark px. |
| **Raw band L10048 → L16033** | ~5,990 lines. Bounded at the far end by p. 45's `QUAESTIONES DISPUTATAE / DE MYSTERIO TRINITATIS` display heading at L16034–16037. |

**Body extent: pp. 3–43 = 41 printed pages.**

## ⭐⭐ THE HALF-TITLE COVERS THREE WORKS — so works 3 and 4 have NO half-title leaf

p. 1 names *de scientia Christi*, *de mysterio SS. Trinitatis* **and** *de perfectione
evangelica* on one leaf. Every Vol V work so far has had a half-title of its own (455, 505,
533…), and the reflex that forms is "each work opens on a half-title verso-blank pair."
**That is wrong for the two QD that follow this one.** p. 44 is blank and **p. 45 opens
directly with a `QUAESTIONES DISPUTATAE / DE MYSTERIO TRINITATIS` display heading of the
same kind as p. 3's** — no half-title, no blank verso pair. Expect the same at p. 117 for
*de perfectione evangelica*, and **fix it on the plate rather than predicting a half-title
that is not there.** This also means the work map's page ranges for works 3 and 4 (45–115,
117–198) are *body* ranges already, with nothing in front of them.

## ⛔ THE WORK DOES NOT END ON A COLOPHON — and that is a genre difference, not a defect

The three Collationes sets all closed on a full-measure `EXPLICIUNT …` line, and the frozen
rule "fix every work's end positively" has been satisfied by that line three times running.
**p. 43 prints no such line.** Both columns of the body end level at ~19 % of the leaf
(*…ut experiri³ donet quod loquimur³.*), the footer register follows, and beneath it stands
an **ornamental squiggle rule** with blank paper for the rest of the leaf.

The end is therefore fixed positively from **three independent facts, none of them white
space**: the ornamental rule set below the register, p. 44 measured blank at 0.0008 %, and
p. 45's display heading opening the next work. ⚠ **The frozen rule that blank space at a
column foot is never a boundary is untouched** — none of the three facts is an inference
from white space. Expect the no-colophon close at the other two QD as well, and do not go
hunting for an `EXPLICIUNT` that the genre does not print.

## ⛔ `QUAESTIO I.` CARRIES NO APPARATUS ANCHOR — the third work running to answer this way

Read at ~2.2× on p. 3. Nothing stands after the period of `QUAESTIO I.`, and the italic
subtitle is unanchored too. **The note that documents the question exists — but it is
anchored in the BODY**: p. 3 n. 1 (`De scientia Christi in genere cfr. III. Sent. d. 14; de
hac vero quaestione I. Sent. d. 35. q. 5, d. 39. a. 1. q. 1-3, d. 43. q. 1-4, et infra
Quaest. disp. de Trin. q. 6. a. 1. — Haec quaestio deest in cod. C.`) answers the opening
sentence's *ad infinita*¹.

⭐ **This is the sharpest form of the anchor lesson the corpus has produced.** The Hexaemeron
test was "does the heading carry an anchor, and if so the heading is the unit"; here a note
of exactly the Hexaemeron's kind — one documenting the question and its codices — exists and
is anchored one line lower, in the body. **The presence of such a note is not evidence of an
anchored heading.** The quaestio is the chunk unit on the index and on Quaracchi's own
citation practice (`Quaest. disp. de scientia Christi q. N`), not on an anchor.

## ⛔ THERE IS NO `SUMMARIUM` IN THIS WORK

Verified on p. 3 (Q. I) and p. 6 (Q. II): the heading is followed immediately by the italic
*Utrum…* subtitle and then by the body. **The `### Summarium` convention is a reportatio
convention and does not port to the QD.** Do not go looking for one; do not emit the heading.

## What DOES port — the Sentences quaestio conventions, essentially entire

The printed shape on p. 3 is the shape `vol1/bon-sent-I-d1-a1-q1.md` already renders:

- opening *Quaeritur…* / *Supposito… quaeritur…* sentence,
- numbered arguments **1., 2., 3.…** for the affirmative,
- `CONTRA:` with its own numbered series,
- a full-measure small-cap **`CONCLUSIO.`** rubric, whose one-sentence content is set as a
  `> **Conclusio.**` blockquote per the frozen corpus convention,
- **`Respondeo:`** and the determination,
- the replies, **`Ad illud quod obiicitur…`** / *Ad 1, 2…*.

⚠ **`CONCLUSIO` garbles**: a case-sensitive grep over the whole band returns **4** for seven
questions. **Find it by content, never by header grep** — the same discipline the `SUMMARIUM`
header needed in the reportationes.

**Marginalia are present and dense**, in the outer margin, and are trimmed to the `## Notes`
Marginalia list per the standing Vol V convention. Attested on p. 3 (`Fundamenta.`) and on
p. 6 (`Aliter.`, `Comparatio duplex.`, `Notandum.`, `Distinctio.`, `Fundamenta.`) — roughly
one per argument, denser than the Collationes and comparable to the Breviloquium. The raw
splices them into the body mid-word exactly as elsewhere (`Fmdamenta.Civitate`,
`Fundamenta.quae`).

## ★★★ THE PAGE MAP — running heads plus thirty surviving page numerals, zero disagreements

Running heads: **verso** `QUAESTIONES DISPUTATAE`, **recto** `DE SCIENTIA CHRISTI QUAEST. N.`
Thirty standalone page numerals survive in the OCR across the band and agree with the head
sequence everywhere. Median page length is **~148 raw lines**.

| p. | numeral L | p. | numeral L | p. | numeral L |
|---|---|---|---|---|---|
| 4 | 10170 | 20 | 12488 | 34 | 14657 |
| 10 | 11033 | 21 | 12642 | 35 | 14799 *(prints `33`)* |
| 12 | 11321 | 22 | 12797 | 36 | 14950 |
| 13 | 11477 | 23 | 12949 | 37 | 15095 |
| 14 | 11618 | 24 | 13108 | 38 | 15230 |
| 17 | 12044 | 27 | 13590 | 39 | 15383 |
| 18 | 12182 | 28 | 13737 | 40 | 15531 |
| 19 | 12341 | 30 | 14032 | 41 | 15686 |
|  |  | 31 | 14192 | 42 | 15824 |
|  |  | 32 | 14352 | 43 | 15960 |
|  |  | 33 | 14504 |  |  |

⚠ **A surviving page numeral is still a raw digit.** p. 35's prints as `33` — caught only
because the line deltas either side (142 and 151 lines) are ordinary page lengths and a jump
back to 33 is not. **This is the same class as *decem praeceptis*' p. 508 printing `308`.**
The map is a **prediction table**; every chunk still closes its own span positively on the
plate.

## SEVEN CHUNKS, and the spans the index gives

Real `QUAESTIO N.` headers on the band: I L10063 · II L10554 · III L11131 · IV L12047 ·
V L13607 · VI L14368 · VII L15153. Index pages: **3 · 6 · 10 · 17 · 27 · 32 · 37**, and the
band puts every header on the index's page.

| chunk | division | span (index + band) | printed pp. |
|---|---|---|---|
| `bon-qsc-q1` | 1 | 3–6 | 4 |
| `bon-qsc-q2` | 2 | 6–10 | 5 |
| `bon-qsc-q3` | 3 | 10–17 | 8 |
| `bon-qsc-q4` | 4 | 17–27 | **11** |
| `bon-qsc-q5` | 5 | 27–32 | 6 |
| `bon-qsc-q6` | 6 | 32–37 | 6 |
| `bon-qsc-q7` | 7 | 37–43 | 7 |

⚠ **Every span above is an index claim except its two ends.** Per the frozen rule, the index
gives a **heading page**, and a heading page may be shared — **never derive a span's last page
by subtracting one from the next question's index page**, and close each span positively.

⛔ **`bon-qsc-q4` is the largest single chunk Vol V has attempted** (11 printed pp., against
the Hexaemeron's ~5.5 and the *decem praeceptis*' ~3.7). It is q. 4, *Utrum quidquid a nobis
certitudinaliter cognoscitur cognoscatur in ipsis rationibus aeternis* — the illumination
question, the most heavily read text in the work. **It is not split**: the quaestio is
Quaracchi's citation unit and splitting it would break the citation match that is the
corpus's whole value proposition. **Build it with the small-incremental-append discipline
from the start** (the content-filter rule frozen at the Itinerarium), not after a first kill.

## ⭐ BOUNDARY 1 (p. 6) MEASURED — IT FORWARDS

The only interior boundary read at the pilot. p. 6 is **shared**: Q. I's replies (*Ad illud
quod obiicitur* 4–11) fill the upper ~60 % of both columns, then `QUAESTIO II.` and its
italic subtitle stand full-measure mid-leaf, and **Q. II's own numbered body begins on the
same leaf** (*Supposito, quod Deus cognoscat infinita, quaeritur…*, then args 1 and 2). The
leaf's register carries **nine notes**, splitting by anchor: **nn. 1–6 are Q. I's**, **nn. 7–9
are Q. II's** (n. 7 answers Q. II's opening *essentiam*⁷). By the p. 498 rule — a shared page
forwards only when the incoming unit's numbered *body* reaches it — **p. 6 forwards.**

⛔ **The remaining five boundaries (pp. 10, 17, 27, 32, 37) are UNMEASURED.** *De decem
praeceptis* answered "no" at its first boundary and "yes" at the other five under one test;
one measurement here licenses nothing. **Re-ask the p. 498 rule on the plate at each.**

## Apparatus density — and a warning about averaging it

p. 3 carries **9** numbered notes, p. 6 carries **9**, p. 43 carries **3**. The naive
~9/page × 41 pp ≈ **370 entries for the work** is a planning figure only, and p. 43 shows why
it will be wrong in both directions: its **n. 3 is a full editorial dissertation** filling
roughly half the leaf — a whole page of small type under three note numbers. **The
*decem praeceptis* lesson stands: a count outside the band is a prompt to recount on the
plate, never a defect on its own.**

## Gutter — p. 3 measured, and it is the work-opening failure

`colcrop.py vol5 3` returns **1103 on an 8 px run** — the loud failure, and the expected one
(the `QUAESTIONES DISPUTATAE` / `DE SCIENTIA CHRISTI` display stack crosses the gutter). The
skew screen reports 135 px drift and names the outlying slices itself: **a stacked region,
not skew.** Profiling rows **0.34–0.62** (below the stack, above the footer) gives eleven
windows agreeing at **1129** on 58–59 px runs, band **1100–1160 (61 px)**, centre-rule island
**1129–1133 (peak 447)**. **ADOPT 1130 for p. 3.**

## Registry (to go in with `bon-qsc-q1`, division 1 only)

`site/scripts/build-content.mjs`: `WORKS["scientia-christi"] = { book: 8, tome: 5, title:
"Quaestiones disputatae de scientia Christi", initial: …, divisionLabel: "Quaestiones",
divisions: { 1: … } }`, **and a new branch in `buildWorkChunkTitle`** returning
`Quaest. ${meta.division}` for the QD slugs, beside the existing `Coll. ${meta.division}`
branch. `type: quaestio`, which the Sentences path already uses.

**Id prefix `bon-qsc-`** (`qsc` = *quaestiones … de scientia Christi*), giving
`bon-qsc-q{1..7}`. It extends cleanly to the two QD that follow — `bon-qmt-…` and
`bon-qpe-…` — and does not collide with any existing prefix (`bon-brev`, `bon-itin`,
`bon-red`, `bon-hex`, `bon-don`, `bon-praec`).

⭐ **This work has no suffix-less slug** — no prologue, no capitula table, no scholion — so
the census blind-spot class does not apply, as in the *septem donis* and the *decem
praeceptis*.

## Cadence

**ONE gate, at the work close** (41 pp, well under the ~100 pp trigger); deploy boundary =
work close. ⚠ **But the shakedown trigger DOES fire here, and it has not fired since the
Hexaemeron** — this is a **new genre** in Vol V, the first QD, and the frozen rule is a
shakedown gate at the first structural seam ~15–25 printed pages in. **That seam is the
close of `bon-qsc-q3` at p. 17** (14 pp in) **or of `bon-qsc-q4` at p. 27** (24 pp in);
q4's close is the better fit for the 15–25 pp window and puts the gate immediately after the
work's largest and most-read chunk. **Recommend: shakedown gate at the close of `bon-qsc-q4`,
then the work-close gate at p. 43.** Plates per quaestio, never in bulk.

## Register — what carries in, and the one open question that may finally be tested

The Sentences key-terminology and scholastic-formulae tables in `CLAUDE.md` govern; this is
the genre they were written for. Both *septem donis* rulings continue to bind
(*pietas* → piety everywhere; *intellectus* → understanding / *intelligentia* → intelligence
in body prose).

⭐ **This work is a live test for two of them, and one is the question the *decem praeceptis*
gate left explicitly open.**
1. ***intellectus* / *intelligentia*** is under **maximum** pressure here — the work is about
   knowing, *intellectus divinus* and *intellectus humanus* stand in one argument on p. 3
   (¶ 8), and q. 4 is the illumination question. Expect the rule to be exercised harder than
   in any previous work, and expect its ratified narrow exception (a fixed philosophical
   doctrine the rule would misname) to be reached for. **It is narrow. c2 of the
   *praeceptis* is the only instance the corpus has ratified.**
2. ⛔ ***vacatio*/*vacare* → leisure vs *quies*/*requies* → rest** closed OPEN at the last
   gate for want of a second data point, and the resume note named this work as a possible
   place to test it. **It is not. Measured on the band at the pilot, so no chunk has to
   re-ask it: *vacatio*, *vacare* and *vacat* occur ZERO times; *quies* returns two hits and
   both are the verb *quiescat*, not the noun.** The *vacatio* side never appears, so no
   contrast can arise and there is nothing to test. **The question carries forward
   untested for a second work** — this is now a fifth consecutive unit (praec. c4–c7 and the
   whole of *de scientia Christi*) with no second reading. The *quietans/quietativus/
   quietatio* family that IS here (≈7 occurrences, all *quietare*-derived, e.g. *fine
   quietante*, *quietatione desiderii*) is a different word and does **not** count as a
   datum on this question — do not let it be read as one at the gate.
