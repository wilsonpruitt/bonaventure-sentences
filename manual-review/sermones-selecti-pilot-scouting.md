# *Sermones selecti de rebus theologicis* — mini-pilot scouting

Work 11 of Vol V, the volume's last. Slug `sermones-selecti`, book id **14**, id prefix
**`bon-serm-`**. Scouted 2026-09-18, the day the *De perfectione evangelica* deployed.
English title: **"Selected Sermons on Theological Matters."**

⛔ **The finding that reframes the whole plan: the work map's "dozens of independent short
pieces, pick N at the pilot" was wrong. There are FOUR sermons and ONE annexed *tractatulus* —
five units, 45 printed pages, and the every-N-sermones rule is moot.** The volume index
(printed p. 582, raw L94273–94282) lists *Sermo I–IV* and then *Tractatus. De plantatione
Paradisi*; the band holds exactly four bare `SERMO N.` headings and one `TRACTATUS`; the
colophon on p. 579, `EXPLICIUNT SERMONES SELECTI.`, closes all five.

Plates extracted for the pilot: **533, 534, 535, 539, 553, 567, 574, 579, 580, 581** (450 dpi).

---

## Structure — verified on the plate, not inferred

- **p. 533 half-title** (`SERAPHICI DOCTORIS / SANCTI BONAVENTURAE / SERMONES SELECTI / DE REBUS
  THEOLOGICIS`), no alternate title, no signature at the foot. **p. 534 MEASURED BLANK
  (0.0005 %).** **Body opens p. 535** directly on `SERMO I.` — no work-level display heading, no
  proemium, no capitula table.
- **Work ends p. 579**, fixed positively: the Tractatus's *Amen.* closes at ~25 % of the leaf in the
  right column; **`EXPLICIUNT SERMONES SELECTI.` set full measure beneath both columns**; a
  five-note register; an ornamental rule at ~56 %; rest white. **p. 580 MEASURED BLANK (0.0016 %);
  p. 581 is the unnumbered `INDEX OPUSCULORUM THEOLOGICORUM` display leaf** (the index numerals
  resume at 582). **Body extent pp. 535–579 = 45 printed pages.**
- **Form: the reportatio shape, not the QD shape.** Every unit opens with a display heading, an
  italic subtitle, and a **full-measure `SUMMARIUM`** keyed to paragraph numbers; the body is
  numbered paragraphs with dense marginalia; there is no *Sed contra*, no *Conclusio*, no reply
  series (a grep of the band returns one inline *respondeo*, zero `CONCLUSIO`). Sermo II's
  Summarium announces *quinque quaestiones* inside Pars I — **quaestio-shaped paragraphs inside a
  sermon; find them by content, they carry no display heading.** Everything in the Hexaemeron /
  *septem donis* / *decem praeceptis* block ports: `### Summarium` at the head of each language
  block, marginalia trimmed to `## Notes`, count the body every time.
- ⛔⛔ ~~**Sermo IV and the Tractatus each end on a printed `— Explicit.`**~~ **— HALF WRONG,
  corrected 2026-09-19 when every unit had been read.** The measured truth is **FOUR OF FIVE**:
  **Sermones I, II, III and IV carry the printed `— Explicit.`** (small caps, inline, after the
  closing *etc.* / *Amen.*; Sermo II's at p. 553, Sermo III's at p. 566, Sermo IV's at p. 574, all
  confirmed at 4×) — **and THE TRACTATUS DOES NOT**, read at 4× across the whole column foot of
  p. 579. It ends on the colophon `EXPLICIUNT SERMONES SELECTI.` alone.
  ▶ **This sheet was wrong about the one unit nobody re-checked, and silently right about two it
  never claimed** (Sermones I and III, found by `s1` and `s3`). **Transcribe the word where it
  stands; it is Quaracchi's text and the positive end-marker of the unit — but never infer it, and
  record its absence at a stated magnification, as `bon-serm-tract` did.**

## ⭐⭐ THE TRACTATUS IS A FIFTH UNIT OF THIS WORK, NOT A WORK OF ITS OWN — Quaracchi says so

