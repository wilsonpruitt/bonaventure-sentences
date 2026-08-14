# `de-reductione` — plate scouting (*De reductione artium ad theologiam*, printed pp. 319–325)

Banked BEFORE the chunk is written, per the frozen rule that plate work is committed
ahead of the writing so a crash costs nothing. Work 7 of Vol V; slug `de-reductione`,
book id 7.

## ✅ The span is closed at both ends, positively

- **p. 317 = the half-title** (`SERAPHICI DOCTORIS / SANCTI BONAVENTURAE / OPUSCULUM /
  DE / REDUCTIONE ARTIUM AD THEOLOGIAM`) — banked at the Itinerarium scholion's scouting,
  not re-derived.
- **p. 318 = MEASURED BLANK — 146 ink px** at 450 dpi (2571×3823). The launch pointer
  flagged it as *expected* blank and never checked; it is now measured, as pp. 292 and 294
  were. Recorded as a checked negative.
- **Body pp. 319–325.** p. 319 opens under a full-width display title `DE / REDUCTIONE
  ARTIUM AD THEOLOGIAM` and the text begins directly at numbered paragraph **`1.`**.
- The work ends at **¶ 26** (*…qui est benedictus in saecula saeculorum. Amen.*), and the
  end is fixed **positively from the `COLLATIONES IN HEXAEMERON` half-title** (raw L57174),
  never from white space.
- **Raw range L56056 → L57174.** 6,811 raw words including the apparatus.

## ⬜→✅ THE CHUNK UNIT — decided from the plate: **ONE CHUNK FOR THE WHOLE WORK**

The launch pointer made this the session's first decision and forbade settling it by
analogy. Four independent witnesses, all pointing the same way:

1. **The plate prints NO division of any kind.** No `Cap. N.`, no `Pars`, no heading of
   any sort on any of the seven leaves — 26 numbered paragraphs of continuous prose under
   a running head. Neither the Breviloquium's nor the Itinerarium's chunk-per-capitulum
   rule has anything to attach to.
2. **⚠⚠ `Pars I.` and `Pars 2.` ARE MARGINAL GLOSSES — confirmed on the plate**, set in the
   outer margin in the same small type as `Comparantur cum 6 formationibus in Genesi.`,
   `Principium statuitur pro 2. parte.`, `Reductio cognitionis sensitivae quoad tria.`
   They are Quaracchi's editorial outline, not the author's division, and are trimmed to
   the Marginalia list like every other gloss. **`Pars 2.` stands at ¶ 8**
   (*Videamus igitur, qualiter aliae illuminationes reducuntur…*).
3. **★★ THE VOLUME'S OWN INDEX GIVES THIS WORK ONE LINE AND NO SUB-ENTRIES** —
   `OPUSCULUM DE REDUCTIONE ARTIUM AD THEOLOGIAM. … pag. 319` — where the Itinerarium
   immediately above it is indexed capitulum by capitulum *plus* its Scholion, and the
   Hexaemeron immediately below is indexed collatio by collatio. **The editors' own table
   of contents treats this work as an undivided unit.** This is the strongest witness and
   it is independent of the plate.
4. **The frozen test — apparatus ON the division — returns nothing to chunk on.** The only
   divisional apparatus in the work is **p. 319 n. 1**, which records that *codex K* inserts
   a list of **ten capitula** after *veritatis salutaris* and prefixes the corresponding
   chapter to each part (`subinde cuilibet parti praemittit correspondens cap.`). That is
   apparatus about a division **Quaracchi did not adopt and does not print**; there is no
   printed division carrying apparatus, as the Itinerarium's capitula table did.

**Rejected, with reasons recorded so this is not re-opened:**

- **Chunking on the four lights** (*lumen exterius / inferius / interius / superius*) —
  authorial and stated in ¶ 1, but it divides only ¶¶ 1–5. ¶ 6 immediately restates the
  division as **six** illuminations and ¶¶ 8–26 are ordered by that six, so the four lights
  are a division of the work's first page and a half, not of the work. A scheme that leaves
  five of seven printed pages in one undivided lump is not a chunking of this work.
- **Chunking on the marginal `Pars`** — rejected in advance by the launch pointer and
  confirmed marginal on the plate (witness 2).

