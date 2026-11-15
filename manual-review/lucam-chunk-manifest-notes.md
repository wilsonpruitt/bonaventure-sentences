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
