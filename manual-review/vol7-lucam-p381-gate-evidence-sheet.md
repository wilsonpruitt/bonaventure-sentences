# Vol VII *Lucam* p. 381 GATE (ruling 14: close of c. 14; the *pietas* review): EVIDENCE SHEET

Compiled 2026-11-16 by a read-only agent (Opus, on Wilson's authorization). **Nothing here is settled. Wilson rules off this
sheet.** No file under `vol7/`, `tools/`, `site/`, `index/`, the manifest, the ruling file or the resume note was edited.
Nothing was committed, pushed or stashed. No plate was read (no docket item needed one).

**Scope: the 19 chunks of pp. 288–381** (`bon-luc-c11-v14-26` → `bon-luc-c14-v25-35`; XI 4 · XII 5 · XIII 5 · XIV 5). Where
a register question needs it, the census runs over **all 82 Lucam chunks (pp. 3–381)**, and over Vols V–VI where a corpus
precedent decides. Docket source: the consolidated items 1–27 (A–H), D-1..D-7 and the tool items T-a..T-g at the top of
`next-session-resume.md` (ll. 3–71), and each chunk's `## Notes`. Rulings 1–76 (`manual-review/vol7-pilot-setup.md`) bind.

⛔ **Every census is taken over the RENDERED region only:** the `## Latin` and `## English` bodies and the `**La.**` /
`**En.**` halves of `## Apparatus`. Frontmatter, `## Notes` and the `tr-` definitions are excluded. "¶" is the Quaracchi
paragraph in which the site stands; "p. N n. M" is an apparatus entry. Scripts: scratchpad `g381/regions.py`, `cen.py`,
`ctx.py`, `align.py`, `grepl.py`, `show.py`, `reg.py` (the p. 288 sheet's, re-scoped to Cap. XI v. 14 – XIV; `reg.py` runs
76 Latin → English register pairs region by region over the 19 chunks and lists every shortfall, each then read by eye).
Douay checked against `~/douay-glossa/raw/DRC.json`. **Lines** in the cost columns are lines of the chunk file (every body
paragraph, every apparatus half and every `tr-` definition is one line; a frontmatter field is one line).

---

## ⚠ FOUND BY THE SHEET (builder's claim wrong, or a defect / fact not on the docket)

| # | chunk / site | what is wrong | ⭐ fix | lines |
|---|---|---|---|---|
| **F1** | `c12-v8-12` ll. 69, 77, 79, 81, 93, 95, 213 · `c12-v13-34` ll. 155, 203 · `c13-v18-21` ll. 106, 124 · `c13-v31-35` l. 92 (+ `c10-v17-24` ll. 101, 108, pre-interval) | **"Holy Ghost" against ruling 17 ("Holy Spirit" everywhere, Douay quotations included).** 16 occurrences on 12 lines in four interval chunks; `c12-v8-12` has **zero** "Holy Spirit" (the Luke 12:10 lemma ¶ 15, I Cor. 12:3 ¶ 12, Bede's quotation ¶ 16, p. 315 n. 12 **En.**, all "Holy Ghost"). Lucam total: **"Holy Spirit" 164 / "Holy Ghost" 20**, and the 20 are these 14 lines. `c10-v17-24` (Luke 10:21 *exsultavit in Spiritu sancto*, Rom. 14:17, ¶ 39) passed the p. 288 gate unseen. Not on the docket; no Notes in any of the five chunks claims it | "Holy Ghost" → "Holy Spirit", literal replace on the 14 lines (grep `Holy Ghost` → 0 in the rendered region after) | **12** (+ **2** pre-interval) |
| **F2** | `c14-v12-15` ¶¶ 26, 27 (ll. 68, 72); `c14-v25-35` `title_en` (l. 11), `####` (l. 96), ¶ 51 (l. 98) | ***erudire* → "teach" / "instruct" against ruling 32's row** (*erudire* body prose "school"; *instruere* "instruct", kept apart). *exhortationem erudientem* "the exhortation teaching" ×2; the t4 *Tertio erudiuntur turbae subsequentes* "Third the multitudes following are **instructed**" (also `title_en`); ¶ 51 *erudivit convivantes … erudit comitantes … Erudiens* "instructed … instructs … instructing". `c14-v1-6` ¶ 1 renders the same divisio clause *erudit turbas subsequentes* "**schools** the crowds following", so the two chunks name one member two ways. Both chunks' Notes claim the wrong register (`c14-v25-35` l. 549 "*erudire* 'instruct' (the house verb)"; `c14-v12-15` l. 335 "*eruditio / erudiens* 'teaching'"). **Census, all 82:** *erudire* (verb, prose) "school" at 25 paragraphs; the non-"school" prose sites are these five lines and **two pre-interval**: `c9-v10-17` ¶ 16 *ut Dominum erudirent* "teach" (l. 82), `c9-v32-36` ¶ 64 *erudiuntur contemplativi* "are taught" (l. 105). Douay verses (Prov. 9:7, Jer. 13:21, Dan. 12:3, II Tim. 3:16) keep the Douay | "the exhortation schooling" (¶¶ 26, 27); "Third the multitudes following are schooled, of which two things" (`title_en` + `####`); ¶ 51 "and schooled the guests at table … In the first he schools *those who accompany him* … Now schooling through *express words*"; (pre-interval) "that they might school the Lord", "contemplatives are schooled" | **5** (+ **2** pre-interval) |
| **F3** | `c13-v1-9` ¶ 12 (l. 176); `c14-v16-24` ¶ 37 (l. 93); `c14-v25-35` ¶ 52 (l. 102) (= passes **N-1**) | ***benignitas* → "benignity" against ruling 45 / ruling 32's row** (*benignitas* "kindness", *benignus* "kind", **into quotations too**). Rom. 2:4 *benignitas Dei* "the benignity of God" (the Douay's word, which ruling 45 adjusts: Ps. 64:12 "the year of thy kindness"); ¶ 37 *summam liberalitatem et benignitatem* "liberality and benignity" and ¶ 52 *conversus … per benignitatem* "through benignity" are Bonaventure's prose. **Census, all 82:** *benignitas* 38 La body; "kindness" 35; **"benignity" 3, all three in this interval.** Not on the docket | "the kindness of God"; "the highest liberality and kindness"; "through *kindness*" | **3** |
| **F4** | `c12-v1-7` ¶ 2 (l. 94), ¶ 6 (l. 104) (= passes **N-2**) | ***lumen* in Bonaventure's own prose → "light", no `tr-lumen` anywhere in the chunk.** ¶ 2 *et tenebra per lumen expellitur* "and darkness is driven out by light" (outside the guillemets of the maxim at p. 310 n. 6); ¶ 6 *Lumen enim solis visui cetera manifestat* "For the light of the sun makes other things manifest to sight", glossing the lemma Luke 12:3 *in lumine dicentur* "shall be spoken in the light" in the same paragraph. Ruling 32's row and ruling 50: *lumen* in the prose is "lumen" (the physical lamp-*lumen* of `c11-v33-41` ¶ 71, `c12-v35-48` ¶ 50 is so rendered). **Census, all 82 (case-insensitive align):** 55 *lumen* sites; every other non-"lumen" site is a verse quoted as a verse with nothing leaning. **These two are the only *lumen* of Bonaventure's prose rendered "light" in the work.** And ¶ 6's prose **leans on the lemma's word**, so under rulings 27 / 50 the lemma takes "lumen" too (the p. 288 F8 shape: Matt. 10:27 "in the lumen" where the paragraph leans; Luke 11:35 "the lumen which is in thee"). Item 7's "12:3 'spoken in the light'" (the adjustment of the Douay's "published") is untouched in its verb. Not on the docket | ¶ 2 "and darkness is driven out by lumen[^tr-lumen]"; ¶ 6 "*shall be spoken in the lumen.*" … "For the lumen of the sun makes other things manifest to sight"; + one `tr-lumen` at ¶ 2 (the `c12-v35-48` form, naming ¶ 6's lemma) | **3** |
| **F5** | `c11-v42-54` ¶ 87 (l. 99), p. 305 n. 6 **En.** (l. 182) (= passes **N-3**) | ***redarguere* → "rebukes" against ruling 56** (*redarguere* "convict"; "rebuke" is *increpatio*'s, ruling 32). The Gloss (Ambrose) *Arrogantiam redarguit* "He rebukes arrogance", body and note. **Census, all 82:** *redarguere* 20 regions, "convict(s / ed / ion)" at 18; **these two are the only exceptions** | "He convicts arrogance" ×2 | **2** |
| **F6** | `c14-v12-15` ¶ 28 (l. 76) | **Prov. 23:21 off the Douay with nothing leaning:** *dantes symbola* "and that give clubs", where the Douay (and `c12-v13-34` ¶ 29, the same verse two chunks earlier) reads "and that club together". Quaracchi's Latin is the same at both sites; ruling 28's split is licensed only by a lean, and none stands | "and that club together" | **1** |
| **F7** | `c14-v7-11` p. 365 n. 15 **En.** (l. 328) | ***mirabilis* → "wonderful" in an editors' quotation** (*efficit operationes mirabiles*), against ruling 32's row (*admirabilis* "wonderful" · *mirabilis* "marvellous", into quotations too). In the apparatus of all 82: *mirabil-* "marvel-" 5, "wonderful" 2 (this and `c2-v40-52` p. 67 n. 11, pre-interval, not re-read) | "effects marvellous operations" | **1** |
| **F8** | D-2 framing | **The docket calls Ps. 4:7 "light" a defect; under the corpus test it is not** (§ D-2). The CLAUDE.md line keeps "lumen" at Ps. 4:7 *because* `bon-qmt-q1-a2` p. 55 n. 9 anchors the body's own *lumen divini vultus*; the test it states is per site. `c12-v49-59` ¶ 84 has no *lumen* in the unit | none (record) | doc |
| **F9** | D-3 scope | **D-3 is two defects, not one, and the third named site is not one.** p. 316 n. 2 (Augustine) and **p. 373 n. 12** (Gregory, *nullum ingenii lumen* "no light of wit") are Fathers' quotations, which ruling 50 puts inside the rule; **p. 339 n. 5** is Isa. 9:2 quoted as a verse inside the Gloss, which leans on *umbra mortis*, not on *lumen*: exempt by the test | D-3 at two sites (§ D-3) | (in D-3) |
| **F10** | D-5 census (= passes **N-4**) | ***excessivus* stands at 4 Lucam sites, "excessive" at 3** (`c9-v32-36` ¶ 61 + p. 236 n. 7 *excessivum desiderium … prae nimietate desiderii*; `c12-v49-59` ¶ 72 *adhaerentiam excessivam* "an excessive adherence"), **"transporting" at 1** (D-5). The docket presents D-5 as one site; the ruling it asks for governs all four | (§ D-5) | doc |
| **F11** | D-6 cause | **Located:** `scan_page()` in `tools/build-citations.py` (l. ~794) captures `supra` / `infra` but never checks the direction against the citing page, so *supra pag. 297, nota 7* (cited from p. 295) resolves by page + note to `fn-p297-7` (`c11-v27-32`, Gen. 15:5 / Ps. 131:11), which carries nothing of Jerome on Matt. 12:43. **A direction screen over the whole ledger finds 4 such records** (this one; `bon-ioan-c13-v21-30` p. 432 n. 9 *supra pag. 436*; `bon-sent-III-d27-dubia` p. 615 n. 15 *supra pag. 877*, p. 619 n. 1 *supra pag. 643*) | a `CROSSREF_SLIPS` row + a report-only direction screen (§ T, J-12) | 0 text |
| **F12** | records | No text effect: (a) item 7's "12:20 'soul'" is the **Douay's own** wording (DRC: "this night do they require thy soul"), not an adjustment; (b) Luke 14:26 is a **ruling-28 split across chunks** the docket does not list: "his own **life**" at `c12-v49-59` ¶ 75 (adduced, nothing leans) / "his own **soul**" at `c14-v25-35` ¶ 52 (the lemma; ¶ 53 leans); (c) John 12:25 is "soul" at all three Lucam sites (`c9-v18-27`, `c12-v13-34` ¶ 29, `c14-v25-35` ¶ 53), each on a leaning paragraph; (d) the docket's T-e names *notam 11* at p. 373 n. 5, but the ledger's record is `supra pag. 261` → `page-multi` (the accusative is not captured: J-4's class, as T-e says) | doc | doc |
| **F13** | `c11-v14-26` ¶ 56 (l. 196); `c14-v1-6` ¶ 11 (l. 114); `c12-v13-34` p. 318 n. 4 **En.** (l. 332); (+ `c6-v1-11` ¶ 21, l. 162, pre-interval) | ***accidia* → "sloth" / "accidie", against the work's "acedia"** (`c8-v11-21` ¶ 23 *In lecto autem accidia designatur* "acedia"; `c8-v26-33` p. 203 n. 11, Du Cange, "Acedia" ×3; the p. 288 sheet's item 24 claimed "acedia at every Bonaventure / Du Cange site", which `c6-v1-11` already belied). In the interval *accidia* is "sloth" twice and "accidie" once, while ***desidia* is "sloth" at all 10 of its regions** (`c11-v42-54` ¶¶ 89–93, `c14-v1-6` ¶ 7, …): `c14-v1-6` sets *desidia* (¶ 7) and *accidia* (¶ 11) in one chunk, both "sloth" — the builder's own item (140). The seven-vice list at `c11-v14-26` ¶ 56 (*fortitudini accidia*) is the capital vice, which English theology calls acedia. *pigritia*: "sluggishness" at 3 regions, "sloth" at `c9-v10-17` ¶ 22 (record only) | *accidia* "acedia" at all four: "to *fortitude* acedia"; "by which is understood *acedia*"; "of leisure and of acedia or sluggishness"; (pre-interval) "And *of acedia*" | **3** (+ **1** pre-interval) |

**Also noted, outside the gate's reach (no edit proposed).** Ps. 4:7 is "light" at Vol V `bon-hex-c3` ¶ 25, where the body
leans (*Sine isto lumine indito*), and at `bon-itin-c5` p. 308 n. 3: both pre-date the Vol V *lux / lumen* ruling
(2026-09-04) and belong to a Vol V errata list with the three *excessus* sites the p. 288 sheet recorded.

---

## THE DEFECTS D-1..D-7 (exact lines, current text, ⭐ fix)

### D-1. `c13-v1-9` ¶ 6 *defectus credulitatis* "lack of credulity" → "lack of belief" (1 line) — **CONFIRMED**

**Census, all 82 chunks:** *credulitas* 18 La body + 2 app (`c1-v26-38` ×3, `c4-v1-13`, `c4-v14-22` ×4, `c5-v1-11`,
`c7-v36-50` ×2, `c8-v22-25` ×4, `c8-v40-48` + p. 211 n. 5 ×2, `c13-v1-9`, `c13-v18-21` ¶ 45). English "belief" at every site
but one; **"credulity" once in the rendered region, here.** Ruling 55 is work-wide and was applied to three earlier sites in
exactly this good sense (`c1-v26-38` ¶¶ 67, 69). The builder's own reason (item (85): "*credulitas* in its good sense,
answered by John 3:15 *qui credit*") is the reason "belief" is right: ¶ 6's cure-verse *qui credit* "believeth" is the verb
of "belief", not of "credulity".

| file line | site | old | new |
|---|---|---|---|
| 146 | ¶ 6 **En** | `6. Seventhly, for lack of *credulity;*` | `6. Seventhly, for lack of *belief;*` |

Notes (l. 558, the "New here" list): `*credulitas* "credulity", in its good sense …` → amend in place, struck wording kept
(the ruling-63 practice); item (85) answered "conformed at the p. 381 gate (D-1)".

### D-2. `c12-v49-59` ¶ 84 Ps. 4:7 *lumen* "light" — **NOT A DEFECT under the corpus test; ⭐ no edit**

**The test** (repo CLAUDE.md, *mysterio Trinitatis* shakedown gate, Wilson 2026-09-06; carried into Lucam by ruling 27, its
unit fixed by ruling 50): *a received scriptural wording is exempt only where the verse is quoted AS A VERSE and no
surrounding body prose leans on the term.* The CLAUDE.md sentence the docket quotes ("Ps. 4:7 KEEPS 'lumen' at both its
attestations … do not re-raise it") is the **application** of that test to the two Vol V attestations, and gives its
reason: "at p. 55 n. 9 the note is the anchor for the body's own *lumen divini vultus* five words later, on which the whole
*Respondeo* turns." It decides those two sites; it does not exempt the verse from the test elsewhere.

**Applied here.** ¶ 84 adduces the verse for the *naturale iudicatorium* (*per quod dirigitur ad videndum et eligendum*)
between Ecclus. 31:18 and Isa. 46:8; **no *lumen* stands anywhere in the unit or the chunk** besides the verse (the
builder's Notes l. 530 say so, and the align census confirms: `c12-v49-59` ¶ 84 La 1 / En 0, no other *lumen* in the chunk).
The verse is quoted as a verse and nothing leans: **exempt, "light" stands.**

**Corpus record (Ps. 4:7 *lumen vultus tui*):** "lumen" `bon-qmt-q1-a1` p. 50 n. 2, `bon-qmt-q1-a2` p. 55 n. 9 (leans),
`bon-qpe-q4-a1` p. 180 n. 16 · "light" `bon-hex-c3` ¶ 25, `bon-hex-c12` ¶ 16, `bon-don-c8` p. 496 n. 7, `bon-itin-c5` p. 308
n. 3 (all pre-date the rule) · Lucam: this site only.

| alternative | cost |
|---|---|
| **(a) No edit; record the test's verdict in `c12-v49-59`'s Notes (item (71) answered)** | **0 lines** |
| (b) "The lumen of thy countenance" + a `tr-lumen` | 2 lines; makes the CLAUDE.md application a verse-wide exemption from its own test, against ruling 27 ("no famous-verse exception", in either direction) |

**⭐ (a).** If Wilson prefers the verse fixed at "lumen" corpus-wide, that is a new ruling (and reopens the four Vol V
"light" sites); it should be made as such, not as a D-item.

### D-3. *lumen* inside a Father's quotation in the apparatus — **CONFIRMED at two sites; the third is exempt (F9)** (4 lines)

**Ruling 50** (scope sentence): "the *lux* / *lumen* rule reaches the editors' quotations in the apparatus (the Vol VI practice;
`c4-v38-44` p. 110 n. 8, `c6-v32-38` p. 159 n. 7)", while "Rom. 2:19 'a light' with no note stands (the test as written)".
So a **Father's** *lumen* in a note takes "lumen"; a **verse** quoted as a verse in a note keeps the Douay unless the note's
own sentence leans. In the interval the apparatus holds seven *lumen*: the Gloss at p. 301 n. 9 ×2 (`c11-v33-41`) and Isidore at p. 324 n. 7
×2 (`c12-v35-48`), already "lumen", and the three docket sites:

| site | what it is | as built | test | ⭐ |
|---|---|---|---|---|
| `c12-v8-12` p. 316 n. 2 **En.** (l. 221) | Augustine, Ep. 137 c. 5 n. 17: *quoniam veritas lumenque animae rationalis nonnisi Deus est* | "since the truth and the light of the rational soul is none but God" | a Father's prose: ruling 50 reaches it; no *lux* in the note | "the truth and the lumen[^tr-lumen] of the rational soul" |
| `c14-v16-24` p. 373 n. 12 **En.** (l. 344) | Gregory, Hom. 36: *Caeci vero sunt qui nullum ingenii lumen habent* | "who have no light of wit" | a Father's prose: ruling 50 reaches it | "who have no lumen[^tr-lumen] of wit" |
| `c13-v1-9` p. 339 n. 5 **En.** (l. 384) | the Gloss: *de quibus dictum est [Isai. 9, 2.]: Qui sedebant sub umbra mortis, lumen ortum est eis* | "To them that sat in the shadow of death, light is risen" | a verse quoted as a verse; the Gloss leans on *umbra mortis*, not on *lumen*: **exempt** (Rom. 2:19 shape) | **no edit** |

Neither `c12-v8-12` nor `c14-v16-24` carries a `tr-lumen` (both chunks' Notes say none was placed: `c12-v8-12` l. 274
"not `tr-lumen`'s reach" is the claim ruling 50 answers). Each takes one, at its one site, in the `c4-v38-44` form ("Here
the one *lumen* of the pericope stands not in Bonaventure's prose but in the editors' quotation of …").

| chunk | lines | text |
|---|---|---|
| `c12-v8-12` | l. 221 + new `[^tr-lumen]` def | 2 |
| `c14-v16-24` | l. 344 + new `[^tr-lumen]` def | 2 |

**⭐ Apply at the two Fathers' sites (4 lines); record p. 339 n. 5 as exempt in `c13-v1-9`'s Notes (item (87) answered).**

### D-4. `c11-v14-26` ¶ 36 *lucerna* "candle" → "lamp" (1 line) — **CONFIRMED**

**Census, all 82:** *lucerna* 50 La body + 6 app; English "lamp(s)" at every site but one. **"candle" occurs once in the
rendered region:** ¶ 36's forward reference to the Luke 11:33 lemma (*ibi: Nemo lucernam accendit*), which `c11-v33-41`
¶¶ 70–71 render "*No man lighteth a lamp*". The Douay reads "candle" at Luke 11:33, Matt. 5:15 and Luke 8:16 alike; Lucam
adjusts all three to "lamp" because Bonaventure defines the word (*Lucerna dicitur vehiculum luminis sive vas luminis
contentivum*, ¶ 71). A forward reference is an echo of the lemma and follows it (the p. 288 D-2 precedent, ruling 63:
`c9-v1-9` "appointed" → "designated").

| file line | site | old | new |
|---|---|---|---|
| 132 | ¶ 36 **En** | `at: *No man lighteth a candle.*` | `at: *No man lighteth a lamp.*` |

**⭐ Apply (1 line); Notes item (17) answered.** (Not a ruling-28 split: the same verse in the same work with nothing leaning
at ¶ 36.)

### D-5. *dilectio excessiva* "transporting dilection" (`c13-v18-21` ¶ 46, l. 136) — **a ruling on the ADJECTIVE, reaching all four *excessivus* sites (F10 = passes N-4)** — 0 lines on ⭐

**The sentence.** *Nam, sicut dicit Dionysius, tota mystica theologia, « quae scilicet in mysterio abscondita est », ipsa tota
consistit in dilectione excessiva secundum triplicem vim hierarchicam: purgativam, illuminativam et perfectivam.* p. 349
n. 9 sends the reader to *De caelesti hierarchia* c. 7 § 3, *De mystica theologia* c. 1 § 1, and **Bonaventure's own
Hexaëmeron coll. 2 n. 28 ff.**, i.e. the Itinerarium-register passage on the mind's going-out. This is the mental /
contemplative sense of ruling 67's row.

**Census, *excessivus*, rendered region, all 82 Lucam chunks: 4 sites in 3 chunks** (English "excessive" elsewhere — `c10-v4-16` ¶ 24, `c13-v22-30` ×2, `c13-v31-35` ¶ 74, `c14-v16-24` ¶ 47 — renders other Latin, not *excessivus*):

| site | Latin | sense | as built |
|---|---|---|---|
| `c9-v32-36` ¶ 61 (l. 95) + p. 236 n. 7 **En.** (l. 200) | Peter's *excessivum desiderium, quod consuevit esse in contemplantibus … prae nimietate desiderii*; *De desiderio excessivo in contemplativis* (Richard) | glossed by *nimietas* (over-measure), in contemplatives | "excessive desire" ×2 |
| `c12-v49-59` ¶ 72 (l. 108) | charity *elevat per adhaerentiam excessivam* (Cant. 8:5 *Quae est ista, quae ascendit de deserto*) | ambiguous: charity's raising (the ascent of Cant. 8:5) | "an excessive adherence" |
| **`c13-v18-21` ¶ 46 (l. 136)** | *dilectio excessiva* of Dionysian mystical theology | **mental / contemplative** | **"transporting dilection"** |

**Corpus precedents (Vol V):** "transporting" for the contemplative adjective — `bon-serm-tract` *excessivam contemplationem*
"transporting contemplation", *contemplationis excessiva satietas* "the transporting satiety"; `bon-hex-c20` Summarium "the
transporting or ecstatic refulgence"; "excessive love" `bon-brev-p6-c9` (*per excessivum amorem … transferantur*), "the
surpassing love" `bon-brev-prol` (*excessivum amorem beatissimae Trinitatis*); "excessive" for every measure sense.

| alternative | sites changed | cost |
|---|---|---|
| **(a) The adjective follows the noun's sense (ruling 67): "transporting" where the going-out is the mind's (¶ 46, mystical theology); "excessive" where it is measure. Keep all four as built**; ¶ 72 *adhaerentiam excessivam* stays "excessive" (charity's adherence beyond measure; the builder's reading); ¶ 61's contemplatives' desire stays "excessive" because Bonaventure himself glosses it *prae nimietate desiderii* | 0 | **0 lines.** One clause into ruling 32's *excessus* row (below) |
| (b) (a), and also ¶ 72 → "a transporting adherence" (reading Cant. 8:5's ascent as the mind's) | 1 | 1 line (`c12-v49-59` l. 108); the reading is defensible but not forced: the paragraph's four members (*trahit, dilatat, elevat, inclinat*) are charity's operations, not contemplation's |
| (c) One English for the adjective: "excessive dilection" at ¶ 46 | 1 | 1 line; English "excessive love" is *too much* love, and Dionysius' definition of mystical theology would then say so |
| (d) "surpassing dilection" (the Brevil. prol. precedent) | 1 | 1 line; drops the *excess-* root, so the reader loses that ¶ 46 names the Itinerarium's *excessus* |
| (e) "ecstatic dilection" | 1 | blocked: the Itinerarium register gives "ecstatic" to *ecstaticus* (c4 § 3, *ecstaticus amor*) |

**⭐ (a).** Write into ruling 32's *excessus* row: "the adjective *excessivus* follows the noun's sense: mental /
contemplative (mystical theology, *excessiva contemplatio*) 'transporting' (`c13-v18-21` ¶ 46; Vol V *Sermones*); measure
'excessive', including a desire Bonaventure glosses by *nimietas* (`c9-v32-36` ¶ 61)." Record (b) as the one site where
the reading could go either way. **This one needs Wilson's own call (a sense judgment, not a census).**

### D-6. p. 295 n. 15 *supra pag. 297, nota 7* → the ledger's `fn-p297-7` — **CONFIRMED; cause located (F11); tool side only, 0 text lines**

**Ledger record** (`index/citations.tsv`): `bon-luc-c11-v14-26 · apparatus:p295-15 · crossref/page · supra pag. 297, nota 7 →
bon-luc-c11-v27-32 · chunk · anchor fn-p297-7`. p. 297 n. 7 is *Vers. 5. — Duo seqq. loci sunt Ps. 131, 11. et Rom. 9, 5.*
(Gen. 15:5 in ¶ 63, the woman from the crowd): nothing of Jerome. The note means **p. 294 n. 7** (same chunk, l. 524:
*… II. Comment. in Matth. 12, 43. autem per loca arida intelligit gentes*). *supra* from p. 295 cannot point at p. 297.

**Cause.** `scan_page()` (`tools/build-citations.py`, the `supra|infra … pag. N, nota M` pattern at l. ~794) records `rel`
but never compares the page with the citing page; the page + note branch then resolves any existing note. **No chunk text
changes** (ruling 57: Quaracchi's slip is transcribed as printed).

| alternative | cost |
|---|---|
| **(a) A `CROSSREF_SLIPS` row** `("bon-luc-c11-v14-26", "apparatus:p295-15", "supra pag. 297, nota 7", "printed slip — *supra* from p. 295; the locus is p. 294 n. 7 (Jerome on Matt. 12:43); filed as printed, not retargeted")`, the ruling-37 T3 / T4 shape (record kept, verdict → `unresolvable`, listed in the QA slips table) **+ a report-only direction screen** (`supra pag. N` with N > citing page, `infra` with N < citing page, same volume) printed in the QA report | 0 text; tool job J-12 (§ T). The screen finds **4** today (F11); the three outside Vol VII are reported, not fixed here |
| (b) Retarget to `fn-p294-7` | refused: ruling 57 / 37 never emend a printed slip in the ledger |
| (c) Leave it | a wrong edge stays live in the backlink index |

**⭐ (a), as J-12 of the queued tool job.** Item 19's "r.57 C2 annotation owed" is exactly the `CROSSREF_SLIPS` row
(`PRINTED_SLIPS` is for scripture records; this is a crossref).

### D-7. `c14-v12-15` ¶ 26 *spiritualem eruditionem* "spiritual teaching" → "spiritual erudition" (1 line) — **CONFIRMED; widened by F2**

**Census, all 82:** *eruditio* 36 La; "erudition" 35; **the one exception is this line.** Ruling 17 (carried as ruling 32's
row): *eruditio* → "erudition" everywhere, kept off *instructio* "instruction" — and ¶ 34 of the same chunk has *instructio
doctrinae* "the instruction of doctrine", so the two must not meet in "teaching".

| file line | site | old | new |
|---|---|---|---|
| 70 | ¶ 26 **En** | `he might repay spiritual teaching,` | `he might repay spiritual erudition,` |

**The docket's rider is wrong:** "*erudiens* 'teaching' (the participle) is the verb and stands." Ruling 32's row gives the
verb *erudire* in body prose **"school"** ("we are schooled"); the participle is the verb. That is F2: ¶ 26 *exhortationem
erudientem* (l. 68) and ¶ 27 (l. 72) "the exhortation teaching" → "the exhortation schooling", with `c14-v25-35`'s three
lines. Notes: `c14-v12-15` l. 335 and l. 341 (item (156)) and `c14-v25-35` l. 549 / l. 565 ("*erudire* 'instruct' (the house
verb)") amended in place, struck wording kept.

**⭐ Apply D-7 (1 line) with F2 (5 interval lines; 2 pre-interval at Wilson's option, § F2 below).**

#### F2 exact edits

| chunk / line | site | old | new |
|---|---|---|---|
| `c14-v12-15` l. 68 | ¶ 26 | `the exhortation teaching*` | `the exhortation schooling*` |
| `c14-v12-15` l. 72 | ¶ 27 | `*the exhortation teaching*` | `*the exhortation schooling*` |
| `c14-v25-35` l. 11 | `title_en` | `Third the multitudes following are instructed, of which two things` | `Third the multitudes following are schooled, of which two things` |
| `c14-v25-35` l. 96 | `####` **En** | `#### Third the multitudes following are instructed, of which two things.` | `#### Third the multitudes following are schooled, of which two things.` |
| `c14-v25-35` l. 98 | ¶ 51 | `and instructed the guests at table` · `In the first he instructs *those` · `Now instructing through` | `and schooled the guests at table` · `In the first he schools *those` · `Now schooling through` |
| `c9-v10-17` l. 82 (pre-interval) | ¶ 16 *ut Dominum erudirent* | `not that they might teach the Lord` | `not that they might school the Lord` |
| `c9-v32-36` l. 105 (pre-interval) | ¶ 64 *Ex hoc erudiuntur contemplativi* | `this contemplatives are taught that` | `this contemplatives are schooled that` |

⚠ `title_en` feeds the site's breadcrumb / content build; it regenerates at the next `build-content.mjs`. ¶ 51's *informat
comitantes* "forms those who accompany him" (ruling 12) is untouched. **The two pre-interval lines passed the p. 288 gate
unseen; ⭐ include them** (the p. 288 F1 precedent fixed two pre-interval *dilectio* sites the same way). "school the Lord"
is stiff, and is what the ruling says; the alternative is to record ¶ 16 as a sense exception (*erudire* = "inform", the
apostles telling Christ what he already knew), at Wilson's word.

---

## THE OTHER FOUND FIXES (exact edits)

### F1. "Holy Ghost" → "Holy Spirit" (ruling 17) — 12 interval lines + 2 pre-interval

| chunk | lines (occurrences) |
|---|---|
| `c12-v8-12` | 69 (1) · 77 (3) · 79 (2) · 81 (1) · 93 (1) · 95 (1) · 213 (2, p. 315 n. 12 **En.**) |
| `c12-v13-34` | 155 (1) · 203 (1) |
| `c13-v18-21` | 106 (1) · 124 (1) |
| `c13-v31-35` | 92 (1) |
| `c10-v17-24` (pre-interval) | 101 (3) · 108 (1) |

Literal replace on these lines only (⚠ BSD `sed -i` trap: Python or `~/bin/sedi`), then `grep -c 'Holy Ghost'` over the five
files' rendered regions → 0 (`c12-v8-12` l. 233 is in `## Notes` and carries the phrase in a description; amend it in place).
Ruling 17 names "Douay quotations included", so the Luke 12:10 lemma and I Cor. 12:3 change with the rest.
**⭐ Apply all 14 lines.**

### F3. *benignitas* "benignity" → "kindness" (ruling 45) — 3 lines

| chunk / line | site | old | new |
|---|---|---|---|
| `c13-v1-9` l. 176 | ¶ 12, Rom. 2:4 | `the benignity of God leadeth thee to penance` | `the kindness of God leadeth thee to penance` |
| `c14-v16-24` l. 93 | ¶ 37 | `the highest liberality and benignity` | `the highest liberality and kindness` |
| `c14-v25-35` l. 102 | ¶ 52 | `through *benignity;*` | `through *kindness;*` |

**⭐ Apply (3 lines).** (Rom. 2:4 is the Douay's own "benignity"; ruling 45 adjusts a Douay verse to the house word, as at
Ps. 64:12.)

### F4. `c12-v1-7` *lumen* in the prose (rulings 32, 50) — 3 lines

| line | site | old | new |
|---|---|---|---|
| 94 | ¶ 2 | `and darkness is driven out by light.` | `and darkness is driven out by lumen[^tr-lumen].` |
| 104 | ¶ 6 | `*… shall be spoken in the light.*` · `For the light of the sun makes other things manifest to sight.` | `*… shall be spoken in the lumen.*` · `For the lumen of the sun makes other things manifest to sight.` |
| new | `[^tr-lumen]` | — | the `c12-v35-48` form: *lux* "light" / *lumen* "lumen" except a verse quoted as a verse with nothing leaning; here ¶ 2 *tenebra per lumen expellitur* and ¶ 6 *Lumen enim solis visui cetera manifestat*, which glosses the lemma's *in lumine dicentur*, so the lemma follows (the Matt. 10:27 shape, `c8-v11-21` ¶ 24) |

| alternative | cost |
|---|---|
| **(a) All three** | **3 lines** |
| (b) ¶ 2 and ¶ 6's prose only; the lemma keeps "in the light" | 3 lines; the gloss then names a word the lemma does not show (ruling 20's point) |

**⭐ (a).** Item 7's 12:3 record ("spoken", the Douay's "published" adjusted) is unaffected.

### F5. *redarguere* "rebukes" → "convicts" (ruling 56) — 2 lines

| line | site | old | new |
|---|---|---|---|
| `c11-v42-54` l. 99 | ¶ 87, the Gloss | `« He rebukes arrogance, because they seek the primacies »` | `« He convicts arrogance, because they seek the primacies »` |
| `c11-v42-54` l. 182 | p. 305 n. 6 **En.** | `« He rebukes arrogance, because they seek the primacies »` | `« He convicts arrogance, because they seek the primacies »` |

**⭐ Apply (2 lines).**

### F6 and F7 — 1 line each

| line | site | old | new |
|---|---|---|---|
| `c14-v12-15` l. 76 | ¶ 28, Prov. 23:21 | `and that give clubs shall be consumed` | `and that club together shall be consumed` |
| `c14-v7-11` l. 328 | p. 365 n. 15 **En.** | `effects wonderful operations` | `effects marvellous operations` |

**⭐ Apply both (2 lines).**

---

## D. REGISTER QUESTIONS FOR WILSON (docket items 10–18)

### 11. ⭐ THE *pietas* REVIEW (ruling 70; this gate's named task)

**Question.** Rulings 12 and 31 hold *pietas* → "piety" everywhere, human and divine, with `tr-pietas` at the first site of any
chunk where the *pietas* is God's; ruling 51 conformed human *pietas* inside quotations; ruling 70 carried the review here.
Keep the rule as it stands, now that Cap. XV is about to open on it?

**Census.** *pietas / pius / pie* (positive word), rendered region: **interval 22 regions, "piety / pious / piously" at all
22**; all 82 chunks La 75 body + 22 app, every one "piety / pious / piously" (the English count runs higher only by the
`tr-pietas` anchors). *impietas / impius* 24 interval regions: "impiety / impious" in prose, "wicked / ungodly" by the
nearest Douay word in verses (ruling 51's record; the rule binds the positive word only).

| class | interval sites | as built |
|---|---|---|
| **human, prose** | `c11-v33-41` ¶ 78 *praetendebat pietatem* "a pretence of piety", ¶ 79 *pie … impie* "piously … impiously"; `c11-v42-54` ¶ 93 *praetendentes pietatem … impietatem*; `c12-v13-34` ¶ 31 *operibus pietatis*, p. 322 n. 6 *via pietatis*; `c13-v10-17` ¶ 29 *simulatio pietatis*; `c14-v12-15` ¶ 28 *pietatis*, ¶ 30 *commendationem pietatis fraternae* ×2, ¶ 31 *operibus pietatis*; `c14-v25-35` p. 380 n. 4 *piorum affectuum* | "piety", "pious", no note |
| **human, inside a verse** | Titus 2:12 *pie vivamus* "piously" (`c12-v35-48` ¶ 55; echoed in Bernard, `c14-v7-11` ¶ 20); II Tim. 3:5 *Speciem pietatis* "an appearance of piety" (`c13-v10-17` ¶ 29, ruling 51's F4 precedent); II Pet. 2:9 *pios* "the pious" (`c14-v16-24` ¶ 50); I Tim. 4:8 "Piety is profitable" (`c11-v33-41` ¶ 82, `c14-v12-15` ¶ 29) | Douay "godly / godliness" adjusted (ruling 51) |
| **the gift** | `c11-v14-26` ¶ 56 (the seven gifts against the seven vices), `c14-v25-35` ¶ 57 *turris pietatis … pietas oritur ex consideratione passionis* | "piety" (the *septem donis* ruling) |
| **divine, `tr-pietas`** | `c12-v35-48` ¶ 57 *pius Dominus* (Bede's Gloss); `c13-v10-17` ¶ 25 *oculo pietatis*; `c13-v31-35` ¶ 74 *superabundantiam pietatis* + the hen's *sua pietate* (and p. 357 n. 4) | "piety / pious" + `tr-pietas` at each chunk's first site ✓ (3 / 3) |

**Corpus.** Titus 2:12: Vol V `bon-don-c1` and Vol VI `bon-cioan-c8` keep "godly"; `bon-don-c3` and Lucam ×2 "piously" — a
cross-volume split; Lucam's ruling 51 governs Lucam. I Tim. 4:8 "Piety" is the *septem donis* gate's own adjustment.

**Decisive sentence: Cap. XV ¶ 1 (p. 381, already standing on the plate, next interval).** *… in hac parte confutat eorum
impietatem remurmurantium contra clementiam in operibus pietatis. … In quarum prima praemittitur expressio impietatis
Iudaicae. In secunda subditur manifestatio pietatis divinae … In tertia vero adiungitur commendatio et persuasio pietatis
humanae.* The whole of cc. 15–16 is divided by **one word in three forms**: *impietas* / *pietas divina* / *pietas humana*.
Only one English root carries the divisio.

| alternative | cost |
|---|---|
| **(a) Ratify the rule as it stands: "piety" human and divine, `tr-pietas` at the first divine site of each chunk; *impietas* "impiety" in prose** | **0 lines.** Cap. XV ¶ 1 then reads "impiety … the manifestation of divine piety … the commendation and persuasion of human piety" |
| (b) Divine *pietas* "pity" (or "loving-kindness") | the three `tr-pietas` sites + every divine site in cc. 15–16; ¶ 1's divisio splits across two English roots, and "pity" collides with *miseratio* / *compassio*, "loving-kindness" with *benignitas* "kindness" (ruling 45) |
| (c) Human *pietas* in verses back to the Douay "godly" | 4–5 lines; reverses ruling 51 |

**⭐ (a).** Close ruling 70's carried review: the rule HOLDS for cc. 15–16, and `tr-pietas` in the Cap. XV chunks names the
*impietas / pietas divina / pietas humana* divisio at its first site. Record the Titus 2:12 cross-volume split.

### 10. *anima* "soul" against the Douay's "life" (and the other ruling-28 splits)

**Census, interval:** *anima* (noun) 117 La regions; "soul" at 110. The 7 others are the Douay's "life" where nothing leans
(Gen. 9:5 `c11-v42-54` ¶ 96; I John 3:16 `c12-v49-59` ¶ 72; **Luke 14:26 `c12-v49-59` ¶ 75**; John 10:18 `c13-v31-35` ¶ 67)
and three work titles in notes (*de Spiritu et anima*, *de Quantitate animae*). **"soul" against the Douay's "life"** stands
at: Luke 12:22, 12:23 (`c12-v13-34` ¶¶ 33–34, ¶ 32's argument *dat animam et corpus*); John 12:25 (`c12-v13-34` ¶ 29,
glossed *id est animalitati* "that is, to the animal part"; `c14-v25-35` ¶ 53); Luke 14:26 lemma (`c14-v25-35` ¶ 52, ¶ 53's
*odium animae suae … quantum ad carnalitatem* and Gregory's *animam nostram odimus*). Each leans; ruling 20 licenses each.
Pre-interval: Luke 9:24 and John 12:25 "soul" at `c9-v18-27` (ratified in the p. 288 batch C). John 10:11 "life" ×3 (Douay;
nothing leans). **F12(b): Luke 14:26 is now "life" (¶ 75, adduced) and "soul" (the lemma), a cross-chunk ruling-28 split.**

**⭐ Ratify the *anima* batch; record F12(b) in `c12-v49-59`'s and `c14-v25-35`'s Notes.** The other item-10 splits (*ubera*,
*sacculus*, *monumentum / sepulcrum*, *nuptiae*, *convivium*, *supplicium*, *remittetur*, *dispensator*, Mark 3:2 / Luke 14:3,
Matt. 4:4, Ecclus. 1:39, Rom. 1:21) are each ruling 20 or ruling 28 working site by site: **⭐ ratify as a batch, 0 lines**
(F6 above is the one *unlicensed* split the sheet found).

### 12. *lumen* in the apparatus and at Ps. 4:7 — decided by D-2, D-3, F4 above

Item [18] (`tr-lumen` reaching ¶ 75's lemma and p. 301 n. 9; Ps. 118:105 "a light to my paths" kept — a verse, nothing leans
on *lumen* in ¶ 72, which leans on *lucerna*) and item [57] (Isidore p. 324 n. 7) **ratify as built.** Job 24:13 *lumini*
"the light" (`c13-v10-17` ¶ 33) [99]: a verse, nothing leans: **ratify.** After D-3 + F4 the interval holds no *lumen* of
Bonaventure's or a Father's prose outside `tr-lumen`'s reach. **⭐ Ratify; 0 further lines.**

### 13. *lucerna* — D-4 (1 line). Matt. 5:15 "lamp" with nothing leaning (`c14-v25-35` ¶ 59) [174]: the work's house rendering of the lamp verses (Luke 8:16, 11:33, Matt. 5:15 all "lamp"); **⭐ ratify.**

### 14. *excessus* — D-5 above. p. 379 n. 4 Aristotle's *per excessum et defectum* "excess" [179] is ruling 67's measure sense: **⭐ ratify.**

### 15. *intellectus / intelligentia / notitia / cognitio / scientia*

Interval: *notitia* 18, *scientia* 27, *cognitio* 4 La. Where two stand in one region: `c13-v18-21` ¶ 40 Col. 1:10 *crescentes
in scientia Dei* (Douay "knowledge") + *Haec autem notitia* "But this knowledge" — the anaphor needs the shared English;
`c13-v22-30` ¶ 58 *cognitionis* ×2 + *negatio notitiae*, all "knowledge" (the F10 rule offered at p. 288 would give
*cognitio* "cognition" here; ruling 70 took no conformation, so this is a record, not a defect). *intelligentia* 17 La:
"intelligence" where ruling 17 binds; the others are Douay verses (Job 32:8, Phil. 4:7) and three idioms (`c12-v49-59` ¶ 81
*manuducitur ad intelligentiam illorum* "to the understanding of those things", a chunk with no *intellectus*, so ruling 17's
condition does not hold; `c14-v7-11` ¶ 20 Bernard's *ut ad intelligentiam loquar*; p. 309 n. 4 Ambrose). Items [112], [170],
[178] (*varios intellectus*, *hic ultimus intellectus*, a parable's *intelligentia* ×6) follow ruling 17. *desidia* /
*accidia* both "sloth" [140]: **a defect of the same kind, not a house-word choice — see F13.** **⭐ Ratify the rest,
recording `c13-v22-30` ¶ 58; [140] goes by F13.**

### 16. *vacare / quies* — **⭐ ratify as built.** Matt. 12:44 *vacantem* "free" + `tr-vacare` (ruling 32 *vacare a*) [5]; ¶ 70 *quies animarum* "the rest of souls" (ruling 32: *quies* "rest") [133]; *quietari* "be set at quiet" kept off *requiescere* "rest" [109]. Interval census: *vaca-* 4 regions, two "free", two Douay verses (Prov. 23:21 *vacantes potibus* "give themselves to drinking"); *quies / requies* 7, "rest" 7.

### 17. Single house-word decisions — **⭐ ratify as a batch, 0 lines**, with one record

[7] *simulatio* "dissembling" (25 / 25 in the interval) · *redarguere* "convict" (see F5 for the two misses) · [101, 141]
*virtuositas* "powerfulness" · [102] *mirificus*, *curatio* "cure" (interval: *curare* 22 regions, every prose site "cure /
care"; *sanare* 10 / 10 "heal") · [122] ruling 64 in a Father's prose · [73] Cant. 8:6 "Dilection is strong as death" · [132]
*Opportunitas* · [96] *rationabile / rationale* · [171] *excusatio vocatorum* · [111] *infidelis / credulitas* (D-1).
**Record [121]:** `c13-v22-30` ¶ 56 *serotinam poenitudinem* "late repentance" stands beside Wis. 5:3 *poenitentiam agentes*
"repenting" and Heb. 12:17 *locum poenitentiae* "place of repentance" (both the Douay's; the verses illustrate the late
*poenitudo*, nothing leans on *poenitentia*): "repentance" there names two Latin words in one paragraph. Ruling 20 permits
it; the reader of ruling 32's *poenitentia* "penance" row should know it.

### 18. New house words — **⭐ ratify as a batch**, with D-7 and F2 applied (*eruditio*, *erudire*) and F3, F5 applied.

---

## A–C, E–H. BATCHES (ratify)

**A. Boundaries, manifest, structure (items 1–5).** Not re-derived from the plates (none read). Docket statements checked
against the files: last ¶ XI 102, XII 88, XIII 76, XIV 69 match the stage-4 notes and the ruling file's § MANIFEST STAGE 4
(ll. 721–723); `c14-v25-35` frontmatter `paragraphs: "51-69"`. **⭐ Ratify 1–5 as recorded (ruling 36); 0 lines.**

**B. Corrigenda (item 6), seven entries pp. 294–361** — the stage-4 list (pp. 294, 300, 320, 333, 343, 346, 361) is the
docket's. **⭐ Ratify as applied.** `c11-v14-26`'s `tr-corrigenda` (p. 294 n. 13, *cum Vulgata* deleted) checked: ruling 23's
shape. 0 lines.

**C. Ruling-20 adjustments and Douay base (items 7–9).** **⭐ Ratify as a batch**, with F12(a) recorded (12:20 "soul" is the
Douay's) and F4's Luke 12:3 lemma "lumen" applied. 0 further lines.

**E. Quaracchi citation slips (item 19).** **⭐ Ratify as transcribed (r.57 class; ruling 36); p. 295 n. 15's ledger side is
D-6 / J-12.** p. 366 n. 4 (Quaracchi's own substitution *caritatem divinam* from H) is the editors' text: record. 0 lines.

**F. `[so printed]`, `[?]` (items 20–22).** The two `[so printed]` (*eautelam*, *rimediando*) **⭐ ratify.** Item 21, ¶ 10
*quinque ova*: **⭐ no mark.** The sentence reads as Bonaventure's market analogy (*sicut videmus, cum quinque ova venduntur
pro uno denario, duo dantur pro obolo*: small wares sold cheaper by the lot, then *Parvi igitur pretii est passer*), not as
a misprint we caught; `[so printed]` is for misprints only (ruling 36). Zero new `[?]`; the one live `[?]` stays open
(rulings 59, 73).

**G. Readings as printed / plate evidence (items 23–26).** Guillemets and points as recorded; **⭐ ratify, supply nothing**
(the p. 188 / p. 288 practice, rulings 36, 60, 74). Codex H read for `II`: ratify.

**H. Collection change (item 27).** **⭐ Bank; no ruling.**

---

## T. TOOL ITEMS (not for ruling): this interval's sites folded into ruling 76's queued job

**State:** ruling 76's job J-1..J-11 **has not run**. Ledger spot-checks (`index/citations.tsv`), each as the docket says:
T-b — p. 342 n. 11 *loc. cit.* → antecedent *supra pag. 340, nota 7* (`chunk`), p. 342 n. 12 → Ps. 57:9, p. 348 n. 2 → I Pet.
5:8, p. 348 n. 5 → I Cor. 10:17, p. 370 n. 13 → Apoc. 22:17, **p. 378 n. 6 *ex Gregor., loc. cit.* → Matt. 5:14** (all
`anaphor->…`, `ibid_resolved yes`) ✓; T-c — p. 320 n. 3 *pag. 860* → `tom7:p860 forward` ✓; T-d — p. 360 n. 3 *supra pag
238, nota 12*: no record ✓; T-e — p. 373 n. 5: the record is `supra pag. 261` → `page-multi` (`c10-v4-16+c10-v17-24`), the
accusative *notam 11* not captured ✓ (F12(d)).

**⭐ Add to the one job, no new job:**

| merged item | this interval's sites | expected effect |
|---|---|---|
| **J-1** (wrong *ibid. / loc. cit.*) | T-b: p. 342 nn. 11, 12; p. 348 nn. 2, 5; p. 370 n. 13; p. 378 n. 6 | 6 wrong edges removed; anaphora unresolved **+6** unless the named work then resolves |
| **J-2** (misreads) | T-c: p. 320 n. 3 (Buffon's *tom. 25. pag. 860*) | 1 false `forward` removed |
| **J-4 / J-5** (accusative *notam*; `page-multi` by note) | T-e: p. 373 n. 5 *supra pag. 261, notam 11* | `page-multi` → `chunk` |
| **J-6** (no record) | T-d: p. 360 n. 3 *supra pag 238* (no point after *pag*) | +1 record |
| **J-9** (count, classify) | T-a: p. 292 n. 4 · p. 300 n. 8 · p. 312 nn. 3, 5 · p. 324 n. 12 · p. 325 n. 14 · p. 334 n. 9 · p. 339 n. 14 · p. 348 n. 11 · p. 371 n. 6 · p. 374 n. 6 · p. 375 n. 14 | re-measure (391 today; 379 at ruling 76) |
| **J-11** (in-work *c. N. n. M*; deferred) | T-f: p. 373 n. 6, p. 376 n. 5, p. 380 n. 13, p. 381 n. 6 | count only |
| **J-12 (new)** | **D-6 / T-g**: the `CROSSREF_SLIPS` row for p. 295 n. 15, **+ a report-only direction screen** (`supra` page > citing page, `infra` page < citing page) | 1 wrong `chunk` edge → `unresolvable` with reason; the screen reports 4 (F11), the 3 outside Vol VII for a later look |

Same discipline as ruling 76: report → fix → report, before / after per site; `tools/build-citations.py` only, then
`build-citations.py` → `build-index-json.py`; no chunk file.

---

## ▶ DOCKET SUMMARY (one word each: "Approve" takes the ⭐)

| # | items | ⭐ recommendation | lines | kind |
|---|---|---|---|---|
| **D-1** | `c13-v1-9` ¶ 6 "credulity" | **Apply** ("belief") | **1** | fix |
| D-2 | Ps. 4:7 "light" (`c12-v49-59` ¶ 84) | **No edit** — exempt under the test (F8) | 0 | record |
| **D-3** | *lumen* in Fathers' notes | **Apply at p. 316 n. 2 and p. 373 n. 12 + `tr-lumen` in each chunk**; p. 339 n. 5 exempt (F9) | **4** | fix |
| **D-4** | ¶ 36 "candle" | **Apply** ("lamp") | **1** | fix |
| **D-5** | *excessivus* (4 sites, F10 = N-4) | **Keep as built; write the adjective clause into ruling 32's *excessus* row** | 0 | **rule** |
| D-6 | p. 295 n. 15 mis-link | **J-12**: `CROSSREF_SLIPS` row + direction screen (F11) | 0 text | tool |
| **D-7** | ¶ 26 "spiritual teaching" | **Apply** ("erudition") | **1** | fix |
| **F1** | "Holy Ghost" (ruling 17) | **Apply** | **12** (+2 pre-interval) | fix |
| **F2** | *erudire* "teach / instruct" (ruling 32) | **Apply** | **5** (+2 pre-interval) | fix |
| **F3** | *benignitas* "benignity" (ruling 45) = N-1 | **Apply** | **3** | fix |
| **F4** | `c12-v1-7` prose *lumen* "light" = N-2 | **Apply (a)**, lemma included, + `tr-lumen` | **3** | fix |
| **F5** | *redarguere* "rebukes" (ruling 56) = N-3 | **Apply** | **2** | fix |
| **F6** | Prov. 23:21 "give clubs" | **Apply** (Douay) | **1** | fix |
| **F7** | p. 365 n. 15 "wonderful" | **Apply** ("marvellous") | **1** | fix |
| **F13** | *accidia* "sloth" / "accidie" | **Apply** ("acedia") | **3** (+1 pre-interval) | fix |
| F8–F12 | records | Record in the gate record / Notes | doc | doc |
| **11** | **the *pietas* review** | **Ratify the rule (a); close ruling 70's review; `tr-pietas` names Cap. XV ¶ 1's divisio** | 0 | **rule** |
| 10 | *anima* "soul" + the other splits | **Ratify**; record F12(b) | 0 | ratify |
| 12–14 | *lumen*, *lucerna*, *excessus* rest | **Ratify** (after D-2..D-5, F4) | 0 | ratify |
| 15 | *intellectus … scientia* | **Ratify**; record `c13-v22-30` ¶ 58; [140] by F13 | 0 | ratify |
| 16–18 | *vacare / quies*; house words; new words | **Ratify as batches**; record [121] (*poenitudo* / Douay "repentance") | 0 | batch |
| A–C | boundaries, corrigenda, ruling-20 batch | **Ratify as batches** | 0 | batch |
| E | citation slips | **Ratify as transcribed** (p. 295 n. 15 → J-12) | 0 | batch |
| F | `[so printed]`; *quinque ova* | **Ratify; no mark at *quinque ova*** | 0 | batch |
| G | guillemets, points, codex H | **Ratify as recorded; supply nothing** | 0 | batch |
| H | collection change | **Bank** | 0 | bank |
| T | T-a..T-g | **Fold into ruling 76's job; add J-12** | 0 text | tool |

**If every ⭐ is taken: 37 English lines in the interval (D-1 1, D-3 4, D-4 1, D-7 1, F1 12, F2 5, F3 3, F4 3, F5 2, F6 1,
F7 1, F13 3) across 13 interval chunks, + 5 pre-interval lines in 4 earlier chunks (F1 `c10-v17-24` ×2, F2 `c9-v10-17`,
`c9-v32-36`, F13 `c6-v1-11`) = 42 lines; three of the 37 are new `tr-lumen` definitions and one is a frontmatter
`title_en`. Notes records / amendments in ~14 chunks. One clause added to ruling 32's *excessus* row (the adjective). No line
in any `## Latin` body or `**La.**` half changes. No manifest cell changes.**

**Needs Wilson's own judgment beyond approve-all:** (1) **D-5**, a sense ruling (the adjective follows the noun's sense; ¶ 72
*adhaerentiam excessivam* could go either way); (2) **D-2**, where the sheet recommends against the docket (no edit: the
corpus test exempts the verse); (3) whether the **5 pre-interval lines** (passed the p. 288 gate unseen) are touched now —
the p. 288 F1 precedent says yes; F2's `c9-v10-17` "school the Lord" is the stiffest line the ruling produces; (4) F13
overturns a p. 288 sheet claim (item 24's "acedia at every site").
