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

# Stage 5 notes (Cap. XV – Cap. XVIII, pp. 381–472; 2026-11-16, Opus)

19 rows appended to `lucam-chunk-manifest.tsv` (XV 5 · XVI 4 · XVII 5 · XVIII 5), drawn at the p. 381 gate and before
any chunk of the next interval (ruling 2). Labels as in stages 1–4: **MEASURED** (read on a 300 dpi plate crop this
session) or **PREDICTION** (text layer only). No chunk was built.

## Plates read (MEASURED)

Plates pp. 383–473 extracted at 300 dpi (`raw/vision/vol7/p-383 … p-473.png`; pp. 381–382 were on disk). Three screens
found the headings, and every hit was read on a crop:

- a **vertical-gap screen**: each column's inner 76 % profiled for blank bands ≥ 38 px, the synchronised header and
  footer-rule pairs set aside. Column-specific body gaps stood at 381, 382L, 383R, 387L, 389R, 402, 407R, 415R, 417L,
  425, 426L, 429R, 433R, 437L, 437R, 439L, 448, 460R ×2, 472: **every one a heading or a capitulum except 417L**,
  which is Lucan's centred couplet *O quaesitorum terra pelagoque ciborum / Ambitiosa fames…* (456L's gap is the
  *Confiteor, tundo…* couplet on the text layer, the same class). The remaining single gaps (437R ~0.58, 451R, 454L, 460R ~0.54, 461L,
  463L, 467R and the 0.6–0.8 band on many leaves) are short closing lines or the footer zone of leaves whose body
  ends high. A separate check of **synchronised** body gaps (a full-measure heading would leave one) found only the
  four `CAPITULUM` stacks (381, 402, 425, 448, 472) and footer rules. **No t2 stands in pp. 381–472.**
- a **divisio sweep**: the paragraphs that open on a lemma + *Post… / Postquam…* (~20 in pp. 381–472), read on the
  plate wherever one is a boundary or a named joint;
- the **text layer's** small-type lines (`pdftotext -bbox-layout`, pdf pp. 407–499). It found every t4 and missed the
  437L t3, and was a cross-check only. ⚠ On pp. **421** and **444** the text layer reports every body line ~10 pt high
  (body ≈ 11 elsewhere); the plates show ordinary body type. A height filter that drops "small" lines drops those two
  leaves' paragraphs (c16 ¶¶ 50–52, c17 ¶¶ 53–56).

Full-width crops: pp. **402**, **425**, **448**, **472**. Boundary and heading crops: **382L**, **383R**, **387L**,
**389R**, **394R**, **398R**, **407R**, **415R**, **417L**, **419L**, **426L**, **429R**, **433R**, **437L**, **437R** (×2),
**439L**, **441R**, **444L**, **452R** (×3), **457R** (×2), **460R**, **465R**. Every row's opening, ending and
`title_la` was read on one of these.

## Headings found in pp. 381–472 (MEASURED; wording from the plate)

| Page | Tier (typography) | Wording | Row |
|---|---|---|---|
| 381 | capitulum | CAPITULUM XV. | c15-v1-7 |
| 381L | t4 (small bold) | Impietas Iudaeorum confutatur tripliciter. | c15-v1-7 |
| 382L | t4 | Expressio Iudaicae impietatis describitur tripliciter. | c15-v1-7 |
| 383R | t4 | Manifestatio pietatis divinae describitur triplici parabola. | c15-v1-7 (interior) |
| 387L | t4 | Parabola de drachma perdita. | c15-v8-10 |
| 389R | t4 | Parabola de filio prodigo. | c15-v11-20 |
| 402 | capitulum | CAPITULUM XVI. | c16-v1-8 |
| 402L | t4 | Commendatio et persuasio pietatis humanae describitur per documenta et exempla parabolica quoad duo. | c16-v1-8 |
| 402R | t4 | Primo, de pietate humana quoad opera corporalia tripliciter. | c16-v1-8 |
| 407R | t4 | Documentum pietatis perfectae quoad duo. | c16-v9-18 |
| 415R | t4 | Exemplum impietatis punitae, de quo tria. | c16-v19-22 |
| 425 | capitulum | CAPITULUM XVII. | c17-v1-4 |
| 425L | t4 | De pietate humana quoad opera spiritualia tripliciter. | c17-v1-4 |
| 426L | t4 | Informatio per documentum rationabile. | c17-v1-4 |
| 429R | t4 | Manuductio per duplex exemplum sensibile. | c17-v5-10 |
| 433R | t4 | Confirmatio per factum mirabile. | c17-v11-19 |
| 437L | t3 (larger roman) | Curiositas Iudaeorum confutatur dupliciter. | c17-v20-30 |
| 437R | t4 | De reprehensione Iudaicae curiositatis tria. | c17-v20-30 |
| 439L | t4 | De ratione huius reprehensionis tria. | c17-v20-30 (interior) |
| 448 | capitulum | CAPITULUM XVIII. | c18-v1-8 |
| 448L | t4 | De persuasione studiositatis exhibentur duo. | c18-v1-8 |
| 460R | t4 | Secundo curiositas in possidendo confutatur dupliciter. | c18-v18-27 |
| 460R | t4 | Primo, commendando paupertatem quadrupliciter. | c18-v18-27 |
| 472 | capitulum | CAPITULUM XIX. + t4 *Secundo confutat curiositatem in possidendo approbando liberalitatem duplicem.* | (next interval) |

