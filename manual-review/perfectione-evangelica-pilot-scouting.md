# *Quaestiones disputatae de perfectione evangelica* — mini-pilot scouting

Work 4 of Vol V. Slug `perfectione-evangelica`, book id **10**, id prefix **`bon-qpe-`**.
Scouted 2026-09-15, immediately after the *De mysterio Trinitatis* work-close gate closed,
pushed and deployed. **The third and last *quaestio disputata* in Vol V.** The genre's
conventions are frozen at `scientia-christi` and `mysterio-trinitatis`; this document records
only what is DIFFERENT here, plus what had to be measured again.

English title: **"Disputed Questions on Evangelical Perfection."**

⛔ **The differences that drive everything below:** (1) a MIXED division shape — Q. I is
undivided, Qq. II–IV each divide into three articuli; (2) **one articulus, Q. II Art. II (the
mendicancy question), runs ~21 printed pages**, nearly twice the largest chunk Vol V has built;
(3) a **new register** — the vocabulary of poverty, vows and religious life, none of which the
Sentences tables or the two earlier QD exercised; (4) **the just-ratified *vacatio* rule meets
a construction it was not ratified on** (*vacare* + dative, 13 sites).

Plates extracted for the pilot: **117, 124, 125, 198, 199** (450 dpi, `raw/vision/vol5/`).

---

## Structure — verified on the plate, not inferred

| Fact | How it was fixed |
|---|---|
| **NO half-title leaf** | As predicted at the work-2 pilot (p. 1's half-title covers all three QD). p. 116 blank (read on the plate at the *mysterio* gate); **p. 117 opens directly** on `QUAESTIONES DISPUTATAE` / `DE PERFECTIONE EVANGELICA`, ornamental squiggle rule, proemium. |
| **Body opens p. 117** | Plate. Proemium (two columns, 5 lines), then `QUAESTIO I.` + italic subtitle, then ¶ *Et quoniam habitus cognoscitur per actus*², then arg. 1. |
| **FOUR quaestiones; Q. I undivided; Qq. II–IV three articuli each** | Volume index (raw L93689–L93745) and a header grep over the band agree. Real headers: Q. I L26493 · Q. II L27584 · II.1 L27627 · II.2 L28999 · II.3 L32212 · Q. III L33707 · III.1 L33726 · III.2 L34549 · III.3 L35099 · Q. IV L35703 · IV.1 L35724 · IV.2 L36301 · IV.3 L37199. |
| **NO scholia, NO Summarium, NO colophon** | Grep zero for `SCHOLION` over the band; no `EXPLICI`. `CONCLUSIO` present (7 recognizable spellings for 10 units — **find it by content**, as always). |
| **Work ends p. 198, NO colophon** | Plate: Q. IV Art. III reply 16 ends *…deducat ad ovile summi Pastoris*³ at ~40 % of the leaf; the register below it is dominated by **n. 3, a full editorial dissertation** (see Apparatus), then an ornamental rule. **Fixed positively:** p. 199 is the **Breviloquium's half-title** (`SERAPHICI DOCTORIS / SANCTI BONAVENTURAE / BREVILOQUIUM`, read on the plate), matching the frozen Breviloquium record (half-title 199, prologue opens 201). |
| **Raw band L26470 → ~L38640** | ~12,170 lines over 82 pp ≈ **148 lines/page**, the volume's median. Bounded by p. 199's half-title at L38643. |

**Body extent: pp. 117–198 = 82 printed pages** — the largest QD in Vol V.

### ⭐ Q. II's opener announces TWO articuli and the question has THREE

p. 124: *Quaestio est de paupertate, et quaeruntur **duo**. Primo … quantum ad abrenuntiationem.
Secundo, quantum ad mendicationem.* The third articulus (head of p. 156) introduces itself as a
supplement: *Tertio **ad maiorem evidentiam eorum quae de mendicitate dicta sunt**, quaeritur,
utrum pauperes validi … ad opera manualia universaliter sint astricti.* **Transcribe the opener
as printed; do not harmonise it to the index.** Qq. III and IV's openers announce three each and
have three.

⚠ **Q. IV's openers and index disagree on Art. III's subject:** the index gives *De obedientia
summo Pontifici debita*; the opener's third item is *utrum sit conveniens christianae religioni,
quod omnes obediant uni*. **Verify the in-place `ARTICULUS III.` subtitle on p. 189 word for word
before it goes in the registry**, per the standing one-at-a-time rule.

## ▶ CHUNKING: ONE CHUNK PER ARTICULUS (+ Q. I whole) — 10 chunks

**Settled by how the corpus already cites the work.** The deployed chunks carry five citations
into it, and **four of the five name an articulus**: `perfect. evang. q. 2. a. 1.` ·
`q. 3. a. 2.` · `q. 4. a. 3.` (twice) · one bare `q. 4.` Quaracchi's own work-end note (p. 198
n. 3) cites `supra de Perfectione evangelica q. 2. a. 2. ad 19 (pag. 147)`. Internal
cross-references are sparse here (`supra q. 2. a. 3.` once, `supra q. 1.` once; the work
otherwise cross-refers by `supra pag. N`), but they point the same way. The *mysterio* pattern
holds; the unit is the articulus.