**Size sanity check:** ~4,300 words of Latin body — the same order as `bon-itin-scholion`
(4 pp, ~4,300 words), which was written in one chunk without trouble by the incremental
method. This is not an outsized unit; it is the second-largest in Vol V.

**Consequence for the census:** the id is **`bon-red`**, suffix-less — the census
blind-spot class for the **third** time after `bon-brev-prol` and `bon-itin-prol`, exactly
as the launch pointer predicted (it predicted the slug `bon-red-prol`; there is no prologue
to give it that name, but the blind-spot shape is the same). Ledger line required.

## Gutters — MEASURED per leaf, and `colcrop`'s default is WRONG on three of seven

Method: the frozen three-step. Step 1 `colcrop.py vol5 <page>`; step 2/3 the direct
per-column ink profile over several row windows, taking **the full band's midpoint** —
the band being the low-ink run **including the printed centre rule's ink island**, which
is what splits a true ~63 px band into two ~28 px sub-bands and collapses the window vote.

| p. | `colcrop` default | run | true band | island (centre rule) | **adopted** | verdict |
|---|---|---|---|---|---|---|
| 319 | 1205 | 61 px | 1174–1236 (63) | 1203–1208 | **1205** | default CONFIRMED |
| 320 | 1347 | 61 px | 1315–1379 (65) | 1345–1351 | **1347** | default CONFIRMED |
| 321 | 1211 | **20 px** | 1163–1225 (63) | 1193–1196 | **1194** | default **REJECTED** (−17) |
| 322 | 1371 | **37 px** | 1348–1410 (63) | 1376–1384 | **1379** | default **REJECTED** (−8) |
| 323 | 1182 | 54 px | 1156–1219 (64) | 1186–1190 | **1184** | ⚠ skewed leaf, see below |
| 324 | 1315 | **21 px** | 1304–1366 (63) | 1334–1337 | **1335** | default **REJECTED** (−20) |
| 325 | 1187 | 53 px | 1151–1215 (65) | 1181–1185 | **1183** | default confirmed (−4) |

- **★ THE SUB-60 RULE FIRED THREE TIMES AND WAS RIGHT THREE TIMES.** Every default on a
  run under 40 px was wrong (321 by 17 px, 324 by 20 px, 322 by 8 px); both defaults on a
  61 px run were right. **Run width triggers the look; it still never decides** — 323 and
  325 came in at 53–54 px and were within 4 px.
- **★★ SCAN SKEW IS ATTESTED ON THIS LEAF-SET — the fourth mechanism, now seen.** Profiled
  in five vertical bands, **p. 323's gutter drifts MONOTONICALLY LEFT down the page**:
  1196 (rows .25–.39) · 1187 · 1184 · 1176 · 1169 (rows .81–.95) — 27 px of drift with a
  tight island in each band, i.e. not noise and not two regions in different measures.
  p. 321 drifts the same way more mildly. **A single split_x is therefore an approximation
  on a skewed leaf**; 1184 is the body-centre value and the ±60 px crop padding absorbs
  the rest. Read the top and foot of a skewed leaf's columns with the drift in mind.
- ⚠ **The 0.55–0.90 window blew out to 389 px on p. 320 and 155 px on p. 321** — the
  footer register's blocks are narrower than the columns, the same third failure mode c7
  found on p. 313's footer. Do not profile a footer region for a body gutter.

## Per-leaf register — read off the 450 dpi bands, anchors only

### p. 319 — 6 notes · anchors 3 L / 3 R · block 3 L / 3 R (**coincide**) · ⚠ gutter runover
- Anchors: **¹** *primo capitulo* · **²** *artis mechanicae* · **³** *in Didascalico* (all LEFT);
  **⁴** *illud Horatii* · **⁵** *gesticulationibus corporis* · **⁶** *armaturam fabricatam*
  (all RIGHT).
- **⚠ n. 3 RUNS OVER THE GUTTER** — the left block breaks at *…omissa* theatrica*, sub-* and
  continues *stituebantur militaris et fabrilis…* at the head of the right block, **carrying
  a verse line** (*Rus, nemus, arma, rates, vulnera, lana, faber.*). Ledger: 1 gutter-crossing
  runover. The continuation opens on a lower-case fragment, the familiar trap.
- Digits corroborated at the band: n. 3 `II. c. 21` + `I. Excerpt. prior. c. 14`; n. 4
  `v. 333` / `ibid. v. 343`; n. 6 `II. Erudit. didascal. c. 23`, `molli et leni 1, 2, 3`.