The headings stand far apart in four stretches, and those rows are cut at Bonaventure's divisio paragraphs (ruling 1b):

- **c. 15:** the 389R t4 to `CAPITULUM XVI.` is ~12.9 pp (the prodigal son).
- **c. 16:** the 415R t4 to `CAPITULUM XVII.` is ~10.1 pp.
- **c. 17:** the 439L t4 to `CAPITULUM XVIII.` is ~8.9 pp.
- **c. 18:** `CAPITULUM XVIII.` to the 460R t4 is ~12.4 pp; the 460R t4 to `CAPITULUM XIX.` ~11.9 pp.

Every cut is named in a higher paragraph's own *ibi:* list.

⚠ **The 460R t4 *Secundo curiositas in possidendo…* is set as a t4 but is the second member of the 437L t3's
division** (¶ 35: *in perscrutando / in possidendo, infra decimo octavo*). Typography and logical rank part company
here; the manifest records the typography. Its partner on the far side of the gate is the 472L t4 under
`CAPITULUM XIX.` (*Secundo confutat curiositatem in possidendo approbando liberalitatem…*), the second member of ¶ 34.

## Last paragraph per capitulum (MEASURED)

**XV = 52** (402L, Vers. 32, running across the top of 402R; the setup table's **~50+** resolves to 52).
**XVI = 61** (425L, Vers. 31; the marginale *Epilogus* on 425R stands inside ¶ 61; the setup table's 61 is right).
**XVII = 62** (447R, Vers. 37, whose text runs across the top of both columns of p. 448; the table's 62 is right).
**XVIII = 66** (472L–R, Vers. 43; the table's 66 is right). Each capitulum's first and last pages are as the setup
table predicts (381–402, 402–425, 425–448, 448–472). **None overran.**

## The p. 472 gate (MEASURED)

Ruling 14 places the gate at the **close of c. 18**, p. 472. On the plate: ¶ 65 is Vers. 42 (472L, *Quarto quantum ad
integritatem sanitatis*); ¶ 66 (Vers. 43, *Et confestim vidit, per circumspectionem prudentiae…*) runs from 472L into
472R and ends at ~0.40 of the leaf (*…maior enim est omni laude ».*); `CAPITULUM XIX.` stands full measure at ~0.44,
with the 472L t4 *Secundo confutat curiositatem in possidendo approbando liberalitatem duplicem.* and ¶ 1 *Et ingressus
perambulabat Iericho etc.* below it (the next interval's). **The last row, `bon-luc-c18-v28-43`, ends exactly there.**
p. 472's running head already reads *C. XIX.* (the p. 381 habit). Nothing else is odd at the boundary; the one thing
to carry is the cross-gate pairing of the two *Secundo … in possidendo* headings above.

## The p. 381 opening (MEASURED; as the stage-4 notes and the resume describe)

¶ 69 closes c. 14 at ~0.52 of 381R; `CAPITULUM XV.` full measure at ~0.55; the 381L t4 *Impietas Iudaeorum confutatur
tripliciter.*; ¶ 1 *Erant autem appropinquantes etc.* (381L–R, the three-part divisio) ends at the foot of 381R; the
382L t4 *Expressio Iudaicae impietatis describitur tripliciter.* heads the next leaf over an un-numbered sentence and
¶ 2 (Vers. 1). `c15-v1-7` opens at the capitulum, and its `title_la` is the 382L t4 (ruling 22, the `c12-v1-7` shape).
p. 381 nn. 12–13 (pending from `c14-v25-35`) are this row's.

## Corrections to the setup table and the record (MEASURED)

- **Cap. XV last ¶ = 52**, not ~50+. The other three capitula match the table.
- **`CAPITULUM XV.` and `CAPITULUM XVII.` each have a t4 directly under them**, and each opening runs ¶ 1 to its end
  before a second t4 at the head of the next column/leaf (382L, 426L); `CAPITULUM XVI.` carries two t4s side by side
  (402L, 402R); `CAPITULUM XVIII.` one (448L). None is a bare capitulum, so ruling 40 does not arise.
- **¶ 13 of c. 18 prints *iuducere*** (452R, third line; turned *n*, read at full scale) in the title sentence of
  `c18-v9-14`. Recorded as printed; the builder handles it on the `[so printed]` convention (ruling 59 class).

## `low` rows (5, three decisions), with the alternatives

Joint positions are page-equivalents (column fractions from text-layer paragraph positions against plate-measured
column extents; PREDICTION within ±0.1 pp).

1. **Cap. XV: `bon-luc-c15-v1-7`, `-v8-10` (¶¶ 1–14 / 15–20).**
   - **The problem:** four sibling sections of ~1.7 (expressio, 382L t4), ~3.5 (the sheep, under the 383R t4), ~2.67
     (the drachma, 387L t4) and ~12.9 pp (the prodigal son, 389R t4). The expressio cannot stand alone; the drachma
     sits just under the ~2.7 test. Joint positions: CAP 381.78 · 383R t4 383.55 · 387L t4 387.04 · 389R t4 389.70 ·
     ¶ 26 391.63 · ¶ 29 393.30 · ¶ 33 394.84 · ¶ 42 398.76 · end 402.58.
   - **Chosen:** ¶ 1–14 (~5.25, across the 383R t4) | ¶ 15–20 (~2.67, the whole drachma section) | the prodigal son
     cut at ¶ 33 and ¶ 42.
   - **Alternatives:** (a) ¶ 1–20 kept as one row (~7.9, across two t4s; under cap 8); (b) ¶ 1–14 | ¶ 15–28 (~6.3, the
     drachma joined to the prodigal son's insolentia and miseria across the 389R t4, the `c11-v27-32` shape) | ¶ 29–41
     (~5.5) | ¶ 42–52 (~3.8).
2. **Cap. XVI: `bon-luc-c16-v9-18` (¶¶ 13–34) kept whole at ~7.9 pp over 9 printed pages** (the `c12-v13-34` shape): the
   407R and 415R headings stand ~7.9 apart, just under ruling 1b's ~8, so no divisio cut is licensed. **Alternative:**
   if ~7.9 is read as ~8, cut at ¶ 25 (*Audiebant autem omnia haec*, 411R, the second member of ¶ 13), 4.2 + 3.7 pp.
3. **Cap. XVIII: `bon-luc-c18-v9-14`, `-v15-17` (¶¶ 13–26 / 27–33).**
   - **The problem:** the reverentia member (¶ 13 to the 460R t4) is ~8.1 pp, over cap 8, so it is cut. Joint
     positions: ¶ 13 452.50 · ¶ 16 453.90 · ¶ 24 456.89 · ¶ 27 457.87 · 460R t4 460.59.
   - **Chosen:** ¶ 27, ¶ 13's own joint (*exemplum parabolicum / exemplum expressum*): 5.4 + 2.72 pp, the second at the
     edge of the ≥ 2.7 test.
   - **Alternative:** ¶ 24 (the parable's third *conditio*, *exauditio*, named in ¶ 13's sub-list): ¶ 13–23 (~4.4) |
     ¶ 24–33 (~3.7), joining the parable's tail to the infants across ¶ 13's principal joint.

Each row's builder applies ruling 39's procedure (reads its boundary plates, promotes its own row or STOPS).

## Rule applications that needed a choice (not `low`)

- **Required cuts at named joints** (heading gap over ~8 pp):
  - **c. 15 ¶¶ 33, 42** (389R to `CAPITULUM XVI.` ~12.9 pp): ¶ 21 names four members (¶¶ 21, 26, 29, 33) of ~1.9 /
    ~1.7 / ~1.5 / ~7.75 pp; the first three cannot stand alone and stay together (~5.1). The fourth, ¶¶ 33–52, is under
    cap 8 but over the 3–6 band and is cut at its own joint ¶ 42: 3.9 + 3.8. **Alternative:** ¶ 33–52 kept whole
    (~7.75).
  - **c. 16 ¶ 46** (415R to `CAPITULUM XVII.` ~10.1 pp): the third of ¶ 35's three members (causa / culpa ¶ 40 / poena
    ¶ 46). 3.8 + 6.3. **Alternatives:** ¶ 53 alone (6.55 + 3.6); ¶ 46 + ¶ 53 (3.8 + 2.75 + 3.6).
  - **c. 17 ¶ 53** (439L to `CAPITULUM XVIII.` ~8.9 pp): the third of ¶ 41's members. The reprehensio section (437R
    t4, ~2.0 pp) is joined to the ratio section across the 439L t4 (ruling 1c): 6.75 + 4.1. **Alternative:** cuts at
    ¶ 45 (*Et sicut factum est in diebus Noe*, 440L) and ¶ 53: 3.1 + 3.7 + 4.1.
  - **c. 18 ¶ 13** (`CAPITULUM XVIII.` to 460R ~12.4 pp): ¶ 1's two members, 4.3 + 8.1; the second is cut again (low
    decision 3).
  - **c. 18 ¶ 47** (460R t4 to `CAPITULUM XIX.` ~11.9 pp): the third of the subdivisio's four members (¶¶ 35, 42, 47,
    52). 5.0 + 6.9. **Alternatives:** ¶ 52 alone (7.1 + 4.85); ¶ 42 alone leaves 8.9 (no).
- **Kept whole, no licensed cut:** the three c. 17 sibling t4 sections (~3.6 / ~3.9 / ~3.7, each a row).

## Titles (ruling 22 / 33 / 40)

- **Lowest heading of the opening stack, whole:** `c15-v1-7` (the 382L t4, below CAPITULUM XV., the 381L t4 and ¶ 1),
  `c15-v8-10` (387L), `c15-v11-20` (389R), `c16-v1-8` (the 402R t4), `c16-v9-18` (407R), `c16-v19-22` (415R), `c17-v1-4`
  (the 426L t4), `c17-v5-10` (429R), `c17-v11-19` (433R), `c17-v20-30` (the 437R t4, below the 437L t3 and ¶ 35),
  `c18-v1-8` (448L), `c18-v18-27` (the second 460R t4) — twelve.
- **Sentence titles** (lemma + dividing words through the sentence naming the member; footnote anchors dropped):
  `c15-v20-24` (¶ 33), `c15-v25-32` (¶ 42), `c16-v22-31` (¶ 46, whose sentence runs on through its *ibi* clause),
  `c17-v31-37` (¶ 53), `c18-v9-14` (¶ 13, *iuducere* as printed), `c18-v15-17` (¶ 27), `c18-v28-43` (¶ 47) — seven.
- No Corrigenda entry touches a title (ruling 4).

## Corrigenda

**None.** The Corrigenda's Luke entries jump from p. 361 to p. 533; no entry falls in pp. 381–472. Every `corrigenda`
cell in this stage is empty.

## Split verses

Two rows share a verse with their neighbour (the `c4-v14-22` / `c4-v22-30` precedent): **Luke 15:20** (`c15-v11-20`
¶ 32 *Et surgens venit*; `c15-v20-24` ¶ 33 *Cum autem adhuc longe esset*) and **Luke 16:22** (`c16-v19-22` ¶ 44
*Factum est autem ut moreretur mendicus*; `c16-v22-31` ¶ 46 *Mortuus est autem et dives*).

## Size distribution (19 rows)

- **Printed pages touched:** min 3 / mean 5.8 / max 9.
- **Estimated text extent** (PREDICTION, method as stage 4): min 2.67 / mean 4.8 / max 7.9 pp; the 19 rows sum to
  ~90.7 pp (381.78 → 472.51).

## Not verified

- **Paragraph numbers inside rows** come from the text layer, anchored by plate-read numbers at both ends of every row.
  The text layer misreads several (¶ 15 as `13`, ¶ 25 of c. 15 as `23`, ¶ 35 of c. 15 as `33`, ¶ 51 of c. 17 as `31`,
  a 444R paragraph of c. 17 (¶ 54 or 55) as `53`, ¶ 65 of c. 18 as `63`); every boundary number was read on the plate.
- **Verse ends** are taken from the `(Vers. N.)` tags and the next row's lemma. The lemmas named in divisio *ibi:*
  lists that are not boundaries (e.g. c. 15 ¶¶ 26, 29, 48; c. 16 ¶¶ 25, 40, 53; c. 17 ¶¶ 30, 45, 58, 61; c. 18 ¶¶ 9,
  16, 24, 42, 52, 58) were matched to their ¶ numbers on the text layer only.
- **Footer registers** were not counted (the builders count them; ruling 15).

# Stage 6 notes (Cap. XIX – Cap. XXI, pp. 472–540; 2026-11-20, Opus)

18 rows appended to `lucam-chunk-manifest.tsv` (XIX 7 · XX 5 · XXI 6), drawn after the p. 472 gate and before any
chunk of the next interval (ruling 2), on Wilson's go of 2026-11-20. Labels as in stages 1–5: **MEASURED** (read on a
300 dpi plate crop this session) or **PREDICTION** (text layer only). No chunk was built; no existing row was touched.

## Plates read (MEASURED)

Plates pp. 474–541 extracted at 300 dpi (`raw/vision/vol7/p-474 … p-541.png`, 2476 × 3921, pHYs 300 dpi; pp. 472–473
were on disk and checked at 300 dpi). Three screens found the headings, and every hit was read on a crop:

- a **vertical-gap screen**: each column's inner 76 % profiled for blank bands ≥ 38 px (re-run at ≥ 28 px: nothing
  new), the running-head gap and the footer-rule pair (two gaps ≤ 14 px apart) set aside, plus a check for a second
  gap under the running head (a heading at a column head). Body gaps stood at 472, 487L, 487R ×2, 495L, 498L, 499R,
  501, 506L, 507R, 512L ×2, 516R, 518L, 518R ×2, 520, 523L, 540: **every one a heading or a capitulum except 495R**
  (the centred verse *Vagit infans, inter arcta conditus praesepia.*), **506L** (the footer zone; that leaf's rule pair
  was not resolved by the screen) and **507R** (a short closing line before ¶ 22). A check of **synchronised** gaps
  found only the four `CAPITULUM` stacks (472, 501, 520, 540). **No t1 or t2 stands in pp. 472–539.**
