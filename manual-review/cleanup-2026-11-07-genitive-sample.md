# Genitive sigla (ruling 148(b)): the full sample (NOT APPLIED)

`tools/authorities.json` is untouched. Method: scratch copies of the table with the genitive added to the author's `sigla`, run through the unmodified `tools/build-authorities.py`, diffed against the committed `index/authorities.tsv` (17,127 rows; to a work 16,785).

## Measured effect

| scenario | rows | to a work | author only | key-level net new records | net removals |
|---|---|---|---|---|---|
| committed | 17,127 | 16,785 (98.0%) | 175 | | |
| **A: Dionysii, Augustini, Bernardi** | 17,318 (+191) | 16,967 (98.0%) | 178 | **+194** (Augustine 141, Bernard 37, Dionysius 16) | **3** |
| B: A plus the genitive of every other author whose nominative siglum is a full name (Gregorii, Aristotelis, Ambrosii, Hieronymi, Anselmi, Boethii ...; 51 authors) | 17,572 (+445) | 17,183 (97.8%) | 195 | +463 | 18 |

Row-level the diff of A is +210 / -19, because 16 existing records only change their raw span (`August. ... de Spiritu et anima` becomes `Augustini ... de Spiritu et anima`); by (chunk, note, author, work) it is +194 / -3. (The gate's +196 / -4 was measured against the table before the ruling-148(a) edit.)

## The removals, all reviewed

| note | record lost | verdict |
|---|---|---|
| `bon-sent-II-d24-p1-a1-q2` n. 5 | `prosper / sententiae` (the note says the collection is Prosper's, excerpted *ex Augustini operibus*) | **WRONG**: the genitive hands the clause to Augustine and Prosper's record is lost |
| `bon-sent-IV-d15-p2-a1-q4` n. 3b | `john-damascene / orationes-de-imaginibus` (*Oratio est ascensus intellectus in Deum*) | right: the base record was a false positive (a quoted definition, not a title); lost by accident |
| `bon-sent-I-d1-dubia` n. 17 | author-only `augustine` becomes `augustine / de-diversis-quaestionibus-83` for `August. loc. cit.` | UNCLEAR: a work assigned by inheritance with no antecedent in the note |

The 16 span-only changes are benign, except two that lose locus detail (`bon-sent-II-d17-a1-q2` n. 13 `c. 36`, `bon-sent-II-d8-p2-a1-q4` n. 5 `c. II. seq.`).

## Precision, scenario A (76 of the 194 new records: all 16 Dionysius, 20 of 37 Bernard, 40 of 141 Augustine; at least 2 per volume present, the rest random, seed 7)

| form | sampled | right | wrong | unclear | precision |
|---|---|---|---|---|---|
| Dionysii | 16 | 12 | 4 | 0 | **75%** |
| Bernardi | 20 | 18 | 2 | 0 | **90%** |
| Augustini | 40 | 36 | 1 | 3 | **90%** |
| all | 76 | 66 | 7 | 3 | **86.8%** (90.4% if the 3 unclear are dropped) |

Failure shapes: (1) **Hugh of St. Victor's *Expositio in Hierarchiam* read as Dionysius' own work** (4 of the 4 Dionysius errors: `Expos. in Hierarch. caelest. S. Dionysii`); (2) a **negation** (`Hic textus non in operibus Bernardi invenitur`, `Augustinus ... falso` on *De Ecclesiasticis Dogmatibus*); (3) one **duplicate** (the same Bernard citation filed as `sermones` and `sermones-in-cantica`).

## Precision, the extra authors of scenario B (30 of the 269 extras, 3 per author, seed 5)

right 21 · wrong 3 (a note about translations of the *Metaphysics*; *in antiquis edd. operum Origenis*; *in libris Chrysostomi locum istum non invenimus*) · unclear 6: **70% (87.5% dropping unclear)**. Not recommended.

## Recommendation

**Yes to `Augustini` and `Bernardi` (measured 90% each; +178 records, nearly all right), no to `Dionysii` until Hugh's *Expositio in Hierarchiam* has its own work entry** (75%, and the errors all one shape). **No to scenario B.** Records feed the authority pages, where a wrong attribution is worse than none, so the 10% error is the cost to weigh; the failures are mostly fixable by table entries for Hugh and a `not_authorities` note rather than by dropping the genitives.

## Sample A (76)

| # | note | assigned | verdict | evidence |
|---|---|---|---|---|
| 0 | bon-sent-I-d1-a2-q1 n.28 | dionysius/de-caelesti-hierarchia  c. 7. | WRONG | …Hic loquendi modus sumtus est ex Hugonis de S. Victore *Expos. in Dionysii libr. de Caelest. Hierarch.* c. 7.… |
| 1 | bon-sent-I-d45-a2-q1 n.14 | dionysius/de-caelesti-hierarchia  c. 1. | right | …Hi duo textus sunt Dionysii, quorum prior quoad sensum depromptus est ex libro *de Caelest. Hierarch.* c. 1. e… |
| 2 | bon-sent-I-d45-a2-q1 n.14 | dionysius/de-divinis-nominibus  c. 4. | right | …Hi duo textus sunt Dionysii, quorum prior quoad sensum depromptus est ex libro *de Caelest. Hierarch.* c. 1. e… |
| 3 | bon-sent-I-d45-a2-q1 n.14 | dionysius/de-divinis-nominibus  c. 4. § 31 | right | …Hi duo textus sunt Dionysii, quorum prior quoad sensum depromptus est ex libro *de Caelest. Hierarch.* c. 1. e… |
| 4 | bon-sent-I-d46-a1-q5 n.14 | dionysius/de-divinis-nominibus  c. 4. § 20. | right | …Fide codd. F M P Q Z ff etc. nec non ed. 1 substituimus *Dionysius* pro *Boethius*, cui Vat. sententiam allata… |
| 5 | bon-sent-I-proem-q2 n.p10-2 | dionysius/de-divinis-nominibus  c. 1 | right | …tione forsan respicitur illud Dionysii de Div. Nom. c. 1: Eius quidem (… |
| 6 | bon-sent-II-d10-a2-q2 n.22 | dionysius/-  c. 3 | WRONG | …pos. in Hierarch. caelest. S. Dionysii, c. 3: « Primum *purgantur*, postea *illuminantur*, deinde *perficiuntur*. Nisi enim praecederet *purgatio*, no… |
| 7 | bon-sent-II-d22-a1-q1 n.19 | dionysius/de-divinis-nominibus  c. 4. | right | …Gen. 3, 1. — Textus seq. est Dionysii, de Div. Nom. c. 4. §§ 19. et 31. Cfr. tom. I. pag. 804, nota 6. et pag.… |
| 8 | bon-sent-III-d20-a1-q6 n.p431-1 | dionysius/de-divinis-nominibus  c. 4. § 19. | right | …Libr. XIII. de Trin. c. 10. n. 13. Vide hic lit. Magistri, c. I. — Seq. testimonium est Dionysii, de Div. Nom.… |
| 9 | bon-hex-c2 n.p339-4 | dionysius/-  c. 2 | WRONG | …sit. in Hierarch. caelest. S. Dionysii, c. 2, ubi data descriptione hierarchiarum, i. e. sacrorum principatuum, in c. 3. deinde docet, quod tres sint … |
| 10 | bon-hex-c2 n.p340-9 | dionysius/de-divinis-nominibus  c. 2. § 11 | right | …Vers. 6-10. Vulgata plura hinc inde interserit. — Inferius, opinionem sui temporis secutus, S. Bonaventura ins… |
| 11 | bon-hex-c20 n.p427-8 | dionysius/de-caelesti-hierarchia  c. 1. § 2. | right | …Cap. 43, 6. — Sententia Dionysii habetur in lib. de Caelesti Hierarch. c. 1. § 2.… |
| 12 | bon-hex-c20 n.p429-5 | dionysius/de-caelesti-hierarchia  c. 1. § 2 | right | …Haec Dionysii verba, quae a B C D omittuntur, in eius operibus non invenimus; cfr. tamen de Caelest. Hierarch.… |
| 13 | bon-red n.p325-9 | dionysius/-  lib. II. c. 1. | WRONG | …xposit. in Hierarch. caelest. Dionysii lib. II. c. 1.… |
| 14 | bon-cioan-app n.p632-4 | dionysius/de-divinis-nominibus  c. 4. § 12 | right | …In cod. A, ut supra nota 3. iam diximus, in fine Collationum in Ioannem additur *index rerum,* cui subiungitur… |
| 15 | bon-cioan-app n.p632-5 | dionysius/de-divinis-nominibus  c. 4. § 4. (cfr. Sap. 7, 26.) | right | …Ioan. 1, 5. — Sententia Dionysii habetur libr. de Div. Nom. c. 4. § 4. (cfr. Sap. 7, 26.) post quam sequitur G… |
| 16 | bon-sent-I-d17-p1-a1-q3 n.13 | bernard/de-diligendo-deo   | right | …Duo habentur inter opera S. Bernardi opuscula, quae Dei amorem respiciunt. Unum intitulatur: *de Diligendo Deo… |
| 17 | bon-sent-I-d14-dubia n.21 | bernard/epistolae   | right | …Verba ista non sunt Gregorii, sed Bernardi, qui *Epistol.* III. ad parentes suos ait: *Gustato spiritu necesse… |
| 18 | bon-sent-II-d3-p2-a3-q1 n.1 | bernard/de-diligendo-deo  c. 8 | right | …Notat P. Nicolai in ed. librorum Sent. S. Thomae, hic q. 4, hanc sententiam Bernardi colligi ex ipsius libro d… |
| 19 | bon-sent-II-d25-p2-a1-q5 n.16 | bernard/de-gratia-et-libero-arbitrio  c. 4. n. 9. | right | …Hic q. 1, ubi et sententia Bernardi, immediate ante memorata, integra redditur (sumta est ex eius libro de Gra… |
| 20 | bon-sent-III-d26-a2-q2 n.15 | bernard/sermones  68. | right | …non alienum nobis videtur, ex Bernardi Serm. 68. in Cantic. n. … |
| 21 | bon-sent-III-d3-p1-a1-q2 n.24 | bernard/epistolae  174. n. 2 | right | …Epist. II. Cor. 5, 14. — Cfr. Bernardi Epist. 174. n. 2, nec non Petri… |
| 22 | bon-sent-IV-d15-p2-a2-q2 n.12 | bernard/sermones  40. | right | …Epist. ad Fratres de Monte Dei (inter opera Bernardi), lib. I. c. 11. n. 32: Modus in omnibus habendus est; af… |
| 23 | bon-sent-IV-d17-p3-a2-q3 n.2 | bernard/de-consideratione 2 c. 13. n. 22. | right | …Vers. 18. — Verba Bernardi inveniuntur in II. de Considerat. c. 13. n. 22. Vide etiam supra d. 16. p. I. dub. … |
| 24 | bon-brev-p7-c7 n.p289-1 | bernard/sermones-in-cantica  n. 5. | right | …Epist. I. Cor. 13, 12. — Sententia Bernardi habetur in serm. 11. in Cantic. n. 5.… |
| 25 | bon-don-c2 n.p466-3 | bernard/sermones-in-cantica  n. 9 | right | …Psalm. 102, 17. — Sententia Bernardi habetur in Serm. 54. in Cantic. n. 9: *In veritate didici, nil aeque effi… |
| 26 | bon-cioan-c2 n.p549-4 | bernard/sermones  1. | right | …Vers. 4. De expositione cfr. supra n. 2. — Verba Bernardi habentur in Serm. 1. in Assumt. B. V. Mariae, n. 3.… |
| 27 | bon-cioan-c11 n.p588-7 | bernard/meditationes-piissimae  c. 3. n. 8. | right | … dein allegati inveniuntur in Meditation. piissimis de cognitione humanae conditionis (inter opera Bernardi), c. 3. n. 8.… |
| 28 | bon-sent-II-d29-a2-q1 n.2 | bernard/sermones   | WRONG | …Hic textus non in operibus Bernardi invenitur, sed in *Sermone de Symbolo contra Iudaeos, paganos et Arianos* … |
| 29 | bon-sent-IV-d3-p2-a3-q1 n.25 | bernard/sermones   | right | …(p.85, nota 4) Vers. 21. — In operibus Augustini Homilia de circumcisione non invenitur, et circumcisio Christ… |
| 30 | bon-sap-c3 n.p126-1 | bernard/sermones   | right | …Vers. 23. — Sententia prima, quae Bernardo tribuitur, et quam in ipsius operibus invenire non potuimus (cfr. t… |
| 31 | bon-sap-c5 n.p137-6 | bernard/sermones-in-cantica  serm. 2. n. 6 | right | …Vers. 27. — Verba Bernardi habentur in Serm. in Cantic. serm. 2. n. 6; in ipsis allegatur Gen. 2, 23: Hoc nunc… |
| 32 | bon-sent-II-d40-a1-q1 n.14 | bernard/de-praecepto-et-dispensatione  c. 14. n. 36. | right | …Sicut iam supra pag. 891, nota 4. diximus, haec Bernardi verba habentur in eius libro *de Praecepto et dispens… |
| 33 | bon-ioan-c14-v15-24 n.p442-6 | bernard/sermones   | right | …Vers. 49. — Cfr. Serm. 9. de Verbis Domini in Coena (inter opera Bernardi) n. 10: « *Et sermonem, quem audisti… |
| 34 | bon-don-c2 n.p466-3 | bernard/sermones  54. | WRONG | …Psalm. 102, 17. — Sententia Bernardi habetur in Serm. 54. in Cantic. n. 9: *In veritate didici, nil aeque effi… |
| 35 | bon-sap-c11 n.p184-5 | bernard/sermones   | right | …Vers. 4. — Sequitur Ioan. 15, 13. Verba Bernardi habentur in Serm. de Passione Domini in feria IV. Hebdom. san… |
| 36 | bon-sent-I-d1-dubia n.17 | augustine/de-diversis-quaestionibus-83   | UNCLEAR | …Cfr. August. loc. cit.; insuper B. Albert., hi… |
| 37 | bon-sent-I-d44-dubia n.7 | augustine/de-vera-religione  c. 14. n. 27 | right | …Haec Augustini sententia ad verbum non invenitur in eius Comment. in Gen., sed tamen erui potest ex cit. oper.… |
| 38 | bon-sent-II-d15-a1-q1 n.9 | augustine/de-genesi-ad-litteram 12 c. 16. n. 32 | right | …Vide tom. I. pag. 134, nota 10. — Verba Augustini, XII. de Gen. ad lit. c. 16. n. 32: *Spiritus omnis omni est… |
| 39 | bon-sent-II-d7-p2-a1-q2 n.5 | augustine/de-trinitate 12 c. 7. n. 12. | right | …Cfr. supra pag. 45, nota 5. — De sententia Augustini, quae paulo inferius affertur, vide XII. *de Trin.* c. 7.… |
| 40 | bon-sent-III-d26-a2-q4 n.9 | augustine/de-spiritu-et-anima  c. 3. et 4. (P. 576, n. 5.) | right | …rietur. Cfr. de hoc arg. lib. de Spiritu et anima (inter opera Augustini) c. 3. et 4. *(P. 576, n. 5.)*… |
| 41 | bon-sent-III-d6-a1-q2 n.4 | augustine/-   | right | …. De hoc ipso arg. vide verba Augustini, hic lit. Magistri, c. 3. allata, et Epist. 137. (alias 3.) c. 3. n. 11.… |
| 42 | bon-sent-IV-d14-p2-dubia n.11 | augustine/de-utilitate-credendi  c. 11. n. 25. | right | …Vide infra d. 16. p. I. dub. 9. De verbis seqq. cfr. II. Sent. d. 39. dub. 1, et Augustini, de Utilitate crede… |
| 43 | bon-sent-IV-d4-p2-dubia n.p117-2 | augustine/-   | right | …ister, deducens hoc ex verbis Augustini, hic in lit. c. 8.… |
| 44 | bon-hex-c1 n.p331-6 | augustine/de-trinitate 6 c. 10. n. 11. | right | …In Epist. Ioan. tr. 3. n. 13. iam supra pag. 324, nota 2. allegata. Sententia *aliorum* Sanctorum proposita es… |
| 45 | bon-hex-c21 n.p433-2 | augustine/de-spiritu-et-littera  c. 4. n. 6 | right | …Eph. 4, 25. — Sententia Augustini inferius posita habetur in libro de Spiritu et lit. c. 4. n. 6; verbotenus o… |
| 46 | bon-cioan-c17 n.p610-11 | augustine/manuale   | right | …Cfr. Enarrat. in Ps. 85. n. 11. 14. et 24. Vide etiam de Spiritu et anima (inter opera Augustini), c. 55. et 5… |
| 47 | bon-sap-c6 n.p148-6 | augustine/contra-academicos 1 c. 3. n. 9 | right | …Libr. I. Eruditionis didascalicae, c. 2. Cfr. supra pag. 107, nota 5. — Sententia Augustini inferius posita ha… |
| 48 | bon-sent-II-d19-a3-q1 n.6 | augustine/de-peccatorum-meritis   | right | …Hic c. 4., ubi et verba Augustini. — Seq. textus Augustini est ex l. de Peccatorum meritis et remiss. et de ba… |
| 49 | bon-sent-II-d38-a1-q4 n.3 | augustine/-   | right | …Sententia Augustini hic allata invenitur l. de Lib. Arb. c. 3. n. 8. Vide supra d. 31. a. 2. q. 3. in corp. et d. 36. a. 1. q. 2. arg. 1. ad oppos.… |
| 50 | bon-sent-II-d29-a1-q2 n.6 | augustine/epistolae  194. (alias 105.) c. 5. n. 19 | right | …Vers. 23. — Glossa hic allata apud Lyranum habetur non ad loc. cit., sed ad Eph. 1, 4, et est Augustini, in cu… |
| 51 | bon-sent-I-d46-a1-q3 n.3 | augustine/de-civitate-dei 11 c. 18. | right | …Boeth., II. *de Differentiis topicis*. Cfr. supra pag. 31, nota 1. — In textu Augustini (XI. *de Civ. Dei*, c.… |
| 52 | bon-sent-II-d35-dubia n.18 | augustine/enarrationes-in-psalmos  7. n. 19 | UNCLEAR | …Libr. IV. de Fide orthod. c. 20. Cfr. etiam II. c. 30. et Dialog. contra Manich., ubi plures definitionum pecc… |
| 53 | bon-sent-I-d42-a1-q3 n.12 | augustine/de-genesi-ad-litteram 6 c. 18. n. 29. | right | …Sententia citata invenitur in libro sententiarum Prosperi Aquitani ex operibus Augustini excerptarum, sub n. 2… |
| 54 | bon-sent-II-d38-a1-q2 n.13 | augustine/enchiridion  c. 121. n. 32. | right | …Hic c. 1, ubi etiam verba Apostoli et Augustini (Enchirid. c. 121. n. 32.) habentur.… |
| 55 | bon-sent-II-d23-a2-q3 n.26 | augustine/de-trinitate  c. 9. n. 16. | right | …pist. I. Cor. 13, 12. — Verba Augustini, loc. cit. c. 9. n. 16. sunt: *Sicut nomine speculi imaginem voluit intelligi, ita nomine aenigmatis quamvis s… |
| 56 | bon-sent-II-d36-a3-q1 n.14 | augustine/de-genesi-ad-litteram 6  | right | …Cfr. verba Augustini, ex VI. de Gen. ad lit. supra pag. 435, nota 1. et pag. 437, nota 3. allata. — Mox pro *e… |
| 57 | bon-sent-IV-d21-p1-littera n.6 | augustine/enarrationes-in-psalmos  37. n. 3 | right | …Haec et quae sequuntur sumta sunt ex longiore Glossa loc. cit. et apud Lombard. ibid., quae collecta est ex Au… |
| 58 | bon-sent-III-d26-dubia n.p583-4 | augustine/soliloquia 1  | right | …Etiam B. Albert., hic a. 1, hanc definitionem ut in August. libro de Civ. Dei occurrentem memorat. In Suppleme… |
| 59 | bon-sent-II-d12-a1-q2 n.3 | augustine/de-genesi-ad-litteram 4 c. 33. n. 52. seqq. | right | …Vers. 10. — Sententiam Augustini vide IV. *de Gen. ad lit.* c. 33. n. 52. seqq.; V. c. 3. n. 5. seqq. et c. 23… |
| 60 | bon-sent-I-d40-a1-q1 n.3 | augustine/de-praedestinatione-sanctorum  c. 17. n. 34 | right | …Definitio haec est etiam Augustini, *de Praedest. Sanctor.* c. 17. n. 34, et fundatur in verbis Apostoli ad Ro… |
| 61 | bon-sap-c6 n.p150-8 | augustine/de-doctrina-christiana 4 c. 11. n. 26. | right | …Vers. 31; ibid. 37, 20. est seq. locus. — Sententia Augustini habetur IV. de Doctr. christiana, c. 11. n. 26.… |
| 62 | bon-eccl-prooem n.p6-7 | augustine/sermones  385. (alias 38. inter 50 Homil.) c. 5. n. 6. seq. | right | …De Arrha animae (ubi etiam seq. distinctio amoris insinuatur), ex quo opusculo plura iisdem verbis habentur in… |
| 63 | bon-sent-III-d1-littera n.9 | augustine/contra-sermonem-arianorum  c. 4. n. 4. | right | …Ed. 1 bene *indivisibilis*, cod. C *non dissimilis.* Quoad doctrinam Vide Augustini librum contra Sermonem Ari… |
| 64 | bon-sent-II-d12-a1-q2 n.3 | augustine/de-civitate-dei 11 c. 6. seq. | right | …Vers. 10. — Sententiam Augustini vide IV. *de Gen. ad lit.* c. 33. n. 52. seqq.; V. c. 3. n. 5. seqq. et c. 23… |
| 65 | bon-sent-II-d27-a2-q2 n.7 | augustine/-   | right | …*Quaest. praeced.* — Verba Augustini, hic ex IV. *de Trin.* c. 1. n. 2. citata, integra haec sunt: *Pluviam quippe voluntariam* (Ps. 67, 10.) *non nis… |
| 66 | bon-sent-I-d40-a1-q1 n.2 | augustine/de-dono-perseverantiae  c. 14. n. 35. | right | …Haec definitio est Augustini, *de Dono persev.* c. 14. n. 35. Cfr. q. seq. in corp. — Cod. B voci *beneficioru… |
| 67 | bon-sent-II-d35-dubia n.18 | augustine/de-civitate-dei 11 c. 9. | UNCLEAR | …Libr. IV. de Fide orthod. c. 20. Cfr. etiam II. c. 30. et Dialog. contra Manich., ubi plures definitionum pecc… |
| 68 | bon-sent-III-d29-dubia n.p652-9 | augustine/de-doctrina-christiana  c. 23. n. 22 | right | …Cui Magister haec verba tribuit. — De sententia Augustini, prolata l. de Doctr. christ. c. 23. n. 22, vide hic… |
| 69 | bon-sent-I-d31-p2-a2-q1 n.5 | augustine/de-trinitate 4 c. 9 | right | …Vers. 30. — Rationem Augustini, quae hic respicitur, vides hic in *lit. Magistri*, c. 4. Cfr. etiam IV. *de Tr… |
| 70 | bon-sent-II-d37-a1-q2 n.6 | augustine/de-natura-boni   | right | …Vers. 4. — Verba, quae hic ut ex Augustini libro de Natura boni desumta signantur, ibi non habentur. In libro … |
| 71 | bon-sent-I-d3-p2-a1-q2 n.19 | augustine/de-trinitate 12  | right | …Augustini opinionem de trinitate in potentiis animae ad inferiora conversis vide XII. *de Trin.*, et de trinit… |
| 72 | bon-sent-II-d8-littera n.13 | augustine/de-ecclesiasticis-dogmatibus   | WRONG | …*De Ecclesiasticis Dogmatibus* c. 50. — Vat. et ed. 4 verbis *in libro de Ecclesiasticis Dogmatibus* praefigun… |
| 73 | bon-sent-II-d13-dubia n.20 | augustine/enarrationes-in-psalmos   | right | …ssa mox allegata sumta est ex Augustini Enarratione in hunc Psalmu… |
| 74 | bon-sent-II-d32-a1-q2 n.16 | augustine/contra-iulianum 6  | right | …Cod. cc et ed. 1 adiiciunt *et.* — Cfr. August., loc. cit. c. 27. n. 43. seqq. — Augustini exemplificatio infr… |
| 75 | bon-qmt-q5-a1 n.p90-3 | augustine/de-trinitate 4 c. 20. n. 28. | right | …Ut dicit Aristot., supra pag. 21, nota 8. allegatus. — Verba Augustini paulo inferius adducta inveniuntur in I… |

## Sample B extras (30)

| # | note | assigned | verdict | evidence |
|---|---|---|---|---|
| 0 | bon-sent-IV-d45-a1-q2 n.p941-4 | gregory-the-great/dialogi 4 c. 25. | UNCLEAR | …Vers. 1: *Scimus enim, quoniam, si terrestris domus nostra huius habitationis dissolvatur, quod aedificationem… |
| 1 | bon-serm-s1 n.p535-4 | gregory-the-great/homiliae-in-evangelia 2 homil. 12. n. 1. | right | …Cfr. Matth. 13, 24. 31. 33. 44. 47; 22, 2; 25, 1. — Locus Gregorii est II. Homil. in Evang. homil. 12. n. 1.… |
| 2 | bon-sap-c19 n.p231-10 | gregory-the-great/homiliae-in-evangelia 2 homil. 23. n. 1. | right | …Vers. 3. — Sequitur Luc. 24, 29. Sententia Gregorii habetur in II. Homil. in Evang. homil. 23. n. 1.… |
| 3 | bon-sent-I-d29-a1-q1 n.3 | aristotle/topica 4 c. 1 | right | …Codd. aa bb addunt *secundum Philosophum*. — Verba Philosophi integra invenies supra pag. 215, nota 9. Cfr. et… |
| 4 | bon-sent-II-d29-a1-q2 n.3 | aristotle/physica 7 text. 18. (c. 3.) | right | …Deut. 32, 4. — Dictum Aristotelis, quod hic secundum antiquam translationem affertur, habetur VII. *Phys.* tex… |
| 5 | bon-sent-II-d1-p1-dubia n.14 | aristotle/metaphysica   | WRONG | …Aetate media duae versiones librorum *Metaphysicorum* Aristotelis vulgo in usu erant, nempe Graeco-latina et A… |
| 6 | bon-sent-IV-d18-p1-littera n.8 | ambrose/in-lucam  libr. VI. n. 109 | right | …[Locus Ambrosii continuatur ex Exposit. in Evang. Lucae libr. VI. n. 109, nota praecedente cit.; sententia « I… |
| 7 | bon-sent-II-d13-littera n.5 | ambrose/-  hom. 1. libr. I. c. 9. n. 33 | right | …d exemplum ponitur in Hexaëm. Ambrosii, hom. 1. libr. I. c. 9. n. 33, et Basilii, hom. … |
| 8 | bon-sent-II-d43-a1-q1 n.6 | ambrose/-   | right | …mbol. Athanas. nec non dictum Ambrosii hic in lit. Magistri, in fine, allatum. Specialiter contra *personam* Spiritus S. peccari potest vel per *infid… |
| 9 | bon-sent-II-d39-a2-q1 n.2 | jerome/in-ezechielem  1, 7. | right | …Vers. 10. — Glossa, cuius verba alludunt ad Rom. 8, 26, habetur apud Lyranum et sumta est ex Hieronymi Expos. … |
| 10 | bon-sent-III-d3-p1-a2-q3 n.16 | jerome/in-matthaeum  1, 3 | UNCLEAR | …Cfr. Damasc., Homil. 1. in Dormition. B. M. V. n. 10, (ubi etiam transitum B. Virginis non mortem, sed somnum,… |
| 11 | bon-sent-III-d5-a1-q5 n.6 | jerome/-   | right | …Vide verba Hieronymi hic in lit. Magistri, c. 1, circa medium, insuper locum Damasceni, sup… |
| 12 | bon-sent-II-d41-a1-q3 n.15 | anselm/meditationes  medit. 2. | UNCLEAR | …In opusculo a Gaufrido, Bernardi discipulo, composito et inscripto « Declamationes ex S. Bernardi sermonibus »… |
| 13 | bon-sent-IV-d17-p1-a1-q4 n.1 | anselm/de-veritate  c. 12. | right | …Vers. 13. — Definitio iustitiae inferius allata est Anselmi, Dialog. de veritate, c. 12.… |
| 14 | bon-sent-II-d3-p2-a1-q1 n.7 | anselm/de-casu-diaboli  c. 11 | right | …Vide infra d. 12. a. 1. q. 2. — Verba Anselmi, de Casu diaboli, c. 11, sunt: *Malum non est aliud quam non bon… |
| 15 | bon-sent-IV-d17-p3-a2-q3 n.3 | boethius/de-differentiis-topicis 4  | UNCLEAR | …Formata est haec definitio ex doctrina Ciceronis, I. Rhetor. c. 5. et 23. seqq. Vide supra pag. 400, nota 1, u… |
| 16 | bon-sent-II-d1-p1-a3-q1 n.17 | boethius/de-consolatione 3  | UNCLEAR | …Aristoteles, VIII. *Phys.* text. 34. seqq. (c. 5.) generaliter probat, omnem motum procedere ab immobili, sive… |
| 17 | bon-sent-I-d13-a1-q4 n.2 | boethius/-   | right | ….* c. 1. (c. 10.) et Comment. Boethii in hunc locum, ubi ait: *Idem enim valet ad intelligentiam quod dicitur «iniustus», tanquam si dicatur «non iust… |
| 18 | bon-sent-II-d40-a2-q3 n.2 | origen/-  homil. I. | right | …. — Glossa, quae sumta est ex Origenis homil. I. in Iudic. n. 3, habetur apud Strabum et Lyr… |
| 19 | bon-qsc-q4 n.p18-6 | origen/homiliae   | WRONG | …In antiquis edd. operum Origenis v. g. Parisiensis, impressa a Ioan. Parvo (circa annum 1512) tom. III, habent… |
| 20 | bon-sent-I-d6-a1-q2 n.10 | origen/in-ioannem  tom. II. | right | …Haec verba referuntur a Pamphylo Martyre inter fragmenta Origenis *Comment. in Ioan.* tom. II. sub n. 30. ed. … |
| 21 | bon-sent-III-d10-a1-q3 n.p229-8 | john-damascene/de-fide-orthodoxa 3 c. 11. | right | …Dist. 6. a. 1. q. 3. — De dicto Damasceni (III. de Fide orthod. c. 11.) vide supra pag. 15, nota 5.… |
| 22 | bon-sent-III-d5-a2-q2 n.1 | john-damascene/de-fide-orthodoxa 3 c. 11. | right | …In libro de Una Persona et duabus naturis, c. 3. — Dictum Damasceni habetur III. de Fide orthod. c. 11. Cfr. q… |
| 23 | bon-sent-III-d3-p1-a2-q3 n.5 | john-damascene/de-fide-orthodoxa 4 c. 14. | right | …Vers. 35. — Dictum Damasceni, quod habetur in eius IV. de Fide orthod. c. 14., et simile est sententiae a Cyri… |
| 24 | bon-sent-III-d14-a1-q3 n.p303-1 | john-chrysostom/in-ioannem  n. 1. | right | …Vers. 18. Cfr. I. Ioan. 4, 12. — Verba Chrysostomi inveniuntur in eius homil. 15. (alias 14.) in Ioan. n. 1. C… |
| 25 | bon-sent-II-d42-littera n.12 | john-chrysostom/in-ioannem   | WRONG | …Est in Glossa apud Lyranum, Deut. 23. 23. In libris Chrysostomi locum istum non invenimus, sed in Ioan. Cassia… |
| 26 | bon-sent-IV-d5-dubia n.p132-4 | john-chrysostom/in-ioannem  1, 31. | UNCLEAR | …Exposit. in Evang. secundum Ioan. (inter opera), ubi ad 1, 33. ait: « *Et ego nesciebam eum,* ostendit Ioannes… |
| 27 | bon-brev-p6-c12 n.p278-1 | isidore/etymologiae 7 c. 12. n. 3 | right | …Psalm. 15, 5. — Sententia Isidori invenitur in VII. Etymolog. c. 12. n. 3; II. de Offic. ecclesiast. c. 12. et… |
| 28 | bon-sap-c13 n.p193-9 | isidore/sententiae 1 c. 4. n. 2 | right | …Vers. 32. Cfr. Breviloq. p. II. c. 11. et 12. (tom. V. pag. 229 seq.). — Seq. sententia Isidori habetur in I. … |
| 29 | bon-sent-IV-d33-a1-q1 n.p748-1 | isidore/etymologiae 5 c. 2 | right | …Introduct. d. 1, ubi Gratian. sententiam Isidori, V. Etymolog. c. 2, his verbis complectitur.… |