- Marginalia, body order: `Pars I.` · `Origo omnis illuminationis et multiplicis luminis
  emanatio.` · `Quadruplex lumen.` · `De 1. lumine.` · `Est septuplex.` · `Sufficientia.` ·
  `Divisio.` · `De 1. membro.` · `Subdivisio 2. membri.` · `Quoad operimentum artes 2.` ·
  `Item, quoad cibum.`
- ⚠ **The plate bleaches two words the raw also mangles** — *cum hoc insinuat [multiplicis]
  luminis ab illa fontali luce liberalis [emanatio]*: both are faint on the scan, and both
  are recoverable **from the marginal gloss beside them**, which reads *…multiplicis luminis
  emanatio*. Recorded as settled, not flagged.

### p. 320 — 8 notes · anchors 4 L / 4 R · **block 6 L / 2 R — overruns LEFT by two**
- Anchors: **¹** *cibi multiplicem* · **²** *excellentiam et curialitatem* · **³** *Theatrica
  autem est unica* · **⁴** *tertio super Genesi* (LEFT); **⁵** *quinta essentia* · **⁶**
  *sufficientiam sensuum* · **⁷** *naturaliter sunt inserta* · **⁸** *ordo vivendi* (RIGHT).
- **The left block prints nn. 1–6** and n. 6 itself **runs over the gutter** (*…ut paulo
  inferius insi-* | *nuatur, plures…*). So the overrun and a runover are the same note.
  Ledger: 1 gutter-crossing runover.
- **★ Digits settled at the band against a garbled raw:** n. 4 raw `C(i: VII. c. \'6.` →
  plate **`Cfr. VII. c. 15. n. 21.`**; n. 5 raw `supra pag. ^9` → plate **`supra pag. 29,
  nota 6`**. Also confirmed: n. 4 `Cap. 4. et 5. n. 6. et 7.`, `et XII. c. 16. n. 32.`,
  `Vide supra pag. 227, nota 5`; n. 5 `Breviloq. p. II. c. 3. seq.`, `Quaest. de scientia
  Christi, q. 4. ad 11`, `I. Sent. d. 3. p. I. q. 1. ad 2`; n. 6 `Alex. Hal., S. p. II.
  q. 66. m. 3`, `Ioan. a Rupella, Sum. de Anima, p. II. c. 19`; n. 7 `Itinerar. c. 3. n. 2.
  et pag. 120, nota 11`, `August., VIII. de Civ. Dei, c. 4`, `ibid. II. c. 7; XI. c. 20.
  et Epist. 137. (alias 3.) c. 5. n. 17`; n. 8 `supra pag. 19, nota 7`, `Itinerar. mentis
  etc. c. 3. n. 7. et I. Sent. pag. 73, nota 7`.
- Marginalia, body order: `Alius modus.` · `Item, quoad utriusque adminiculum.` ·
  `De 2. lumine.` · `Est quintuplex.` · `Sufficientia sec. naturam luminis elementorum.` ·
  `Notandum.` · `Alius modus commemoratur.` · `De 3. lumine.` · `Est triplex.` ·
  `Sufficientia.` · `Modus 2.` · `Modus 3.`
### p. 321 — 8 notes · anchors 4 L / 4 R · **block 3 L / 5 R — UNDERRUNS by one** · no runover
- Anchors: **¹** *ad veritatem doctrinae* · **²** *has tres passiones* · **³** *in
  metaphysicam* · **⁴** *nonnulla fuerit controversia* (LEFT); **⁵** *apparet ex ipsis
  nominibus* · **⁶** *a Patre luminum descendit* · **⁷** *qualiter est Deo adhaerendum* ·
  **⁸** *Hugo vero omnia haec* (RIGHT).
- **★ THE OVERRUN REVERSED AGAIN, ONE LEAF AFTER OVERRUNNING BY TWO.** p. 320's left block
  took two of the right column's notes; p. 321's left block **gives one of its own away** —
  n. 4 anchors in the LEFT column and prints at the head of the RIGHT block. Read anchors,
  only anchors, on every leaf: the run direction carries nothing forward.
