# Vol VI *Collationes in Evangelium S. Ioannis* WORK-CLOSE GATE (p. 634, ruling 123): EVIDENCE SHEET

**STATUS: OPEN — awaiting Wilson's rulings.** Compiled 2026-11-07 by a read-only agent on Wilson's go ("Run the gate"). No file under
`vol*/` was edited; no tool, ledger, registry, `build-progress.mjs` or resume note was touched; nothing pushed, deployed or stashed; no
plate deleted. Baseline and passes 1–3: `manual-review/vol6-cioan-workclose-gate-passes.md`.

**Scope: 22 chunks, `bon-cioan-c1` … `bon-cioan-app`, pp. 535–634, 889 numbered entries + 22 `tr-` notes.** The W-list is the resume
note's (W1–W61 + W-auth); W4 is fixed, W10 was closed by `b199bc8`, W45 by ruling 136. **Proposed rulings are numbered from 137.**
Line numbers are those of the files at `63b71d9`. Every census is over the RENDERED regions (`## Latin`, `## English`, `## Apparatus`);
frontmatter and `## Notes` excluded.

**Carried statements REFUTED or corrected as worded (found at this gate):**
- **W18 / the brief's "c8 'the light of life' vs c10 'the lumen of life'"** — there is no such pair. `bon-cioan-c8` never quotes John
  8:12b; it quotes 8:12a *Ego sum lux mundi* → "I am the light of the world" (*lux*). The only "light of life" in Vol VI is
  `bon-ioan-c8-v12-20` ¶'s *in futuro erit **lux** vitae* (*lux*, correctly "light"). Every *lumen vitae* in Vol VI — the *Ioannem*
  lemma, c10 Coll. XL ¶ 10, the Appendix's Annot. 1 — reads "the lumen of life". (Ruling 138.)
- **W21 "at all 80 sites"** — 75. Five *infirm-* sites in c11 are "sick", one of them the lemma John 11:3 that W21 says was adjusted.
  (Ruling 139.)
- **W11's PRINTED_SLIPS row as written (`apparatus:p574-4 · Ioan 8:26`) would be STALE** — the ledger has no apparatus record for
  p. 574 n. 4's `Vers. 26`; the slip lives in the **body-join** record `latin_body · p574-4 · Ioannis octavo → Ioan 8:26`. **W49's row
  as written (`Isa 32:17`) would be STALE too** — the ledger's target string is `Isai 32:17`. (Ruling 145.)
- **Two of the five *Ioannem* citation rows queued at ruling 113 cannot be written** — p. 472 n. 4 (`infra n. 31`) and p. 473 n. 3
  (`29, 11`) emit no ledger record, so a row would report "matched 0 records". (Ruling 145.)
- **The index slips (ruling 120) cannot be PRINTED_SLIPS rows at all**: the volume index is in no ledger record. (Ruling 146.)
- **W23 is half fixed already**: p. 593 n. 6's `et XL. n. 1.` now resolves to `bon-cioan-c10` (record present). Only the lower-case
  `supra coll. XVIII.` (p. 589 n. 4) is left. (Ruling 147(d).)
- **W-auth: Du Cange, Forcellini and Mone are in `not_authorities` by design** — they are not gaps. (Ruling 148.)
- **The resume's plate inventory is stale**: 75 plates `p-560` … `p-634` (168 MB) are on disk, not 16. (Ruling 151.)
- **NEW, not on the W-list:** "Holy Ghost" ×2 in c21 (ruling 80(b)); "judgment" ×39 and "recognise" ×4 against ruling 101 N9.

---

## ▶ ONE-SCREEN SUMMARY

