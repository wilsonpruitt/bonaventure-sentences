# d.7 Scaffolds Sweep-Audit Resolution Log

Audit date: **2026-05-08**. Source of truth: `raw/bonaventure_vol1_raw.txt` (Internet Archive djvu OCR of Quaracchi 1882, Tomus I, pt. 1). Same sweep model used for d.1, d.2, d.3 — diff `## Latin` body against OCR slice; diff every `[^N]:` apparatus entry against the OCR footer block for the relevant printed page; never invent Latin; never fabricate apparatus.

The three d.7 scaffold chunks under audit:

| Chunk | Original bounds | True OCR bounds | Pages |
|---|---|---|---|
| d7-littera | 29025–29108 | **28913–29107** (chunk's bounds were offset by one printed page; missed all of p.132) | pp. 132–133 |
| d7-divisio | 29109–29244 | 29109–29242 | pp. 134–135 |
| d7-dubia | 30742–31016 | 30742–31015 | pp. 145–146 |

## Per-chunk verdicts

### d7-littera — REBUILT (4 body restorations + full apparatus rebuild)

**Bounds were wrong**: chunk frontmatter said `line_start: 29025` but actual Lombard text of *Distinctio VII* in OCR begins at line 28913 (printed p. 132, not p. 133). The chunk's `printed_pages: [133, 134]` was also wrong — the Master's text on this distinction occupies pp. 132–133 (p. 134 is where the *Commentarius / Divisio textus* begins, which is the divisio chunk's territory).

**Body departures fixed (silent abridgment caught):**

1. **Augustine quotation truncated.** The chunk ended Augustine's "Immoderata enim..." quote at *impotens diceretur* but OCR (lines 28962–28968) continues: «Similiter etiam ille, si nepotem non gigneret avo suo et pronepotem proavo suo, non a vobis appellaretur omnipotens; nec impleretur generationis series, si semper alter ex altero nasceretur; nec eam perficeret ullus, si non sufficeret unus omnipotens. Itaque omnipotentem genuit Filium Patris natura, non fecit». **The truncated 4-clause continuation has been restored** in both Latin and English bodies.

2. **Lombard's gloss after "nasci non potuit" dropped.** OCR line 29034–29036 reads: «Si enim nasci potuit, potuit esse filius, et ita mutabilis esse potuit». The chunk omitted this entire sentence (which is the Master's own reductio). **Restored.**

3. **Quomodo ergo accipietur — Lombard's confessional gloss dropped.** OCR lines 29040–29043 contain: «Non est nobis perspicuum aperire, quomodo sit hoc verum, et ideo sub silentio potius esset praetereundum, nisi me super hoc aliquid loqui cogeret instantia quaerentium». The chunk had collapsed past this (Lombard openly admitting he can't fully expound the point) directly to the *Potest sic intelligi* solution. **Restored.**

4. **Cap. I tail (Maximinus dialogue + "De quibus proprietatibus...") dropped.** OCR lines 29048–29056 read: «Nam et Pater similiter non est Filius, nec hoc est ex impotentia Patris. Sed quaerit Maximinus, Arianorum Episcopus: unde ergo est, quod Pater non potest esse Filius, vel Filius Pater? Non utique ex impotentia, sed Pater proprietate generationis Pater est, qua oportet eum non esse Filium, et Filius proprietate nativitatis Filius est, qua oportet eum non esse Patrem. De quibus proprietatibus postea plenius tractabitur». **All eight clauses restored** — this is the doctrinally critical move from impotence-language to property-language that the Master uses to pivot into d.8.

5. **Cap. II — full *e converso* passage dropped.** OCR lines 29094–29100 contain a substantive expansion: «sicut dicitur: Pater habet potentiam, qua potest esse Pater; Filius vero non habet potentiam, qua possit esse Pater; et e converso, Filius habet potentiam, qua potest esse Filius, Pater vero non habet potentiam, qua possit esse Filius: habet ergo aliquam Pater, quam non habet Filius, et e converso. Absit». The chunk had elided this entirely between *falsum est* and *Absit*. **Restored.**

