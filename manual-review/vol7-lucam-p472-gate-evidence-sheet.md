# Vol VII *Lucam* p. 472 GATE (ruling 14: close of c. 18): EVIDENCE SHEET

Compiled 2026-11-16 by a read-only agent (Opus, on Wilson's authorization). **Nothing here is settled. Wilson rules off this
sheet.** No file under `vol7/`, `tools/`, `site/`, `index/`, the manifest, the ruling file or the resume note was edited.
Nothing was committed, pushed or stashed. No plate was read: the one item that might have needed one (R-1, p. 410) was
settled from the Vol VII text layer.

**Scope: the 19 chunks of pp. 381–472** (`bon-luc-c15-v1-7` → `bon-luc-c18-v28-43`; XV 5 · XVI 4 · XVII 5 · XVIII 5).
Where a register question needs it, the census runs over **all 101 *Lucam* chunks (pp. 3–472)**, and over Vols V–VI where
a corpus precedent decides (*supplicium*: Vol VI ruling 59; *intellectus / affectus*: Vol VI ruling 101). Docket source:
the consolidated items 1–31 (A–H), D-1..D-7 and the tool items T-a..T-f at the top of `next-session-resume.md`
(ll. 19–74), and each chunk's `## Notes` (builders' items (1)–(290)). Rulings 1–92 (`manual-review/vol7-pilot-setup.md`)
and the repo `CLAUDE.md` tests bind (the *lux / lumen* test ~ll. 1288–1311; the house-word list ~l. 3502). The passes
1–3 draft (`manual-review/vol7-lucam-p472-gate-passes-draft.md`, uncommitted, read not edited) is folded in: its
**N-1, N-2, N-3 are F2, F3, F4 below, its R-1 is F10, its O-1 is in § 1**. Build figure at the last chunk: **2,418 / 2,418**.

⛔ **Every census is taken over the RENDERED region only:** the `## Latin` and `## English` bodies and the `**La.**` /
`**En.**` halves of `## Apparatus`. Frontmatter, `## Notes` and the `tr-` definitions are excluded. "¶" is the Quaracchi
paragraph in which the site stands (an un-numbered continuation belongs to the ¶ it continues, ruling 5); "p. N n. M" is
an apparatus entry. Scripts: scratchpad `g472/` (the p. 381 sheet's `regions.py`, `cen.py`, `ctx.py`, `align.py`,
`grepl.py`, `show.py`, `drc.py`, `reg.py`, re-scoped to Cap. XV–XVIII; `reg.py` now runs **107** Latin → English register
pairs over the 19 chunks and lists every shortfall, each read by eye; `enline.py` maps a region to its file line). Douay
checked against `~/douay-glossa/raw/DRC.json`. **Lines** in the cost columns are lines of the chunk file (every body
paragraph line, every apparatus half and every `tr-` definition is one line; a frontmatter field is one line).

---

## ⚠ FOUND BY THE SHEET (builder's claim wrong, a defect, or a fact not on the docket)

