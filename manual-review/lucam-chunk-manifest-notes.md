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