| # | item(s) | recommendation | lines if adopted | kind |
|---|---|---|---|---|
| **137** | **W57** Appendix breadcrumb | **type-first `appendix` branch → "Appendix"** (alt: `division === 22` case; keep "Cap. 22") | 1 code line + comment in `build-content.mjs`; 1 built title | ⚖ Wilson's call |
| **138** | **W18 (John 8:12)**, W58, *lumen* census | **c10 is right ("the lumen of life"); no inconsistency exists; ratify W18's *lumen* half and W58** | 0 | ratify |
| **139** | W21 residue (c11) | **conform the 5 "sick" sites to the family** | 5 sites / 4 English lines | per-site |
| **140** | ruling-93 families W2 W5 W15 W18 W24 W27 W29 W32 W33 W35 W39 W43 W50 W56 W61 | **ratify as built**; by-passage splits ratified under ruling 61 | 0 | ratify |
| **141** | **W1** Ps. 59:4 | **by passage: c5 L181 → "Heal thou the contritions thereof"; L157 keeps the Douay** (builder kept both) | 1 | ⚖ differs from builder |
| **142** | W12, W13 | ratify *doctrina* → "learning" (+ `tr-doctrina`); W13 record | 0 | ratify |
| **143** | NEW "Holy Ghost" ×2 (c21) | **conform to "Holy Spirit"** (ruling 80(b)) | 2 | per-site |
| **144** | NEW spelling | ⚖ **conform "judgment" ×39 → "judgement" (17 lines) and "recognise" ×4 → "recognize" (3 lines)** per ruling 101 N9; alt record-only (Vols I–V write "judgment") | 20 | ⚖ close call |
| **145** | PRINTED_SLIPS: W8 W11 W14 W17 W20 W26 W49 + ruling 126's two + *Ioannem*'s | **14 rows** (9 this work, 5 *Ioannem*), W11/W49 rows corrected; 5 queued items not rowable | ~28 tool lines; 0 records move; annotated 6 → 20 | tool |
| **146** | index slips W38 W42 W46 W52 + Coll. I 536 | **record as an INDEX SLIPS list in the gate record + pilot-setup ruling; no tool row** | 0 | record |
| **147** | resolver D1–D7, W23 W37 W41 W51 | **at this gate: D7, D2, W23, W41, W37** (each with a before/after diff); **D1 (4) / D4 / D5 / D6-W51 stay queued for one resolver session** | tool | ⚖ scope |
| **148** | W-auth (c9–app) | **ONE table edit: 6 scoped entries (+8 records, 0 removed)**; ⚖ genitive sigla (+196 / −4 corpus-wide) as a separate yes/no | `authorities.json` only | tool / ⚖ |
| **149** | W53 p. 632 n. 3 | **ratify ownership by anchor (plate confirms)** | 0 | ratify |
| **150** | record-only W3 W6 W7 W9 W10 W16 W19 W22 W25 W28 W30 W31 W34 W36 W40 W44 W47 W48 W54 W55 W59 W60 (+ W4) | **ratify as built** | 0 | record |
| **151** | housekeeping | `complete: true`; Pass 4 = all 75 plates | 1 + deletions | — |
| **152** | close | suite re-run vs the baseline | — | — |

**If every recommendation is taken: ~32 English lines (4 + 1 + 2 + 20 + the Appendix title) and 0 `**La.**` halves, 0 `## Latin`
lines; 1 code line in `build-content.mjs`; 1 line in `build-progress.mjs`; 14 PRINTED_SLIPS rows; the resolver jobs of 147; one
`authorities.json` edit.** ⚠ Real decisions for Wilson: **137** (breadcrumb), **141** (W1, where I differ from the builder), **144**
(spelling — corpus is split), **147** (how much resolver work runs before the deploy), **148(b)** (genitive sigla).

---

## 137. W57 — THE DIVISION-22 BREADCRUMB

**Evidence.** `content.json` gives `bon-cioan-app` the title **"Cap. 22"** (`buildWorkChunkTitle`, `build-content.mjs` L1103–1106:
`if (meta.division === 19) return "Cap. 18–19"; return \`Cap. ${meta.division}\`;`). The chunk is `type: appendix` — **the only chunk
in the corpus with that type** (grep). Registry division 22 = `"Appendix"`; ruling 122 names it "22 (Appendix)"; the plate's heading is
`APPENDIX.⁴` and p. 632's running head reads `APPENDIX COLL. I.` (read this pass). John has 21 chapters, so "Cap. 22" names a chapter
that does not exist. The builder already has type-first branches for units that are not chapters: `capitula` → "Capitula", `scholion`
→ "Scholion", `schemata` → "Schemata", `opusculum`, `tractatus`, `prooemium`, `expositio` (L1069–1092) — `bon-ioan-scholion` (division
22 of *Ioannem*) renders "Scholion", not "Cap. 22".

**Alternatives.**
- **(a) type-first branch** beside `schemata`: `if (meta.type === "appendix") return "Appendix";` — 1 code line (+ the L1101 comment
  "The Appendix (22) is to be decided" rewritten). Blast radius: 1 chunk today; any future `type: appendix` chunk names itself the same way.
- (b) `if (meta.division === 22) return "Appendix";` inside the `collationes-ioannem` branch — the ruling-136 shape; same output, scoped to the work.
- (c) keep "Cap. 22" — 0 lines; the breadcrumb asserts a 22nd chapter.

