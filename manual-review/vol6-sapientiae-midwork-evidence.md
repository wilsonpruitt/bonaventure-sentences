# Vol VI — *Commentarius in librum Sapientiae*, MID-WORK GATE (ruling 34): EVIDENCE SHEET

Compiled 2026-10-16 by a read-only agent on Wilson's go. **Nothing here is settled. Wilson rules off this sheet.**
No chunk, tool, resume note or ledger was edited; no push, deploy or stash. `build-citations.py` was run into the scratchpad
(`--out`/`--qa`), and its ledger came out **byte-identical** to the tracked `index/citations.tsv`. Gate log:
`manual-review/vol6-sapientiae-midwork-gate.md`.

**Scope (from frontmatter): `bon-sap-c3` … `bon-sap-c12`, pp. 125–191, 736 numbered entries, 9 `tr-` notes.** Every census below
is over the BUILT files and the RENDERED regions (`## Latin`, `## English`, `## Apparatus`; frontmatter and `## Notes` stripped),
never `raw/`. Scripts: scratchpad `gate/sweep.py`, `gate/census.py` (not in the repo).

## ▶ ONE-SCREEN SUMMARY

**A — text / register questions that need a ruling**

| # | question | recommendation | lines |
|---|---|---|---|
| A1 (18) | *punitio* and *poena* both → "punishment" (41 + 66 sites; 27+ more *punitio* to come, and XIII's own heading is *de punitione per poenas graviores*) | **Split now, before c13: *punitio* → "punishing"**, *poena* stays "punishment" (ruling 20) | ~43 En (per-site) |
| A2 (1, 6, 12, 22 + 5 new) | the misprint class: wrong sorts, slips and unnameable sorts | **Ratify as built**: identifiable wrong sort or slip → as printed + English bracket; unnameable sort → read plain + disclosed (`necessarium` rule); compositor's blank → reproduced + `[*sic*]` | 0 |
| A3 (3 + 2 new) | verse test applied at three new scriptural *lumen* sites (Job 37:3, Col. 1:12, Isa. 50:11) | **Ratify** — all three are quoted only as verses | 0 |
| A4 (11, 16) | fused headings taken whole for `title_la` (c10 run+member; c11 member+sub-member) | **Ratify as a corollary of ruling 36**: a fused heading is taken whole; never split | 0 |
| A5 (17) | ruling 37's bracket used for a BODY slip (c11 p. 180, Prov. 24:16) | **Ratify: ruling 37 covers body and apparatus alike** | 0 |
| A6 (2) | c7 p. 156 *Amans bonum, actum* (Vulgate *acutus*) | **Leave as printed, no bracket** — it reads as a gloss; one site, not three | 0 |
| A7 (15) | c11 expounds to Vers. 27 under `verses: "1-26"` | **Keep the index label** (ruling 27; the c1 Vers. 16 precedent) | 0 |
| A8 (4, 8) | marginal-quaestio counting: the unlabelled p. 159 L pair; numbered `Quaestio 1./2.` | **Keep both as built** (count by marginale; numbered = one each; the unlabelled pair is not counted) | 0 |
| A9 (new) | c6 Sap. 6:27 *accipite disciplinam* → Douay "instruction" (45 of 46 *disciplina* sites → "discipline") | **Decline** (ruling 42: one site, no ruling earned) | 0/1 |

**B — convention defects that are plainly repairs**

| # | defect | repair | lines |
|---|---|---|---|
| B1 (13) | **`tr-doctrina` owed in THREE chunks, not two:** c6 (2 sites), **c7 (1, apparatus p. 154 n. 3 — not on the running list)**, c8 (4). Ruling 11 = one note per chunk carrying the word, apparatus-only included (c3's precedent) | write three notes | 3 notes |
| B2 (new) | **`tr-studium` owed in c8**: *studium* ×7 body + 1 app, rendered **"zeal"** ×5 and "study" ×1, no note — and against the work's kept root (prooem / c1 / c6 notes keep "study") | write the note; **Wilson picks: keep "zeal" (contextual, noted) or conform to "study"** | 1 note (+5 En if conformed) |
| B3 (9, 20) | scouting doc's index table still reads `Cap. X … 174` (printed `171`) | correct the one line in `sapientiae-pilot-scouting.md` | 1 doc line |
| B4 (new) | documentation: item 8's "first numbered quaestiones" is false (c1 p. 112/116, c6 p. 146 came first); item 2's "printed cleanly (3×)" is one site read at 3×; c6's Notes count *doctrina* once (it is twice) | correct in the resume carry-list; chunk Notes not touched unless Wilson wants it | doc only |

**C — resolver / tool artefacts (ruling 40: logged, chunks never edited)**

| # | class | in scope | recommendation |
|---|---|---|---|
| C1 (14, 19, 21, 5, 7) | ⭐ **an in-note `ibid. C, V` / `ibid. v. N` NEVER keeps its own coordinates** — the anaphor copies its antecedent's target whole | **30 scripture records + 4 false crossrefs + 2 non-scripture `ibid.`s filed as scripture**; **corpus-wide 251 scripture records, 1 honoured** (I 4 · II 24 · III 23 · IV 49 · V 88 · VI 63) | **Fix `build-citations.py` as a scoped job BEFORE the p. 235 deploy**, with a before/after diff; not inside this gate |
| C2 (ruling 37 class) | printed slips indexed as printed: c3 Job 24:19 (A), c5 Cor* 12:30 (B), c11 Prov 16 (C) (+ c1 Job 6:2) | 3 (+1) | park; fold into C1's job as a small override table |
| C3 (10, 19) | chain continuations dropped (`et a. 2. q. 1.`, `q. 1-3; a. 2. q. 2.`) | 2 | park |
| C4 (5, 7, 14, 21) | unparsed named units (`supra Prooemium, n. 6`, `Cfr. supra 11, 16.`, `Comment. in Eccle. 1; 15. Quaest. 2.`, `Collat. in Hexaëm.`, `lit. Magistri d. VIII/XXXIX`, `d. 40, dub. 2`, `tom. V. pag. 203 et 403`'s second page) | ~9 | park |
| C5 (new) | `page-multi` where the note's `nota N` already names the owner | 4 here; **1,178 corpus-wide** | park; a design improvement, not a defect |

**If every A/B recommendation is taken: ~43 English lines (A1) + 4 translator's notes (B1, B2) + 1 doc line (B3). No Latin line changes.**

---

## ▶ MECHANICAL PASSES, WITH DENOMINATORS

| pass | what it COUNTED | verdict |
|---|---|---|
| 1 `check-live-flags.py vol6` | **59 vol6 chunks** | **no live `[?]`** |
| 2 `polish-style-scan.py` | **2,178 chunks, vol1–vol6** | 11 issues / 6 chunks (10 PAIR Vols III–IV, 1 V5LABEL) — **ZERO in vol6** |
| `check-vol5-apparatus.py --volume=vol6` | **59 chunks, 1,756 entries**; in scope 67 · 58 · 82 · 74 · 105 · 75 · 55 · 71 · 72 · 77 = **736**, La = En in all ten | **All checks passed**; p. 191 `PENDING n.8` (c13's) |
| `check-vol5-census.py` | vol5 167/167 · **vol6 59/59**; vol6 86 runovers (84 gutter, 2 page) | **Rosters agree.** In scope **29 runovers: 28 gutter + 1 page-crossing (p. 168 n. 11, c9-internal)** |
| `build-citations.py` (scratchpad) | **2,178 chunks → 27,744 records**; ours **1,787** (scripture A 864 · B 304 · C 519; crossref 100 = 77 chunk · 19 page-multi · 2 distinctio · 2 work) | corpus QA **208**; **ZERO QA lines ours**; zero dangling/unresolvable/ambiguous; ledger byte-identical |
| La/En digit multiset | **736 entries** | **4 mismatches, all dispositioned:** c3 p. 126 n. 1 and c5 p. 140 n. 3 = ruling-37 English brackets; c5 p. 144 n. 1 = wrong-sort bracket (`9.` for `q.`); c11 p. 182 n. 8 = number word (*65 Qq.* → "Sixty-five Questions") |
| page markers / anchor sequences | 7–9 markers, 55–105 anchors per chunk | **identical La/En in all ten**; anchor set = def set; no duplicates; `tr-` anchors English-only |

## ▶ PASS 3 — BOUNDARY SWEEP

Every page 125–191 owned exactly once; every register contiguous 1..N; `KNOWN_TOTALS_VOL6` matches on all 67 pages (191 = 8,
n. 8 PENDING). Shared leaves: **125** c2 1–3 / c3 4–11 · **131** c3 1–8 / c4 9–11 · **137** c4 none / c5 1–9 (body-only) ·
**144** c5 1–5 / c6 6–9 · **151** c6 1 / c7 2–9 · **159** c7 1–11 / c8 none (body-only) · **166** c8 1–8 / c9 9–12 ·
**171** c9 1–4 / c10 5–9 · **177** c10 1–6 / c11 7–9 · **184** c11 1–5 / c12 6–10 · **191** c12 1–7 / c13 8 (PENDING). Every
apparatus header states the same split from both sides; every tail is a complete sentence; every incoming body opens on
`### Capitulum N.` + its `####` heading. **CLEAN; no plate needed for any seam.**

---

## ▶ A. TEXT / REGISTER QUESTIONS

### A1 (item 18) — *punitio* / *poena*

**Count (rendered Latin, body + app):** *punitio* c3 3 · c6 1 · c10 5 · c11 20+1 · c12 11 = **40+1**; *poena* c3 12 · c4 5+1 · c5 6+2 ·
c6 5 · c7 1 · c10 2 · c11 18+3 · c12 10+1 = **59+7**; *supplicium* 9. English "punishment" **100+9** — every site of all three
words. *poenalitas* ZERO in scope, so "penalty" is unused. **Forward:** the raw holds **27+ more *punitio*** in cc. XIII–XIX.

**Decisive sentence** (c11 p. 177 L, the divisio for cc. XI–XIX):
> *Hic agit de beneficiis pertinentibus ad adversariorum **punitionem,** et primo de pertinentibus ad **punitionem** per **poenas**
> leviores … secundo de pertinentibus ad **punitionem** per **poenas** graviores, ordinatas ad condemnationem*
> "…pertaining to the **punishment** of the adversaries, and first of those pertaining to **punishment** through lighter
> **punishments**… secondly… to **punishment** through heavier **punishments**…"

and c13's own opening heading (p. 191, read by c12): *Secundo, de **punitione** per **poenas** graviores ordinatas ad condemnationem.*
⚠ For c16: *de **supplicio poenae** culpabilium* — under ruling 20 that reads "the punishment of punishment"; ruling 20's sharing of
*poena*/*supplicium* will need its own look there (not this gate's).

| option | cost |
|---|---|
| (a) keep "punishment" for both | 0 lines; "punishment through heavier punishments" stands in the run heading of cc. XIII–XIX and the act/penalty distinction the divisio is built on is invisible |
| **(b) *punitio* → "punishing"** (verbal noun; *poena* keeps "punishment") | ~41 English body sites + 2 `title_en` (c11, c12) + c13 onward; per-site (the English does not mark which word it renders); same root kept, act vs suffering visible: "punishing through heavier punishments" |
| (c) *punitio* → "chastisement" | wrong for the *ad condemnationem* half (chastisement implies correction); *castigatio* occurs (c3 ×3) |
| (d) *poena* → "penalty" | collides with ruling 20 (*poenalitas* → penalty) and reverses ruling 20 corpus-wide |

**RECOMMENDATION: (b), ruled now so c13 builds to it.** Per-site, ~43 lines, English only. The ruling-20 *dominium* test applies the
other way here: n is large and growing, and the one-word rule is hiding the hinge of Part II's ratio 3.

### A2 (items 1, 6, 12, 22 + five sites not on the list) — the misprint class

| site | printed | treatment as built | sort |
|---|---|---|---|
| c6 p. 148 L | *merilo abstinentiae* | as printed + "merit [so printed: *merilo* for *merito*]" | ascender stroke as tall as *b*/*l* (5×) — an *l*, not a failed *t* |
| c6 p. 146 R | *Sed si **sequalis*** | as printed + "[so printed; *sequalis* for *aequalis*]" | **not on the list**; *s* at full strength (5×) |
| c6 p. 147 heading | *…ad **sapientium** concupiscendam* | as printed + bracket inside the English `####` | **not on the list**; Quaracchi slip in a heading |
| c8 p. 165 R | *sine **defcctione*** | as printed + "[so printed: *defcctione* for *defectione*]" | clean *c*, no eye (10×); same-page control *defectione* |
| c10 p. 173 R | ***Sapientium**, inquam, praetereuntes* | as printed + bracket | dotted *i* + *u* (4×, 9×) |
| c10 p. 171 L | *Haec **illam*** | as printed + "[so printed: *illam*; the verse reads *illum*, him]" | slip against the same chunk's lemma |
| c5 p. 144 n. 1 | Alex. Hal. `S. p. I. 9. 49.` | as printed + "[so printed; a figure *9* stands for *q.*]" | **not on the list**; wrong sort in a locus (authority, unindexed) |
| c5 p. 137 R | *coa tam* | gap reproduced, English "forced [*sic*]" | **not on the list**; compositor's blank, measured (gap min 217–221, flanks full strength) |
| c12 p. 185 | *vigesimo*, n. 5 *ob* | read plain, disclosed | unnameable sorts (the `bon-qmt-q7-a1` *necessarium* rule) |
| c12 p. 187 n. 1 | `Eccle. 1; 15.` | Latin as printed, English `1:15` | printed semicolon, dot measured dark |

**Alternatives:** (a) **ratify as built** — 0 lines; (b) read *merilo* as a failed-crossbar *t* (the `bon-qmt-q4-a1` *sententia*
precedent) — 1 Latin + 1 English line; refused by the builder's measurement (the stroke is a full ascender, not a *t* stem missing
its bar); (c) emend silently — refused by ruling 9. **RECOMMENDATION: (a), one ruling for the whole class.** ⚠ Two bracket forms
are in use and both are consistent: `[so printed: X for Y]` for a letter-level fault, `[so printed; the verse/passage is …]` for a
locus slip.

### A3 (item 3 + two sites in c5) — the verse test at new *lumen* sites

*lumen* in scope: c5 4+2 · c6 1 · c7 5+3 · (c8's *luminaria*, Phil. 2:15, is *luminare*, not *lumen* — "lights", correct).
`tr-lumen` written in c5, c6, c7 — **every chunk carrying the word**. English "lumen" stands where the exposition leans on it
(c5 *iustitiae lumen* glossed "intransitively"; c6 Sap. 6:23 *Diligite lumen sapientiae*; c7 Sap. 7:10 *inexstinguibile est lumen
illius*, Ecclus. 24:6). Received "light" kept at four quoted-only verses, each disclosed in its chunk's `tr-lumen`:
**Job 37:3** *lumen eius* (c7 p. 157) · **Col. 1:12** *in lumine* (c5 p. 139) · **Isa. 50:11** (c5 p. 144 n. 2) · Ps. 35:10 (the
standing exemption). *Super omnes caelos considerat, et lumen eius super omnes terminos terrae* → "…and his light is upon all the
ends of the earth" — quoted for *Omnia prospiciens*, nothing in the prose turns on *lumen*. **RECOMMENDATION: ratify all three. 0 lines.**

### A4 (items 11, 16) — fused headings

c10: *Tertio hortatur ad sapientiam acquirendam per rationes sumtas ab eius effectibus, **et primo** a beneficiis pertinentibus ad
amicorum Dei promotionem* — ratio 3 (cc. X–XIX) + its first member (exactly Cap. X) in one line; no lower heading covers the chapter.
c11: *Primo, de punitione Aegyptiorum propter duplex peccatum, **primo** propter depressionem iniustam* — member (Cap. XI) + its first
sub-member (Vers. 1–15). Options: (a) take whole (as built); (b) cut at *et primo* / *primo* — invents a title Quaracchi did not print;
(c) a lemma-pointer (ruling 17) — discards a printed heading. **RECOMMENDATION: (a), written as ruling 36's corollary.** 0 lines.
(c12's title is the plain sibling of c11's, no descent — the prediction held.)

### A5 (item 17) — ruling 37 in the body

c11 p. 180 R: *Unde **Proverbiorum decimo sexto**: « Septies in die cadit iustus »* → "Proverbs, the sixteenth [so printed; the
verse is Prov. 24:16]" (the leaf's n. 9 itself gives `Prov. 24, 16`). Two more ruling-37 brackets in scope were applied to apparatus
as written (c3 p. 126 n. 1 `Iob 24, 19` → Job 5:19; c5 p. 140 n. 3 `Vers. 30` → I Cor. 12:31). **RECOMMENDATION: ratify — the
bracket marks a certain printed slip wherever it stands.** 0 lines.

### A6 (item 2) — *actum*

c7 p. 156 R: *Dicit ergo: Amans bonum, **actum**;* → "*Loving that which is good,* act;". ⚠ **One site** (the resume's "3×" is the
zoom it was read at). Roman, not lemma face; construes as a gloss (*the good loved is the good act*); no note questions it. Options:
(a) leave; (b) bracket `[so printed; the Vulgate continues *acutus*]` — 1 line, but asserts a slip nobody has shown. **RECOMMENDATION: (a).**

### A7 (item 15) — last address vs `verses`

Measured over all ten: last `(Vers. N.)` matches the field in nine (c3 *18. 19.*, c6 *26. 27.* included); **c11 alone** reaches
`(Vers. 27.)` under `"1-26"`. Options: (a) keep the index label verbatim (ruling 27; the c1 Vers. 16 precedent, gate 6d); (b) change
the field to `"1-27"` — breaks ruling 27's "index label verbatim" and the breadcrumb then disagrees with the index. **RECOMMENDATION: (a).**
XII–XIX labels are re-read by each chunk against its own last address (already the practice).

### A8 (items 4, 8) — marginal quaestiones

By marginale, from each chunk's `### Marginal quaestiones` table (present in all ten, ruling 39): c3 **4** · c4 **1** · c5 **2** · c6 **4** ·
c7 **5** · c8 **3** · c9 **0** · c10 **0** · c11 **3** · c12 **3** = **25** in pp. 125–191 (38 in pp. 107–191 with c1 9, c2 4).
Item 4: c7 p. 159 L *Sed, si omnia potest… Dicendum est…* — no surviving marginale (binding margin cut, ink profile zero) — not
counted. Item 8: c8 p. 162's `Quaestio 1.` / `Quaestio 2.` count as two — **and they were not the work's first numbered pair**
(c1 p. 112 R / p. 116 L, c6 p. 146 R `Quaestio 1`/`2` precede; B4). **RECOMMENDATION: keep both conventions as built** (count what is
printed; an unlabelled pair is recorded in Notes, not counted). 0 lines.

### A9 (new) — one *disciplina* site

*disciplina* → "discipline" at **45 of 46** body sites (c3 6 · c6 12 · c7 5 · c8 10 · c9 2 · c10 1 · c11 4 · c12 5). The exception: c6
Sap. 6:27 lemma *accipite disciplinam* → "*receive therefore instruction* (*disciplinam*), that is, wisdom", the Douay kept because
the gloss equates it with *sapientia*. c11 had adjusted Douay to "discipline" at all six of its sites. **RECOMMENDATION: decline
(ruling 42: one site, no ruling earned)**; optional conform = 1 line.

---

## ▶ B. CONVENTION DEFECTS

### B1 (item 13) — `tr-doctrina`: three chunks owe it

**Verified the convention requires it:** ruling 11 — *"Four notes written, **one per chunk carrying the word**, because notes do not
reach across chunks"* — and c3 wrote one for an **apparatus-only** site (Rabanus's *germina doctrinarum*). Census:

| chunk | *doctrina* sites (body + app La) | English | note |
|---|---|---|---|
| c3 | 0+1 | teachings | ✓ |
| c4 | 3+1 | teaching / teachings | ✓ |
| **c6** | **1+1** — p. 150 *doctrinae manifestationem*; p. 150 n. 11 Rabanus *quorum doctrina sanitas est orbis* | "teaching"; "doctrine" | **✗** (c6's Notes say one site) |
| **c7** | **0+1** — p. 154 n. 3 Cicero *doctrinam rerum honestarum* | "the teaching of honourable things" | **✗ — not on the running list** |
| **c8** | **2+2** — p. 160 Ecclus. 6:18 *excipe doctrinam*; p. 164 Jerome *doctrina Pythagorae*; p. 164 n. 2 *quorum doctrina*; p. 165 n. 7 *Quintum est doctrina sive praedicatio* | Douay "instruction"; "teaching" ×3 | **✗** (running list says two) |
| c10 | 1 (Prov. 1:7) | Douay "instruction" | ✓ (admits "instruction") |
| c11 | 1 | teaching | ✓ |
| c5, c9, c12 | 0 | — | none owed |

**Decisive sentence for the note's content:** c8 p. 165 n. 7 *Quartum est studium… **Quintum est doctrina sive praedicatio*** →
"The fifth is **teaching** or preaching". "Instruction" (c8 Ecclus. 6:18, c10 Prov. 1:7) is the quotation branch of the
*intelligentia* rule — Douay kept inside a quotation nothing leans on — and c10's note already says so. **RECOMMENDATION: write the
three notes (c6, c7, c8), English-only in `## Apparatus`, c8's covering "instruction"; ratify "instruction" as the quotation branch.
Mechanical as a class, per-site in wording.** 3 notes, 0 text lines.

### B2 (new) — `tr-studium` owed in c8, and a register choice inside it

c8 carries *studium* **7 body + 1 app** with no note; every earlier Sapientiae chunk carrying the word wrote one (prooem, c1, c6;
c3–c5, c7, c9–c12 carry none). English: body **"zeal" ×5** (*ex studio inveniendi* "the zeal of finding", *studio lectionis et
orationis* "the zeal of reading and of prayer", *ex studio quaerendi sapientiam* ×2, *mentis proposito et studio*), *studiose* →
"studiously", and p. 165 n. 7 *Quartum est studium* → "**study**". The prooem/c1/c6 notes **keep one root, "study"**, precisely
because the work's exhortation is *ad studium et amorem sapientiae*; c8's heading *Tertio idem ostenditur ex **studio** quaerendi
sapientiam* is that same exhortation's third proof.

| option | cost |
|---|---|
| (a) keep "zeal", add a `tr-studium` saying why (contextual under the dikaisune rule) | 1 note; the root breaks against prooem/c1/c6 inside one argument of Part II |
| **(b) conform to "study"** + note | 5 English lines + 1 note; "the study of finding/seeking her" reads stiffer but keeps the work's one root |

**RECOMMENDATION: (b)**, on the prooem note's own reasoning; (a) is defensible. Either way the note is owed. Per-site.

### B3 (items 9, 20) — the index table

Tested over all eleven in-scope chapter openings, the index page = **the page of `(Vers. 1.)`** in 11 of 11; = the heading page in
9 of 11. The two that discriminate: **Cap. VIII** (heading p. 159 ~0.65, Vers. 1 p. 160, index **160**) and **Cap. XIII** (191 / 192,
index **192**). ⚠ VIII had already decided item 20's either/or before c12 — "indistinguishable until here" was not true. **Conclusion:
the index keys a chapter to its first verse-address; not a slip.** Owed: `manual-review/sapientiae-pilot-scouting.md` l. 28 still
reads `Cap. X … 174` (printed `171`). XIV–XIX can only be re-read on idx-678 (not on disk); each chunk already re-reads its own line.
**RECOMMENDATION: correct the X line; adopt "index page = Vers. 1 page; the heading may stand on the leaf before" as the end-prediction
rule for c13–c19.** 1 doc line.

### B4 (new) — documentation drift in the carry-list
Item 8 "the work's first NUMBERED marginal quaestiones" (false: c1, c6 first) · item 2 "printed cleanly (3×)" (one site, read at 3×) ·
c6 Notes "*doctrina* (one…)" (two) · item 20 "indistinguishable until here" (VIII). Correct in the next resume block; chunk Notes only on Wilson's word.

---

## ▶ C. RESOLVER / TOOL ARTEFACTS (ruling 40 — logged, never edited)

### C1 ⭐ — `ibid. C, V` loses its own coordinates (items 5, 7, 14, 19, 21 are all this one rule)

**Mechanism (read in the code):** `resolve_anaphora()` (`tools/build-citations.py` ~l. 763) copies the antecedent's
`normalized_target`, `confidence` and `resolution` wholesale; the `ibid.` record's `raw_text` is just `ibid.`, so the chapter/verse
printed after it is never read. ⚠ **It is not a cross-note problem**: c4 p. 132 n. 2 `Psalm. 141, 8; ibid. 41, 3.` emits Ps 141:8
**twice** and loses Ps 41:3; c11 p. 180 n. 4 `Psalm. 77, 42; ibid. v. 11.` emits 77:42 twice. Cross-note binding is the worse sub-case
(wrong BOOK), not the cause.

**In scope:** 34 scripture anaphors in apparatus — **11 bind within the note (right book, wrong verse), 23 across notes** — of which
**30 print their own coordinates and all 30 are filed at the antecedent's** (confidence A). Known wrong-book: c12 p. 186 n. 2 (Gen
6:3 → Ps 73:12), p. 187 n. 5 (Deut 32:39 → Job 9:13). Non-scripture `ibid.` filed as scripture: c11 p. 180 n. 5 (*Moralia* → Ps 77:42),
**c6 p. 146 n. 11 `ibid. Comment. dub. 6` → Apoc 20:12 (new)**. False crossrefs: c10 p. 177 n. 4 → II:d40, c12 p. 185 n. 2 → c1
(loses Gen 26:3, 28:13), c8 p. 164 n. 11 → III d27 (loses Ecclus 24:27, 29), c7 p. 157 n. 13 → IV d45/46 page-multi.

**Corpus blast radius (measured):** **251 scripture records print `ibid. C, V`/`ibid. v. N` and 1 is honoured** — Vol I 4 · II 24 ·
III 23 · IV 49 · V 88 · VI 63; Vols I–V are deployed. A fix changes ~250 scripture-index entries (each moves to the verse actually
printed) and removes the false crossref lines from Cited-by.

| option | cost |
|---|---|
| (a) park (ruling 14 status quo) | 0 now; the p. 235 deploy ships ~250 wrong verses at confidence A, ~65 in this volume |
| **(b) scoped job before the p. 235 deploy:** capture the coordinates after `ibid.`; take the antecedent's BOOK and the ibid's own C:V; when the antecedent is non-scripture or Sentences, keep looking back for a scripture locus (or the body-ordinal join through the anchor) | one tool change + before/after ledger diff reviewed once; the deploy regenerates the index anyway |
| (c) fix now, inside this gate | refused — the gate is read-only and the diff needs its own review |

**RECOMMENDATION: (b).** Mechanical (tool), not per-site; zero chunk edits.

### C2–C5 — park
- **C2 printed slips** (ruling 37 in the ledger): c3 p. 126 n. 1 Job 24:19 (A, for 5:19) · c5 body `ad Corinthios duodecimo` + `Vers. 30`
  → Cor* 12:30 (B, for I Cor 12:31) · c11 body `Proverbiorum decimo sexto` → Prov 16 (C, for 24:16) · (c1 Job 6:2). A small override
  table keyed chunk + label; do it inside C1's job.
- **C3 chain continuations:** c9 p. 171 n. 4 `III. Sent. d. 25. a. 1. q. 2. et a. 2. q. 1. seqq.` (second locus lost) · c11 p. 181 n. 5
  `d. 12. a. 1. q. 1-3; a. 2. q. 2.` (only q. 1; `d. 13. a. 1. q. 1.` is emitted).
- **C4 unparsed named units:** c8 p. 166 n. 1 `supra Prooemium, n. 6` · c12 p. 190 n. 6 `Cfr. supra 11, 16.` · c12 p. 187 n. 1
  `Comment. in Eccle. 1; 15. Quaest. 2.` (only `pag. 19` resolves) · c7 p. 155 n. 7 `tom. V. pag. 203 et 403` (403 dropped) and
  p. 158 n. 16 `Collat. in Hexaëm., collat. 12` · c7 p. 157 n. 13 / c6 p. 146 n. 11 `lit. Magistri, d. VIII / d. XXXIX` (roman *d.*) ·
  c10 p. 177 n. 3 `II. Sent. d. 40, dub. 2` (distinctio only). Body: c12 *item ibidem* after Deut. 32 → 32:35 (B, for 32:39).
- **C5 owner-blind `page-multi`:** in scope `supra pag. 171, nota 5` (c10's), `pag. 166, nota 9`/`10` (c9's), `pag. 184, nota 4`
  (c11's) each list both chunks though the nota number decides; **1,178 such records corpus-wide**. Right chunk always in the set — an
  improvement, not a defect.

---

## ▶ REGISTER CENSUS (rendered regions; body+app Latin → English)

| term | c3 | c4 | c5 | c6 | c7 | c8 | c9 | c10 | c11 | c12 | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *doctrina* / note | 0+1 ✓ | 3+1 ✓ | 0 | 1+1 **✗** | 0+1 **✗** | 2+2 **✗** | 0 | 1 ✓ | 1 ✓ | 0 | **B1** |
| *studium* / note | 0 | 0 | 0 | 2 ✓ | 0 | 7+1 **✗** | 0 | 0 | 0 | 0 | **B2** |
| *lumen* / note | 0 | 0 | 4+2 ✓ | 1 ✓ | 5+3 ✓ | (*luminaria*) | 0 | 0 | 0 | 0 | ✓ A3 |
| *lux* → light | 3 | 0 | 8+1 | 12+1 | 22+4 | 1 | 2 | 2+1 | 2 | 2 | ✓ |
| *vaca-* / note | 0 | 0 | 1+1 ✓ | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ✓ never "rest" |
| *punitio* · *poena* · *supplicium* | 3·12·2 | 0·5+1·0 | 0·6+2·4 | 1·5·2 | 0·1·0 | 0 | 0 | 5·2·1 | 20+1·18+3·0 | 11·10+1·0 | all → punishment (**A1**) |
| *intellect-* / bare "intellect" | 1/0 | 3/0 | 2/0 | 3/0 | 7/0 | 4/0 | 10+1/0 | 0 | 0 | 1/0 | ✓ **zero bare** |
| *intelligentia* → intelligence | 1→1 | 0 | 5→5 | 0 | 6→6 | 1→1 | 2→2 | 3 (Douay in quot.) | 0 | 0 | ✓ |
| *impius* → impious | 13+1 | 16+1 | 17+3 | 1+4 | 0 | 1 | 0 | 3 | 6+1 | 4 | ✓ **61+10 = 61+10** |
| *iniquus* → wicked/iniquity | 5+2 | 10+1 | 7+1 | 0 | 1 | 1 | 0 | 0 | 6+4 | 9+1 | ✓ (ruling 42 stands) |
| *disciplina* → discipline | 6 | 0 | 0 | 13 (12 + 1 "instruction") | 5 | 10 | 2 | 1 | 4 | 5 | A9 |
| purity triple | *munditia* 1 | *puritas* 1 | 0 | 0 | *puritas* 4, *munditia* 1 | *munditia* 3 | 0 | 0 | 0 | 0 | *pudicitia* 0 body; applied |
| *quies/requies* → rest | 2+1 | 1 | 0 | 1 | 0 | 1+1 | 1 | 0 | 1+1 | 0 | ✓ |
| English `**Contra:**`/`**Sed contra:**` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ✓ ruling 41 (13 "On the contrary:") |
| *idol-* / *simulacrum* | 1 | 0 | 0 | 0 | 0 | 0+1 | 0 | 0 | 3 | 1+1 | ruling 32; XIII–XV will load it |

`tr-` notes in scope (9): c3 doctrina · c4 doctrina · c5 vacare, lumen · c6 studium, lumen · c7 lumen · c10 doctrina · c11 doctrina.
