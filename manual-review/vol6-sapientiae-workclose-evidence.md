# Vol VI — *Commentarius in librum Sapientiae*, WORK-CLOSE GATE (ruling 34, p. 235): EVIDENCE SHEET

Compiled 2026-10-16 by a read-only agent on Wilson's go ("Run the gate"). **Nothing here is settled. Wilson rules off this sheet.**
No chunk, tool, resume note or ledger was edited; no push, deploy or stash. `build-citations.py` was run into the scratchpad
(`--out`/`--qa`) and its ledger came out **byte-identical** to the tracked `index/citations.tsv`; `build-content` →
`build-index-json` → `build-content` regenerated only gitignored outputs. Gate log: `manual-review/vol6-sapientiae-workclose-gate.md`.

**Scope (derived from frontmatter): all 23 units, `bon-sap-prooem` … `bon-sap-schemata`, pp. 107–235 with no gap, 1,361 numbered
entries, 29 `tr-` notes.** Every census is over the BUILT files and the LIVE region (`## Latin`, `## English`, `## Apparatus`;
frontmatter and `## Notes` stripped), never `raw/`. Latin and English paired by paragraph index (the two blocks are parallel in all
23; the Scholion's and Schemata's extra English "paragraph" is the closing `---` rule). Scripts: scratchpad `gate/sweep.py`,
`gate/seams.py`, `gate/hand.py`, `gate/census.py`, `gate/pair.py` (not in the repo).

## ▶ ONE-SCREEN SUMMARY

**A — needs a ruling**