**▶ RECOMMENDATION: (a)** — it is the corpus's own pattern for a non-chapter unit, and the type already says what the unit is. (b) is
equally safe. Verification: diff the built titles of the 22 `bon-cioan-` chunks — exactly one line changes, `Cap. 22` → `Appendix`.

## 138. W18 (JOHN 8:12), W58, AND THE *LUMEN* CENSUS OF THE WHOLE WORK

**The test (ruling 125):** a verse quoted only as a verse, which no surrounding prose leans on, keeps the Douay "light"; where the prose
leans on *lumen*, "lumen" stands.

**John 8:12 across Vol VI (every site):**

| site | Latin | English | prose leaning? | verdict |
|---|---|---|---|---|
| `bon-cioan-c8` Notes register (8:12a) | *Ego sum lux mundi* | "I am the light of the world" | *lux* — not a *lumen* site | ✓ |
| `bon-cioan-c10` L102/L183 (Coll. XL ¶ 10) | *Lumen iucunditatis;* Ioannis octavo: « … sed habebit **lumen vitae** » | "*The lumen of joyfulness*[^tr-lumen]; John, the eighth chapter: « … but shall have **the lumen of life** »" | **yes** — the verse is the proof-text of the division term *Lumen iucunditatis*, which takes its noun from it | **"lumen" right** |
| `bon-ioan-c8-v12-20` L36/L103 (lemma) | *Sed habebit lumen vitae* | "But shall have the lumen of life" | the lemma (ruling 74) | ✓ |
| `bon-ioan-c8-v12-20` (same ¶) | *in futuro erit **lux** vitae* | "a light of life" | *lux* | ✓ |
| `bon-cioan-app` L33/L80 (Annot. 1) | *propter hoc dicitur lumen vitae* | "the lumen of life" | Bonaventure's own prose (W58) | ✓ |

**So: c10 is right and there is nothing to conform.** "Light" at c10 would make the prose's *Lumen iucunditatis* ("the lumen of
joyfulness") prove itself by "the light of life" — exactly c1's Isa. 60:1 case at ruling 125. **0 lines.**

**The whole work (pass 2): 12 body units + 2 apparatus entries carry *lumen*, every quoted one decided by the test, consistently:**
exempt → "light": Eph. 5:13 (c1), Tob. 5:12 ×3 (c1 ¶ 7, c9 Coll. XXXVII ¶ 4, app Annot. 1), Ps. 37:11 (c5 Annot. 18), Job 24:13 (c3),
Ps. 35:10 (c4), Eccle. 11:7 (app); leaned on → "lumen": Isa. 60:1, Ps. 4:7 (c1), John 8:12 (c10), Acts 12:7 (c11 Annot. 39, *lumine,
pulsu, clamore* … *ecce, primum*), the Appendix's two prose sites. `tr-lumen` present in all 9 chunks with a live *lumen*.
**▶ RECOMMENDATION: ratify W18's *lumen* half and W58 as built. 0 lines.**

## 139. W21 — THE FIVE *INFIRM-* SITES IN CAPITULUM XI LEFT AS "SICK"

W21 claims *infirmitas / infirmari* → "infirmity / be made infirm" "at all 80 sites" of Capitulum XI. Aligned count: **80 Latin → 75**.

| line | Latin | English as built | why it leans |
|---|---|---|---|
| L215 | *Infirmatur homo in delectatione; quod figuratum est, Ioannis quarto, in filio [reguli], qui **infirmabatur** Capharnaum* (John 4:46) | "who « was sick at Capharnaum »" | the verse is adduced as the figure of the prose's own *Infirmatur homo* one clause before ("*is made infirm*") |
| L220 | *hic describitur **infirmus** ex nomine et loco et genere* | "here the sick man is described" | prose |
| L226 | *Necessitas **infirmi**, cum dicitur: **infirmatur*** | "The need of the sick man, when it is said: *is sick*" | **same paragraph opens "*the need of the infirm man*"**; and *infirmatur* is the lemma John 11:3, which W21 says reads "is infirm" |
| L230 | Ecclus. 7:39 *Non te pigeat visitare **infirmum**. Ex his enim in dilectione firmaberis* | "Be not slow to visit the sick. For by these things thou shalt be confirmed in dilection" | *De hac potest exponi* — the verse is expounded of the prose's *infirmitas tribulationis*; and W21 already adjusted *dilectio* in this very verse |