| Chunk id | Unit | Printed pp. (index-derived) | Raw band | ~pp |
|---|---|---|---|---|
| `bon-qpe-q1` | Q. I (undivided) + proemium | **117–124** ✅ measured | 26470–27583 | 8 |
| `bon-qpe-q2-a1` | Q. II Art. I | 124–134 | 27584–28998 | 10 |
| `bon-qpe-q2-a2` | Q. II Art. II | 134–156 | 28999–32211 | **21** |
| `bon-qpe-q2-a3` | Q. II Art. III | 156–166 | 32212–33706 | 10 |
| `bon-qpe-q3-a1` | Q. III Art. I | 166–171 | 33707–34548 | 6 |
| `bon-qpe-q3-a2` | Q. III Art. II | 171–175 | 34549–35098 | 4 |
| `bon-qpe-q3-a3` | Q. III Art. III | 175–179 | 35099–35702 | 4 |
| `bon-qpe-q4-a1` | Q. IV Art. I | 179–183 | 35703–36300 | 4 |
| `bon-qpe-q4-a2` | Q. IV Art. II | 183–189 | 36301–37198 | 6 |
| `bon-qpe-q4-a3` | Q. IV Art. III | 189–**198** ✅ end measured | 37199–~38640 | 10 |

`division: <quaestio 1–4>`, `articulus: <1|2|3>` (absent on `q1`), `type: quaestio`.

⚠ **Every interior END is provisional** — the *mysterio* index was wrong at the end of a span
four times and at the START once (by two leaves). **The raw band is the reliable half of every
line; the page range is not.** Only boundary 1 (p. 124) and the work's end (p. 198) are measured.
Leaf-position hints from the raw, to be checked: Q. II Art. III and Q. III both stand at the
**very head** of their leaves (L32212 is 6 lines after p. 156's numeral; L33707 is 6 lines after
p. 166's) — **candidate leaf-edge boundaries**, so `q2-a2` probably ends on 155 and `q2-a3` on
165. Q. IV opens mid-p. 179.

⚠ **A chunk that opens an articulus I also carries its QUAESTIO heading and the quaestio's
opener** (mysterio rule). Here the Q. II heading and opener stand on **p. 124** while `ARTICULUS
I.` stands at the head of **p. 125** — the opener and heading still fold into `q2-a1`.

## ▶ BOUNDARY 1 (p. 124) MEASURED: FORWARDS IN THE BODY ONLY, split 5/0

Q. I's replies 7–15 fill both columns to ~58 %; `QUAESTIO II.`, *De paupertate.* and the
two-line opener stand full measure below. **All five register entries are Q. I's** (n. 1
*crucifixoris*¹ reply 8 · n. 2 *honor*² reply 9 · n. 3 *servi*³ reply 12 · n. 4 *corde*⁴
reply 13–14 · n. 5 *Augustinus*⁵ reply 15). **Heading, subtitle and opener are unanchored**
(read at ~3×; the only mark is a centred speck between heading and subtitle, no digit shape).
So `q1` = pp. 117–124 and owns p. 124's whole register; `q2-a1` inherits body only. This is the
*mysterio* p. 78 / p. 96 shape.

## ▶ THE PROEMIUM FOLDS INTO `bon-qpe-q1` — and it IS ANCHORED