p. 574 n. 8, the note on the Tractatus's title (read at 2×): *Quatuor praecedentibus sermonibus
annectimus hunc **tractatulum**, secundum formam valde similem sermonibus. — Bonelli hunc
tractatulum ex unico sumsit cod. Tudertino, quem cum iterum cum editione contulerimus, invenimus in
ipso fere 35 locos alius et melioris lectionis quam recepta ab illo. Pauca manifesta vitia iam a
Bonelli emendata erant.* Three facts converge: the editors **annex** it to the four sermons as a
*tractatulus* of the same form; the colophon that closes it is the **sermons'** colophon; the volume
index lists it inside the Sermones section. ⚠ Against that, the *Index alphabeticus* gives it its own
siglum **DPL** beside **SS** (raw L94290). ✅ **RULED (Wilson, 2026-09-18): ONE WORK, FIVE DIVISIONS** — the
editors' *annectimus* outranks their own back-matter siglum (ruling 1 below).

⭐ **It is a ONE-WITNESS text** (*ex unico cod. Tudertino*), collated by the editors against
Bonelli's edition with ~35 improved readings. Expect conjectures note by note, as in
`bon-qmt-q6-a2` after p. 104 n. 4. Sermo III's textual note (p. 553 n. 3) likewise records the
editors' policy for that sermon: *Bonelli, unius codicis apographo usus … lectiones variantes ad
calcem ponendae viderentur* — read it in full before building `s3`.

## ▶ CHUNKING: ONE CHUNK PER SERMON + ONE FOR THE TRACTATUS — FIVE chunks

| chunk | unit | pp. (measured at both ends) | raw band | size |
|---|---|---|---|---|
| `bon-serm-s1` | Sermo I *De triplici testimonio sanctissimae Trinitatis* | **535–538** | L86902 → L87455 | 4 pp |
| `bon-serm-s2` | Sermo II *De regno Dei descripto in parabolis evangelicis* | **539–553** | L87456 → ~L89674 | 15 pp |
| `bon-serm-s3` | Sermo III *De sanctissimo corpore Christi* | **553–566** | ~L89675 → L91703 | 14 pp |
| `bon-serm-s4` | Sermo IV *Christus unus omnium magister* | **567–574** | L91704 → L92777 | 8 pp |
| `bon-serm-tract` | Tractatus *de plantatione Paradisi* | **574–579** | L92778 → L93513 | 6 pp |

Frontmatter: `work: sermones-selecti`, `division: 1..5`, `type: sermo` (1–4) / `type: tractatus`
(5). The sermon is the citation unit — Quaracchi cites these pieces **by name** (`bon-hex-c17`
p. 410 n. 1 *in opusculo de plantatione paradisi*; `bon-don-c1` *sermone de Plantatione paradisi
infra impresso*; p. 535 n. 1 cites *Hexaëm. collat. 9* the other way), which is the resolver's one
silent class (named-work references) and goes on the resolver docket, not the build.

⚠ **`bon-serm-tract` is a suffix-less slug — the census blind-spot class.** Ledger line
`bon-serm-tract<TAB>…`; check any enumeration of this work against a roster of **5**.

⚠ **Sermo II (15 pp) and Sermo III (14 pp) are the largest single-agent chunks Vol V would have
attempted** (previous single-agent max: `bon-qsc-q4`, 11 pp; the 21-page `q2-a2` took three passes).
✅ **RULED (Wilson, 2026-09-18): TWO sequential passes each** into one uncommitted file (A: heading,
Summarium, Pars I; B: the rest, audits, both commits), with the `q2-a2` hand-off discipline —
measurements as measurements, predictions as predictions, resume POINT not resume page. **Sermones I,
IV and the Tractatus: one agent, the normal cadence.**

## ▶ BOUNDARIES — ALL FOUR INTERIOR SEAMS MEASURED ON THE PLATE