- a **divisio sweep**: the paragraphs that open on a lemma + *Post… / Postquam…* (~22 in pp. 472–540), read on the
  plate wherever one is a boundary or a named joint;
- the **text layer's** small-type lines (`pdftotext -bbox-layout`, pdf pp. 498–567). It found every t4 except the
  516R one, missed the 487L t3 (larger type), and was a cross-check only. It found no `CAPITULUM` by that spelling
  (`Capitclom XX.`, `Capitulu»! XXII.`). ⚠ **The pp. 421 / 444 height trap recurs on p. 490**: every body line there
  reports h ≈ 10 (body ≈ 11 elsewhere); the plate shows ordinary body type (c. 19 ¶¶ 49–50).

Full-width crops: pp. **472**, **501**, **520**, **540**. Boundary and heading crops: **472L**, **472R**, **477L**,
**477R**, **478L**, **480L**, **480R**, **481L**, **483R**, **487L**, **487R**, **491R**, **495L**, **495R**, **498L**,
**499R**, **500R**, **501L**, **503R**, **504R**, **506L**, **507R**, **509L**, **512L**, **516R**, **518L**, **518R**,
**519R**, **523L**, **524R**, **527L**, **530L**, **530R**, **533L**, **533R**, **536L**, **539R**, **540L**. Every row's
opening, ending and `title_la` was read on one of these.