**Alternatives.** (a) conform all five → "the infirm man" ×2, "*is infirm*", "was infirm at Capharnaum", "to visit the infirm": **5 sites
on 4 lines** (L215, L220, L226, L230). (b) conform only L220/L226 (prose + lemma; 3 sites, 2 lines), ratify John 4:46 and Ecclus. 7:39 as
verses. (c) record only — c11 then says "infirm man … sick man … is sick" inside one paragraph.
**▶ RECOMMENDATION: (a).** Notes: c11's W21 line corrected ("80 sites" true after the edit). (c4 / c5 render *infirmitas* "sickness /
sick" by passage — 13 of c4's 35, c5's 4 — before the family was formed; by ruling 61 they stand.)

## 140. THE RULING-93 FAMILY BLOCK (W2, W5, W15, W18, W24, W27, W29, W32, W33, W35, W39, W43, W50, W56, W61)

**The rule** (ruling 93, carried by 121): the Douay is adjusted to Bonaventure's word where the exposition leans on it; where nothing
leans, the Douay stands; decided by passage (ruling 61).

**Census in the claiming chunk (Latin family tokens → English family word, aligned paragraph by paragraph; Pass 2):** *vivificare* c5
23 · *trahere* c6 51/51 · *lutum* c9 65/65 · *exaltare* c12 60/61 · *transire* c13 29/31 · *tradere* c13 11/11 · *advocatus* c14 21/21 ·
*manere* c15 15/15 · *arguere* c16 33/33 · *tristitia* c16 68/70 · *clarificare / claritas* c17 28/28 · *calix* c18 23/24 · *tradere* c18-19
31/46 · *illudere* c18-19 50/52 · *monumentum* c18-19 8/8 · *ascendere* c20 45/46 · *manifestare* c21 4/4 · *conflare* app 6/6. **No
short paragraph anywhere except W21's (ruling 139).**

**By-passage splits inside the work, all ruling-61-shaped (the verse leaned on in one chapter, quoted as a verse in another):** Prov.
23:30 "cups" (c2) / "chalices" (c18) · John 19:41 "sepulchre" (c18) / "monument" (c18-19) · *virtus* "virtue" (c11, II Cor. 12:9) /
"power" (c14) · *infirmitas* "sick(ness)" (c4, c5) / "infirm(ity)" (c11) · *tradere* "betrayal" (c2 prose *proditio*, a different word).
**▶ RECOMMENDATION: ratify the block as built. 0 lines.**

## 141. W1 — Ps. 59:4 *SANA CONTRITIONES EIUS*