**Apparatus — full rebuild from real OCR footers.** Original chunk had 4 entries: 2 Augustine *contra Maximinum* and *de Trin.* citations (substantive but only loosely paraphrased) and 2 cross-reference stubs. The actual Quaracchi apparatus comprises **17 textual-variant notes** in two blocks:

- p. 132 *Notae ad Lib. Sententiarum* (raw lines 29002–29022) — 8 footnotes (`Vat. vel`; `Supple cum cod. A divinae`; `praepositi loco propositi`; `Edd. 1, 2, 8 addunt et`; `Vat. cum edd. 4, 6 non`; `Dist. XXVIII c. 5`; `Cap. 12, n. 2` [Augustine *c. Maximinum* II]; `potuerit`).
- p. 133 footer (raw lines 29133–29170) — 11 footnotes consolidated to 9 chunk entries (`hic repetit aliquam`; `accipiatur`; `Mendum Vat. omittentis ergo`; `Codd. hic repetunt ex`; `Dist. XXVI`; long Vat./codd. block on `hoc...non...Pater`; `addit et`; `significas` + `ADE addunt et`; the two `scilicet`/`Vat. cum ed. 4 indebite omittit`/`In codd. BDE deest esse` notes consolidated as `[^17]`).

All 17 entries are now bilingual `**La.** ... **En.** ...` traces of the Quaracchi footer, with body anchors placed at OCR-verified positions. Augustine's *contra Maximinum* II c. 12, n. 2 — which the chunk had given a Patrologia-style apparatus pointing at the body quote — is now apparatus entry `[^7]` (the actual Quaracchi note: `Cap. 12, n. 2. — Mox Vat... post potentiorem addit esse...`). The Augustine citation is preserved in the *body* text where Bonaventure himself cites it; the apparatus does what the Quaracchi apparatus actually does (textual collation).

**Frontmatter:** `printed_pages: [132, 133]`, `pdf_pages: [234, 235]`, `line_start: 28913`, `line_end: 29107`. `transcription_status` updated to canonical Tier-2 string with audit-date 2026-05-08.

### d7-divisio — REBUILT (1 body restoration + full apparatus rebuild)

**Body departure fixed:** the chunk had truncated the *Divisio textus* discussion at *vera est* (corresponding to OCR line 29207) and skipped the entire *gerundium / significatio passiva-activa* block (OCR lines 29207–29221), which contains Bonaventure's grammatical analysis of *generandi* (gerund of personal vs. impersonal verb, with worked-out senses of «Filius habet potentiam, qua aliquis generat»). **Roughly 14 OCR lines of dense scholastic grammatical analysis restored** in both Latin and English. The English now exposes the *ly generandi* / personal-vs-impersonal distinction faithfully.

Also restored: the lemma *«Item quaeritur a quibusdam, si Pater»* etc. which OCR (line 29188) re-prints at the head of the second-part divisio (the chunk had used a quoted-italic but had merged the lemma into running prose).

**Apparatus — fabrication caught and replaced.** The original 2 chunk entries (`[^1]` "Cfr. supra d.6, *Divisio textus*..." and `[^2]` "De distinctione *active* / *passive* ... cfr. infra a. unic., q. 2") are **invented cross-references — not in OCR**. The actual *Notae* at the foot of printed p. 134 covering the Commentarius (raw OCR lines 29270–29316) contain **8 textual-variant footnotes**:

1. `Ex vetustioribus mss. et ed. 1 supplevimus ipsam` (anchored at *exponens ipsam*).
2. `Vat. absque auctoritate mss. et ed. 1, omittendo verba Item quaeritur... mutat constructionem...; codd. cum ed. 1 tres loco duas, sed falso` (anchored at lemma + `duas particulas`).
3. `Ex mss. X Y bb et ed. 1 adiecimus Et... cod. Q vero Secundo et paulo infra tertio pro secundo, at falso` (anchored at *Et ad hanc quaestionem*).
4. `Ex antiquioribus mss. et ed. 1 substituimus intelligatur pro intelligitur...habeat loco habet...ista pro illa...aliquos loco alios` (anchored at `intelligatur active`).
5. `Vat. Sed... omittit hoc... pro gerundium ponunt gerundimum` (anchored at start of restored gerundium passage).
6. `Cod. O glossando addit: scilicet Pater, quia eadem est potentia in Patre et in Filio ad hoc ut generetur...` (anchored at `aliquis generat`).
7. `Ope mss. et ed. 1 restituimus omissum Filio` (anchored at *Pater communicet Filio* in the question list).
8. `Mendum Vat. fide mss. correximus substituendo univocum pro unicum` (anchored at the fourth question's *posse univocum*).

All 8 reset bilingually at OCR-verified positions. `line_end` corrected from 29244 to 29242.

### d7-dubia — REBUILT (3 body fixes + apparatus rebuild)

**Body departures fixed:**

1. **Dub. I preamble was duplicated.** Chunk had a free-standing preamble «In parte ista incidunt dubitationes circa litteram, et prima est de solutione ista Magistri.» followed by `#### Dubium I` and then «Prima est de solutione ista Magistri, qua dicit, quod...». OCR (line 30744–30745) has the preamble as the *opening clause of Dub. I itself*, not as a separate sentence: «In parte ista incidunt dubitationes circa litteram, et prima est de solutione ista Magistri, qua dicit, quod...». **De-duplicated.**

2. **Dub. VII tail dropped.** Chunk ended Dub. VII at *quin potentia gignendi passiva sit in Filio*. OCR (lines 30960–31015) continues for ~15 more lines: «Sed illa potentia non / est principium generationis, sed idoneitas / sive hypostasis cum sua proprietate ad generari. / Unde quod dicitur posse gigni, potentia potest intelligi originaliter, et sic est in solo Patre; vel formaliter, et sic ponitur esse in Filio; alio autem modo non». **The Master's own resolution of Dub. VII (with the originaliter / formaliter distinction) was missing entirely. Restored.**

3. **Page-break placement wrong.** Chunk placed `<!-- page 146 -->` between Dub. V and Dub. VI. OCR shows the printed-page-146 boundary at line 30995 — **mid-Dub. VII**, between *quin potentia gignendi passiva sit in Filio. Sed illa potentia non* and *est principium generationis*. **Page-break moved to the correct OCR-verified position.**

**Apparatus — partial rebuild.** Of the original 7 chunk entries:

- `[^2]` Richard *de Trin.* III, c. 4 quote → **AUTHENTIC** (matches OCR p. 145 fn 6, raw lines 30835–30836). Retained as `[^5]` in renumbered apparatus.
- `[^4]` "De hoc et sequenti dubio vide hic q. 3 et 4 cum Scholiis" → **AUTHENTIC** (matches OCR p. 145 fn 5, raw line 30833). Renumbered.
- `[^1]`, `[^3]`, `[^6]` (cross-reference inventions like "Cfr. supra hic q. 1 in corp.: distinctio inter potentiam essentialem...") → **FABRICATED**, replaced with the actual Quaracchi textual variants.
- `[^5]`, `[^7]` ("Cfr. supra hic q. 2 et q. 1") → loose paraphrases of OCR p. 146 fns 5 and 7 (`Plura de hoc dubio... vide hic q. 2 et 3...` and `Vide supra q. 1, fundam. 2`). Replaced with verbatim Quaracchi.

The rebuilt apparatus has **18 entries** mapped to the actual Quaracchi footers:

- p. 145 (raw lines 30779–30850): `Supple ... potest`; long Vat./Cum/Tunc note; Vat. *eum generare Filium* corruption + cod. O variant; `praeomittit Vat. effectum seu`; Richard *de Trin.* III c. 4 quote; *intelligit/intelligas* + *a* pro *ex*; Vat. *si Pater non esset aliquid* corruption; `contrahitur` codd. variant; `infra d. 23` cross-ref; one body anchor at *potest dici* preserved with empty-content note (no separate Quaracchi entry there).
- p. 146 (raw lines 30963–30992): Vat. addit *idem*; long *proprietas / hypostasim* note (with d. 26 cross-ref); `diversificationem ponunt pro diversitatem`; *Cod. dd addit potest*; *Plura de hoc dubio... vide hic q. 2 et 3 ac apud Richardum, hic q. 3*; Aristot. *Metaph.* V text 17 + IX text 2 ref; *vide supra q. 1, fundam. 2*; *Aliqui codd. ut T cc modo positivo* + `codd. omittunt tamen`.

`line_end` corrected from 31016 to 31015.

## Summary table

| Chunk | Verdict | Body departures fixed | Apparatus departures fixed | Bounds fixed |
|---|---|---|---|---|
| d7-littera | Tier-2 promoted (rebuilt) | **5** (Augustine quote 4 clauses; *Si enim nasci potuit*; Lombard's *Non est perspicuum* gloss; Maximinus dialogue + *De quibus proprietatibus* — 8 clauses; Cap. II *e converso* expansion) | **17** (apparatus rebuilt; 4 prior entries replaced with 17 Quaracchi textual-variant notes) | **YES** — bounds were 29025–29108 (off by one printed page); now 28913–29107; printed_pages 132–133 |
| d7-divisio | Tier-2 promoted (rebuilt) | **1** (gerundium / significatione passiva-activa block, ~14 OCR lines) | **8** (2 fabricated cross-refs replaced with 8 real OCR footer notes) | line_end 29244→29242 |
| d7-dubia | Tier-2 promoted (rebuilt) | **3** (de-duplicated Dub. I preamble; restored Dub. VII tail with *originaliter/formaliter* distinction; corrected p. 146 page-break) | **18** (3 invented cross-refs replaced; 2 paraphrases tightened to verbatim Quaracchi; 13 new entries added from real OCR) | line_end 31016→31015 |

**Totals:**

- Body paraphrase / silent-abridgment departures fixed across d.7: **9** (5 in littera, 1 in divisio, 3 in dubia).
- Fabricated / placeholder / paraphrased apparatus entries replaced: **9 entries removed, 43 authentic Quaracchi entries reinstated** (17 littera + 8 divisio + 18 dubia).
- Bound corrections: **2** (littera 29025→28913 start; line_end ticks on divisio + dubia).
- `[?]` flags newly added: **0** — all fixes resolvable from OCR without ambiguity. (Note: dubia `[^10]` retains an editorial note that the OCR p. 145 footer has no separate variant note for the *potest dici* clause; the body anchor is preserved for continuity rather than dropped, which would require renumbering 18 markers.)

Backups for chunks edited: `vol1/_backup-d7-{littera,divisio,dubia}-pre-rebuild-20260508/`.

## Pattern observation

The d.7 sweep extends the d.1/d.2/d.3 finding pattern: scaffold chunks (littera + divisio + dubia) were generated by a low-fidelity first pass that (a) silently abridged Lombard's text wherever it wandered into doxographical asides (Lombard's confession that he can't expound how *non potuit / non oportuit* coheres; the Maximinus dialogue) or technical grammatical analysis (the *gerundium* personal/impersonal distinction in d.7 divisio), and (b) treated the apparatus block as a license to invent editorial cross-references rather than transcribe Quaracchi's actual textual-variant notes. The four quaestiones (a1-q1 through a1-q4) of d.7 were not in scope for this sweep but should be checked at the next decade-polish cycle if d.1/d.2 patterns hold (a1-q* tend to be more faithful than the surrounding scaffolds, but it's worth a spot-check).

The d7-littera bound error (29025 instead of 28913) is also a lesson: bounds in scaffold chunks should be cross-checked against the actual semantic start of the Lombard text (the `DISTINCTIO N.` heading + body), not against the OCR's running-head tag for the new printed page. A `tools/audit-bounds.py` that flags chunks whose `line_start` lands on a `DISTINCTIO` running head rather than on body text would catch this class of error mechanically.
