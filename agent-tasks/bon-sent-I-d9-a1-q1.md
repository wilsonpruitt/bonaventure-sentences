# Agent Task: bon-sent-I-d9-a1-q1

## Target output

Write the completed Tier-2 chunk to `vol1/bon-sent-I-d9-a1-q1.md`, replacing the existing file.
Preserve the YAML front matter exactly. Replace `[Translation pending]` and
`[Notes pending]` placeholders with translated content. Add `### Apparatus`
section if the Latin body contains footnote markers.

## Front matter (preserve verbatim)

```yaml
id: "bon-sent-I-d9-a1-q1"
volume: 1
book: 1
distinctio: 9
articulus: 1
quaestio: 1
type: quaestio
title: "I Sent., d. 9, a. unicus, q. 1"
line_start: 36135
line_end: 36546
word_count_latin: 2542
boundary_note: "2026-04-14: ARTICULUS UNICUS intro + QUAESTIO I. (a1 = articulus unicus per project naming.)"
```

## Tier-2 standard

Per `feedback_bonaventure-translation-depth.md`: literal translation, not
paraphrase. Translate ALL scholion and apparatus content fully (do NOT mark
as `[Scholion omitted]` — the legacy prompt's instruction to skip them is
superseded). Preserve every Quaracchi citation in full form.

Output structure (h2 sentinel headings, parser-required):

```
## Latin
<full Latin body, paragraph-for-paragraph>

## English
<full English translation, paragraph-for-paragraph parallel>

## Apparatus
[^1] **La.** <Latin apparatus text> — **En.** <English translation>
[^2] **La.** ... — **En.** ...

## Notes
<editorial notes, cross-references, doctrinal flags>
```

Inline footnote markers `[^N]` must appear in BOTH the Latin and English
bodies at matching positions. Scholion content lives inside the body blocks
as `### Scholion` subsections.

## Translation prompt (apply this)

# Bonaventure Sentences — Translation Prompt for Sonnet

Use this prompt for bulk translation. Paste the Latin text from a chunk's `### Latin` section where indicated.

---

```
You are translating St. Bonaventure's Commentary on the Sentences of Peter Lombard (Quaracchi critical edition, 1882) from Latin to English. This is a scholastic theological text from the 13th century.

## Critical Instructions

- Translate ALL Latin text provided, even if it begins mid-sentence or mid-argument. Do not skip, summarize, or reorganize any content. The chunks may start or end mid-quaestio — translate exactly what is given.
- Produce paragraph-for-paragraph parallel translation. Each Latin paragraph should have a corresponding English paragraph in the same order.
- Do NOT add editorial markup (bold headers, section labels, inline source citations) that does not appear in the Latin. Preserve only the structural markers that appear in the source (e.g., DIST., ART., QUAEST., CONCLUSIO, numbers like 1., 2., 3.).
- Do NOT identify or cite sources beyond what the Latin text itself states. If the Latin says "Augustinus in Soliloquiis," translate that reference as-is. Do not add "[De Trinitate IX.4.5]" or similar editorial additions.
- The critical apparatus (footnotes at the bottom referencing manuscript variants like "Vat. cum cod. cc") should be noted as "[Critical apparatus omitted]" — do not translate it line by line.
- The scholion sections (marked SCHOLION or SCHOLIOK in OCR) should be noted as "[Scholion omitted]" — these are Quaracchi editorial commentary, not Bonaventure's text.

## Translation Style

- Formal academic English suitable for theological scholarship
- Translate standard scholastic formulae consistently:
  - *Videtur quod...* → "It seems that..."
  - *Sed contra* / *Contra* → "On the contrary"
  - *Respondeo dicendum quod...* → "I respond: It must be said that..."
  - *Ad primum/secundum/tertium...* → "To the first/second/third [objection]..."
  - *Praeterea* / *Item* → "Likewise"
  - *Ergo* → "Therefore"
  - *Dicendum quod...* → "It must be said that..."

## Key Terminology (translate consistently)

- *esse* → being / existence (context-dependent)
- *essentia* → essence
- *substantia* → substance
- *forma* → form
- *materia* → matter
- *potentia* → potency / power (context-dependent)
- *actus* → act / actuality
- *ratio* → account / ground / formal character (context-dependent)
- *intellectus* → intellect / understanding
- *voluntas* → will
- *caritas* → charity
- *gratia* → grace
- *exemplar* → exemplar
- *illuminatio* → illumination
- *vestigium* → vestige / trace
- *imago* → image
- *similitudo* → likeness
- *processio* → procession
- *suppositum* → supposit

## OCR Notes

The Latin comes from OCR of 1882 typography. Common artifacts:
- Broken words across lines (e.g., *ehci-tus* = *elicitus*)
- Garbled marginal glosses inline (e.g., *Fundameata.invicem* = marginal note bleeding into text)
- Letter substitutions (*ahquid* = *aliquid*, *ahud* = *aliud*)
- Inline footnote numbers

Silently correct obvious OCR errors. Only note genuinely ambiguous readings.

## Output Format

Produce exactly two sections:

### English

[Full paragraph-for-paragraph translation of ALL provided Latin text]

### Notes

[Brief notes: genuinely ambiguous passages, key translation decisions, important theological context. 5-10 bullet points maximum.]

---

## Latin Text

[PASTE LATIN HERE]
```