## Headings found in pp. 472–540 (MEASURED; wording from the plate)

| Page | Tier (typography) | Wording | Row |
|---|---|---|---|
| 472 | capitulum | CAPITULUM XIX. | c19-v1-10 |
| 472L | t4 (small bold) | Secundo confutat curiositatem in possidendo approbando liberalitatem duplicem. | c19-v1-10 |
| 487L | t3 (larger roman) | Incredulitas Iudaeorum confutatur tum per facta tum per verba et documenta. | c19-v29-35 |
| 487R | t4 | Primo per facta confutat horum incredulitatem ostendendo, se habere quatuor dona in Lege promissa. | c19-v29-35 |
| 487R | t4 | Potestatem regalem promissam se habere, ostendit per tria. | c19-v29-35 |
| 495L | t4 | Pietatem pontificalem promissam se habere, ostendit per quatuor. | c19-v41-48 |
| 498L | t4 | Aequitatem iudicialem promissam se habere, ostendit per tria. | c19-v41-48 (interior) |
| 499R | t4 | Auctoritatem magistralem promissam se habere, ostendit per tria. | c19-v41-48 (interior) |
| 501 | capitulum | CAPITULUM XX. | c20-v1-9 |
| 501L | t4 | Secundo confutat Iudaeorum incredulitatem per verba et documenta et hoc in tribus partibus. | c20-v1-9 |
| 501L | t4 | Confutatio Pharisaeorum errantium ex malitia per tria. | c20-v1-9 |
| 512L | t4 | Confutatio Sadducaeorum errantium ex ignorantia quoad duo. | c20-v27-40 |
| 512L | t4 | Primo confutatur error circa resurrectionem per duo. | c20-v27-40 |
| 516R | t4 (column head) | Secundo confutatur error circa mysterium incarnationis, de quo tria. | c20-v41-47 |
| 518L | t4 | Informatio discipulorum ad prudentiam, de qua tria. | c20-v41-47 (interior) |
| 518R | t4 (column head) | Informatio ad cautelam quatuor malorum. | c20-v41-47 (interior) |
| 520 | capitulum | CAPITULUM XXI. | c21-v1-4 |
| 520L | t4 | Informatio ad eligentiam meliorum per exemplum viduae. | c21-v1-4 |
| 523L | t4 | Informatio ad providentiam respectu futurorum. | c21-v5-11 |
| 540 | capitulum; 540L t1 (large roman), t2 (italic), t3 (roman semi-bold) | CAPITULUM XXII. / Pars III. De passionis medicamento agitur dupliciter. / *Primo, de passione quoad quatuor antecedentia.* / Primo, de machinatione proditoris dicuntur quatuor. | (next interval) |

