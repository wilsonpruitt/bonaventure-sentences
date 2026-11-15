# *Lucam* chunk manifest: stage 1 notes (Cap. I–III + division 0; 2026-11-14, Opus)

Rows are in `lucam-chunk-manifest.tsv`. Each claim below is labelled **MEASURED** (read on a 300 dpi plate crop
this session) or **PREDICTION** (text layer only). No chunk was built and nothing was committed.

## Plates read (MEASURED)

35 targeted crops. They were taken from `raw/vision/vol7/p-NNN.png` at 300 dpi and cut to column and row windows
(the gutter was measured per leaf, as `colcrop`'s `auto` does). The crops cover pp. **3** (top), **6R**, **7**
(full top, L zoom, R), **10R**, **11** (top), **12L/R**, **13L**, **17R**, **20R**, **27R**, **30R**, **34L/R**,
**38L**, **43** (full), **44L**, **48L**, **51R**, **54L/R**, **56L**, **58L**, **61L**, **62R**, **65L**, **69**
(full), **75L/R**, **78L**, **81R**, **85L**, **87R**, **88** (full). Every opening and every end in the TSV was
read on one of these. Paragraph numbers lying between boundaries come from the text layer (PREDICTION). They are
anchored by the plate-read numbers on either side.

## Where the draft rows were wrong (MEASURED)

- **c. 1 vv. 5–17 / 18–25:** the 17R rubric *Tertio describitur promissionis confirmatio quadrupliciter.* stands
  ABOVE **¶ 29**, the un-versed divisio *Et dixit Zacharias etc.*, and ¶ 30 is the first paragraph tagged Vers. 18.
  So the chunks are **¶¶ 7–28** and **¶¶ 29–39**, not 7–30 and 31–39.
- **Prooemium:** last ¶ is **24**, not ~27. It ends 7L upper, as predicted.
- **Prologus + expositio:** these end on **p. 11**, not p. 10. Expositio ¶ 11 runs across the top of both columns of
  p. 11, above the `COMMENTARIUS / IN EVANGELIUM S. LUCAE / Capitulum I.` stack. Row: pp. 7–11.
- **Cap. II's last ¶ is 111**, not 110 as the setup table has it. ¶ 111 is an un-versed epilogue paragraph on 69R.
- The other Cap. I drafts held: ¶ 40 (20R), ¶ 71 (27R), ¶ 86 (30R), ¶ 104 (34R), ¶ 119 (38L), all at the
  predicted headings.
- Headings the draft did not name, wording read on the plate:
  - 34R `De gratiarum actione pro ortu praecursoris dicuntur tria.` stands over ¶ 104.
  - The t3 headings `Secundo, de Christi nascentis humilitate, quatenus factus est sub triplici lege.` (54L),
    `Secundo, de baptismo et praedicatione Ioannis in speciali quoad tria.` (75L) and
    `Tertio, de baptismo et praedicatione Ioannis in singulari quoad duo.` (81R) are each followed by a numbered
    divisio paragraph and then a t4.
  - The text layer misses every one of these t3s.
- ⚠ **The *Prologus S. Hieronymi* is set in ROMAN type on the plate (7L, zoomed), not italic.** Ruling 3 says
  "italic as printed". Wilson should correct the ruling text. This manifest changes nothing on that account.
  The `PROLOGUS SANCTI HIERONYMI` heading carries footnote anchor ².

## Last paragraph per capitulum (MEASURED)

**Cap. I = 144** (43R). **Cap. II = 111** (69R). **Cap. III = 63** (87R). p. 88 above `CAPITULUM IV.` continues
¶ 63 with no new number.

## The p. 88 close (MEASURED)

`CAPITULUM IV.` is full measure, about two-thirds down the body of p. 88. `Pars II. De praedicationis magisterio
agitur dupliciter.` stands **below** it on 88L, with `Primo explicatur veritas doctrinae quadrupliciter.` on 88R.
Both belong to Cap. IV. The running head of p. 88 already reads `C. IV.`

## Rule applications that needed a choice

- **Size rule as applied:** a section over 6 pp is split at a print-marked joint only if both pieces come out at
  ≥ ~2.7 pp. Otherwise it is kept whole up to the cap of 8.
  - **c. 1 vv. 26–38 kept whole at ~7.0 pp (8 printed pp touched).** Both internal t4 joints leave a fragment:
    22L gives 1.9 + 5.1, and 26L gives 5.8 + 1.2.
  - **c. 3 vv. 10–20 split at the 78L t4:** 2.9 + 3.6.
  - **c. 3 vv. 21–38 split at the 85L t4:** 3.3 + 3.3.
  - **c. 1 vv. 39–56 split at the 30R t4:** 3.2 + 4.2.
- **`title_la` rule (RESTATED at the p. 27 gate, ruling 22, Wilson 2026-11-14; *Ioannem* ruling 79(b)):** the
  LOWEST heading of the chunk's opening stack, taken whole, whether or not its scope covers the whole chunk (it may
  overrun, as at `bon-ioan-c1-v43-51`, or under-cover, as at `bon-luc-c1-v18-25`). A sentence title (the divisio
  paragraph's lemma plus its dividing words) only where no heading stands. No stage-1 title changes under the
  restated rule (each row's `title_la` is already the lowest heading of its opening stack). *(Superseded wording, kept for the record: "the most specific heading in the chunk's opening cascade
  whose scope covers the whole chunk. If none covers it, the opening heading itself. If there is no heading, the
  divisio paragraph's lemma plus its dividing words.")*
  - Ruling 4 does not decide between this and "the opening heading". Under the opening-heading reading:
    - c1-v5-17 would be titled `Divisio generalis`;
    - c1-v39-45 would take the t3 *Secundo, de gratiarum actione…*;
    - c2-v1-7, c3-v1-9 and c3-v10-14 would take their t2/t3.
  - This needs a one-word ruling before the build. **Settled by ruling 22 (lowest heading of the opening stack).**
- **Tier labels** are by typography on the plate: small bold = t4, larger roman = t3, italic = t2. `Primo, de
  regeneratione Christi sacramentali duo.` (81R) and `Secundo, de genealogia temporali tria.` (85L) are Tabula
  members but are set in small bold, so they are labelled **t4**.

## `low` rows (2), with the alternatives

**Rows:** `bon-luc-c2-v25-35` (¶¶ 58–80) and `bon-luc-c2-v36-39` (¶¶ 81–90).

**[2026-11-14, `bon-luc-c2-v25-35`'s builder: pp. 58–62 read on the plates; ¶ 80 closes at 62L's foot, ¶ 81 opens at the head of 62R with no heading (ruling 26's cut confirmed). `bon-luc-c2-v25-35` promoted to `high`; `bon-luc-c2-v36-39` stays `low` until its builder reads pp. 62–65.]**

**[2026-11-14, `bon-luc-c2-v36-39`'s builder: pp. 62–65 read on the plates; ¶ 81 opens at the head of 62R with no heading, ¶ 90 closes at ~0.42 of 65L directly above the t4 *Qualiter Christus factus sit sub lege morali.* (¶ 91 below it). Both ends as drawn; `bon-luc-c2-v36-39` promoted to `high` (confidence cell only; no span change).]**

**Why a divisio cut is needed here:**

- The editors print no in-column heading between 56L (*sub lege caeremoniali*) and 65L (*sub lege morali*). That
  gap is 9 pp, so ruling 1b licenses divisio-paragraph cuts.
- Here they put the divisions in the margin instead: *Secundo, de Christi clarificatione per duplex testimonium*;
  *De testimonio Simeonis dicuntur tria*; *Tertio, de praeconii temperamento tria*; *De testimonio Annae*.
- The cut at ¶ 58 is firm. ¶ 50's own division names it, and ending at the 56L heading instead would leave a
  1.6 pp chunk.

**Chosen:** cut at **¶ 81** (Anna, 62R top), the higher-order joint, giving 4.4 + 2.7 pp.

**Alternatives:**

- (a) No cut: ¶¶ 58–90 as one chunk of ~7.1 pp, under the cap.
- (b) Cut at ¶ 75 (61L, *Et benedixit illis Simeon etc. Post…*), giving 3.0 + 4.1 pp. The sizes are more even, but
  the joint is lower-order.

## Things the rule did not cover

- `bon-luc-c1-v1-4` is **~1.7 pp, under 2.** Ruling 3 (the p. 11 stack) and `DIVISIO GENERALIS` fix both of its
  ends, so it stands as ruled.
- The 51L small-type hymn couplet (*Gloria tibi, Domine, / Qui natus es de Virgine!*) and the 43R hymn are verse
  set in the column, **not headings**.
- `PROLOGUS SANCTI HIERONYMI²` and `DIVISIO GENERALIS⁸` carry footnote anchors. The setup's "no anchored heading"
  expectation does not hold in this work.

## Tabula references (MEASURED in the body; the Tabula itself was not re-read)

- **"c. 1, 30" for *de gratiarum actione* is a misprint for c. 1, 39.** The Tabula's numbers are verses (cf.
  "c. 1, 5" and "c. 1, 26"). The t3 heading stands over ¶ 71, whose lemma *Exsurgens autem Maria* is v. 39, and
  ¶ 72 is tagged Vers. 39. "30" is a paragraph number on a different page (¶ 30 is on p. 17).
- **"pro conceptu Praecursoris (c. 1, 56)" also misses by one.** The heading (34R) and ¶ 104 open on v. 57
  (*Elisabeth impletum est tempus*), and ¶ 71's own division and its note 7 both give v. 57.
- c. 3, 10 / 21 / 23 match the body exactly.

## Corrigenda (assigned by page; none of pp. 9, 16, 22, 23 is a boundary page)

- **p. 9 → `bon-luc-prol`.**
- **p. 16 → `bon-luc-c1-v5-17`.**
- **pp. 22 and 23 → `bon-luc-c1-v26-38`.** The col. 1 l. 14 site on p. 22 is above the unused 22L joint in any
  case.
- The line positions themselves were NOT read on the plate. The builder fixes each one.

## Size distribution (22 rows)

- **Printed pages touched (`pages` column):** min 2 / mean 4.9 / max 8.
- **Estimated text extent** (column fractions from text-layer line positions, PREDICTION): min 1.7 / mean 3.9 /
  max 7.0 pp.

## Not verified

- **Paragraph numbers inside chunks** (e.g. ¶ 118 as the last of c1-v57-66, ¶ 16, ¶ 43, ¶ 56) are inferred from
  the plate-read number of the next chunk.
- **The `headings` column off boundary pages** is text-layer only (PREDICTION). It is a floor: undetected t4s may
  exist, most likely in c. 1 vv. 57–80 and c. 2 vv. 40–52. Builders count on the plate.
- **Verse ends** with no `(Vers. N.)` tag (c. 1 v. 38, c. 3 v. 9, v. 22, v. 38) are taken from the lemma
  sequence.
- **The ~N pp extents** are estimates.

---

# Stage 2 notes (Cap. IV–VII, pp. 88–188; 2026-11-14, Opus)

19 rows appended to `lucam-chunk-manifest.tsv` (IV 5 · V 4 · VI 6 · VII 4). Labels as in stage 1: **MEASURED**
(read on a 300 dpi plate crop this session) or **PREDICTION** (text layer only). No chunk was built.

## Plates read (MEASURED)

Plates pp. 89–188 extracted at 300 dpi (`raw/vision/vol7/p-089 … p-188.png`). Two screens found the headings,
because the text layer misses the larger-roman tier (t3) and garbles the small-bold one:

- a **plate screen** over every page 88–188: each column's text lines segmented from the image, and every line
  indented equally on both sides (a centred line) flagged. Checked first against stage 1's known headings on pp.
  54, 56, 65, 75, 78, 81 (all caught; p. 62, which has none, gave none);
- the **text layer's** small-type lines in the body zone.

Every flagged line, and every row boundary, was then read on a crop: pp. **88** (full), **89L**, **89R**, **91R**,
**95L**, **95R**, **98L**, **98R**, **100L**, **104L**, **104R**, **107R**, **112** (full), **114L**, **119L**, **123R**,
**128R**, **134** (full), **140R** (top to ¶ 25), **147R**, **153L**, **156L**, **159R**, **160R**, **162L**, **165**
(full), **168R**, **170L**, **173L**, **177L**, **182L**, **188** (full), **188R**. The flagged lines that were not
headings were footnote lines (89R, 91R, 98L), paragraph indents (98R, 168R), a full-measure line (159R) and a
centred verse (162L, *Turpe est doctori, dum culpa redarguit ipsum*).

## Headings found in pp. 88–188 (MEASURED; wording from the plate)

| Page | Tier (typography) | Wording | Row |
|---|---|---|---|
| 88 | capitulum | CAPITULUM IV. | c4-v1-13 |
| 88L | t1 (large roman) | Pars II. De praedicationis magisterio agitur dupliciter. | c4-v1-13 |
| 88R | t2 (italic) | *Primo explicatur veritas doctrinae quadrupliciter.* | c4-v1-13 |
| 89L | t4 (small bold) | Authenticatur doctrina Christi ex merito vitae. | c4-v1-13 |
| 95R | t4 | Authenticatur doctrina Christi ex testimonio Scripturae. | c4-v14-22 |
| 95R | t4 | Primo testimonium Scripturae affertur ad eruditionem credentium. | c4-v14-22 |
| 100L | t4 | Secundo affertur testimonium Scripturae ad confutationem detrahentium. | c4-v22-30 |
| 104R | t4 | Authenticatur doctrina Christi ex miraculo potentiae. | c4-v31-37 |
| 112 | capitulum | CAPITULUM V. | c5-v1-11 |
| 112L | t3 (larger roman) | Secundo determinatur discipulorum vocatio per duo. | c5-v1-11 |
| 112R | t4 | Primo, quomodo vocentur discipuli de statu iustitiae. | c5-v1-11 |
| 128R | t4 | Secundo, quomodo vocentur discipuli de statu culpae. | c5-v27-39 |
| 134 | capitulum | CAPITULUM VI. (nothing below it: ¶ 1 follows directly) | c6-v1-11 |
| 140R | t3 (larger roman) | Tertio determinatur vocatorum instructio per duo. | c6-v12-19 |
| 140R | t4 | In prima parte Apostoli instruuntur in veritate explicata et praeceptis apertis. | c6-v12-19 |
| 140R | t4 | Primo exprimitur veritas doctrinae tripliciter. | c6-v12-19 |
| 165 | capitulum | CAPITULUM VII. | c7-v1-16 |
| 165L | t4 | Secundo declaratur sublimitas in Doctore tripliciter. | c7-v1-16 |
| 165R | t4 | Primo propter excellentiam potestatis probatam per duo miracula. | c7-v1-16 |
| 173L | t4 | Secundo, declaratur sublimitas Doctoris propter evidentiam veritatis per testimonium Praecursoris. | c7-v17-23 |
| 182L | t4 | Tertio declaratur sublimitas Doctoris propter affluentiam pietatis tripliciter. | c7-v36-50 |
| 188 | capitulum + t4 + t4 | CAPITULUM VIII. / In secunda parte Apostoli instruuntur specialiter in doctrina mystica Scripturarum. / Primo ponitur instructio parabolica in occultis mysteriis per tria. | (c. 8) |

Tier labels are by typography, as in stage 1. Several Tabula members are set in small bold (89L, 95R, 104R), so
they are labelled **t4**. Two members are in the larger roman (112L, 140R), so they are labelled **t3**. The
headings stand far apart:

- **c. 5:** 112R to 128R is ~16 pp.
- **c. 6:** 140R to 165 is ~25 pp, and the editors put the members in the margin (as at c. 2 vv. 25–39).

Rows in those stretches are cut at Bonaventure's divisio paragraphs (ruling 1b). Every one of them is named in a
higher paragraph's own *ibi:* list.

## Last paragraph per capitulum (MEASURED)

**IV = 98** (112R). **V = 85** (134L). **VI = 111** (165R; ⚠ the setup table says **109**: wrong). **VII = 84**
(188R, Vers. 50). Each capitulum's first and last pages are as the setup table predicts (88–112, 112–134, 134–165,
165–188). **No capitulum overran.**

## Corrections to the scouting sheet and setup table (MEASURED)

- **Cap. VI last ¶ = 111, not 109.** ¶ 111 is *Subiungit postremo negligentis praecipitium*, ending in the
  marginal *Epilogus*.
- **Cap. V is 4 chunks, not the scouting sheet's 5.** Its demonstration split *de statu culpae* at ¶ 75 (vv.
  27–29 / 30–39). That cut is unlicensed: the 128R heading and `CAPITULUM VI.` stand ~5.9 pp apart, under 8. So
  ¶¶ 63–85 is one row.
- The other scouting cuts in c. 5 hold, at the plate: ¶ 24 (119L) and ¶ 40 (123R), divisio paragraphs with no
  heading, marginalia only.
- **CAPITULUM VI. has no heading under it.** The opening stack is the capitulum alone, so `bon-luc-c6-v1-11`
  takes a sentence title (see "Needs a look").
- **The 140R t3 *Tertio determinatur vocatorum instructio per duo.* stands ABOVE ¶ 24.** The text layer misses
  it. So `bon-luc-c6-v12-19` opens on a heading, not on a bare divisio.
- **c. 7 verse joint:** ¶ 33's lemma *Et exiit hic sermo* is **v. 17**. So the c. 7 rows are vv. 1–16 / 17–23,
  not 1–17.
- **c. 4 v. 22 is shared** by `c4-v14-22` and `c4-v22-30`: ¶ 46 and ¶ 48 are both tagged (Vers. 22.).

## `low` rows (5), with the alternatives

1. **`bon-luc-c4-v31-37` and `bon-luc-c4-v38-44` (¶¶ 64–78 / 79–98).**
   - **The problem:** the *ex miraculo potentiae* member runs from 104R to `CAPITULUM V.`, ~8.1 pp. That is over
     cap 8, and the heading gap is over ~8, so a divisio cut is licensed. ¶ 64's own three-part division leaves
     fragments at both of its joints (¶ 69 after 1.2 pp; ¶ 92 with 1.8 pp left).
   - **Chosen:** ¶ 79 (*Post miraculosam curationem sexus virilis … sexus muliebris*; cf. ruling 26's Anna
     cut), giving 3.3 + 4.8 pp.
   - **Alternatives:** (a) ¶ 87 (*Cum autem sol occidisset*, the universal cure, 109R), giving 5.0 + 3.1 pp;
     (b) no cut, one pass at ~8.1 pp.
2. **`bon-luc-c5-v1-11` (¶¶ 1–23, ~6.4 pp).**
   - **Kept whole.** ¶ 1's three-part division offers ¶ 9 (*Ut cessavit autem loqui*, 115L), which gives ~2.7 +
     3.7 pp. That sits on the edge of stage 1's ≥ 2.7 test. The other joint, ¶ 18, would leave 1.6 pp.
   - **Alternative:** cut at ¶ 9.
3. **`bon-luc-c6-v27-31` and `bon-luc-c6-v32-38` (¶¶ 64–76 / 77–91).**
   - **The problem:** the *leges praeceptorum* member is ~7.5 pp.
   - **Chosen:** ¶ 77 (*hic secundo probat ex conditione deficiente*, 156L), giving 3.3 + 4.2 pp.
   - **Alternatives:** (a) no cut, ~7.5 pp; (b) ¶ 82 or ¶ 86, less even.
4. **`bon-luc-c7-v1-16` (¶¶ 1–32, ~7.6 pp over 9 printed pp).**
   - **Kept whole.** The two miracles split cleanly at ¶ 20 (170L foot, marginale *Secundo, de suscitatione
     mortui tria*), giving ~4.8 + 2.7 pp. But the 165 and 173L headings stand only ~7.6 pp apart, under ruling
     1b's ~8, so no divisio cut is licensed.
   - **Alternative:** cut at ¶ 20 (`c7-v1-10` + `c7-v11-16`).
   - ⚠ This is the one row touching 9 printed pages. Wilson may prefer the cut.

## Rule applications that needed a choice (not `low`)

- **`c4-v1-13` (~7.1 pp) and `c6-v12-19` (~7.1 pp) are kept whole.**
  - In c. 4, no divisio cut is licensed (the 89L to 95R headings stand ~6.5 pp apart), and ¶ 8 would leave 2.0 pp.
  - In c. 6, the attractio auditorum joint (¶ 41) leaves 2.1 pp.
- **`c5-v27-39` (~5.9), `c6-v1-11` (~5.9) and `c7-v36-50` (~6.3) have no licensed internal cut.** Each heading
  gap is under 8 pp.
- **`c7-v17-23` / `c7-v24-35`:** the 173L member is ~9.1 pp, so it must be cut. ¶ 47 is the top-order joint of
  ¶ 33's own division.

## Needs a look (title rule)

**`bon-luc-c6-v1-11`'s `title_la`.** Ruling 22 says "lowest heading of the opening stack", but under `CAPITULUM
VI.` no heading stands. The row takes ¶ 1's lemma plus its dividing words, as at `c2-v25-35`. If Wilson reads the
capitulum itself as the stack, the title would be `Capitulum VI.` One word decides it.

## Corrigenda (assigned by page and column; line positions NOT read on the plate)

- **p. 95 col. 1 penult.** → `bon-luc-c4-v1-13`. p. 95 is a boundary page, but col. 1 lies wholly before the
  95R opening of `c4-v14-22`.
- **p. 114 col. 2 notes l. 2** → `bon-luc-c5-v1-11`.
- **p. 168 col. 1 l. 4 from foot** → `bon-luc-c7-v1-16`. It stays in the same row if Wilson takes the ¶ 20 cut:
  ¶ 20 opens at 170L.

## Size distribution (19 rows)

- **Printed pages touched:** min 4 / mean 6.2 / max 9.
- **Estimated text extent** (column fractions from text-layer positions; capitulum breaks placed from the
  plates; PREDICTION): min 3.3 / mean 5.3 / max 7.6 pp.

## Not verified

- **Paragraph numbers inside rows** come from the text layer. Each is anchored by plate-read numbers at both ends.
- **Verse ends** are taken from the `(Vers. N.)` tags and the lemma of the next row's first paragraph.

---

# Stage 3 notes (Cap. VIII–XI v. 13, pp. 188–288; 2026-11-15, Opus)

22 rows appended to `lucam-chunk-manifest.tsv` (VIII 7 · IX 8 · X 5 · XI 2), drawn after the p. 188 interval was
built and before any Cap. VIII chunk (ruling 2). Labels as in stages 1–2: **MEASURED** (read on a 300 dpi plate crop
this session) or **PREDICTION** (text layer only). No chunk was built.

## Plates read (MEASURED)

Plates pp. 189–290 extracted at 300 dpi (`raw/vision/vol7/p-189 … p-290.png`; p. 188 was already on disk). Three
screens found the headings, and every hit was read on a crop:

- a **divisio sweep**: the region above every lemma paragraph (*Lemma etc. Post… / Hic…*) in pp. 188–288, ~60
  paragraphs, read on the plate. This is where every heading in stages 1–2 stood;
- a **vertical-gap screen**: each column's inner 76 % profiled for blank bands ≥ 38 px in the body zone. A heading
  leaves a gap above and below itself; the footnote rule leaves a synchronised pair in both columns and was set aside.
  The 19 single, column-specific gaps it raised were read (pp. 192L, 194L, 202L, 219L, 220L, 224R, 230L, 232L, 235L ×2,
  250L, 255L, 257L, 258L, 269L, 275L, 287L, 204R): every one is a short closing line, none a heading;
- the **text layer's** small-type lines in the body zone (as in stage 2). It missed 216R, 272L and one of the two
  266L headings, so it was used as a cross-check only.

Full-page or full-width crops: pp. **188**, **216**, **252**, **277**, **288**. Boundary and heading crops: **190R**,
**192L**, **193R**, **195R**, **196R**, **197L**, **197R**, **198R**, **199L**, **200L**, **201R**, **204L**, **205R**,
**207L**, **208R** (×2), **210L**, **211R**, **213L**, **214L**, **215R**, **216L**, **219R**, **220R**, **221L**,
**222L**, **223L**, **225L**, **227R**, **230L**, **233L**, **234R**, **237L**, **238L**, **239L**, **241L**, **242L**,
**243L**, **245L**, **246L**, **248R**, **250L**, **251L**, **251R**, **254R**, **257L**, **258L**, **259R**, **261L**
(×2), **263L**, **266L**, **269L**, **269R**, **270L**, **272L**, **274L**, **278L**, **282R** (×2), **284R**, **286L**,
**287R**. Every row's opening, ending and `title_la` was read on one of these.

## Headings found in pp. 188–288 (MEASURED; wording from the plate)

| Page | Tier (typography) | Wording | Row |
|---|---|---|---|
| 188 | capitulum | CAPITULUM VIII. | c8-v1-10 |
| 188L | t4 (small bold) | In secunda parte Apostoli instruuntur specialiter in doctrina mystica Scripturarum. | c8-v1-10 |
| 188R | t4 | Primo ponitur instructio parabolica in occultis mysteriis per tria. | c8-v1-10 |
| 193R | t4 | Secundo ponitur informatio apostolica in apertis eloquiis per duo. | c8-v11-21 |
| 198R | t4 | Tertio ponitur confirmatio authentica in manifestis miraculis. | c8-v22-25 |
| 216 | capitulum | CAPITULUM IX. | c9-v1-9 |
| 216L | t3 (larger roman, hanging indent) | Quarto determinatur instructorum discipulorum delegatio, primo quoad Apostolos, deinde quoad septuaginta. | c9-v1-9 |
| 216R | t4 | Primo agitur de missione Apostolorum quoad tria. | c9-v1-9 |
| 216R | t4 | Forma praedicandi dupliciter explicatur. | c9-v1-9 |
| 225L | t4 | Via proficiendi dupliciter explicatur. | c9-v18-27 |
| 243L | t4 | Norma praesidendi tripliciter explicatur. | c9-v46-56 |
| 252 | capitulum | CAPITULUM X. | c10-v1-3 |
| 252L | t4 | Secundo agitur de missione septuaginta duorum discipulorum quoad tria. | c10-v1-3 |
| 252L | t4 | Prima pars agit de missione discipulorum comitantium tripliciter. (as printed; see Corrigenda) | c10-v1-3 |
| 266L | t4 | Secunda pars agit de data discipulis forma vivendi dupliciter. | c10-v25-37 |
| 266L | t4 | Ad informationem praemittitur divinum praeceptum dupliciter propositum. | c10-v25-37 |
| 272L | t4 | Ad informationem discipulorum subiungitur humanum exemplum dupliciter propositum. | c10-v38-42 |
| 277 | capitulum | CAPITULUM XI. | c11-v1-4 |
| 277L | t4 | Tertia pars agit de forma orandi tripliciter. | c11-v1-4 |
| 288L | t2 (italic) | *Secundo confutatur falsitas Iudaeorum adversantium quadrupliciter.* | (next interval) |
| 288R | t3 (larger roman) | Dolositas Iudaeorum calumniantium miracula confutatur dupliciter. | (next interval) |
| 288R | t4 | Primo confutantur Iudaei calumniantes miracula ex parte causae efficientis, deinde discipuli informantur. | (next interval) |
| 288R | t4 | Primo, de Iudaeorum dolositate et triplici fallacia. | (next interval) |
| 288R | t4 | Confutatur fallacia blasphemantium per tria. | (next interval) |

Tier labels are by typography, as in stages 1–2. The 216L delegatio member is set like 112L and 140R (larger roman), so
it is labelled **t3**; it is the fourth of the Tabula's four members of *Primo explicatur veritas doctrinae
quadrupliciter* (88R). The headings stand far apart:

- **c. 8:** 198R to `CAPITULUM IX.` is ~17.8 pp; the editors put the three miracles in the margin.
- **c. 9:** 225L to 243L is ~18.2 pp; 216 to 225L ~8.5 pp; 243L to `CAPITULUM X.` ~8.9 pp.
- **c. 10:** 252 to 266L is ~13.9 pp.
- **c. 11:** 277 to the 288 stack is ~11.0 pp.

Rows in those stretches are cut at Bonaventure's divisio paragraphs (ruling 1b). Every cut is named in a higher
paragraph's own *ibi:* list, or (¶ 87) names the joint itself in its opening sentence.

## Last paragraph per capitulum (MEASURED)

**VIII = 99** (216R; ⚠ the setup table says **98**: wrong). **IX = 111** (251R; its text runs unnumbered across the top
of p. 252; the setup table's ~110–111 resolves to 111). **X = 80** (277R; ⚠ the setup table says **~79**). Each
capitulum's first and last pages are as the setup table predicts (188–216, 216–252, 252–277). **None overran.**

## The p. 288 gate (MEASURED)

Ruling 14 places the gate at **c. 11 v. 13**, p. 288. On the plate: ¶ 34 is Vers. 13 (287R); ¶ 35 (*Et ideo concludit:
Quanto magis Pater de caelo dabit spiritum bonum petentibus se?*) closes v. 13 on 288L; **¶ 36 (*Et erat Iesus eiiciens
daemonium etc.*, the v. 14 lemma) opens at ~0.41 of 288L**. The last row, `bon-luc-c11-v5-13`, ends there. ⚠ The
heading stack that opens Pars II's second member does NOT stand above ¶ 36: ¶ 36's first eleven lines (*Sicut habitum fuit
in principio libri…*) come first, then the italic t2 *Secundo confutatur falsitas Iudaeorum adversantium
quadrupliciter.* (288L ~0.6), the un-numbered *Prima parte terminata…*, and on 288R the t3 and three t4s, then ¶ 37
(Vers. 14). Under ruling 1d the next interval's first chunk opens at **¶ 36**, and its opening stack is the t2 / t3 / t4
cascade inside ¶ 36 (the c4-v1-13 shape). The gate placement is right; only its exact line differs from "above the
heading".

## Corrections to the setup table (MEASURED)

- **Cap. VIII last ¶ = 99, not 98.** ¶ 99 is the un-versed *Secundo vero quantum ad humilem occultationem*.
- **Cap. X last ¶ = 80, not ~79.** ¶ 80 is *Et sic patet, quomodo istud Evangelium…*, on 277R above `CAPITULUM XI.`
- **The 216L delegatio heading is a t3 (larger roman)**, not a small-bold t4.

## `low` rows (8, four decisions), with the alternatives

1. **`bon-luc-c8-v26-33` and `bon-luc-c8-v34-39` (¶¶ 46–59 / 60–71).**
   - **The problem:** the second miracle (the legion) is ~7.0 pp: under cap 8, over the 3–6 target. The heading gap
     (~17.8 pp) licenses a cut. ¶ 46 divides it four ways, each named.
   - **Chosen:** ¶ 60 (*Quod ut viderunt factum*, 205R), the middle joint, giving 3.9 + 3.1 pp.
   - **Alternatives:** (a) no cut, one row ~7.0 pp (`c8-v26-39`); (b) ¶ 55 (2.5 + 4.5) or ¶ 65 (5.6 + 1.4).
2. **`bon-luc-c8-v40-48` and `bon-luc-c8-v49-56` (¶¶ 72–86 / 87–99).**
   - **The problem:** the third miracle (the woman and Jairus's daughter) is ~7.7 pp, under cap 8.
   - **Chosen:** ¶ 87 (*Adhuc illo loquente*, 213L), the joint of ¶ 72's two-part division (the body / the soul), giving
     4.5 + 3.2 pp.
   - **Alternative:** no cut, one row ~7.7 pp (`c8-v40-56`).
3. **`bon-luc-c9-v46-56` and `bon-luc-c9-v57-62` (¶¶ 85–101 / 102–111).**
   - **The problem:** 243L to `CAPITULUM X.` is ~8.9 pp, so a cut is required; ¶ 85 offers two named joints, and taking
     both would leave a 2.5 pp middle.
   - **Chosen:** ¶ 102 (*Factum est autem, ambulantibus*, 248R), giving 5.6 + 3.3 pp.
   - **Alternative:** ¶ 94 (*Factum est autem, dum complerentur*, 246L), giving 3.1 + 5.8 pp (`c9-v46-50` + `c9-v51-62`).
4. **`bon-luc-c10-v1-3` and `bon-luc-c10-v4-16` (¶¶ 1–6 / 7–27).**
   - **The problem:** the forma praedicandi (252 to 266L, ~13.9 pp) has three named members of ~2.7, 6.4 and 4.8 pp.
     The first two together are ~9.1 pp.
   - **Chosen:** both named joints, ¶ 7 (*Nolite portare*, 254R) and ¶ 28 (*Reversi sunt*, 261L). `c10-v1-3` is the
     stage's shortest row (~2.7 pp, 3 printed pp, the edge of the ≥ 2.7 test) and `c10-v4-16` its longest in printed
     pages (8).
   - **Alternatives:** (a) cut at ¶ 14 (*Et in quamcumque civitatem*, 257L, the informatio specialis, named in ¶ 7's own
     division) instead of ¶ 7, giving ¶¶ 1–13 ~4.8 + ¶¶ 14–27 ~4.3; (b) no cut at ¶ 7, ¶¶ 1–27 ~9.1 pp (one-pass to 10).

## Rule applications that needed a choice (not `low`)

- **Required cuts at a single named joint** (heading gap over ~8 pp, and the member over cap 8):
  - **c. 9 ¶ 15** (216 to 225L ~8.5 pp; *divino praecepto / divino exemplo*, named in the 216R divisio), 4.5 + 4.0 pp.
    ⚠ ~8.5 pp sits close to ruling 1b's ~8; if Wilson reads it as under, the row would be one ~8.5 pp chunk over cap.
  - **c. 9 ¶¶ 43, 56, 70** (225L to 243L ~18.2 pp): ¶ 29's two-part division, then ¶ 43's three named parts.
  - **c. 11 ¶ 18** (277 to ¶ 36 ~11.0 pp): ¶ 1's third member; its second joint (¶ 4) would leave 1.1 pp.
  - **c. 8 ¶¶ 46, 72** (198R to `CAPITULUM IX.` ~17.8 pp): ¶ 34's three named miracles.
- **Kept whole, no licensed cut** (heading gap under ~8 pp): `c8-v1-10` (~5.0), `c8-v11-21` (~4.9), `c10-v25-37` (~6.3),
  `c10-v38-42` (~5.0).
- **Kept whole, licensed but the sub-joint leaves a fragment:** `c9-v18-27` (¶ 37 would leave 2.1 pp), `c10-v17-24`
  (¶ 34, 2.1 + 2.7).

## Titles (ruling 22 / 33 / 40)

- Where an opening stack holds several headings, `title_la` is the lowest, whole: `c8-v1-10` (188R t4, not the 188L
  t4), `c9-v1-9` (*Forma praedicandi dupliciter explicatur.*, not the 216L t3 or the first 216R t4), `c10-v1-3` (the
  second 252L t4), `c10-v25-37` (the second 266L t4).
- **`c10-v1-3` takes the Corrigenda's reformed rubric** (ruling 4: "the governing rubric as amended by the
  Corrigenda"). p. 858: *Prima pars* etc., "sic reformanda est": *Prima pars, quae agit de forma praedicandi, tractat de
  missione comitantium discipulorum, de informatione euntium, de consolatione redeuntium.* The printed rubric (*Prima
  pars agit de missione discipulorum comitantium tripliciter.*) is the one the builder transcribes in place, with ruling
  8's note. ⚠ The reformed rubric names all three members, so its scope runs past this ~2.7 pp row to ¶ 42; ruling 22
  takes it whole all the same.
- Twelve rows open on a divisio paragraph with no heading and take a sentence title (lemma + the dividing words,
  through the sentence that names the member), read on the plate, footnote anchors dropped, as stage 2.
- **No row opens on a bare `CAPITULUM`** (ruling 40 is not engaged): a heading stands under each of VIII–XI.

## Corrigenda (assigned by page and column; positions as the Corrigenda gives them)

- **p. 252 col. 1, the second rubric** → `bon-luc-c10-v1-3` (the rubric stands in its opening stack). No other
  Corrigenda entry falls in pp. 188–288.

## Size distribution (22 rows)

- **Printed pages touched:** min 3 / mean 5.5 / max 8.
- **Estimated text extent** (column fractions from text-layer paragraph positions against plate-measured body ends;
  capitulum breaks placed from the plates; PREDICTION): min 2.7 / mean 4.5 / max 6.4 pp.

## Not verified

- **Paragraph numbers inside rows** come from the text layer. Each is anchored by plate-read numbers at both ends.
- **Verse ends** are taken from the `(Vers. N.)` tags and the lemma of the next row's first paragraph. ¶ 26 of c. 10
  (v. 16) is not legible in the text layer; `c10-v4-16`'s end verse rests on ¶ 25 (Vers. 15) and ¶ 28's lemma (v. 17).

# Stage 4 notes (Cap. XI v. 14 – Cap. XIV, pp. 288–381; 2026-11-15, Opus)

19 rows appended to `lucam-chunk-manifest.tsv` (XI 4 · XII 5 · XIII 5 · XIV 5), drawn at the p. 288 gate and before
any chunk of the next interval (ruling 2). Labels as in stages 1–3: **MEASURED** (read on a 300 dpi plate crop this
session) or **PREDICTION** (text layer only). No chunk was built.

## Plates read (MEASURED)

Plates pp. 291–382 extracted at 300 dpi (`raw/vision/vol7/p-291 … p-382.png`; pp. 288–290 were on disk). Three screens
found the headings, and every hit was read on a crop:

- a **vertical-gap screen**: each column's inner 76 % profiled for blank bands ≥ 38 px in the body zone, the
  synchronised footer-rule pair set aside. Column-specific pairs (a heading leaves a gap above and below itself) stood
  at 288L/R, 298L, 300L, 309L, 310L ×2, 311R, 313R, 315L, 316L ×2, 324L ×2, 330R, 336R, 341R ×2, 358L/R, 362L, 375L,
  381: **every one a heading or a capitulum**. Single gaps at 289R, 301R, 304L, 307R, 312R, 315R, 321R, 325R, 327L,
  338R, 347R, 366L, 374R, 378R were read: short closing lines, a centred verse list (304L), or the footer zone of
  leaves whose body ends high. **None is a heading.**
- a **divisio sweep**: the paragraphs that open on a lemma + *Post… / Postquam… / Supra… / Hic…* (~35 in pp. 288–381),
  read on the plate wherever one is a boundary or a named joint;
- the **text layer's** small-type lines in the body zone. It found every heading except the 288R t3 and the 341R
  second t4, and was a cross-check only.

Full-width crops: pp. **309**, **336**, **358**, **381**. Boundary and heading crops: **288L**, **288R** (×2), **290L**,
**290R** (×2), **295R**, **297R**, **298L**, **300L**, **300R**, **302L**, **304R**, **309L**, **309R**, **310L**,
**311R**, **313L**, **313R**, **315L**, **316L** (×2), **316R**, **324L**, **327L**, **330R**, **335R**, **338R**,
**341R** (×2), **342L**, **346L**, **347R**, **350L**, **354L** (×2), **361R**, **362L**, **366L**, **370L**, **375L**.
Every row's opening, ending and `title_la` was read on one of these.

## Headings found in pp. 288–381 (MEASURED; wording from the plate)

| Page | Tier (typography) | Wording | Row |
|---|---|---|---|
| 288L | t2 (italic) | *Secundo confutatur falsitas Iudaeorum adversantium quadrupliciter.* | c11-v14-26 (inside ¶ 36) |
| 288R | t3 (larger roman) | Dolositas Iudaeorum calumniantium miracula confutatur dupliciter. | c11-v14-26 |
| 288R | t4 (small bold) | Primo confutantur Iudaei calumniantes miracula ex parte causae efficientis, deinde discipuli informantur. | c11-v14-26 |
| 288R | t4 | Primo, de Iudaeorum dolositate et triplici fallacia. | c11-v14-26 |
| 288R | t4 | Confutatur fallacia blasphemantium per tria. | c11-v14-26 |
| 298L | t4 | Confutatur fallacia tentantium sive incredulorum triplici via. | c11-v27-32 (interior) |
| 300L | t4 | Confutatur fallacia simulantium per duo. | c11-v33-41 |
| 309 | capitulum | CAPITULUM XII. | c12-v1-7 |
| 309L | t4 | Secundo informat ad fallaciam confutatam vitandam duplici modo. | c12-v1-7 |
| 310L | t4 | Primo ad cavendam duplicitatem venientem ex timiditate monet quadrupliciter. | c12-v1-7 |
| 310L | t4 | Informatio duplex ad cavendam dolositatem. | c12-v1-7 |
| 311R | t4 | Informatio ad repellendam timiditatem per duo. | c12-v1-7 (interior) |
| 313R | t4 | Informatio duplex ad servandam veracitatem. | c12-v8-12 |
| 315L | t4 | Informatio duplex ad securitatem contra pusillanimitatem. | c12-v8-12 (interior) |
| 316L | t4 | Secundo ad cavendam cupiditatem venientem ex timiditate monet dupliciter. | c12-v13-34 |
| 316L | t4 | A sollicitudine avaritiae revocatur quadrupliciter. | c12-v13-34 |
| 324L | t4 | Ad sollicitudinem providentiae invitatur dupliciter. | c12-v35-48 |
| 324L | t4 | Primo invitatur consideratione secundi adventus. | c12-v35-48 |
| 330R | t4 | Secundo invitatur ad vigilantiam consideratione primi adventus. | c12-v49-59 |
| 336 | capitulum | CAPITULUM XIII. (no heading beneath it) | c13-v1-9 |
| 341R | t4 | Secundo confutantur calumniantes miracula ex parte circumstantiae temporis secundum duplicem opportunitatem. | c13-v10-17 |
| 341R | t4 | Confutatio, quae fit in concilio, de qua duo. | c13-v10-17 |
| 358 | capitulum | CAPITULUM XIV. | c14-v1-6 |
| 358L | t4 | Confutatio calumniantium miracula, quae fit in convivio, de qua tria. | c14-v1-6 |
| 358L | t4 | Primo confutantur Pharisaei observantes, de quo tria. | c14-v1-6 |
| 362L | t4 | Secundo informantur convivantes quoad tria. | c14-v7-11 |
| 375L | t4 | Tertio erudiuntur turbae subsequentes, de quo duo. | c14-v25-35 |
| 381 | capitulum | CAPITULUM XV. + t4 *Impietas Iudaeorum confutatur tripliciter.* | (next interval) |

The headings stand far apart in two stretches, and those rows are cut at Bonaventure's divisio paragraphs (ruling 1b):

- **c. 11:** the 288R t4 to the 298L t4 is ~9.7 pp; the 300L t4 to `CAPITULUM XII.` ~9.6 pp.
- **c. 13:** the 341R t4 to `CAPITULUM XIV.` is ~16.6 pp; `CAPITULUM XIII.` stands with no heading under it.
- **c. 14:** the 362L t4 to the 375L t4 is ~13.1 pp.

Every cut is named in a higher paragraph's own *ibi:* list.

## Last paragraph per capitulum (MEASURED)

**XI = 102** (309R, Vers. 54; the setup table's 102 is right). **XII = 88** (335R, the un-versed epilogue, marginale
*Epilogus*, whose text runs unnumbered across the top of p. 336; the setup table's ~87–88 resolves to 88).
**XIII = 76** (358L, un-versed *Et nota, quod, secundum quod exponit Glossa…*; ⚠ the setup table says **~73–74**: wrong).
**XIV = 69** (381R, un-versed, closing v. 35; ⚠ the setup table says **68**: wrong, ¶ 68 is Vers. 35). Each
capitulum's first and last pages are as the setup table predicts (277–309, 309–336, 336–358, 358–381). **None overran.**

## The p. 381 gate (MEASURED)

Ruling 14 places the gate at the **close of c. 14**, p. 381. On the plate: ¶ 68 is Vers. 35 (381L); ¶ 69 (*Tertio quantum
ad spiritualem intelligentiam utriusque subiungit: Qui habet aures audiendi audiat…*) ends 381R at ~0.52 of the leaf; then
`CAPITULUM XV.` full measure at ~0.55, the t4 *Impietas Iudaeorum confutatur tripliciter.* and ¶ 1 *Erant autem
appropinquantes etc.* (the next interval's; it opens the 288L divisio's second part, *impietas*). **The last row,
`bon-luc-c14-v25-35`, ends exactly there.** p. 381's running head already reads *C. XV.* above Cap. XIV's close (the
p. 277 / p. 309 habit).

## The p. 288 opening (MEASURED; as the stage-3 notes and the resume describe)

¶ 35 closes v. 13 at ~0.37 of 288L; ¶ 36 *Et erat Iesus⁴ eiiciens daemonium etc. Sicut habitum fuit in principio libri…*
opens at ~0.41 and runs eleven lines before the italic t2. The t2 / t3 / three t4s stand INSIDE ¶ 36 (ruling 1d), so
`c11-v14-26` opens at ¶ 36 and its `title_la` is the lowest heading of that stack (ruling 22), the third 288R t4.
`opens_on` is recorded as `divisio-para` because ¶ 36's head stands above the stack.

## Corrections to the setup table and the record (MEASURED)

- **Cap. XIII last ¶ = 76, not ~73–74.** **Cap. XIV last ¶ = 69, not 68.**
- **The blasphemantium member's second joint is ¶ 43, not ¶ 41** (a text-layer reading would take ¶ 41, which is the
  expositio's Vers. 16, *Tertio vero quantum ad controversiam litis adiunctae*; ¶ 42 is an *expositio spiritualis*;
  ¶ 43 *Ipse autem, ut vidit cogitationes eorum* is the joint the 288R divisio names). It is not a cut in this stage.
- **Cap. XIII has no heading under its `CAPITULUM`** (the c6 case; ruling 40 applies).

## `low` rows (7, three decisions), with the alternatives

1. **Cap. XI: `bon-luc-c11-v14-26`, `-v27-32`, `-v33-41`, `-v42-54` (¶¶ 36–57 / 58–69 / 70–84 / 85–102).**
   - **The problem:** three sibling t4 sections of ~9.7, ~2.1 and ~9.6 pp. The first and third are over cap 8 and
     must be cut; the middle one (tentantium, 298L) is under the ~2.7 test and cannot stand alone. Joint positions:
     ¶ 36 288.3 · ¶ 43 290.8 · ¶ 58 295.9 · 298L t4 298.0 · 300L t4 300.1 · ¶ 77 302.3 · ¶ 85 304.8 · end 309.8.
   - **Chosen:** ¶ 36–57 (~7.6) | ¶ 58–69 (~4.2, the blasphemantium tail joined to the tentantium section across the
     298L t4, ruling 1c) | ¶ 70–84 (~4.6) | ¶ 85–102 (~5.0). Every piece ≥ 2.7, none over 8.
   - **Alternatives:** (a) ¶ 36–63 kept whole (~9.7, one-pass to 10), then ¶ 64–76 (~4.3, across the 300L t4) and
     ¶ 77–102 (~7.5) — the cuts at headings and at ¶ 70's own joint, but one row near 10; (b) ¶ 36–42 (~2.5) |
     ¶ 43–57 (~5.1) | ¶ 58–69 (~4.2) | ¶ 70–84 | ¶ 85–102 — both named joints of the 288R divisio, but a first row
     under ~2.7; (c) ¶ 36–57 | ¶ 58–76 (~6.4, across both t4s) | ¶ 77–102 (~7.5).
   - ⚠ **New shape:** `c11-v27-32` opens on a divisio paragraph and carries an interior t4 (298L). Earlier stages carry
     interior t4s only in heading-opened rows. The title is the ¶ 58 sentence (no heading in its opening stack).
2. **Cap. XII (two decisions): `bon-luc-c12-v1-7`, `-v8-12` (¶¶ 1–11 / 12–20) and `bon-luc-c12-v13-34` (¶¶ 21–48).**
   - **The 313R cut:** the four sibling t4 sections under the 310L t4 (dolositas · timiditas · veracitas · securitas)
     run ~6.3 pp together. **Chosen:** cut at the 313R t4, 3.6 + 2.7, the subdivisio's own pairing (*duae postremae
     correspondent duabus primis*). `c12-v8-12` is at the edge of the ≥ 2.7 test (the `c10-v1-3` case).
     **Alternative:** one row ¶¶ 1–20 (`c12-v1-12`, ~6.3 pp), or the 311R cut (2.4 + 3.9, fails the test).
   - **`c12-v13-34` kept whole at ~7.8 pp over 9 printed pages** (the `c7-v1-16` shape): the 316L to 324L headings
     stand ~7.8 pp apart, just under ruling 1b's ~8, so no divisio cut is licensed. **Alternative:** if ~7.8 is read as
     ~8, cut at ¶ 32 (*Dixitque ad discipulos suos*, 319L, the third member of the 316L divisio), 3.1 + 4.7 pp.

Each row's builder applies ruling 39's procedure (reads its boundary plates, promotes its own row or STOPS).

## Rule applications that needed a choice (not `low`)

- **Required cuts at named joints** (heading gap over ~8 pp, member over cap 8):
  - **c. 13 ¶¶ 36, 48, 64** (341R to `CAPITULUM XIV.` ~16.6 pp): the 341R subdivisio's second member (¶ 36), then
    ¶ 36's (¶ 48), then ¶ 48's (¶ 64); ¶ 36–76 (~12.2) and ¶ 48–76 (~8.3) are each over 8.
    4.35 + 3.9 + 4.35 + 3.9 pp.
  - **c. 14 ¶¶ 26, 36** (362L to 375L ~13.1 pp): both named members of ¶ 14's division, 4.2 + 3.8 + 5.1 pp; ¶ 36 alone
    would leave an 8.0 pp row, ¶ 26 alone an 8.9.
- **Kept whole, no licensed cut** (heading gap under ~8 pp): `c12-v35-48` (~6.6; ¶ 60 would give 3.3 + 3.3),
  `c12-v49-59` (~5.5), `c13-v1-9` (~5.6), `c14-v25-35` (~6.7; ¶ 56 would leave 1.7).

## Titles (ruling 22 / 33 / 40)

- **Lowest heading of the opening stack, whole:** `c11-v14-26` (the third 288R t4, below the t2 / t3 / two t4s inside
  ¶ 36), `c11-v33-41` (300L), `c12-v1-7` (the second 310L t4, below the 309L and first 310L t4s), `c12-v8-12` (313R),
  `c12-v13-34` (the second 316L t4), `c12-v35-48` (the second 324L t4), `c12-v49-59` (330R), `c13-v10-17` (the second
  341R t4), `c14-v1-6` (the second 358L t4), `c14-v7-11` (362L), `c14-v25-35` (375L) — eleven.
- **Sentence titles** (lemma + dividing words through the sentence naming the member; footnote anchors and `(Vers. N.)`
  tags dropped, as stages 2–3): `c11-v27-32` (¶ 58), `c11-v42-54` (¶ 85, whose naming sentence runs on through the
  Matthew quotation), `c13-v1-9` (¶ 1), `c13-v18-21` (¶ 36), `c13-v22-30` (¶ 48), `c13-v31-35` (¶ 64), `c14-v12-15`
  (¶ 26), `c14-v16-24` (¶ 36) — eight.
- **`c13-v1-9` opens on a bare `CAPITULUM XIII.`**: ruling 40 applies (a `CAPITULUM` heading is never a `title_la`).
- No Corrigenda entry touches a title (ruling 4).

## Corrigenda (assigned by page and column; positions as the Corrigenda gives them)

- **p. 294 col. 2 note 13** (*ubi cum Vulgata* → delete *cum Vulgata*) → `c11-v14-26`.
- **p. 300 col. 2 notes l. 5** (*suam* → *suum*) → `c11-v33-41`. ⚠ The line stands inside **p. 300 n. 8**, which begins
  in the left block and runs over the gutter into the right (*…Bernardus: Suam vas et secretum conscientia*); its
  anchor is in ¶¶ 70 ff. (the *lucerna*), so the builder of `c11-v33-41` re-derives the anchor.
- **p. 320 col. 2 l. 18** (*insiderat* → *insederat*) → `c12-v13-34`.
- **p. 333 col. 2 ll. 15 and 17** (*exterioris iudicii* → *indicii*, twice) → `c12-v49-59`.
- **p. 343 col. 2 l. 7** (*similiter* → *simul*) → `c13-v10-17`.
- **p. 346 col. 1 l. 16** (*Manducit* → *Manuducit*) → `c13-v18-21`; it stands in ¶ 36 (*Manducit igitur per exemplum
  dupliciter*, read on the plate), below the title sentence.
- **p. 361 col. 2 note 13** (*nota 3* → *nota 13*) → `c14-v1-6`.

Seven entries, all of the Corrigenda's Luke entries between pp. 288 and 381.

## Size distribution (19 rows)

- **Printed pages touched:** min 4 / mean 5.8 / max 9.
- **Estimated text extent** (column fractions from text-layer paragraph positions against plate-measured body ends;
  capitulum breaks and headings placed from the plates; PREDICTION): min 2.7 / mean 4.9 / max 7.8 pp.

## Not verified

- **Paragraph numbers inside rows** come from the text layer, anchored by plate-read numbers at both ends of every row.
- **Verse ends** are taken from the `(Vers. N.)` tags and the next row's lemma. The lemmas named in divisio *ibi:*
  lists that are not boundaries (e.g. c. 12 ¶¶ 26, 41; c. 14 ¶¶ 40, 44) were matched to their ¶ numbers on the text
  layer only.
- **Footer registers** were not counted (the builders count them; ruling 15).
