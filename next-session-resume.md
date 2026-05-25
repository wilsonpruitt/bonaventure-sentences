# Next session — **d.18 eighth chunk DONE 2026-05-25.** Begin `d18-dubia` (⚠ manual-rescue).

**d.1–d.17 + d18-littera + d18-divisio + d18-a1-q1 + d18-a1-q2 + d18-a1-q3 + d18-a2-q1 + d18-a2-q2 + d18-a2-q3 = 209 chunks promoted.** Build: 620 translated, 879 quaestio routes.

## Last session (2026-05-25, d.18 eighth chunk — d18-a2-q3 promotion)

Promoted `d18-a2-q3` Tier-2:
- *Utrum anima rationalis sit ex traduce.* Spans p.451 R-1 (QUAESTIO III header at raw 31767 immediately after d18-a2-q2 SCHOLION close + Q3 opener + Ad oppositum args 1–6 partial) → p.452 (args 6 *Si producitur ex materia praeiacente* close + Contra/Fundamenta args 1–6 with arg 4 ex carne/ex anima dichotomy + arg 5 materia praeiacente quaero-block + arg 6 discindi-semen + CONCLUSIO + Respondeo opener with *triplex modus dicendi* + *Opinio 1.* Intelligentia + *Ratio* divina unitas/immutabilitas + *Reprobatur* haereticum) → p.453 (Opinio 1 close with Isaac *de Definitionibus* umbra-intelligentiae quote + *Opinio 2.* Traductio Augustinus dubitavit + *Non probatur* Christi anima reductio + *Opinio 3.* catholicus et verus + *Duplex ratio.* dignitas + immortalitas + *Conclusio.* + *Solutio oppositorum.* ad 1, 2, 3, 4, 5 partial) → p.454 L-1 (Solutio ad 5 close + ad 6 close at *Patent etiam ea quae dicuntur in littera.* + SCHOLION I Petr. a Tar. four-opinion fluctuation + Gennadius identification of *de Ecclesiast. Dogm.* + Traducianism consensus + SCHOLION II commentator list close at raw 31977 immediately before `DUBIUM CIRCA LITTERAM MAGISTRI.` at raw 31978).
- **25 apparatus entries [^1]–[^25].** p.451 L-2 ¹–⁷ = [^1]–[^7]; p.452 L-2 ¹ + R-2 ²–¹¹ = [^8]–[^18]; p.453 L-2 ¹ + R-2 ²–⁷ = [^19]–[^25]. Notable: [^1] Genesis 46 Vulgate text + sexaginta-sex vs septuaginta apparatus + Hieronym. *Qq. hebraic.* + Aug. *Qq. in Gen.* q.152 lengthy block; [^6] Aug. Epist. 166 ad Hieronym. + Hieronym. *contra Rufinum* III + *Quotidie Deus operatur animas* block on adultery/incest souls + Greg. Nyssen. *de Anima*; [^10] long Aristot. *de Anima* I + Aug. multi-citation block (*de Immort. animae* + *de Quant. animae* + *de Anima et eius origine* + *de Gen ad lit* VII+X) impugning Tertullian; [^17] longest entry — Aristot. XII *Metaph.* + *de Causis* + Isaac *de Definitionibus* Monacensis codex 8001 full transcription of three-order souls (rationalis/bestialis/vegetalis) doctrine; [^21] Ioan. 5,26 *Sicut Pater habet vitam in semetipso* + Vat. *Creatore pro creatione* variant.
- Marginal labels preserved inline per locked Vol II convention: *Ad oppositum.*, *Fundamenta.*, *Opinio 1./2./3.*, *Ratio.*, *Reprobatur.*, *Non probatur.*, *Duplex ratio.*, *Conclusio.*, *Solutio oppositorum.* (eleven labels).
- `has_scholion: true` — single SCHOLION split per Vol II convention into I (doctrinal: Petr. a Tar. four-opinion Augustinian fluctuation + Gennadius identification of *de Ecclesiast. Dogm.* + Traducianism consensus reproved) + II (standard commentator list: Alex. Hal. + Scotus + S. Thom. + B. Albert + Petr. a Tar. + Richard. a Med. + Aegid. R. + Durand. + Biel).
- No `[?]` flags — all 25 anchors + 11 marginal labels crisp at 450 dpi across pp.451–454. OCR around raw 31767–31977 two-column cascade-fragmented around Respondeo (Opinio 1–3 + Duplex ratio) and the long p.453 L-2 ¹ Isaac/Monacensis quote; column-band PDF read authoritative per Vol II Override.
- Cross-chunk hand-off: received nothing from d18-a2-q2 (Q2 forward-bequeathed nothing; Q2's stray `²` on *absque dolore* still requires the 600 dpi decade-polish pass per d.11–d.20). Forward hand-off to d18-dubia: **none** — d18-dubia opens with its own p.454 L-2/R-2 footer block (Cap. 6. n. 9. seqq. + Cap. 15. n. 28. + Civ. Dei XII c. 1 + lit. Magistri c. 1).
- Audits: paraphrase HIGH (1 chunk, expected first-pass); apparatus-count flag CLEARED for d18-a2-q3 (diff +5, at threshold, no flag); header audit DUB-LOSS -2 persists pending d18-dubia.
- Build: 619 → 620 translated, 879 quaestio routes.

## What to do this session

**Promote `d18-dubia`** — ninth and final d.18 chunk. **⚠ This is the remaining manual-rescue chunk per the d.11–d.20 boundary-sweep audit** — the original auto-chunker 2026-05-13 dropped the DUBIUM CIRCA LITTERAM MAGISTRI block; manual rescue 2026-05-23 derived raw line range 31978–32015 from boundary sweep. DUBIUM opens on p.454 L-1 (lower half) at raw 31978 immediately after Q3 SCHOLION II close (`Bicl, II. Sent. d. 17. q. 1.`) with `DUBIUM CIRCA LITTERAM MAGISTRI.` header + opener `Posset tamen aliquis dubitare de hoc quod dicit, quod mulier de costa facta est eo miraculo, quo de quinque panibus etc.…` + *Adiungitur quaestio* on Angeli-ministerium + Aug. *de Gen ad lit* libro nono quote + *Ratiomes 6 pro unitate generis humani* tripartite (ex ordine + ex connexione + ex significatione) closing on p.455 just before `DISTINCTIO XIX.` at raw 32016. Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read. p.454 + p.455 crops cached at `/tmp/colcrop/vol2-p454-*` (p.455 still needs `python3.11 tools/extract-pages.py --volume vol2 --pages 455 --dpi 450` then `python3.11 tools/colcrop.py vol2 455`). After d18-dubia: **d.18 CLOSES** and d.11–d.20 decade-polish-blocker pass triggers (resolve any [?] across d.11–d.20 + Q2's stray *absque dolore* `²`).

## d.18 chunk inventory (in semantic order)

- ~~`d18-littera`~~ **DONE 2026-05-25.**
- ~~`d18-divisio`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q1`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q2`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q3`~~ **DONE 2026-05-25.**
- ~~`d18-a2-q1`~~ **DONE 2026-05-25.**
- ~~`d18-a2-q2`~~ **DONE 2026-05-25.**
- ~~`d18-a2-q3`~~ **DONE 2026-05-25.**
- **`d18-dubia`** — ⚠ manual-rescue (auto-chunker dropped 2026-05-13; rescued 2026-05-23). — NEXT.

## Prior session (2026-05-25, d.18 seventh chunk — d18-a2-q2 promotion)

Promoted `d18-a2-q2` Tier-2:
- *Utrum animae omnium fuerint simul productae.* Spans p.448 R band 1 (QUAESTIO II opener at raw 31566 immediately after d18-a2-q1 SCHOLION II close) → p.449 (Ad oppositum/*Fundamenta* args 1–5 + CONCLUSIO + Respondeo with *Tres modi dicendi* + *Primus.* Plato-Macrobius circulation + *Reprobatur dupliciter.* + *Secundus.* Manichaei + *Reprobatur* contra fidem/philosophiam/sensibilem experientiam + *Tertius.*) → p.450 (*De anima Adae dubitat Augustinus.* + duplex ratio + *Conclusio.* + Gregorius Nazianzenus/Damascene/de Anima et spiritu + *Solutio obiectorum.* ad 1–4) → p.451 L band 1 (ad 4 close *finis in intentione/executione* + ad 5 *absque dolore* + *Posset tamen dici* + single SCHOLION close at raw 31766 immediately before QUAESTIO III).
- **24 apparatus entries [^1]–[^24].** p.448 L-2 ¹–⁴ (forwarded from d18-a2-q1) = [^1]–[^4]; p.448 R-2 ⁵–⁷ = [^5]–[^7]; p.449 L-2 ¹–⁵ = [^8]–[^12]; p.449 R-2 ⁶–¹¹ = [^13]–[^18]; p.450 L-2 ¹–⁵ = [^19]–[^23] (with [^23] absorbing the long Albert-via-Damascene Greg.Naz./Greg.Nyss. apparatus + *de Hominis opificio* + *de Spiritu et anima* p.450 R-2 inline gloss); p.451 L-2 ¹ (Phys 89 / Metaph 23 / de Anima 49) = [^24] anchored at ad 4 *executione*. Notable: [^11] Plato *Timaeus* + *Phaedrus* triplex-status-animae + Macrobius *Somnium Scip.* c.14+21 block; [^15] Aug. *de Haeresibus* c.70 Priscillianistae+Origenes; [^20] long Aug. multi-citation VI *de Gen ad lit* + *de Anima et eius origine* + Epist. 166+190 block; [^23] long Greek-ἔπρεπε apparatus on Gregory Nazianzen vs Gregory Nyssen reading.
- Marginal labels preserved inline: *Ad oppositum.*, *Fundamenta.*, *Tres modi dicendi.*, *Primus.*, *Reprobatur dupliciter.*, *Secundus.*, *Reprobatur.* (Manichaei), *Tertius.*, *De anima Adae dubitat Augustinus.*, *Conclusio.*, *Solutio obiectorum.* (eleven labels).
- `has_scholion: true` — single SCHOLION (no II split) — doctrinal recap to d.17 a.1 q.3 + commentator list (Alex. Hal. + Scotus + S. Thom. + B. Albert + Petr. a Tar. + Richard. a Med. + Aegid. R. + Durand. + Dionys. Carth. + Biel).
- **One `[?]` flag:** Q2 ad 5 body anchor `²` at *absque dolore²* on p.451 L-1 has no matching p.451 L-2 footer (visible L-2 jumps from ¹ Phys 89 — Q2 ad 4 *executione* — directly to ² *Cfr. infra d. 19* — Q3 arg 6). Either a stray punctuation artifact or the `²` rides into Q3's footer block as the *infra d. 19* note. Decade-polish 600 dpi pass for d.11–d.20 to resolve.
- Cross-chunk hand-off: received p.448 L-2 ¹–⁴ from d18-a2-q1 (folded as [^1]–[^4]). Forward hand-off to d18-a2-q3: **none** — p.451 L-2 ²–³ + R-2 ⁴–⁷ all anchor in Q3 args.
- Audits: paraphrase HIGH (2 chunks, expected first-pass); apparatus-count flag CLEARED for d18-a2-q2 (diff -6, not flagged); header audit DUB-LOSS -2 persists pending d18-dubia.
- Build: 618 → 619 translated, 879 quaestio routes.

## What to do this session

**Promote `d18-a2-q3`** — eighth d.18 chunk. QUAESTIO III opens on p.451 R band 1 at raw 31767 with `QUAESTIO III.` + italic title *Utrum anima rationalis sit ex traduce.* + opener `Tertio quaeritur, supposito, quod animae producantur successive, utrum anima rationalis sit ex traduce. Et quod sic, videtur: 1. Genesis quadragesimo sexto: Omnes animae, quae egressae sunt de femore Iacob, sunt septuaginta duo…` No cross-chunk footer migrates from d18-a2-q2. Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read. p.451 crops cached at `/tmp/colcrop/vol2-p451-*`; generate p.452+ as needed.

**⚠ d18-dubia is a remaining manual-rescue chunk per the d.11–d.20 boundary-sweep audit — keep this flag visible until d18-dubia clears.**

## d.18 chunk inventory (in semantic order)

- ~~`d18-littera`~~ **DONE 2026-05-25.**
- ~~`d18-divisio`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q1`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q2`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q3`~~ **DONE 2026-05-25.**
- ~~`d18-a2-q1`~~ **DONE 2026-05-25.**
- ~~`d18-a2-q2`~~ **DONE 2026-05-25.**
- **`d18-a2-q3`** — *Utrum anima rationalis sit ex traduce.* — NEXT. (skeleton)
- `d18-dubia` (skeleton; ⚠ manual-rescue)

## Prior session (2026-05-25, d.18 sixth chunk — d18-a2-q1 promotion)

Promoted `d18-a2-q1` Tier-2:
- *Utrum animae omnium hominum sint una substantia, an diversae.* Spans p.444 L-1 at raw 31292 (`ARTICULUS II.` + subtitle *De productione animae Evae aliorumque hominum.* + opener `Consequenter quaeritur de secundo articulo…` + 3-question sub-divisio folded in per locked Vol II Override step 5 + QUAESTIO I opener) → p.444 R-1 (Ad oppositum args 1–3) → p.445 (Ad oppositum args 4–6 + Contra/Fundamenta args 1–6 partial) → p.446 (CONCLUSIO + Respondeo with *Error 1.* Pythagoras/Varro anima-est-Deus + *Reprobatur* + *Error 2.* Averroes unitatem-intellectus + *Rationes 2.* + Commentator-tripartition quotation *intellectus recipiens/efficiens/factum* + Aristoteles-interpretatio + intellectus *adeptus*) → p.447 (*Reprobatur triplici ratione* contra christianam-religionem/rectam-rationem/sensibilem-experientiam + *Conclusio* + *Solutio oppositorum* ad 1–6 with *Notandum* ×4 on indigentia/manifestatio-bonitatis-divinae/species-singularis-accidens/duo-specula) → p.448 L-0 (Notandum close at *adiuvetur per radium fidei.* + SCHOLION I Arab-philosophers + Parisian condemnations + Scotus + Albert + Aquinas + Henr. Gand. Aristoteles-undecidedness) + p.448 R-0 (SCHOLION II commentator list close at raw 31565 immediately before QUAESTIO II at raw 31566).
- **23 apparatus entries [^1]–[^23].** Page-split map: p.444 L-2 ¹ (Aristot. II de Anima text.20 + Averroes Comment. super III de Anima + Destruct. destruct. + Algazel + dividuationem/individuationem variant; **migrated from d18-a1-q3 prior-chunk hand-off**) = [^1]; p.444 R-2 ² = [^2]; p.445 L-2 ¹–⁴ + R-2 ⁵–⁷ = [^3]–[^9]; p.446 L-2 ¹–⁵ + R-2 ⁶–⁹ = [^10]–[^18]; p.447 L-2 ¹–⁵ + R-2 ⁶ = [^19]–[^23]. Notable: [^3] Averroes III de Anima text 5 *prima materia recipit formas diversas / ista [intellectus] recipit formas universales* full block; [^7] Boethius *de Unitate et uno* *Quidquid est, ideo est quod unum est* + *Esse est existentia formae in materia* block; [^10] Augustinus *de Civ. Dei* IV.31 + VII.6+23 attribution to Varro + Isidor./Cicero/Lactantius/Minucius Felix; [^15] Commentator-tripartition pointer to d.1 p.1 a.1 q.2; [^17] Averroes *intellectus adeptus* doctrina *cum intellectus materialis fuerit copulatus*; [^22] Avicenna V Metaph. c.2 *universale-singulare per relationem ad multa* full block.
- Marginal labels preserved inline per locked Vol II convention: *Ad oppositum.*, *Fundamenta.*, *Error 1.*, *Reprobatur.*, *Error 2.*, *Rationes 2.*, *Explicatur erro[r].*, *Reprobatur triplici ratione.*, *Notandum.* (×4), *Conclusio.*, *Solutio oppositorum.*, *Dupliciter deficit.*
- `has_scholion: true` — SCHOLION I substantial doctrinal (Averroist unitatem-intellectus error + Parisian condemnations 1277 theses 20/22/27 + Scotus IV *Sent.* d.43 q.2 + Albert *S.* p.II tr.13 q.77 m.3 + Aquinas opusculum 15 + Summae/SCG + Henr. Gand. on Aristotle's undecidedness); II = q1 commentator list (Scot. + Hier. de Montefortino + Petr. a Tar. + Richard. a Med. + Aegid. R. + Durand. + Dionys. Carth.).
- No `[?]` flags — all 23 anchors + 13 marginal labels crisp at 450 dpi across pp.444–448. OCR around raw 31292–31565 two-column cascade-fragmented around Error II + Commentator-quotation + Notandum (×4) + SCHOLION boundary; column-band PDF read authoritative per Vol II Override.
- Cross-chunk hand-off: received p.444 L-2 footer ¹ from d18-a1-q3 (folded as [^1]). Forward hand-off to d18-a2-q2: **none** — p.448 L-2 footers ¹ (Vers.10) + ² (supra d.2 p.1 a.2 q.3) + ³ (Aristot. II de Anima text.36 c.4) + ⁴ (Simile invenitur supra pag.210) all anchor in Q2's *Iob quadragesimo* / *non est anima propter corpus* args and migrate forward.
- Audits: paraphrase HIGH (1 chunk, expected first-pass); apparatus-count flag CLEARED for d18-a2-q1 (not in flagged list); header audit DUB-LOSS -2 persists pending d18-dubia.
- Build: 617 → 618 translated, 879 quaestio routes.

## What to do this session

**Promote `d18-a2-q2`** — seventh d.18 chunk. QUAESTIO II opens on p.448 R band 1 at raw 31566 with `QUAESTIO II.` + italic title *Utrum animae omnium fuerint simul productae.* + opener `Secundo quaeritur, utrum animae omnium fuerint simul productae. Et quod sic, videtur: 1. Iob quadragesimo: Ecce Behemoth, quem feci tecum…` Per the d18-a2-q1 forward hand-off, p.448 L-2 footers ¹–⁴ (Vers.10 + supra d.2 p.1 a.2 q.3 + Aristot. II de Anima text.36 + Simile invenitur supra pag.210) migrate here as the first apparatus entries. Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read. p.448 crops cached at `/tmp/colcrop/vol2-p448-*`; generate p.449+ as needed.

**⚠ d18-dubia is a remaining manual-rescue chunk per the d.11–d.20 boundary-sweep audit — keep this flag visible until d18-dubia clears.**

## d.18 chunk inventory (in semantic order)

- ~~`d18-littera`~~ **DONE 2026-05-25.**
- ~~`d18-divisio`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q1`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q2`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q3`~~ **DONE 2026-05-25.**
- ~~`d18-a2-q1`~~ **DONE 2026-05-25.**
- **`d18-a2-q2`** — *Utrum animae omnium fuerint simul productae.* — NEXT. (skeleton)
- `d18-a2-q3` (skeleton)
- `d18-dubia` (skeleton; ⚠ manual-rescue)

## Prior session (2026-05-25, d.18 fifth chunk — d18-a1-q3 promotion)

Promoted `d18-a1-q3` Tier-2:
- *Utrum ratio seminalis sit forma universalis, vel singularis.* Spans p.439 (QUAESTIO III header at raw 30919 immediately after d18-a1-q2 p.438 L close + Ad oppositum args 1–6 + Contra/Fundamenta args 1–3) → p.440 (Fundamenta args 4–6 + CONCLUSIO + Respondeo with *Praenotandum* + *Opinio 1.* universalia realiter in natura + *Iudicium de opinione 1.* magnorum concors auctoritati/rationi/sensui) → p.441 (Philosophus Physicorum + *Opinio 2.* forma totius vs forma partis + *Magis approbatur.* via communis + *Ratio 1.* cognitionem + univocationem + Avicenna *essentia* = quidditas + *Ratio 2.* Philosophus *cum dico caelum dico formam* + Boethius species totum esse) → p.442 (*Ratio 3.* egressus specierum a genere vs eductio formarum + elementarem/mixtionis/complexionis + *Iudicium de utraque opinione.* albedo defined-vs-produced + *Conclusio 1.* (proprie sensu) + *Conclusio 2.* (largiore sensu) + *De argumentis.* + *Solutio oppositorum.* ad 1 + ad 2) → p.443 (ad 3 Petrus/Paulus + ad 4 + ad 5 + ad 6 + SCHOLION I doctrina Augustini + descendentia critique) → p.444 (SCHOLION II 5 earlier opinions: Quidam/Scotus/S.Thom/Richard/Aegid + SCHOLION III S. Bonav. ab Alex. Hal. *natura simplex et incorporea* + SCHOLION IV Petr. a Tar. lac→sanguis→caro→embryo→animal + ovum + SCHOLION V Posteriores cum S. Thoma/Scoto/Aegidio/Henrico Gand non approbant + Apostoli *Ex parte cognoscimus* close at raw 31291 immediately before `ARTICULUS II.` at raw 31292).
- **32 apparatus entries [^1]–[^32].** Page-split map: p.439 L-2 ¹–⁴ = [^1]–[^4]; p.439 R-2 ⁵–⁸ = [^5]–[^8]; p.440 L-2 ¹–⁶ = [^9]–[^14]; p.441 L-2 ¹–³ = [^15]–[^17]; p.441 R-2 ⁴–⁹ = [^18]–[^23]; p.442 L-2 ¹–² = [^24]–[^25]; p.442 R-2 ³–⁶ = [^26]–[^29]; p.443 L-2 ¹–³ = [^30]–[^32]. p.444 L-2 footer ¹ stays with d18-a2-q1. Notable: [^14] Averroes XII Comment. *Quoniam autem in fundamento* mat-vs-gen full block (Venice 1560 vs 1489); [^17] *Triplex universale* (*in causando / in repraesentando / in essendo*) systematic note + Aug. V *de Gen. ad lit.* c.4 n.11 *Causaliter ergo*; [^24] Averroes III *de Caelo* text 67 mixture-as-mean block; [^25] Porphyry metaphysicus-vs-logicus + *genus generalissimum* gloss; [^29] *Sex Principiorum* + Petr. a Tar. *prioritas naturae non temporis*.
- Marginal labels preserved inline: *Ad oppositum.*, *Fundamenta.*, *Praenotandum.*, *Opinio 1.*, *Iudicium de opinione 1.*, *Opinio 2.*, *Magis approbatur.*, *Ratio 1./2./3.*, *Iudicium de utraque opinione.*, *Conclusio 1./2.*, *De argumentis.*, *Solutio oppositorum.*
- `has_scholion: true` — FIVE scholia (I Augustinian origin + descendentia critique; II 5 earlier opinions; III S. Bonav. + reception via Alex. Hal. + Albert; IV Petr. a Tar. q3-specific with embryonic analogy; V Posteriores Scholastici dissents). SCHOLION III spans p.443 R-1 → p.444 L-0; SCHOLION V occupies p.444 R-0.
- No `[?]` flags — all 32 anchors + 13 marginal labels crisp at 450 dpi pp.439–444. OCR around raw 30919–31291 two-column cascade-fragmented around Respondeo + SCHOLION III↔IV↔V boundaries; column-band PDF read authoritative per Vol II Override.
- Cross-chunk hand-off: received nothing from d18-a1-q2; forward to d18-a2-q1: none (p.444 L-2 footer ¹ anchors in q1 arg.1).
- Audits: paraphrase HIGH (1 chunk, expected first-pass); apparatus-count flag CLEARED for d18-a1-q3 (diff +21, below threshold); header audit DUB-LOSS -2 persists pending d18-dubia.
- Build: 616 → 617 translated, 879 quaestio routes.

## What to do this session

**Promote `d18-a2-q1`** — sixth d.18 chunk. ARTICULUS II opens on p.444 L band 1 at raw 31292 with `ARTICULUS II.` + subtitle *De productione animae Evae aliorumque hominum.* + opener `Consequenter quaeritur de secundo articulo, scilicet de productione animae ipsius Evae et per consequens omnis alterius animae ab anima Adae. Et circa hoc quaeruntur tria.` + 3-question sub-divisio (folded into a2-q1 per Vol II Override step 5) + QUAESTIO I opener *Utrum animae omnium hominum sint una substantia, an diversae.* p.444 L-2 footer ¹ migrates here as the first apparatus entry. p.444 crops cached at `/tmp/colcrop/vol2-p444-*`; generate p.445+ as needed.

**⚠ d18-dubia is a remaining manual-rescue chunk per the d.11–d.20 boundary-sweep audit — keep this flag visible until d18-dubia clears.**

## d.18 chunk inventory (in semantic order)

- ~~`d18-littera`~~ **DONE 2026-05-25.**
- ~~`d18-divisio`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q1`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q2`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q3`~~ **DONE 2026-05-25.**
- **`d18-a2-q1`** — *Utrum animae omnium hominum sint una substantia, an diversae.* — NEXT. (skeleton)
- `d18-a2-q2` (skeleton)
- `d18-a2-q3` (skeleton)
- `d18-dubia` (skeleton; ⚠ manual-rescue)

## Prior session (2026-05-25, d.18 fourth chunk — d18-a1-q2 promotion)

Promoted `d18-a1-q2` Tier-2:
- *Utrum mulier formata fuerit de costa viri secundum rationem seminalem.* Spans p.434 R-0 at raw 30582 (QUAESTIO II opener `Secundo quaeritur, utrum mulier formata sit de costa viri secundum rationem seminalem. Et quod sic, videtur: 1. Primo per textum: Consummavit Deus sexto omne opus suum…` immediately after q1 SCHOLION II close on p.434 R-0) → p.434 R (Ad oppositum args 1–4) → p.435 (args 5–6 + Contra/Fundamenta args 1–6 + *Quaestio incidens* on causales-vs-seminales differentia via Aug. *de Gen ad lit* 6 lengthy block) → p.436 (rationes seminales-vs-naturales differentia + CONCLUSIO + Respondeo with *Praenotandum* + *Notiones generales* causa/ratio/semen distinctions + *Differentia rationum primordialium et causalium* + *Item naturales rationes et seminales* + *Aliter* + magi-virgis-serpentes exemplum + *Applicatio* obedientia-vs-potentia-naturae) → p.437 (*Distinguitur potentia propinqua et remota* propinqua/sufficiens vs remota/insufficiens + *Conclusio 1* (esse-in-costa) + *Conclusio 2* (facta-de-costa) + *Solutio oppositorum* ad 1.2 / 3 / 4 / 5 *Natura accipitur dupliciter* + *Distinguitur contra naturam et supra naturam* with caeco-mortuum exemplum) → p.438 L (caeco-mortuum-ad-vitam close + *Quid mirabile, quid miraculum* + ad 6 close at *non fuit proprie contra naturam nec est miraculum dicendum.*) + SCHOLION I–IV. Closes immediately before `DIST. XVIII. ART. I. QUAEST. III` page header at raw 30916; q3 opens at raw 30919.
- **32 apparatus entries [^1]–[^32].** p.434 L-2 ³ + R-2 ⁴–⁶ (hand-off from d18-a1-q1) = [^1]–[^4]; p.435 L-2 ¹–⁵ = [^5]–[^9]; p.435 R-2 ⁶–⁹ = [^10]–[^13]; p.436 L-2 ¹–⁴ = [^14]–[^17]; p.436 R-2 ⁵–¹⁰ = [^18]–[^23]; p.437 L-2 ¹–⁵ = [^24]–[^28]; p.437 R-2 = [^29]; p.438 L-2 ¹ = [^30]; p.438 R-2 ²–³ = [^31]–[^32]. Notable: [^5] = Aug. XXVI *contra Faustum* c.3 *Deus creator nihil contra naturam facit* + Prosper + VI *de Gen ad lit* c.18 n.29 *Tam enim non fecit* block; [^10] = Aug. V *de Gen ad lit* c.23 n.44 *In semine ergo illa omnia fuerunt primitus* with multi-codex variant apparatus; [^13] = Aug. VI *de Gen ad lit* c.11/14/15 triple-citation *quemadmodum formaturus* block; [^16] = Aristot. II *Phys* text 48 *quae ab intellectu aguntur, et a natura* + nature-definition pointer to tom.1 pag.134 nota 10; [^28] = Aug. VI *de Gen ad lit* c.13 n.23–24 + IX c.17 n.32 + XXVI *contra Faustum* c.3 duplex-acceptio-naturae block.
- Marginal labels preserved inline: *Ad oppositum.*, *Fundamenta.*, *Quaestio incidens.*, *Praenotandum.*, *Notiones generales.*, *Differentia rationum primordialium et causalium.*, *Item naturales rationes et seminales.*, *Aliter.*, *Applicatio.* (×2), *Distinguitur potentia propinqua et remota.*, *Conclusio 1./2.*, *In membris.*, *Solutio oppositorum.*, *Natura accipitur dupliciter; item locutio contra naturam.*, *Distinguitur contra naturam et supra naturam.*, *Quid mirabile, quid miraculum.*
- `has_scholion: true` — SCHOLION I = Alex. Hal. esse-vs-produci distinction (2 conclusions, second universally granted, first disputed); II = quadruple Augustinian terminology + Scotus *semen* + Richard a Med. inter-elemental ratio seminalis gloss; III = S. Thom. tripartite miracle taxonomy harmonized with Bonav.'s binary; IV = q2 commentator list (Alex. Hal., S. Thom., B. Albert, Petr. a Tar., Richard a Med., Aegid. R., Durand., Dionys. Carth., Biel).
- No `[?]` flags — all 32 anchors + 17 marginal labels crisp at 450 dpi across pp.434–438.
- Cross-chunk hand-off received from d18-a1-q1: p.434 L-2 ³ + R-2 ⁴–⁶ folded as [^1]–[^4]. Forward hand-off to d18-a1-q3: none.
- Audits: paraphrase HIGH (1 chunk); apparatus-count flag CLEARED for d18-a1-q2 (5 skeleton-suspect flags persist on d18 a1-q3/a2-*/dubia siblings); header DUB-LOSS / Q-LOSS persists pending d18 siblings.
- Build: 615 → 616 translated, 879 quaestio routes.

## What to do this session

**Promote `d18-a1-q3`** — fifth d.18 chunk. QUAESTIO III opens on p.439 at raw 30919 with `QUAESTIO III.` + italic title *Utrum ratio seminalis sit forma universalis, vel singularis.* + opener `Tertio quaeritur, quid sit ratio seminalis secundum essentiam; et cum constet, eam esse formam, est quaestio, utrum sit forma universalis, an singularis. Et quod sit forma universalis, videtur: 1. Primo per Philosophum in decimo sexto de Animalibus, ubi dicit, quod prius est animal quam homo…` No cross-chunk footer migrates from d18-a1-q2. Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read for p.439+. Generate p.439+ crops as needed.

**⚠ d18-dubia is a remaining manual-rescue chunk per the d.11–d.20 boundary-sweep audit — keep this flag visible until d18-dubia clears.**

## d.18 chunk inventory (in semantic order)

- ~~`d18-littera`~~ **DONE 2026-05-25.**
- ~~`d18-divisio`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q1`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q2`~~ **DONE 2026-05-25.**
- **`d18-a1-q3`** — *Utrum ratio seminalis sit forma universalis, vel singularis.* — NEXT. (skeleton)
- `d18-a2-q1` (skeleton)
- `d18-a2-q2` (skeleton)
- `d18-a2-q3` (skeleton)
- `d18-dubia` (skeleton; ⚠ manual-rescue)

## Last session (2026-05-25, d.18 third chunk — d18-a1-q1 promotion)

Promoted `d18-a1-q1` Tier-2:
- *Unde fuerit productum corpus mulieris.* Spans p.431 R-1 bottom (QUAESTIO I opener `Circa primum sic proceditur et quaeritur, unde fuerit productum corpus mulieris.` immediately after d18-divisio close) → p.432 (9 numbered objections grouped *Contra primum/secundum/tertium thesim* + CONCLUSIO + Respondeo opener with *Duplex congruitas* / *Secundum congruitatem respondetur ad 3 qq.*) → p.433 (Triplex significatio: *Deus et anima* / *Christus et Ecclesia* / *superior portio rationis et inferior* + Solutio ad 1, 2, 3 with Anselm 4-modi quote) → p.434 L-mid (Ad 4-5-6 grouped reply on sopor + Ad 7-8-9 grouped reply on osse/costa closing at *sicut planius explicatur in quarto.*) + SCHOLION I (Petr. a Tar. *somnus* vs. *sopor* distinction with reference to arg. 4) + II (commentator list).
- **23 apparatus entries [^1]–[^23].** p.431 R-2 footers ²–³ received per d18-divisio hand-off, folded together as [^1] on the opener phrase *de costa eius et osse.* p.432 L-2 ¹–⁵ = [^2]–[^6]; p.432 R-2 ⁶–¹⁰ = [^7]–[^11]; p.433 L-2 ¹–⁶ = [^12]–[^17]; p.433 R-2 ⁷–¹⁰ = [^18]–[^21]; p.434 L-2 ¹–² = [^22]–[^23]. Notable: [^17] = Anselm *Cur Deus homo* II c.8 *Quatuor modis potest Deus facere hominem* block; [^21] = Aug. IX *de Gen ad lit* c.19 n.36 *Ac per hoc etiam illa ecstasis* block.
- Marginal labels preserved inline per locked Vol II convention: *Theses 3.*, *Contra 1./2./3. thesim.*, *Tres quaestiones.*, *Duplex congruitas.*, *Secundum congruitatem respondetur ad 3 qq.*, *Item secundae congruitatem.*, *Triplex significatio.*, *Significatio 1./2./3.*, *Ratio obiectorum.*
- `has_scholion: true` — SCHOLION I substantial (Bonav.'s ingeniously-developed mystical significations + Petr. a Tar. *somnus* vs. *sopor* distinction); II = q1 commentator list (Alex. Hal., S. Thom., B. Albert, Petr. a Tar., Richard. a Med., Aegid. R., Durand., Dionys. Carth., Biel).
- No `[?]` flags — all 23 anchors crisp at 450 dpi across pp.431–434. OCR around raw 30377–30581 two-column cascade-fragmented; column-band PDF read authoritative per Vol II Override.
- Cross-chunk hand-off: received p.431 R-2 ²–³ from d18-divisio (folded as [^1]). Forward hand-off to d18-a1-q2: **p.434 L-2 footer ³ (Gen. 2, 2 Septuaginta / August. IX de Gen ad lit c.1 n.1 + c.2 n.6; VI c.11 n.18) + p.434 R-2 footers ⁴ (*Cap. 11. n. 18, ubi textus originalis in fine* erant quasi semina futurorum*; Dein non pauci codd. cum primis edd.* sed non nisi costa *pro* sed non nisi in costa*.*) + ⁵ (*Vide supra pag. 400, nota 7. — De ultima huius argumenti propositione cfr. Aristot., II. de Generat. animal. c. 1. seqq.*) + ⁶ (*Vat.* passibilis*.*)** all anchor in Q2 opener/args and migrate forward.
- Audits: paraphrase HIGH (1 chunk, expected first-pass); apparatus-count flag CLEARED for d18-a1-q1 (6 skeleton-suspect flags persist on d18 a*/dubia siblings); header DUB-LOSS / Q-LOSS still fires because d.18 siblings remain skeleton — clears as those promote.
- Build: 614 → 615 translated, 879 quaestio routes.

## What to do this session

**Promote `d18-a1-q2`** — fourth d.18 chunk. QUAESTIO II opens on p.434 R-0 at raw 30582 with `QUAESTIO II.` + italic title *Utrum mulier formata fuerit de costa viri secundum rationem seminalem.* + opener `Secundo quaeritur, utrum mulier formata sit de costa viri secundum rationem seminalem. Et quod sic, videtur: 1. Primo per textum: Consummavit Deus sexto omne opus suum…` Per the d18-a1-q1 forward hand-off, p.434 L-2 footer ³ + p.434 R-2 footers ⁴–⁶ migrate here as the first apparatus entries. Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read. p.434 crops cached at `/tmp/colcrop/vol2-p434-*`; generate p.435+ as needed.

**⚠ d18-dubia is a remaining manual-rescue chunk per the d.11–d.20 boundary-sweep audit — keep this flag visible until d18-dubia clears.**

## d.18 chunk inventory (in semantic order)

- ~~`d18-littera`~~ **DONE 2026-05-25.**
- ~~`d18-divisio`~~ **DONE 2026-05-25.**
- ~~`d18-a1-q1`~~ **DONE 2026-05-25.**
- **`d18-a1-q2`** — *Utrum mulier formata fuerit de costa viri secundum rationem seminalem.* — NEXT. (skeleton)
- `d18-a1-q3` (skeleton)
- `d18-a2-q1` (skeleton)
- `d18-a2-q2` (skeleton)
- `d18-a2-q3` (skeleton)
- `d18-dubia` (skeleton; ⚠ manual-rescue)

## Prior session (2026-05-25, d.18 second chunk — d18-divisio promotion)

Promoted `d18-divisio` Tier-2:
- *Commentarius in Distinctionem XVIII — De formatione mulieris de viro.* Spans printed p.431 only (PDF p.453, vol II offset +22). Opens at raw 30339 with `COMMENTARIUS IN DISTINCTIONEM XVIII.` on p.431 L band 1 (immediately after d18-littera p.431 L-0 tail close at *...singillatim animas de nihilo creat.* at raw 30338); holds title + subtitle *De formatione mulieris de viro.* + epigraph *In eodem quoque paradiso etc.* + DIVISIO TEXTUS (L+R band 1 interleaved, 4 paragraphs: corpus/anima split → 4 causal sub-parts of corpus → 4 sub-parts of anima → recapitulation) + TRACTATIO QUAESTIONUM (L+R band 1 bottom, 2-question high-level split) + ARTICULUS I header + subtitle *De productione corporis mulieris de latere viri.* + ART. I sub-divisio `Circa primum quaeruntur tria` (3-question listing) + QUAESTIO I header + italic title *Unde fuerit productum corpus mulieris.* Closes immediately before the Q1 opener `Circa primum sic proceditur...` on p.431 R band 1.
- **1 apparatus entry [^1]** from p.431 L band 2 *NOTAE AD COMMENTARIUM* footer (`Plures codd. cum edd. 3, 4 et Vat. omittunt quantum ad corpus`), anchored at *primum est formatio mulieris quantum ad corpus*¹ inside the recapitulation paragraph of DIVISIO TEXTUS. p.431 L band 2 upper block (*NOTAE AD LIBR. SENTENTIARUM* ¹–²) belongs to d18-littera and stays there. p.431 R band 2 footers ²–³ (`Ita cod. cc et ed. 1; ceteri codd. cum aliis edd. ex` / `Hic c. 1. — Gen. 2, 21. seqq.`) anchor in Q1 opener and migrate forward to d18-a1-q1.
- **d.18 pars-split**: confirmed NO pars split (re-verified) — `DIST. XVIII. ART. I/II.` running heads only. Chunk id `d18-divisio`, not `d18-p1-divisio`.
- **Article fold-in** per locked Vol II Override step 5: divisio holds DIVISIO TEXTUS + TRACTATIO QUAESTIONUM + the ART. I header + subtitle + the ART. I sub-divisio (3-question listing). Unlike d.17 where the article sub-divisio is absent (3-question listing lives in TRACTATIO), d.18 has BOTH: a 2-question high-level TRACTATIO (corpus vs anima) AND the 3-question ART. I sub-divisio (`Circa primum quaeruntur tria`).
- No `[?]` flags — single anchor crisp at 450 dpi. OCR around raw 30339–30371 is two-column cascade-fragmented; column-band PDF read authoritative per Vol II Override.
- `has_scholion: false` — divisio chunks carry no SCHOLION by design.
- Cross-chunk hand-off: received nothing from d18-littera. Forward hand-off to d18-a1-q1: p.431 R-2 footers ²–³ migrate as first apparatus entries.
- Audits: paraphrase HIGH (1 chunk, expected first-pass); apparatus-count flag CLEARED for d18-divisio (7 skeleton-suspect flags persist on d18 a*/dubia siblings — clears as they promote); header audit Q-LOSS / DUB-LOSS fires because d.18 a*/dubia siblings are skeleton (a divisio chunk has 1 ART, no QUAEST/DUB headers) — clears as those promote.
- Build: 613 → 614 translated, 879 quaestio routes.

## What to do this session

**Promote `d18-a1-q1`** — third d.18 chunk. QUAESTIO I opens on p.431 R band 1 with `Circa primum sic proceditur et quaeritur, unde fuerit productum corpus mulieris. Et dicit Magister in littera³, et tractum est de secundo Genesis...` Per the d18-divisio forward hand-off, p.431 R band 2 footers ²–³ (cod. cc/ed.1 *ex* variant + *vide infra principium 1. quaest.* / Hic c. 1. — Gen. 2, 21. seqq.) migrate here as the first apparatus entries. Q1 body extends across pp.431 R-1 (opener) → p.432 (six Ad oppositum + Contra args + CONCLUSIO + Respondeo with *Duplex congruitas ordinis* + *Significatio 1/2/3* + Solutio ad 1–6) → p.433+. Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read. p.431 + p.432 crops already cached at `/tmp/colcrop/vol2-p43{1,2}-*`; generate p.433+ as needed.

**⚠ d18-dubia is a remaining manual-rescue chunk per the d.11–d.20 boundary-sweep audit — keep this flag visible until d18-dubia clears.**

## d.18 chunk inventory (in semantic order)

- ~~`d18-littera`~~ **DONE 2026-05-25.**
- ~~`d18-divisio`~~ **DONE 2026-05-25.**
- **`d18-a1-q1`** — *Unde fuerit productum corpus mulieris.* — NEXT. (skeleton)
- `d18-a1-q2` (skeleton)
- `d18-a1-q3` (skeleton)
- `d18-a2-q1` (skeleton)
- `d18-a2-q2` (skeleton)
- `d18-a2-q3` (skeleton)
- `d18-dubia` (skeleton; ⚠ manual-rescue)

## Prior session (2026-05-25, d.18 first chunk — d18-littera promotion)

Promoted `d18-littera` Tier-2:
- *Distinctio XVIII — Littera Magistri*, Cap. I–VII (7 capitula), spans p.429 L-1 (`DISTINCTIO XVIII.` + `Cap. I. De formatione mulieris.` immediately after d17-dubia DUB V close *Alia satis patent per iam dicta.* at raw 30201) → p.429 R (Cap. II close + Cap. III opener *Quare dormienti viro...* with *Hugo.* marginal + Cap. IV opener *Quod de costa, in se multiplicata sine additamento extrinsecae rei, facta fuerit.* with *Dubium unicum.* marginal) → p.430 L (Cap. IV close *Solum Deus, id est Trinitas, est Creator¹* + Cap. V *De causis superioribus et inferioribus* with *Hugo.* + *Rationes seminales.* marginals) → p.430 R (Cap. VI *De causis, quae in Deo simul sunt et in creaturis* with *Notandum.* marginal + Cap. VII *De anima mulieris* opener with *Tres opiniones.* marginal + Ecclesiasticis Dogmatibus quote) → p.431 L-0 + R-0 (4-line tail closing at *...sed singillatim animas de nihilo creat.* at raw 30338 immediately before `COMMENTARIUS IN DISTINCTIONEM XVIII.`).
- **17 apparatus entries [^1]–[^17].** Page-split map: p.429 *NOTAE AD LIBR. SENTENTIARUM* L-2 ¹–³ + R-2 ⁴–⁷ = [^1]–[^7] (Gen 2,21,22 + Hugo de Sacram p.VI cc.34–36 + Sum Sent tr.3 c.3 + Gandolph cit / Aug XII de Civ Dei c.27 / Edd 1,5,8 *adiungunt viri* / Aug loc.cit + IX de Gen ad lit c.13 n.23 + de Bono coniugali c.1 / Hugo I de Sacram p.VI c.36 + Sum Sent + Vat. *scilicet ut nullam* variant / Ephes 5,32 + Ioan 19,34 / Hugo Sum Sent + *addito* codd. abest); p.430 L-2 ¹–⁵ + R-2 ⁶–⁸ = [^8]–[^15] (Aug IX de Gen ad lit c.15 n.26 + c.16 n.30 / Cfr IX de Gen ad lit cc.16–17 n.32 + 83 Qq q.46 + c.18 n.33 / Haec omnia ex Hugone Sum Sent tr.3 c.3 / Quae praecedunt Hugo ex Aug IX de Gen ad lit c.17 n.32 + c.18 n.33 / Vat. *creaturae* / Edd 1,8 *factorum* + Cod Erf *futurorum* from VI lib c.8 n.13 + *quo natura substituit* gloss / Aug X de Gen ad lit c.1 n.1 + Hugo / Gennadius c.14 + Vat. *in corporibus* pro *cum corporibus*); p.431 L-2 ¹–² = [^16]–[^17] (Post *plenus* edd 1,8 *et anima et corpore* / Glossa Ps.32,15 ex Hieronymo contra Ioan. Ierosolymitanum).
- Marginal labels preserved inline per locked Vol II convention: *Augustinus.* (×2), *Hugo.* (×2), *Dubium unicum.*, *Rationes seminales.*, *Notandum.*, *Tres opiniones.*
- `has_scholion: false` — littera chunks carry no SCHOLION by design.
- No `[?]` flags — all 17 anchors + 8 marginal labels crisp at 450 dpi across pp.429–431. OCR around raw 30201–30338 is two-column cascade-fragmented; column-band PDF read authoritative per Vol II Override.
- **p.429 dual footer block:** the critical-apparatus footnotes (¹ Vat. *spiritualis* + ² Cfr. d.20 dub.7) anchor entirely in d17-dubia's p.429 L-1 tail and stay there; this chunk takes only the *NOTAE AD LIBR. SENTENTIARUM* Lombard-text block (¹–⁷).
- Cross-chunk hand-off: none received from d17-dubia; none forward to d18-divisio (d18-divisio opens p.431 L-1 with its own *NOTAE AD COMMENTARIUM* footer block).
- Audits: paraphrase HIGH (1 chunk, expected first-pass); apparatus-count flag CLEARED for d18-littera (chunk diff -4, no flag); header audit Q-LOSS / A-LOSS / DUB-LOSS fires because d.18 divisio + a*/dubia siblings are skeleton — clears as those promote.
- Build: 612 → 613 translated, 879 quaestio routes.

## What to do this session

**Promote `d18-divisio`** — second d.18 chunk. COMMENTARIUS IN DISTINCTIONEM XVIII opens at raw 30339 on p.431 L-1 with `De formatione mulieris de viro.` subtitle + epigraph *In eodem quoque paradiso etc.* + DIVISIO TEXTUS + TRACTATIO QUAESTIONUM. d.18 has NO pars split. Per locked Vol II convention the divisio holds DIVISIO TEXTUS + TRACTATIO QUAESTIONUM + the first-article sub-divisio fold-in (no standalone d18-a1-divisio). Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read for p.431 + p.432. p.431 crops cached at `/tmp/colcrop/vol2-p431-*`; generate p.432 as needed.

**⚠ d18-dubia is a remaining manual-rescue chunk per the d.11–d.20 boundary-sweep audit — keep this flag visible until d18-dubia clears.**

## d.18 chunk inventory (in semantic order)

- ~~`d18-littera`~~ **DONE 2026-05-25.**
- **`d18-divisio`** — COMMENTARIUS + DIVISIO TEXTUS + TRACTATIO QUAESTIONUM (no pars split). — NEXT. (skeleton)
- `d18-a1-q1` (skeleton)
- `d18-a1-q2` (skeleton)
- `d18-a1-q3` (skeleton)
- `d18-a2-q1` (skeleton)
- `d18-a2-q2` (skeleton)
- `d18-a2-q3` (skeleton)
- `d18-dubia` (skeleton; ⚠ manual-rescue)

## Prior session (2026-05-25, d.17 ninth chunk — d17-dubia promotion; d.17 CLOSED)

Promoted `d17-dubia` Tier-2:
- *Dubia circa litteram Magistri (Dist. XVII).* Spans p.426 R band 1 (DUBIA CIRCA LITTERAM MAGISTRI header + DUB I opener immediately after d17-a2-q3 SCHOLION II close at raw 30010) → p.426 R band 2 (DUB II opener) → p.427 L (DUB II body 3-opinion structure: *Opinio 1.* corporalis / *Opinio 2.* spiritualis / *Opinio 3 cum distinctione.* with *Subdistinctio.* + *Alia subdistinctio.* + Damascene cit. + *Rationes congruentiae.*) → p.427 R (DUB II *Ad obiecta.* close + DUB III opener with sphaera ignis + Augustinus subtilitas argg. + Respondeo *quodam modo vergens ad meridiem*) → p.428 L (DUB III close + DUB IV opener + Respondeo *Triplex differentia lignorum.* corporis/animae/coniuncti) → p.428 R (DUB IV Augustinus *de Civ. Dei* citation + DUB V opener with 3 obiecta + Respondeo *Duplex finis.* + *Mandatum disciplinae.*) → p.429 L band 0 (DUB V close at *Alia satis patent per iam dicta.* immediately before DISTINCTIO XVIII. at raw 30201).
- **5 dubia** (DUB I–V).
- **22 apparatus entries [^1]–[^22].** Page-split map: p.426 R-2 footers 1–4 = [^1]–[^4] (Sive non absoluta conditionata / In edd. 2,3,4 et Vat. desideratur habitationi sit congruus / Hic c. 5 / Sub hoc respectu Isidor. XIV Etymol. c. 3. n. 2 hortus deliciarum block); p.426 R-2 footer 5 + p.427 L-2 footer 1 (continuation across page break) = [^5] (Vers. 43 + Ezech. 28, 13 + Origenes IV Periarch. n. 16 + Epiph./Anastasius lengthy block); p.427 L-2 footer 2 = [^6] (Damascene *de Fide orthod.* II c. 11); p.427 R-2 footers 2–7 = [^7]–[^12] (Cfr. August. VIII de Gen ad lit c. 11 + Alex. Hal. sex rationes / Sive atrium + commentator cross-refs / Cfr. supra pag. 321 nota 4 / De Gen. ad lit. imperf. c. 14 + III c. 6 / Vide Damasc. II de Fide orthod. c. 11 + Bedam et Strabum / Ita cod. aa second hand + alii incongrue esse contemperantiam); p.428 L-2 footers 1–4 = [^13]–[^16] (Idem dubium Alex. Hal./Albert + Thomas Apostolus paradisus lunarem globum quote / Nempe lignum vitae et scientiae / In cod. V additur paradisi + universalitas vs universitas lignorum / Plures codd. ed. 2 spirituales); p.428 R-2 footers 5–9 = [^17]–[^21] (Nam secundum Aristot. I Elench. + II de Caelo opposita iuxta se posita / Libr. XIII c. 20 textus originalis mirabili Dei gratia praestabatur / Secundum August. XIII de Civ. Dei c. 20 + VIII de Gen ad lit + Alex. Hal./Albert/Aegid / Cfr. Ambros. de Paradiso + August. VIII de Gen ad lit c. 13 + XIV de Civ. Dei + Edd. homine / Vat. cui pro de quo Deo); p.429 L-2 footer 1 = [^22] (Vat. cum nonnullis codd. *spiritualis*).
- Marginal labels preserved inline per locked Vol II convention: *Quaestio connexa.*, *Ad quaest. connexam.*, *Opinio 1./2./3 cum distinctione.*, *Subdistinctio.*, *Alia subdistinctio.*, *Rationes congruentiae.*, *Ad obiecta.*, *Triplex differentia lignorum.*, *Duplex finis.*, *Mandatum disciplinae.*
- `has_scholion: false` — DUBIA chunks in d.17 carry no SCHOLION by design; d.17 doctrinal scholia live in q-chunks (a1-q1/q2/q3, a2-q1/q3).
- No `[?]` flags — all 22 anchors + 10 marginal labels crisp at 450 dpi across pp.426–429. OCR around raw 30010–30200 is two-column cascade-fragmented; column-band PDF read authoritative per Vol II Override.
- Cross-chunk hand-off: received nothing from d17-a2-q3 (p.426 L footers consumed by q3). No forward hand-off to d18-littera (d.18 opens p.429 L-1 with its own NOTAE AD LIBR. SENTENTIARUM apparatus block).
- Audits: paraphrase NO flags (0 critical / 0 high — first time across d.17 promotion that the full distinction lands clean); apparatus-count flag CLEARED for d17-dubia (last d.17 skeleton-suspect flag now gone — d.17 fully clean); header audit NO LOSS flags — **d.17 final clean state achieved**.
- Build: 611 → 612 translated, 879 quaestio routes.

## d.17 inventory — ALL DONE 2026-05-25

All nine d.17 chunks promoted Tier-2 in a single day:
`d17-littera`, `d17-divisio`, `d17-a1-q1`, `d17-a1-q2`, `d17-a1-q3`,
`d17-a2-q1`, `d17-a2-q2`, `d17-a2-q3`, `d17-dubia`.

## What to do this session

**Promote `d18-littera`** — first d.18 chunk. d.18 opens at raw 30201 with `DISTINCTIO XVIII. — Cap. I. De formatione mulieris.` on p.429 L-1 immediately after d17-dubia DUB V close at *Alia satis patent per iam dicta.* **d.18 pars-split determination: d.18 has NO pars split.** Running heads read `DIST. XVIII. ART. I/II.` only — `P. I.` / `P. II.` never appears (verified by grep `DIST\. XVIII` against raw OCR running heads at raw 30616/31610/31883). Chunk inventory proceeds with `d18-divisio` (not `d18-p1-divisio`). Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read for every Cap. opener + footer.

**⚠ d18-dubia is a remaining manual-rescue chunk per the d.11–d.20 boundary-sweep audit — keep this flag visible until d18-dubia clears.** Watch for the cascade-merge signature when the d18-dubia boundary is reached.

Remaining d.18 chunk inventory after d18-littera: `d18-divisio`, `d18-a1-q1`, `d18-a1-q2`, `d18-a1-q3`, `d18-a2-q1`, `d18-a2-q2`, `d18-a2-q3`, `d18-dubia` (⚠ manual-rescue).

## Prior session (2026-05-25, d.17 eighth chunk — d17-a2-q3 promotion)

Promoted `d17-a2-q3` Tier-2:
- *Utrum corpus Adae constitutum fuerit ex elementis in complexione et compositione aequali.* Spans p.424 L band 0 (QUAESTIO III header + italic title + opener `Tertio quaeritur, utrum corpus primi hominis constitutum fuerit ex elementis in complexione et compositione aequali. Et quod sic, videtur.` immediately after q2 *habitatio caeli empyrei* close on p.423 R band 1; raw 29847) → p.424 L bands 1–2 (Argg. pro parte affirmativa args 1–4) → p.424 R bands 0–2 (Sed contra / Pro parte negativa args 1–5 begin) → p.425 L (arg 5 close + arg 6 + CONCLUSIO + Respondeo with *Duplex aequalitas miscibilium.* + *Aequalitas a pondere modo 1./2./3.* openers) → p.425 R (*Conclusio 1.* + *Ad rationes pro parte negativa.* + *Aequalitas a iustitia.* + *Triplex est aequalitas secundum 3 status.* + *Conclusio 2.* opener) → p.426 L band 0 (*Ad rationes pro parte affirm.* paragraph; closes at *ita patet responsio ad totum.* on p.426 R band 0) + SCHOLION I (Avicenna *de medicina* source + Petr. a Tar. gold/lead exemplum gloss on equiparation vs. proportion) + II (commentator list Alex. Hal. S. p. II q. 77 m. 2 a. 1–2 + Petr. a Tar. + Richard. a Med. + back-pointer to q.1 scholion). Closes immediately before `DUBIA CIRCA LITTERAM MAGISTRI` opener at p.426 R band 1 / raw 30010.
- **10 apparatus entries [^1]–[^10].** Page-split map: p.424 L footers 1–4 = [^1]–[^4] (Cfr. supra pag. 380 nota 1 / Vat. *iniustitiae* / Avicenna Canon I Fen 1 doctr. 3 c. 1 heat-of-life block / Aristot. II de Partib. animal. + Avicenna phlegm/melancholy block); p.424 R footers 5–7 = [^5]–[^7] (Aristot. I de Caelo text 7 + Averroes + cod. aa gloss / Averroes II de Generat. text 18 + IV Meteor + X Metaph + Galen impugnat + Vat. *fuit* supplement / Aug. XIII de Civ. Dei c. 20+23 + XIV c. 26 + I de Peccatorum meritis c. 3 + d.19 forward pointer); p.425 L footer 1 = [^8] (Avicenna Canon I Fen 1 doctr. 3 c. 1 *iustitia in divisione* block); p.425 R footers 2–3 = [^9]–[^10] (Vat. *ratione* / edd. 2,3,4 + Vat. deest *reperitur in his quae miscentur naturaliter*).
- Marginal labels preserved inline per locked Vol II convention: *Argg. pro parte affirmativa.*, *Pro parte negativa.*, *Duplex aequalitas miscibilium.*, *Aequalitas a pondere modo 1./2./3.*, *Conclusio 1./2.*, *Ad rationes pro parte negativa./affirm.*, *Aequalitas a iustitia.*, *Triplex est aequalitas secundum 3 status.*
- `has_scholion: true` — SCHOLION I substantial doctrinal scholion (Avicenna *de medicina* as source for the *a pondere* / *a iustitia* distinction + Petr. a Tar. gold/lead exemplum gloss); II = q3-specific commentator list.
- No `[?]` flags — all 10 anchors + 12 marginal labels crisp at 450 dpi across pp.424–426. OCR around raw 29847–30009 is two-column cascade-fragmented (`QUAESTIO 111.` header + `lll` Roman-numeral garble + diagonal token reorder around CONCLUSIO/Respondeo splice + marginal-label bleed-through); column-band PDF read authoritative per Vol II Override. **The OCR raw 29847 `QUAESTIO 111.` line is the printed-p.424 header pulled above the p.423 R-2 footer block by the cascade** — verified column-band PDF assigns it to p.424 L band 0.
- Cross-chunk hand-off: received nothing from d17-a2-q2. Forward hand-off to d17-dubia: none — p.426 R band 2 footers 4–5 (Vers. 43 + Isidor. XIV Etymol. c. 3 + Origenes Periarch. IV n. 16) all anchor in DUB I/II body, which d17-dubia owns.
- Audits: paraphrase HIGH (1 chunk, expected first-pass); apparatus-count flag CLEARED for d17-a2-q3 (only d17-dubia +18 skeleton-suspect flag persists — clears as it promotes); header audit NO LOSS flags (ART +3 / QUAEST +5 / DUB +0).
- Build: 610 → 611 translated, 879 quaestio routes.

## What to do this session

**Promote `d17-dubia`** — ninth and final d.17 chunk. DUBIA CIRCA LITTERAM MAGISTRI opens on p.426 R band 1 at raw 30010 with `DuB. I.` immediately after q3 SCHOLION II close. Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read for p.426 R + p.427+. p.426 crops already cached at `/tmp/colcrop/vol2-p426-*`; generate p.427+ as needed. d.17 closes with this chunk.

## d.17 chunk inventory (in semantic order)

- ~~`d17-littera`~~ **DONE 2026-05-25.**
- ~~`d17-divisio`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q1`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q2`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q3`~~ **DONE 2026-05-25.**
- ~~`d17-a2-q1`~~ **DONE 2026-05-25.**
- ~~`d17-a2-q2`~~ **DONE 2026-05-25.**
- ~~`d17-a2-q3`~~ **DONE 2026-05-25.**
- **`d17-dubia`** — NEXT. (skeleton)

## Prior session (2026-05-25, d.17 seventh chunk — d17-a2-q2 promotion)

Promoted `d17-a2-q2` Tier-2:
- *Utrum corpus Adae constitutum fuerit ex natura pure elementari.* Spans p.420 R band 2 bottom (QUAESTIO II header + italic title + opener `Secundo quaeritur, utrum corpus primi hominis constitutum fuerit de natura pure elementari, an simul cum natura elementari concurrerit natura caelestis ad eius constitutionem.` immediately after q1 SCHOLION II commentator list close at raw 29621) → p.421 (*Ad oppositum* args 1–6 + Contra/*Fundamenta* args 1–2) → p.422 (Fundamenta args 3–6 + CONCLUSIO + Respondeo with *Opinio 1.* + *Improbatur.* + *Opinio 2.* + *Non probatur.* + *Opinio 3 cum distinctione.* + *Membrum 1 distinctionis.* + *Conclusio 1.* opener) → p.423 (Conclusio 1 close + *Membrum 2.* + *Conclusio 2.* + Iuxta hanc tertiam viam response-to-question + *Solutio oppositorum* ad 1–6 with *Triplex lux.* + *Notandum.* (×2) closing at *habitatio caeli empyrei*). Closes immediately before QUAESTIO III opener on p.423 R band 2 at raw 29847.
- **17 apparatus entries [^1]–[^17]** (+ supplementary keys `[^16-bis]` and `[^17b]` to accommodate Quaracchi's per-page restart at p.423 L footer 5 and R footer 7). Page-split map: p.421 L footers 1–4 = [^1]–[^4] (Aug. VII *de Gen ad lit* c.13+19 + Avicenna *de Anima* p.IV c.6 lengthy block / Aristot. *de Animalibus* old/new division + Virgil *Aen.* 6.730 + VII Metaph. text 3 + Porphyr. *de Praedicab.* / d.14 p.I a.1 q.2 + p.II a.2 q.2 cross-refs / Alanus ab Insulis II *de Articul. cath. fidei* prop. 13 lengthy block); p.421 R footers 5–6 = [^5]–[^6] (Aug. *super Gen ad lit* III c.4 n.6 / Aristot. I *de Generat. et corrupt.* text 87 + d.8 p.I a.2 q.2 *corporis quinti* cross-ref); p.422 L footers 1–3 = [^7]–[^9] (d.13 a.3 q.1 + *radium* vs *per radium* / Cod. cc + ed. 1 *eo* / Aristot. II *de Anima* text 11+21 + codd. V W *sensum* pro *sensificationem*); p.422 R footers 4–7 = [^10]–[^13] (Aug. VII *de Gen ad lit* c.21 n.27 + d.14 p.I a.1 q.2 / Part. I a.1 q.2 in corp. / Nonnulli codd. *animale* / Vat. *formam*); p.423 L footers 1–3 = [^14]–[^16] (Multi codd. *sublimatione* / Quaest. seq. / codd. D O Y cc ed. 1 *secundum virtutem* + Vat. omittit *secundum virtutem* + post *magis quam* codd. *secundum*); p.423 R footers 4–8 = [^16-bis], [^17b], [^17] (Fide codd. supplevimus *responsio ad quaestionem propositam* + Vat. *mediante anima rationali* / Vat. *mediante anima rationali* pro *in homine* / Cap. 5 n.7 super Gen. / Vat. interpunctione *Et quia cum haec* / Vide scholion ad praecedentem quaest. — collected into [^16-bis] (Cap. 5 cit. anchored at *Ad 5* end), [^17b] (Vat. interpunct. gloss anchored at *Et quia haec*), and [^17] (closing *Vide scholion* pointer)).
- Marginal labels preserved inline: *Ad oppositum.*, *Fundamenta.*, *Opinio 1.*, *Improbatur.*, *Opinio 2.*, *Non probatur.*, *Opinio 3 cum distinctione.*, *Membrum 1 distinctionis.*, *Conclusio 1.*, *Membrum 2.*, *Conclusio 2.*, *Solutio oppositorum.*, *Triplex lux.*, *Notandum.* (×2).
- `has_scholion: false` — per locked Vol II sibling-shared-scholion pattern (cf. d16-a1-q2, d16-a2-q2), q2's closing [^17] explicitly points back to q1 SCHOLION I via *Vide scholion ad praecedentem quaest.*
- No `[?]` flags — all 17 anchors + 15 marginal labels crisp at 450 dpi across pp.420–423.
- Cross-chunk hand-off: received nothing from d17-a2-q1 (p.420 R band 2 footers ⁴–⁶ all anchored in q1 body, consumed as q1 [^15]–[^17]). Forward hand-off to d17-a2-q3: none — q3 opens p.423 R band 2 with its own opener + fresh p.424 footer sequence.
- Audits: paraphrase HIGH (1 chunk, expected first-pass); apparatus-count flag CLEARED for d17-a2-q2 (2 skeleton-suspect flags persist on d17-a2-q3 +19 and d17-dubia +18 — clears as they promote); header audit NO LOSS flags (ART +2 / QUAEST +3 / DUB +0).
- Build: 609 → 610 translated, 879 quaestio routes.

## What to do this session

**Promote `d17-a2-q3`** — eighth d.17 chunk. QUAESTIO III opens on p.423 R band 2 at raw 29847 immediately after q2 closing line `habitatio caeli empyrei`. No cross-chunk footer migrates from d17-a2-q2. Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read for p.423 R + p.424+. p.423 crops cached at `/tmp/colcrop/vol2-p423-*`; generate p.424+ as needed.

## d.17 chunk inventory (in semantic order)

- ~~`d17-littera`~~ **DONE 2026-05-25.**
- ~~`d17-divisio`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q1`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q2`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q3`~~ **DONE 2026-05-25.**
- ~~`d17-a2-q1`~~ **DONE 2026-05-25.**
- ~~`d17-a2-q2`~~ **DONE 2026-05-25.**
- **`d17-a2-q3`** — NEXT. (skeleton)
- `d17-dubia` (skeleton)

## Prior session (2026-05-25, d.17 sixth chunk — d17-a2-q1 promotion)

Promoted `d17-a2-q1` Tier-2:
- *Utrum corpus Adae debuerit produci de natura pure caelesti.* Spans p.418 R band 1 bottom (ARTICULUS II header + subtitle *De productione hominis quoad corpus.* + opener `Consequenter quaeritur de productione primi hominis ex parte corporis. Et circa hoc quaeruntur tria.` + 3-question sub-divisio folded in per locked Vol II Override step 5; raw 29467) → p.419 (QUAESTIO I header + title + 4 Ad oppositum argg. + Sed contra/Fundamenta argg. 1–4 + CONCLUSIO + Respondeo opener with *Conclusio 1.* + *Conclusio 2.* + *Quadruplex ordo.* + *Ordo hominis in se*) → p.420 (Ad creaturam inferiorem + Ad creaturam parem + Ad Deum finem + Solutio oppositorum ad 1–4 with *Notandum.* + SCHOLION I + II commentator list). Closes immediately before QUAESTIO II opener on p.420 R band 2 at raw 29621.
- **17 apparatus entries [^1]–[^17].** Page-split map: p.419 L footers 1–5 = [^1]–[^5] (Cfr. supra pag. 380 + Y aa supplied conclusion / pag. 216 + 346 / Aristot. II Phys. + d.2 p.II a.2 q.1 cross-ref / Cod. W *et ideo si* / Aristot. III de Anima); p.419 R footers 6–11 = [^6]–[^11] (Sive *operatione* + d.13 a.1 q.2 / Aristot. II de Anima text 31 / Aristot. I de Caelo text 7 / Cap. 2,7 + *quem*/*quam* codex variant / Codd. F l aa vs Vat. *vero* / Dist. 15 a.2 q.1 + infra pag.421 forward pointer); p.420 L footers 1–3 = [^12]–[^14] (Vat. *Deum finem* + F l *Deo* / Vat. *etsi* / *illuc* desideratur ed. 1); p.420 R footers 4–6 = [^15]–[^17] (Gen. 2,8 / Dist. 49 p.II / Unus alterque cod. *defectum*).
- Marginal labels preserved inline: *Ad oppositum.*, *Fundamenta.*, *Conclusio 1./2.*, *Quadruplex ordo.*, *Ordo hominis in se.*, *Ad creaturam inferiorem.*, *Ad creaturam parem.*, *Ad Deum finem.*, *Solutio oppositorum.*, *Notandum.*
- `has_scholion: true` — SCHOLION I brief doctrinal note tying article's three qq. to Alex. Hal. S. p. II. q. 77 + q. 81 m. 1 + d. 15. a. 1. q. 2–3 supposita; II = q1 commentator list (Scot. + Hier. de Montefortino + S. Thom. + B. Albert + Petr. a Tar. + Richard. a Med. + Aegid. R. + Dionys. Carth.).
- ARTICULUS II opener + 3-question sub-divisio folded into a2-q1 per locked Vol II Override step 5.
- No `[?]` flags — all 17 anchors + 11 marginal labels crisp at 450 dpi across pp.418–420.
- Cross-chunk hand-off: received nothing from d17-a1-q3; forward to d17-a2-q2: none (p.420 R footers 4–6 all anchor in q1 body; q2 opens p.420 R band 2 with own opener + fresh p.421 footer sequence).
- Audits: paraphrase HIGH (1 chunk, expected first-pass); apparatus-count flag CLEARED for d17-a2-q1 (3 skeleton-suspect flags persist on d17-a2-q2/q3/dubia — clears as they promote); header audit NO LOSS flags (ART +2 / QUAEST +2 / DUB +0).
- Build: 608 → 609 translated, 879 quaestio routes.

## What to do this session

**Promote `d17-a2-q2`** — seventh d.17 chunk. QUAESTIO II opens on p.420 R band 2 at raw 29621 with `QUAESTIO II.` header + italic title *Utrum corpus Adae constitutum fuerit ex natura pure elementari* + opener `Secundo quaeritur, utrum corpus primi hominis constitutum fuerit de natura pure elementari, an simul cum natura elementari concurrerit natura caelestis ad eius constitutionem.` No cross-chunk footer migrates from d17-a2-q1. Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read for p.420 R + p.421+. p.420 crops already cached; generate p.421+ as needed.

## d.17 chunk inventory (in semantic order)

- ~~`d17-littera`~~ **DONE 2026-05-25.**
- ~~`d17-divisio`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q1`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q2`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q3`~~ **DONE 2026-05-25.**
- ~~`d17-a2-q1`~~ **DONE 2026-05-25.**
- **`d17-a2-q2`** — *Utrum corpus Adae constitutum fuerit ex natura pure elementari.* — NEXT. (skeleton)
- `d17-a2-q3` (skeleton)
- `d17-dubia` (skeleton)

## Prior session (2026-05-25, d.17 fifth chunk — d17-a1-q3 promotion)

Promoted `d17-a1-q3` Tier-2:
- *Utrum anima Adae fuerit producta ante corpus, vel postea.* Spans p.416 R band 1 (QUAESTIO III header + italic title + opener `Tertio quaeritur, utrum anima Adae producta fuerit ante corpus, vel postea. Et quod ante, videtur:` immediately after q2 SCHOLION II close on p.416 R band 1 top) → p.416 R band 2 (Ad oppositum args 1 close) → p.417 L (args 4–6 + Contra/Fundamenta args 1–3 + arg 4 opener) → p.417 R (Fundamenta args 3–6 close + CONCLUSIO + Respondeo with *Dubitat Augustinus.* + *Conclusio.* + *Rationes Augustini.* + *Rationes pro conclusione.* + Solutio ad 1–2 begin) → p.418 L (ad 2 close + ad 3 with *Et praeterea.* + ad 4 opener) → p.418 R (ad 5–6 with *Notandum.* closing at *suo loco quaeretur.* + SCHOLION I (Origen/Plato pre-existence Concilio V can.1 anathema) + SCHOLION II (Alex. Hal. + S. Thom. + B. Albert + Petr. a Tar. + Aegid. R. commentator list)). Closes immediately before `ARTICULUS II.` opener on p.418 R band 1 at raw 29467.
- **22 apparatus entries [^1]–[^22].** Page-split map: p.416 L footers 1–3 = [^1]–[^3] (inherited per q2 forward hand-off: Vers. 26 + Cfr. supra pag. 398 nota 5 + Vide supra d.2 p.I a.1 q.1); p.416 R footers 4–5 = [^4]–[^5] (Aristot. *absolutum/dependens* + Vat. *extra corpus*); p.417 L footers 1–5 = [^6]–[^10] (Vers. 7 + Aristot. II de Anima text 26 + d.15 a.2 q.2 + Cfr. supra pag. 330 nota 5 + Cfr. infra d.18 a.2 q.2 fundam. 3 with cod. cc *et* gloss); p.417 R footers 6–11 = [^11]–[^16] (Aug. VII de Gen ad lit c.25 + X de Civ. Dei c.30 + Aristot. I de Anima text 53 cod. cc *antequam culpa* / Aug. VII de Gen ad lit c.24 / Plures codd. *ostenderet* + d.16 a.2 q.1 + d.1 p.II a.2 q.2 cross-refs / Vat. *perperam tamen* / Scriptura *totum* pro *parte* / Aug. VI de Gen ad lit c.1); p.418 L footers 1–2 = [^17]–[^18] (d.15 a.2 q.2 + d.1 p.II a.2 q.2 cross-refs with *consummat*/*conserve* variants + Vat. *etsi* gloss with edd. 3,4 *etsi in quantum* omission); p.418 R footers 3–6 = [^19]–[^22] (Non pauci codd. *non dependet* + Apoc. 22:13 + Eccli. 1:4 with d.2 p.I a.2 q.3 + d.10 a.2 q.2 + d.15 a.2 q.1 cross-refs + Dist. 18 a.2 q.2 forward pointer).
- Marginal labels preserved inline per locked Vol II convention: *Ad oppositum.*, *Fundamenta.*, *Dubitat Augustinus.*, *Conclusio.*, *Rationes Augustini.*, *Rationes pro conclusione.*, *Solutio oppositorum.*, *Notandum.*, *Et praeterea.* inline italic.
- `has_scholion: true` — SCHOLION I substantial doctrinal scholion (Concilio generali V can. 1 anathema on Origen/Plato pre-existence + forward pointer to d.18 a.2 q.2 + speciatim treatment of *anima primi parentis*); II = q3 commentator list (Alex. Hal. S. p. II q. 60 m. 2 a. 2 + S. Thom. S. I q. 91 a. 4 ad 3 + B. Albert hic a. 2 + S. p. II tr. 12 q. 72 m. 4 a. 1 + Petr. a Tar. hic q. 1 a. 3 quaestiunc. 1 + Aegid. R. hic q. 2 a. 2).
- No `[?]` flags — all 22 anchors + 8 marginal labels crisp at 450 dpi across pp.416–418. OCR around raw 29326–29466 is two-column cascade-fragmented (`QU\EST10 111.` header garble + diagonal token reorder around CONCLUSIO/Respondeo splice + marginal-label bleed-through); column-band PDF read authoritative per Vol II Override.
- Cross-chunk hand-off received from d17-a1-q2: p.416 L footers 1–3 migrate here as [^1]–[^3]. Forward hand-off to d17-a2-q1: none — ARTICULUS II opens on p.418 R band 1 with its own *Consequenter quaeritur de productione primi hominis ex parte corporis* + 3-question sub-divisio (fold-in per Vol II Override step 5); p.418 R footers 3–6 all anchor in q3 body.
- Audits: paraphrase HIGH (1 chunk, expected first-pass over OCR-cascade base); apparatus-count flag CLEARED for d17-a1-q3 (4 skeleton-suspect flags persist on d17 a2-*/dubia siblings — clears as they promote); header audit NO LOSS flags (ART +1 / QUAEST +0 / DUB +0).
- Build: 607 → 608 translated, 879 quaestio routes.

## What to do this session

**Promote `d17-a2-q1`** — sixth d.17 chunk. ARTICULUS II opens on p.418 R band 1 with `ARTICULUS II.` + subtitle *De productione hominis quoad corpus.* + opener `Consequenter quaeritur de productione primi hominis ex parte corporis. Et circa hoc quaeruntur tria.` followed by 3-question sub-divisio (folded into a2-q1 per Vol II Override step 5). QUAESTIO I header at raw 29492. No cross-chunk footer migrates from d17-a1-q3 (all p.418 footers consumed). Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read for p.418+. p.418 crops already cached at `/tmp/colcrop/vol2-p418-*`; generate p.419+ as needed.

## d.17 chunk inventory (in semantic order)

- ~~`d17-littera`~~ **DONE 2026-05-25.**
- ~~`d17-divisio`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q1`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q2`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q3`~~ **DONE 2026-05-25.**
- **`d17-a2-q1`** — *Utrum corpus primi hominis productum fuerit ex natura caelesti.* — NEXT. (skeleton)
- `d17-a2-q2` (skeleton)
- `d17-a2-q3` (skeleton)
- `d17-dubia` (skeleton)

## Prior session (2026-05-25, d.17 fourth chunk — d17-a1-q2 promotion)

Promoted `d17-a1-q2` Tier-2:
- *Utrum anima Adae fuerit producta ex materia.* Spans p.413 L band 1 (QUAESTIO II header + italic title + opener `Secundo quaeritur, utrum anima Adae producta fuerit ex materia. Et quod non, videtur:` immediately after q1 SCHOLION II commentator list close on p.413 L band 0 at `In solutione ad 3. notanda est expositio verborum S. Augustini`) → p.413 R bands 0–1 (Ad oppositum args 1–6 + Sed contra/Fundamenta args 1–3 begin) → p.414 L (Fundamenta args 3–6 close + CONCLUSIO + Respondeo *Opinio 1.* + *Non probatur.* + *Opinio 2.*) → p.414 R (Opinio 2 *Non probatur.* + *Opinio 3.* opener) → p.415 L (Opinio 3 body with *Conclusio 1./2./3.* + *Corollarium* + Solutio ad 1–4 with *Ratio notabilis 1.* + *Alia ratio.*) → p.415 R (ad 4 close + ad 5 with *Multiplex simplicitas.* + *Notandum.* + ad 6 with *Notandum.*) → p.416 L band 0 (ad 6 close at *appetitum ad suscipiendam animam.*). SCHOLION I (substantial: S. Thomas + Richard + Alex. Hal. + Petr. a Tar.) + SCHOLION II (Scotus / Albert / Aegid. R. commentator list) on p.416 L band 0 bottom → R band 1, closing immediately before QUAESTIO III opener.
- **24 apparatus entries [^1]–[^24].** Page-split map: p.413 L footers 1–5 = [^1]–[^5]; p.413 R footers 6–10 = [^6]–[^10]; p.414 L footers 1–4 = [^11]–[^14] (incl. [^13] = Aug. de Trin. c.2 + de Hebdomadibus + de Unitate et uno + Moribus Manich. + In Ioan. tract. 19 + Spirit. et anima c.36 + Bernard. Cant. serm. 81 *anima vivens se ipsa* block); p.414 R footers 5–6 = [^15]–[^16]; p.415 L footers 1–4 = [^17]–[^20]; p.415 R footers 5–8 = [^21]–[^24] (incl. [^24] *autem* cod. cc + Vat. *corporalem materiam* + *sustinendam animam* variants). p.416 carries no body apparatus — L band 2 footer (Vers. 26 / Cfr. pag. 398 / Vide supra d.2 p.I a.1 q.1) anchors in QUAESTIO III opener and migrates forward to d17-a1-q3.
- Marginal labels preserved inline per locked Vol II convention: *Ad oppositum.*, *Fundamenta.*, *Opinio 1./2./3.*, *Non probatur.* (×2), *Conclusio 1./2./3.*, *Corollarium.*, *Solutio oppositorum.*, *Ratio notabilis 1.*, *Alia ratio.*, *Multiplex simplicitas.*, *Notandum.* (×2).
- `has_scholion: true` — SCHOLION I is a substantial doctrinal scholion (S. Thomas Sum. I q.75 a.5 + S.c.G. II c.30 parallel reading; Richard's *unigenea* materia distinction; Alex. Hal. spiritualis-materia magnitudo; Petr. a Tar. on the now-obsolete-but-once-*celebris* materia-spiritualis opinion); II = q2 commentator list.
- No `[?]` flags — all 24 anchors + 13 marginal labels crisp at 450 dpi across pp.413–416. Column-band PDF read authoritative per Vol II Override; OCR around raw 29107–29473 is two-column cascade-fragmented.
- Cross-chunk hand-off: received nothing from d17-a1-q1 (q1's last body anchor sat on p.412; p.413 L band 0 holds q1's SCHOLION only). Forward hand-off to d17-a1-q3: p.416 L band 2 footers 1–3 migrate.
- Audits: paraphrase HIGH (1 chunk, expected first-pass); apparatus-count flag CLEARED for d17-a1-q2 (5 skeleton-suspect flags persist on d17 a*/dubia siblings — clears as they promote); header audit Q-LOSS -1 still fires because d.17 a2-siblings + dubia skeleton — clears as those promote.
- Build: 606 → 607 translated, 879 quaestio routes.

## What to do this session

**Promote `d17-a1-q3`** — fifth d.17 chunk. QUAESTIO III opens on p.416 R band 1 with `QUAESTIO III.` header + italic title *Utrum anima Adae fuerit producta ante corpus, vel postea.* + opener `Tertio quaeritur, utrum anima Adae producta fuerit ante corpus, vel postea. Et quod ante, videtur: 1. Per textum Genesis primo: Faciamus hominem ad imaginem etc.` Per the d17-a1-q2 forward hand-off, p.416 L band 2 footers 1–3 (Vers. 26 = Gen. 1, 26 + Cfr. supra pag. 398 nota 5 + Vide supra d.2 p.I a.1 q.1) migrate here as the first apparatus entries. Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read for p.416+. p.416 crops already cached at `/tmp/colcrop/vol2-p416-*`; generate p.417+ as needed.

## d.17 chunk inventory (in semantic order)

- ~~`d17-littera`~~ **DONE 2026-05-25.**
- ~~`d17-divisio`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q1`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q2`~~ **DONE 2026-05-25.**
- **`d17-a1-q3`** — *Utrum anima Adae fuerit producta ante corpus, vel postea.* — NEXT. (skeleton)
- `d17-a2-q1` (skeleton)
- `d17-a2-q2` (skeleton)
- `d17-a2-q3` (skeleton)
- `d17-dubia` (skeleton)

## Last session (2026-05-25, d.17 third chunk — d17-a1-q1 promotion)

Promoted `d17-a1-q1` Tier-2:
- *Utrum anima humana sit ex Dei substantia.* Spans p.410 R band 1 bottom (QUAESTIO I header + italic title + opener `Circa primum sic proceditur et ostenditur, quod anima humana sit ex Dei substantia.` immediately after d17-divisio ARTICULUS I header+subtitle close) → p.410 R band 2 (Ad oppositum arg 1 first-half) → p.411 L (args 1 close + args 2–5 + arg 6 opener + Contra/Fundamenta args 1–2 + arg 3 opener) → p.411 R (args 3–6 close + CONCLUSIO + Respondeo *Opinio 1.* + *Improbatur.* + *Opinio 2.* opener) → p.412 L (Opinio 2 Manichaean + *Refellitur.* + *Sententia catholica et conclusio.* + Solutio oppositorum ad 1–2) → p.412 R (ad 3 *Genus dupliciter.* + *Notandum de luce creata.* + ad 4–6 with *Lux corporalis differt a spirituali.*) → p.413 L band 0 (ad 6 close at `sit nata coniungi materiae.`). SCHOLION I+II on p.413 L band 1 / R band 0 between Q1 body close and QUAESTIO II opener.
- **19 apparatus entries [^1]–[^19]** continuously renumbered. Page-split map: p.410 R footers 3–5 = [^1]–[^3] (received per d17-divisio hand-off: Vers. 7 + Aug. Manichaean attribution / Cap. 20, 22 Glossa interlinearis from August. in Ioan. tract. 121 / Vers. 7 Eccles. *Et revertatur pulvis*); p.411 L footers 1–4 = [^4]–[^7] (Acts 17:28 Vat. *philosophorum nostrorum* variant / David of Dinant *de tomis* cit. / 1 Tim. 6:16 + de Spiritu et anima c.18 + Cassiodorus de Anima c.8 / Manichaean visible-light Aug. *de Haeresibus* c.46 + *finis* pro *fons* variant); p.411 R footers 5–9 = [^8]–[^11] (Gen 1:26 + Aug. cross-refs / I Sent. d.8 p.II q.2 / I Sent. d.19 p.II q.3 / `Non pauci codd. incongrue hoc`); p.412 L footers 1–4 = [^12]–[^15] (Aug. de Duabus Animabus c.1 + Retract. + cod-variant *facere mala* lacuna / d.31 + d.34 + d.1 cross-refs / `Intellige exemplaris` Y aa codex variant + Vat. ed.4 *quia quod se habet ut materiale* / Aug. VII de Gen ad lit + XIII de Civ. Dei + Vat. *verbo*/*dicendo*); p.412 R footers 5–8 = [^16]–[^19] (John 20:22 Greek ἐνεφύσησε + Aug. VII de Gen ad lit + lit. Magistri c.2 + Vat. *Insufflavit* / Confess. I c.1 n.1 *inquietum cor* / Cap. 15 n. 24 de Trin. + de Humanae Cognitionis ratione + Vat. *spiritualis* pro *specialis* / Dist. 19 a.1 q.1 + I Sent. d.8 p.II a.2 q.2 cross-refs). p.413 carries no body apparatus (SCHOLION-only column).
- Marginal labels preserved inline per locked Vol II convention: *Ad oppositum.*, *Fundamenta.*, *Opinio 1.*, *Improbatur.*, *Opinio 2.*, *Refellitur.*, *Sententia catholica et conclusio.*, *Solutio oppositorum.*, *Genus dupliciter.*, *Notandum de luce creata.*, *Lux corporalis differt a spirituali.*
- `has_scholion: true` — SCHOLION I = substantial doctrinal scholion citing Dionys. Carth. on the David-of-Dinant / Manichaean error + the *lux sui generis* exposition (cross-ref I Sent. d. 3 p. I q. 1 scholion) + light-as-form cross-ref (d. 13 a. 2 q. 2); II = q1 commentator list (Alex. Hal., Scotus, Thomas, Albert, Petr. a Tar., Aegid. R., Biel).
- No `[?]` flags — all 19 anchors + 11 marginal labels crisp at 450 dpi across pp.410–413. OCR around raw 28950–29100 is two-column cascade-fragmented (`c 0 N c L D s I 0.` CONCLUSIO splice + diagonal token reorder); column-band PDF read authoritative per Vol II Override.
- Cross-chunk hand-off received from d17-divisio: p.410 R footers 3–5 migrate here as [^1]–[^3]. Forward hand-off to d17-a1-q2: none — p.413 carries no q1 body footer; q2 opens p.413 L band 1 with its own *Ad oppositum* argg. and fresh per-page footer sequence on p.414.
- Audits: paraphrase HIGH (1 chunk, expected first-pass over OCR-cascade base); apparatus-count flag CLEARED for d17-a1-q1 (6 skeleton-suspect flags persist on d17 a*/dubia siblings — clears as they promote); header audit Q-LOSS / DUB-LOSS still fires because d.17 siblings are skeleton — clears as those promote.
- Build: 605 → 606 translated, 879 quaestio routes.

## What to do this session

**Promote `d17-a1-q2`** — fourth d.17 chunk. QUAESTIO II opens on p.413 L band 1 with `QUAESTIO II.` header + italic title *Utrum anima Adae fuerit producta ex materia.* + opener `Secundo quaeritur, utrum anima Adae producta fuerit ex materia. Et quod non, videtur:` Per the d17-a1-q1 forward hand-off, no p.413 footer migrates forward (q1's last body anchor [^19] sits at p.412 R band 2). Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read for p.413 + p.414+. p.413 crops already cached at `/tmp/colcrop/vol2-p413-*`; generate p.414+ as needed.

## d.17 chunk inventory (in semantic order)

- ~~`d17-littera`~~ **DONE 2026-05-25.**
- ~~`d17-divisio`~~ **DONE 2026-05-25.**
- ~~`d17-a1-q1`~~ **DONE 2026-05-25.**
- **`d17-a1-q2`** — *Utrum anima Adae fuerit producta ex materia.* — NEXT. (skeleton)
- `d17-a1-q3` (skeleton)
- `d17-a2-q1` (skeleton)
- `d17-a2-q2` (skeleton)
- `d17-a2-q3` (skeleton)
- `d17-dubia` (skeleton)

## Prior session (2026-05-25, d.17 second chunk — d17-divisio promotion)

Promoted `d17-divisio` Tier-2:
- *Commentarius in Distinctionem XVII — De productione Adae quoad
  principia constituentia.* Spans p.410 only (PDF p.432, vol II
  offset +22). Opens at raw 28895 with `COMMENTARIUS IN DISTINCTIONEM
  XVII.` on p.410 L band 0 (immediately after d17-littera p.409 R
  close); holds DIVISIO TEXTUS (L bands 0–2 + R bands 0–1), TRACTATIO
  QUAESTIONUM (L+R band 1), and ARTICULUS I header + subtitle
  *De productione hominis quoad animam.* (R band 1 bottom). Closes
  immediately before `QUAESTIO I.` header on p.410 R band 1.
- **2 apparatus entries [^1]–[^2]** from p.410 L band 2 footer:
  [^1] = *Plures codd. constituentia.* anchored at *constituentia¹*
  in DIVISIO para 1; [^2] = *Vat. hominis iam formati.* anchored
  at *formati²* in DIVISIO para 2. p.410 R band 2 footer notes
  ³–⁵ (Vers. 7 / Cap. 20.22 / Vers. 7) anchor in QUAESTIO I body
  and migrate forward to d17-a1-q1.
- **d.17 pars-split**: confirmed NO pars split — `DIST. XVII. ART.
  I/II.` running heads only.
- **Article fold-in** per locked Vol II Override step 5: divisio
  holds the ART. I header + subtitle. No separate ART. I sub-divisio
  paragraph exists (the 3-question listing `Circa primum quaeruntur
  tria` is already inside TRACTATIO QUAESTIONUM).
- No `[?]` flags — both anchors crisp at 450 dpi. OCR around
  raw 28895–28940 is two-column cascade-fragmented; column-band
  PDF read authoritative per Vol II Override.
- `has_scholion: false` — divisio chunks carry no SCHOLION by design.
- Audits: paraphrase HIGH (1 chunk, expected first-pass over
  OCR-cascade base); apparatus-count flag CLEARED for divisio
  (7 skeleton-suspect flags persist on the d.17 a*/dubia siblings —
  clears as they promote); header audit Q-LOSS / A-LOSS / DUB-LOSS
  fires because d.17 a*/dubia siblings are skeleton (a divisio
  chunk has no ART/QUAEST/DUB headers) — clears as those promote.
- Build: 604 → 605 translated, 879 quaestio routes.

## What to do this session

**Promote `d17-a1-q1`** — third d.17 chunk. QUAESTIO I opens at
raw ~28950 on p.410 R band 1 with `QUAESTIO I.` header + italic
title *Utrum anima humana sit ex Dei substantia.* + opener
`Circa primum sic proceditur et ostenditur, quod anima humana sit
ex Dei substantia.` Per the d17-divisio forward hand-off, p.410 R
band 2 footer notes ³–⁵ (Vers. 7 / Cap. 20.22 / Vers. 7) migrate
here as the first apparatus entries. Standard Vol II Tier-2
procedure: 450 dpi column-band PDF read for pp.410–412.

## d.17 chunk inventory (in semantic order)

- ~~`d17-littera`~~ **DONE 2026-05-25.**
- ~~`d17-divisio`~~ **DONE 2026-05-25.**
- **`d17-a1-q1`** — *Utrum anima humana sit ex Dei substantia.* — NEXT. (skeleton)
- `d17-a1-q2` (skeleton)
- `d17-a1-q3` (skeleton)
- `d17-a2-q1` (skeleton)
- `d17-a2-q2` (skeleton)
- `d17-a2-q3` (skeleton)
- `d17-dubia` (skeleton)

## Prior session (2026-05-25, d.17 first chunk — d17-littera promotion)

Promoted `d17-littera` Tier-2:
- *Distinctio XVII — Littera Magistri*, Cap. I–VII (7 capitula),
  spans p.408 L band 0 bottom (`DISTINCTIO XVII.` + `Cap. I. De
  creatione animae, an de aliquo facta sit.` immediately after
  d16-dubia DUB IV close `...Vel dicendum, quod...`) → p.408 L
  band 1 (Cap. I body + `Cap. II. De insufflatione et inspiratione
  Dei` opener with *Quaestio 1.* + *Opinio haeretica.* marginals) →
  p.408 R bands 0–1 (Cap. II body with *Impugnatur.*, *Quaestio 2.*,
  *Opinio 1.*, *Opinio 2.* marginals + Cap. III opener with
  *Augustinus.* + *Causae superiores.*) → p.409 L bands 0–1 (Cap. III
  Augustine causarum-conditione body with *Dubium 1.* + Cap. IV
  *Quare homo, extra paradisum creatus* with *Dubium 2.* + Cap. V
  *Quibus modis paradisus accipiatur* with *Dubium 3.*) → p.409 R
  bands 0–1 (Cap. V close with *Dubium 4.* + Cap. VI *De ligno vitae*
  + Cap. VII *De ligno scientiae boni et mali* with *Glossa.*,
  *Notandum.*, *Dubium 5.*; closes immediately before
  `COMMENTARIUS IN DISTINCTIONEM XVII.` at raw 28895 / p.410 L
  band 0).
- **15 apparatus entries [^1]–[^15]** continuously renumbered across
  pp.408–409. Page-split map: p.408 L band 2 NOTAE 1 = [^1] (Gen.
  2, 7 + Aug. *de Gen. ad lit.* VIII source attribution); p.408 R
  band 2 footers 2–6 = [^2]–[^6] (codex variant cap. II boundary +
  Isa. 57, 16 LXX/Vulg. + Aug. c. 25. 27 + Cfr. dist. IV/XXIII +
  Aug. VI cc. 13–17 + Exod. 7, 10); p.409 L band 2 footers 1–5 =
  [^7]–[^11] (Vat. *creaturarum* + Gen. 2, 8 + Aug. VIII c. 1 +
  Septuag. *ad orientem* + Bede + Erf. Strabus + Damascene); p.409
  R band 2 footers 6–9 = [^12]–[^15] (Bede + Strabus on Gen. 2, 9
  + Glossa ord. + Aug. XIV cc. 13–15 + Prov. 21, 28 + Vat. *haec*
  + edd. 1–9 *prohibuisset* variant). p.408 L band 2 footers 1–2
  belong to d16-dubia DUB IV ([^13]–[^14] there); no migration.
- Marginal labels preserved inline per locked Vol II convention:
  *Quaestio 1.*, *Opinio haeretica.*, *Impugnatur.*, *Quaestio 2.*,
  *Opinio 1.*, *Opinio 2.*, *Augustinus.*, *Causae superiores.*,
  *Dubium 1./2./3./4./5.*, *Glossa.*, *Notandum.*
- `has_scholion: false` — littera chunks carry no SCHOLION by design.
- No `[?]` flags — all 15 anchors + 14 marginal labels crisp at
  450 dpi across pp.408–409. OCR is two-column cascade-fragmented
  here (`DISTINCTIOterumXVII.` at raw 28750 = R-column *alterum²*
  splice with L-column running head); column-band PDF read
  authoritative per Vol II Override.
- Forward hand-off to d17-divisio: none — d17-divisio opens p.410 L
  with its own block.
- Audits: paraphrase HIGH (1 chunk, expected first-pass over
  OCR-cascade base); apparatus-count NO FLAG for d17-littera; header
  audit Q-LOSS / A-LOSS / DUB-LOSS fires because d.17 divisio +
  a*/dubia siblings are skeleton — clears as those promote.
- Build: 603 → 604 translated, 879 quaestio routes.

## What to do this session

**Promote `d17-divisio`** — second d.17 chunk. COMMENTARIUS IN
DISTINCTIONEM XVII opens at raw 28895 on p.410 L band 0 with
`De productione Adae quoad principia constituentia.` subtitle +
epigraph *Hic de origine animae plura quaeri solent etc.* + DIVISIO
TEXTUS + TRACTATIO QUAESTIONUM. Per locked Vol II convention the
divisio holds DIVISIO TEXTUS + TRACTATIO QUAESTIONUM + the first-
article sub-divisio fold-in (no standalone d17-a1-divisio).
Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read.

## d.17 chunk inventory (in semantic order)

- ~~`d17-littera`~~ **DONE 2026-05-25.**
- **`d17-divisio`** — COMMENTARIUS + DIVISIO TEXTUS + TRACTATIO
  QUAESTIONUM (no pars split). — NEXT. (skeleton)
- `d17-a1-q1` (skeleton)
- `d17-a1-q2` (skeleton)
- `d17-a1-q3` (skeleton)
- `d17-a2-q1` (skeleton)
- `d17-a2-q2` (skeleton)
- `d17-a2-q3` (skeleton)
- `d17-dubia` (skeleton)

## Last session (2026-05-25, d.16 ninth chunk — d16-dubia promotion; d.16 CLOSED)

Promoted `d16-dubia` Tier-2:
- *Dubia circa litteram Magistri (Dist. XVI).* Spans p.406 L band 1
  (DUBIA CIRCA LITTERAM MAGISTRI opener + DUB I body immediately after
  d16-a2-q3 SCHOLION II close at raw 28638) → p.406 R bands 1–2 (DUB I
  Respondeo with persona-etymology footer 5 + DUB II opener) → p.407 L+R
  (DUB II Respondeo + DUB III with *Quaestio incidens.* + *Duplex
  expositio.* + *Primus modus iter triplex.* + *Secunda item triplex.* +
  *Ad quaest. incidentem.* + *Notandum.* + DUB IV opener with
  Boethius-aequivoca cit.) → p.408 L band 0 (DUB IV Respondeo close
  with *Notandum.* + *Alia solutio.* + closing at *...repraesentat
  alterum.* immediately before `DISTINCTIO XVII. — Cap. I.`).
- **4 dubia** (DUB I–IV).
- **14 apparatus entries [^1]–[^14].** Page-split map: p.406 L band 2
  footers 3–4 = [^1]–[^2] (August. II de Trin. c.10 n.18 + Scilicet
  sexto / Gen. 1,24 — inherited per d16-a2-q3 forward hand-off);
  p.406 R band 2 footers 5–6 = [^3]–[^4] (Boethius persona etymology +
  Cfr. d.15 a.2 q.2 / Alex.Hal/Albert/Petr/Richard); p.407 L band 2
  footers 1–6 = [^5]–[^10] (Vide supra d.10 a.3 q.2 + Petr. a Tar. +
  Rom 8,29 + Gen 1,26 + Hic c.3 + Cfr. supra a.2 q.3 with Vat.
  *secundum esse* variant); p.407 R band 2 footers 7–8 = [^11]–[^12]
  (In pluribus codd. desideratur *est* + Alex.Hal/Albert/Thom/Aegid
  cross-refs; Boeth. de Praedicam. *de Aequivocis* with homo
  vivens/pictus quote); p.408 L band 2 footers 1–2 = [^13]–[^14]
  (August. VI de Trin. c.10 n.11 *ars quaedam omnipotentis* with Vat.
  *fabricat ipsum natura* variant + Alex.Hal/Petr. a Tar.).
- Marginal labels preserved inline per locked Vol II convention:
  *Quaestio incidens.*, *Duplex expositio.*, *Primus modus iter
  triplex.*, *Secunda item triplex.*, *Ad quaest. incidentem.*,
  *Notandum.* (×2), *Alia solutio.*
- `has_scholion: false` — DUBIA chunks in d.16 carry no SCHOLION
  (d.16 doctrinal scholia live in d16-a1-q1, d16-a2-q1, d16-a2-q3).
- No `[?]` flags — all 14 anchors + 8 marginal labels crisp at 450 dpi
  across pp.406–408.
- Cross-chunk hand-off received from d16-a2-q3: p.406 L footer 3 +
  p.406 R footers 5+ migrate here. No forward hand-off to d17-littera
  (d.17 opens p.408 L with its own NOTAE footer block).
- Audits: paraphrase HIGH (1 chunk, expected first-pass over
  OCR-cascade base); apparatus-count NO FLAGS for d.16 (only
  d16-littera +3 benign remainder, already accepted noise);
  header audit NO LOSS flags — **d.16 final clean state achieved**
  (ART +2 / QUAEST +5 / DUB +4 all positive diffs from per-pars
  repeats, expected).
- Build: 602 → 603 translated, 879 quaestio routes.

## d.16 inventory — ALL DONE 2026-05-25

All nine d.16 chunks promoted Tier-2 in a single day:
`d16-littera`, `d16-divisio`, `d16-a1-q1`, `d16-a1-q2`, `d16-a1-q3`,
`d16-a2-q1`, `d16-a2-q2`, `d16-a2-q3`, `d16-dubia`.

## What to do this session

**Promote `d17-littera`** — first d.17 chunk. d.17 opens at raw 28812
with `DISTINCTIO XVII.` + `Cap. I. De creatione animae, an de aliquo
facta sit.` on p.408 L band 0 (immediately after d16-dubia DUB IV
close). **d.17 pars-split determination: d.17 has NO pars split.**
Running heads read `DIST. XVII. ART. I/II.` only — `P. I.` / `P. II.`
never appears (verified by grep `DIST\. XVII` against raw OCR running
heads at raw 28950/29085/29489/29912). Chunk inventory proceeds with
`d17-divisio` (not `d17-p1-divisio`). Standard Vol II Tier-2
procedure: 450 dpi column-band PDF read for every Cap. opener + footer.

Remaining d.17 chunk inventory after d17-littera: `d17-divisio`,
`d17-a1-q1`, `d17-a1-q2`, `d17-a1-q3`, `d17-a2-q1`, `d17-a2-q2`,
`d17-a2-q3`, `d17-dubia`.

## Last session (2026-05-25, d.16 eighth chunk — d16-a2-q3 promotion)

Promoted `d16-a2-q3` Tier-2:
- *Utrum imago principalius sit in cognitiva quam in affectiva.* Spans
  p.404 L band 0 bottom (QUAESTIO III header + italic title + opener
  *Tertio quaeritur, utrum imago principalius sit in cognitiva quam in
  motiva sive affectiva.*, immediately after q2 *Ad arg. 1, 2 ad
  oppositum* close at *accidentaliter.*; raw 28474) → p.404 L bands 1–2
  (*Fundamenta* args 1–4 + *Ad opposit.* args 1–3 begin) → p.404 R
  bands 0–2 (q2 ad-arg close on R-0 top; *Ad opposit.* arg 4 + *Quaestio
  incidens 1* (Iuxta hoc quaeritur quae sit differentia inter imaginem
  et similitudinem) + *Quaestio incidens 2* (Item cum duae sint potentiae
  ex parte affectionis) closing at *in rationali.*) → p.405 L (CONCLUSIO
  + Respondeo *de prima nominis impositione differt* + *Triplex modus
  distinguendi.* with *Primus/Secundus/Tertius* and embedded *Conclusio
  1./2.*) → p.405 R (*Ad 2. quaestionem incidentem.* + Solutio opposit.
  ad 1, ad 2 begin) → p.406 L (ad 2 close + ad 3 + ad 4 with *Notandum.*
  + SCHOLION I open) → p.406 R bands 0–1 (SCHOLION I close + SCHOLION II
  commentator list, closing immediately before `DUBIA CIRCA LITTERAM
  MAGISTRI` opener at raw 28638).
- **16 apparatus entries [^1]–[^16].** Page-split map: p.404 L
  footers 4–7 = [^1]–[^4] (inherited per q2 forward hand-off: Libr.
  de Spiritu et anima c. 10 + Cfr. I Sent. d. 31. p. II. q. 2 + Vide
  infra pag. 405 nota 2 + Cfr. infra d. 26 q. 5); p.404 R footers
  8–11 = [^5]–[^8] (Vide supra pag. 115 nota 6 + Quaest. 74 + Vide
  tom. I pag. 197 nota 6 + Cfr. III. Sent. d. 23 a. 1 q. 2); p.405 L
  footers 1–3 = [^9]–[^11] (Aristot. de Praedicam. de Qualitate +
  Gen. 1, 26 / Hugo I de Sacram. p. VI c. 2 + Cfr. August. IX de Trin.
  c. 12 n. 17 with Vat. *donationis* pro *derivationis*); p.405 R
  footers 4–6 = [^12]–[^14] (I Sent. d. 3 p. II a. 1 q. 1 ad 4 +
  Duplex proprietas August. XIV de Trin. c. 3 n. 6 + cod. cc *informet*
  pro *reformet* + Vat. *magis*); p.406 L footers 1–2 = [^15]–[^16]
  (Vat. *nobilissimum* + cod. W *considerationem* pro *conditionem*
  + Plures codd. cum edd. 1–4 *utramque* non recte). p.406 L footer 3
  (August. II de Trin. c. 10 n. 18) anchors in d16-dubia DUB I body,
  does NOT migrate.
- Marginal labels preserved inline per locked Vol II convention:
  *Fundamenta.*, *Ad oppositum.*, *Quaestio incidens 1./2.*,
  *Conclusio.*, *Triplex modus distinguendi.*, *Primus./Secundus./
  Tertius.*, *Conclusio 1./2.*, *Ad 2. quaestionem incidentem.*,
  *Solutio oppositorum.*, *Notandum.*
- `has_scholion: true` — SCHOLION I substantial doctrinal scholion on
  imago creationis / recreationis (reformationis) distinction with
  vestigium/imago/similitudo grades; SCHOLION II = q3-specific
  commentator list.
- Forward hand-off to d16-dubia: p.406 L footer 3 + p.406 R footers
  4+ migrate to DUB I body. p.404 q3-side footers do NOT migrate.
- No `[?]` flags — all 16 anchors + 11 marginal labels crisp at
  450 dpi across pp.404–406.
- Audits: paraphrase HIGH (expected first-pass); apparatus-count
  flag CLEARED for q3 (only d16-dubia +23 skeleton flag persists);
  header audit DUB-LOSS still fires because d16-dubia is skeleton —
  clears as it promotes.
- Build: 601 → 602 translated, 879 quaestio routes.

## What to do this session

**Promote `d16-dubia`** — final d.16 chunk. DUBIA CIRCA LITTERAM
MAGISTRI opens at raw 28638 on p.406 R band 1 with `Dub. I.` immediately
after d16-a2-q3 SCHOLION II close. Standard Vol II Tier-2 procedure.
Cross-chunk hand-off received from q3: p.406 L footer 3 + p.406 R
footers 4+ migrate here. d.16 closes with this chunk.

## Last session (2026-05-25, d.16 seventh chunk — d16-a2-q2 promotion)

Promoted `d16-a2-q2` Tier-2:
- *Utrum imago principalius sit in masculo quam in femina.* Spans
  p.403 L band 0 (QUAESTIO II header + italic title + opener *Secundo
  quaeritur, utrum principalius sit imago in masculo quam in femina.
  Et quod sic, videtur.* immediately after p.402 R SCHOLION III close;
  raw 28398) → p.403 L bands 1–2 (*Ad opposit.* args 1–4) → p.403 R
  band 0 (*Contra / Fundamenta* args 1–4 + CONCLUSIO) → p.403 R
  bands 1–2 (Respondeo with *Conclusio 1.* + *Conclusio 2.* +
  *Ad argg.*) → p.404 L band 0 (Ad argg. 1, 2 ad oppositum solutio
  with Augustine *XII de Trin.* exposition closing at *accidentaliter.*
  immediately before QUAESTIO III opener at raw 28474). q3 opens
  on p.404 R band 0.
- **13 apparatus entries [^1]–[^13].** Page-split map: p.403 L
  footers 1–6 = [^1]–[^6] (1 Cor 11,7 + Glossa/Augustine cross-ref +
  Gen 1,26 + Gen 1,27 / Gen 2,18 / 2,21 + Aristot. X Metaph. text 25
  + Cfr. Aug. XIV de Trin. c.16 n.22 with Col 3,9 plus *non ordinatur*
  variant); p.403 R footers 7–10 = [^7]–[^10] (Quaest. praeced. + I
  Sent. d.3 p.II a.1 q.1 cross-ref + Gal 3,28 + Vat. *imago* pro
  *magis* + 1 Cor 11,3 + 11,8); p.404 L footers 1–3 = [^11]–[^13]
  (Aug. XII de Trin. c.7 nn.10+12 with cross-refs + *ibi* codex
  variant + Eph 5,22 + *Vide scholion ad praecedentem quaest.*).
  p.404 L footers 4+ belong to d16-a2-q3.
- Marginal labels preserved inline per locked Vol II convention:
  *Ad opposit.*, *Fundamenta.*, *Conclusio 1.*, *Conclusio 2.*,
  *Ad argg.*, *Ad argg. 1, 2 ad oppositum*.
- `has_scholion: false` — d.16-a2 doctrinal scholion (SCHOLION I on
  *simpliciter* / *secundum quid* distinction) lives in d16-a2-q1 per
  the printed layout; SCHOLION III on p.402 R = forward-pointer
  commentator list for q2 anchored in q1, does NOT migrate. Confirmed
  by p.404 [^13] = *Vide scholion ad praecedentem quaest.* explicit
  pointer back to q1.
- No `[?]` flags — all 13 anchors + 6 marginal labels crisp at 450
  dpi across pp.403–404.
- Forward hand-off to d16-a2-q3: none — q3 opens p.404 R band 0
  with its own Fundamenta args 1–4 + footers 4+.
- Audits: paraphrase HIGH (expected first-pass); apparatus-count
  flag CLEARED for q2 (skeleton flags persist on d16-a2-q3 +24 and
  d16-dubia +23 — clears as they promote); header audit DUB-LOSS
  still fires because d16-dubia is skeleton.
- Build: 600 → 601 translated, 879 quaestio routes.

## Last session (2026-05-25, d.16 sixth chunk — d16-a2-q1 promotion)

Promoted `d16-a2-q1` Tier-2:
- *Utrum imaginis ratio principalius reperiatur in Angelo quam in
  anima.* Spans p.399 R band 1 bottom (ARTICULUS II header + sub-title
  *De imagine secundum considerationem relatam* + opener *Consequenter
  quaeritur de imagine secundum considerationem relatam. Et circa hoc
  quaeruntur tria.* with 3-question sub-divisio folded in per locked
  Vol II Override step 5; raw 28166) → p.399 R band 2 (sub-divisio
  close at *affectiva*) → p.400 L (QUAESTIO I header + Argg. pro
  parte affirmativa 1–4) → p.400 R (Contra/Pro parte negativa 1–6 +
  CONCLUSIO + Respondeo opener with *Opinio 1.*) → p.401 L+R (Opinio 1
  cont., *Non omnino probatur,* *Opinio 2* with *Principium generale,*
  *Triplex convenientia ordinis,* *Triplex ordo,* *Conclusio 1./2.,*
  *Duplex convenientia proportionis,* *Conclusio 3.,* *Subdistinctio,*
  *Conclusio 4.* opener) → p.402 L+R (Conclusio 4 close + *Conclusio
  5* + *Conclusio generalis* + *Ad 3, 4* with *Notandum* + *Ad arg.
  pro parte negativa, Ad 5* with *Notandum* + SCHOLION I + II + III).
  Closes immediately before p.403 QUAESTIO II opener.
- **20 apparatus entries [^1]–[^20].** Page-split map: p.399 R
  footer 8 (anchored on `affectiva` in sub-divisio) = [^1]; p.400 L
  footers 1–6 = [^2]–[^7]; p.400 R footers 7–10 = [^8]–[^11]; p.401 L
  footers 1–3 = [^12]–[^14]; p.401 R footers 4–7 = [^15]–[^18]; p.402
  L footer 1 = [^19]; p.402 R footer 2 = [^20]. p.399 R footers 5–7
  belong to d16-a1-q3 (already consumed); p.402 SCHOLION block has
  no body footnote.
- Marginal labels preserved inline per locked Vol II convention:
  *Argg. pro parte affirmativa,* *Pro parte negativa,* *Opinio 1.,*
  *Non omnino probatur,* *Opinio 2.,* *Principium generale,* *Triplex
  convenientia ordinis,* *Triplex ordo,* *Conclusio 1./2./3./4./5.,*
  *Duplex convenientia proportionis,* *Subdistinctio,* *Conclusio
  generalis,* *Ad argg. pro parte affirm.,* *Ad arg. pro parte negat.,*
  *Ad 5,* *Notandum* (×2).
- `has_scholion: true` — SCHOLION I substantial doctrinal scholion on
  *simpliciter*/*secundum quid* distinction with the Aquinas/Richard/
  Scotus consensus; II = commentator list for q1; III = forward-
  pointing commentator list for d16-a2-q2 (parallel to d15-a2-q1's
  SCHOLION III forward-pointer).
- No `[?]` flags — all 20 anchors + 17 marginal labels crisp at
  450 dpi across pp.399–402.
- Forward hand-off to d16-a2-q2: SCHOLION III lives here per printed
  layout (does NOT migrate); q2 opens p.403 with its own running head
  + body. No p.402 footer migrates forward.
- Audits: paraphrase HIGH (expected first-pass); apparatus-count flag
  CLEARED for q1 (skeleton flags persist on d16-a2-q2 +9, d16-a2-q3
  +24, d16-dubia +23 — clears as they promote); header audit DUB-LOSS
  still fires because d16-dubia is skeleton.
- Build: 599 → 600 translated, 879 quaestio routes.

## Last session (2026-05-25, d.16 fifth chunk — d16-a1-q3 promotion)

Promoted `d16-a1-q3` Tier-2:
- *Utrum esse imaginem conveniat homini proprie, ita quod nulli alii.*
  Spans p.398 L band 1 bottom (QUAESTIO III header + title +
  *Fundamenta* arg 1 opener immediately after d16-a1-q2 *alio vero
  modo non.* close at raw 28075) → p.398 L band 2 (args 1 close +
  arg 2 Augustine *de imagine*) → p.398 R bands 0–1 (args 3–6 +
  *Contra* / *Ad oppositum* args 1–4) → p.399 L band 0 (arg 4 close
  + CONCLUSIO + Respondeo with *Proprium dupliciter* + bipes
  analogy) → p.399 L band 1 + R band 0 (*Solutio oppositorum* ad 1,
  ad 2, ad 3 with *Duplex sensus superlativi* marginal, ad 4) →
  p.399 R band 1 (ad 5–6 with *Notandum* marginal closing at
  *explanata fuit.* immediately before ARTICULUS II opener at
  raw 28166).
- **15 apparatus entries [^1]–[^15].** Page-split map: p.398 L
  footers 4–5 = [^1]–[^2] (Gen. 1, 26 + Serm. 43 / *de Verbis
  Apostoli* serm. 27 — inherited per d16-a1-q2 forward hand-off);
  p.398 R footers 6–13 = [^3]–[^10] (Aristot. V Topic. + Q I corp.
  + Ambros. Epist. 43 + III Sent. d. 2 + Pseudo-Dion. *de Div.
  Nom.* c. 4 + August. XIV de Trin. + d. 1. p. II. a. 2. q. 2 +
  Dist. 3. p. II.); p.399 L footers 1–4 = [^11]–[^14] (Aristot. V
  Topic. c. 1 + cross-ref + cod. variant + Priscian III Grammat.);
  p.399 R footer 5 = [^15] (Gregor. *omnis creaturae nomine
  signatur homo*). p.399 R footer 8 (*Multi codd. cum ed. 2
  activa/affectiva*) anchors in d16-a2-divisio/q1 TRACTATIO
  sub-divisio listing; does not migrate here.
- Marginal labels preserved inline per locked Vol II convention:
  *Ad oppositum.*, *Fundamenta.* (×2), *Conclusio.*, *Solutio
  oppositorum.*, *Duplex sensus superlativi.*, *Notandum.*
- `has_scholion: false` — q3 has no scholion of its own per the
  locked Vol II sibling-shared-scholion pattern; d16-a1-q1
  SCHOLION I owns the doctrinal note for this article. p.399 has
  no SCHOLION between q3 close and ARTICULUS II opener.
- No `[?]` flags — all 15 anchors + 7 marginal labels crisp at
  450 dpi across pp.398–399.
- Forward hand-off to d16-a2-q1: none — ARTICULUS II opens on
  p.399 R band 1 bottom with its own `Consequenter quaeritur de
  imagine secundum considerationem relatam` opener + 3-question
  sub-divisio (folded into a2-q1 per Vol II Override step 5).
- Audits: paraphrase HIGH (expected first-pass); apparatus-count
  flag CLEARED for q3 (skeleton flags persist on d16-a2-q1/q2/q3
  and d16-dubia — clears as they promote); header audit DUB-LOSS
  still fires because d16-dubia is skeleton.
- Build: 598 → 599 translated, 879 quaestio routes.

## Last session (2026-05-25, d.16 fourth chunk — d16-a1-q2 promotion, manual-rescue) Vol II d.1–d.10 LIVE on
bonaventure.wrootpress.com since 2026-05-23; per "deploy after each
decade ships" rule, the next live ship is at end-of-d.20.

## Last session (2026-05-25, d.16 fourth chunk — d16-a1-q2 promotion, manual-rescue)

Promoted `d16-a1-q2` Tier-2 (manual-rescue chunk per d.11–d.20
boundary sweep — the auto-chunker 2026-05-13 had collapsed q1+q2
because `QU.\ESTIO n.` at raw 27969 was the OCR-garbled QUAESTIO II
header; pre-promote skeleton boundaries verified clean against
450 dpi PDF, no re-split needed):
- *Utrum homo sit imago Dei naturaliter.* Spans p.396 L band 2
  (QUAESTIO II header + title + Fundamenta arg 1 opener immediately
  after d16-a1-q1 SCHOLION III close) → p.396 R band 2 (arg 1 close
  + arg 2 opener) → p.397 L (Fundamenta arg 2–5 + Ad oppositum
  contra arg 1–5) → p.397 R (CONCLUSIO + Respondeo with
  *Duplex imago.* + *Conclusio 1.* + *Tertia species Imaginis.* +
  *Conclusio 2.* + *Solutio oppositorum.* ad 1–3 begin with
  *Notandum.* + *Ratio.*) → p.398 L (ad 3 close + ad 4 with
  *Notandum.*) → p.398 R bottom (ad 5 with *Notandum.* closing at
  `alio vero modo non.` immediately before QUAESTIO III opener at
  raw 28075).
- **14 apparatus entries [^1]–[^14].** Page-split map: p.396 L
  footers 1–2 = [^1]–[^2]; p.396 R footer 3 = [^3]; p.397 L
  footers 1–5 = [^4]–[^8]; p.397 R footers 6–8 = [^9]–[^11];
  p.398 L footers 1–3 = [^12]–[^14]. p.398 L footers 4–5 (Gen. 1,26
  + Serm. 43) anchor in d16-a1-q3.
- Marginal labels preserved inline per locked Vol II convention:
  *Fundamenta.*, *Ad oppositum.*, *Duplex imago.*, *Conclusio 1.*,
  *Tertia species Imaginis.*, *Conclusio 2.*, *Solutio oppositorum.*,
  *Notandum.* (×3), *Ratio.*
- `has_scholion: false` — q2 has no scholion of its own per the
  locked Vol II sibling-shared-scholion pattern; q2's closing
  footer [^14] = *Vide scholion ad praecedentem quaest.* explicitly
  points back to d16-a1-q1 SCHOLION I (the substantial doctrinal
  scholion on the *imago naturalis / connaturalis / artificialis*
  trichotomy).
- No `[?]` flags — all 14 anchors + 9 marginal labels crisp at
  450 dpi.
- Audits: paraphrase HIGH (expected first-pass over OCR-cascade
  base); apparatus-count flag CLEARED for q2 (skeleton flags
  persist on d16-a1-q3, d16-a2-q1/q2/q3, d16-dubia — clears as
  they promote); header audit DUB-LOSS / Q-LOSS still fires
  because d.16 siblings are skeleton.
- Build: 597 → 598 translated, 879 quaestio routes.

## Last session (2026-05-25, d.16 third chunk — d16-a1-q1 promotion)

Promoted `d16-a1-q1` Tier-2:
- *Utrum homo sit vere imago Dei.* Spans p.393 L band 2 (QUAESTIO I
  header + title + *Fundamenta* args 1–3 opener, immediately after
  d16-divisio TRACTATIO close *Tertio, utrum sit imago Dei proprie.*)
  → p.393 R band 2 (arg 3 close) → p.394 L (arg 4 + *Ad oppositum*
  args 1–6) → p.394 R (CONCLUSIO + Respondeo with *Quadruplex
  similitudo* + *Applicatio ad Deum* + *Probatio: Primo de
  convenientia ordinis*) → p.395 L (*Confirmatur* + *Probatio 2* +
  *Distinctio* + *Confirmatur*) → p.395 R (*Solutio oppositorum*
  ad 1–5 begin, with *Notandum* at ad 2) → p.396 L (ad 5 close +
  ad 6 opener with *Notandum*) → p.396 R (ad 6 close + SCHOLION
  I (substantial doctrinal scholion) + II + III commentator lists).
  Closes immediately before `QU.\ESTIO n.` (q2 opener) at raw 27970.
- **24 apparatus entries [^3]–[^26]** continuously renumbered.
  Page-split map: p.393 L footers 3–5 = [^3]–[^5] (inherited per
  d16-divisio hand-off: Vers. 26 / Vers. 1 / Hugo *de Arrha animae*);
  p.394 L footers 1–5 = [^6]–[^10]; p.394 R footers 6–11 = [^11]–
  [^16]; p.395 L footers 1–6 = [^17]–[^22]; p.395 R footers 7–10 =
  [^23]–[^26]. p.396 carries no body footnote (SCHOLION only).
  Numbering does NOT restart at [^1]: [^1] and [^2] are owned by
  d16-divisio per cross-chunk p.393 footer split.
- Marginal labels preserved inline per locked Vol II convention:
  *Fundamenta.*, *Ad oppositum.*, *Quadruplex similitudo.*,
  *Applicatio ad Deum.*, *Conclusio.*, *Probatio.* (×2),
  *Confirmatur.* (×2), *Distinctio.*, *Solutio oppositorum.*,
  *Notandum.* (×3).
- `has_scholion: true` — SCHOLION I is a substantial doctrinal
  scholion on the definition of imago + the connatural / natural /
  artificial trichotomy; II + III are commentator lists.
- No `[?]` flags — all 24 anchors + marginal labels crisp at 450 dpi
  across pp.393–396. Forward hand-off to d16-a1-q2: no p.396 footer
  migrates; q2 opens p.396 R bottom with its own footers ¹–³.
- Audits: paraphrase HIGH (expected first-pass over OCR-cascade
  base); apparatus-count flag cleared for q1 (skeleton flags persist
  on d16-a1-q2/q3, d16-a2-q1/q2/q3, d16-dubia — clears as they
  promote); header audit DUB-LOSS / Q-LOSS still fires because d.16
  siblings are skeleton — clears as those promote.
- Build: 596 → 597 translated, 879 quaestio routes.

## Last session (2026-05-25, d.16 second chunk — d16-divisio promotion)

Promoted `d16-divisio` Tier-2:
- *Commentarius in Distinctionem XVI — Qualiter Deus produxerit
  hominem ad suam imaginem.* Spans p.392 R band 2 bottom
  (COMMENTARIUS opener + epigraph *His excursis...* at raw 27717,
  immediately after d16-littera Cap. IV close) → p.393 L bands 0–1
  + R bands 0–1 (DIVISIO TEXTUS in two-column flow + TRACTATIO
  QUAESTIONUM + Articulus I sub-divisio fold-in). Closes at
  *Tertio, utrum sit imago Dei proprie.* (raw 27734) immediately
  before `ARTICULUS I.` at raw 27736. Per locked Vol II convention
  the divisio holds DIVISIO TEXTUS + TRACTATIO QUAESTIONUM + the
  first-article sub-divisio fold-in (no standalone d16-a1-divisio).
- **2 apparatus entries [^1]–[^2]** from p.393 L band 2 footer:
  [^1] = *Ita codd. et edd.; textus Magistri melius primo.* anchored
  at *statu primi¹ hominis* in DIVISIO para 1; [^2] = *Codd. W an
  relativam.* anchored at *considerationem relatam²* in TRACTATIO.
  Footnotes ³ (Vers. 26), ⁴ (Vers. 1), ⁵ (Hugo *de Arrha animae*)
  on p.393 L band 2 anchor in d16-a1-q1 (Genesis 1, 26 + Ecclus 17, 1
  + Hugo citations in q1's affirmative arguments 1–3). p.392 R band 2
  footer (notes 4–7) belongs entirely to d16-littera as [^8]–[^11]
  (already consumed).
- No `[?]` flags — both anchors crisp at 450 dpi. The OCR around
  raw 27720–27732 is cascade-fragmented (two-column diagonal token
  splice); column-band PDF read authoritative per Vol II Override.
- `has_scholion: false` — divisio chunks carry no SCHOLION by design.
- Audits: paraphrase HIGH (expected first-pass over OCR-cascade
  base); apparatus-count flag cleared for divisio (skeleton flags
  persist on the 6 a*/dubia siblings — clears as they promote);
  header audit Q-LOSS / A-LOSS / DUB-LOSS still fires because
  d.16 a*/dubia siblings are skeleton (a divisio chunk has no
  ART/QUAEST/DUB headers) — clears as those promote.
- Build: 595 → 596 translated, 879 quaestio routes.

## Prior session (2026-05-25, d.16 first chunk — d16-littera promotion)

Promoted `d16-littera` Tier-2:
- *Distinctio XVI — Littera Magistri*, Cap. I–IV (4 capitula),
  spans p.391 L band 2 (Cap. I *De hominis creatione* opener immediately
  after d15-dubia close `Et sic patet responsio ad obiecta.`) → p.391
  R bands 1–2 (Cap. II *Qualis factus sit homo* with *Dubium 1.* +
  *Dubium 2.* marginals; Cap. III *De imagine et similitudine, ad quam
  factus est homo* opens on R band 2) → p.392 L bands 0–2 (Cap. III
  body with *Imago proprie.* + *Improprie.* + *Dubium 3. et opinio 1.*
  + *Opinio 2.* + *Opinio 3.* + *Exemplum.* marginals) → p.392 R bands
  0–1 (Cap. IV *Quare homo dicitur imago et ad imaginem, Filius non
  ad imaginem* with *Augustinus.* + *Dubium 4.* marginals; closes
  immediately before *COMMENTARIUS IN DISTINCTIONEM XVI.* at raw 27717).
- **11 apparatus entries [^1]–[^11]** continuously renumbered across
  pp.391–392. Page-split map: p.391 R band 2 NOTAE 1–4 = [^1]–[^4];
  p.392 L band 2 footers 1–3 = [^5]–[^7]; p.392 R band 2 footers 4–7
  = [^8]–[^11]. p.391 L band 2 footers 1–7 belong to d15-dubia (per
  its Notes block) — none migrate here.
- Cross-chunk hand-off forward: d16-divisio receives the *COMMENTARIUS
  IN DISTINCTIONEM XVI.* opener at raw 27717 + p.393 DIVISIO TEXTUS
  footer share. No littera-side footer migrates forward.
- **d.16 pars-split determination:** d.16 has **NO pars split.**
  Running heads read `DIST. XVI. ART. I/II.` only — `P. I.` / `P. II.`
  never appears. Chunk inventory therefore proceeds with `d16-divisio`
  (not `d16-p1-divisio`).
- `has_scholion: false` — littera chunks carry no SCHOLION by design.
- No `[?]` flags — all 11 anchors + 9 marginal labels crisp at 450 dpi.
- Audits: paraphrase HIGH (expected first-pass over OCR-cascade
  base); apparatus-count audit no longer flags d16-littera (diff +3
  benign — raw heuristic catches 14 vs chunk 11, normal noise);
  header audit Q-LOSS / A-LOSS / DUB-LOSS fires because d.16
  divisio + a*/dubia siblings are still skeletons (a littera chunk
  has no ART/QUAEST/DUB headers) — will clear as those promote.
- Build: 594 → 595 translated, 879 quaestio routes.

## What to do this session

**Promote `d16-a2-q2`** — seventh d.16 chunk. QUAESTIO II opens on
p.403 with `QUAESTIO II.` header + italic title *Utrum imago
principalius sit in masculo quam in femina* + opener `Secundo
quaeritiir, utrum principalius sit imago in masculo quam in feniina.
Et quod sic, videtur.` Per the d16-a2-q1 forward hand-off, SCHOLION
III on p.402 R is a forward-pointer commentator list anchored in q1
(does NOT migrate to q2). Standard Vol II Tier-2 procedure: 450 dpi
column-band PDF read. p.403 crops already cached at
`/tmp/colcrop/vol2-p403-*`; generate p.404+ as needed.

## d.16 chunk inventory (in semantic order)

- ~~`d16-littera`~~ **DONE 2026-05-25.**
- ~~`d16-divisio`~~ **DONE 2026-05-25.**
- ~~`d16-a1-q1`~~ **DONE 2026-05-25.**
- ~~`d16-a1-q2`~~ **DONE 2026-05-25.**
- ~~`d16-a1-q3`~~ **DONE 2026-05-25.**
- ~~`d16-a2-q1`~~ **DONE 2026-05-25.**
- ~~`d16-a2-q2`~~ **DONE 2026-05-25.**
- ~~`d16-a2-q3`~~ **DONE 2026-05-25.**
- **`d16-dubia`** — DUBIA CIRCA LITTERAM MAGISTRI (DUB I–?). — NEXT. (skeleton)

## Last session (2026-05-25, ninth chunk — d15-dubia promotion; d.15 CLOSED)

Promoted `d15-dubia` Tier-2:
- *Dubia circa litteram Magistri (Dist. XV).* Spans printed
  **pp. 388–391** (4 pages, raw 27417–27615). **6 dubia**
  (DUB I–VI): DUB I on reptiles vs natatilia + adornment of
  waters vs earth + *anima vivens* triple objection (p.388
  L–R + p.389 L head); DUB II on the *iumenta / bestiae /
  reptilia / pecora* threefold and the sea/air/earth-symmetry
  question (p.389 L–R); DUB III on the catholic doctors'
  apparent dissension with the *assertive / opinando*
  distinction and the *Alia solutio* (p.389 R + p.390 L head);
  DUB IV on *Novam creaturam facere cessavit* with the twofold
  *novum* distinction + Christ-as-pure-grace alternative
  (p.390 L); DUB V on the seventh-day blessing + sanctification
  with the *dies = mensura actionis* solution and the sabbath
  Mosaic-law trace (p.390 R); DUB VI on the septenary computation
  + the Ptolemaic planet-naming sequence + the *secunda/tertia
  feria* ecclesiastical override (p.391 L–R).
- **27 apparatus entries [^2]–[^27]** continuously renumbered
  across pp.388–391. Page-split map: p.388 L footer 1
  (Val. *rerum.*) sits as parked prelude inside DUB I body;
  L footers 2–3 + R footer 4 = [^2]–[^4]; p.389 L footers 1–5
  = [^5]–[^8] + [^10], R footers 6–7 = [^11]–[^12] (one
  Vat.*sub una* gloss collapsed into [^8], leaving an internal
  gap at [^9] — known and accepted); p.390 L footers 1–5 =
  [^13]–[^17], R footers 6–8 = [^18]–[^20]; p.391 L footers 1–7
  = [^21]–[^27], R footers: none.
- Marginal labels preserved inline per locked Vol II convention:
  *Quaest. incid.*, *Tres species motus in animalibus.*,
  *Notandum.* (×3 across DUB I, III, V), *Quadruplices modi
  quibus reptilia.*, *Ad quaest. incidentem.*, *Quaestio 1.*
  + *Quaestio 2.*, *Differentia 1.* + *Differentia 2.*,
  *Alia solutio.*, *Distinctio.*, *Aliter.*, *Quaestio.*
  (DUB VI), *Ad quaestionem.* (DUB VI).
- Cross-chunk footer-split check: clean. p.388 commentator-list
  block (`Vide scholion ad praecedentem quaest.`) already
  consumed by d15-a2-q3 per that chunk's Notes; no d15-a2-q3
  footer migrates here. d16-littera opens on p.392 with its
  own NOTAE block — no footer migrates from d15-dubia.
- `has_scholion: false` — DUBIA in Vol II d.15 carry no SCHOLION
  (d.15-a2 scholion lives in d15-a2-q1; d.15-a1 in d15-a1-q1).
- No `[?]` flags — all 27 anchors + 14 marginal labels crisp
  at 450 dpi.
- Audits: paraphrase HIGH (1 chunk in HIGH bucket, expected
  first-pass over OCR-cascade-shattered base); apparatus-count
  audit no longer reports d15-dubia (only d15-littera +1
  benign remainder); header audit no LOSS flags — d.15 final
  clean state achieved (ART +2 / QUAEST +6 / DUB +5 all
  positive diffs from per-pars repeats, expected).
- Build: 593 → 594 translated, 879 quaestio routes.

## d.15 inventory — ALL DONE 2026-05-25

All nine d.15 chunks promoted Tier-2 in a single day:
`d15-littera`, `d15-divisio`, `d15-a1-q1`, `d15-a1-q2`,
`d15-a1-q3`, `d15-a2-q1`, `d15-a2-q2`, `d15-a2-q3`, `d15-dubia`.

## What to do this session

**Promote `d16-littera`** — first d.16 chunk. Opens at raw
27616 with `DISTINCTIO XVI.` running head + `Cap. I. De hominis
creatione.` on p.391 R band 2 (bottom of p.391, immediately
after d15-dubia DUB VI close) and continues onto p.392.
Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read
for every Cap. opener + footer.

Remaining d.16 chunk inventory after d16-littera: `d16-divisio`,
`d16-a1-q1`, `d16-a1-q2`, `d16-a1-q3`, `d16-a2-q1`, `d16-a2-q2`,
`d16-a2-q3`, `d16-dubia`.

**d.15 inventory correction (2026-05-25):** d.15 has **THREE a2
sub-quaestiones** (q1 *Utrum omnia sensibilia facta sint propter
hominem*; q2 *Quo ordine ex parte temporis Deus produxerit res
sensibiles*; q3 *Qui sit ordo productionis animalium respectu
quietis*), **NOT** two as the prior auto-chunked inventory implied.
The auto-chunker had assigned the q3 body (raw 27258–27416,
"Tertio quaeritur…") to the q2 skeleton, with the true q2 body
(raw 27119–27257, "Secundo quaeritur…") falling in an unassigned
gap. Rechunk commit: misaligned skeleton renamed q2→q3 with
frontmatter id+quaestio updated; fresh q2 scaffold built from
raw 27119–27257; smoke build green. q2 was then promoted Tier 2
in the same session (this entry). d.15-a2-q3 remains skeleton,
to be promoted next.

## Last session (2026-05-25, eighth chunk — q3 promotion)

Promoted `d15-a2-q3` Tier-2:
- *Qui sit ordo productionis animalium respectu quietis.* Spans
  p.386 L band 0 (QUAESTIO III header + italic title, immediately
  after q2 ad 8 close `quod habeat veritatem.`) → p.386 L bands 1–2
  (*Fundamenta* arg. 1–4 + *Ad oppositum* arg. 1–3 begin) → p.386 R
  bands 0–2 (Contra arg. 1–6 close + CONCLUSIO + Respondeo opener
  with *Praenotandum.* marginal) → p.387 L bands 0–2 (Respondeo cont.
  with *Duplex genus.* + *Duplex perfectio universi.* + *Corollarium.*
  + *Conclusio.* + *Solutio oppositorum.* ad 1, ad 2 begin) → p.387 R
  bands 0–2 (ad 2 close + *Quiescere secundum August.* + *Sec. alios
  Sanctos.* on ad 3; ad 4; ad 5–6 with *Notandum.* marginal) → p.388
  L band 0 (Three-kinds appendix with *Tria rerum genera producta.*
  + *Genus 1./2./3.*) → p.388 L band 1 + R band 0 (SCHOLION I + II).
  Closes immediately before `DUBIA CIRCA LITTERAM MAGISTRI` opener
  at raw 27638.
- 13 apparatus entries [^2]–[^15] (numbering preserves the per-page
  Quaracchi footer continuity established in q2's hand-off): p.386 L
  footers 2–5 = [^2]–[^5]; p.386 R footers 6–8 = [^6]–[^8]; p.387 L
  footers 1–4 = [^9]–[^12]; p.387 R footers 5–6 = [^13]–[^14]; p.388
  L footer = [^15]. p.386 L footer ¹ `Vide scholion ad praecedentem
  quaest.` is a redirect-pointer to the q1 sibling scholion AND to
  this chunk's own SCHOLION I+II at p.388; not rendered as a numbered
  apparatus entry.
- **has_scholion divergence from session brief:** brief specified
  `has_scholion: false`. PDF 450 dpi shows a clear q3-specific
  SCHOLION I+II on p.388 L+R between the q3 body close and the
  DUBIA opener; SCHOLION II commentator list is tagged `hic q. 3.
  a. 1. 2`. Frontmatter set to `has_scholion: true` per Vol II
  Override "PDF authoritative in damaged regions"; transcribed +
  translated. Owner: confirm whether to keep here as printed or
  collapse into a2-q1 in a polish pass.
- Marginal labels preserved inline: *Fundamenta.*, *Ad oppositum.*,
  *Praenotandum.*, *Duplex genus.*, *Duplex perfectio universi.*,
  *Corollarium.*, *Conclusio.*, *Solutio oppositorum.*, *Quiescere
  secundum August.*, *Sec. alios Sanctos.*, *Notandum.*, *Tria rerum
  genera producta.*, *Genus 1./2./3.*
- No `[?]` flags — all anchors + marginal labels crisp at 450 dpi.
- Audits: paraphrase q3 not in content scope (no line_start/line_end
  on Tier-2 chunks per Vol II convention); apparatus-count clean for
  q3 (only d15-dubia +28 skeleton flag persists); header audit no
  LOSS flags (QUAEST diff +3 from per-pars repeats, expected).
- Build: 592 → 593 translated.

## Prior session (2026-05-25, seventh chunk — q2 promotion after rechunk)

Promoted `d15-a2-q2` Tier-2:
- *Quo ordine ex parte temporis Deus produxerit res sensibiles.*
  Spans p.384 L band 0 bottom (QUAESTIO II header + italic title)
  → p.384 L bands 1–2 (Secundo quaeritur + Contra series 1
  arg. 1–4 + series 2 transition `Item, obiicitur contra ordinem
  productionis animalium in comparatione ad hominem`) → p.384 R
  bands 1–2 (arg. 5–8 + CONCLUSIO + Respondeo *duplex ordo* +
  *Primus ordo* per *exigentiam finis et materiae*) → p.385 L
  bands 0–2 (Primus ordo completion + *Secundus ordo* per
  *praecellentiam perfectionis naturae* + *Rationes 3 quare
  homo post omnia producitur* — multitudo / distantia / perfectio)
  → p.385 R bands 0–2 (*Conclusio generalis* + *Solutio
  oppositorum* ad 1, 2, 3, 4, 5–6, 7 begin) → p.386 L band 0
  (ad 7 finish + ad 8 final, closes at `quod habeat veritatem`).
- 13 apparatus entries continuously renumbered across pp.384–385:
  p.384 L footers 1–4 = [^1]–[^4] (Gen. 1, 20 seqq.; *Scilicet
  die tertio* d. 14. p. II. dub. 1.; Vat. *operationum*; Gen.
  1, 20 + cross-ref a. 1. q. 2. seq.); p.384 R footers 5–8 =
  [^5]–[^8] (Gen. 1, 24; supra d. 1. p. II. a. 2. q. 2.;
  Aristot. II Metaph. text. 10 + V text. 16; supra a. 1. q. 3
  in fine corp.); p.385 L footers 1–3 = [^9]–[^11] (supra pag.
  330 nota 5; cod. cc *quanto aliquid completius* variant +
  Alex. Hal. Avicebron / Isaac de Elementis cit.; Aristot. II
  de Anima text. 21 + Greg. Naz. Or. 37/42/43); p.385 R footers
  carry [^12]–[^13] (Vide supra d. 14. p. II. dub. 1.; Hic in
  corp. quaest. et supra a. 1. q. 2. seq.). The remaining p.385 R
  footer slots cross-reference ad-arg dispositions and were
  absorbed into the relevant body footnotes per the locked
  Vol II cross-chunk footer-split convention.
- Marginal labels preserved inline per locked Vol II convention:
  *Ad oppositum series 1. argumentor.*, *Series 2.*,
  *Duplex ordo.*, *Primus ordo.*, *Secundus ordo.*, *Conclusio
  1./2.*, *Rationes 3, quare homo post omnia producitur.*,
  *Conclusio generalis.*, *Solutio oppositorum.*
- Cross-chunk footer-split: p.384 L footers 1–4 and R footers
  5–8 entirely anchor q2 body (q1's p.384 share was its tail
  Aug. quote + SCHOLION I+II+III footer-less block, already
  documented in d15-a2-q1 Notes). p.386 L footers 1–5 DO NOT
  belong to q2 — they anchor q3's `Tertio quaeritur…` body on
  p.386 L bands 1–2.  q2 has **no scholion** — the d.15-a2
  scholion sits in d15-a2-q1 per the printed layout (q1's
  SCHOLION III `De seq. quaestione` is the forward-pointing
  commentator list covering both q2 and q3). `has_scholion:
  false` is correct here per Vol II Override step 5
  (sibling-shared-scholion pattern).
- No `[?]` flags — all anchors + marginal labels crisp at 450 dpi.
- Audits: paraphrase q2 unflagged (no line_start/line_end field
  on Tier-2 chunks per Vol II convention — audit reports
  "content audit skipped"); apparatus-count flag cleared for q2
  (skeleton flags persist on d15-a2-q3 +24 and d15-dubia +28 —
  clears as those promote); header audit no LOSS flags.
- Build: 591 → 592 translated, 878 → 879 quaestio routes.

## Prior session (2026-05-25, sixth chunk)

Promoted `d15-a2-q1` Tier-2:
- *Utrum omnia sensibilia facta sint propter hominem.* Spans
  p. 382 L (ARTICULUS II opener *Consequenter quaeritur, quo
  ordine animalia sint producta. Et circa hoc quaeruntur tria.*
  + 3-question sub-divisio *ex parte finis / ex parte temporis /
  de ordine productionis et quietis* folded in per locked Vol II
  Override step 5; QUAESTIO I opener + *Fundamenta* arg. 1–4 +
  *Ad oppositum* arg. 1–5) → p. 382 R (CONCLUSIO + Respondeo
  opening *Duplex finis* + *Conclusio 1*) → p. 383 L
  (*Conclusio 2* + *Rationes* + *Conclusio 3* + *In statu
  innocentiae quadrupliciter* with 4 sub-reasons +
  *Corollarium*) → p. 383 R (*Item in statu naturae lapsae cum
  distinctione* + *De bestiis* + *Epilogus* + *Solutio
  oppositorum* ad 1, 2, 3 with *Notandum*, ad 4–5 with
  *iuvantia*/*offendentia* analogy + Augustine *Nimirum aliae
  bestiae* citation opener) → p. 384 L band 0 (Augustine
  citation tail closing at `...patet responsio ad obiecta.`)
  + SCHOLION I + II + III. q2 opens p. 384 L below SCHOLION.
- 18 apparatus entries continuously renumbered across pp.382–383:
  p.382 R footers 1–6 = [^1]–[^6]; p.382 R footers 7–8 =
  [^7]–[^8]; p.382 R band 2 footer ⁹ = [^9]; p.383 L footers
  1–5 = [^10]–[^14]; p.383 R footers 6–9 = [^15]–[^18]. p.384
  carries SCHOLION only (no body footnotes). No `[?]` flags —
  all anchors crisp at 450 dpi.
- Marginal labels preserved inline per locked Vol II convention:
  *Fundamenta.*, *Ad oppositum.*, *Duplex finis.*,
  *Conclusio 1./2./3.*, *Rationes.*, *In statu innocentiae
  quadrupliciter.*, *Corollarium.*, *Item in statu naturae
  lapsae cum distinctione.*, *De bestiis.*, *Epilogus.*,
  *Solutio oppositorum.*, *Notandum.*
- Cross-chunk footer-split check: p.382 carries no a1-q3-side
  footer (p.382 opens with the ARTICULUS II header at top of L
  column; q3 tail closed on p.381 R). All p.382 footers anchor
  in this q1 body. SCHOLION III `De seq. quaestione` is a
  forward-pointing commentator list for q2 but lives in q1's
  scholion block per the printed layout — kept here, d15-a2-q2
  will not duplicate.
- Audits: paraphrase HIGH (expected first-pass); apparatus-count
  flag cleared for q1 (only d15-a2-q2 +24 and d15-dubia +28
  skeleton flags persist); header audit DUB -1 fires because
  d15-dubia is still skeleton — clears as it promotes.
- Build: 590 → 591 translated.

## Prior session (2026-05-25, fifth chunk)

Promoted `d15-a1-q3` Tier-2:
- *Utrum corpora animalium magis constent ex elementis passivis
  quam activis.* Spans p. 379 L bands 1–2 + R bands 1–2 (q3 opener
  immediately below q2 SCHOLION II close on p. 379 R band 0;
  *Pro 1. opinione* arg. 1–4 on L + *Ad oppositum* / *Pro 2. opinione*
  arg. 1–3 on R) → p. 380 L+R (arg. 3 wraparound + arg. 4 with
  *Replicatur.* clause + arg. 5; CONCLUSIO + Respondeo opening
  *Duplex quantitas et praedominantia.* + *Conclusio 1./2.* +
  *Ratio ex fine, tripliciter.* + *Idoneitas ad vitam.* +
  *Item ad sensum.* + *Item ad motum.*) → p. 381 L (Augustine *Ignis
  omnia penetrat* citation tail + *Aqua igitur et terra…* artisan
  analogy + *Duplex commixtio.* + *Duplex modus producendi.* +
  *Corollarium.* on natatilia/volatilia + Augustine *Iste inferior
  aër*) → p. 381 R bands 0–2 (close of Augustine citation + general
  resolution *Ex praedictis igitur patet…* + *Ad replic. in 5.
  pro 2. opinione.* solutio ad 4 + ad 5, closing at `…potissimum
  enim actum suum ibi exercent.`). p. 382 opens ARTICULUS II.
  (next chunk). q3 has **no scholion of its own** — the printed
  footer note 7 at the chunk close = *Vide scholion ad praecedentem
  quaest.* redirects to the q2 SCHOLION I+II (consistent with q1
  SCHOLION I's `pro quaest. seq.` pointer; locked Vol II Override
  step 5 sibling-shared-scholion pattern).
- 23 apparatus entries renumbered sequentially across three pages:
  p. 379 L footer 1–4 = [^1]–[^4] (Elementa passiva/activa
  editorial gloss + Gen 1,20+24 + Aristot. II. de Gener. et corrupt.
  text. 50 + Aristot. de Respirat. + cod. A *animalium*); p. 379 R
  footer 5–8 = [^5]–[^8] (Aristot. II. de Partib. anim. + de Spir.
  et anima; Aristot. de Longit. et brevit. vitae; Cap. 5 n. 7 +
  cross-ref p. 319; Aristot. III. de Anima text. 40); p. 380 L
  footer 1–3 = [^9]–[^11] (Aristot. II. de Gener. anim. c. 3 *nobile
  perfectibile*; Aristot. I. de Caelo text. 8 secundum quantitatem;
  Gen 1,20+26 + *secundum* desideratur); p. 380 R footer 4–8 =
  [^12]–[^16] (August. de Quant. animae c. 3 n. 4 *vitam et sensum
  et motum*; Aristot. II. de Anima text. 36 + Vat. *molem*;
  harmonia controversy + Avicenna; August. cap. 4 n. 6 *Tactus
  quintus*; cross-ref cap. 4 n. 6 *Ignis omnia penetrat*); p. 381 L
  footer 1–4 = [^17]–[^20] (Cod. cc + ed. 1 *quia*; Vat.
  *fluctuantis*; codd. *aëre*/cod. K *aërem*; Cap. 6 n. 8 with the
  long Maurist textual gloss); p. 381 R footer 5–7 = [^21]–[^23]
  (Sola Vat. *quia aves moventur sursum* + numbering remark;
  Plures codd. *quia actus et motus maxime est in volatu*;
  *Vide scholion ad praecedentem quaest.*). No `[?]` flags — all
  anchors crisp at 450 dpi.
- Marginal labels preserved inline per locked Vol II convention:
  *Pro 1. opinione.*, *Pro 2. opinione.*, *Replicatur.*,
  *Duplex quantitas et praedominantia.*, *Conclusio 1.*,
  *Conclusio 2.*, *Ratio ex fine, tripliciter.*,
  *Idoneitas ad vitam.*, *Item ad sensum.*, *Item ad motum.*,
  *Duplex commixtio.*, *Duplex modus producendi.*, *Corollarium.*,
  *Ad replic. in 5. pro 2. opinione.* — all crisp at 450 dpi
  from p. 379 L+R gutters, p. 380 L+R gutters, p. 381 L gutter.
- Cross-chunk footer-split check: q2's Notes explicitly stated
  `p. 379 carries no q2-side footer; q3's footers will live in
  d15-a1-q3`. The 4 L-column + 4 R-column p. 379 footer notes all
  anchor unambiguously in q3 (none migrate back to q2). q3-close
  footer 7 at p. 381 R = the *Vide scholion ad praecedentem quaest.*
  pointer (intra-chunk).
- Audits: paraphrase HIGH (expected first-pass); apparatus-count
  flag cleared for q3 (skeleton flags persist on `d15-a2-q1` +30,
  `d15-a2-q2` +24, `d15-dubia` +28 — clears as those promote);
  header audit ART -1 / DUB -1 fires because `d15-a2-q1/q2` +
  `d15-dubia` are still skeleton — clears as those promote.
- Build: 589 → 590 translated.

## Prior session (2026-05-25, fourth chunk)

Promoted `d15-a1-q2` Tier-2:
- *Utrum corpora animalium sint composita ex quatuor elementis.*
  Spans p. 377 R bands 1–2 (`QUAESTIO II.` opener immediately after
  q1 SCHOLION II ends on p. 377 R band 0; *Ad oppositum* args 1–6 +
  *Ad oppositum arguitur sic* / *Fundamenta* 1–3) → p. 378 L+R
  (Fundamenta arg. 4 + CONCLUSIO + Respondeo with *Rationes 4.* +
  *Corollarium.* on aqua/aer/ignis penetration proportions +
  *Solutio oppositorum* ad 1–6 with *Notandum.* marginal) → p. 379
  L+R top (SCHOLION I = Petr. a Tar. / Richard. a Med. / Scot. /
  S. Thom. / B. Albert. on plurality of forms in mixtions; SCHOLION
  II = commentator list including Aegid. R., Dionys. Carth., Biel).
  q3 opens lower on p. 379 in the next chunk.
- 14 apparatus entries renumbered sequentially across two pages:
  p. 377 L footer 1–3 = [^1]–[^3] (Gen 1,20 + Aristot. Phys./Metaph./
  de Anima + Lib. de Causis prop. 17); p. 377 R footer 4–5 = [^4]–
  [^5] (cross-ref to d. 14. p. II. a. 2. q. 1 + Aristot. II. de
  Anima text 121 with Vat. *et radicatur* variant); p. 378 L footer
  1–3 = [^6]–[^8] (organicum + Alex. Hal. compound; Aristot. II. de
  Anima text 31; Vat. *complexionis*/*dicitur*); p. 378 R footer 4–9
  = [^9]–[^14] (Cod. cc *profundit* + Aristot. de Gener. et corrupt.;
  *Quaest. seq.* short cross-ref; Dist. 17. a. 2 + I Sent. d. 17 p. II
  q. 2 ad 2/3; codices on *formis*/*spiritibus*; Vat. *secundum
  earum partem*; Aristot. II. de Gener. et corrupt. text 59 with
  Vat. *materiae vel*). No `[?]` flags — all anchors crisp at 450 dpi.
  p. 379 carries no q2-side footer (scholion runs above the q3 body;
  q3 footers will live in `d15-a1-q3`).
- Marginal labels preserved inline per locked Vol II convention:
  *Ad oppositum.* (× 2 — once at the affirmative-side opener via
  the printed marginal and once at the *Ad oppositum arguitur* turn),
  *Fundamenta.*, *Conclusio.* (× 2 — once as the head before the
  conclusio block, once embedded inside the Respondeo as the
  *Conclusio.* marginal), *Rationes 4.*, *Corollarium.*, *Solutio
  oppositorum.*, *Notandum.*
- Cross-chunk footer-split check: p. 377 footer was reviewed against
  `d15-a1-q1` Notes — q1 already absorbed its share (the q1 scholion-
  side footers anchored at [^28]/[^29] per the q1 hand-off). The 3
  L-column footer notes used here anchor unambiguously in q2's
  fundamenta arg. 1/2/3; the 2 R-column notes anchor unambiguously
  in q2's *Ad oppositum* arg. 4 and *Fundamenta* 1. No q2 footer
  migrates back to q1.
- Audits: paraphrase HIGH (expected first-pass over OCR-mangled
  base); apparatus-count flag cleared for q2 (skeleton flags
  persist on the four a*/dubia siblings — d15-a1-q3, d15-a2-q1,
  d15-a2-q2, d15-dubia); header audit Q-LOSS/A-LOSS/DUB-LOSS still
  fires because the four siblings + dubia are skeleton — clears as
  those promote.
- Build: 588 → 589 translated.

## Prior session (2026-05-25, third chunk)

Promoted `d15-a1-q1` Tier-2:
- *Utrum animae irrationalium sint productae ex aliquo.* Spans
  p. 372 R bottom (`ARTICULUS 1.` L foot, `QUAESTIO I.` R band 2) →
  p. 373 (Fundamenta 3–6 + *Ad oppositum* 1–6) → p. 374 (Conclusio
  + Respondeo opening *Opinio 1./2./3.* + *Non approbantur*) →
  p. 375 (*Opinio 4.* + *Corollarium 1./2.* + *Ratio ex Augustino
  et Philosopho* + *Conclusio 2.* + Solutio ad 1, 2) → p. 376
  (*Alia solutio,* Solutio ad 3, 4 + *Obiectio solvitur* + Solutio
  5 + *Solutio aliorum non probatur* + Solutio 6 + SCHOLION opener)
  → p. 377 L top (SCHOLION I continuation: Petr. a Tar. / S. Thom. /
  Scot. discussion of seminal reasons) + R top (SCHOLION II
  commentator list). `QUAESTIO II.` opens L bottom of p. 377 in
  the next chunk.
- 29 apparatus entries renumbered sequentially across six pages:
  p.372 commentary-side footers 3–4 = [^1]–[^2] (picked up from
  d15-divisio hand-off, both anchors crisp); p.373 footers 1–9 =
  [^3]–[^11]; p.374 footers 1–3 (incl. Phys. I text 82) +
  cross-page = [^12]–[^15]; p.375 footers 1–6 = [^16]–[^22]
  (incl. the long Gul. Mara *hoc aliquid* gloss at [^22]); p.376
  footers 1–3 = [^23]–[^25]; remaining SCHOLION-area + Solutio 5/6
  cross-references = [^26]–[^29]. No `[?]` flags — all anchor
  positions crisp at 450 dpi.
- Marginal labels preserved inline per locked Vol II convention:
  *Fundamenta.*, *Ad oppositum.*, *Conclusio.* (× 2 inside
  Respondeo), *Opinio 1./2./3./4.*, *Non approbantur.*,
  *Corollarium 1./2.*, *Ratio ex Augustino et Philosopho.*,
  *Conclusio 2.*, *Solutio oppositorum.*, *Notandum.* (× 5),
  *Alia solutio.*, *De generatione aequivoca.*, *Obiectio
  solvitur.*, *Solutio aliorum non probatur.*
- Audits: paraphrase HIGH (expected first-pass over OCR-mangled
  base); apparatus-count flag cleared for q1 (skeleton flags
  persist on a*/dubia siblings); header audit Q-LOSS still fires
  because remaining d.15 quaestiones + dubia are skeleton —
  clears as those promote.
- Build: 587 → 588 translated.

## Prior session (2026-05-25, second chunk)

Promoted `d15-divisio` Tier-2:
- *Commentarius in Distinctionem XV — De productione mixtorum et
  sensibilium sive animalium.* Single-page chunk on p. 372 below the
  d15-littera tail (`completum et consummatum vidit.`) at the
  *COMMENTARIUS IN DISTINCTIONEM XV.* opener (raw 26280) → DIVISIO
  TEXTUS (3-part split, then 2/2/2 sub-split) → TRACTATIO QUAESTIONUM
  (2 quaestiones; the first sub-divides into 3 articles) → close at
  *Circa primum quaeruntur tria. … an e contrario.* immediately before
  `ARTICULUS 1.` at raw 26310. Per locked Vol II convention the
  divisio holds DIVISIO TEXTUS + TRACTATIO QUAESTIONUM (+ the
  first-article sub-divisio fold-in).
- 2 apparatus entries from p.372 commentary-side footer ([^1] = Vat.
  *simplicium et insensibilium.* anchored at `productione rerum
  insensibilium¹`; [^2] = Vat. *dubitationes duas. Unam, ibi:
  Quaeri solet de venenosis. Aliam, ibi: De quibusdam etiam minutis.*
  anchored at `solvit dubitationem²`). Picked up the cross-chunk
  hand-off from d15-littera (which flagged footer ¹ as belonging
  here); footer ² also anchored in divisio. Footers ³–⁴ migrate to
  d15-a1-q1 (Fundamenta arg. 1 + arg. 2). No `[?]` flags — both
  anchor positions crisp at 450 dpi.
- Audits: paraphrase HIGH (expected first-pass); apparatus-count flag
  cleared for divisio (skeleton flags persist on a*/dubia siblings);
  header audit Q-LOSS / A-LOSS expected (divisio has no
  ART/QUAEST/DUB headers — clears as the article quaestiones promote).
- Build: 586 → 587 translated.

## Earlier session (2026-05-25, first chunk)

Promoted `d15-littera` Tier-2:
- *Distinctio XV — Littera Magistri*, Cap. I–X (10 capitula),
  pp. 370 L bottom (DISTINCTIO XV. Cap. I. *Dixit etiam Deus...*
  immediately after d.14-p2-dubia close at raw 26148) → 371 L+R →
  372 L+R band 0 close at *completum et consummatum vidit.*
  immediately before *COMMENTARIUS IN DISTINCTIONEM XV.* opener.
  Lombard's chapter sequence covers: Cap. I work of the fifth day
  (creatures from waters); Cap. II work of the sixth day (animals
  and reptiles from earth); Cap. III venomous and noxious animals
  created innocuous, made noxious through sin; Cap. IV minute
  animals from putrefaction; Cap. V why man was made last + the
  two opinions on creation through intervals vs simultaneously
  introduced; Cap. VI the *simul-omnia* opinion of Augustine
  (formaliter / materialiter / causaliter); Cap. VII rest of God
  on the seventh day; Cap. VIII how God can be said to complete
  on the seventh day; Cap. IX all things called *valde bona;*
  Cap. X sanctification of the seventh day.
  12 apparatus entries continuously renumbered: p.370 footer
  NOTAE 1–4 = [^1]–[^4]; p.371 footer NOTAE 1–8 = [^5]–[^12].
  p.372 carries no littera-side footer (COMMENTARIUS opens
  immediately after the *completum et consummatum vidit.* tail).
  No `[?]` flags — all 12 anchors and all marginal labels crisp
  at 450 dpi. Marginal labels preserved inline per locked Vol II
  convention: *Dubium 1.* (Cap. I), *Dubium 2.* (Cap. II),
  *Augustinus.* (×5), *Dubium 3.* + *Opinio 1.* (Cap. V),
  *Opinio 2.* (Cap. VI), *Dubium 4.* (Cap. VII), *Dubium 5.* +
  *Dubium 6.* (Cap. X) — Dubium numbering runs 1→6 continuously
  with no Pars-reset ambiguity (unlike d.14-p1-littera).
  Apparatus-count audit: chunk=12 vs raw=13 diff=+1 (no flag —
  raw 13th is the p.370 commentator-list note already consumed
  at `d14-p2-dubia` [^38]). Paraphrase audit: HIGH bucket
  (expected first-pass for new Tier-2 chunk over OCR-mangled
  base). Header audit: Q-LOSS / A-LOSS flags fire only because
  d15-divisio + d15-a*-q* + d15-dubia are still skeletons (no
  ARTICULUS/QUAESTIO/DUB headers in a littera chunk by design) —
  will clear as those promote.
  Build: 585 → 586 translated.

**d.15 PARS-SPLIT DETERMINATION:** d.15 has **NO pars split.** Running
heads across the entire d.15 commentary read `DIST. XV. ART. I.
QUAEST. I/II/III.` and `DIST. XV. ART. II. QUAEST. I/II/III.` — no
`P. I.` / `P. II.` ever appears. The d.15 chunk inventory therefore
proceeds without `d15-p1-*` or `d15-p2-*` files; see chunk list below.

## What to do this session

**Promote `d15-dubia`** — last d.15 chunk. Opens at raw 27638 with
`DUBIA CIRCA LITTERAM MAGISTRI` header on p.388 L band 1 +
R band 0 immediately after the d15-a2-q3 SCHOLION II close. DUB. I
opener `In parte ista incidunt dubitationes circa litteram, et primo
quaeritur de hoc quod dicit: Producant aquae reptile animae viventis.`
Standard Vol II Tier-2 procedure: 450 dpi column-band PDF read for
every Respondeo + footer. Apparatus-count audit flags +28
(skeleton) — clears as it promotes.

Remaining d.15 chunk inventory after d15-dubia: empty (d.15 complete).
(Vol II convention: a short articulus opener like *Consequenter...
quaeruntur duo...* folds into that article's q1, so no standalone
`d15-a1-divisio` or `d15-a2-divisio`.)

The "Vat. … quando" parked footer from `d14-p1-littera` Notes still
has no obvious d.14 anchor — defer to the polish-blocker. The
"Art. 2. q. 2." cross-reference catalog from p. 333 is documented
in `d14-p1-a2-q2` Notes as deferred (no clean inline anchor in
q2 body) pending the polish-blocker.

## d.15 chunk inventory (in semantic order)

- ~~`d15-littera`~~ **DONE 2026-05-25.**
- ~~`d15-divisio`~~ **DONE 2026-05-25.**
- ~~`d15-a1-q1`~~ **DONE 2026-05-25.**
- ~~`d15-a1-q2`~~ **DONE 2026-05-25.**
- ~~`d15-a1-q3`~~ **DONE 2026-05-25.**
- ~~`d15-a2-q1`~~ **DONE 2026-05-25.**
- ~~`d15-a2-q2`~~ **DONE 2026-05-25.**
- ~~`d15-a2-q3`~~ **DONE 2026-05-25.**
- **`d15-dubia`** — NEXT.

## Tooling status

- 450 dpi PDF crops cached for pp. 274–379 at `/tmp/colcrop/vol2-p*`.
  Generate p. 380+ as needed.
- Manual-rescue chunks (d.11–d.20 boundary sweep) still skeleton:
  d18-dubia, d19-littera. (d16-a1-q2 cleared 2026-05-25.) Promote in normal Vol II cadence.
- Pre-promotion boundary sweep log:
  `manual-review/d11-d20-boundary-sweep-audit.md` — all blockers
  cleared 2026-05-23.

## Open `[?]` flags (parked for d.11–d.20 polish-blocker)

From `d14-p1-littera`:
1. Cap. IX marginal *Dubium 3.* vs *Dubium 1.* (Pars II reset
   ambiguity) — `[?]` flag in chunk + Notes block.
2. Cap. X marginal *Dubium 1.* vs *Dubium 4.* (gutter-crushed digit).
3. Cap. VII Pars II reset of Dubium numbering — preserved as printed.

From `d14-p1-a1-q1`:
4. Scholion II at `Alex. Hal., S. p. II. q. 50. m. 1.[?]` — stray glyph
   (likely `1.` or `n. 1.`) before em-dash to `Scot.` at 450 dpi.

From `d14-p1-a1-q2`:
5. Affirmative arg 1: markers [^1][^2][^3] are clustered at the end
   of "*auctoritatem Scripturae*" — in-line positions of the three
   Quaracchi marker glyphs within arg 1's body were not recoverable
   at 450 dpi. Resolve at 600 dpi.
6. p.338 footer split-convention discrepancy: the resume + q1's Notes
   claimed all four p.338 footer notes belong to q2, but column-band
   re-read showed notes ¹ Gen 1,2 and ² Gen 1,6 also anchor in q1's
   Corollarium body ("*ut ibi¹: Spiritus Domini... aliquando..., ut
   ibi²: Fiat firmamentum*"). Decision to promote here per the resume;
   polish-blocker should reconcile (accept dual anchor, or move ¹/²
   back to q1 as [^22]/[^23]).

From `d14-p1-a2-q1`:
7. Arg 2 in-line position of marker [^2] (p.341 footer note `Part.
   II. huius d. a. 2. q. 2.`) — no printed superscript glyph visible
   at 450 dpi within arg 2; placed at end of clause as the
   cross-reference for *motus circularis*. Resolve at 600 dpi.
8. Scholion II codex sigil `F1 (T a secunda manu)` — parenthesis is
   faint at 450 dpi (confirmed but not crisp).

From `d14-p1-a2-q2`:
9. *Ad oppositum* arg. 6 in-line position of marker [^9]
   (`quod nullo modo concedi potest⁹`) — footer note exists
   unambiguously (Aristot. text 15) but the printed `⁹` superscript
   is faint at clause-end at 450 dpi; placed at the natural
   cross-reference position. Resolve at 600 dpi.
10. Parked p. 333 *Art. 2. q. 2. — Cfr. etiam supra d. I. p. I. dub.
    1; d. 10. dub. 1; d. 12. dub. 1; …* cross-reference catalog from
    `d14-p1-littera` Notes: confirmed no clean inline anchor in
    a2-q2's body. Disposition (capture as appended Scholion-style note,
    or confirm as p.333 NOTAE editorial apparatus that does not
    migrate) deferred to polish-blocker.

From `d14-p1-a3-q1`:
11. *Ad 3* in-line position of marker [^13] (p. 346 R footer note 7,
    `Cfr. Aristot. VIII Phys. text. 35`) — printed superscript not
    crisp at 450 dpi between [^12] (*per quem movet*) and the *Ad 4*
    opener; placed at *nec perfectus status* by inference. Resolve at
    600 dpi.

From `d14-p1-a3-q2`:
12. `[^25]` apparatus body (p. 350 L footer note 1): the verbatim
    Vat. variant `In Vat. desiderantur verba et per hoc etiam...
    litteram [?]. Vide scholion ad praecedentem quaest.` — the
    ellipsis-bracketed tail at *litteram* could read *litteralis* or
    be elided differently. Resolve at 600 dpi.

## Open project-wide TODOs

- **Next decade polish-blocker fires after d.20.** Three-pass cadence;
  `manual-review/d11-d20-polish-resolution-log.md` will be the log.
- **Vol I site copy** still hardcodes "Volume I" in
  `site/src/app/page.tsx:47,57` — update when Vol II has enough real
  chunks to surface in landing copy.

## Convention reminders

- "keep going" = continue chunk-by-chunk, committing each, no check-ins
  (cf. [[feedback_bonaventure-bucket-e-autopilot]]).
- Tier-2 = literal, not paraphrase, incl. scholia/apparatus.
- Marginal labels (*Ad oppositum.*, *Fundamenta.*, *Ratio …*,
  *Solutio …*, *Notandum.*, *Alia solutio.*, *Dubium N.*, etc.) are
  preserved inline per Vol II convention, NOT promoted to headings.
- Backup before any rebuild: `cp <chunk>.md _backup-<chunk>-pre-<reason>-<YYYYMMDD>/`.
- Vol II offset: `pdf = printed + 22`. Trust running-head text, never
  the OCR'd digits.

Prior session-by-session vol2 history (sessions 1–77) is trimmed per
Wilson's request 2026-05-22; the per-decade resolution logs and chunk
`## Notes` are the durable record. Backup of the pre-trim resume is at
`_backup-resume-pre-trim-20260522.md` if you need to walk back.