p. 117's proemium (*Volentes*¹ *circa evangelicam perfectionem aliqua indagare…*, then the four
heads: humility as root, poverty, continence, obedience) folds into `q1` under the short-opener
rule, exactly as p. 45's did. **Unlike p. 45, it carries n. 1** — the textual note for the whole
work: *Hanc quaestionem sumsimus ex codicibus E D I…*, stating the edition follows **codex E**
chiefly, with D and I. ⚠ **A thin textual base again** (three codices; compare *mysterio*'s D
alone from p. 104). Expect Quaracchi conjectures and codex-specific variants in the register.

## ⛔ NO APPARATUS ANCHOR ON ANY DIVISION HEADING — the FIFTH work running

p. 117 `QUAESTIO I.` + subtitle (read at ~2×): unanchored. p. 124 `QUAESTIO II.` + subtitle +
opener: unanchored. p. 125 `ARTICULUS I.` + subtitle: unanchored (Art. I's first note is arg. 1's
*nono*¹). **Still look at every heading and every opener** — p. 117's proemium and *mysterio*'s
p. 59/p. 106 openers show openers vary.

## Page map

**68 surviving numerals over 82 leaves**, monotonic after correction. ⚠ **Seven are digit-garbled
in the raw** and are the band's answers, not the raw's: L31605 `182`=**152** · L32206 `136`=**156**
· L33569 `163`=**165** · L34772 `178`=**173** · L37456 `101`=**191** · L37901 `104`=**194** ·
L38064 `193`=**195**. Anchors for the provisional spans: 118 L26575 · 124 L27495 · 126 L27767 ·
134 L28963 · 156 L32206 · 166 L33701 · 171 L34479 · 176 L35216 · 179 L35656 · 183 L36278 ·
189 L37167 · 198 L38506. **A PREDICTION table**; every chunk fixes its own pages on the plate.

## Apparatus density

p. 117 = **8** · p. 124 = **5** · p. 125 = **10** · p. 198 = **3**. ~7/page × 82 ≈ **570 for the
work** — planning only. ⚠ **p. 198 n. 3 is an 1890s editorial DISSERTATION on papal primacy and
infallibility** (citing Pius IX, *Pastor aeternus*, the Vatican Council, and the Olivi case),
filling most of the leaf's register in two columns. **Render it literally and in full, as
editorial matter of its date** — it is Quaracchi's text, not ours, and it is neither trimmed nor
glossed. Its internal cross-refs (`supra … q. 2. a. 2. ad 19 (pag. 147)`, `infra Breviloquium
p. VI. c. 10`, `I. Sent. d. 11 …`) are free controls for `build-citations.py`.

## Gutter, p. 117: ADOPT 1164

`colcrop.py vol5 117` → **1164 on a 56 px run** (under the 60 px floor, so escalated). Body
rows 0.48–0.84 (below the heading stack): twenty windows **1163–1166 (3 px spread)**, band
**1135–1192 (58 px)**, midpoint 1163, centre-rule island **1160–1168** (peak 465) — the frozen
inked-rule case. **Default confirmed, not corrected.** ⚠ *mysterio*'s p. 45 adopted 1159 and
*scientia*'s p. 3 1130 on leaves of the same kind. Measure every leaf.

## Register — what carries, what is testable, what is new

### Carried rulings (census over the band)

1. ***intellect-* 4 · *intellig-* 55** (mostly *intelligendum* and *Ad praedictorum
   intelligentiam* → "for the understanding of the foregoing", the `bon-qsc-q2` idiom).
   `intellectus agens/possibilis`: zero → **any bare English "intellect" is a defect by
   construction.**
2. ***lux* 4 · *lumen* 6 — ruling 2 LIVE, lightly.** ⚠ **Ps. 4:7 *Signatum est super nos lumen
   vultus tui* recurs** (in a note). Apply the *mysterio* test at the site: exempt only if quoted
   AS A VERSE with no body prose leaning on *lumen*. ⚠ **Jas. 1:17 *Patri luminum*** also occurs —
   same test; if it passes, the received "Father of lights" stands. *luminaria* (Ecclus.) and
   *emolumentum* are not *lumen* hits.
3. ***contuit-* 1** (*idoneus est ad contuitionem sublimium*) → **"contuition"**, ruling 3.
4. ***fundam.* 15 — ruling 5 WILL be met repeatedly** → *fundamentum N* / *fundamenta N* in the
   apparatus. **Every chunk that meets one must say so in its Notes and quote its rendering**
   (the *mysterio* lesson: the chunk that meets a reserved site is the one that drops it).