| seam | leaf | shape | register split | incoming subtitle |
|---|---|---|---|---|
| 1 | p. 539 | **LEAF EDGE** — running head + numeral, then `SERMO II.` at the head | 0/all | **ANCHORED** ¹ |
| 2 | p. 553 | **SHARED** — Sermo II closes *Amen. — EXPLICIT.* at ~25 %; `SERMO III.` + subtitle + a Summarium that fills the rest of the leaf and continues on 554 | **2/1** (nn. 1–2 Sermo II; n. 3 = Sermo III's textual note, **runs over the gutter**) | **ANCHORED** ³ |
| 3 | p. 567 | **LEAF EDGE** — `SERMO IV.` at the head | 0/all | unanchored (2× read; builder re-checks) |
| 4 | p. 574 | **SHARED** — Sermo IV closes *— Explicit.* at ~30 %; `TRACTATUS / de plantatione Paradisi` + Summarium + ¶ 1 on the leaf | **7/2** (nn. 1–7 Sermo IV; n. 8 = title note, n. 9 = ¶ 1's Gen. 2:8) | **ANCHORED** ⁸ |

⭐ **A NEW CASE FOR THE p. 498 RULE.** On p. 553 the incoming unit's numbered body does NOT reach the
leaf (Sermo III's ¶ 1 begins on 554 below the two-leaf Summarium), yet the leaf forwards n. 3 —
because **the subtitle itself is anchored**. The rule's letter ("only when the incoming unit's
numbered BODY reaches it") was written for works whose headings carry nothing; its spirit ("read
anchors, only anchors") decides here and gives 2/1. ▶ **State it as: a shared leaf forwards
whatever the incoming unit ANCHORS on it — body, subtitle or opener.**

⚠ **Subtitle anchors: I no · II yes · III yes · IV no · Tractatus yes.** Three of five — the
*mysterio* opener lesson again: neither expectation is a rule; read the line each time.

⚠ **The running head on both shared leaves names the INCOMING unit** (p. 553 `SERMO III.` over a
quarter-leaf of Sermo II; p. 574 `TRACTATUS DE PLANTATIONE PARADISI.` over a third of Sermo IV).
The frozen rule holds: never derive ownership from a running head.

## ⛔ `SERMO I.` CARRIES NO APPARATUS ANCHOR — the SIXTH work running

Read at 2× on p. 535: nothing after `SERMO I.`, nothing after the subtitle's period. The Hexaemeron's
`COLLATIO I.`¹ remains the only anchored division heading in Vol V.

## ⛔⛔ THE p. 535 PLATE IS SCANNED MIRROR-REVERSED — flip it before anything else

The archive's page image for printed p. 535 (PDF 611) is a horizontal mirror of the leaf: every line
reads right-to-left, the columns are swapped, and **the djvu OCR for the leaf (raw L86902–87020) is
reversed-letter garbage** (`.eiJfiJinhT oKmiaailon£8 …`). `extract-pages.py` faithfully produces the
mirrored plate. **`ImageOps.mirror()` restores it exactly** — flipped, the leaf reads cleanly, the
left column holds ¶ 1–2 and the right ¶ 3, the register reads in order.

- The flipped image has been written over `raw/vision/vol5/p-535.png` for this pilot.
  ⚠ **Any `--force` re-extraction (and pass 4 followed by re-extraction) brings the mirror back.**
  The `s1` builder must flip first and say so in `## Notes`.
- **The raw is unusable for p. 535's body and footer** — the leaf is set from the plate alone, as
  a badly-degraded leaf would be. The three later leaves of Sermo I (536–538) OCR normally.
- **Gutter p. 535 (flipped): ADOPT 1356.** `colcrop.py vol5 535` gives 1356 on a **63 px** run;
  `gutter-profile.py 535` returns 24 windows at 1356, spread **0 px**, band 1325–1387, centre-rule
  island 1353–1358 (peak 205). ⚠ The value is a *verso*-range number on an odd leaf because the
  mirror moves the gutter to the other side of the image — it is the right split for the image you
  read, and it is not evidence about the unflipped leaf.
- Only this leaf is affected: the OCR reverses nowhere else in the band (checked by the page
  numerals and running heads, which read normally from p. 536 on).

## Page map — a PREDICTION table

Running-head numerals surviving in the raw (band L86894 → L93513, ~150 lines/page):
536 L87022 · 537 87176 · 538 87310 · 540 87551 · 541 87709 · 543 88024 · 544 88174 · 549 88965 ·
553 89585 (prints `833`) · 554 89673 (`334`) · 560 90621 · 561 90769 · 562 90925 · 563 91112 (`363`) ·
564 91279 (`364`) · 565 91430 (**prints `563`** — a raw digit slip of the `p. 508 → 308` class) ·
568 91803 · 572 92421 · 574 92727 (`b74`) · 577 93173 (`877`) · 578 93327 (`378`).
Display headers: `SERMO II.` L87456 · `SERMO III.` L89675 · `SERMO IV.` L91704 · `TRACTATUS`
L92778 · `EXPLICIUNT` L93513. **Every chunk still closes its own span on the plate.**

## Apparatus density

p. 535 = 4 notes (n. 1 runs over the gutter and cites **our own `bon-qmt-q1-a2` at *pag. 54 seqq.***
and `bon-hex-c9`) · p. 553 = 3 · p. 574 = 9 · p. 579 = 5. ~6/page × 45 ≈ **270 for the work** — a
planning figure, not a gate. ⚠ p. 553 n. 3 and p. 574 n. 8 are **editorial dissertations on the
sources** (Bonelli's apograph, the Todi codex); expect the *scientia Christi* p. 43 n. 3 shape and
render in full. ⭐ The Tractatus's apparatus will carry Bonelli variants (*Bonelli: …*, attested p. 579
n. 3) — a **printed-edition witness by name**, not a siglum; transcribe as printed.

## Register — what carries, what is new

**Census over the band (L87022–93513, p. 535 excluded as unreadable in the raw):**
- ***intellect-* 9, *intelligent-* 8** → understanding / intelligence on the rule; bare "intellect" is
  a defect unless inside *intellectus agens/possibilis* (none seen).
- ⭐⭐ ✅ ***lux/luc-* ~37 against *lumen/lumin-* ~45 — RULING 2 AT ITS HEAVIEST IN VOL V, AND IT
  STANDS UNCHANGED (Wilson, 2026-09-18).** The Tractatus turns on *duodecim rerum creatarum lumina*
  (§§ 4–6) and Sermo IV on *lumen revelationis*. "Lumen/lumina" stands at all ~45 sites; the
  `tr-lumen` note goes in **at the first occurrence of each chunk**, per the frozen convention.
  Verse test at every scriptural site (**Ps. 4:7 keeps "lumen"**; **Jas. 1:17 *Patri luminum* →
  "Father of lights"**, `bon-don-c1` precedent). ⛔ **The *lumina* → "lights" carve-out for the
  Tractatus was REFUSED** — *lux* stands in the same treatise (*veritatis lumina et caritatis
  solatia* against the closing *arma lucis*), so the carve-out would collide at exactly the sites
  the ruling protects. **Cost accepted: a transliteration ~45 times in 45 pages.**
- ***vaca-* ZERO; noun *quies* ZERO** (only *conquiescat*, *quiescens* and *quietudo* — p. 579
  *internarum quietudinum* → "inward quietudes", a different noun). **The pair is untestable here;
  record it, do not reopen it.**
- ***contuitum* 1** (Sermo IV, *per simplicem contuitum*) → "contuition" (ruling 3).
- ⛔⛔ ~~***fundam.* ZERO** — ruling 5 not reached~~ **— THIS CENSUS LINE IS WRONG (corrected
  2026-09-18 at `bon-serm-s2` pass B).** p. 552 n. 4 prints **`fundam. 3`**, retained as
  *fundamentum* 3 under ruling 5. `s2` pass A repeated the false zero because it inherited it from
  this sheet. ▶ **Cause: this census was run over the RAW, and Vol V's raw is cascade-fragmented
  precisely in the APPARATUS — where ruling 5 lives.** A raw-side census cannot see a register item
  that occurs only in footers. **Every remaining chunk re-runs the `fundam.` census over the BUILT
  FILES; no ruling-5 zero is ever reported off the raw again.**
- ***pietas* 3** → piety.
- **Carried from the Collationes and binding:** *praeceptum* precept / *mandatum* commandment /
  *lex* law; *intellectus*/*intelligentia*; *pietas*.

**New — the work's own vocabulary, WORKING renderings for Wilson's shakedown ruling:**
- ⭐ ✅ ***magister* → "teacher" throughout Sermo IV — RULED (Wilson, 2026-09-18), including inside
  Matt. 23:10.** Title *Christus unus omnium magister* → "Christ the one teacher of all";
  *magisterium* → "teaching office" / "mastership" by context; the Douay's *"one is your master,
  Christ"* adjusted to *"one is your teacher, Christ."* The sermon argues throughout from *docere*,
  *doctrina*, *discipulus*, so quotation and expounding prose carry one English word (the
  Douay-adjusted-to-Quaracchi rule, *pietas* precedent). ⛔ **Lombard stays "the Master"** —
  the two never meet here. See ruling 2 below.
- ***testimonium* → "testimony"**, *testis* → "witness" (Sermo I; I John 5:7 Douay *there are three
  who give testimony* agrees).
- ***regnum Dei* → "the kingdom of God"**; *parabola* → parable; *regnare* → reign.
- ***corpus Christi* → "the Body of Christ"** (capital, the sacrament); *figura* → figure;
  *praefigurare* → prefigure.
- ***plantatio* → "planting"**, *plantula* → "little plant", *paradisus* → paradise (never "garden"
  except where *hortus* is printed); *lignum vitae* → "the tree of life" (Douay).
- ***meditatio* / *contemplatio* / *devotio*** → meditation / contemplation / devotion — the
  Itinerarium's *contemplatio* rule; *excessus* → "transport" (Tractatus § 3 *excessivam
  contemplationem* → "transporting contemplation").
- ***sapientia* 68** → wisdom (Sermo I's *documenta sapientiae*, Tractatus § 1 *invisibilis Dei
  sapientia*).

## Marginalia

Dense, one per paragraph or argument, both margins (p. 535: `Introductio.`, `Est triplex ratione
effectuum.`; p. 574: `Ortus et effectus dissensionis.`, `Epilogus.`, `Tria impedimenta …`,
`Introductio.`). Trimmed to `## Notes` in body order. ⚠ Check the gutter-side margin on every leaf
for scan clipping (the `bon-qmt-q3-a1` class) on a full-image-width strip.

## Registry and site wiring (when `s1` lands, not before)

- `WORKS["sermones-selecti"]`: `book: 14`, `tome: 5`, `title: "Sermones selecti de rebus
  theologicis"`, `initial: "S"`, `divisionLabel: "Sermones"`, `divisions: { 1: "Sermo I: De triplici
  testimonio sanctissimae Trinitatis" }` — then one line per chunk, each verified in place.
- `buildWorkChunkTitle`: a new branch for `sermones-selecti` returning **`Sermo ${division}`**, and
  **type-first `if (meta.type === "tractatus") return "Tractatus"`** beside `capitula`/`scholion`/
  `opusculum`.
- `check-vol5-census.py`: nothing (the ledger is slug-keyed). `KNOWN_TOTALS`: fed per page as read.

## Gate cadence

✅ **RULED (Wilson, 2026-09-18): ONE GATE, AT THE CLOSE (p. 579). NO SHAKEDOWN.** 45 pp, one work,
trigger 2; trigger 1 does not fire; the "every-N-sermones" rule is retired unused. The trigger-3
seam after Sermo II (p. 553, two chunks, 19 pp) was **declined for a stated reason**: Sermo IV's
*magister* and the Tractatus's *lumina* are the work's two register loads and **both fall after
it**, so a shakedown there would see neither. The register was ruled instead — off this sheet,
before the first chunk — which is what made the *perfectione* gate arrive with nothing to repair.
Deploy boundary = work close = **the end of Vol V**.

## ✅✅ THE FIVE RULINGS — WILSON, 2026-09-18, off this sheet, before a chunk existed

**All five taken as recommended, in one sitting, no file opened.** These are the work's settled
conventions; do not re-litigate them chunk by chunk.

1. ✅ **THE TRACTATUS IS THE FIFTH DIVISION OF `sermones-selecti`** — `bon-serm-tract`,
   `division: 5`, `type: tractatus`. **The editors' own sentence decided it** (p. 574 n. 8,
   *Quatuor praecedentibus sermonibus **annectimus** hunc tractatulum, secundum formam valde
   similem sermonibus*), with the shared colophon and the index placement agreeing. The
   *Index alphabeticus*' separate **DPL** siglum is an indexing convenience and does not
   outweigh the editors' statement of what the piece IS.
   ▶ **Transferable: when the edition says in words what a unit is, that outranks how the
   edition's own back-matter files it.** An index is a finding aid; a note is a claim.
2. ✅ ***magister* → "teacher" THROUGHOUT SERMO IV, INCLUDING INSIDE Matt. 23:10.** The Douay's
   *"one is your master, Christ"* is adjusted to *"one is your teacher, Christ"* on the frozen
   Douay-adjusted-to-Quaracchi rule and the *pietas* precedent: the sermon's whole argument runs
   on *docere* / *doctrina* / *discipulus*, so the quotation and the prose expounding it must
   carry one English word. ⛔ **Lombard remains "the Master" everywhere in the corpus** — the two
   never meet in this work. ⚠ The third option (teacher in the body, master in the quotation) was
   **refused**: it is the shape the *scientia Christi* gate rejected when it declined "quotation
   boundary" as a licence class.
3. ✅ **SERMO II AND SERMO III ARE BUILT IN TWO SEQUENTIAL PASSES EACH**, one uncommitted file per
   sermon, `q2-a2` hand-off discipline — **measurements as measurements, predictions as
   predictions, resume POINT not resume page.** Pass A: heading, Summarium, Pars I. Pass B: the
   rest, audits, both commits. Committed only when pass B closes it at Tier 2.
   ⛔ **Splitting either sermon into two chunks was refused** — Quaracchi cites these pieces whole
   and by name, and splitting breaks the citation match.
4. ✅ **ONE GATE, AT THE WORK CLOSE (p. 579). No shakedown.** ▶ **The reason is the one the
   *perfectione* gate proved: a shakedown is worth firing only where it can see the work's
   register loads, and both of this work's — Sermo IV's *magister* and the Tractatus's twelve
   *lumina* — fall AFTER the p. 553 seam.** Ruling the register now, off the evidence sheet,
   does what the shakedown would have done and does it for the whole work.
5. ✅ **RULING 2 STANDS UNCHANGED AT ALL ~45 SITES** — *lux* → light, *lumen*/*lumina* → "lumen"/
   "lumina", with a **`tr-lumen` note at the first occurrence in each chunk** (the frozen `tr-`
   convention, unchanged) and the verse test at every scriptural site: **Ps. 4:7 keeps "lumen"**,
   **Jas. 1:17 *Patri luminum* → "Father of lights"** (Douay, `bon-don-c1` precedent).
   ⛔ **The *lumina* → "lights" carve-out for the Tractatus was refused**, because *lux* occurs in
   the same treatise (*veritatis lumina et caritatis solatia* against the closing *arma lucis*) and
   the carve-out would collide with it at exactly the sites the ruling exists to keep apart.
   **Cost accepted knowingly: a transliteration standing ~45 times in 45 printed pages.**

▶ **Procedure note — the *perfectione* finding held a second time, and earlier.** There the
evidence sheet was compiled the morning of the gate; here it was compiled **before a single chunk
existed**, and the rulings are in hand before the first dispatch rather than at the close. All five
turned on the same three columns: the site census, the decisive quoted sentence, and the one-line
cost of each alternative. **Two of the five (1 and 5) were decided by a sentence the edition itself
prints; two (2 and 3) by a precedent already ratified elsewhere in the corpus; one (4) by where the
load falls.** None needed a file opened.

## Plates

Per unit, never in bulk; pass 4 deletes them. For `s1`: 535–538 (**flip 535 first**). Extract the
span's LAST leaf alone and read it first — every interior seam here is measured, but the standing
order stays.