| line | context | English as built | leans? |
|---|---|---|---|
| c5 L35/L157 (Coll. XX) | *commotio aquae … commotio mentis humanae ad dolorem vel compunctionem; de qua commotione Psalmus: « Sana contritiones eius, quia commota est »* | "Heal thou the breaches thereof, for it has been moved" | on *commota* (the prose's *commotio*), **not** on *contritiones* → Douay stands |
| c5 L58/L181 (Coll. XXI ¶ 2) | *Medicina praeparativa est **dolor contritionis**, et per hanc sanatur infirmus; unde Psalmista: « Sana contritiones eius… »* | "Heal thou the breaches thereof" | **yes** — the verse proves *dolor contritionis* |

Corpus: `bon-sent-IV-d17-p1-a1-q3` keeps "heal thou the breaches thereof".
**Alternatives.** (a) by passage: **L181 → "Heal thou the contritions thereof"**, L157 unchanged — 1 line. (b) keep both (the builder's
choice) — 0 lines; the medicine of contrition is proved by "breaches". (c) both "contritions" — 2 lines; L157 then departs where nothing leans.
**▶ RECOMMENDATION: (a)** — ruling 93's own test gives it, and W1 itself says so. ⚠ **This differs from the builder's choice.**

## 142. W12, W13

**W12** *doctrina* → "learning" at Coll. XXXVI ¶ 5 (*Praelatio sine doctrina … gladius in manu stulti*), with `tr-doctrina`
explaining: ruling 53 decides *doctrina* by sense and asks only that the note say so; `tr-doctrina` stands in all 11 chunks carrying
the word. **W13** (Tit. 2:12 Douay "ungodliness … godly", a verse; *supplicium* "penalty" beside *poena* "punishment" — ruling 101;
*tria* introducing four; Matt. 24:45 *tuam*) record-only. **▶ Ratify both. 0 lines.**

## 143. NEW — "HOLY GHOST" ×2 IN c21 (ruling 80(b))

Ruling 80(b): **"Holy Spirit" everywhere, Douay quotations included** (Vols I–IV have none). c21 L333 John 3:5 *…ex aqua et Spiritu
Sancto…* → "…of water and the Holy Ghost…"; L370 Acts 7:55 → "But Stephen being full of the Holy Ghost". The work's other 36 rendered
sites read "Holy Spirit". **▶ Conform both: 2 lines.**

## 144. NEW, ⚖ — SPELLING: "judgment" ×39, "recognise" ×4 (ruling 101 N9)

Ruling 101 N9 (*Ioannem* p. 466 gate) conformed "judgement ×4, honour ×2, recognized ×1"; ruling 121 carries every *Ioannem* ruling.
This work: **"judgment(s)" 39 sites on 17 lines** — c1 L292, L297 (3) · **c7 L132 L134 L136 L138 L142 L147 L149 L151 L153 L155 L157
L203 L249 (34; Coll. XXXI on John 7:24)** · c12 L239 · c13 L135 — against "judgement" 54 (c2–c5, c16, c18, c21); "honour" only (0
"honor"); **"recognise / recognises / recognised" 4 sites on 3 lines** (c3 L147 ×2, c8 L252, c18-19 L132) against "recognized" 1 (c10).
⚠ **The corpus is split:** Vol VI "judgement" 387 / "judgment" 128 (*Ioannem* 176 / 21 even after ruling 101); **Vols I–V "judgment"
1,145 / "judgement" 254** (whole files); "recognize" 38 / "recognise" 17 in Vol VI.
**Alternatives.** (a) conform this work to ruling 101's forms: 43 sites on 20 lines (scripted, single-word, English only, Notes excluded).
(b) record-only — spelling is not uniform across the corpus and no ruling makes it so outside its scope. (c) a corpus-wide spelling
decision later (one pass, every volume).
**▶ RECOMMENDATION: (a)**, since ruling 121 carries ruling 101 and the work is otherwise uniform within each chunk except c1 / c7 /
c12 / c13. ⚖ **Close call** — Wilson may prefer (c), which would leave this work as it is now and fix all volumes together.

## 145. PRINTED_SLIPS ROWS (ruling 57 C2 / 126) — W8, W11, W14, W17, W20, W26, W49 + ruling 126's two + the *Ioannem* queue

`apply_printed_slips` **annotates, never corrects**: a row must match exactly one ledger record (chunk, section, anchor label, target
as filed), or the QA report prints "⚠ … table is stale". Each row below was checked against `index/citations.tsv`: **1 match each.**

| # | chunk | section | anchor | filed | meant | W |
|---|---|---|---|---|---|---|
| 1 | `bon-cioan-c1` | `apparatus:p537-6` | p537-6 | `Ps 75:2` | `Ps 75:3` | r. 126 |
| 2 | `bon-cioan-c4` | `apparatus:p556-1` | p556-1 | `Luc 16:10` | `Luc 16:19` | r. 126 |
| 3 | `bon-cioan-c7` | `apparatus:p571-1` | p571-1 | `Exod 3:8` | `Exod 23:8` | W8 |
| 4 | `bon-cioan-c8` | **`latin_body`** | p574-4 | `Ioan 8:26` | `Ioan 8:16` | **W11 — corrected** (the slip is the body-join record `Ioannis octavo` + n. 4's `Vers. 26.`) |
| 5 | `bon-cioan-c9` | `apparatus:p580-4` | p580-4 | `Ps 39:2` | `Ps 39:3` | W14 |
| 6 | `bon-cioan-c10` | `apparatus:p583-9` | p583-9 | `Ps 79:1` | `Ps 79:2` | W17 |
| 7 | `bon-cioan-c11` | `apparatus:p590-8` | p590-8 | `Ps 115:5` | `Ps 115:15` | W20 |
| 8 | `bon-cioan-c13` | `apparatus:p598-2` | p598-2 | `Ps 44:3` | `Ps 44:4` | W26 |
| 9 | `bon-cioan-c20` | `apparatus:p622-4` | p622-4 | **`Isai 32:17`** | `Isai 32:18` | **W49 — corrected** (`Isa` would be stale) |
| 10 | `bon-ioan-c17-v20-23` | `apparatus:p474-9` | p474-9 | `Gal 3:18` | `Gal 3:28` | r. 113 |
| 11 | `bon-ioan-c18-v4-12` | `apparatus:p481-8` | p481-8 | `Act 3:3` | `Act 4:3` | r. 113 (5:18 emits no record) |
| 12 | `bon-ioan-c20-v26-31` | `apparatus:p518-11` | p518-11 | `2Cor 15:53` | `1Cor 15:53` | r. 113 (the one QA line) |
| 13 | `bon-ioan-c11-v1-6` | `apparatus:p397-9` | p397-9 | `Luc 8:7` | `Luc 8:2` | r. 103 |
| 14 | `bon-ioan-c13-v21-30` | `apparatus:p432-9` | p432-9 | `bon-ioan-c14-v1-14` | `bon-ioan-c13-v21-30` (p. 430 n. 7) | r. 103 — **a crossref to a WRONG CHUNK**, annotated |

**Not rowable (no ledger record to annotate):** p. 472 n. 4 (`infra n. 31`), p. 473 n. 3 (`29, 11`), the three name slips (`Chysostomus`,
`Caipbae`, `Corranus`). p. 500 n. 7 (`supra pag. 492`) already binds the right chunk (`bon-ioan-c19-v1-16` owns both p. 492 n. 2 and
p. 493 n. 2): no row. The c7 body record `Exodi vigesimo tertio → Exod 23:3` is correct (n. 1's `Vers. 3.`), not a slip.
**Expected effect:** ledger and QA flag count unchanged (35,240 / 211); "printed slips 6 annotated, 0 stale" → **20 annotated, 0
stale**; the QA report gains 14 annotation lines. **▶ RECOMMENDATION: add the 14 rows (~28 lines in `tools/build-citations.py`).**

## 146. INDEX SLIPS (ruling 120) — W38, W42, W46, W52, and the pilot's Coll. I

| item | index (PDF 682, p. 640) prints | plate | W |
|---|---|---|---|
| Coll. I | 536 | **535** | pilot |
| Cap. XVIII | `LXXI. (Vers. 36.) 615` | **`COLLATIO LXVI.`** p. 614 (two LXXIs, no LXVI) | W38 |
| Annot. 69 | `(Vers. 19)` | **`(Cap. 19, 29.)`** p. 618 | W42 |
| Cap. XX + Annot. 70 | "ib." = 618 | **619** | W42 |
| Annot. 71 | `(Vers. 13.)` | **`(Vers. 15.)`** p. 622 | W46 |
| Coll. LXXVI | `(Vers. 15.)` | **`(Vers. 17.)`** p. 624 | W52 |
| (Annot. 52) | 601 | 601 — measured right | W28 |

The volume index is not chunked and produces no ledger record, so a PRINTED_SLIPS row would match nothing. **▶ RECOMMENDATION:** read
ruling 120's "PRINTED_SLIPS-class rows" as *recorded in that form*: the table above goes into the closed gate record and the ruling
text; never normalised; 0 tool lines (the chunks' Notes already carry each one). Alt: a doc-only `INDEX_SLIPS` list in
`build-citations.py` (~8 lines, read by nothing).

## 147. RESOLVER DOCKET (rulings 82(a), 94, 103, 113, 126, 128) — NO TEXT EDIT; MEASURED DELTAS

| job | definition | sites | expected ledger delta | in this work |
|---|---|---|---|---|
| **D7** (r. 128) | `Hexa[eë]m\w*\.\s*(\(tom\. V\.\)\s*)?collat\.\s*N` + `hexaemeron` `chunk_pattern` `bon-hex-coll{coll}` → `bon-hex-c{coll}` **in the same diff** + ruling-116 guard widened | **84 = 83 add + 1 refine** (Vol V 73, Vol VI 11) — re-counted this pass, unchanged | **+83 crossref records** to `bon-hex-cN`; `forward` stays 3 (without the pattern fix: +84 false forwards) | c1 p. 541 n. 5 (1) |
| **D2** (r. 94) | *primae / secundae / tertiae Ioannis* read as the Gospel | ***Ioannem* 16 + 6 queued; this work 27 body sites** | retarget ≥31 records `Ioan` → `1Ioan`/`2Ioan`/`3Ioan`, 0 added | **27 body sites; ≥9 bound to the Gospel at confidence B with a verse:** p543-1 (`Ioan 4:16`), p602-5 (`Ioan 2:3`), p603-1 (`Ioan 2:1`), p604-7 (`Ioan 1:9`), p604-9 (`Ioan 4:15`), p604-10 (`Ioan 3:21`), p605-6 (`Ioan 3:15`), p607-3 (`Ioan 3:18`), p613-5 (`Ioan 2:23`); the rest chapter-level C |
| **D1 + (4)** (r. 94/103/113) | cross-note anaphora onto Scripture at A / a wrong `chunk`; `Tom. V.` wrong chunk | *Ioannem* 33 + 12 as banked (10 + 2 to a WRONG CHUNK) | per-site retargets; some → unresolvable | **0 new**: all 41 anaphora records in this work bind inside their own note or to the body sentence carrying the anchor (checked one by one) |
| **W23** | lower-case `supra coll. N.` unread by the ruling-116 scanner | **1** (p. 589 n. 4 `supra coll. XVIII.`) — the only lower-case `coll.` cross-reference in the corpus | **+1** crossref → `bon-cioan-c4` | the `et XL. n. 1.` half is **already fixed** (→ `bon-cioan-c10`) |
| **W37** | `ibid. [a. N.] q. N` keeps the antecedent's question | **20 such sites corpus-wide; ≤14 bound to another question** (incl. p. 610 n. 1 → `II-d27-a2-q1` for q. 2, and D1's p. 514 n. 1) | ≤14 retargets, 0 added (per-site confirmation in the diff) | 1 |
| **W41** | point-for-comma `Book N. M.` filed chapter-level | **29 records corpus-wide** (Vols I–VI) | 29 refined chapter → verse, C → A; 0 added | 2 (p. 613 n. 1 `Ps. 10. 7.`, p. 559 n. 4 `Eccli. 26. 15`) |
| **W51 / D6** | bare `Vers. N; ibid. v. M` (no book in the note) | **28 unresolved corpus-wide** (*Ioannem* 14, Sent. 8, Eccl. 3, Sap 1, Praec. 1, this work 1) | anaphora unresolved 286 → ≥258; ≤+28 scripture records, taking the chapter from the body-join or the lemma — ruling 57 C1's "look back past a non-scripture antecedent" applied | 1 (p. 622 n. 7) |
| **D4** | roman book numeral unemitted (`Reg*`, `Cor*` …) | this work **144** (Reg* 45 · Cor* 42 · Petr* 22 · Mach* 12 · Tim* 9 · Par* 6 · Thess* 5 · Esdr* 3); *Ioannem* 19 + 72 | refine only | 144 |
| **D5** | body ordinal with no record (*ultimo*, nominative evangelist) | *Ioannem* ~63 + 24; not re-censused here | adds | — |

**Alternatives.** (a) **at this gate, before the deploy: D7, D2, W23, W41, W37** — five mechanical classes, each with a before/after
ledger diff for Wilson; **D1 + (4), D4, D5, D6/W51 stay queued for one resolver session after the deploy** (D1 needs per-site
judgement on 45 records; D6 changes ruling 57 C1's "right not to guess" practice). (b) everything now, per the resume's housekeeping
step 4 — the largest diff the ledger has had; delays the deploy. (c) nothing now; all queued. **▶ RECOMMENDATION: (a).** ⚖ Wilson's
scope call — the resume's step 4 reads as (b).

## 148. W-AUTH — THE ONE `authorities.json` EDIT (prototyped on a scratch copy; nothing in `tools/` touched)

**(a) Scoped additions — measured: 17,118 → 17,126 (+8, 0 removed); to-a-work 16,776 → 16,784.**

| entry | added records |
|---|---|
| `bernard` work `sermo-in-assumptione` ("Serm. in Assumt. B. Mariae", "Serm. in Assumpt. B. Mariae") | c17 p. 609 n. 4 (pseudo via *inter opera Bernard.*) |
| `augustine` work `manuale` ("Manuale", pseudo) | `bon-ioan-c17-v24-26` p. 477 n. 1 (c17 p. 610 n. 11's needs (b)) |
| `jerome` `in-ieremiam` abbrev + **"Comment. in Ier."** only | app p. 633 n. 7; `bon-sap-c5` p. 143 n. 2 — ⚠ **NOT "in Ier."**: tried, it false-matches *in Ierusalem* (`bon-eccl-c2-v4-10` p. 23 n. 5, `bon-ioan-c5-v1-9` p. 304 n. 1) |
| NEW `juvenal` (sigla "Iuvenal.", "Iuvenalis"; work `satirae` "Satyra", "Sat.") | c12 p. 596 n. 4; `bon-sent-II-d38-a1-q4` n. 4 |
| NEW `vitae-patrum` (sigla "de Vitis Patrum", "Vitae Patrum", "Vitis Patrum"; default work) | c17 p. 610 n. 8; `bon-sent-IV-d20-p1-a1-q5` n. 8 |
| `bernard` work `meditationes-piissimae` ("Meditation. piissimis de cognitione humanae conditionis", pseudo) | lands only with (b) (c11 p. 588 n. 7 names *inter opera Bernardi*) |

**(b) ⚖ Genitive sigla `Dionysii`, `Augustini`, `Bernardi`** — measured: **+196 / −4 corpus-wide** (all volumes; Augustine 141, Bernard
39, Dionysius 16); in this work +6 (app p. 632 nn. 4–5 *De div. nom.*, c11 p. 588 n. 7 *Meditationes*, c17 p. 610 n. 11 *De spiritu
et anima* + *Manuale*, c2 p. 549 n. 4). Random sample of 12 added records: **12 genuine** (`Augustini … Serm. 95. n. 5`, `Bernardi … de
Praecepto et dispens. c. 14`, `Dionysii … de Div. Nom. c. 4` …). A corpus-wide change: it needs the full before/after sample the
housekeeping step names, not a 12-row one.

**(c) No entry, by reason:** Du Cange (p. 615 n. 9, p. 627 n. 5), Forcellini (p. 618 n. 2), Mone (p. 620 n. 2) — **already in
`not_authorities` by design** (lexicographers / editors). The Roman Breviary (p. 614 n. 6), the Office of One Martyr (p. 626 n. 2), the
hymn *Iesu corona virginum* (p. 633 n. 3) — a `breviarium-romanum` entry was prototyped and **adds nothing** (no locus shape), so
omitted; record-only. **Tool-side, not table:** Hugh of Saint-Cher (p. 623 n. 6, title *before* the author outside a parenthesis);
ps.-Ambrose *Ep.* 1 (p. 625 n. 3, `in appendice operum S. Ambrosii` — `INTER_OPERA_RE` needs `operum`). **No work named:** Gregory
(p. 593 n. 3 `Sententia Gregorii … supra pag. 203`), Lombard (p. 590 n. 3's bracket), Gregory on I Kings (p. 610 n. 6), Jerome on
Malachi (p. 628 n. 11 `in hunc locum`, same-passage author-level), Augustine *Enarrat. in Ps. 85* (p. 610 n. 11, no siglum).
**▶ RECOMMENDATION: (a) as the one edit + `build-authorities.py` + a fresh sample; (b) only on Wilson's yes, with a full sample.**

## 149. W53 — p. 632 n. 3 TO c21 BY ANCHOR

`bon-cioan-c21` L766 holds `[^p632-3]` in full (codex C's *Finitur. Amen.*, the *Vita nostra comparatur* schema, the *index rerum*
note); its anchor is c21's last words, *visio salutaris*³ (**read on the plate this pass**: p. 632 right column, the line above the
full-measure `APPENDIX.⁴`). `bon-cioan-app`'s n. 4 opens *In cod. A, ut supra nota 3. iam diximus* and its Notes point to c21. Ruling
118's "p. 632 n. 3 … in full" is satisfied as extent; "split the register by anchor" decides ownership. **▶ Ratify. 0 lines.**

## 150. RECORD-ONLY BLOCK — ratify as built, 0 lines

W3 (Coll. XXV `(Vers. 28. 25.)`) · W4 (fixed after c5; record) · W6 (*panis* / *panes*) · W7 (John 6:44's *qui in caelis est*) · W9
(*punitio* / *poena*) · W10 (closed by `b199bc8`: `ioan-paragraph` records present ×4) · W16 · W19 · W22 · W25 (incl. the Lucan-like
couplet, ruling 127's class) · W28 · W30, W34, W36, W40, W44 (the anchored Cap. XV / XVII / joint XVIII–XIX headings — confirmed in
the files; splits 2/8, 1/9, 7/1, 4/6, 5/4 confirmed in Pass 3) · W31 (Cap. XV, annotationes only) · W47 (Coll. LXXIII's `3.` twice —
confirmed, c20 L64/L66) · W48 · W54 (*conservantis*) · **W55** (no `PRINTED_QUERIES` row: `[sive ?]` has no bare `[?]` token, so a row
would never fire) · W59 · W60. The banked italic sites (COLLECTION CHANGE) stay banked; no discriminator proposed.

## 151. HOUSEKEEPING (after the rulings, in the resume's order)

1. `site/scripts/build-progress.mjs` L190 `complete: false` → `true` (1 line). 2. Pass 4: **delete all 75 plates `raw/vision/vol6/p-560.png`
… `p-634.png` (168 MB)** — the resume's list of 16 is stale; there is no next chunk to keep a leaf for; `/tmp/colcrop` is already empty.
3. Ruling text into `manual-review/vol6-pilot-setup.md`; the closed record; the resume note's START HERE. 4. Then the deploy stop.

## 152. CLOSE

Suite re-run in the build order against the baseline in the passes file. Predicted: ledger +83 (D7) +1 (W23) if 147(a); refinements
from D2 / W37 / W41 visible only in the diff; QA 211 → 211 ± the D2 / W41 lines; printed slips 20 / 0 stale; authorities 17,126 (a) or
~17,318 (a)+(b); content 2,317 / 2,317; English-only edits move no ledger record.