5. ***pietas* 9** → "piety" everywhere (*septem donis* ruling).
6. ***praeceptum* 63** → "precept"; its partner ***consilium* 55** → "counsel" — **the
   counsels/precepts axis is this work's backbone**, and *decem praeceptis*' ruling carries it.

### ⭐⭐⭐ *vacare* — THE RULE RATIFIED TODAY MEETS A CONSTRUCTION IT WAS NOT RATIFIED ON.

✅ **RULED (Wilson, 2026-09-15): the dikaisune rule — contextual rendering + a translator's note;
never "rest". Recorded in repo CLAUDE.md § PERFECTIONE EVANGELICA.** Site map: `q2-a2` L29436,
29507, 29508, 29935 (the *vacare manibus* pun), 30009, 30348, 30594, 30808, 31960 (*ab …
occupationibus vacant* — "free from") · `q2-a3` L32457, 32883 (*licentia vacationis*), 33371
(*vacando … vacatio*). The analysis below is kept as the record of why.

*vacatio*/*vacare* → "leisure" / "to keep leisure" was ratified at the *mysterio* gate
(2026-09-15) on **absolute** uses (`bon-praec-c4`'s Sabbath *vacatio*; `q7-a2`'s *vacando*).
**This work has 15 `vaca-` sites, and ~11 are *vacare* + DATIVE** — *qui divinis vacant*,
*vacant divinis laudibus, orationibus*, *praedicationi … vacabant*, *spiritualibus vacare
exercitiis*, *doctrinae … et lectioni vacant* — where the Latin means "to be free for, give
oneself to". "Those who keep leisure for divine things" misreads the construction. Two sites are
the absolute/pejorative sense in Augustine's *De opere monachorum* (*dissoluta licentia
vacationis*; *eorum vacatio*), and one is his pun *qui vacare volunt manibus, omnino vacare…*,
which **turns on the one word going over** and needs one English root across both halves.
Against it, the *quies* family is present (16, incl. *Maria quiescens* vs *Martha laborans*,
and II Thess. 3's *inquieti*/*quieti*), so the distinction the rule protects is live here too.

**Recommendation (not a ruling):** keep the ratified rule for absolute *vacatio*/*vacare*, and
scope it so ***vacare* + dative → "to be free for" / "to give oneself to"** — still a `vaca-`
English distinct from "rest", so the families never collapse. Augustine's pun takes the rule
("keep leisure") in both halves. **The first chunk to meet a site is `q2-a2` (the mendicancy
replies, where *qui divinis vacant* is the objectors' own phrase) and `q2-a3` (manual labour,
where most sites are). Decide before `q2-a2` is dispatched.**

### New register — WORKING renderings, carried to the shakedown gate (not frozen)

| Latin | Working English | Why / pressure |
|---|---|---|
| *perfectio evangelica* | evangelical perfection | the title; 184 *perfectio-* |
| *mendicitas* / *mendicatio* / *mendicare* / *mendicantes* | mendicancy / begging / to beg / mendicants | 201 hits; state vs act — keep *mendicitas* and *mendicatio* apart (the opener uses one, Art. III's opener the other) |
| *paupertas* | poverty | 92 |
| *abrenuntiatio* / *renuntiare* | renunciation / to renounce | 29 |
| *dominium* / *usus* / *proprietas* / *possessio* | ownership / use / property / possession | ⚠ **the Franciscan *usus*/*dominium* distinction is load-bearing** (*quantum ad usum, non quantum ad dominium*; *absque dominio et proprietate*). "Lordship" is the alternative for *dominium*; **Wilson's call at the shakedown gate** |
| *in communi* / *in privato* / *in proprio* | in common / in private / as one's own | Art. I's own axis |
| *vilificare se* / *vilificatio* | to make oneself vile / self-abasement? | ⚠ Q. I's key term (62 *vil-* hits). Must stay distinct from *humiliare*/*humiliatio* (28), which takes "humble / humiliation"; modern "vilify" means slander. **Open — settle at `q1`, disclose, carry.** |
| *castitas* / *pudicitia* | chastity / purity | **both occur (23 / 30)**, so they cannot share "chastity". *pudicitia coniugalis* → "conjugal purity"? Open. |
| *continentia vidualis* / *sanctimonia virginalis* | widowly continence / virginal holiness | Q. III's article titles |
| *votum* | vow | 56 |
| *obedientia* | obedience | 72 |
| *praelatus* | prelate | 35; one English word throughout, even of a religious superior |
| *regulares* / *religiosi* / *religio* | regulars / religious / religion (= an order) | *religio* often means a religious order; gloss nothing, translate literally |
| *opera manualia* | manual labour | Art. III |
| *otiosi* / *inquieti* / *curiosi* | idle / restless / busybodies | II Thess. 3:11, Augustine's *De opere monachorum*; Douay has "walk disorderly … curiously meddling" — Douay adjusted to Quaracchi's Latin where the argument turns on the word |

