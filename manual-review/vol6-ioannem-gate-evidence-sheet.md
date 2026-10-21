# Vol VI *Ioannem* SHAKEDOWN GATE (p. 268, ruling 76): EVIDENCE SHEET

Compiled 2026-10-20 by a read-only agent. **Nothing here is settled. Wilson rules off this sheet.** No file under `vol*/` was
edited. Nothing was committed, pushed or stashed. Passes 1–3 are in the separate `vol6-ioannem-gate-passes-draft.md`
(another agent's file, untouched here).

**Scope: 13 chunks, pp. 239–269.** prooem 52 · prol 9 · c1-v1-2 22 · v3-5 22 · v6-8 18 · v9-14 29 · v15-18 25 · v19-23 23 ·
v24-28 23 · v29-30 7 · v31-34 17 · v35-42 38 · v43-51 46 = **331 numbered entries + 12 `tr-` notes.**

⛔ **Every census below is taken over the LIVE REGION only** (`## Latin` body, `## English` body, and the `**La.**`/`**En.**`
halves of `## Apparatus`). Frontmatter and `## Notes` are excluded. Cells read **body+apparatus**. Paragraph parity La = En holds in all 13
chunks (39/11/18/22/22/29/25/26/18/12/19/40/36), so body sites were aligned paragraph by paragraph. Scripts: scratchpad `gate/*.py`.
Read-only checks run at compile: `check-live-flags.py vol6` → 81 chunks, none · `check-vol5-apparatus.py --volume=vol6` → 81 chunks /
2,539 entries, all passed (p. 269 PENDING n. 2–13) · `check-vol5-census.py` → rosters agree, 124 runovers.

---

## ▶ ONE-SCREEN SUMMARY

| # | item | recommendation (mine) | text lines | kind |
|---|---|---|---|---|
| 1 | headless-pericope titles (4 chunks) | ⭐ **Apply RULING 17**, which already governs Vols VI–X: `title_la` = the divisio's first sentence after the lemma. The lemma default came from the dispatch brief and departs from ruling 17 | 16 | mechanical |
| 2 | stacked heading at c1-v43-51 | **Keep the lowest heading, taken whole.** Cap. II's first chunk then falls under ruling 17. **Separately, restore the dropped ordinals** (*Primo,* / *Secundo,*) at v3-5, v15-18 and v19-23, as Eccl/Sap keep them (33 of 64 titles) | 0 + 9 | mechanical |
| 3a | *virtus* → power/virtue | **Ratify the sense split as built:** 9 "power", 11 "virtue", and keep ¶ 71 *virtutem baptizandi* as "virtue" against *potestas* | 0 | — |
| 3b | "Holy Spirit" in Douay | **Use "Holy Spirit" everywhere** (Vols I–IV have 0 "Holy Ghost"). Conform the one outlier, c1-v15-18 p. 254 n. 9 | 1 | mechanical |
| 3c | `tr-` one-root (*studium*) | **Release *studium* in *Ioannem* to the dikaisune rule:** contextual English plus the existing note. Ruling 54's reason belongs to *Sapientiae*, and n = 3 here | 2 + 2 notes | per-site |
| 4 | ruling 74 register review | Holds at every item except **four inconsistencies:** (i) *testimonium perhibere* give/bear split → conform the 7 "bear" sites to "give" (ruling 74's letter); (ii) *doctor* → "teacher" once → "doctor"; (iii) I Tim. 6:16 *habitat* → "dwelleth in" ×2 (v3-5 says "inhabiteth"); (iv) Wis. 7:24 *munditiam* is "purity" here and "cleanness" in Sap c7 → ratify the release (*pudicitia* = 0) | 7 + 2 + 1 + 0 | per-site |
| 5 | resolver docket | 41 Notes items + **3 new ones found here**. 2 are transcription matters needing nothing. **About 8 tool jobs.** Two classes file a silent wrong target (wrong `chunk`, or a wrong book at confidence A/B), and those go first | 0 | tool |
| 6 | other reserved items | `verses: "14-18"` → **conform to "15-18"** (rulings 15/50). The index misses and the Douay block are record-only. **Doc defect:** c1-v43-51 has 46 entries, not "45" | 1 + doc | mechanical |

**If all are taken: 39 English/frontmatter lines + 2 note rewrites + ~5 doc lines. No Latin line in `## Latin`/`## Apparatus`
changes** (titles change in frontmatter and in the `## *…*` subtitle only).

---

## 1. HEADLESS-PERICOPE TITLE PROCEDURE

**Census (4 of 11 Cap. I pericopes, plus Cap. II's first).** Each opens on an ordinary paragraph with no `####` above it. Each stands under `c1-v19-23`'s
`Primo, de manifestatione per Ioannem.`, which governs John's three testimonies (¶¶ 44–88). None carries an opener heading (correct under ruling 17).

| chunk | pp. | `title_la` / `title_en` NOW (lemma) | divisio's first sentence after the lemma (ruling 17), La / En as already built in the body |
|---|---|---|---|
| c1-v24-28 | 258–259 | *Et qui missi fuerant* / "And they that were sent" | *Iam dixit Ioannes veritatem de se ipso; hic vero testimonium dat de Christo et describit hoc ordine* / "John has already told the truth about himself; but here he gives testimony about Christ, and he describes it in this order" |
| c1-v29-30 | 259–260 | *Altera die vidit Ioannes* / "The next day John saw" | *Perhibuit supra beatus Ioannes testimonium de Christo absente; hic perhibet testimonium de Christo ad se veniente* / "Above blessed John bore testimony about Christ absent; here he bears testimony about Christ coming to him" |
| c1-v31-34 | 260–261 | *Et ego nesciebam* / "And I knew not" | *Posita est testificatio, ponitur hic eius corroboratio sive certitudo, quae describitur hoc ordine* / "The testifying has been set down; here is set down its corroboration or certitude, which is described in this order" |
| c1-v35-42 | 261–265 | *Altera die iterum stabat* / "The next day again he stood" | *Supra posuit duo testimonia, hic sequitur tertium, quod perhibuit, ipso ante eum deambulante; et describitur testimonium cum fructu suo* / "Above he set down two testimonies; here follows the third, which he bore while the other was walking before him; and the testimony is described with its fruit" |

**The decisive text: ruling 17 (Wilson, 2026-10-11, `vol6-pilot-setup.md`).** *"▶ General rule for Vols VI–X: a pericope that opens with no
printed heading takes no opener heading, and its `title_la` is the first sentence of its divisio after the lemma"*. Reason given:
*"a heading invented for the reader would be our text set where Quaracchi set none … the divisio's first sentence after the lemma is the
unit's own statement of what it is."* The precedent is `bon-eccl-c10-v4-7`, with `c7-v1` and `c9-v1-3` before it. ⚠ **None of the four chunks' Notes cites ruling 17.** Each says
*"the provisional default (from the dispatch brief) applied"*. The departure came from the brief. No builder chose it.

| option | cost (one line) |
|---|---|
| **(a) Apply ruling 17 as written** | 4 lines × 4 chunks (`title_la`, `title_en`, `## *…*`, `transcription_status`) = 16. The titles run long (one to two clauses), as Eccl c10-v4-7's does |
| (b) Keep the lemma titles; amend ruling 17 for *Ioannem* | 0 lines. Lemma titles are short and are the Gospel's own words. But one work now diverges from a Vols VI–X general rule, and from Eccl inside this volume |
| (c) Title from the governing heading above (`Primo, de manifestatione per Ioannem`) | 8 lines. **Five consecutive chunks (v19-23 … v35-42) would share one title** |
| (d) Editorial title, e.g. from the marginale *Testimonium Ioannis secundum.* | Invents a heading Quaracchi did not set. Ruling 17's own reason refuses it, as do the four chunks' Notes |
| (e) Verse range only ("Vers. 24-28") | The breadcrumb already says it. The title field would be empty of content and would need a new title shape in the build |

**What Capitulum II will need.** p. 269 sets `CAPITULUM II.` and then `1. Et die tertio nuptiae etc.` with no heading. Under (a), the
c7-v1/c9-v1-3 "first sentence below a capitulum heading" precedent and ruling 17 agree. The title is the first sentence after the lemma. The raw
reads *Postquam descripta est discipulorum vocatio, describitur hic facta per Verbum et de Verbo incarnato manifestatio*
(raw L42977, **unverified on the plate**). Under (b) it would be *Et die tertio nuptiae*. How many later *Ioannem* pericopes are headless is
**unmeasured**. The class will recur, so one rule is needed now.

**Kind:** mechanical (every sentence is already transcribed and translated in its chunk). **⭐ Recommendation (mine): (a).** It is
the standing rule. The lemma default was a brief's provisional stand-in that nobody checked against ruling 17.

---

## 2. STACKED-HEADING TITLE AT c1-v43-51 (and a related ordinal drop)

**The printed situation (p. 265).** Three centred headings stand at the head of the chunk:

| # | heading | governs | covers this chunk exactly? |
|---|---|---|---|
| 1 | `De manifestatione Verbi per se ipsum.` (roman, larger) | 1:43–11:47 (¶ 89: *usque ad finem undecimi*) | no (ten capitula) |
| 2 | `Primo, de hac manifestatione quoad conditiones a parte eorum quibus fit.` | 1:43–4:54 (four kinds of persons) | no (four capitula) |
| 3 | `Prima manifestatio, quae est facta discipulis.` | 1:43–2:11 (*vocatio* + *Et die tertio nuptiae*) | no (spills into Cap. II) |

The exact unit (*vocatio discipulorum*, 1:43–51) has **no heading**, only the marginale *De 1. membro quatuor.* and the sentence
*Vocatio igitur discipulorum a Domino facta describitur hoc ordine.* **Built:** heading 3 taken whole (ruling 47), *Prima…* →
"The first manifestation, which was made to the disciples". This follows `c1-v19-23`'s lowest-heading precedent.

| option | cost |
|---|---|
| **(a) Lowest heading, whole (as built)** | 0 lines. The title also names 2:1–11. **Capitulum II then opens with no heading and falls under item 1's rule**, so the two chunks do not share a title |
| (b) Highest heading (1) | 3 lines. It would title ten capitula, and it breaks the v19-23 precedent |
| (c) The governing divisio sentence, *Vocatio igitur discipulorum a Domino facta describitur hoc ordine* | 3 lines. It covers the chunk exactly. But it extends ruling 17 to a chunk that **does** carry printed headings, a new sub-rule |
| (d) Heading 3 also for Cap. II's first chunk | Two chunks with one title. Refused by the same logic as 1(c) |

**⚠ Related finding, not raised in any Notes: *Ioannem* drops leading ordinals and *Ecclesiastes*/*Sapientia* keep them.** Built titles:
`c1-v3-5` *De Verbo in comparatione…* (heading *Secundo, de Verbo…*); `c1-v15-18` *De manifestatione Verbi incarnati in generali* (heading
*Primo, de…*); `c1-v19-23` *De manifestatione per Ioannem* (heading *Primo, de…*); `c1-v1-2` also drops `Pars. I.` The Eccl/Sap practice:
**33 of 64 `title_la` keep the leading ordinal** (e.g. `bon-sap-c1` *Primo, de triplici iustitia hominis quoad Deum*; `bon-sap-c12`
*Secundo, de punitione…*). Ruling 47's reason is that *"cutting invents a title Quaracchi did not print."* Restoring the ordinals at the three chunks costs 9 lines
(`title_la`, `title_en`, `## *…*`), mechanical. The `Pars. I.` label can stay dropped, because Sap c1/c6 never title from the PARS line.

**⭐ Recommendation (mine): (a) for c1-v43-51, 0 lines, and restore the three ordinals, 9 lines, mechanical.** A rule worth writing down:
*stack → descend to the lowest heading and take it whole; if even that overshoots, keep it; a sentence title only where no heading stands.*

---

## 3. PROVISIONAL CONVENTIONS

### 3a. *virtus* → "power" / "virtue": all 20 sites (no ruling exists. The corpus renders it by sense. The Itinerarium had a work-scoped *virtus* → power against *potentia* → potency)

| chunk | site | Latin | English | sense |
|---|---|---|---|---|
| prooem | p. 241 ¶ 5 | *per virtutum multitudinem* | the multitude of the virtues | moral (Ezek. 17:3 allegory) |
| prol | p. 245 n. 4 | *aquilina visus virtute* | the incorrupt **power** of an eagle's sight | faculty |
| c1-v1-2 | p. 247 n. 7 | *quid sit Dei virtus et Dei sapientia* [I Cor. 1:24] | the **power** of God | Douay |
| c1-v3-5 | p. 249 n. 11 | *nihil sine Filii virtute productum* | the **power** of the Son | efficacy |
| c1-v9-14 | p. 253 Quaest. reply | *fides est prima virtutum* | the first of the virtues | moral |
| c1-v9-14 | p. 253 n. 10 ×2 | Cod. D *prima virtus … virtutum fundamentum* | the first virtue … of the virtues | moral |
| c1-v19-23 | p. 257 | *in spiritu et virtute Eliae* (Luke 1:17) | spirit and **power** of Elias | Douay |
| c1-v29-30 | p. 260 ¶ 62 ×3 | *de virtute Divinitatis* ×2, *solius divinae virtutis* | **power** of the Divinity; the divine **power** alone | divine might |
| c1-v31-34 | p. 260 ¶ 67 | *in eius solo nomine et virtute* | in his name and **power** alone | efficacy |
| c1-v31-34 | **p. 261 ¶ 71** | ***virtutem baptizandi***, then *quintuplex est **potestas** baptizandi* | "***virtue*** of baptizing", then "the **power** of baptizing" ×5 | **power sense, rendered "virtue" to keep it off *potestas*** |
| c1-v35-42 | p. 265 ¶¶ 87–88 ×3 | *aedificium virtutis*; *virtutum incitamentum*; *ad virtutem incitativum* | edifice of virtue; incitement to virtues; incitative to virtue | moral |
| c1-v35-42 | p. 265 n. 2 ×3 | *ad virtutem exercendam*; *ex virtute* ×2 | virtue | moral |
| c1-v43-51 | p. 268 ¶ 101 | *esse virtutis divinae, non humanae prudentiae* | of divine **power** | divine might |

**Totals: 9 "power", 11 "virtue".** Nothing else in scope makes English "virtue". "Power" also renders *potestas* (13: v9-14 ×6, v19-23 1, v31-34 ×6),
*potentia* (v1-2 *operativam potentiam*, v35-42 *fortitudinem potentiae*) and *vis* (v29-30 *vim regenerativam*). **A sentence that holds both
*virtus* and another "power" word occurs once (¶ 71).** Same Latin, same sense, same English at every other site.

| option | cost |
|---|---|
| **(a) Ratify the sense split as built**, with ¶ 71 kept as "virtue" | 0 lines. The cost: one "virtue" carries a power sense, disclosed in c1-v31-34 Notes (a) |
| (b) Sense split, but ¶ 71 → "power" | 1 line. Erases *virtus*/*potestas* in the one sentence that sets them side by side |
| (c) One root, "virtue" everywhere (archaic "virtue" = power) | 9 lines, including Douay I Cor. 1:24 and Luke 1:17 adjusted. "the virtue of the Divinity" |
| (d) Dikaisune, contextual plus a `tr-virtus` note per chunk | 0 text lines, ~10 notes in scope, with the note burden growing across 105 chunks |

**⭐ Recommendation (mine): (a).** *virtus* is pervasive and the two senses never collide except at ¶ 71, where the built choice already
protects the Latin distinction. Per-site if anything changes.

### 3b. "Holy Spirit" inside Douay quotations: every *Spiritus sanctus* site

| chunk | Latin sites (prose / quotation) | English |
|---|---|---|
| prooem | 9 body + 1 n. (p. 239 n. 1), all prose | "Holy Spirit" ×10 |
| c1-v31-34 | 5 prose (¶¶ 66, 67, 69 ×3) + **4 quotations**: Mark 1:8 (¶ 65), Luke 3:22 (¶ 66), John 1:33 lemma (¶ 67), Wis. 1:5 *Spiritus enim sanctus effugiet fictum* (¶ 69) | "Holy Spirit" at all 9 |
| **c1-v15-18** | **1 quotation, p. 254 n. 9**: Luke 1:15 *Et Spiritu sancto replebitur* | **"Holy Ghost"** ← the only one in scope |
| c1-v43-51 | 0 (*a Spiritu*, Matt. 4:1 → "by the Spirit") | — |

**20 sites: 15 prose, all "Holy Spirit"; 5 quotation, 4 "Holy Spirit" and 1 "Holy Ghost".** Corpus, live region: Vols I–IV
**3,580 "Holy Spirit" / 0 "Holy Ghost"**. Vol V 464 / 8 (all 8 inside Douay quotations). Vol VI 67 / 2 (`bon-sap-c9` John 14:26 and this one).
Decisive: c1-v31-34 ¶ 66 glosses the Luke quotation in the same sentence: *descensus Spiritus sancti … « Descendit Spiritus sanctus
corporali specie »* → "the descent of the Holy Spirit … « The Holy Spirit descended in a bodily shape »". "Holy Ghost" there would split the gloss from its
quotation. That is the split the Sermones gate refused for *magister* (ruling 2; ruling 74 inherits it).

| option | cost |
|---|---|
| **(a) "Holy Spirit" everywhere, Douay included** | 1 line (c1-v15-18 p. 254 n. 9 En). Out of scope: `bon-sap-c9`'s one site and Vol V's 8 (deployed) as a parked job |
| (b) Douay "Holy Ghost" inside quotations only | 4 lines in c1-v31-34. ¶ 66 then reads "Holy Spirit" against "Holy Ghost" in one sentence |
| (c) Leave mixed | 0 lines. The one-site outlier stands undisclosed |

**⭐ Recommendation (mine): (a)**, mechanical.

### 3c. The `tr-` notes and the *studium* one-root rule

**All 12 `tr-` notes in scope** (English-only anchors; Latin `tr-` anchors: 0):
`tr-doctrina` ×5 (prooem; prol; c1-v1-2; c1-v24-28, anchored in the p. 258 n. 4 En half; c1-v35-42) · `tr-lumen` ×5 (prol; v3-5;
v6-8; v9-14; v19-23. These are exactly the 5 chunks with *lumen*, one note each) · `tr-studium` ×2 (v35-42; v43-51).

***studium* census: 3 sites, all in the two chunks:**

| site | Latin | English | the rule's cost |
|---|---|---|---|
| c1-v35-42 ¶ 79, p. 263 | *quia studiose eum quaerebat* | "because he was **studiously** seeking him" | fits |
| c1-v35-42 p. 264 n. 1 (Chrysostom) | *haec humano studio peracta visa fuissent* | "they would have seemed accomplished by **human study**" | sense = human effort/contrivance |
| c1-v43-51 ¶ 94, p. 267 | *non veniebat voluntate tentandi, sed studio proficiendi* | "he came not with a will to tempt, but with **a study of profiting**" | sense = eager application to advance |

**Where the rule comes from:** Sap ruling 54: *"c8 *studium* → 'study' (the work's one root)… Reason: c8's heading *ex studio quaerendi
sapientiam* is a proof inside the exhortation *ad studium et amorem sapientiae*."* The reason belongs to *Sapientia*. *Ioannem* has no
such frame. Ruling 74 carried the note ("`tr-studium`") without restating the reason.

| option | cost |
|---|---|
| (a) Keep one root, "study" (as built) | 0 lines. "human study" and "a study of profiting" stand. Both builders flagged them |
| **(b) Release *studium* in *Ioannem* to the dikaisune rule** (*doctrina*/*vacare* shape): contextual English plus the existing `tr-studium` note rewritten to say which side | 2 En lines (e.g. "by human effort", "with an eagerness to profit") + 2 note rewrites. "studiously" stays. A recorded cross-work divergence (cf. Sap ruling 59 on *supplicium*; Sermones ruling 6 released the purity triple on the census) |
| (c) Contextual, no note | 2 lines. Breaks the dikaisune rule, which always carries a note |

**⭐ Recommendation (mine): (b)**, per-site. At n = 3, with no exhortation and no competing Latin word, the one-root rule protects nothing. This is the
*dominium* test (CLAUDE.md § PERFECTIONE ruling 2).

---

## 4. RULING 74 REGISTER REVIEW (live region; Latin body+app → English)

| item | Latin sites by chunk (pr·pl·v1·v3·v6·v9·v15·v19·v24·v29·v31·v35·v43) | rendering | verdict |
|---|---|---|---|
| *lux* | ·/·/3+1/13+3/17+3/9+2/·/·/·/·/·/2/1 = **54** | light (+ Douay I Tim 6:16 "light" ×2 for *lucem*) | ✓. ⚠ see (iii) |
| *lumen* | ·/1+1/·/2/4/3+1/·/1/·/·/·/·/· = **13** | lumen 13/13. `tr-lumen` at the first site in 5/5 chunks | ✓ |
| verse test | Ps. 4:7 ×2 (v3-5 body leans *Sine quo lumine*; v9-14 Bede) → "lumen"; John 1:7 ×2 (v6-8 lemma; v19-23 quotation) → "lumen"; John 1:9 *lux vera* → "true light" | as ruled | ✓ |
| *luminosior* (v1-2 ¶ 8) / *luminaria* (v6-8, Phil. 2:15) | 1 / 1 | "more luminous" / "luminaries" (Douay "lights" adjusted, so "light" stays *lux*'s) | ✓ ratify. Neither is *lux* or *lumen*. Both builders reserved them |
| *Verbum*/*verbum* | 86 / 72 | follows the print | ✓ |
| *signum* / *miraculum* | 12 / 9 | sign / miracle | ✓ (no Douay "miracle" verse in Cap. I) |
| *caritas* / *dilectio* / *diligere*,*amare* / *amor* | 10 / 2 / — / 5 | charity (2 apparatus sites are variant readings kept in Latin) / dilection 2/2 / love / love | ✓ |
| *testimonium* / *testis* | 84 / 2 (+ Prov. 14:5 *Testis*) | testimony / witness | ✓ |
| ***testimonium perhibere*** | see (i) | give **and** bear | ⚠ **(i)** |
| *magister* | v9 1+1 · v35 5+1 · v43 1 = **9** | teacher 9/9, including Douay 1:38 and Matt. 8:19 "Teacher"; prol *magisterii* → "office of teacher" | ✓ |
| Lombard *Magister* | v1-2 n ×3 · v24 n ×1 · v31 ¶ 71 | the Master 5/5 | ✓ |
| ***doctor*** | prooem ×2 · v24 1 · v43 1 = **4** | doctor ×3, **teacher ×1** | ⚠ **(ii)** |
| *discipulus* | 44 | disciple 44 | ✓ |
| *Glossa* / *Evangelista* / *Iudaei* / *Rabbi* / *Paraclitus* | 15 / 26 / 12 (+2 *Iudaea*) / 4 / 0 | Gloss / Evangelist (print's lower-case *evangelista* ×3 → capital) / Jews / Rabbi / — | ✓ |
| *doctrina* | 23 in 5 chunks | teaching 23/23. `tr-doctrina` in 5/5 chunks | ✓ |
| *intellectus* / *intelligentia* | 12 / 13 | understanding 12/12, zero bare "intellect" / intelligence 9 in body prose. "understanding" in Dan. 1:17 Douay ×2 and the *Ad intelligentiam praedictorum* idiom (v1-2; the `bon-qsc-q2` precedent) | ✓ |
| *pietas* | 1 (prooem) | piety | ✓ |
| *vaca-* · *fundam.* · *pudicitia* · *supplicium* · *quies* | 0 · 0 · 0 · 0 · *quieto*/*quietem*/*quietus* 4 | — / — / — / — / rest | ✓ positive zeros |
| purity triple | *munditia* 1, *puritas* 0, *pudicitia* **0** | Wis. 7:24 *propter sui munditiam* → "purity" (Douay) | ⚠ **(iv)** |

**The four inconsistencies:**

**(i) *testimonium perhibere* in Bonaventure's own prose: two verbs, split at the chunk boundary.** Inside Douay and lemma quotations the verb is "give"
at every site (1:7, 1:8, 1:15, 1:32, 1:34, 5:33, 19:35), which is consistent. In the prose:
- **"give" ×6:** c1-v6-8 p. 251 Quaest. II *testimonium perhibetur alicui* ×3 → "testimony is given"; *testimonium sufficiens perhibuit* → "gave sufficient
  testimony"; c1-v19-23 p. 256 ¶ 44 *perhibitum est* → "was given"; ¶ 45 *quibus Ioannes perhibet testimonium* → "to whom John gives testimony".
- **"bear" ×7 (+ *perhibitio* "bearing" ×3):** prol p. 245 *perhibentur* → "are borne"; c1-v29-30 ¶ 61 *Perhibuit supra … hic perhibet* →
  "bore … bears", ¶ 62 → "bears"; c1-v31-34 ¶ 71 *Testimonium perhibuit Ioannes* → "bore"; c1-v35-42 ¶ 72 → "bore", ¶ 83 → "bore".
- Ruling 74's text: *"`testimonium perhibere` → 'give testimony' (Douay)."* The "bear" form begins at c1-v29-30 and is carried forward as a construal
  ("as `c1-v31-34`"). It was never raised for the gate. **The one sense reason** is c1-v31-34 ¶ 71, which sets *perhibuit* beside ***tulit***
  *testimonium* (*ferre*). There "bore" is right for *tulit*.

| option | cost |
|---|---|
| **(a) Conform the prose to "give"** (ruling 74's letter; the gloss then tracks its lemma). *perhibitio* → "giving"; ¶ 71 *tulit* keeps "bore" | 7 En lines, per-site |
| (b) Ratify "give" in quotations and "bear" in prose, and conform v6-8/v19-23 | 4 En lines, per-site. Amends ruling 74 |
| (c) Leave mixed | 0. Same Latin, two verbs, no sense reason at 12 of 13 sites |

**(ii) *doctor* → "teacher" at prooem p. 241 ¶ 4:** *doctoris sublimitas manifestatur in sublimitate doctrinae* → "the sublimity of a
**teacher** is made manifest in the sublimity of his teaching". The other 3 sites read "doctor" (prooem p. 243 *libri doctorum*; v24-28 ¶ 53 *veritatis
doctorem*; v43-51 ¶ 101 *magnum doctorem in Lege*). The prooem's Notes do not disclose it. Sense reason offered: "teacher/teaching" keeps the
*doctor*/*doctrina* root echo. Cost of keeping it: "teacher" then renders two Latin words (*magister* is ruled "teacher"). **Conform: 1 body line + 1
line of the prooem `tr-doctrina` note** (*"the excellentia doctrinae of a teacher"*). ⭐ Mine: conform, mechanical.

**(iii) I Tim. 6:16, printed *Lucem habitat inaccessibilem* (Vulgate *inhabitat*) at two sites:** c1-v3-5 p. 250 → "inhabiteth light
inaccessible"; c1-v15-18 p. 255 → "He dwelleth in light inaccessible". Each chunk's apparatus gives the Vulgate as "inhabiteth". "Dwelleth in" adjusts the Douay to the print's *habitat*
(ruling 5), so the body and the Vulgate note read differently, as the Latin does. ⭐ Mine: **conform c1-v3-5 to "dwelleth in"**, 1 line.
(The corpus is mixed too: `bon-qmt-q1-a1` "dwelleth in", `bon-hex-c12`/`bon-qsc-q4` "inhabiteth".)

**(iv) Wis. 7:24 *propter sui/suam munditiam*: "purity" here (c1-v9-14 p. 252), "cleanness" in `bon-sap-c7` p. 158.** Ruling 74 says:
*"the purity triple **if** *pudicitia* is live (census at the shakedown; release per Sermones ruling 6 if zero)."* The census is **0**, so the
release condition is met. "Purity" is the release working as Sermones ruling 6 did ("deliberately… so no later work inherits a phantom
rule"). ⭐ Mine: **ratify the release; record the cross-work divergence.** 0 lines.

---

## 5. RESOLVER DOCKET

Every ⚠ RESOLVER NOTES item in the 13 chunks' Notes was checked against `index/citations.tsv` (**374 records** from `bon-ioan-*`:
223 verse · 45 chapter · 86 chunk · 5 page-multi · 3 distinctio · 2 work · 1 articulus · 1 ambiguous · 1 dangling · 5 unresolvable ·
2 excluded). Every Notes claim was checked: present rows against the ledger, "no record" claims by the absence of a row. **All were CONFIRMED as described, and none was found wrong.** **Three new items** (★) were found in the ledger and are in
no chunk's Notes.

| class | sites (chunk, note) | ledger shows | kind | fix |
|---|---|---|---|---|
| **A. Silent wrong `chunk`, bare book numeral in a chain** | v6-8 p. 250 n. 8 `et IV. d. 2. dub. 2.`; v15-18 p. 256 n. 3 `II. d. 23. a. 2. q. 3` | → `III-d2-dubia`; → `I-d23-a2-q3` | resolver defect, **dangerous** | **tool**: a bare roman book numeral before `d.` restarts the book |
| A′. same note, dangling | v15-18 p. 256 n. 3 `III. d. 14. a. 1. q. 3.` | dangling (the QA's 1 line) | resolver | same tool fix |
| **B. Silent wrong `chunk`, `pag. N` of a non-Bonaventure book** | prooem p. 239 n. 1 `pag. 128` / `pag. 132` (Fidelis a Fanna, *Ratio*); v1-2 p. 246 n. 7 `tom. I. pag. 812` (De la Bigne) | → `bon-sap-c3`, `bon-sap-c4`, `bon-sent-I-d45-dubia` | resolver, **dangerous** (looks resolved) | **tool**: the known bare-`pag.` volume-inheritance class (Vol V docket) |
| **C. Wrong book or kind at confidence A/B** | v35-42 ¶ 77 `primae Ioannis secundo`; prol p. 245 n. 2 Bede's `Ioan. 1, 1`; ★ prooem p. 241 n. 3 `ibidem` (= Augustine, Tract. 1); ★ v15-18 p. 254 n. 8 `Cfr. ibid. XXV. c. 10. n. 25` (= Gregory, *Moralia*) | → `Ioan 2:18` B (Gospel); `Ioan 1:1` A; `Apoc 21:10` **A** by cross-note anaphor from p. 240 n. 10; `Ioan 1:14` A by in-note anaphor to a bracketed verse | resolver, **dangerous** | **tool**: ordinal-word numerals (row D); *ibid.* binds only inside its own note and never to a bracketed verse (Eccl ruling 14's "2a/2b" rule); a commentary siglum blocks a scripture reading (cf. *in Ioan.* already handled) |
| D. Unnumbered bucket from an ordinal-word numeral | v24-28 ¶ 59 `primae ad Corinthios tertio`; v35-42 ¶ 80 `…decimo`; v43-51 ¶ 101 `…primo`; ★ prooem p. 239 n. 1 `tertii Reg. 3, 12` | `Cor*` 3:11, `Cor*` 10, `Cor*` 1:26, `Reg*` 3:12 | resolver (never guessed; information lost) | **tool**: read *primae/secundae/tertii/quarti* as the book numeral |
| E. Lost self-references | v6-8 p. 251 n. 12 `S. Bonav., IV. Sent.…`; v31-34 p. 261 n. 11 `Ed. fide Commentarii Bonav. in IV. Sent.…`; v9-14 p. 253 n. 9 `Breviloq. … et 3.`; v19-23 p. 258 n. 3 `… q. 2. et 3`; v15-18 `q. 1-3`, `q. 1. et 2`; v24-28 p. 259 n. 15 roman `d. XXV.`; prooem p. 243 n. 7 / p. 244 n. 4 `I. Sent. Prooem. q. 2`; v3-5 / v24-28 `Comment. in Sap. 14, 3`, `Hexaëm. collat. N` | `excluded` ×2; continuation, range and roman forms absent; named-work forms absent | resolver | **tool**: a `Bonav.` siglum is self; `et N` continuations; `q. a-b` ranges; roman distinctio; Sentences Prooemium; named-work forms (the Vol V `p198-nota` class) |
| E′. Ambiguous by design | v19-23 p. 258 n. 3 `IV. d. 17. p. I. q. 2` (articulus unstated, two candidates) | `ambiguous` | **correct behaviour** | nothing |
| F. Work's own paragraph form (ruling 73) | v9-14 `infra c. 13, 38`; v19-23 `infra n. 52. ad 2.`; v24-28 / v31-34 `infra n. 71.`; v31-34 `[n. 60. 65. et 67.]`; v35-42 `infra n. 90. et 101.`; v43-51 `n. 44`, `n. 17`; (Cap. II p. 269 n. 2 `n. 89.`) | no record | resolver (anticipated) | **tool**: read the `paragraphs:` field (ruling 73 already provides it) |
| G. Scripture *ibid.* read as a crossref | v1-2 `ibid. 10, 30`; v3-5 `ibid. 15, 5`; v6-8 `ibid. v. 9`; v15-18 `ibid. v. 11`; v19-23 `ibid. v. 35`; v31-34 `Ibid. v. 18`, `Ibid. 34, 5` (no record) | `unresolvable` ×5 (in QA); 2 absent | resolver | **tool**: same rule as row C (the in-note scripture antecedent). Control: v29-30 `ibid. v. 15` → Matt 3:15 resolves correctly |
| H. No record by design | bare `Supra v. 7.`/`v. 19.`/`v. 33.`; body *infra quinto* etc. (own Gospel); tier-C body ordinals with the verse in a sibling note; patristic loci; v24-28 `Comment. in Luc. 3, 16` (Vol VII, not in corpus); `supra notam 1` | as designed | — | **nothing** |
| I. Transcription matter (as printed) | v43-51 p. 266 n. 4 `Matth. 5 16.` (comma missing in print) → `Matth 5` C; v9-14 p. 253 n. 5 `Cfr:` (resolved fine) | as printed | **transcription, correct** | **nothing** (optional resolver tolerance for a missing comma) |

**Counted:** about 8 tool jobs (A, B, C-ibid, C/D ordinal-word, C-commentary siglum, E ×several forms, F, G shares C's rule). **Rows I and H and E′ need nothing.** ⭐ **Mine:**
record all of it on the ruling-14 docket. **Run A, B and C first**, because they file a wrong target that looks right. None is a text edit.

---

## 6. OTHER ITEMS THE NOTES RESERVED FOR THE GATE / FOR WILSON

| item | evidence | options (cost) | ⭐ mine |
|---|---|---|---|
| **c1-v15-18 `verses: "14-18"`** (id stays the index's `v15-18`). *"For Wilson at the p. 268 gate."* | ¶ 35 opens on 1:14b *Et vidimus gloriam eius*; the first `(Vers. N.)` marker is `(Vers. 15.)`; the index label is *Vers. 15-18*. **Eccl ruling 15:** a folded-in earlier verse is *"recorded in its Notes and `transcription_status`, not in the label"*; **Sap ruling 50:** *"The `verses` field keeps the index label VERBATIM"* | (a) conform to `"15-18"`, with 1:14b recorded in Notes/status: 1 frontmatter line, breadcrumb → "Vers. 15-18"; (b) ratify `"14-18"` as a new mid-verse class: 0 lines, departs from two rulings | **(a)**, mechanical |
| Index misses: *Vers. 35-42 » 262* (lemma on 261, first marker on 262); *Capitulum II » 268* (Cap. I closes on 269) | c1-v31-34 and c1-v43-51 Notes, "recorded for the gate" | record as the *Ioannem* analogue of Sap ruling 55 (index page = page of the first `(Vers. N.)` marker; it explains 262 and does not explain 268) | record only, 0 lines |
| Gate page vs close page | "p. 268" names the gate; Cap. I closes four lines into p. 269 | — | record only |
| Douay adjustments disclosed "for the gate" (ruling 5 applications) | 1:14 "dwelt in us"; 1:9 "illumines"; 1:15/27/30 "Who was made before me" ×3; 1:25 "a prophet"; 1:29 plural *peccata* "sins"; 1:37 "speaking"; 1:39 "stayed there"; 1:42 "Joanna"; 1:46 two readings; 1:50 "A greater thing"; 1:51 "that"; *Nazaraeus* "Nazarite" | ratify as a block (0) or reopen any one (1 line each) | ratify the block |
| Hand-lettered `C.P I. Sent. d. 5. dub. 11.` (v3-5, p. 249) | ruled 2026-10-18 (ruling 78) | — | **closed**, nothing owed |
| ⚠ **Doc defect (found here):** c1-v43-51 claims "FORTY-FIVE ENTRIES" (status line, Notes, resume ×4) | its own page-split map sums 6+12+12+15+1 = **46**, and the file holds 46 numbered defs. Every other chunk's claimed count matches its file | correct "45" → "46" (status + Notes + resume): doc only | conform |
| Observed (not reserved): *certitudinaliter* in three English forms | "with certitude" ×3 (prooem p. 243 ×2, v15-18 p. 255) · "with certainty" ×1 (v24-28 p. 259) · "certitudinally" ×1 + p. 261 n. 10 (v31-34). No sense reason | (a) conform to "with certitude": 3 lines; (b) leave it | (a), optional |

---

**Not checked here:** the plates (no plate was opened; every quotation above is from the built files). The Cap. II opening sentence is **raw only**.