| # | chunk / site | what is wrong | ⭐ fix | lines |
|---|---|---|---|---|
| **F1** | the interval's 19 *supplicium* sites; the register line every builder carried | **The register line "*supplicium* 'punishment' / 'torment' by sense (ruling 87; never 'penalty')" is not what binds.** `CLAUDE.md:3502` reads ***poena* → "punishment"; *supplicium* → "penalty" (Vol VI rulings 20, 101, 109)**, and **Vol VI ruling 59** made it so *because* one English word for both produced "the punishment of punishment", and refused "torment" because it is *tormentum* / *cruciatus*'s (`vol6-pilot-setup.md` ll. 346–356). Ruling 11 carries the Vol V–VI register into Luke. **Ruling 87 ratified "the *supplicium* split" as one item of a batch of ruling-20 / 28 splits; it says nothing about "never penalty"**, and the p. 381 docket did not put `CLAUDE.md:3502` or Sap ruling 59 before Wilson. Census, all 101 (45 sites): **"penalty" 10** (all in Cap. I–VII), **"punishment" 25**, **"torment" 10**. In the interval: "punishment" 17, "torment" 2, "penalty" 0; and *poena* "punishment" stands beside *supplicium* "punishment" in one sentence or one sibling pair at `c16-v22-31` ¶ 58 (Gregory: *in suppliciis amplius torqueantur … illorum poenam*), `c17-v1-4` ¶ 5, `c18-v9-14` ¶ 22, and the `c17-v20-30` ¶ 45 / ¶ 49 triads (item 14's collision). Its "torment" collides with `c16-v22-31`'s *tormenta* / *cruciari* "torments / tormented" (¶¶ 48, 49, 55, 58) | **§ 3 below (item 14)**: ⭐ restore the house rule, *supplicium* → "penalty", at the 19 interval sites and the 16 pre-interval non-"penalty" sites | **16** (+ **~10** pre-interval) |
| **F2** (= passes **N-1**) | `c16-v1-8` p. 405 n. 3 **En.** (l. 252) · pre-interval `c12-v49-59` ¶ 86 (l. 149), ¶ 87 (l. 151), p. 335 n. 9 **En.** (l. 453), p. 335 n. 13 **En.** (l. 469) · `c1-v18-25` p. 18 n. 6 **En.** (l. 134) | ***poena* → "penalty / penalties" against `CLAUDE.md:3502`.** The Gloss's *ut poenas evitem* "that I may avoid the **penalties**": the interval's only "penalt-" in the rendered English, and the exact word D-4 conformed away at `c17-v20-30`. **Census, all 101, *poena* rendered "penalt-" with no *supplicium* / *poenalitas* in the region: 6 regions** — this one; `c12-v49-59` ¶¶ 86–87 and its two notes (Bede's *reddit poenas*, Augustine's *terminum poenae*, the Gloss's *poenam exigit*, *poenas … luit*: "penalty" ×6, beside the same paragraph's *supplicia* "torments" — the two words exactly inverted against the house rule; passed the p. 381 gate unseen); `c1-v18-25` p. 18 n. 6 *poenam luit* "paid the penalty". Not on the docket | "that I may avoid the **punishments**" · `c12-v49-59`: "exact the **punishment** for the fault … that **punishment** is irremediable" · "He pays the **punishments** for his sins … not a term of the **punishment**" · p. 335 n. 9 "exacts the **punishment**" · n. 13 "pays the everlasting **punishments**" · p. 18 n. 6 "paid the **punishment**" (stiff, as the rule is; the idiom alternative is to record it) | **1** (+ **5** pre-interval) |
| **F3** (= passes **N-2**) | `c16-v19-22` p. 417 n. 12 **En.** (l. 242) | **Chrysostom's *ut magnitudo poenarum faceret magnitudinem misericordiae* → "the greatness of the pains"** (Lazarus's sores), undisclosed. The house row admits no sense split for *poena*, **but the work already has one, ratified**: `c13-v22-30` ¶¶ 59–60 *poena sensus / poena damni* "the pain of sense / the pain of loss" (the scholastic term), "pains" for *hae duae poenae corporales*. All 101: *poena* → "pain(s)" in these three regions only | ⭐ **keep "pains"; record as a disclosed sense exception** in `c16-v19-22`'s Notes (bodily pain, no penal sense; the `c13-v22-30` precedent). Alternative "punishments" (1 line) makes Lazarus punished | **0** (doc) |
| **F4** (= passes **N-3**) | `c18-v18-27` ¶ 44 (l. 118) | **Bernard's *Non sic, impie, non sic ingredieris* → "Not so, wicked one"**, a Father's prose, against ruling 86 (*impietas / impius* "impiety / impious" in prose; the Douay word only inside a verse). Interval: 72 *impi-* regions; every other prose site "impious / impiety". Undisclosed | "Not so, **impious one**, not so shalt thou go in" | **1** |
| **F5** | `c18-v15-17` (item 12); work-wide *puer* | **The builder read ruling 54 as a general prose rule ("*puer* 'boy' in prose"); the work does not.** Ruling 54 was ratified on the centurion's *puer* (`c7-v1-16`, a servant; the p. 188 sheet's reason: "keeps *puer* off *servus*"). **Census of *puer* outside `c18-v15-17`, all 101: "child(ren)" ~60 regions** (the Baptist and the child Jesus throughout Cap. I–II; Luke 9:47–48 `c9-v46-56` ¶¶ 87–88 "Taking a child … Israel was a child"; `c11-v5-13` ¶ 21 Luke 11:7 "my children" and p. 283 n. 7, the etymology note that p. 460 n. 2 cites, *pueri* ("children") *a puritate*; `c18-v1-8` ¶ 8 Luke 11:7 "my children") · "boy(s)" ~20 (the centurion's boy, Luke 9:38–42 the epileptic boy, the servants of Luke 12:45) · "servant" ~15. So `c18-v15-17` creates cross-chunk splits the docket half-lists: **Luke 11:7** "my boys" against "my children" at **two** chunks (`c11-v5-13`, and `c18-v1-8` inside the interval: passes O-1); **Osee 11:1** "Israel was a boy" / "a child" (`c9-v46-56` ¶ 87); **I Cor. 14:20** "Do not become boys in sense" / "In malice be children" (`c1-v67-80` ¶ 136); **Luke 1:76** "Thou boy, Prophet" / "child" (`c1-v67-80`) | **§ 1 below**: ⭐ *puer* = a child → "child(ren)" through `c18-v15-17` | **12** |
| **F6** | `c15-v1-7` ¶ 1 (l. 98), ¶ 5 (l. 109) · pre-interval `c6-v1-11` ¶ 6 (l. 119), `c6-v39-49` ¶ 99 (l. 126), ¶ 105 (l. 142), `c9-v1-9` ¶ 7 (l. 124), `c9-v57-62` ¶¶ 102–105 (ll. 66, 68, 70, 72) | ***simulatio* → "simulation" against the house word "dissembling"** ratified at the p. 381 gate (ruling 88, item 17 [7]: *simulatio* "dissembling", 25 / 25 in pp. 288–381). ¶ 1's divisio member *simulatio aequitatis iustitiae* "the simulation of the equity of justice", ¶ 5 its echo. **All 101:** 38 *simulatio* La; "dissembling" at the 25 of Cap. XI–XIV; **"simulation" 10** (c6-v39-49 ×2, c9-v1-9, c9-v57-62 ×5, c15-v1-7 ×2), "pretence" 2 (c6-v1-11 ¶ 6 *simulatione hypocrisis*), Rom. 12:9 the Douay's "without dissimulation" (`c6-v27-31` ¶ 65, a verse: stands). Not on the docket | ¶ 1 "*the dissembling of the equity of justice*"; ¶ 5 "*the dissembling of the equity of justice* … Whence by dissembling equity" (the gerund follows); pre-interval: "the dissembling of hypocrisy" ×2, "a deceptive dissembling", "the deceptive dissembling", "the doubleness of dissembling", "the dissembling of simplicity" ×2, "by dissembling", "the outward / inward dissembling" | **2** (+ **8** pre-interval) |
| **F7** | `c16-v9-18` ¶ 17 (l. 124), ¶ 19 (l. 128) | ***infidelitas* → "infidelity" ×3 against ruling 71** (*infidelitas* "faithlessness", kept off *incredulitas* "unbelief"). Set against *fidelitas* "fidelity" of the steward. **All 101:** 18 *infidelitas*; "faithlessness" at every site but these three (`c9-v37-45`, `c10-v4-16`, `c11-v5-13`, `c11-v27-32`, `c18-v1-8` ¶ 12 and p. 452 n. 5 inside the interval). The builder's register line ("*infidelitas* 'infidelity'") is the error. Not on the docket | ¶ 17 "on the contrary, faithlessness about the least things sets down faithlessness about greater ones"; ¶ 19 "the peril of faithlessness" ("fidelity / faithlessness" keeps the antonymy) | **2** |
| **F8** | pre-interval `c1-v39-45` ¶ 71 (l. 86), `c1-v46-56` ¶ 96 (l. 110) | **The locative formula *in intellectu … in affectu* rendered "in the understanding … in (the) affection"**, against ruling 32's own row ("in the intellect … in the affection"). Both are in the p. 88 interval, where the row was written; passed three gates. Every other locative-formula site in the 101 is "intellect" (`c2-v40-52` ¶ 110, `c6-v39-49` ¶¶ 103, 107, `c7-v1-16` ¶ 20, `c11-v1-4` ¶ 9, `c12-v1-7` ¶ 5, `c18-v9-14` ¶ 26). Found by § 6's census | "*the certification of truth* in the intellect and *the showing of charity* in the affection"; "proud in the intellect through *presumption* and in the affection" | **(2** pre-interval) |
| **F9** | `c17-v11-19` `[^tr-praeceptor]` def (l. 347) | The note says "Quaracchi sets the word in lower case here, **and the Douay prints 'Jesus, master'**". `DRC.json` Luke 17:13: "Jesus, **Master**, have mercy on us". The claim about the Douay is wrong (the capital needs no defence: the Douay has it) | strike "and the Douay prints 'Jesus, master'"; the sentence then reads "Quaracchi sets the word in lower case here; the capital follows the Douay and the earlier sites." | **1** |
| **F10** (= passes **R-1**) | D-5 / item 15 [88] | **Settled without the plate: the site is ¶ 21, and the docket, the resume and `c16-v9-18`'s item (88) are wrong to say ¶ 22.** The file has *invitando ad pietatem divinam* in ¶ 21's un-numbered continuation (La l. 59, En l. 136), before `22.` at La l. 61 / En l. 138; **the Vol VII text layer agrees** (`raw/doctorisseraphic07bona_djvu.txt` L68829–68831: *… invitando ad pietatem divinam. Unde Glossa … non ut servi ». ⏎ 22. Secundo quantum ad assertionem reprobationis*). The file is right | amend item (88)'s "¶ 22" → "¶ 21" in place (struck wording kept); gate record says ¶ 21 | **0** (doc) |
| **F11** | `c15-v1-7` p. 386 n. 8 | **A thirteenth wrong anaphor edge, not in T-b's twelve:** *ex Gregor., loc. cit. n. 15* (Gregory's homily, via the Gloss) → `Isai 49:13`, the same note's verse (`index/citations.tsv`: `anaphor->apparatus-explicit`, antecedent *Isai. 49, 13*). The p. 393 n. 7 / p. 405 n. 2 shape | add to J-1 (§ T) | 0 text |
| **F12** | T-d coverage | **The accusative *notam M* (J-4) stands at 10 interval sites, not the docket's 2:** p. 382 n. 2 *supra pag. 76, notam 8 … pag. 129, notam 4* (both page-only, no anchor), p. 418 n. 14 *tom. VI. pag. 126, notam 1*, p. 434 n. 3 *supra pag. 379, notam 4*, p. 440 n. 10 *tom. V. pag. 258, notam 2* (`page-multi`), p. 448 n. 9 *tom. IV. pag. 368, notam 4*, p. 463 n. 1 *tom. II. pag. 697, notam 3* (`page-multi`) and *tom. III. pag. 95, notam 10*, p. 466 n. 2 *supra pag. 228, notam 8 … pag. 380, notam 12*. **And p. 399 n. 1 *pag. 295, nota. 4.*** (the point after *nota*; item 22 lists it as a slip) resolves `page-multi` (`c11-v14-26+c11-v27-32`) for want of the note: J-5. **Direction screen (J-12) over the interval's 159 crossref records: 0 slips**; p. 405 n. 10 *supra pag. 403, nota 20* resolves to the chunk with no anchor (no wrong edge; the J-12 row is still owed, § E) | add to J-4 / J-5 (§ T) | 0 text |
| **F13** | the *mirus* adjective, work-wide | **Record, no edit:** *mirus / mira / miro modo* is "wonderful" at ~17 regions and "marvellous" at ~14 in the 101 (interval: "wonderful" `c15-v25-32` ¶ 51, `c18-v1-8` ¶ 9, `c18-v9-14` ¶ 24; "marvellous" `c16-v19-22` ¶ 43, `c17-v5-10` ¶ 15, `c17-v11-19` ¶ 29 + p. 435 n. 7, `c18-v28-43` ¶¶ 53, 54). Ruling 32's row covers *admirabilis* · *mirabilis* · *mirari* only; nothing is broken. If Wilson wants a row, "marvellous" (the *mirabilis* root) would be the conform, ~17 lines | none (record); a row is Wilson's option | doc |
| **F14** | item 13 / D-2 framing | **The Ps. 35:10 "inconsistency" is the test working, not a defect** (§ 2): both sites are right under the written test. Ruling 78's framing (a docket "defect" that the test clears) | none (record) | doc |