Every heading in a row's span is in that row's `headings` cell, interior ones and stacked pairs included (ruling 100's
lesson). The headings stand far apart in four stretches, and those rows are cut at Bonaventure's divisio paragraphs
(ruling 1b):

- **c. 19:** `CAPITULUM XIX.` to the 487L t3 is ~14.8 pp (Zacchaeus and the parable of the pounds); the 487L t3 to
  the 495L t4 ~8.1 pp (`low`, below).
- **c. 20:** `CAPITULUM XX.` to the 512L t4 is ~11.2 pp (the Pharisees).
- **c. 21:** the 523L t4 to `CAPITULUM XXII.` is ~16.8 pp (the eschatological discourse).

Every cut is named in a higher paragraph's own *ibi:* list.

⚠ **Typography and logical rank part company twice, as at 460R.** The 501L t4 *Secundo confutat Iudaeorum
incredulitatem per verba et documenta…* is set as a t4 but is the second member of the 487L t3's division (¶ 43:
*per facta / per verba et documenta, infra vigesimo*); its partner is the 487R t4 *Primo per facta…*. And the 518L t4
*Informatio discipulorum ad prudentiam* governs across `CAPITULUM XXI.`: its members two and three are c. 21 ¶ 1 (the
520L t4) and c. 21 ¶ 9 (the 523L t4). The manifest records the typography, and ruling 1a keeps the capitulum a hard
boundary.

## Last paragraph per capitulum (MEASURED)

**XIX = 75** (500R, Vers. 48, running across the top of both columns of p. 501 to *…et hauriet salutem a Domino ».*;
the setup table's 75 is right). **XX = 56** (519R, printed *56..*, un-versed, v. 47 continued; it runs across the top
of both columns of p. 520 to *…carnibus eorum ».*; the setup table's **~53** resolves to 56; ¶ 55 is Vers. 47).
**XXI = 60** (539R, Vers. 38, running across the top of both columns of p. 540; the setup table's **~54+** resolves to
60; ¶ 55 is *Attendite autem vobis* (Vers. 34); ¶ 56 is un-versed, ¶¶ 57–59 are Vers. 35–37). Each capitulum's first and last pages are as the
setup table predicts (472–501, 501–520, 520–540). **None overran.** XIX and XXI both close on the same Proverbs 8:34–35
quotation (*Beatus homo, qui audit me…*).

## The p. 540 gate (MEASURED)

Ruling 14 places the gate where **Pars II closes**, p. 540. On the plate: ¶ 60 (Vers. 38) runs from 539R across the top
of both columns of p. 540 and ends at ~0.13 of the leaf; `CAPITULUM XXII.` stands full measure at ~0.155; below it on
540L stand the t1 **`Pars III. De passionis medicamento agitur dupliciter.`** (large roman, centred; the third
*Pars* heading of the work, after 13L and 88L), ¶ 1 *Appropinquabat autem dies festus azymorum etc.* (divisio:
*antecedentia / concomitantia, ibi Adhuc eo loquente, ecce turba, infra eodem capitulo*), the italic t2 *Primo, de
passione quoad quatuor antecedentia.*, an un-numbered divisio naming the Tabula's four *antecedentia* (machinatio
proditoris / institutio Sacramenti altaris, ibi *Venit autem dies azymorum* / eruditio discipulorum, ibi *Facta est
autem et contentio inter eos* / supplicatio, ibi *Et egressus, ibat secundum consuetudinem in montem Olivarum*), and the
t3 *Primo, de machinatione proditoris dicuntur quatuor.* **The Pars III heading stands at p. 540, as ruling 14 assumed:
it fixes the gate.** **The last row, `bon-luc-c21-v28-38`, ends exactly at `CAPITULUM XXII.`** p. 540's running head
reads *C. XXII.* Anchors read (the register was not counted): p. 540 n. 1 (*accelerare*¹, 540L top band) is c. 21's;
n. 2 on is c. 22's. **Stage 7 opens on a five-element stack (capitulum, t1, ¶ 1, t2, un-numbered text, t3)**; under
ruling 22 its first row's title would be the t3 *Primo, de machinatione proditoris dicuntur quatuor.* (a prediction
for the stage-7 drafter, not a ruling).