## Latin body to translate

```
ARTICULUS    UNICUS. 


De  generationo  in 
QUAESTIO  I. 


Utruni  in  divinis  generatio  ponenda  sit. 


Circa  primum,  quod  generatio  sit  in  divinis, 
ostenditur^: 

1.  Primo  a  minori.  Multo  fortius  debet  esse 
generatio  in  eo  qui  generationem  aliis  tribuit,  quain 
in  his  quae  recipiunt;  sed  generatio  est  in  creatu- 
ris:  ergo  et  in  Deo  qui  tribuit.  Et  hoc  est  quod 
dicitur  Isaiae  ultimo^:  Si  ego  generationem  aliis 
Irihuo ,  sterilis  ero  ?  dicit  Dominus,  quasi  dicat,  non. 

2.  Item,  ostenditur  illud  idem  a.  posteriori.  Per 
prius  enim  est  paternitas  in  Deo  quam  in  creatura; 
sed  paternitas  et  generatio  vere  est  in  creatura: 
ergo  et  in  Deo.  Quod  prius  sit  ibi ,  dicit  Apostolus 
ad  Ephesios  tertio^:  Ex  quo  omnis  paternitas  in 
caelo  et  in  terra  nominatur. 

3.  Item,  ostenditur  hoc  ipsum  a  simili,  quia 
omne  quod  perfectionis  est,  attribuendum  est  Deo, 
in  quo  est  summa  omnis  perfectionis ;  sed  generatio 
est  perfectionis  in  creatura,  ut  vult  Philosophus% 
quia  «perfectum  est  quod  potest  generare  quale 
ipsum  est»:  ergo  etc. 

4.  Item ,  illud  idem  ostenditur  alia  ratione 
sic  ^ :  divina  natura  est  summe  bona  et  actualis- 
sima:  ergo  summe  potest  et  vult  se  communicare; 
sed  prima  et  summa  ratio  communicandi  est  in  ge- 
neratione :  ergo  necesse  est  in  divinis  ponere  gene- 
rationem. 


CoNTRA :  1 .  Generatio  in  creaturis  aut  est  per-  m  , 
fectionis ,  aut  impe^'fectionis.  Si  perfectionis ,  tunc 
ergo,  cum  substantiae  spirituales  et  incorporales 
sint  nobilissimae ,  debet  in  eis  generatio  esse:  ergo 
cum  non  sit  in  eis ,  non  est  nobilitatis ;  sed  quod  non 
est  nobilitatis  non  est  in  Deo:  ergo  etc. 

2.  Item ,  ubi  est  generatio ,  ibi  est  variatio ;  ge- 
neratio  enlm  est  species  motus ,  et  inter  omnes  spe- 
cies  motus  maior  est  variatio  in  motu  secundmn 
substantiam,  quia  est  entis  in  potentia,  minor  in 
motu  secundum  locum ' :  ergo  cum  in  Deo  non  sit 
variatio  nec  aliqua  species  motus,  etiam  illa  quae 
minima  est,  ut  loci  mutatio:  ergo  nec  generatio. 

3.  Item,  ubi  est  generatio,  ibi  est  corruptio, 
unde  Philosophus  '  dicit ,  quod  ><  propter  longe  stare 
a  principio  reliquo  modo  complevit  esse  Deus,  con- 
tinuam  in  his  faciens  generationem » ;  et  huiusmodi 
signum  est,  quod  sola  corruptibilia  generant  et  ge- 
nerantur  in  creaturis;  sed  in  Deo  nulla  cadit  cor- 
ruptio:  ergo  nec  generatio. 

4.  Item,  ubi  est  generatio,  ibi  est»  nutritio; 
unde  ad  tot  et  plures  se  extendit  vis  nutritiva 
quam  generativa;  sed  in  Deo  non  est  vis  nutritiva: 
ergo  nec  generativa,  ergo  nec  nutritio,  nec  gene- 
ratio:  ergo  generatio  non  est  in  divinis. 


1  Auctoritate  plurimorum  mss.  et  ed.  I  expunximus  liic 
additum  ponenda. 

2  Cod.  W  addit  sic. 

3  Vers.  9 ,  ubi  Vulgata  loco  aliis  ponit  cetetis  et  pro 
dicii  liabet  ail. 

*  Vers.  1 5,  in  quo  textu  Vulgata  caelis  loco  caelo.  —  Paulo 
ante  ed.  1  per  prius  pro  prius. 

5  Libr.  II.  de  Anima ,  text.  34.  (c.  4.)  et  IV.  Meteor.  text. 
19.  (c.  3.). 

"  Vat.  cum  cod.  cc  omittit  sic,  et  pro  alia  ratione  ponit 
ilkt  ratione,  sed  obest  auctoritas  aliorum  mss.  et  ed.  1. 

'  Vide  Aristot.,  V.  Phys.  text.  7.  seqq.  et  VIH.  text.  53. 
seqq.  (e.  7.). 


*  Libr.  II.  de  Gener.  et  corrupt.  text.  59.  secundum  transl. 
arabico-latinam.  In  ed.  vero  Paris.  c.  10.  ita  exhibetur:  Hoe 
vero  (esse  sive  existere)  in  omnibus  inesse  impossibile  sit , 
propterea  quod  longe  ab  ipso  principio  distent;  reliquo  modo 
Deus  ipse  universum  complevit,  continua  facta  generatione. 
Vide  etiam  II.  de  Anima,  text.  33.  (c.  4.). —  Vat.  loco  Philo- 
sophus  ponit  Auctor  de  causis,  sed  falso  et  contra  omnes 
mss. ,  quorum  pauci  ut  H  1 0  indicant  etiam  locum  addendo 
in  Hbro  de  Gerierat.  et  corruptione,  et  plures  primo  ponunt  pro 
principio.  Mox  nonnulli  codd.  ut  HT  ee  ff  cum  ed.  1  quia 
loeo  qnod. 

8  Fide  antiquiorum  mss.  et  ed.  1  adiecimus  est.  —  Vide 
Aristot.  ,  II.  de  Anima  ,  text.  42.  seqq.  (c.  4.). 


DIST.  IX.  ART.  UNICUS  QUAEST.  I. 


181 


CONCLUSIO. 


Generatio  ponenda  est  in  divinis,  cuius  congruitas 
ei  modtis  explicatur. 

Respondeo  :  Dicendum ,  quod  generatio  ponenda 
conciusio  est  in  divino  esse '. 

4)rincipais.  ^^  huius   Tatio   potissima   est,  ut  credo,  quia 

Raiio  po-  omnis  natura  est  communicabilis ;  et  quia  in  Deo 
propter  sui  nobililatem  est  aptitudo  actui  coniuncta, 
immo  ipse  actus,  oportet  quod  natura  sit  pluribus 
communicata;  sed  non  possunt  esse  plures  ab  una 
natura ,  quin  unus  sit  ab  alio ,  vel  ambo  a  tertio : 
ergo  cum  ante  divinas  personas  nihil  sit,  oportet 
quod  una  sit  ab  alia.  Et  quoniam  sunt  conformes 
in  natura ,  et  generatio  est  emanatio  secundum  con- 
formitatem  naturae:  ideo  credo,  quod  necesse  est  in 
divinis  ponere  generationem. 

Ut  autem  intelligatur,  per  quem  modum,  no- 
tandum ,  quod  generare  de  sui  propria  ratione  est 
similem  sibi  in  substantia  et  natura  producere  ^  Sibi 
Tripiex  ge-  vero  similem  contingit  produci  triphciter  " :  aut  per 
impressionem  suae  similitudinis  in  alio;  et  sic  ge- 
neratur  character  a  sigillo,  lumen  a  luminoso,  spe- 
cies  ab  obiecto;  alio  modo  per  eductionem  speciei 
consimilis  ab  alio;  et  sic  generatur  elementum  ab 
elemento;  tertio  modo  per  productionem  similis 
de  simili  sive  de  se  ipso ;  et  sic  generatur  animatum 
ab  animato;  et  isle  tertius  modus  est  perfectior, 
unde  non  reperitur  nisi  in  substantiis  habentibus 
forraam  nobilem ,  quae  est  vita  \  Et  iste  modus  ge- 
DiiTen  ge-  nerationis  est  secundum  nascentiam  et  est  in  Deo  et  * 

De""°et  iS  creaturis,  sed   differenter ;   quia  producere  alium 

"AJia"disiin- ex  se  ipso   potest   esse  dupliciter,  vel  ex  se   toto , 

«misf '"'"'"  vel  ex  parte  sui. 

Ex  se  toto  non  potest  producere  nisi  ille, 
cuius  essentia  potest  esse  in  pluribus  una  et  tota.  Nam 
si  non  potest  esse  in  pluribus  una  et  tota ,  si  gene- 
rans  dat  totam  suam  substantiam  generato,  tunc 
substantia  tota  transit  in  generatum%  et  generans 
perdit  substantiam  totam  generando ,  quod  esse  non 
potest.  Ideo  ad  hoc  necesse  est,  quod  taiem  habeat 


substantiam ,  quae  una  et  tota  sit  in  pluribus.  Talis 
autem  substantia  non  est  nisi  substantia  habens  sum- 
mam  simplicitatem ;  haec  autem  est  sola  divina  es- 
sentia ',  in  qua  propter  summam  simplicitatem  sup- 
positum  non  addit  ad  essentiam,  unde  nec  ipsam 
coarctat  nec  limitat  nec  formam  multiplicat.  Et  ideo 
in  ea'  potest  esse  generatio  communicans  eandem 
substantiam  totam;  et  talis  generatio  est  omnimodae  conoiusio  a. 
perfectionis  et'in  solo  Deo  reperitur,  ratione  iam  dicta. 

Alio  modo  contingit  aliquem  ex  se  producere. 
quantum  ad  partem  sui.  Sic  pater  naturalis  ge- 
nerat  filium ,  partem  substantiae  transmittendo  et 
decidendo'.  Et  haec  generatio  necessario  est  cum 
transmutatione ;  quia  enim  pars  decisa  non  habet 
actum  totius,  necesse  est,  quod  per  mutationem 
acquirat;  sed  quod  acquirit  quod  non  habet,  va- 
riatur ;  ideo  haec  generatio  est  mutatio  et  habet 
variationem  coniunctam.  Est  etiam  cum  corrup- 
tione  annexa ;  quia  enim  aliqua  pars  generantis  de- 
perditur,  generans  est,  a  quo  potest  fieri  ablatio 
et  ita  corruptio.  Est  etiam  cum  conservatione"'  adiun- 
cta ;  quia  enim  fit  deperditio ,  necesse  est  quod  per 
nutrimentum  flat  restauratio.  Et  ideo  generatio  in 
creatura  et  perfectionis  et  imperfectionis  est:  perfe- 
ctionis  a  parte  virtutis  producentis ,  imperfectionis  a 
parte  subiecti  divisibilis.  Et  ideo  est  in  solis  ani- 
matis ,  quae  habent  formam  perfectionis ,  ipsam  sci- 
licet  "  animam,  et  corpus  defectibile  et  restaurabile. 

Generatio  vero  in  divinis  est  omnimodae  per- 
fectionis.  Quia''  enim  non  est  ex  parte,  ideo  est, 
quod  habet  actu  speciem.  Et  ideo  nec  ibi  est  in 
natura  imperfectio  nec  variatio,  quia  nihil  novum 
acquiritur;  nec  corruptio,  quia  nihil  adimitur;  nec 
nulritio,  quia  nihil "  restituitur. 

Et  ex  hoc  patet  solutio  obiectorum;  quia  geiie-  ^ 
ratio  '*  de  toto  est  tantae  perfectionis ,  quod  non  po- ' 
test  esse  in  creatura  aliqua;  generatio  vero  ex  parte 
tantam  habet  imperfectionem  coniunctam  ",  ut  non 
possit  esse  circa  substantiam  invariabilem  et  incor- 
ruptibilem  et  simplicem ,  non  solum  in  natura  increata, 
verum  etiam  in  creata.  Aliae  rationes  probant  de 
generatione  quae  est  ex  parte. 


divinac    ge- 


•  Ex  codd.  et  ed.  1  subslituimus  divino  esse  pro  divinis , 
deinde  supplevimus  particulam  Et.  Mox  post  credo  codd.  H I 
quia  in  divinis  et  ed.  I  qnia  Dei  loco  quia  omnis. 

2  Vide  Aristot. ,  II.  de  Anima ,  text.  34.  (c.  4.);  VII.  Metaph. 
text.  22.  et  28.  (VI.  c.  7.  et  8.). 

5  Vat.  cum  cod.  cc ,  antiquioribus  autem  mss.  et  ed.  1 
refragantibus ,  in  natura  producere  tnpliciter  est  loco  contin- 
git  produci  tripliciter. 

*  Hinc  et  generatio  sub  hoc  respectu  communiter  deflni- 
tur :  origo  viventis  a  vivente  ut  principio  coniuncto  in  similitu- 
dinem  naturae. 

5  Aliqui  codd.  ut  X  Z  repetunt  hic  in. 

fi  Cod.  R  et  est  in  generato  pro  m  generatum.  Paulo  post 
mendum  Vat.  adhuc  loco  ad  hoc  correximus  ex  mss. 

'  Ed.  1  substantia.  Mox  post  suppositum  cod.  R  nihil 
loco  non ,  et  paulo  infra  cod.  V  ipsam  praemittit  verbo  li- 
mitat. 


'  Fide  plurimorum  mss.  el  ed.  1  substituimus  ea  pro  eo , 
quod  ponitur  in  Vat. 

^  Ope  plurimorum  mss.  et  ed.  1  exhibemus  deddendo  loco 
descindendo ,  quod  non  ita  bene  subnexo  verbo  decisa  corre- 
spondet.  Mox  cod.  T  causa  transmutabiHtatis  pro  cum  trans- 
mutalione. 

1"  Nempe :  conservatione  passive  sumla.  —  Antiquam  lectio- 
nem  plurimorum  mss.  et  sex  primarum  edd.  reslituimus  pro  con- 
versione  ponendo  conservatione  ;  utriusque  lectionis  idem  sensus. 
Pro  lectione  mss.  stat  Aristot. ,  II.  de  Anima,  text.  47.  (c.  4.). 

"  Ita  mss.  cum  ed.  1  ,  dum  Vat.  hic  id  est  pro  ipsam 
scilicei  habet  et  mox  ipsum  scilicet  praemittit  nomini  corpus. 

1''  Consentientibus  mss.  et  ed.  1  ,  commutavimus  in  hac 
propositione  Quod  in  Quia  et  deinde  quia  in  quod. 

>3  Ed.  1  addit  restauratur  vel. 

"  Cod.  bb  adiicit  quae  est 

'5  Vat. ,  obnitenUbus  mss.  et  ed.  1  ,  adiunctam. 


SENTENTIARUM  LIB.  I. 


SCHOLIOK 


I.  Obiectiones  iam  in  corp.  solutae  sunt,  Quoad  Angelos 
patet,  quod  nullam  habere  possunt  generaUonem  :  non  generatio- 
nem  imperfectam,  quae  est  ex  parte ,  propter  siniplicitatem  sub- 
stantiae  angelicae ;  non  perfectam ,  quae  est  ex  toto ,  quia  eorum 
natura  est  flnita.  —  Quoad  argumenta  congruentiae ,  quae  suppo- 
sito  fidei  dogmate  hic  alTerunlur,  cfr.  supra  d.  2.  q.  2;  d.  5.  q.  2; 
dub.  3.  10.  liuius  d. ;  Breviloq.  p.  1.  c.  3 ;  Hexaem.  Serm.  II. 
—  Alex.  Hal. ,  S.  p.  I.  q.  i2.  m.  1.  2.  —  Scot.,  I.  Sent.  d.  2. 


q.  6.  7.  —  S.  Thom. ,  I.  Sent.  d.  K.  q.   I .  a.   I  ;  S.  I.  q.  27.  a_ 

1.  2;  S.  c.  Gent.  IV.  c.  10.  11.  —  B.  Albert. ,   I.    Sent.  d.  4. 

a.  3 ;  S.  I.  tr.  7.  q.  30.   m.  1.  —  Petr.  a  Tar. ,  I.  Sent.  d.  4. 
q.  1.  —  Richard.  a  Med. ,  hic  a.  1.  q.  1.  —  /Egid.  R. ,  I.  Scnt.. 

d.  4.  1.  princ.  q.  1.  —  Henr.  Gand. ,  S.  a.  58.  q.  1.  n.  8-24. 

—  Durand. ,  I.  Sent.  d.   4.   q.  1.  —  Dionys.  Carth. ,   I.  Scnl. 
d.  4.  q.  1 .  —  Biel ,  hic  q.  1  ;  d.  1 0.  q.  1 .  prop.  1 . 


QU.VESTIO  II. 

Utrum  in  divinis  generatio  distinguat  inter  gignentem  et  genitum. 


Secundo  quaeritur,  utrum  generatio  in  divinis 
sit  personarum  distinctiva.  Et  quod  sic,  ostenditur 
hoc  modo. 

1.  Augustinus  circa  principium  de  Trinitate  ': 
Fundamenui. « Nulla  res  Bst ,  quae  se  ipsam  gignat,  ut  sit»:  si 

ergo  gignit,  aliam  gignit;  sed  inter  aliam  et  aliam 
est  distinctio:  ergo  etc. 

2.  Item,  generatio  est  emanatio;  sed  ubi  est 
emanatio,  ibi  est  multiplicatio  sive  plurificatio;  ubi 
autem  multiplicatio  ,  ibi '  distinctio :  ergo  ubi  gene- 
ratio ,  ibi  necessario  est  distinctio. 

3.  Item ,  generatio  in  divinis  est  relatio ' ;  sed 
relatio  importat  respectum  et  ordinem ;  sed  ubi  re- 
spectus  et  ordo,  ibi  suppositorum  et  relatorum  sive 
ordinatorum  distinctio:  et  sic  etc. 

4.  Item ,  maior  *  diversitas  sustinetur  a  suppo- 
sito  vel  in  supposito  composito  et  multiplici  quam 
in  subiecto  simplici  et  uniformi ;  sed  relative  oppo- 
sita  non  stant  insimul  in  eodem  individuo  creato : 
ergo  nec  in  simplici  hypostasi.  Probatio  mediae. 
Bene  sequitur:  Socrates  est  pater  Platonis :  ergo  non 
est  filius  eius,  vel  est  distinctus  ab  eo:  ergo  multo 
fortius  in  divinis. 

Contra:  1.  Pater  generando  Filium  dat  ei   to- 

.Mopposi-tum  quod  habet;  sed  habet  essentiam  etpersonam: 

'™'     ergo  dal  ei  essentiam  ei  personam:    ergo  sicut   Fi- 

lius  non  distinguitur   a  Patre  essentialiter ,  ita  nec 

personaliter ,  ut  videtur. 


2.  Item ,  Pater  communicat  Filio  essentiam  suam 
propter  summam  ^  simplicitatem ;  sed  aeque  sim- 
plex  est  persona  ut  essentia:  ergo  qua  ratione  com- 
municat  essentiam,  communicat  et  personam. 

3.  Itenij  in  Patre  idem  est  natura  et  persona: 
ergo  impossibile  est,  quod  communicet  unum,  quod 
non*  communicet  abud,  ergo  si  dat  naturam,  et 
personam. 

4.  Item,  videtur  quod  relatio  non  distinguat 
aliqua '  ratione ,  quia  unus  et  idem  punctus  est 
principium  et  finis  respectu  diversarum  linearum: 
ergo  si  istae  relationes  non  sunt  distinctivae ,  vide- 
tur  similiter,  quod  nec  paternitas  et  flliatio.  Si  di- 
cas ,  quod  non  omnes  relationes  distinguunt,  sed  so- 
lum  mutuae,  ut  principium  et  principiatum ,  finis 
et  finitum;  contra^:  Pater  et  Filius  se  habent ,  sicut 
intelligens  et  intellectum,  ut  dicit  Anselmus";  sed 
idem  polest  esse  intelligens  et  intellectum :  ergo  etc. 

5.  Item,  maior  est  repugnantia  in  contrariis 
quam  in  relativis '";  sed  albedo  et  nigredo,  quae 
sunt  conlraria,  non  faciunt  distinctionem  circa  Petrum, 
quia  idem  potest  modo  esse  albus,  modo  niger: 
ergo  multo  fortius  unus  in  divinis  modo  erit  Pater 
modo  Filius. 

6.  Item,  quaeritur ,  quare  potius  relationes  fa- , 
ciunt  distinctionem  personae  quam  essentiae,  cum ' 
aeque  bene  possint  esse  plures  essentiae  vel  naturae 
in  una  persona ,  sicut  e  converso. 


1  Libr.  I.  c.  I.  n.  1.  —  Circa  flnem  argumenli  flde  mul- 
torum  mss.  et  ed.  1  post  inter  aliam  expunximus  rem. 

*  Vat.  adiungit  et. 

3  Cod.  Y  addit  m  creaturis  vero  actio  vel  mutatio. 

*  Multi  codd.  ut  ACGKORSUV  Y  etc.  cum  sex  primis  edd. 
minor,  sed  mendose.  Paulo  infra  ex  antiquioribus  mss.  et  ed. 
1  subsUtuimus  subiecto  pro  substanlia  et  relative  pro  relativa.  — 
Sensus  argumenti  est:  Suppositum  creatum  et  compositum  est 
capax  ad  maiorem  diversitatem  sustinendam,  quam  increatum  et 
simplex ;  sed  in  creato  sujiposito  non  est  capacitas  ad  simul  susli- 
nendarelativeopposita;ergomullo  minusinsimplici  supposito  elc. 

5  In  mss.  et  ed.  1  deest  suam,  quod  Vat.  hic  addit.  Mox 
Vat.  cum  cod.  cc  conlra  alios  codd.  et  ed.  1  et  pro  ut. 


^  Sequimur  vetustiores  codd.  cum  ed.  1  ponendo  quod 
non  loco  quin.  Cod.  Z  brevius  unum  sine  altero. 

'  Multi  codd.  utACLOPQRSTUVY  etc.  cum  ed.  1 
oKo  loco  aliqua ,  sed  ,  ut  videtur ,  minus  bene  ,  etiamsi  sub 
alia  ratione  intelligas  modum  distinguendi  relativis  proprium, 
quia,  uti  ex  subnexis  patet,  agitur  de  eo,  quod  relatio  sim- 
pliciter  non  distinguat.  Cod   Z  nisi  pro  aliqm. 

*  Cod.  Y  addit  videlur  quod  nec  mutuae  quia.  Mox  Vat. 
cum  cod.  cc,  aliis  tamen  codd.  renitentibus,  ut  pro  sicut. 

s  Monolog.  c.  32,  ubi  hoc  quoad  sensum  invenitur. 

'"  Cfr.  Aristot. ,  de  Praedicam.  c.  de  Oppositis.
```