**Also noted, no edit proposed.** *largitas* "largess" holds at every noun site; the 10 `reg.py` shortfalls are *largiri*
"bestow" / *largitio* "bestowal" (the verb). *dilectio*'s 4 shortfalls are Douay verses (Ecclus. 24:24, 7:39, 25:16, Cant.
8:7 "love"; ruling 64's verse clause). *Ducange* (item 27 / D-6) is the printed line-end break *Du-|cange*, the **En.** half
already "Du Cange" (§ G).

---

## THE FIVE THAT MOST NEED WILSON'S RULING

### 1. Ruling 54's *puer* in the children passage (`c18-v15-17`, item 12 [239]) — ⭐ **"child(ren)"; the three "servant" verses keep the Douay** (12 lines)

**Ruling 54's own words** (p. 188 gate): "*puer* 'boy' (prose) / 'servant' (the Douay's verses) … RATIFIED", on item 39 of the
p. 188 sheet, whose whole evidence is the centurion's *puer* in `c7-v1-16` (¶ 1 *curatio pueri morituri*, the lemma 7:7
*sanabitur puer meus* "my servant"), and whose reason is: "**The split keeps *puer* off *servus* in the prose**" (¶ 16
*curationem servi*). **Its scope is the *puer* who is a servant.** It was never put to a *puer* who is a child, and the work
had by then already rendered that *puer* "child" some sixty times (F5). Nothing in rulings 1–92 says otherwise.

**The pericope.** ¶¶ 27–33 (pp. 457–460) carry three Latin words for the young: *infantes* (the lemma Luke 18:15, the
Douay's "infants"), *parvuli* ("little ones"; the Douay's "little children" at Matt. 18:3, "little child" at Matt. 18:5),
and *pueri* (Luke 18:16–17 and ~45 sites). ¶ 32 glosses *ut puer* as *esse sicut puerum, id est purum et parvum*, and
p. 460 n. 2 sends the reader to the etymology note p. 283 n. 7 (*pueri a puritate*), which `c11-v5-13` renders "*pueri*
('children') from *puritas*". ¶ 33 sets *parvulis* against *pueris, qui sunt puri*.