## The p. 472 opening (MEASURED; as the stage-5 notes and the resume describe)

¶ 66 closes c. 18 at ~0.40 of 472R; `CAPITULUM XIX.` full measure at ~0.44; the 472L t4 *Secundo confutat curiositatem
in possidendo approbando liberalitatem duplicem.*; ¶ 1 *Et ingressus perambulabat Iericho etc.* (472L, no Vers. tag,
marginale *Divisio.*), continued on 472R through the un-numbered *Studiositas autem Zachaei commendatur ex tribus*
(marginale *Subdivisio.*) to ¶ 2 (Vers. 1). `c19-v1-10` opens at the capitulum and its `title_la` is the 472L t4
(ruling 22). **p. 472 nn. 8–12 are this row's** (anchors *secundo*⁸, *ibi*⁹, *caelum*¹⁰, *ibi*¹¹, *inardescit*¹²).

## Shared capitulum leaves (anchors read; registers not counted)

- **p. 501:** c. 19 ¶ 75's tail in the top band carries no anchor; n. 1 (*documenta*¹) is c. 20 ¶ 1's. Prediction: the
  whole p. 501 register is `c20-v1-9`'s.
- **p. 520:** the top band (c. 20 ¶ 56) carries nn. 1–2 (*sexto*¹ 520L, *tertio*² 520R); n. 3 (*secundo*³) is c. 21
  ¶ 1's. `c20-v41-47` owns p. 520 nn. 1–2, `c21-v1-4` from n. 3.
- **p. 540:** n. 1 `c21-v28-38`'s; n. 2 on, the next interval's.

## Corrections to the setup table and the record (MEASURED)

- **Cap. XX last ¶ = 56**, not ~53. **Cap. XXI last ¶ = 60**, not ~54+. Cap. XIX's 75 is right; all three page spans
  are right, and XXII opens on p. 540 with the Pars III heading.
- **No capitulum in this stage is bare** (ruling 40 does not arise): `CAPITULUM XIX.` and `CAPITULUM XXI.` each have one
  t4 under them; `CAPITULUM XX.` two, stacked in 501L around ¶ 1.
- **Two lemmas print against the Vulgate**, both with an anchor on the word (transcribe as printed; the builders read
  the notes): c. 19 ¶ 32 *Et tertius*¹¹ *venit dicens* (Vulgate v. 20 *Et alter venit*), in `c19-v20-28`'s title;
  c. 19 ¶ 53 *Exeunte*¹³ *autem illo* (Vulgate v. 36 *Euntе autem illo*), in `c19-v36-40`'s title.
- The Tabula's references for this stretch check out on the body: *approbatur liberalitas dupliciter (c. 19, 11)* = ¶ 15;
  *incredulitas (c. 19, 29)* = ¶ 43; *per verba et documenta (c. 20, 1)* = c. 20 ¶ 1; *Pharisaei, Saducaei, informantur
  discipuli ad tria* = c. 20 ¶¶ 1, 34, 52.

## `low` rows (9, four decisions), with the alternatives

Joint positions are page-equivalents (column fractions from text-layer paragraph positions against plate-measured
column extents and footer rules; PREDICTION within ±0.1 pp).

1. **Cap. XIX: `bon-luc-c19-v29-35`, `-v36-40` (¶¶ 43–52 / 53–62).**
   - **The problem:** the 487L t3 and the 495L t4 stand ~8.1 pp apart (487.33 → 495.45), over cap 8 by less than the
     estimate's own error (the `c16-v9-18` ~7.9 case, from the other side). Joints: ¶ 48 489.82 · ¶ 53 491.87.
   - **Chosen:** cut at ¶ 53 (*Exeunte autem illo*, the third member of the 487R subdivisio): 4.5 + 3.6.
   - **Alternatives:** (a) ¶ 43–62 kept whole (~8.1, one-pass build to 10, ruling 1c); (b) ¶ 48 instead: 2.5 + 5.6,
     the first under the 2.7 test (no).