- **✅ RECORDED NEGATIVE: no runover on this leaf.** Both blocks close cleanly — the left
  block ends on n. 3's *(in principio).* followed by the printed signature line
  **`S. Bonav. — Tom. V.`**, and the right block opens **numbered ⁴**. Checked, not assumed.
  ★ The signature line is printer's furniture (gathering signature), not text and not
  apparatus — do not transcribe it.
- **★★ A 1/4 SETTLEMENT, AND THE RISK RAN IN THE USUAL DIRECTION.** n. 3's `Cfr. Aristot.,
  VI. Metaph. text. 2. et XI. c. 6. (V. c. 1. et X. c. 7.)` — at band scale the `1` in
  `(V. c. 1.` reads convincingly as a **4**; magnified it is a plain serif `1` (upper-left
  flag, foot serif, no open triangle), the raw's `I.` agrees, and the sense agrees
  (Metaph. V c. 1 is *de principio*, and the sentence is about *principium, finis et
  exemplar*). Two independent witnesses, as the frozen rule requires. Likewise
  **`Boeth., Dialog. 1. in Porphyr.`** — a `4` is impossible, the first commentary having
  two books.
- Other digits corroborated: n. 1 `XI. de Civ. Dei, c. 25`; n. 2 `supra pag. 206, nota 11`
  (raw `nota II.`) and `supra pag. 287, nota 5`; n. 4 `I. Metaph. text. 6. et 25. seqq.
  (c. 6. et 9.)`, `83 Qq. q. 46`, `II. Sent. d. 1. p. I. a. 1. q. 1. ad 3. et 4. ac dub. 2`;
  n. 5 `II. Erudit. didascal. c. 20` + `Isidor., II. Etymolog. c. 24. in fine` (raw `c. 2i.`);
  n. 6 `Iac. 1, 17`; n. 7 `Breviloq. Prolog. § 4`.
- Marginalia, body order: `Rationalis philosophia triplicatur.` · `Grammatica, logica,
  rhetorica.` · `Naturalis philosophia triplicatur.` · `Physica, mathematica, metaphysica.` ·
  `Item, moralis philosophia.` · `Monastica, oeconomica, politica.` · `De 4. lumine.` ·
  `Unus intellectus litteralis, triplex mysticus.` · `Quid doceat Scriptura.` · `Notandum.` ·
  `Sex differentiae luminis.` · `Sex illuminationes cum vespera.`

### p. 322 — 8 notes · anchors 5 L / 3 R · **block 4 L / 4 R — underruns by one** · no runover
- Anchors: **¹** *omnis scientia destruetur* · **²** *Unde valde apte* · **³** *et propterea*
  · **⁴** *cognoscendi oblectamentum* · **⁵** *venit plenitudo temporis* (LEFT); **⁶** *aut ex
  superbia* · **⁷** *nec auris auditu impletur* · **⁸** *in illuminatione* [artis mechanicae]
  (RIGHT).
- **★ A THIRD DIRECTION IN THREE LEAVES** — p. 320 overran by two, p. 321 underran by one,
  p. 322 underruns by one again. Both blocks close cleanly; **recorded negative: no runover
  on this leaf**, checked at both block feet.
- **★★ THE 1/4 CLASS AGAIN, AND THE SENSE SETTLED IT: n. 1 is `Epist. I. Cor. 13, 8`**, not
  the `43, 8` the plate appears to print — 1 Cor 13:8 is *scientia destruetur*, which is the
  very clause the anchor sits on. The raw prints `43` too, so **both witnesses are wrong
  together and only the sense saves it**; a purely mechanical reading of either would have
  shipped a citation to a chapter 1 Corinthians does not have.
- Other digits: n. 1 `Breviloq. p. II. c. 2. et Itiner. mentis in Deum, c. 7. n. 1`; n. 5
  `Gal. 4, 4` + `[cfr. Phil. 2, 7.]`; n. 6 `I. Ioan. 2, 16`, `Breviloq. p. III. c. 9`,
  `Aristot., II. de Anima, text. 63. seqq. (c. 6.); III. text. 28. seqq. (c. 7.) et X. Ethic.
  c. 4. seq.`; n. 7 `Eccle. 1, 8` (corroborated by the quoted *Non saturatur oculus*),
  `tom. IV. pag. 137, nota 6`, `Breviloq. p. V. c. 6`; n. 8 `CIKL et 1, 2 lumine`.
- Marginalia, body order: `Comparantur cum 6 formationibus in Genesi.` · `Principium
  statuitur pro 2. parte.` · **`Pars 2.`** · `Reductio cognitionis sensitivae quoad tria.` ·
  `Primo, de medio.` · `Applicatio.` · `Secundo, de exercitio.` · `Applicatio.` · `Unde
  inordinatio.` · `Tertio, de oblectamento.` · `Applicatio.` · `Epilogus.` · `Reductio artis
  mechanicae quoad tria.` · `Primo, de egressu.`
- ⚠ **This is the leaf that carries the editors' `Pars 2.`** — at ¶ 8, beside *Videamus
  igitur, qualiter aliae illuminationes…*, with `Principium statuitur pro 2. parte.` beside
  ¶ 7 one paragraph above. Marginal, trimmed to the Marginalia list, **not a chunk boundary**.

### p. 323 — 11 notes (the heaviest leaf) · anchors 6 L / 5 R · **block 8 L / 3 R — overruns
by two** · ⚠ gutter runover
- Anchors: **¹** *sicut disposuit* · **²** *quae ab eo* · **³** *in quo omnia disposuit* ·
  **⁴** *Ioannis decimo quarto* · **⁵** *totius fidei integritatem* · **⁶** *perseveranter
  operari* (LEFT); **⁷** *bonum honestum, conferens et delectabile* · **⁸** *et Deus in eo* ·
  **⁹** *mentis conceptum* · **¹⁰** *Proverbiorum octavo* · **¹¹** *modum, speciem et ordinem*
  (RIGHT).
- **⚠ n. 8 RUNS OVER THE GUTTER** — the left block ends *…Et qui manet in caritate in Deo etc.*
  and the right block **opens on an em-dash fragment**, *— Seq. locus est Prov. 8, 31. —
  Mox pro* ita quod…, before n. 9's numeral. Ledger: 1 gutter-crossing runover. ★ The
  fragment opens with `—`, not a lower-case word: **a third opening shape for a runover**,
  alongside the mid-word and mid-parenthesis breaks already recorded.
- **★ TWO TIER-B JOINS CHECK OUT AGAINST THE QUOTED TEXT ITSELF** (the index's second QA
  channel, applied at the plate): n. 4 `Vers. 6` against the body's *Ioannis decimo quarto*
  and *Nemo venit ad Patrem nisi per me* = John 14:6 ✓; n. 10 `Vers. 24` against
  *Proverbiorum octavo* and *Nondum erant abyssi* = Prov 8:24 ✓; and the runover's
  `Prov. 8, 31` against *deliciae meae esse cum filiis hominum* ✓.
- Other digits: n. 1 `Senecae (Epist. 65. ad Lucilium)`, `tom. I. pag. 600, nota 7`; n. 3
  `August. in Ps. 61, 12`, `supra pag. 211, nota 3`, `Breviloq. p. II. c. 12. in fine`; n. 4
  `Matth. 11, 27`, `Ioan. 1, 14`; n. 5 `Breviloq. p. V. c. 7`; n. 6 `Aristot., II. Ethic.
  c. 4`; n. 7 `I. Rhetor. c. 16. seqq. (c. 6. seqq.) et II. Ethic. c. 3`, `supra pag. 167,
  nota 2`; n. 8 `Epist. I. Ioan. 4, 16`; n. 9 `I. Periherm. c. 1`; n. 10 `Ibid. v. 18`,
  `Brevil. p. IV. c. 1`; n. 11 `Breviloq. p. III. c. 1, ubi in nota 1`, `Phil. 4, 5`,
  `Prov. 22, 11`, `Matth. 6, 22`.
- Marginalia, body order: `Notandum.` · `Applicatio.` · `Secundo, de effectu.` ·
  `Applicatio.` · `Tertio, de fructu.` · `Applicatio.` · `Epilogus.` · `Reductio rationalis
  philosophiae quoad tria.` · `Primo, de sermone quoad loquentem.` · `Applicatio.` ·
  `Secundo, quoad prolationem.` · `Applicatio.`

### p. 324 — 9 notes · anchors 4 L / 5 R · **block 4 L / 5 R — COINCIDE** · no runover
- Anchors: **¹** *sermonem ratione finis* · **²** *concludit Augustinus* · **³** *verbo
  virtutis suae* · **⁴** *inter seminales et ideales* (LEFT); **⁵** *dixit Augustinus* ·
  **⁶** *uniatur materiae corporali* · **⁷** *alpha et omega* · **⁸** *sole, luna et stellis*
  · **⁹** *vitam suscipiat ab anima* (RIGHT).
- **★★ A `1`/`4` SETTLED BY THE `II`→`H` FLATTENING, WHICH IS THE OTHER DOCUMENTED CLASS
  DOING THE WORK.** n. 2's `Enarrat. in Ps. 118. serm. 18. n. 4` prints so that the `118`
  reads as `148` and the raw gives **`Ps. H8.`** — the crossbar-less `II` again. Three
  witnesses agree on **118**: the raw's `H`, the serif shape, and the decisive fact that
  *Enarratio in Ps. 118* is the one enarratio delivered in **sermones** (32 of them), so
  `serm. 18` is only possible there. A mechanical read would have shipped Ps. 148.
- Other digits: n. 2 `In Epist. Ioan. tr. 3. n. 13`, `in Ioan. Evang. tr. 20. n. 3. et
  tr. 26. n. 7`, `de Magistro, c. 11. n. 38. seqq.`, `I. de Peccator. meritis etc. c. 25.
  n. 37`, `tom. II. pag. 690, nota 1. et tom. III. pag. 895, nota 1`; n. 3 `Hebr. 1, 3`
  (corroborated by the quoted *splendor gloriae et figura substantiae*); n. 4 `II. Sent.
  d. 18. a. 1. q. 1. seq.`, `Aristot., V. Physic. text. 7. (c. 1.), I. de Generat. et
  corrupt. text. 11. seqq. (c. 3.) et VII. Metaph. text. 22. seqq. (VI. c. 7.)`; n. 5
  `Libr. VI. de Trin. c. 10. n. 11`, `supra pag. 12, nota 7`; n. 6 `II. Sent. d. 17. a. 1.
  q. 2. ad 6. et d. 19. a. 1. q. 1. in corp.`; n. 7 `Apoc. 1, 8; 21, 6. et 22, 13`,
  `Breviloq. p. IV. c. 1. et 4`; n. 8 `Breviloq. p. II. c. 3. et 4`; n. 9 `Alfredi Anglici
  lib. de Motu cordis`, `Costa-Ben-Lucae lib. de Differentia animae et spiritus (ed.
  Innsbruck 1878)`, `tom. IV. pag. 848, nota 4. et pag. 907, nota 9; tom. II. pag. 421,
  nota 1. seq. et pag. 424, nota 3`.
- ⚠ n. 9's last clause is **bleached on the scan** — *Superius pr⟨o⟩ ad Deum A B et Dei.*
  The word is *pro*, which every other note in the volume uses in that formula; recorded
  as settled from the formula, not flagged.
- Marginalia, body order: `Tertio, quoad finem.` · `Applicatio.` · `Epilogus.` · `Reductio
  naturalis philosophiae quoad tria.` · `Primo, quoad habitudinem proportionis.` ·
  `Applicatio 1.` · `De appetitu in materia.` · `Applicatio 2.` · `Conclusio.` · `Secundo,
  quoad effectum causalitatis.` · `Applicatio.` · `Tertio, quoad medium unionis.` ·
  `Applicatio.`

### p. 325 — 9 notes · anchors 3 L / 6 R · **block 5 L / 4 R — overruns by two** · ⚠ runover
- Anchors: **¹** *ut dicit Anselmus* · **²** *cuius medium non exit ab extremis* · **³**
  *Mediatorem Dei et hominum* (LEFT); **⁴** *beneplacens et perfecta* · **⁵** *apex ipsius
  mentis sursum erigatur* · **⁶** *Deo adhaeret unus spiritus est* · **⁷** *multiformis
  sapientia Dei* · **⁸** *honorificetur Deus* · **⁹** *Amen* (RIGHT).
- **⚠ n. 5 RUNS OVER THE GUTTER** — left block ends *…rectum fit cor eius, ut* and the right
  block opens *bonus illi sit Deus. Cfr. Bernard.…*. Ledger: 1 gutter-crossing runover.
- **★ A DIGIT WHERE THE RAW IS SIMPLY WRONG AND THE ANCHOR PROVES IT:** n. 3 reads
  **`Epist. I. Tim. 2, 5`** on the plate; the raw gives `2,3`. 1 Tim 2:5 is *mediator Dei et
  hominum* — the very phrase the anchor sits on. Settled at the plate, corroborated by the
  body.
- Other digits: n. 1 `De Conceptu virg. et orig. pecc. c. 3. et Dialog. de veritate, c. 12`,
  `supra pag. 256, nota 6`; n. 2 `Plato, in Parmen.`, `tom. II. pag. 4, nota 11`,
  `Breviloq. p. I. c. 8`; n. 4 `Rom. 12, 2`, `Enarrat. in Ps. 31. enarrat. 2. n. 26`,
  `Enarrat. 2. in Ps. 32. n. 2; Enarrat. in Ps. 63. n. 18; in Ps. 67. n. 10; in Ps. 93.
  n. 18. et in Ps. 124. n. 2`; n. 5 `August., Enarrat. in Ps. 50. n. 15` (raw `Ps. iiO.`),
  `Bernard., Sermon. in Cantic. serm. 24. n. 5. seqq.`, `Breviloq. p. II. c. 10`; n. 6
  `Epist. I. Cor. 6, 17`, `Breviloq. p. V. c. 4`; n. 7 `Eph. 3, 10`; n. 8 `Epist. I. Petr.
  4, 11`; n. 9 `Ioan. 16, 13`, `Rom. 1, 25`, `Hugonis a S. Vict. Exposit. in Hierarch.
  caelest. Dionysii lib. II. c. 1`.
- Marginalia, body order: `Reductio moralis philosophiae quoad tria.` · `Triplex rectum.` ·
  `De primo cum applicatione.` · `Item, de secundo.` · `Item, de tertio.` · `Epilogus totius
  opusculi.` · `Fructus omnium scientiarum.`

### ★★ THE WORK'S END — a bare `EXPLICIT.`, centred across the full page
The text closes at ¶ 26 (*…qui est benedictus in saecula saeculorum. Amen.*) and beneath both
columns, **centred across the whole measure and not inside either column**, stands the single
word **`EXPLICIT.`** — **with no work title**, unlike `EXPLICIT ITINERARIUM IN DEUM` and
`EXPLICIT BREVILOQUIUM`. Located by ink-row profile (row ~2025 of 3823) after two wrong
crops; **a full-width centred line is invisible in a column band and nearly invisible in the
whole-page view.** Transcribe exactly as printed. The end is corroborated positively by the
`COLLATIONES IN HEXAEMERON` half-title at raw L57174.

## Register — TOTALS for the chunk

| p. | notes | anchors L/R | block L/R | runover |
|---|---|---|---|---|
| 319 | 6 | 3 / 3 | 3 / 3 (coincide) | n. 3 gutter |
| 320 | 8 | 4 / 4 | 6 / 2 (over by 2) | n. 6 gutter |
| 321 | 8 | 4 / 4 | 3 / 5 (under by 1) | — (checked) |
| 322 | 8 | 5 / 3 | 4 / 4 (under by 1) | — (checked) |
| 323 | 11 | 6 / 5 | 8 / 3 (over by 2) | n. 8 gutter |
| 324 | 9 | 4 / 5 | 4 / 5 (coincide) | — (checked) |
| 325 | 9 | 3 / 6 | 5 / 4 (over by 2) | n. 5 gutter |
| **total** | **59** | 29 / 30 | | **4 gutter-crossing** |

- **✅ RECORDED NEGATIVE, CHECKED LEAF BY LEAF: there is NO page-crossing runover anywhere in
  this work.** Every leaf's left footer block opens **numbered ¹** (pp. 320–325 each checked
  at the joint), so no register is left open across a leaf. This is the check c4 and c5 of the
  Itinerarium each found unforwarded; here it is checked and it is clean.
- **★ BLOCK vs ANCHOR STRUCTURE TOOK ALL THREE VALUES IN SEVEN LEAVES** — coincide (319, 324),
  overrun (320, 323, 325), underrun (321, 322) — and never twice in the same direction
  consecutively except 322→323, which reversed. **Read anchors, only anchors.**

- ⚠ **The raw's apparatus DOES carry digits inside the note bodies** even though Vol V's
  raw has no footnote numerals: what is missing is the superscript **openers** (`'` `"` `*`
  `°`), so entry numbering and ownership still come from the bands only — but a note's
  interior digits can be cross-read against the raw, and twice here the raw was the one
  that was wrong.