| # | question | recommendation | lines |
|---|---|---|---|
| A1 | ⭐ ***supplicium*** — **25 sites in 11 units**, all "punishment" but three "torment"; it meets *poena* at 7, giving "the punishment of punishment" ×5 and a silent *poena* → "penalty" workaround in c1 | ***supplicium* → "penalty"** at 24 sites (Matt. 25:46 inside c3's Gloss keeps "punishment", the quotation branch); c1's *poena* back to "punishment" | ~22 En |
| A2 | c11 p. 182 *poenas seu punitiones* → "punishments or punishings" | **Keep** (ruling 44 applied exactly; the pair is the Latin's) | 0 |
| A3 | Job 24:13 *rebelles lumini*: c14 p. 201 "light" vs c17 p. 218 "lumen" | **Ratify** — ruling 46 decides by passage; c17's prose leans on it, c14's does not | 0 |
| A4 | c17 p. 218 *id est **dati** radii* bracketed "[so printed: *dati* for *clari*]" | **Keep the bracket** (ruling 45) — *dati* does not gloss *limpidae*; unlike c7's *actum* (ruling 49) it does not construe as a gloss | 0 |
| A5 | *meritum culpae* (cc. XIII–XV): c13 "merit of their fault", c16 "merit of fault", **Schemata "desert of fault"** | **Conform the Schemata to "merit of fault"** (Latin untouched; the c13 heading's printed *demerito* stays "demerit") | 1 En |
| A6 | marginal-quaestio count — c19 p. 229 `[O]pponitur.` **and its sibling c16 p. 214 `Obiectio.`/`Solutio.`** | **Keep ruling 51: work total 61** (63 if both counted) | 0 |
| A7 | *tormentum* → "punishment" at two Douay sites (c11 p. 180 lemma Sap. 11:14; c5 p. 142 n. 8 Sap. 16:24) against "torment" at ~59 | **Conform both to "torment(s)"** (Douay adjusted, the *impius* rule; c16 already renders Sap. 16:24 "unto torment") | 2 En |

**B — defects found (plain repairs)**

| # | defect | repair | lines |
|---|---|---|---|
| B1 | **Ruling 44 never reached the two pre-c3 chunks:** `prooem` p. 108–109 *in punitione rebellium* and `c1` p. 115 *id est punitionem* still read "punishment" (the mid-work gate's scope began at c3) | "punishing" at both | 2 En |
| B2 | **`tr-studium` missing in `bon-sap-schemata`** — p. 235 *ex studio eam inveniendi* → "the study of finding her"; every other unit carrying *studium* (prooem, c1, c6, c8) has the note, and the Schemata wrote `tr-vacare`/`tr-doctrina` on the same one-per-chunk logic | write the note | 1 note |
| B3 | Documentation only: the mid-work gate log places *poenas seu punitiones* on **p. 183** (it is p. 182); the running list's "c18 … *supplicium* ZERO" is right only because c18's two `supplic-` hits are *supplicatio* — say so | next resume block | doc |

**C — confirmations needing only a nod** (detail in § C): passes 1–3 clean; every binding ruling present in every chunk that
carries its word (except B1/B2); the 21 misprint brackets of item 6; ruling 50's three over-runs; the colophon, Scholion and
Schemata as built; resolver classes logged (ruling 40/58).

**If every A/B recommendation is taken: ~27 English lines + 1 translator's note + doc. No Latin line changes.**

⛔ **Ruling 57's C1 job (the `ibid. C, V` resolver fix, with its before/after `index/citations.tsv` diff for Wilson) is STILL OWED
before the p. 235 deploy.** `tools/build-citations.py` was last changed at the Ecclesiastes gate (`dfb5adb`); the job has not been
run. It is not part of this gate's repairs.

---

## ▶ MECHANICAL PASSES, WITH DENOMINATORS

| pass | what it COUNTED | verdict |
|---|---|---|
| 1 `check-live-flags.py vol6` | **68 vol6 chunks** | **no live `[?]`** |
| 2 `polish-style-scan.py` | **2,187 chunks, vol1–vol6** | 11 issues / 6 chunks (10 PAIR Vols III–IV, 1 V5LABEL `bon-hex-c23`) — the standing baseline, **ZERO in vol6** |
| `check-vol5-apparatus.py --volume=vol6` | **68 chunks, 2,208 entries** (Eccl 847 + Sap 1,361); all 23 Sapientiae units La = En | **All checks passed**; no PENDING, no GAP; `KNOWN_TOTALS_VOL6` matches every page 107–233 |
| `check-vol5-census.py` | vol5 167/167 · **vol6 68/68**; vol6 107 runovers (104 gutter, 3 page) | **Rosters agree.** Sapientiae **59 runovers — 57 gutter + 2 page (p. 168 n. 11 c9-internal; p. 216 n. 9 → p. 217, c16)**; scholion/schemata negative |
| `build-citations.py` (scratchpad) | **2,187 chunks → 28,709 records** | QA **208**, **ZERO lines ours** (the QA file lists `prol`/`scholion`/`schemata` only on the no-citation list); ledger **byte-identical** |
| ours in the ledger | **3,136 records**: scripture A 1,472 · B 594 · C 879; crossref 148 chunk · 37 page-multi · 4 distinctio · 2 work | zero dangling / unresolvable / ambiguous |
| `build-content` → `build-index-json` → `build-content` | **16 books, 2,186 / 2,186 translated**; index **1,732 cited / 10,560 backlinks** | built; `git status` clean |
| anchors / markers (per chunk, all 23) | numbered anchors La = En in identical order; anchor set = def set; no duplicates; `<!-- page N -->` list = `printed_pages` in both languages; `tr-` anchors English-only (or apparatus `**En.**`, ruling 13) | **clean in all 23** |

## ▶ PASS 3 — BOUNDARY SWEEP (whole work, derived from the files)

**Every page 107–235 owned; every register contiguous 1..N; `KNOWN_TOTALS_VOL6` agrees on all.** Twenty shared leaves, with the
split derived from the defs and stated identically in BOTH chunks' apparatus headers:

**109** prooem 1–5 / prol 6–8 · **110** prol 1 / c1 2–7 · **118** c1 1–3 / c2 4–8 · **125** c2 1–3 / c3 4–11 · **131** c3 1–8 / c4 9–11 ·
**137** c4 0 / c5 1–9 · **144** c5 1–5 / c6 6–9 · **151** c6 1 / c7 2–9 · **159** c7 1–11 / c8 0 · **166** c8 1–8 / c9 9–12 · **171** c9 1–4 /
c10 5–9 · **177** c10 1–6 / c11 7–9 · **184** c11 1–5 / c12 6–10 · **191** c12 1–7 / c13 8 · **196** c13 1–4 / c14 5–11 · **209** c15 1–5 /
c16 6–7 · **217** c16 1–4 / c17 5–8 · **221** c17 1–12 / c18 0 (body-only) · **228** c18 1 / c19 2–8 · **233** c19 1–6 / Scholion 0.
**One leaf edge: 203/204** (c14 owns 203 whole, "Capitulum XV opens at the head of p. 204"; c15 owns 204–208 whole).
**234–235**: the Schemata, no register.

- **Seam sentences**: every outgoing tail is a complete sentence in both languages; every incoming body opens on `### Capitulum N.`
  + its printed heading (c6 on `(Vers. 1.)`, c10 on its lemma, as built), the prol on its `### Prologus`, c1 on the `Commentarius`
  stack, the Scholion after c19's `**Explicit postilla in librum Sapientiae.**`, the Schemata on `### Schema I.`
- **Runover ledger**: all **59** Sapientiae entries are owned by the chunk that ledgers them, and each is stated in that chunk's Notes;
  the p. 216 n. 9 page-crossing is ledgered once (c16) and c17 places its own nn. 5–8 "in the RIGHT block below c16's n. 4" (the
  tail is c16's; c17 does not restate it — consistent, no double count).
- **No plate was needed** for any seam or docket item. Plates 191–237 are on disk and were not opened.

---

## ▶ A. NEEDS A RULING

### A1 ⭐ — *supplicium* (running-list item 1; the c1–c12 census owed by it)

**Census (live region, Latin):** 25 sites — c1 **5** · c2 **1+1 app** · c3 **2** · c5 **4** · c6 **2** · c10 **1** · c13 **1** · c16 **3** · c17 **1** ·
Schemata **4**; prooem, prol, c4, c7–c9, c11, c12, c14, c15, c18, c19, Scholion **0**. (c18's two `supplic-` hits, p. 222, are
*supplicatio* / *supplicationis* → "supplication", correct and not this word.) The running list had 9; the 16 in c1–c12 are new.

| # | unit | p. | Latin | current English |
|---|---|---|---|---|
| 1 | c1 | 113 | *rapietur ad **supplicium*** | carried off … to punishment |
| 2 | c1 | 117 | *perditio **supplicii** aeterni* | the destruction of eternal punishment |
| 3 | c1 | 117 | *de perditione **supplicii*** | of the destruction of punishment |
| 4 | c1 | 117 | ***supplicium** iniustitiae* | the punishment of injustice |
| 5 | c1 | 117 | *aequitatem **supplicii** seu **poenae** inflictae* | the equity of the punishment or of the **penalty** inflicted ⚠ |
| 6 | c2 | 119 | *non erit refrigerium nec **supplicium*** | neither refreshment nor punishment |
| 7 | c2 | 124 n. 3 | Aug.: *A locis **suppliciorum** [crux] fecit transitum* | From the places of punishment |
| 8 | c3 | 128 | *de **supplicio** incontinentiae* | the punishment of incontinence |
| 9 | c3 | 129 | Gloss < Matt. 25:46: *impii ibunt in **supplicium** aeternum* | the impious shall go into eternal punishment |
| 10 | c5 | 138 | *propter **suppliciorum** praeparatorum et tortorum horribilium* | the torments prepared and of the terrible torturers |
| 11 | c5 | 142 | *secundo, **supplicium** reproborum* | the punishment of the reprobate |
| 12 | c5 | 142 | *Hic tangit **supplicium** reproborum sub metaphora* | the punishment of the reprobate |
| 13 | c5 | 143 | *timor de praesentibus **suppliciis*** | fear over the present torments |
| 14 | c6 | 144 | *insipientium rectorum **poenam** et **supplicium*** | the *punishment* and torment of unwise rulers |
| 15 | c6 | 146 | *fortior instat cruciatio, in **supplicio*** | a mightier torment is ready, in punishment |
| 16 | c10 | 173 | *per publicum **supplicium*** | through a public punishment |
| 17 | c13 | 191 | *de **supplicio poenae** eorum* | the punishment of their *punishment* |
| 18 | c16 | 209 | run heading *Secundo determinatur de **supplicio poenae** culpabilium.* | Secondly is determined the punishment of the punishment of the culpable. |
| 19 | c16 | 209 | divisio *hic agit de **supplicio poenae*** | here he treats of the *punishment of punishment* |
| 20 | c16 | 210 | *scilicet **poenae** interimentis **supplicium*** | namely the punishment of slaying punishment |
| 21 | c17 | 219 | *pessima, scilicet **supplicia** pro peccatis inferenda* | the punishments to be inflicted for sins |
| 22 | Schem. | 234 | ***supplicium** iniustitiae* | the punishment of injustice |
| 23 | Schem. | 234 | *aequitatem **supplicii*** | the equity of the punishment |
| 24 | Schem. | 234 | ***supplicium** reproborum sub metaphora arma moventis* | the punishment of the reprobate under the metaphor of one taking up arms |
| 25 | Schem. | 235 | *de **supplicio poenae*** | on the punishment of punishment |

**What the table shows.** (i) *supplicium* is "punishment" at 21, **"torment" at 3** (10, 13, 14). (ii) It **meets *poena* at seven sites**
(5, 14, 17–20, 25) and the collocation ***supplicium poenae*** is the **run heading of cc. XVI–XIX** (18), set against
*de merito culpae* (cc. XIII–XV) — the hinge of ratio 3's second member, exactly as *punitio*/*poena* was for ruling 44.
(iii) c1 p. 117 dodged the collision by rendering ***poena* → "penalty"** (5) — a **silent departure from ruling 20**, not disclosed
in c1's Notes. (iv) **"Penalty" is otherwise nearly free in this work**: the only other English "penalty" is c2 p. 119
*propter poenalitatem* → "on account of penalty" (ruling 20's *poenalitas*), one site, which never meets *supplicium*.

**Decisive sentence** (c16 p. 209, the divisio under the run heading):
> *Postquam a decimo tertio capitulo egit de **merito culpae** quoad poenas graviores … hic agit de **supplicio poenae**, et primo de
> **poenis** antecedentibus mortem … secundo, de **poenis** inferentibus mortem*
> "After he has treated, from the thirteenth chapter, of the merit of fault as regards the heavier punishments … here he treats of the
> ***punishment of punishment***, and first of the punishments *preceding death* … secondly, of the punishments *inflicting death*"

| option | cost |
|---|---|
| (a) keep (ruling 20's sharing) | 0 lines; "the punishment of punishment" stands ×5 incl. the run heading and the Schemata; c1's silent "penalty" must then be either disclosed or reverted (→ "the punishment or of the punishment inflicted", 1 line); the three "torment" sites stay a contextual mix |
| **(b) *supplicium* → "penalty" throughout the work** (one Latin word, one root — the *impius* rule), Matt. 25:46 inside c3's Gloss keeping Douay "punishment" (the quotation branch, rulings 46/53) | **24 sites, ~21 English lines, per-site** (the English does not mark which word it renders); c1 p. 117 *poenae* back to "punishment" (+1) → "the equity of the penalty, or of the punishment inflicted"; the hinge reads "**the penalty of punishment**"; shares "penalty" with *poenalitas* at 1 non-meeting site (c2). ⚠ Ecclesiastes' 4 body *supplicium* sites stay "punishment" under ruling 20 unless extended — a cross-work divergence, recorded |
| (c) *supplicium* → "torment" | **refused by census**: "torment" is the settled word for *tormentum* / *cruciatus* / *cruciare* / *torquere* (~61 Latin sites, all "torment" but A7's two), and it **meets *supplicium* on two leaves** — c5 p. 138 (*suppliciorum … tortorum*, whose n. 2 records A's variant *tormentorum*) and c6 p. 146 (*cruciatio, in supplicio*) |
| (d) "penalty" only where *supplicium* meets *poena* (sites 5, 14, 17–20, 25 + 23 to keep the Schemata/c1 pair) | 8 lines; cheaper, but one Latin word with one sense then takes two English words by position, and the three "torment" sites stay |

**RECOMMENDATION: (b).** Per-site, English only, ~22 lines. Same argument as ruling 44: n is not small (25), the word has one sense,
and the one-word rule (ruling 20's sharing) is hiding Part II's run heading. "Torment" is barred by its own settled word.

### A2 — c11 p. 182 *poenas seu punitiones* (running-list item 18's leftover; the mid-work log says p. 183)

> *non tantum creaturas ipsas, sed et earum retributiones et **poenas seu punitiones**, disposuisti in mensura*
> "not only the creatures themselves, but also their requitals and **punishments or punishings**, *thou hast ordered in measure*"

Options: (a) keep — ruling 44 exactly (*poena* punishment / *punitio* punishing), the *seu* pair visible; (b) "punishments or acts of
punishing" — 1 line, smoother, same root; (c) "penalties or punishings" — collides with ruling 20 (*poena*). **RECOMMENDATION: (a).**
0 lines. (If A1(b) is taken this site is unaffected — no *supplicium*.)

### A3 — Job 24:13, c14 vs c17 (running-list item 4)

- **c14 p. 201** (n. 11): *unde Iob vigesimo quarto: « Ipsi fuerunt **rebelles lumini** ». Tot, scilicet quoad numerum…* → "« They have been
  rebellious to the light »[tr-lumen]" — quoted as a verse; the next words gloss *tot*, nothing leans on *lumen*.
- **c17 p. 218**: *Et merito defuit eis **lumen**, quia scilicet rebelles fuerunt **lumini spirituali**; Iob vigesimo quarto: « Ipsi fuerunt
  rebelles **lumini** »* → "And deservedly lumen was lacking to them, because … they were rebels against the spiritual lumen; … « They have
  been rebellious to the lumen »" — the body's own *lumen* leans on the verse; Sap. 5:6 *iustitiae lumen non luxit* follows ("the lumen of
  justice"), same reason.

Options: (a) ratify as built (ruling 46 decides by passage, both disclosed in their `tr-lumen`); (b) conform c14 to "lumen" — 1 line,
and turns the test into a verse rule. **RECOMMENDATION: (a).** Other verse-test sites in c13–c19, all as the running list says:
c16 p. 216 n. 8 Damascene *spirituale lumen* (apparatus, not a verse) "lumen" · c18 p. 223 Sap. 18:4 *incorruptum lumen legis* "lumen"
(FAILS: *lex aliquando dicitur lumen* leans) · c19 p. 231 Eph. 5:13 *a lumine manifestatur* "light" (PASSES) · c8 p. 163 Phil. 2:15
*luminaria* "lights" (*luminare*, not *lumen*). `tr-lumen` stands in **every** unit carrying *lumen* (prooem, c2, c5, c6, c7, c14, c16,
c17, c18, c19); c13, c15, Scholion, Schemata carry none.

### A4 — c17 p. 218 *dati* (running-list item 6)

> *Nec siderum, id est stellarum, limpidae flammae, id est **dati** radii, illuminare poterant illam noctem horrendam*
> "*the clear flames,* that is, given [so printed: *dati* for *clari*] rays, *could illuminate that horrible night*"

The plate prints *dati* (2.2×; the raw's `dali` agrees on the shape). The expositor glosses noun by noun (*siderum → stellarum*,
*flammae → radii*), so the adjective owes a gloss on *limpidae*; "given" is not one. Options: (a) keep the bracket (ruling 45); (b) drop
it and read plain, as ruling 49 did for c7's *actum* — 1 line, but *actum* construed as a gloss and *dati* does not; (c) soften to
"[so printed; the gloss on *limpidae* wants 'clear']" — 1 line, asserts less about the sort. **RECOMMENDATION: (a).** 0 lines.

### A5 — *de merito culpae* in the Schemata (running-list item 11)

| site | Latin | English |
|---|---|---|
| c13 p. 191 divisio | *Et primo determinat de **merito culpae** ipsorum, scilicet usque ad decimum sextum capitulum* | "the **merit** of their *fault*" |
| c13 p. 191 heading | *Primo determinatur de **demerito** culpae tripliciter.* | "the **demerit** of fault" (as printed) |
| c16 p. 209 divisio | *Postquam a decimo tertio capitulo egit de **merito culpae*** | "of the **merit** of fault" |
| Schemata p. 235 | *de **merito culpae*** (summarising cc. 13–15) | "on the **desert** of fault" |

The Schemata summarise the very sentences c13 and c16 render "merit of fault". (*meritum* is otherwise contextual: c19 p. 228
*meritum ex parte punitorum* → "desert", c19 p. 231 *merita* → "deserts" — fine where it is not this collocation.) Options:
(a) keep "desert" (the Schemata builder's choice, defensible English); **(b) conform the Schemata line to "on the merit of fault"** —
1 English line; the Latin's *merito* vs c13's *demerito* stays recorded as printed (housekeeping (a) of the Eccl gate). **RECOMMENDATION: (b).**

### A6 — marginal quaestiones (ruling 51; running-list item 8)

By printed `Quaestio` marginale (`Quaestio solvitur.` included), from each chunk's table (c1, c2 from Notes per ruling 39):
prooem 0 · prol 0 · c1 9 · c2 4 · c3 4 · c4 1 · c5 2 · c6 4 · c7 5 · c8 3 · c9 0 · c10 0 · c11 3 · c12 3 · **c13 3 · c14 7 · c15 2 · c16 5 ·
c17 1 · c18 3 · c19 2** = **61 in the work** (38 in pp. 107–191, 23 in pp. 191–233). **Labelled non-`Quaestio` objections, not counted — two,
not one:** c19 p. 229 L `[O]pponitur.` / `Resp.` (*Sed contra: Quia poterant poenitere…*) **and c16 p. 214 R `Obiectio.` / `Solutio.`**
(*Sed contra: Quia, si habebat saporem a quolibet desideratum…*); plus c14 p. 201's `Obiectio.` inside a counted `Quaestio` row and c7
p. 159's unlabelled pair. **RECOMMENDATION: keep ruling 51 — 61.** (Counting the class would give 63; it reopens what "marginal
quaestio" means for two sites.) 0 lines.

### A7 — *tormentum* → "punishment" at two Douay sites (new)

*tormentum*/*cruciatus*/*cruciare*/*torquere* take "torment(s)/tormented" at ~59 sites. Two take Douay's "punishment":
- c11 p. 180 lemma, Sap. 11:14: *Cum enim audirent … **per sua tormenta** bene secum agi* → "that by their **punishments** it was well with them"
- c5 p. 142 n. 8 (apparatus): *ubi post exardescit Vulgata addit **in tormentum*** → "the Vulgate adds *in tormentum* (**unto punishment**)" —
  while **c16 p. 216's lemma renders the same words of Sap. 16:24 "unto torment"** (*in tormentum, punitionis* → "unto torment, of punishing").

Options: (a) leave (Douay kept); **(b) conform both to "torment(s)"** — 2 lines; the lemma is Douay adjusted to Quaracchi's Latin (ruling 5,
the *impius* precedent of ruling 32), and Sap. 16:24 then reads one way in the work. **RECOMMENDATION: (b).** ⚠ Under A1(b) this matters
more: "punishment" would then be *poena*'s alone.

---

## ▶ B. DEFECTS FOUND

### B1 — ruling 44 not applied before c3

*punitio* (noun), all 69 live sites: c13–c19 + Schemata **all "punishing"** (c13 3 · c14 2 · c16 8 · c17 2 · c18 4 · c19 11 · Schem. 3);
c3–c12 conformed at the mid-work gate (34). **Two sites predate that scope and still read "punishment":**
- `bon-sap-prooem` p. 108–109: *Potentiam Dei notificat in **punitione** rebellium* → "It makes known the *power* of God in the
  **punishment** of the rebellious" → **"in the punishing of the rebellious"**
- `bon-sap-c1` p. 115: *et ad correptionem, id est **punitionem**; iniquitatum illius* → "*and to the reproof,* that is, the **punishment**,
  *of his iniquities*" → **"that is, the punishing"**

Mechanical as a class (ruling 44's wording), per-site in English. **2 lines.** (*punire* forms — 57 sites — are untouched by the
ruling and correctly left: "punished", "the one punishing".)

### B2 — `tr-studium` owed in the Schemata

*studium* in the live region: prooem 5+2 ✓ · c1 1 ✓ · c6 2 ✓ · c8 7+1 ✓ (ruling 54) · **Schemata 1 ✗** — p. 235 Ratio 2 member *ex **studio**
eam inveniendi* → "from the **study** of finding her" (the root is right; the note is missing). Ruling 11's reason — "notes do not reach
across chunks" — is the same one the Schemata already followed for `tr-vacare` and `tr-doctrina`. **Write the note** (English-only,
in `## Apparatus`). 1 note, 0 text lines.

### B3 — documentation
- mid-work gate log / resume item 18: *poenas seu punitiones* is on **p. 182**, not p. 183 (the paragraph runs 182→183; the phrase
  stands before the break).
- running-list item 1's "c18 … ZERO" is true of *supplicium*; c18's two `supplic-` hits are *supplicatio* — add the word so a later
  stem census does not re-find them.
Next resume block only; no chunk.

---

## ▶ C. CONFIRMATIONS (a nod each)

1. **Passes 1–3 clean** (above), with the denominators read.
2. **Binding rulings, every chunk, live region:**
   - **44** — see B1; otherwise complete. English "punishings" ×1 (A2).
   - **46** — A3.
   - **50** — `verses` = index label verbatim; over-runs exactly three: **c1** Vers. 16 / `1-15`, **c11** Vers. 27 / `1-26`, **c17** Vers. 20 /
     `1-19`; c18 25 = `1-25`, c19 20 = `1-20`; the other 14 capitula match.
   - **51** — A6 (61).
   - **53** — `tr-doctrina` in **every** unit whose Latin carries *doctrin-*: prooem, c1, c3, c4, c6, c7, c8, c10, c11, **c15**, **Schemata** (11);
     c2, c12, c16's English hits are other words (a *docere* form, *instructio*) or Augustine's title abbreviated `de Doctr. christ.` — none owed.
   - **54** — *studium* → "study" everywhere (English "zeal" now only for *zelus*, c5 p. 142); notes per B2.
   - **36/47** — every capitulum's `title_la` is a heading printed in its own Latin body (c1–c19, prooem); prol's is its `Prologus` heading + "et expositio prologi" (ruling 28), Scholion/Schemata titled by type.
   - **39** — `### Marginal quaestiones` table present in **c3–c19** (17 of 17; c9 and c10 carry a positive-zero row).
   - **20** — *poena* → "punishment" everywhere **but c1 p. 117** (A1); *poenalitas* → "penalty" (c2, 1 site).
   - **41/43** — English `**Contra:**` / `**Sed contra:**` labels **0**; "On the contrary" 52; c13/c18/c19's `Sᴇᴅ ᴄᴏɴᴛʀᴀ` → "**But on the contrary:**".
   - **vacare** (dikaisune) — 6 *vaca-* sites (prooem 2, c2 1, c5 1+1 app, Schemata 1), `tr-vacare` in each unit, **none "rest"**.
   - ***intellectus*** — 48 Latin sites, **bare "intellect" 0**. ***impius*** 97+12 → "impious" **109 = 109**.
3. **Item 6, the misprint brackets** — 21 in the live English (inventory in the gate log), all of rulings 37/38/45/48's forms; c16 ×3, c17 ×2,
   c18 ×2, Schemata ×1 exactly as the running list. Readings left plain (c16 *Neque*, *remunerationem*, `8, 17`) stand.
4. **Item 10** — c19's colophon ***Explicit postilla in librum Sapientiae.*** rendered; the Scholion six lines, no anchor, no apparatus; c19's
   Notes call rows 0.25–0.33 "the Scholion's region", which `bon-sap-scholion` records as the chapter's close (true Scholion rows 0.51–0.55) —
   Notes-level, c19 unedited. Nod.
5. **Item 11** — the Schemata as built (158 nodes, 23 `(c. N.)`, `(11. 12.)`, Ratio 2's `(c. 7. 8.)`, ~20 wording differences recorded as
   printed), save A5 and B2.
6. **Items 3, 9, 12** — resolver classes C3–C5 and the new chapter classes logged under rulings 40/58, never edited; ruling 55 measured;
   ruling 43's `Contra:` job stays parked. Nod.

---

## ▶ THE 12-ITEM RUNNING LIST — ACCOUNTED FOR

| item | where on this sheet |
|---|---|
| (1) *supplicium* | **A1** (25 sites; census extended to c1–c12 as owed) |
| (2) ruling 57's C1 job + diff | **OWED before the deploy** — not run (tool untouched since `dfb5adb`); not this gate's repair |
| (3) C3–C5 + new resolver classes | C6 — logged, parked (ruling 58) |
| (4) the verse test | **A3** (Job 24:13) + the four other sites, confirmed |
| (5) `tr-doctrina` | C2 (ruling 53) — 11 of 11 units |
| (6) misprint brackets | **A4** (*dati*) + C3 (21 brackets) |
| (7) ruling 50 | C2 — three over-runs, kept |
| (8) ruling 51 | **A6** (61; c16's sibling added) |
| (9) ruling 55 | C6 — nothing for Wilson |
| (10) the close and the Scholion | C4 |
| (11) the Schemata | **A5** (*de merito*) + **B2** (`tr-studium`) + C5 |
| (12) ruling 43's parked job | C6 — stays parked |

New, not on the list: **A7** (*tormentum* at two Douay sites), **B1** (ruling 44 before c3), the c1 p. 117 *poena* → "penalty" (inside A1),
the c16 `Obiectio` sibling (inside A6), B3.

---

## ▶ REGISTER CENSUS, c13–c19 + Schemata (rendered regions; Latin body+app → English)

| term | c13 | c14 | c15 | c16 | c17 | c18 | c19 | Schem. | verdict |
|---|---|---|---|---|---|---|---|---|---|
| *supplicium* | 1 | 0 | 0 | 3 | 1 | 0 (*supplicatio* 2) | 0 | 4 | **A1** |
| *punitio* → punishing | 3/3 | 2/2 | 0 | 8/8 | 2/2 | 4/4 | 11/11 | 3/3 | ✓ (ruling 44) |
| *poena* (body+app) | 7 | 9+1 | 1 | 21+1 | 10+1 | 10 | 2+1 | 10 | → punishment ✓ |
| *lumen* / `tr-lumen` | 0 | 1 ✓ | 0 | 0+1 ✓ | 9 ✓ | 3 ✓ | 1 ✓ | 0 | ✓ (A3) |
| *doctrina* / note | 0 | 0 | 1 ✓ | 0 | 0 | 0 | 0 | 1 ✓ | ✓ |
| *studium* / note | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 **✗** | **B2** |
| *vaca-* / note | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 ✓ | ✓ |
| *intellect-* / bare | 4/0 | 1/0 | 2/0 | 0 | 0 | 2/0 | 0 | 0 | ✓ |
| *impius* → impious | 0 | 4 | 3 | 7 | 0 | 2 | 5 | 1 | ✓ |
| *idol-* / *simulacr-* | 12 | 74 | 45 | 3 | 0 | 0 | 1 | 5 | ruling 32 ✓ |
| *tormentum* etc. → torment | 0 | 3 | 0 | 7 | 2 | 0 | 1 | 0 | ✓ (A7 is c5/c11) |

Whole work: `tr-` notes **29** — prooem 4 (lumen, studium, vacare, doctrina) · c1 2 · c2 2 · c3 1 · c4 1 · c5 2 · c6 3 · c7 2 · c8 2 · c10 1 ·
c11 1 · c14 1 · c15 1 · c16 1 · c17 1 · c18 1 · c19 1 · Schemata 2 (+1 if B2).