**Census (`c18-v15-17`, rendered region): 66 *puer* La / 56 "boy(s)" En** on 6 body lines (ll. 61, 63, 65, 67, 70, 72)
and 6 apparatus **En.** lines (ll. 92, 132, 144, 192, 208, 212); the 10 others are the three "servant" verses, Luke 1:54
"his child", three Latin-italic *puer* where the word is named, Luke 1:73 kept Latin, and Gen. 19:4 (that one is
`c17-v20-30`). **Of the ~26 verses adjusted to "boy", the Douay says "child(ren)" at ~20** (Luke 18:16, 18:17, Matt. 21:15,
Ps. 112:1, I Cor. 14:20, Prov. 20:11, 22:15, 23:13, 29:15, Wis. 8:19, 12:25, Eccles. 4:13, 10:16, Jer. 1:6–7, Luke 1:76,
Mark 7:28, Dan. 1:4, 1:17, I Kings 2:18, Osee 11:1), "boy" at two (Gen. 37:2 "being but a boy", Dan. 13:45 "a young
boy"), "young men / youths" at Isa. 40:30, I Kings 21:5, "men children" at Matt. 2:16.

| alternative | sites | cost |
|---|---|---|
| (a) Ratify as built: "boy(s)" through the pericope, the lemma included | 0 | **0 lines.** "Suffer boys to come to me" at a famous verse (ruling 27: no famous-verse exception, so this is allowed); **keeps four cross-chunk splits** (Luke 11:7 ×2 chunks, Osee 11:1, I Cor. 14:20, Luke 1:76) and imputes sex to Luke's *infantes* |
| **(b) *puer* = a child → "child(ren)" through the pericope**; the ~20 verses return to their Douay "child(ren)", the lean now served by the Douay's own word; Gen. 37:2 / Dan. 13:45 / Isa. 40:30 / I Kings 21:5 / Matt. 2:16 adjusted to "child(ren)" (ruling 20: ¶¶ 29–31 lean); *infantes* "infants", *parvuli* "little ones" unchanged; ¶ 32 "as a child, that is, pure and little"; ¶ 33 "to *little ones* … and also to *children*, who are pure" | ~56 | **12 lines** (6 body, 6 apparatus **En.**, incl. p. 459 n. 12's variants *puerum illum* ("that child") etc. and p. 460 n. 2 *puer* ("child")) + Notes item (239) answered. Removes all four cross-chunk splits; matches p. 283 n. 7 |
| (c) "child" in the lemma only, "boy" in the prose | 2 | 1 line; the prose glossing *ut puer* would name a word the lemma does not show (ruling 20's point) |

**The three "servant" verses** (Job 29:5 *pueri mei*, Ps. 104:42 *Abraham, puerum suum*, Matt. 12:18 *puer meus*): the Douay
reads "servants / servant" at all three, and each is the *puer*-as-servant of ruling 54's own verse half. ¶ 31's argument
(*vocatur Abraham puer in Scriptura … Christus autem puer dicitur*) is already carried by the Latin italic *puer* the builder
kept (ruling 35's "a name cited as a word"). Adjusting them to "child" or "boy" would make Abraham and Christ "children"
against the verses' sense. **⭐ keep the Douay at all three** (0 lines). Luke 1:54 "Israel his child" stays with
`c1-v46-56` ¶ 99 (ruling 28).

**⭐ (b), and a clarifying sentence for ruling 54:** "*puer* the servant 'boy' in prose / 'servant' in the Douay's verses
(`c7-v1-16`, Luke 12:45); *puer* the child 'child(ren)', the work's ~60 sites from Cap. I on (`c18-v15-17` conformed at the
p. 472 gate)." **This needs Wilson's own call:** "boys" is the ruling as the builder read it; "children" is the work's
record and the Douay's word.

### 2. Ps. 35:10 at `c16-v19-22` ("lumen") and `c17-v31-37` ("light"); John 8:12 at `c18-v28-43` (item 13 / D-2 [99, 184, 271]) — ⭐ **ratify the split; John 8:12 stays exempt** (0 lines)

**The test** (CLAUDE.md ~l. 1292, the *mysterio Trinitatis* shakedown gate, Wilson 2026-09-06; ruling 27 carries it; ruling
50 fixes its unit as "the expository unit the verse is adduced in"): *a received scriptural wording is exempt only where the
verse is quoted AS A VERSE and no surrounding body prose leans on the term.* The CLAUDE.md line "Ps. 35:10 … keeps 'In
thy light we shall see light' … do not 'fix' it" is the test's application to its Vol V site (`bon-qsc-q4`); by ruling 78's
reasoning it decides that site only.

| site | the unit | does the prose lean on *lumen*? | test | as built |
|---|---|---|---|---|
| `c16-v19-22` ¶ 39 | the *splendida epulatio* of the blessed | **yes:** *venit ex fonte luminis sempiterni*, built from the verse's *fons vitae … in lumine tuo* one clause before it | not exempt | "in thy lumen we shall see lumen" + `tr-lumen` ✓ |
| `c17-v31-37` ¶ 62 | the four acts of the soul (*desiderium, contuitum, gustum, amorem*), each proved by a Psalm | **no:** ¶ 62 holds no *lumen / lux / illumin-* outside the verse; the verse is adduced for *contuitum* | **exempt** | "in thy light we shall see light" ✓ |
| `c18-v28-43` ¶ 66 John 8:12 *Ego sum lux mundi … habebit lumen vitae* | ¶¶ 65–66, the fourth member *integritas sanitatis*, ¶ 66 its *sequebatur illum* | **no:** ¶¶ 65–66 hold no *lumen* outside the verse; it is adduced for the *following* of Christ | **exempt** (if the unit is the member) | "the light of the world … the light of life" ✓ |

**Census, all 101:** Ps. 35:10 occurs at these two sites only; John 8:12 also at `c3-v21-22` ¶ 52 (*Ego sum lux mundi*, no
*lumen*: "light"). Ps. 35:10 is a ruling-28 split by design (the Isa. 60:1 shape recorded under ruling 50).

**The unit for John 8:12.** Ruling 50's precedent unit was "one argument" (`c5-v17-26` ¶¶ 60–62). The illumination miracle
¶¶ 58–66 is four members (¶ 58's divisio *opportunitas mendicantis, importunitas petentis, liberalitas sanantis, integritas
sanitatis*), each its own argument; the *lumen* that leans (¶ 57 *lumen … suae lucis*, ¶ 58 *ad lumen veritatis*, the
Gloss's ¶¶ 63–64) stands in the first three. The verse itself pairs *lux mundi* / *lumen vitae*, but the test asks about the
prose, not the verse (Rom. 2:19, `c18-v9-14` ¶ 14, *lumen eorum*, exempt under ruling 50 with nothing leaning).

| alternative | cost |
|---|---|
| **(a) Ratify both Ps. 35:10 sites and John 8:12 as built; record the split in both chunks' Notes and the unit (the member, ¶¶ 65–66) in `c18-v28-43`'s** | **0 lines** |
| (b) Ps. 35:10 "lumen" work-wide | 1 line + a `tr-lumen` in `c17-v31-37` (2 lines); a verse-wide exemption *from* the test, against ruling 27 (no famous-verse rule either way), and a new ruling, not a D-item (ruling 78) |
| (c) Ps. 35:10 "light" work-wide | 2 lines in `c16-v19-22` (¶ 39 + its `tr-lumen`); leaves ¶ 39's prose "fountain of eternal lumen" glossing a verse that does not show the word |
| (d) John 8:12 "the lumen of life" (unit = the whole miracle) | 1 line + amend `c18-v28-43`'s `tr-lumen` (2 lines) |

**⭐ (a).**

### 3. *poena* / *supplicium* (item 14 / D-4 [166, 190, 225, 272]) — ⭐ **ratify `e810ccc`; restore *supplicium* → "penalty" (the house rule)** (16 interval lines + ~10 pre-interval)

**`e810ccc` (D-4).** `c17-v20-30` was built with *poena* "penalty" and *supplicium* "punishment", the house rule exactly
inverted; the post-build commit conformed the *poena* sites to "punishment" (¶ 45 *figura, causa, poena*, ¶ 48 ×2, p. 443
n. 1; 16 lines changed in the chunk, 4 in the resume, Notes amended). It applied `CLAUDE.md:3502` correctly. **⭐ ratify**
(the gate's OK after the fact). What it left is item 14's collision: ¶ 45's *poena* and ¶ 49's *supplicium* now share
"punishment".

**The binding rule** (F1): `CLAUDE.md:3502`, from Vol VI ruling 59 (Sap: 24 sites, "penalty" throughout, "torment"
refused by census), ruling 101 N6 (Ioannem), carried into Luke by ruling 11. **Census of *supplicium*, all 101 (45 sites):**

| rendering | sites |
|---|---|
| **"penalty"** (10) | `c1-v57-66` ¶ 114 · `c6-v20-26` ¶ 49 ×4 (*comminationes poenarum sive suppliciorum* "punishments or penalties": the house pair carrying the Latin pair), ¶ 58 · `c6-v27-31` ¶ 64 · `c6-v32-38` ¶ 86, p. 160 n. 4 · `c7-v24-35` ¶ 58 |
| **"punishment"** (25) | `c9-v37-45` ¶ 83 · `c10-v4-16` p. 260 n. 6 · `c13-v1-9` ¶ 1, ¶ 2 ×2 · `c13-v22-30` ¶¶ 48, 59, 63 · **interval 17:** `c16-v22-31` ¶ 47 *locum suppliciorum*, ¶ 48 Gregory *de suo supplicio*, ¶ 54 *praeambulum ad supplicium*, ¶ 58 ×3 · `c17-v1-4` ¶ 1, ¶ 5 · `c17-v20-30` ¶ 49, ¶ 50, ¶ 52 ×3 · `c17-v31-37` ¶ 58, ¶ 59 · `c18-v1-8` p. 452 n. 1 · `c18-v9-14` ¶ 22 |
| **"torment"** (10) | `c12-v1-7` ¶ 8 ×5 · `c12-v49-59` ¶ 87 ×2 · `c14-v16-24` ¶ 49 · **interval 2:** `c18-v28-43` ¶ 52, ¶ 55 (*acerbitas supplicii*, the Passion) |

No *supplicium* in the 101 stands inside a Douay verse (Sap's one quotation exception, Matt. 25:46, does not occur).

| alternative | lines | cost |
|---|---|---|
| **(a) The house rule: *supplicium* → "penalty" at all 35 non-"penalty" sites; *poena* "punishment" untouched** | **16 interval** (`c16-v22-31` ll. 87, 90, 108, 120, 122 · `c17-v1-4` ll. 88, 99 · `c17-v20-30` ll. 154, 158, 164 · `c17-v31-37` ll. 84, 86 · `c18-v1-8` l. 308 · `c18-v9-14` l. 117 · `c18-v28-43` ll. 112, 120) **+ ~10 pre-interval** (`c9-v37-45` ¶ 83, `c10-v4-16` p. 260 n. 6, `c12-v1-7` ¶ 8, `c12-v49-59` ¶ 87, `c13-v1-9` ¶¶ 1–2, `c13-v22-30` ¶¶ 48, 59, 63, `c14-v16-24` ¶ 49) | Item 14's collision disappears: ¶ 45 "the *punishment*" / ¶ 49 "the *penalty*"; Gregory's ¶ 58 "tormented the more in penalties … the punishment of those"; ¶ 52 "the bitterness of the penalty". The Cap. I–VII sites need no edit. Reverses the *supplicium* clause of ruling 87's batch (taken without the house rule on the docket) |
| (b) Ratify the Lucam split (punishment / torment by sense) and write it into ruling 32's table as a Luke exception to `CLAUDE.md:3502` | **10 pre-interval** (the Cap. I–VII "penalty" sites conformed to "punishment") | keeps *poena* / *supplicium* on one word at ≥ 4 interval sites and "torment" on *tormentum*'s ground (`c16-v22-31` ¶¶ 48–58); a cross-volume divergence from Vols V–VI |
| (c) Leave all three renderings | 0 | three words for one Latin word, the Cap. I–VII sites against the rest |

**⭐ (a).** With F2 (*poena* "penalty" ×6 → "punishment") it leaves the work with one word for each Latin word, as Vol VI.
**This needs Wilson's own call** because it re-opens one clause of ruling 87.

### 4. *pietas* (item 15 / D-5 [88, 201, 7, 81, 150, 220, 260]) — ⭐ **ratify the inventory; keep ¶ 21 literal; ratify `tr-pietas` on the adjective** (0 lines)

**Rules:** ruling 12 (*pietas* "piety"), ruling 31 (`tr-pietas` at the first site of any chunk where the *pietas* is God's,
work-wide; human *pietas* no note), ruling 51 (human *pietas* in quotations "piety"), ruling 86 (the review closed; in the
Cap. XV chunks the note names ¶ 1's *impietas / pietas divina / pietas humana* divisio).

**Census, interval:** *pietas / pius / pie / piissimus* **89 La / 89 "piety / pious / piously"** (`reg.py`, rendered region).

**`tr-pietas` inventory, interval (9 chunks, 9 notes, each at the chunk's first divine site, none with a rendered "piety"
before its anchor):**

| chunk | anchor (first divine site) | word | names the divisio? |
|---|---|---|---|
| `c15-v1-7` | ¶ 1 *in operibus pietatis* (Christ's works; ¶ 2 *summa pietas Christi*) | noun | ✓ |
| `c15-v8-10` | ¶ 15 *pietas Dei ad hominem* | noun | ✓ |
| `c15-v11-20` | ¶ 21 *pietas Dei ad peccatorem* | noun | ✓ |
| `c15-v20-24` | ¶ 33 *pii patris misericordia* | **adjective** | ✓ |
| `c15-v25-32` | ¶ 42 *misericordiam pii patris* | **adjective** | ✓ |
| `c16-v1-8` | ¶ 1 *notificationem pietatis divinae* (the look-back) | noun | ✓ |
| `c17-v11-19` | ¶ 29 *mira Dei pietas* | noun | — |
| `c18-v1-8` | ¶ 9 *Deum pium et iustum* | **adjective** | — |
| `c18-v9-14` | ¶ 23 *nomen summae pietatis* | noun | — |

**No `tr-pietas`, human piety only (10 chunks):** `c16-v9-18` (¶¶ 13–26: the disciples' *pietas*, incl. ¶ 21 *pietas ad Deum*
"piety toward God" and *pietatem divinam*), `c16-v19-22` ¶ 35, `c16-v22-31` ¶ 56 *praestando pietatis auxilium*, ¶ 61 Abraham
*patre piissimo*, `c17-v1-4` and `c17-v5-10` (*pietas spiritualis*), `c17-v20-30` ¶ 35 and ¶ 48 II Pet. 2:9 *pios*,
`c18-v15-17` (none), `c18-v18-27` ¶ 38 Ambrose, `c18-v28-43` (none). All as ruling 31 requires.

**(i) [201] `tr-pietas` on the adjective (`c18-v1-8` ¶ 9 *Deum pium*).** Ruling 31 names "the *pietas*"; but the adjective has
carried the note since `c12-v35-48` ¶ 57 *pius Dominus*, which **ruling 86 ratified by name**, and the interval does it
twice more (`c15-v20-24`, `c15-v25-32`) with no other divine site in the chunk to bear it. **⭐ ratify** (0 lines); record
that "the *pietas* is God's" reads "the word, noun or adjective, is God's".

**(ii) [88] ¶ 21 (not ¶ 22: F10) *invitando ad pietatem divinam* "inviting to divine piety".** Human piety toward God, the
paragraph's own *pietas ad Deum* ("piety toward God") two sentences earlier; the same English phrase names God's piety in
Cap. XV ¶ 1 and in `c16-v1-8`'s note. The Latin is just as ambiguous: Bonaventure uses one phrase both ways.

| alternative | cost |
|---|---|
| **(a) Keep "divine piety"; record in Notes (item (88) answered, ¶ 21)** | **0 lines**; literal, the ambiguity is the Latin's |
| (b) "inviting to piety toward God" | 1 line; reads ¶ 21's *pietas ad Deum* into the phrase (interpretive) |
| (c) a `tr-pietas` saying the *pietas* here is the disciples' | 2 lines; ruling 31's note is for God's *pietas*, so this would be a new use |

**⭐ (a).** Ratify [7], [81] (the divisio-naming notes), [150], [220], [260] as built.

### 5. The manifest cells (item 4 / D-1 [1, 69, 72, 161]) — ⭐ **apply the four cell edits** (doc; 0 chunk lines)

Checked by script: every interval chunk's count of `###`/`####` headings in `## Latin` against its manifest `headings`
entries, and its `title_la` against the manifest's. **Exactly four cells differ, the docket's four**; the other 15 rows
agree (counts 1/1, 0/0, 2/2, 3/3). The chunks were built right (ruling 22: the lowest heading of the opening stack; the
`c12-v1-7` / `c18-v18-27` shape heading → divisio ¶ → heading); the cells are the gate's to correct (ruling 34; the
ruling-33 `c2-v21-24` and ruling-41 `c4-v1-13` precedents).

| row (`manual-review/lucam-chunk-manifest.tsv`) | cell | old | new |
|---|---|---|---|
| `bon-luc-c15-v1-7` (l. 84) | `headings` | `capitulum@381;t4@381L;t4@382L;t4@383R` | `capitulum@381;t4@381L;t4@382L;t4@383R;t4@383R` (adds *Parabola de ove perdita.*) |
| `bon-luc-c16-v1-8` (l. 89) | `headings` | `capitulum@402;t4@402L;t4@402R` | `capitulum@402;t4@402L;t4@402R;t4@402R` (adds *Exemplum parabolicum pietatis providae.*) |
| `bon-luc-c16-v1-8` (l. 89) | `title_la` | `Primo, de pietate humana quoad opera corporalia tripliciter.` | `Exemplum parabolicum pietatis providae.` |
| `bon-luc-c16-v1-8` (l. 89) | `title_la_source` | `rubric-t4 p.402R` | unchanged string, now naming the **lower** of the two 402R t4s (the `c18-v18-27` cell's convention, `rubric-t4 p.460R` for the lower 460R t4); or `rubric-t4 p.402R (lower)` if Wilson wants it explicit |
| `bon-luc-c17-v20-30` (l. 96) | `headings` | `t3@437L;t4@437R;t4@439L` | `t3@437L;t4@437R;t4@437R;t4@439L` (adds *Primo curiositas in perscrutando confutatur per tria.*) |

Span, END and confidence unaffected in every row. **⭐ Apply in one doc commit, before manifest stage 6 is drawn** (the
next stage's coordinator reads these cells). Ratify the other 15 titles as built (item 5).

---

## THE REST OF THE DOCKET

### D-3 / item 16. *intellectus / affectus* (`c17-v1-4` ¶ 11, `c17-v5-10` ¶ 14 [138]; `c18-v9-14` ¶ 26 [229]) — ⭐ ratify, with a scope clause (0 interval lines; F8's 2 pre-interval)

Ruling 32's row reads "*in intellectu … in affectu* 'in the intellect … in the affection' (ruling 17; Vol VI ruling 101)".
Its source is wider: Vol VI ruling 101 keeps "intellect" for "a named doctrine and **the faculty set against *affectus***",
and the p. 88 sheet called `c2-v40-52` ¶ 110 an instance of that clause. **Census, all 101, paragraphs holding both nouns
(20):** the locative formula is "intellect" at 7 and "understanding" at 2 (F8); outside the formula, "intellect" at 6
(`c6-v12-19` ¶ 37, `c6-v20-26` ¶ 57, `c8-v49-56` ¶ 99 ×2, `c11-v1-4` ¶ 8, …) and "understanding" at 7 (`c1-v5-17` ¶ 22,
`c1-v67-80` ¶ 138, `c8-v11-21` ¶ 27, `c9-v18-27` ¶ 37, `c10-v25-37` ¶ 60, **`c17-v1-4` ¶ 11, `c17-v5-10` ¶ 14**). The two
interval sites are faculty pairs, not the formula (*seducendo intellectum, corrumpendo affectum*; *captivationem intellectus,
accensionem affectus*), and ¶ 14 leans on II Cor. 10:5 *in captivitatem redigentes omnem intellectum* ("every
understanding", the Douay; also `c16-v9-18` ¶ 29 and `c9-v18-27` ¶ 37): the prose *captivat intellectum humanum* echoes the
verse's word.

| alternative | cost |
|---|---|
| **(a) Ratify both as built; write the row's scope: "the locative formula *in intellectu … in affectu* (and the faculty named so) 'intellect'; elsewhere *intellectus* 'understanding' even beside *affectus*, an echo of a Douay verse following the verse"; apply F8** | **0 interval lines** + 2 pre-interval (F8) |
| (b) Vol VI's wider clause: every faculty pair "intellect" | `c17-v1-4` ¶ 11 (1 line), `c17-v5-10` ¶ 14 (1 line, three sites) + ~5 pre-interval; ¶ 14 then needs II Cor. 10:5 adjusted to "every intellect" (ruling 20) or a split inside the paragraph |

**⭐ (a).** [229] (`c18-v9-14` ¶ 26, the formula, "intellect") and [275] (*intelligentia* in prose / Douay "understanding" in
verses) ratify as built.

### D-7. Luke 17:19 "made thee safe" / 18:42 "made thee whole" [147, 279] — ⭐ ratify the pair (0 lines)

Both verses read *fides tua te salvum fecit*; the Douay has "made thee whole" at both. `c17-v11-19` ¶ 34 leans on *salus*
throughout (*fides … salutis initium … Spes … huius salutis incrementum … Christus attribuit salutem fidei … quae salvum
faciat credentem*), so ruling 20 licenses the adjustment, and "safe" is the Douay's own word for the same Latin at Luke 7:50
(`c7-v36-50` ¶ 84 "made thee safe"). `c18-v28-43` ¶ 65 leans on *integritas sanitatis*, not on *salus*: "whole" fits
health. **All 101:** *te salvum / salvam fecit* is Douay-worded at Luke 7:50 "safe", 8:48 ×4 "whole", 18:42 "whole"; 17:19 is
the one adjustment, on a leaning paragraph. A ruling-28 split; record in both Notes.

### 17. *pudicitia / puritas* both "purity" (`c15-v20-24` ¶¶ 37–38 [46]) — ⭐ ratify (0 lines)

Ruling 19 gives *pudicitia* "purity". ¶ 37 is the robe *interioris puritatis* (its divisio pairs it with *exterioris
honestatis*, not with *pudicitia*); ¶ 38 is the ring, *pulcritudo pudicitiae*, a different member. The two words never stand
in one sentence. "Chastity" for *pudicitia* would meet ¶ 38's *per castum amorem* "chaste love" (castus) and II Cor. 11:2
"a chaste virgin". **All 101:** *pudicitia* 9 La, "purity" at all 9. Record only.

### 19. *praeco* "preacher" at II Pet. 2:5 (`c17-v20-30` ¶ 48 [167]) — ⭐ ratify (0 lines); alternative "herald" (1 line)

Ruling 30: *praeco* "herald". **All 101:** *praeco* 7 sites, "herald" at 6 (prol p. 9 n. 4, `c1-v5-17` ¶ 8 + p. 13 n. 10,
`c3-v1-9` p. 72 n. 6, `c10-v1-3` ¶ 3, **`c17-v20-30` ¶ 42 Chrysostom, the same chunk**); "preacher" at II Pet. 2:5 *iustitiae
praeconem*, the Douay's "the preacher of justice", adduced for the flood with nothing leaning on *praeco*. Ruling 32's
preface keeps the Douay inside a quotation where ruling 20 does not adjust it, and ruling 30 has no "into quotations"
clause (contrast rulings 17, 45, 52). The cost: "preacher" is *praedicator*'s word (ruling 12), and the chunk now names
*praeco* two ways. **⭐ ratify (ruling 32's preface)**; if Wilson wants ruling 30 to reach quotations, "Noe, the eighth person,
the herald of justice" (1 line).

### II Pet. 1:19 *lucernae lucenti* "a lamp that shineth" [111] — ⭐ ratify (0 lines)

The Douay's "a light that shineth"; nothing leans. But *lucerna* is "lamp" at every site of the 101 (the p. 381 census: 50
La body + 6 app, all "lamp" after D-4; interval 8 / 8), including Matt. 5:15 with nothing leaning, **ratified under ruling
88** as "the work's house rendering of the lamp verses". "Light" is *lux*'s. Same class; ratify.

### Prov. 9:8 "Rebuke not a scorner" [123] — ⭐ ratify (0 lines); alternative "Reprove" (1 line)

`c17-v1-4` ¶ 9 (l. 111): *increpatio* "rebuke" (ruling 32) opens the paragraph; *argue* "reprove" at Lev. 19:17 and I Tim.
5:20 is the Douay's own word; *corripe* "correct" at Matt. 18:15 is adjusted (Douay "rebuke"). Prov. 9:8 *Noli arguere* keeps
the Douay's "Rebuke", **ratified at this verse by ruling 46** with nothing leaning; ¶ 9 is about the order of correction,
not about *arguere*. "Rebuke" then names two Latin words in one paragraph, which ruling 20 permits (the ruling-88 [121]
record's shape). Ratify and record; "Reprove not a scorner" is the conform if Wilson prefers the word kept off *increpatio*.

### Jer. 18:8 "I also will do penance" [18] — ⭐ ratify (0 lines)

`c15-v8-10` ¶ 19 (the seven reasons for the angels' joy over penance) leans on *poenitentia*; the verse sets *poenitentiam
egerit gens* and *agam et ego poenitentiam* in one sentence, one Latin phrase twice. Ruling 32's row ("do penance") applied
to both keeps the phrase one English phrase; the Douay's "repent" for God alone would split it inside the verse (and
"repent" is otherwise *poenitere*'s Douay word that ruling 32 adjusts). Ratify; record that the divine subject was seen.

### *Praeceptor* capital (`c17-v11-19` ¶ 25) — ⭐ ratify; amend the note (F9, 1 line)

Luke 17:13 *Iesu praeceptor* is lower case in Quaracchi; "Master" + `tr-praeceptor` (rulings 12, 49, 69: the last
*Praeceptor* of the work; no *magister* in ¶ 25, so ruling 69's *magister* sentence is rightly absent). The capital is the
Douay's own ("Jesus, Master", `DRC.json`), not only the earlier sites'; the note says otherwise (F9).

### The *dissipare* chain (`c15-v11-20` ¶ 25 [30]) — ⭐ ratify (0 lines)

¶ 25 is built on the verb (*dissipationem … dissipant … dissipat … dissipatur tota hominis substantia*), so ruling 20
licenses the five verses to "waste" (Nahum 2:2, Isa. 3:12, Ps. 140:7, Ps. 34:16, Luke 9:39). **Interval census:** *dissipare*
23 La body + 2 app; "waste(d / th / ing / rs)" at every Bonaventure / lemma site (`c15-v11-20` ¶¶ 21, 25; `c16-v1-8` ¶ 3 ×9,
Luke 16:1; Jer. 1:10 `c17-v31-37` ¶ 60, the Douay's own "waste"); the Douay's own other verbs where nothing leans (Prov.
25:23 "driveth away", `c16-v22-31` ¶ 51; the Gloss's *dissipant cogitationem* "scatter", `c18-v28-43` ¶ 62). Ps. 34:16 *nec
compuncti* "were not pricked" (Douay "repented not"): the Douay's "repent" would put *poenitere*'s Douay word on
*compungi*; ratify it with the chain.

### 22. Quaracchi citation slips; 23–24. `[so printed]` — ⭐ ratify as transcribed (r.57 class; ruling 36)

- **E (item 22):** p. 397 n. 9 *Eph. 6, 16* for 6:15; p. 398 n. 10 *IV. in Luc.* for VII; p. 397 n. 8 *[Isai 52, 7.]*; p. 402
  n. 2; **p. 399 n. 1 *nota. 4.*** (transcribed; its ledger effect is F12 / J-5); **p. 405 n. 10 *supra pag. 403, nota 20***
  (p. 403 has 13 notes; the locus is n. 10): ⭐ **a J-12 `CROSSREF_SLIPS` row** (`("bon-luc-c16-v1-8", "apparatus:p405-10",
  "supra pag. 403, nota 20", "printed slip — p. 403 has 13 notes; the locus is n. 10; filed as printed, not retargeted")`;
  today it resolves to the chunk with no anchor, not a wrong edge); p. 405 n. 2 *Petr. Diacon.* / p. 403 n. 9 *Paul. Diacon.*
  (record both as printed); p. 421 n. 3 *pro eo*; p. 388 n. 12 *pro gratulantur*; p. 389 n. 7; p. 388 n. 5 the editors' own
  *(?)*; `Epist. I. Cor.` p. 455 n. 6; p. 463 nn. 4, 7 point for comma; **p. 471 n. 6 *Psalm. 77, 2* for 87:2** (printed
  slip; filed Ps 77:2 at A: a T-c / J-3-class row, as printed); **Deut. 27:26 without *nec*** (item 10 [134]): Quaracchi prints
  *et eos opere perficit* with no note; ⭐ transcribe as printed, English "and fulfilleth them in work" (ruling 28), recorded,
  no `[so printed]` (not certainly a misprint: we cannot tell Bonaventure's text from the compositor's; ruling 36).
- **F (items 23–25):** the three `[so printed]` (*pedem* `c15-v11-20` ¶ 32; *eundum* `c17-v1-4` p. 427 n. 4; *iuducere*
  `c18-v9-14` ¶ 13) ⭐ ratify. **Item 20 [219]:** `title_la` keeps *iuducere* as printed, `title_en` translates "lead"
  unbracketed: ⭐ ratify (the body carries the mark; a bracket in `title_en` would print in the breadcrumb). **Item 24:**
  *satisfactionem placativam* beside ¶ 48's *persuasio placativa* (Bonaventure's variation, not a misprint) and ¶ 50
  `(Vers. 30.)` without its point (recorded points stand): ⭐ **no mark** (ruling 90's *quinque ova* line). Zero new `[?]`; the
  live `[?]` (`c5-v12-16` p. 122 n. 11) stays open (rulings 59, 73, 90).

### B (item 7). Corrigenda — ⭐ ratify: none in pp. 381–472

The setup sheet's Corrigenda table runs p. 361 → p. 533 (the p. 447 entry in the same section is Vol VI's,
`bon-ioan-c15-v1-11`); every stage-5 `corrigenda` cell is empty. Nothing to apply, nothing missed.

### C (items 8–11). The ruling-20 adjustment batches and splits — ⭐ ratify as batches, with three records

The lemma adjustments (item 8), the adduced-verse batch (item 9; ruling 43's shape), the Douay-base-follows-Quaracchi batch
(item 10; ruling 28) and the splits (item 11) are each ruling 20 or 28 working site by site; `reg.py` found no
*unlicensed* split in the interval beyond F5 (*puer*) and the *supplicium* sites (§ 3). Records: (a) Luke 11:7 is split at
**two** chunks, not one (passes O-1; F5; closed by § 1 (b)); (b) the *mercenarius* / *alienigena* cluster [34, 152] and
*vindicta* [204] are ruling 28 by design; (c) Luke 18:13 *propitius esto* "be merciful" [222] beside *misericordia* "mercy"
(five sites share the root): ruling 20 keeps the Douay; ratify, alt. "be propitious" (1 line) at Wilson's word.

### 18. *evangelizare* forms [90, 188, 273] — ⭐ ratify the forms

Ruling 18: "preach the gospel", never bare "preach". Luke 16:16 passive *regnum Dei evangelizatur* "is preached as gospel";
Apoc. 10:7 (Douay "declared") "preached the gospel"; Gal. 1:23 *evangelizat fidem* "preacheth the gospel of the faith";
Isa. 40:9 with `tr-evangelizare` (ruling 29). Interval census: *evangeliz-* 5 La, every one carrying "gospel" or the ruling-29
"good tidings". Write the passive form into ruling 18 ("is preached as gospel").

### 19 / 21. Single house-word decisions and new house words — ⭐ ratify as batches, with F4, F6, F7 applied

The item-19 list ([47, 61, 82, 93, 112, 113, 135, 136, 137, 151, 152, 163, 164, 165, 168, 185, 186, 187, 191, 202, 207,
208, 224, 255, 257, 259, 261, 276, 277, 278]) and item 21's new words ([13 … 283]) ratify as built, except where F4 (*impie*),
F6 (*simulatio*) and F7 (*infidelitas*) conform a carried word. Records: *segnitia* "sloth" [93] beside ruling 85's *desidia*
"sloth" (*desidia* absent from the chunk; *pigritia* "sluggishness" in the same sentence): ⭐ give *segnitia* "slackness" (1 line,
`c16-v9-18` ¶ 31) so "sloth" stays *desidia*'s, or record — Wilson's word; [276] *excedentia desiderii* "exceedingness" and
*supra nos excedimus* "are transported above ourselves" follow ruling 81's sense clause (the mental sense; record); passes
O-2 (p. 471 n. 1 Vat. *excessum* "excess") goes with [276]: the variant's noun is the measure word glossed, record.

### G (items 26–30). Readings as printed — ⭐ ratify as recorded; supply nothing

Guillemets as printed (`c18-v1-8` « 70 / » 72, the two opening « absent at James 5:15 and Job 21:15: supply nothing, the p. 188 /
288 / 381 practice); points and sorts; marginalia; codex H read for `II`; set-off verses. **D-6 *Ducange*** (`c17-v31-37` p. 444
n. 8): the plate breaks the name *Du-|cange* with a lower-case *c*, and the **La.** half transcribes it as the break shows; the
**En.** half already reads "cf. Du Cange, *Glossarium*". ⭐ **keep** (ruling 9: transcribe as printed).

### H (item 31). Collection change — ⭐ bank; no ruling.

### A (items 1–3, 5–6). Boundaries, structure — ⭐ ratify (ruling 36); item 4 is § 5

All 19 rows built as drawn; ruling 39's five `low` → `high` promotions; last ¶ XV 52 · XVI 61 · XVII 62 · **XVIII 66** (the
setup table's); titles as built; shared pages, runovers, gutters as recorded. Not re-derived from plates (none read).

---

## T. TOOL ITEMS (not for ruling): this interval's sites folded into the queued job J-1..J-12

**State:** rulings 76 / 92's one job has **not run**. Ledger (`index/citations.tsv`) checked for every docket site.

| merged item | this interval's sites | expected effect |
|---|---|---|
| **J-1** (wrong *ibid. / loc. cit.*, run first) | T-b's twelve: p. 393 n. 7, p. 395 n. 7, p. 400 n. 8, p. 405 n. 2, p. 410 n. 2, `c16-v9-18` ¶ 32 body *ibidem* → Gen 32:28, p. 417 nn. 11–13, p. 437 n. 6 *Ibid.* → `c12-v13-34`, p. 454 n. 4, p. 471 n. 9 · **+ p. 386 n. 8 (F11)** | **13** wrong edges removed; anaphora unresolved **427 → up to 440** unless the named work then resolves. Checked and **right**: p. 387 n. 12 *ibid. 20, 2* → Exod 20:2; p. 426 n. 12 *ibid. 5, 29* → Matt 5:29 |
| **J-3** (printed slips as rows) | T-c: p. 471 n. 6 *Psalm. 77, 2* (for 87:2) | filed as printed, flagged |
| **J-4** (accusative *notam M*) | **10 sites** (F12): p. 382 n. 2 ×2, p. 418 n. 14, p. 434 n. 3, p. 440 n. 10, p. 448 n. 9, p. 463 n. 1 ×2, p. 466 n. 2 ×2 | page-only / `page-multi` → `chunk` + anchor |
| **J-5** (`page-multi` by note) | p. 399 n. 1 *nota. 4.* (point); p. 433 n. 13 *supra pag. 147*; p. 409 n. 8; p. 461 n. 10 | resolve by the note where one is printed |
| **J-6** (no record) | T-d: p. 423 n. 1 *pag: 165* (colon); p. 462 n. 10 *Collat. 1. de Decem Praecept. n. 22*; p. 470 n. 8 *supra 11, 9* | +3 records |
| **J-9** (count, classify) | T-a (12 chunk lists); p. 463 nn. 4, 7 point-for-comma | re-measure (427 today) |
| **J-11** (in-work *n. N*, deferred) | T-f | count only |
| **J-12** (`CROSSREF_SLIPS` + direction screen) | **+ p. 405 n. 10** *supra pag. 403, nota 20* (§ 22); the direction screen over the interval's 159 crossref records finds **0** new direction slips | 1 row; the screen still reports 4 |
| T-e (by hand at the gate) | p. 418 n. 14 → `bon-sap-c3`, p. 421 n. 3 → `bon-sap-c5`, p. 426 n. 5 *tom. VI. pag. 460* | as the docket says; p. 418 n. 14 is also a J-4 site |

Same discipline as ruling 76: report → fix → report; `tools/build-citations.py` only, then `build-citations.py` →
`build-index-json.py`; no chunk file. Baseline QA 213, anaphora unresolved 427.

---

## ▶ DOCKET SUMMARY (one word each: "Approve" takes the ⭐)

| # | items | ⭐ recommendation | lines | kind |
|---|---|---|---|---|
| **1** | item 12, *puer* (F5) | **"child(ren)" through `c18-v15-17`; three "servant" verses keep the Douay; ruling 54 clarified** | **12** | **rule** |
| 2 | item 13 / D-2, Ps. 35:10; John 8:12 (F14) | **Ratify the split; John 8:12 exempt (unit = the member)** | 0 | record |
| **3** | item 14 / D-4, *poena* / *supplicium* (F1) | **Ratify `e810ccc`; *supplicium* → "penalty" (the house rule)** | **16** (+~10 pre) | **rule** |
| 4 | item 15 / D-5, *pietas* (F10) | **Ratify the inventory and the adjective note; ¶ 21 kept literal** | 0 | ratify |
| **5** | item 4 / D-1, manifest | **Apply the four cell edits** | doc | fix |
| D-3 | *intellectus / affectus* | **Ratify; scope clause in ruling 32's row** | 0 | rule |
| D-7 | Luke 17:19 / 18:42 | **Ratify the pair** | 0 | ratify |
| D-6 | *Ducange* | **Keep as printed** | 0 | ratify |
| **F2** | *poena* "penalty" (= N-1) | **Apply** | **1** (+5 pre) | fix |
| F3 | *poena* "pains" (= N-2) | **Keep; record as sense exception** | 0 | record |
| **F4** | *impie* "wicked one" (= N-3) | **Apply** ("impious one") | **1** | fix |
| **F6** | *simulatio* "simulation" | **Apply** ("dissembling") | **2** (+8 pre) | fix |
| **F7** | *infidelitas* "infidelity" | **Apply** ("faithlessness") | **2** | fix |
| **F8** | locative formula "understanding" | **Apply** (pre-interval) | (+2 pre) | fix |
| **F9** | `tr-praeceptor` Douay claim | **Apply** | **1** | fix |
| F10 | ¶ 21 not ¶ 22 (= R-1) | **Amend Notes** | doc | doc |
| F11–F12 | wrong edge p. 386 n. 8; J-4 / J-5 coverage | **Fold into J-1 / J-4 / J-5** | 0 text | tool |
| F13–F14 | *mirus*; Ps. 35:10 framing | **Record** | doc | doc |
| 16–19 | *pudicitia*; *praeco*; II Pet. 1:19; Prov. 9:8; Jer. 18:8; *dissipare*; *Praeceptor*; *evangelizare*; house words | **Ratify** (record the splits; *segnitia* "slackness" optional, 1 line) | 0 | ratify |
| B, C, E, F, G | corrigenda (none); ruling-20 batches; slips (+ J-12 row p. 405 n. 10); `[so printed]`; readings | **Ratify** | 0 | batch |
| H | collection change | **Bank** | 0 | bank |
| T | T-a..T-f | **Fold into the queued job; J-1 now 13 sites, J-4 10** | 0 text | tool |

**If every ⭐ is taken: 35 English lines in the interval** (§ 1 12, § 3 16, F2 1, F4 1, F6 2, F7 2, F9 1) **across 12
interval chunks, + ~25 pre-interval lines** (§ 3 ~10, F2 5, F6 8, F8 2) **in ~16 earlier chunks**; one of the 35 is a
`tr-` definition. Five manifest cells in three rows (§ 5). Notes records / amendments in ~15 chunks. Ruling 54 gains a
clarifying sentence (§ 1), ruling 32's *intellectus* row a scope clause (D-3), ruling 18 the passive form; ruling 87's
*supplicium* clause is replaced by the house rule (§ 3). No line in any `## Latin` body or `**La.**` half changes.

**Needs Wilson's own judgment beyond approve-all:** (1) **§ 1**, "children" against the builder's "boys", which was the
ruling as he read it; (2) **§ 3**, because the ⭐ re-opens one clause of ruling 87 and touches ~10 lines in chunks that
passed the p. 288 / p. 381 gates; (3) whether the **~25 pre-interval lines** (F2, F6, F8, § 3) go in now (the p. 288 and
p. 381 precedents say yes); (4) **D-3**'s scope clause, which chooses the narrow reading of ruling 32's row over Vol VI
ruling 101's wider one.

**Could not settle from the files:** nothing on the docket needed a plate. Two points rest on the builders' plate reads
and are not re-derived: the four manifest headings' page positions (§ 5), and Deut. 27:26's missing *nec* as printed.