2. **Cap. XX: `bon-luc-c20-v1-9`, `-v10-18` (¶¶ 1–13 / 14–24).**
   - **The problem:** the Pharisee member (CAPITULUM XX. 501.09 → 512L t4 512.28, ~11.2 pp) must be cut. Its three
     members are calumnia ¶ 1–9 (~2.4), perfidia ¶ 10–24 (~5.8), versutia ¶ 25–33 (~3.0). Calumnia is under the 2.7
     test, and calumnia + perfidia (¶ 1–24, ~8.2) is over cap 8. Joints: ¶ 10 503.50 · ¶ 14 504.70 · ¶ 21 507.48 ·
     ¶ 25 509.32.
   - **Chosen:** ¶ 1–13 | ¶ 14–24 | ¶ 25–33 (3.6 / 4.6 / 3.0): calumnia joined to the head of the perfidia member
     (the benignitas parable, ¶¶ 10–13) across ¶ 10, cut at ¶ 14, ¶ 10's own joint (the `c11-v27-32` shape). Every
     piece ≥ 2.7, none over 6.
   - **Alternatives:** (b) ¶ 1–9 | ¶ 10–24 | ¶ 25–33 (2.4 / 5.8 / 3.0): Bonaventure's three members exactly, which are
     also the three Gospel pericopes (Luke 20:1–8, 9–18, 19–26), but the first is under the 2.7 test; (c) ¶ 1–20 |
     ¶ 21–33 (6.4 / 4.8; ¶ 21 is the third member of ¶ 10, *Quid ergo faciet illis dominus vineae*), two rows, the
     second joined across ¶ 25.
3. **Cap. XX: `bon-luc-c20-v27-40`, `-v41-47` (¶¶ 34–46 / 47–56).**
   - **The problem:** three sections between the 512L stack and `CAPITULUM XXI.`: resurrectio (512L t4, ~4.2),
     incarnatio (516R t4, ~1.8), the discipuli member's first section (518L + 518R t4s, ~1.9). The last two cannot stand
     alone, and the capitulum stops the third from joining its own siblings in c. 21. Positions: 512L 512.28 · 516R
     516.52 · 518L ~~518.36~~ 518.53 (plate, p. 540 gate, ruling 122; the incarnatio section is then ~2.0 pp, not ~1.8, and the 518L / 518R section ~1.7, not ~1.9; their sum, the built `c20-v41-47`, unchanged) · CAPITULUM XXI. 520.26.
   - **Chosen:** ¶ 34–46 | ¶ 47–56 (4.2 + 3.7), the second joined across the 518L t4 (a higher joint, ¶ 1's third
     member) to the incarnatio section.
   - **Alternatives:** (a) ¶ 34–51 | ¶ 52–56 (6.1 + 1.9; the second a capitulum-bounded fragment); (b) ¶ 34–56 kept
     whole (~8.0, at cap 8).
4. **Cap. XXI: `bon-luc-c21-v1-4`, `-v5-11`, `-v12-19` (¶¶ 1–8 / 9–17 / 18–27).**
   - **The problem:** the widow (520L t4, ~3.0) is bounded by two headings; then no heading for ~16.8 pp. ¶ 9's four
     members are generaliter ¶ 9–12 (~1.5), persecutio ¶ 13–27 (~5.6), Ierusalem ¶ 28–40 (~2.9), iudicium ¶ 41–60
     (~6.8). Generaliter cannot stand alone. Positions: 523L t4 523.28 · ¶ 13 524.80 · ¶ 18 527.06 · ¶ 28 530.44.
   - **Chosen:** ¶ 1–8 | ¶ 9–17 | ¶ 18–27 (3.0 / 3.8 / 3.4): generaliter joined to persecutio (¶ 9–27, ~7.2, over 6),
     which the size rule then splits at ¶ 18, ¶ 13's own joint.
   - **Alternatives:** (b) ¶ 1–12 | ¶ 13–27 (4.5 + 5.6): generaliter joined back to the widow across the 523L t4, and
     the persecution member (Luke 21:8–19) kept whole; (c) ¶ 1–8 | ¶ 9–27 kept whole (~7.2).

Each row's builder applies ruling 39's procedure (reads its boundary plates, promotes its own row or STOPS). In
decision 4, `c21-v1-4`'s own span is fixed by two headings under (a) and (c); it is `low` because (b) moves its end.

## Rule applications that needed a choice (not `low`)