⚠ **Polemical register.** Q. II Art. II is the mendicant controversy (against the Paris secular
masters); several objections are the opponents' own texts. **Translate them at the same literal
register as everything else**; no softening and no heightening.

## Marginalia

Dense, as in the other QD: p. 117 `Fundamenta.`; p. 124 `Duplex defectus.`, `Distinctio.`,
`Aliter.`, `Notandum.` ×3; p. 125 `Fundamenta.`, `Loci Scripturae.`, `Exemplum Christi.`; p. 198
`Duplici­ter dicitur immediatus praelatus.`, `Notanda doctrina.`, `Duplex causa universalis.`,
`Quo sensu Deus causa universalis.`, `Notandum.` Trimmed from the body, listed in `## Notes`.
**Check the gutter-side margin at full image width on every leaf** (the *mysterio* 69–73 and
p. 106 clipping).

## Registry and site wiring (when `q1` lands, not before)

Add `perfectione-evangelica` to `WORKS` (book 10, tome 5, `title: "Quaestiones disputatae de
perfectione evangelica"`, `initial: "Q"`, `divisionLabel: "Quaestiones"`), and **add the slug to
the `mysterio-trinitatis` branch of `buildWorkChunkTitle`** — the same shape (articulus present →
`Quaest. N, Art. M`; absent → `Quaest. N`, which is Q. I here, not the last question). Divisions
go in one at a time, each subtitle verified in place; **Q. I's is *De humilitate quoad actum
ipsius, utrum scilicet christianae perfectionis sit se ipsum vilificare pro Christo*, verified
on p. 117** — ⚠ the plate prints *ch istianae* with the *r* broken or absent; **`q1` settles it
by the ratified flanking-letter test** (failing impression → *ch[r]istianae*; compositor's blank →
reproduce), not by the index, which spells it in full.
`VOLUME_COMPLETE` / forward resolution: the five `forward` records into this work, and the
Breviloquium's `supra pag. 120/161/188` notes, will self-resolve as chunks land — **read the
citations diff for inbound lines at every chunk.**

## ⚠ THE BUILD PROBLEM: `bon-qpe-q2-a2` (~21 pp, raw L28999–L32211)

Twelve+ affirmative arguments (pp. 134–~139), `CONCLUSIO` at L29858 (~p. 139), a *Respondeo* to
~L30210 (~p. 142), then **~13 printed pages of replies** (at least 19; p. 198 n. 3 puts *ad 19*
on p. 147). **Not split** — the articulus is the citation unit (above), and splitting breaks the
match. But one subagent reading ~120 column bands will likely exhaust its context.

**Recommendation: ONE CHUNK, BUILT IN SEQUENTIAL PASSES into the same file** — pass A: heading,
arguments, opposing series (~pp. 134–139); pass B: *Conclusio*, *Respondeo*, replies through
~p. 147; pass C: remaining replies to the end + audits + both commits. Each pass is a fresh
subagent briefed with the prior pass's hand-off (last anchor, open register entries, page-split
map), and appends by small incremental `Edit`s (the content-filter discipline). **Nothing is
committed until pass C closes the chunk at Tier 2** — "no half-verified chunk" still holds; the
uncommitted file on disk is the hand-off. Ask Wilson before dispatch.

## Gate cadence — TWO gates

The frozen table says one gate at close (82 pp, under trigger 1's ~100). **Recommend a
shakedown as well** (trigger 3), because the register is new here even though the genre is not:
**at the close of `q2-a1` (p. 134, ~18 pp in, two chunks)** — before the giant articulus, so its
vocabulary is ruled before 21 pages are written in it. The work-close gate at p. 198 as usual.

## Plates

Per articulus, never in bulk; pass 4 deletes them. For `q1`: extract **117–124** (117 and 124
already on disk). **Extract the span's LAST leaf alone and read it first** (the standing order
that paid twelve times in *mysterio*).
