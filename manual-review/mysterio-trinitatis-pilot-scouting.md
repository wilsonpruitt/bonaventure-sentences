# *Quaestiones disputatae de mysterio Trinitatis* — mini-pilot scouting

Work 3 of Vol V. Slug `mysterio-trinitatis`, book id **9**. Scouted 2026-09-05, immediately
after the *De scientia Christi* work-close gate closed, pushed and deployed. **The second
*quaestio disputata* in Vol V** — the genre's conventions are already frozen at
`scientia-christi`, and this document records only what is DIFFERENT here plus what had to be
measured again from scratch.

English title: **"Disputed Questions on the Mystery of the Trinity."**

⛔ **The one structural difference from work 2, and it drives everything below: every question
here divides into ARTICULI.** Work 2 had none.

---

## Structure — verified on the plate, not inferred

| Fact | How it was fixed |
|---|---|
| **NO half-title leaf** | Predicted at the work-2 pilot (p. 1's half-title covers all three QD) and **confirmed**: p. 44 measured blank, **p. 45 opens directly on the display heading**. The prediction held; it was still checked. |
| **p. 44 MEASURED BLANK** | **0.0007 %** dark px at `< 160` (work 2's gate measured 0.0008 % on a different sampling stride — same leaf, same answer). |
| **Body opens p. 45** | Plate: `QUAESTIONES DISPUTATAE` small caps, `DE MYSTERIO TRINITATIS` large caps, an ornamental squiggle rule, then the **proemium** (see below), then `QUAESTIO I.`, italic subtitle, `ARTICULUS I.`, italic subtitle, and ¶ 1. |
| **EIGHT quaestiones; FOURTEEN articuli; Q. VIII undivided** | Volume index raw L93610–L93660 **and** a header grep over the whole band, which agree exactly. Real headers at raw L16054 · 16058 · 17009 · 18089 · 18107 · 18701 · 19462 · 19477 · 20251 · 21029 · 21063 · 21831 · 22322 · 22336 · 23105 · 23648 · 23685 · 24533 · 25101 · 25119 · 25571 · 26000. |
| **NO scholia, NO Summarium, NO colophon** | Grep over the band returns zero for `SCHOLION`, `SUMMARIUM` and `EXPLICIU`. Same as work 2; the reportatio conventions still do not port. |
| **Work ends p. 115** | Body runs to the foot of p. 115's right column (`…per deiformitatem gloriae in beatissimam Trinitatem.`), register beneath it. **Fixed positively, not from white space:** p. 116 measured blank and **read at full page — nothing on it**, and p. 117 carries the next work's display heading. |
| **p. 116 blank — but it does NOT measure like the others** | **0.1333 %** dark px, against 0.0007 % (p. 44), 0.047 % (*decem praeceptis*), 0.084 % (*septem donis*). ⭐ **The excess is the scan's dark gutter edge down the right margin, identified by READING the plate, not by lowering a threshold.** A blankness number is a screen; the plate is the evidence. |
| **Raw band L16037 → L26475** | ~10,440 lines over 71 printed pp. ≈ **147 lines/page**, the volume's median. Bounded at the far end by p. 117's `QUAESTIONES DISPUTATAE / DE PERFECTIONE EVANGELICA` display heading at L26474–26476. |

**Body extent: pp. 45–115 = 71 printed pages** — the largest QD in the volume and the second
largest work in Vol V after the Hexaemeron.

## ▶ CHUNKING: ONE CHUNK PER ARTICULUS — 15 chunks. Settled by Quaracchi's citation practice.

The frozen test ("look for an apparatus anchor ON the division") **returns nothing here, as it
did at the three works before it** — see below. So the unit was settled the other way, and this
work supplies the cleanest evidence the corpus has yet had for it: **Quaracchi's own internal
cross-references.**

Of the **27** `supra`/`infra q. N.` references inside the work, **26 carry `a. N.`**:

```
5  supra q. 2. a. 2      4  supra q. 3. a. 1      4  supra q. 2. a. 1
3  supra q. 5. a. 2      3  supra q. 1. a. 1/2    2  supra q. 3. a. 1/2
1 each: q. 4. a. 1 · q. 5. a. 1 · q. 6. a. 1      1  infra q. 7.   ← the only bare one
```

plus two intra-question `supra a. N`. **The articulus is the citation unit — 26 attestations
to 1 exception.** Splitting on the quaestio would break the citation match on 26 sites inside
this work alone, which is precisely the value proposition the corpus sells.

| Chunk id | Q | Art | Printed pp. | Raw band | pp. |
|---|---|---|---|---|---|
| `bon-qmt-q1-a1` | I | I | 45–51 | 16037–17008 | 7 |
| `bon-qmt-q1-a2` | I | II | 51–58 | 17009–18088 | 8 |
| `bon-qmt-q2-a1` | II | I | 59–63 | 18089–18700 | 5 |
| `bon-qmt-q2-a2` | II | II | 63–67 | 18701–19461 | 5 |
| `bon-qmt-q3-a1` | III | I | 68–73 | 19462–20250 | 6 |
| `bon-qmt-q3-a2` | III | II | 73–78 | 20251–21028 | 6 |
| `bon-qmt-q4-a1` | IV | I | 79–84 | 21029–21830 | 6 |
| `bon-qmt-q4-a2` | IV | II | 84–85 | 21831–22321 | 2 |
| `bon-qmt-q5-a1` | V | I | 86–93 | 22322–23104 | 8 |
| `bon-qmt-q5-a2` | V | II | 93–96 | 23105–23647 | 4 |
| `bon-qmt-q6-a1` | VI | I | 97–102 | 23648–24532 | 6 |
| `bon-qmt-q6-a2` | VI | II | 102–105 | 24533–25100 | 4 |
| `bon-qmt-q7-a1` | VII | I | 106–109 | 25101–25570 | 4 |
| `bon-qmt-q7-a2` | VII | II | 109–111 | 25571–25999 | 3 |
| `bon-qmt-q8` | VIII | — | 112–115 | 26000–26475 | 4 |

⚠ **Those page ranges are INDEX-DERIVED and every one of their ends is provisional.** The
frozen warning from work 2 applies unchanged: *an index span's last page is the next unit's
heading page, and that leaf may or may not be shared.* Fourteen interior boundaries here, one
per articulus transition; **each is measured on its own leaf at chunk time.** Only p. 51 has
been measured so far (below). The largest chunk is 8 printed pages — well inside what `q4` of
work 2 (11 pp.) proved buildable.

⚠ **A chunk that opens an articulus I also carries its QUAESTIO heading** (they stand on
consecutive lines: `QUAESTIO N.` + italic question subtitle, then `ARTICULUS I.` + italic
articulus subtitle). Both go into the chunk that opens.

## ▶ THE PROEMIUM FOLDS INTO `q1-a1` — it does not get its own chunk

p. 45 carries, between the display heading and `QUAESTIO I.`, a two-column proemium of seven
lines: *Volentes circa mysterium Trinitatis aliquid indagare, divina praevia gratia, duo
praemittimus tanquam praeambula…*, then the two praeambula stated (`Primum est, utrum Deum
esse sit verum indubitabile. / Secundum est, utrum Deum esse trinum sit verum credibile.`) —
which are exactly the subtitles of q. 1's two articuli. **It carries no apparatus anchor.**

It folds into `bon-qmt-q1-a1` under the frozen short-opener rule (part/work openers fold into
the first chunk of the unit they open). The alternative — a `division: 0`, `type: prologus`
chunk of its own on the Breviloquium's model — was rejected: the Breviloquium prologue is
eight printed pages in six numbered sections and is cited in its own right, this is seven
lines and **nothing in the volume cites it**. ⚠ *De perfectione evangelica* opens the same way
(`Volentes circa evangelicam perfectionem aliqua indagare…`, L26479) — **that is a prediction
to check on p. 117, not a rule already made.**

## ⛔ NO APPARATUS ANCHOR ON ANY DIVISION HEADING — the FOURTH work running

Read at ~2.2× on p. 45: nothing after the period of `QUAESTIO I.`, nothing after `ARTICULUS
I.`, and **both italic subtitles are unanchored.** The Hexaemeron's `COLLATIO I.`¹ remains the
only anchored division heading in Vol V.

★ **And the test was still worth running.** It is cheap, it is the only thing that can settle a
chunk unit positively, and the answer here freed the decision to rest on the 26 citation sites
instead — which is a *stronger* warrant than an anchor, not a weaker one.

## ⛔ p. 51 n. 1 PRINTS WITHOUT ITS NUMERAL — and two independent sources agree

p. 51's register opens with an indented entry `Cfr. III. Sent. d. 23. a. 1. q. 4.` carrying
**no superscript numeral**. Read at 3× on the plate: the indent is there, the space where the
numeral belongs is blank. **The djvu raw agrees** — the line has no marker glyph, where every
other entry on the leaf has one (`2 Vei's. 19.`, `^ F delerminationes.`, `* Respicitur…`).
The anchor exists in the body: p. 51's opening sentence ends *…feste consideranti apparet*¹
(raw L16909, glyph present).

**So the entry is real, is n. 1, and its numeral did not print.** Consequences:

- ⚠ **Do not "repair" it by renumbering the register.** The leaf carries **six** entries,
  nn. 1–6, and n. 1 is this one.
- ⚠ **An entry with no numeral is not automatically a runover from the previous page.** That
  was the first hypothesis here and it was wrong; it was killed by finding the body anchor,
  not by looking harder at the type.
- This is the *inverse* of the digit class the last two works fought: there the glyph was
  misread, here it is absent. **Both are found the same way — by pairing every footer entry
  with a body anchor, never by reading the register alone.**

## ▶ BOUNDARY 1 (p. 51) MEASURED: it FORWARDS. Split 5/1.

Art. I's replies 9–13 fill **both** columns to ~72 % of the leaf; `ARTICULUS II.` then stands
full-measure mid-leaf with its italic subtitle, and Art. II's opening (*Supposito, quod Deum
esse sit verum indubitabile…*) plus argument 1 begin **on the same leaf**. Shape family: work
2's pp. 27/32/37.

Register split **nn. 1–5 Art. I / n. 6 Art. II** (n. 6 answers Art. II's *Matthaei ultimo*⁶),
so `q1-a1` owns nn. 1–5 of p. 51 and **forwards n. 6** to `q1-a2`.

⛔ **The other thirteen boundaries are UNMEASURED.** One measurement licenses nothing — work 2
answered "yes" five times and "no" once, and no two of its six splits were alike.

## ⚠ THE RUNNING HEAD NAMES THE UNIT THAT *OPENS* ON THE LEAF, NOT THE ONE THAT FILLS IT

p. 51's head reads `DE MYSTERIO TRINITATIS QUAEST. I. ART. II.` while roughly three quarters
of the leaf is **Art. I**. Verso heads are the flat `QUAESTIONES DISPUTATAE`. **Never derive a
page's ownership from its running head** — derive it from the body anchors and the heading
positions. (This matters more here than in any earlier Vol V work, because the head is the
only place `ART. N` appears outside the headings themselves.)

## Page map

**Forty-nine surviving page numerals across 71 leaves, strictly monotonic, zero
disagreements** — no repeat of *decem praeceptis*' p. 508 → `308` or work 2's p. 35 → `33`.
Numerals at raw L16131 (46) · 16440 (48) · 16593 (49) · 16743 (50) · 17349 (54) · 17638 (56) ·
17940 (58) · 18086 (59) · 18218 (60) · 18368 (61) · 18526 (62) · 18823 (64) · 18981 (65) ·
19705 (70) · 19858 (71) · 20004 (72) · 20166 (73) · 20319 (74) · 20473 (75) · 20615 (76) ·
20775 (77) · 21060 (79) · 21206 (80) · 21359 (81) · 21669 (83) · 21813 (84) · 22097 (86) ·
22247 (87) · 22525 (89) · 22671 (90) · 22824 (91) · 23241 (94) · 23542 (96) · 23682 (97) ·
23828 (98) · 23983 (99) · 24137 (100) · 24287 (101) · 24426 (102) · 24567 (103) · 24718 (104) ·
25038 (106) · 25175 (107) · 25326 (108) · 25474 (109) · 25925 (112) · 26072 (113) ·
26223 (114) · 26367 (115). ⚠ **It is a PREDICTION table** — the leaves that dropped their
numeral are pinned by the recto running heads, and every chunk still fixes its own pages on the
plate.

## Apparatus density

p. 45 = **6** entries (nn. 1–6, register runs left column then right; **n. 4 runs over the
gutter** into the head of the right column). p. 51 = **6**. At ~7/page × 71 pp ≈ **500 for the
work** — a PLANNING figure only, of exactly the kind work 2's p. 43 n. 3 punished. ⭐ p. 45 n. 1
is *Similis quaestio solvitur I. Sent. d. 8. p. I. a. 1. q. 2.* — **an outbound citation into
our own deployed Vol I on the work's first leaf**; expect this work to be citation-dense in
both directions.

## Gutter, p. 45: ADOPT 1159

`colcrop.py vol5 45` returns **1129 on a 1 px run** — the work-opening failure in its purest
form (display heading, proemium and two centred heading stacks all cross the gutter above the
body). Profiling body rows **0.53–0.82** gives twelve windows: six at **1159–1160 on 62–65 px
runs**, six at **1133 on 12 px runs**. Band **1128–1189 (62 px)**, midpoint 1158, **centre-rule
ink island at 1155–1161 (peak 614)** — the rule sits just left of the band's middle, which is
what truncates the six narrow windows. **Adopt 1159.** ⚠ Work 2's p. 3 adopted **1130**; that
is 29 px away on a leaf of the same kind. **Measure every leaf.**

## Register — what carries, what is testable, what is absent

Counts over the whole band (10,440 lines):

| Family | Count | Status here |
|---|---|---|
| `intellect-` | **96** | Ruling: *intellectus* → **understanding**. ⭐⭐ **The narrow exception is UNREACHABLE in this work: `intellectus agens` / `intellectus possibilis` occur ZERO times.** So all 96 go to "understanding", and any bare English "intellect" in a built chunk is a defect by construction — the same mechanical check work 2 used, with an even cleaner denominator. |
| *lux* / *lumen* | 26 / **15** | Ruling 2 (*lux*→light, *lumen*→"lumen") is **LIVE** and will need the translator's note again. ⚠ **The Ps. 35:10 exemption is UNREACHED**: *In lumine tuo videbimus lumen* does not occur. The psalm *is* quoted — p. 115's last note gives Ps. 35:10 *Apud te est fons vitae* — **a different clause of the same verse, and it carries no *lumen*.** Do not let the verse number trigger the exemption; the exemption is scoped to the WORDING. |
| `contuit-` | **0** | Ruling 3 (*contuita* → "contuited") is **absent, not broken.** |
| *vacatio* / *vacare* | **2** | ⭐⭐⭐ **THE OPEN QUESTION IS FINALLY TESTABLE — see below.** |
| *quies* (noun) | 2 of 5 | ⭐⭐⭐ *quietis* twice (raw L23636, L23645, both in `q5-a2`); *quiescunt/quiescentis/quiescit* three times. |
| `notiti-` | 21 | Ordinary; watch it against *cognitio* as usual. |

### ⭐⭐⭐ *vacatio* / *quies* — OPEN SINCE `bon-praec-c4`, UNTESTABLE THROUGH TWO WHOLE WORKS, AND THIS WORK HAS THE DECISIVE SITE

The question (*vacatio*/*vacare* → "leisure / to keep leisure" against *quies*/*requies* →
"rest") has been carried unresolved through the *decem praeceptis* and closed as **untestable**
on the *de scientia Christi*, where the noun never once occurred. Here **both halves are
present, and one line holds them together**:

> raw **L25824** (`q7-a2`, printed ~p. 111): *…non **quiescit** nisi in summe amabili
> **vacando*** ^

**One clause, the verb of each family, in contrast.** The second site is raw **L25900**
(*…vacabimus et videbimus; videbimus et amabimus…*, Augustine, *De civ. Dei* XXII. 30) and the
noun sites are raw L23636/23645 (*silentium quietis*, *supercaelestis quietis*).

⚠ **DO NOT SETTLE IT AT THE PILOT.** It is settled where it is met, in `q5-a2` and `q7-a2`,
with the plate in view — and **the pilot's job was to find out that it CAN be settled and
where**, so that the chunk that meets it knows it is the deciding chunk and does not treat the
site as routine. ⚠ **A pilot's term census is a MAP, not a ruling** — that distinction is what
made work 2's four rulings hold across seven chunks.

⚠ **The near-miss to record:** the first census here ran the pattern `vacatio|vacare|vacat`
and returned **zero** — it misses *vacando* and *vacabimus*, which are the only two sites in
the work. **A stem census must be run on the stem (`vaca`), not on a list of inflections.** The
question would have closed a third time as "untestable", wrongly, on a two-character pattern
bug. ⭐ **The standing rule applies: an empty grep is not absence — when the search comes back empty
but the text is plainly doing the thing, THE SEARCH is wrong.**

## Marginalia

**Dense — one per argument or reply**, as in work 2: p. 45 gives `Triplex via.`, `Via prima.`,
`Fundamenta.`; p. 51 gives `Certitudo duplex.`, `Notandum.` (×3), `Tres gradus in notitia.`,
`De ratione meritorii in fide Dei.`, `De debito credendi.`, `Fundamenta.` Standing Vol V
convention: trimmed from the body, transcribed into the `## Notes` Marginalia list in body
order. The raw splices them mid-word (`credendi" ^^^^ *^^^ quod est congruum`).

## Registry and site wiring

- `WORKS["mysterio-trinitatis"]`: book **9**, tome 5, title *Quaestiones disputatae de mysterio
  Trinitatis*, initial `Q`, `divisionLabel: "Quaestiones"`, divisions 1–8 titled from the
  volume index.
- **`buildWorkChunkTitle` needs a new branch**, because this is the first Vol V work whose
  chunk is finer than its division: return **`Quaest. N, Art. M`** when `meta.articulus` is
  present and **`Quaest. N`** when it is not (Q. VIII). The existing `scientia-christi` branch
  is left alone.
- **Ordering inside a division already works**: `build-content.mjs` sorts on `articulus` ahead
  of `section`/`capitulum` (the Sentences key, reused). Frontmatter carries
  `work: mysterio-trinitatis`, `division: <quaestio>`, `articulus: <1|2>`, `type: quaestio`.
- Divisions go in **one at a time as each chunk lands**, subtitle verified word for word on the
  plate — the frozen rule, unchanged.

## Gate cadence — TWO gates

1. **Shakedown at the close of q. 2 (p. 67, after four chunks / 23 printed pp.)** — trigger 3,
   the ~15–25 pp seam. Work 2's shakedown found three real defects; this work is 71 pp, so an
   early gate is worth more here, not less.
2. **Work-close gate at p. 115** — trigger 2, unconditional.

Trigger 1 (~100 printed pp.) does not fire inside this work: the last gate closed at p. 43 and
p. 115 is 72 pages on.

⚠ **Carry into the first gate, from work 2's:** *a prior gate's false-positive list is not a
filter for the next work's* — three digit-drift classes there, two at *decem praeceptis*, none
shared. And **`build-citations.py` does not update the site**: run
`python3.11 tools/build-index-json.py` after any ledger rebuild, before building the site.

## Plates

Extracted for this pilot at 450 dpi: **44, 45, 51, 115, 116**. ⛔ Per the standing rule they are
deleted at each work-close gate's pass 4 — **re-extract per chunk, never in bulk.**