- **Required cuts at named joints** (heading gap over ~8 pp):
  - **c. 19 ¶ 15** (`CAPITULUM XIX.` to the 487L t3 ~14.8 pp): ¶ 1's two members, Zacchaeus ¶ 1–14 (~4.9) / the
    parable ¶ 15–42 (~9.9). The parable is cut again.
  - **c. 19 ¶¶ 22, 32** (the parable, ~9.9 pp): ¶ 15's first member (occasio, ¶ 15–17, ~0.8) and ¶ 18's first
    (status meriti, ¶ 18–21, ~2.2) cannot stand alone and stay together (~3.0); ¶ 18's second, status iudicii ¶ 22–42
    (~6.9), is over 6 and is cut at ¶ 32 (*Et tertius venit dicens*, the third of ¶ 22's four members), 3.3 + 3.6
    (the `c15-v20-24` / `c15-v25-32` application of the size rule). Positions: ¶ 15 477.45 · ¶ 22 480.46 · ¶ 25 481.26 ·
    ¶ 32 483.72 · ¶ 40 486.30 · t3 487.33. **Alternative:** one cut at ¶ 25 (*Venit autem primus*): ¶ 15–24 (~3.8) |
    ¶ 25–42 (~6.1, which no joint splits into two pieces ≥ 2.7, so it would stand whole).
  - **c. 20 ¶ 25** (the Pharisee member, ~11.2 pp): the third member of the 501L subdivisio; the other cuts are
    decision 2.
  - **c. 21 ¶¶ 28, 41, 48** (the 523L t4 to `CAPITULUM XXII.` ~16.8 pp): ¶ 28 and ¶ 41 are ¶ 9's third and fourth
    members; the fourth (¶ 41–60, ~6.8) is over 6 and is cut at ¶ 48, ¶ 41's own second member, 2.9 + 3.9 (¶ 55 would
    leave ~1.6). Positions: ¶ 41 533.31 · ¶ 48 536.23 · ¶ 55 538.46 · CAPITULUM XXII. 540.11. **Alternative:** ¶ 41–60
    kept whole (~6.8, the `c18-v28-43` size).
- **Kept together, sibling sections (ruling 1c):** `c19-v41-48`, the 495L / 498L / 499R t4 sections (~2.8 / ~1.1 /
  ~1.7; together ~5.6). **Alternative:** ¶ 63–69 | ¶ 70–75 (2.8 + 2.9).

## Titles (ruling 22 / 33 / 40)

- **Lowest heading of the opening stack, whole:** `c19-v1-10` (the 472L t4), `c19-v29-35` (the second 487R t4, below
  the 487L t3, ¶ 43 and the first 487R t4), `c19-v41-48` (495L), `c20-v1-9` (the lower 501L t4, below CAPITULUM XX.,
  the upper 501L t4 and ¶ 1), `c20-v27-40` (the lower 512L t4, below the upper one and ¶ 34), `c20-v41-47` (516R),
  `c21-v1-4` (520L), `c21-v5-11` (523L) — eight. Where two t4s stand at one column, `title_la_source` names the column
  and the title is the lower (the `c18-v18-27` / `c16-v1-8` convention).
- **Sentence titles** (lemma + dividing words through the end of the sentence naming the member; verse tags and
  footnote anchors dropped): `c19-v11-14` (¶ 15), `c19-v15-19` (¶ 22, whose sentence runs on through its four *ibi*
  clauses onto 480R, the `c16-v22-31` precedent), `c19-v20-28` (¶ 32, *tertius* as printed), `c19-v36-40` (¶ 53,
  *Exeunte* as printed), `c20-v10-18` (¶ 14), `c20-v19-26` (¶ 25), `c21-v12-19` (¶ 18), `c21-v20-24` (¶ 28, the sentence
  crossing to 530R), `c21-v25-27` (¶ 41), `c21-v28-38` (¶ 48) — ten.
- No Corrigenda entry touches a title (ruling 4).

## Corrigenda

**One:** p. 533, col. 2, l. 11, *poterunt* → *poterant*. Read on the plate: 533R l. 11 *siderum limpidissimae flammae
illuminare poterunt*, inside the Wisdom 17:5 quotation in c. 21 ¶ 41 → `bon-luc-c21-v25-27`'s `corrigenda` cell. It
touches no title. No other Luke entry falls in pp. 472–540 (the list jumps from p. 361 to p. 533); every other
`corrigenda` cell in this stage is empty.

## Split verses

**None.** Every row ends on a verse's last paragraph and the next opens on the next verse's lemma.

## Size distribution (18 rows)

- **Printed pages touched:** min 4 / mean 4.8 / max 7.
- **Estimated text extent** (PREDICTION, method as stages 4–5): min 2.87 (`c21-v20-24`) / mean 3.76 / max 5.64
  (`c19-v41-48`); the 18 rows sum to ~67.6 pp (472.51 → 540.11). The mean is the lowest of any stage: the heading
  gaps here are long, and the size rule cuts every piece over 6 that splits into two pieces ≥ 2.7.

## Not verified

- **Paragraph numbers inside rows** come from the text layer, anchored by plate-read numbers at both ends of every row.
  The text layer misreads several (c. 19 ¶ 25 as `23`, ¶ 38 [Vers. 25] as `Vers. 23`, ¶ 45 as `43`, ¶ 53 as `83`,
  ¶ 65 as `63`; c. 20 ¶ 5 as `0`, ¶ 25 as `2o`; c. 21 ¶ 35 as `33`, ¶ 51 as `Sl`, ¶¶ 55–60 as `5b`, `b6`, `b7`, `•58`,
  `b9`, `GO`); every boundary number was read on the plate.
- **Verse ends** are taken from the `(Vers. N.)` tags and the next row's lemma. The lemmas named in divisio *ibi:*
  lists that are not boundaries and were not cropped (c. 19 ¶¶ 8, 12, 40, 48, 56, 60; c. 20 ¶ 21; c. 21 ¶¶ 24, 55)
  were matched to their ¶ numbers on the text layer only.
- **Footer registers** were not counted (the builders count them; ruling 15). The shared-leaf anchor splits above are
  anchors read on crops, not register counts.
- **Gutters** were taken from a minimum-ink screen for cropping only; no gutter here is a measurement for a builder.
