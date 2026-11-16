# Vol VII *Lucam* p. 381 gate: passes 1-3 DRAFT (read-only agent, 2026-11-16)

Uncommitted. No chunk, tool, manifest, ruling file, resume note or plate was edited, committed or deleted. Nothing was pushed or deployed, and `site/.vercel/output` was left alone. Register questions to Wilson belong to the evidence sheet, not this one. Model: `vol7-lucam-p288-gate-passes-draft.md` (and the p. 188 one before it). Pass 3 is the read-through and consistency pass as briefed: file-side parity, register census incl. rulings 63-76, `tr-` inventory, frontmatter continuity, hand-offs. No plate was read in this run.

**Scope:** 82 chunks, pp. 3-381, **4,429 numbered apparatus entries** + **62** `tr-` notes. The new ground is the 19 chunks `bon-luc-c11-v14-26` → `bon-luc-c14-v25-35`, pp. 288-381. They hold **1,229 entries** (3,200 + 1,229 = 4,429) + **13** `tr-` notes (49 + 13 = 62).

Entries per chunk: c11-v14-26 102 · c11-v27-32 47 · c11-v33-41 58 · c11-v42-54 57 · c12-v1-7 40 · c12-v8-12 33 · c12-v13-34 101 · c12-v35-48 93 · c12-v49-59 81 · c13-v1-9 78 · c13-v10-17 60 · c13-v18-21 53 · c13-v22-30 57 · c13-v31-35 53 · c14-v1-6 50 · c14-v7-11 57 · c14-v12-15 52 · c14-v16-24 63 · c14-v25-35 94.

p. 381 nn. 12-13 belong to the next interval (Cap. XV ¶ 1), which is unbuilt (checker: `p.381: 1-11 (11 notes) ok PENDING n.12,13`; `KNOWN_TOTALS_VOL7[381] = 13`). The p. 288 PENDING of the last gate (nn. 4-11) is now closed by `c11-v14-26`.

## PASS 1: live flags. AS EXPECTED (one `[?]`, recorded)
`check-live-flags.py vol7` scanned 82 chunks. **LIVE [?] FLAGS: 2 occurrences, which is one flag counted in La and En:** `bon-luc-c5-v12-16` l. 279 (`[^p122-11]` **La.** … *A C G E [?]*) and l. 281 (**En.**). This is exactly the resume's one live `[?]` (rulings 59, 73: stays open). Tool exit 0, as at p. 288.

No `[?]` stands in any body or apparatus of the 19 new chunks (the resume's "zero new `[?]` in 19 chunks", item 22, confirmed).

## PASS 2: mechanical suite. CLEAN: every resume START-HERE verification figure reproduced, no corpus divergence
| tool | result | resume "Verification at `bon-luc-c14-v25-35`" |
|---|---|---|
| `check-vol5-apparatus.py --volume=vol7` | **82 chunks, 4,429 entries**, every page 1..N through p. 380; p. 381 `1-11 (11 notes) ok PENDING n.12,13`; **All checks passed** (exit 0) | 82 / 4,429 ✓ |
| `check-vol5-census.py --volume=vol7` | vol7 **82 on disk / 82 in ledger**; **221 runovers (192 gutter / 29 page)**; **79 positive, 3 negative**; "Rosters agree". The three negatives are `c10-v38-42` (old) and the interval's **`c12-v49-59`** and **`c13-v10-17`** (ledger rows `-`). Interval page-crossings: p. 348 n. 11 · 362 n. 15 · 365 n. 15 · 370 n. 13 (4 of the 29; the interval added 43 runovers, 39 gutter / 4 page) | 82/82, 221 (192/29), 79/3 ✓ |
| `polish-style-scan.py --volume 7` | **CLEAN (vol7, 82 files)**. Unscoped run: 11 issues / 6 chunks / **2,400 scanned** (`bon-hex-c23`, four Vol III/IV Sentences chunks, as at p. 288), zero in vol7 | ✓ |
| `build-citations.py --out/--qa` to the scratchpad | 2,400 chunks; **44,808 ledger records**; **QA 213**; anaphora 2,346 within-chunk + 86 cross-chunk, **unresolved 391**; coordinate ibid. 485 (382 honoured / 103 unresolvable); printed slips (r.57 C2) 23 annotated, 0 stale. **Both outputs byte-identical (`cmp`) to the tracked `index/citations.tsv` and `manual-review/citation-qa-report.md`** | 44,808 / QA 213 / 391 ✓ |
| `site/scripts/build-content.mjs` → `build-index-json.py` → `build-content.mjs` (resume order) | **19 books, 2,399 questions, 2,399 translated** (both runs); **crossref index 1,879 chunks cited, 11,331 backlinks**; scripture 74 books / 30,311; goto 2,399 chunks / 5,366 printed pages; authorities 89 / 436 / 18,490 | 2,399/2,399; 1,879 / 11,331 ✓ |
| `validate-chunk.py` (each of the 82) | 82 × "1 checked, 0 failed" | OK ✓ |

The interval's growth over the p. 288 figures: entries +1,229; runovers +43 (221 − 178); citations +2,091 (44,808 − 42,717); anaphora unresolved +12 (379 → 391; the resume's T-a list accounts for it); QA flat at 213; crossref +17 chunks cited / +93 backlinks.

**Generated files.**
- `git status --short` before and after the whole suite: `?? .claude/settings.local.json` only. The p. 288 draft's pre-existing ` M index/authorities.tsv` / ` M site/vercel.json` are gone (committed or restored since); the tree was clean when this agent started.
- `build-citations.py` was pointed at the scratchpad, so no tracked file was rewritten even transiently. `build-index-json.py` and `build-content.mjs` write only to gitignored `site/src/data/*`; nothing tracked changed, so **no `git checkout` restore was needed or made.**
- No step was skipped.

## PASS 3: read-through / consistency. No NEW defect in the D-class; all seven KNOWN defects (D-1..D-7) confirmed; four NEW undisclosed register findings for the evidence sheet (3b)

Old ground (pp. 3-288, 63 chunks) is byte-unchanged since the p. 288 gate commit `4cf774e` (`git diff --stat 4cf774e HEAD -- vol7/` lists only the 19 interval files, all pure additions). The p. 288 gate's applied rulings were spot-confirmed in place: r. 63 (`c8-v49-56` has no `(V. N.)` body tag left; `c9-v1-9` "designated"), r. 64 (`c9-v10-17` "perfection of dilection", `c10-v1-3` "commandments of dilection" ×2), r. 66 (`c9-v32-36` ¶ 69 "preach after consummation"), r. 71 (`c10-v4-16` "for faithlessness"). The surviving hits of the old wordings are inside those chunks' Notes records only.

### 3a. Per-chunk La/En parity (all 82, computed from the files, then checked against each interval chunk's own Notes claim)
- **Anchors:** in all 82 chunks the `[^pN-n]` sequence is identical La/En, unique, in page/note order, and the anchor set equals the def set (4,429 = 4,429). Interval: 1,229 = 1,229. Every def's page lies in the chunk's `printed_pages`.
- **Page markers:** identical La/En in all 82, and equal to `printed_pages` in 81. The exception is old-ground `c3-v21-22` (markers 81-84, `printed_pages` 81-85; the p. 84 n. 14 page runover), as at the p. 88, 188 and 288 gates. **Non-defect.**
- **¶ numbers:** La = En in all 82, and each chunk's ¶s run exactly over its frontmatter `paragraphs` range with no gap.
- **`####` headings:** La = En in every interval chunk (5 · 1 · 1 · 0 · 4 · 2 · 2 · 2 · 1 · 0 · 2 · 0 · 0 · 0 · 2 · 1 · 0 · 0 · 1).
- **Guillemets, paragraph by paragraph:** the « and » counts agree La/En in every ¶ of every chunk. Interval ¶s unbalanced in both languages alike, each disclosed and on the resume (item 23): `c12-v1-7` ¶ 8 7 « / 8 » (II Cor. 5:4 without its opening «; chunk 53 / 54) [35]; `c13-v18-21` ¶ 45 11 / 10 (the Gloss, two opened / one closed; chunk 69 / 68) [106]; `c14-v16-24` ¶ 39 5 / 6 and ¶ 47 9 / 8 (Isa. 64:4 / John 9:39, cancelling; chunk 93 / 93) [165]. **Non-defects (recorded).** Old-ground imbalances (`c6-v1-11`, `c6-v12-19`, `c6-v32-38`, `c7-v17-23`, `c8-v49-56`) unchanged since the earlier gates.
- **Verse tags:** the La and En `(Vers. N.)` sequences agree in every ¶ of all 82; **no English `(V. N.)` body tag remains anywhere in vol7** (r. 63 discharged). Interval La counts: 12 · 6 · 9 · 13 · 7 · 5 · 22 · 14 · 10 · 8 · 8 · 4 · 9 · 5 · 6 · 5 · 4 · 9 · 11 (= 167). Every tag's number falls inside the chunk's `verses`. Multi-verse tags as printed, both languages: `c11-v14-26` *(Vers. 17. 18.)*, `c12-v49-59` *(Vers. 52. 53.)*, `c13-v1-9` *(Vers. 2. 3.)* and *(Vers. 4. 5.)*, `c13-v22-30` *(Vers. 23. 24.)*, `c14-v7-11` *(Vers. 7. 8.)*, `c14-v25-35` *(Vers. 25. 26.)* and *(Vers. 29. 30.)*.
- **Notes self-claims:** in every interval chunk the stated apparatus-entry headline (word form, e.g. "ONE HUNDRED AND TWO APPARATUS ENTRIES"), "anchors N = N", "guillemets N « / M »", "`(Vers.` N = N", "page markers N = N" and "`####` N = N" all equal the file. **No false self-claim in the interval** (the p. 288 gate's one false claim, `c8-v49-56`'s, was amended by r. 63).

### 3b. Register-term census, pp. 288-381 (19 chunks, ¶-aligned La vs En, rendered bodies only, anchors stripped; apparatus checked separately where named)
| Latin | English | La / En | ¶s where La > En, resolved |
|---|---|---|---|
| *benignitas* / *benignus* (r. 45) | kindness / kind | 14 / 39 | 2 by the ¶ count, **3 "benignity" by a direct grep — NEW finding N-1 below** (`c13-v1-9` ¶ 12, `c14-v16-24` ¶ 37, `c14-v25-35` ¶ 52). The En surplus is "kind of" |
| *clementia* | clemency | 3 / 3 | 0 |
| *praeconium* (r. 30 / 66) | proclamation | 1 / 1 | 0. **Zero "proclaim" anywhere in the interval's English bodies**; the one "proclamation" sits on the *praeconium* |
| *praedicare* family (r. 30 / 66) | preach- | 46 / 42 | 5, all false hits: *praedictus* / *praedicatum* (`c11-v14-26` ¶ 44 ×2, `c12-v13-34` ¶ 23, `c12-v35-48` ¶ 61, `c14-v25-35` ¶¶ 65, 69) |
| *evangelizare* | "preach the gospel" etc. | 2 / 9 | 0 |
| *magisterium* | teaching office | 1 / 1 | 0 |
| *paupertas* | poverty | 12 / 12 | 0 |
| *misericordia* | mercy | 41 / 56 | 0 |
| *miseratio* | commiseration | 1 / 0 | 1: Zach. 7:9 *miserationes* "compassion", Douay in quotation (`c11-v42-54` ¶ 86); r. 12's Douay clause, non-defect |
| *credulitas* / *incredulitas* (r. 55) | belief / unbelief | 2 / 2 · 7 / 7 | 0 numerically, **but one of the two is D-1** ("credulity", below) |
| *infidelitas* (r. 71) | faithlessness | 3 / 3 | 0. r. 71 holds |
| *redarguere* (r. 56) | convict | 10 / 11 | **1: `c11-v42-54` ¶ 87 — NEW finding N-3 below.** The En surplus is `c13-v1-9` ¶ 17's two *arguitur* "convicted" (observation O-1) |
| *suasio* / *persuasio* (r. 44) | persuasion | 2 / 10 | 0 |
| *curare* / *curatio* (r. 53) | cure | (noisy regex) | Every *curare*-family site checked by hand: all shortfalls are *curare de* "care for" / *cura* "care" (`c11-v33-41` ¶¶ 80-81, `c12-v13-34` ¶¶ 33, 34, 38, `c12-v49-59` ¶ 79, `c13-v10-17` ¶ 30, `c14-v1-6` ¶ 11 *cutem curandam*), except `c14-v1-6` ¶ 3 Mark 3:2 *curaret* "heal" — the resume's ruling-28 split beside Luke 14:3 "cure" (item 10 [137]). Non-defect |
| *sanare* / *sanatio* (r. 53) | heal / healing | 14 / 22 | 2 false hits: *sanam doctrinam* "sound doctrine" (`c11-v42-54` ¶ 90, `c12-v35-48` ¶ 62) |
| *caritas* (r. 52) | charity | 53 / 53 | 0 |
| *dilectio* (r. 52 / 64) | dilection | 18 / 16 | 2, both Douay inside quotations: Ecclus. 7:39 "confirmed in love" (`c14-v12-15` ¶ 30); Jer. 2:33 "to seek love" (`c14-v16-24` ¶ 42). r. 64 ("outside a Douay verse") holds. **No body-prose *dilectio* → "love" in the interval** |
| *otium* / *otiosus* (r. 57) | leisure | 2 / 1 | 2: *verbum otiosum* "idle word" (`c12-v49-59` ¶ 87, Matt. 12:36 in a Father) and Gregory's *amor Dei otiosus* "never idle" (`c13-v18-21` ¶ 47). Adjective *otiosus* = "idle", no *otium* noun; recorded |
| *pietas* (r. 70 review) | piety | 17 / 17 | 0. Divine `tr-pietas` sites `c12-v35-48` ¶ 57, `c13-v10-17` ¶ 25, `c13-v31-35` ¶ 74, exactly item 11's three |
| *pius* / *pie* | pious / piously | 6 / 6 | 0 |
| *impietas* / *impius* | impiety / impious | 24 / 17 | 5 ¶s, all Douay "the wicked" / "wickedness" in quotations (Job 21:7, Eccles. 8:10-14 / 9:2, Ps. 9:6, Isa. 26:10, Prov. 24:15). For the *pietas* review's *impius* record (item 11), not defects |
| *poenitentia* | penance | 44 / 49 | 1: `c13-v22-30` ¶ 56 Wis. 5:3 / Heb. 12:17 "repentance", disclosed (item 17 [121]) |
| *poenitudo* | repentance | 1 / 2 | 0 |
| *auctoritas* (r. 47) | authority | 7 / 7 | 0 |
| *excessus* / *excessivus* (r. 67) | transport / excess | 2 / 5 | 0 numerically; **but see N-4 below** (*excessivus* split across chunks; bears on D-5) |
| *vacare* (r. 32 / 68) | free / free for | 5 / 11 | 3: Prov. 23:21 *vacantes potibus* Douay "give themselves to drinking" ×2 (`c12-v13-34` ¶ 29, `c14-v12-15` ¶ 28; nothing leans); **`c13-v1-9` ¶ 12 Augustine's *quare vacatis?* "why are you idle?" — observation O-2 below** |
| *lumen* (r. 32 table / 27 / 50) | lumen | 16 / 6 | 8 ¶s: Ps. 118:105 (`c11-v33-41` ¶ 72) [18], *luminosa* / *luminaria* (¶¶ 74, 76, not *lumen*), Rom. 2:19 (`c11-v42-54` ¶ 90; r. 50 names it), Ps. 4:7 (**D-2**), Job 24:13 (`c13-v10-17` ¶ 33) [99] — all known; **`c12-v1-7` ¶¶ 2, 6 — NEW finding N-2 below** |
| *lux* | light | 25 / 54 | 0 |
| *lucerna* | lamp | 46 / 55 | 0 in the bodies; "candle" occurs once, **D-4** |
| *eruditio* (r. 17) | erudition | 1 / 0 | 1: **D-7** |
| *Praeceptor* (r. 69) | Master / preceptor | 1 / 28 | 1: Isa. 30:20 *verbum praeceptoris tui* "thy teacher" (`c12-v49-59` ¶ 85), r. 69's OT clause (Douay, nothing leans). No Lucan *Praeceptor* in the interval (the next is Luke 17:13) |
| *claritas* | brightness | 1 / 4 | 0 |
| *intelligentia* (r. 17 / 70) | intelligence | 12 / 8 | 4: Job 32:8 Douay "understanding" (`c12-v8-12` ¶ 20); Phil. 4:7 Douay "minds" (`c12-v49-59` ¶ 74); `c12-v49-59` ¶ 81 *ad intelligentiam illorum* and `c14-v7-11` ¶ 20 Bernard's *ut ad intelligentiam loquar* "understanding" — both the ordinary idiom, both disclosed in their Notes (the `bon-qsc-q2` precedent). Non-defects |
| *intellectus* (noun) | understanding | 12 / 18 | 0 |
| *notitia* | knowledge | 19 / 46 | 0 |

Further ruling-32-table rows checked over the 19 chunks (La / En, ¶ shortfalls resolved): *liberalitas* "liberality" 5 / 5 · *admirabilis* "wonderful" 3 / 5 · *mirabilis* "marvellous" 3 / 6 · *comminatio* "threatening" 13 / 29 · *increpatio* "rebuke" 6 / 12 · *admonitio* "admonition" 3 / 3 · *beatitudo* "beatitude" 4 / 4 · *purgatio* "purgation" 2 / 2 · *corripere* 4 / 3 (Amos 5:10 "him that rebuketh" ×2, `c11-v42-54` ¶ 101 and `c13-v31-35` ¶ 73, r. 46's nothing-leans clause; Wis. 1:8 Douay "chastising judgment", `c12-v1-7` ¶ 6) · *eruditor* 1 / 0 (Rom. 2:20 Douay "an instructor of the foolish", `c11-v42-54` ¶ 90; quotation) · *cultus* 1 / 0 (Ambrose *agricolarum cultum* "tillage", `c12-v13-34` ¶ 39; not the worship sense) · *exsultare* 6 / 4 (observation O-3). No *timoratus*, *largitas* in the interval.

**NEW FINDINGS (not on the resume's D-list or its items; each undisclosed in its chunk's Notes unless said otherwise). Register calls for Wilson; reported here with exact file:line, not decided.**

- **N-1. *benignitas* "benignity" ×3, against ruling 45 (ruling 32's table: *benignitas* "kindness", *benignus* "kind", "into quotations too").**
  - `vol7/bon-luc-c13-v1-9.md` l. 176 (¶ 12 En; La l. 87): Rom. 2:4 *benignitas Dei* "the benignity of God". **The same verse is "the kindness of God" at `c10-v4-16` l. 162 and `c4-v38-44` l. 96**, each disclosed there under r. 45. So this is also a cross-chunk split on one verse.
  - `vol7/bon-luc-c14-v16-24.md` l. 93 (¶ 37 En; La l. 34): *summam liberalitatem et benignitatem* "the highest liberality and benignity" (Bonaventure's prose).
  - `vol7/bon-luc-c14-v25-35.md` l. 102 (¶ 52 En; La l. 35): *conversus … per benignitatem* "turning … through *benignity*" (Bonaventure's prose). Its Notes (l. 567) cite the Latin but not the rendering.
  - The fix would be mechanical: one word at each of three lines.
- **N-2. Body-prose *lumen* rendered "light", with no `tr-lumen`, against ruling 32's table row (*lumen* in Bonaventure's prose → "lumen" + `tr-lumen`).** These are not on item 12's list.
  - `vol7/bon-luc-c12-v1-7.md` ¶ 2: La l. 45 *et tenebra per lumen expellitur* → En l. 94 "darkness is driven out by light".
  - `vol7/bon-luc-c12-v1-7.md` ¶ 6: La l. 55 *Lumen enim solis visui cetera manifestat* → En l. 104 "For the light of the sun makes other things manifest to sight". This sentence expounds the lemma Luke 12:3 *in lumine dicentur* ("spoken in the light", item 7 [32]). Under the Vol V test (rulings 27 / 50), the body prose **leans** on the lemma's *lumen*, so the lemma's rendering falls under the same question.
  - The chunk carries no `tr-lumen`. Its Notes discuss only the Luke 12:3 Douay adjustment ("published" → "in the light").
- **N-3. *redarguere* rendered "rebukes", against ruling 56 (*redarguere* "convict").** The Gloss / Ambrose *Arrogantiam redarguit, quia primatus appetunt*:
  - in the body: `vol7/bon-luc-c11-v42-54.md` ¶ 87, La l. 36 → En l. 99 "He rebukes arrogance";
  - again in the apparatus: p. 305 n. 6, La l. 180 → En l. 182 "He rebukes arrogance".
  - Every other interval *redarguere* site is "convict". The chunk's Notes are silent.
- **N-4. *excessivus* is split across chunks, which bears on D-5.**
  - `c13-v18-21` ¶ 46 *dilectione excessiva* is "transporting dilection" (D-5; l. 136).
  - `vol7/bon-luc-c12-v49-59.md` ¶ 72 *Elevat per adhaerentiam excessivam* (La l. 42) is "**an excessive adherence**" (En l. 108). It is listed among that chunk's new house words (item 18 batch), not under the *excessus* question.
  - Old ground, already past the p. 288 gate: `c9-v32-36` ¶ 61 *per excessivum desiderium, quod consuevit esse in contemplantibus* is "an excessive desire" (l. 95), and p. 236 n. 7 *De desiderio excessivo in contemplativis* is "the excessive desire" (l. 200). Both are contemplative contexts.
  - So "excessive" stands at three sites and "transporting" at one. Whatever D-5 rules for the adjective reaches all four.

**OBSERVATIONS (disclosed or doubtful; recorded, not counted as defects):**
- **O-1.** `vol7/bon-luc-c13-v1-9.md` ¶ 17 (La l. 101, En l. 190): *negligentia humana arguitur … potissime arguitur* → "is rightly convicted … most of all convicted". Ruling 32's table gives *arguere* "reprove" and keeps "convict" for *redarguere*. The chunk's Notes do disclose it, but they file it under ruling 56 ("¶ 17 *arguitur* 'convicted'"), as though *arguere* were *redarguere*.
- **O-2.** `vol7/bon-luc-c13-v1-9.md` ¶ 12 (La l. 87, En l. 176): Augustine's *quare vacatis?* → "why are you idle?". Ruling 32's *vacare* row reads: absolute *vacare* "to be free" (r. 68), never "rest". "Idle" is the *otiosus* word (3b). Undisclosed. One word.
- **O-3.** *exsultare*: ruling 32's table has "exult" ("Douay 'rejoice' adjusted"). Ps. 18:6 *Exsultavit ut gigas* is "He hath rejoiced as a giant" at two sites in `vol7/bon-luc-c14-v25-35.md`, both undisclosed:
  - ¶ 66, inside Ambrose (En l. 149);
  - p. 379 n. 9 **En.**, inside Augustine (l. 424).
  - Separately, Tob. 3:22 *exsultationem* is the Douay "joyfulness" (`c12-v49-59` ¶ 83), inside the disclosed Douay-base batch (item 9 [70]).
- **O-4.** Prov. 23:21 *dantes symbola* is rendered two ways, neither disclosed:
  - "that club together" (Douay) at `vol7/bon-luc-c12-v13-34.md` ¶ 29 (En l. 157);
  - "that give clubs" at `vol7/bon-luc-c14-v12-15.md` ¶ 28 (En l. 76).
  - This is a ruling-28 split, or a conformation to the Douay.
- **O-5.** `c12-v49-59` ¶ 81 *ad intelligentiam illorum* and `c14-v7-11` ¶ 20 Bernard's *ut ad intelligentiam loquar* are rendered "understanding". Both are disclosed as idiom: no *intellectus* stands in `c12-v49-59`; `c14-v7-11`'s Notes name it. Ruling 17 / F10 class; for item 15.

**The seven KNOWN defects, all confirmed in place, none edited:**
- D-1: `c13-v1-9` l. 146 "lack of *credulity*".
- D-2: `c12-v49-59` l. 143, ¶ 84 Ps. 4:7 "light".
- D-3: `c12-v8-12` l. 221, p. 316 n. 2 **En.** "the truth and the light of the rational soul" (*lumenque*). Of the two sister sites, p. 339 n. 5 (`c13-v1-9`, Isa. 9:2) and p. 373 n. 12 (`c14-v16-24`, Gregory's *ingenii lumen*) are also "light". The interval's only apparatus *lumen* rendered "lumen" are `c11-v33-41` p. 301 n. 9 and `c12-v35-48` p. 324 n. 7.
- D-4: `c11-v14-26` l. 132, "No man lighteth a *candle*".
- D-5: `c13-v18-21` l. 136 "transporting dilection" (see N-4).
- D-6: `index/citations.tsv` l. 37380, `bon-luc-c11-v14-26` `apparatus:p295-15` *supra pag. 297, nota 7* resolved to `bon-luc-c11-v27-32` / `fn-p297-7`, with no r.57 C2 annotation.
- D-7: `c14-v12-15` l. 70 "spiritual teaching".

**Ruling 69 (Praeceptor), mechanically:** no Lucan *Praeceptor* in pp. 288-381, so no `tr-praeceptor` is owed in the interval. **Ruling 64:** no body-prose *dilectio* → "love". **Ruling 66:** zero *praedicare* → "proclaim". **Ruling 71:** *infidelitas* "faithlessness" 3 / 3. **Ruling 63:** zero `(V. N.)` body tags in vol7.

### 3c. `tr-` note inventory, pp. 288-381: 13 notes, every def anchored exactly once, every anchor defined
- `c11-v14-26` vacare (¶ 54, Matt. 12:44 *vacantem* "free" [5]); corrigenda (**inside p. 294 n. 13**, item 6)
- `c11-v33-41` lumen (¶ 71); corrigenda (**inside p. 300 n. 8**'s gutter tail, item 6)
- `c12-v13-34` corrigenda (¶ 35, the p. 320 entry)
- `c12-v35-48` lumen (¶ 50), pietas (¶ 57)
- `c12-v49-59` corrigenda (¶ 79, the p. 333 entry, first of two sites)
- `c13-v10-17` pietas (¶ 25), corrigenda (¶ 27, p. 343 *similiter* → *simul*)
- `c13-v18-21` corrigenda (¶ 36, p. 346 *Manducit* → *Manuducit*)
- `c13-v31-35` pietas (¶ 74)
- `c14-v1-6` corrigenda (**inside p. 361 n. 13**, *nota 3* → *nota 13*, ruling 23's shape)

There is no `tr-` anchor in any Latin body. **Three of the interval's notes are anchored inside an apparatus entry, not in the body.** Those are the three Corrigenda that correct the notes themselves (pp. 294, 300, 361), which is the old-ground shape of `c1-v5-17` / `c5-v1-11`. Each of the three is anchored once, in the **En.** half of its host note. Vol VII total: 49 + 13 = **62**. The interval holds seven Corrigenda notes, matching item 6's seven sites. It holds three divine `tr-pietas`, matching item 11, and two `tr-lumen`, matching item 12. It holds one `tr-vacare` and no `tr-excessus` or `tr-praeceptor`.

### 3d. Frontmatter / `printed_pages` continuity, pp. 288-381: no gap, no overlap
- `pdf_pages` = printed + 26 and contiguous in all 82.
- Each consecutive pair either shares exactly its seam page (18 shared pages: 288, 295, 300, 304, 309, 313, 316, 324, 330, 336, 341, 346, 350, 354, 358, 366, 370, 375) or abuts. The one abutment is **`c14-v1-6` (ends 361) → `c14-v7-11` (opens 362)**. Both Notes agree on it:
  - `c14-v1-6`: ¶ 13 closes at the foot of 361R on Zach. 9:11 (anchor n. 16), and p. 362 opens with the t4.
  - `c14-v7-11`: its opening "under the 362L t4".
- p. 381 is the interval's last page, and it is shared with the unbuilt Cap. XV ¶ 1.
- `division` steps 11 → 12 → 13 → 14 once each. `section` runs XI 3-6 · XII 1-5 · XIII 1-5 · XIV 1-5. `paragraphs` restart at 1 at each capitulum and are contiguous within it. `verses` are contiguous with no overlap, and each capitulum closes on Luke's last verse (XI 54 · XII 59 · XIII 35 · XIV 35).
- **Last ¶ per capitulum: XI 102 · XII 88 · XIII 76 · XIV 69.** **Known fact confirmed:** `c14-v25-35` `paragraphs: "51-69"`, with ¶ 69 in both languages. Cap. XIV ends at ¶ 69. The setup table at `manual-review/vol7-pilot-setup.md` l. 58 still reads `XIV | 358–381 | 68`; the correction stands at l. 721 ("Cap. XIV's last ¶ is 69, not 68"). The table cell itself is unamended. That is a records point, not a chunk defect.

### 3e. Hand-offs at every shared page, pp. 288-381 (file ownership derived from the defs; each split checked against BOTH chunks' Notes)
| page | A nn. / B nn. | page | A nn. / B nn. |
|---|---|---|---|
| 288 | c11-v5-13 1-3 / c11-v14-26 4-11 | 336 | c12-v49-59 1 / c13-v1-9 2-9 |
| 295 | c11-v14-26 1-15 / c11-v27-32 16 | 341 | c13-v1-9 1-12 / c13-v10-17 13-14 |
| 300 | c11-v27-32 1 / c11-v33-41 2-13 | 346 | c13-v10-17 none / c13-v18-21 1-11 |
| 304 | c11-v33-41 1-12 / c11-v42-54 13-14 | 350 | c13-v18-21 none / c13-v22-30 1-14 |
| 309 | c11-v42-54 1-10 / c12-v1-7 11 | 354 | c13-v22-30 1-6 / c13-v31-35 7-15 |
| 313 | c12-v1-7 1-6 / c12-v8-12 7-12 | 358 | c13-v31-35 1-5 / c14-v1-6 6-14 |
| 316 | c12-v8-12 1-4 / c12-v13-34 5-16 | 366 | c14-v7-11 1-2 / c14-v12-15 3-13 |
| 324 | c12-v13-34 none / c12-v35-48 1-12 | 370 | c14-v12-15 none / c14-v16-24 1-13 |
| 330 | c12-v35-48 1-8 / c12-v49-59 9-13 | 375 | c14-v16-24 1-2 / c14-v25-35 3-14 |
| | | 381 | c14-v25-35 1-11 / next interval 12-13 PENDING |

On every page the two halves make one contiguous 1..N register, and the apparatus checker confirms N against `KNOWN_TOTALS_VOL7`.

**Where the outgoing chunk holds notes on the page (14 pages),** its Notes state the "nn. a-b" range literally, and so do the incoming chunk's Notes.

**Where the outgoing chunk holds none (pp. 324, 346, 350, 370),** its Notes say so in terms:
- `c12-v13-34`: "p. 324's apparatus is wholly the next chunk's".
- `c13-v10-17`: "p. 346 carries no note of ours".
- `c13-v18-21`: "p. 350 carries no note of ours".
- `c14-v12-15`: "p. 370 carries no note of ours".

On each of those four pages the outgoing chunk's text on the leaf is a few unanchored closing lines. **The p. 288 PENDING of the last gate (nn. 4-11) is closed as handed off.**

p. 381 nn. 12-13 are named in the resume START HERE block: n. 12 at *pietatis* (381L), n. 13 at *ibi* (381R). They are the next interval's.

## Summary
- **Pass 1:** as expected. One live `[?]`, `c5-v12-16` p. 122 n. 11, La + En (rulings 59 / 73). Exit 0. There is no `[?]` in the 19 interval chunks.
- **Pass 2:** clean. Every resume figure was reproduced exactly:
  - apparatus: 82 chunks / 4,429 entries; p. 381 nn. 12-13 PENDING;
  - census: 82/82, 221 runovers (192 / 29), 79 positive and 3 negative (`c10-v38-42`, `c12-v49-59`, `c13-v10-17`);
  - style scan: CLEAN (82 files);
  - citations: 44,808 records, QA 213, both byte-identical to the tracked files;
  - anaphora: 391 unresolved;
  - crossref: 1,879 chunks cited / 11,331 backlinks;
  - build: 2,399 / 2,399;
  - `validate-chunk.py`: OK × 82.

  No tracked file changed, so no restore was needed.
- **Pass 3:** La/En parity holds in every ¶ of all 82 chunks: anchors, page markers, ¶ numbers, `####`, guillemets and verse tags. No interval Notes self-claim is false. The 13 interval `tr-` notes are all paired. There is no page gap or overlap (18 shared pages, 1 abutment). The hand-offs agree on all 18 shared pages, and on p. 381's PENDING. Cap. XIV ends at ¶ 69; the setup table's l. 58 cell still says 68.
- **Known defects D-1 to D-7:** all confirmed at the lines given in 3b. None was touched.
- **NEW findings (register, undisclosed; for the evidence sheet):**
  - **N-1:** *benignitas* "benignity" ×3 against r. 45:
    - `c13-v1-9` l. 176, Rom. 2:4, which is also a cross-chunk split with `c10-v4-16` / `c4-v38-44` "kindness";
    - `c14-v16-24` l. 93;
    - `c14-v25-35` l. 102.
  - **N-2:** body-prose *lumen* "light" with no `tr-lumen`: `c12-v1-7` ¶¶ 2, 6 (En ll. 94, 104). ¶ 6 leans on the Luke 12:3 lemma.
  - **N-3:** *redarguit* "rebukes": `c11-v42-54` ¶ 87, En l. 99, and p. 305 n. 6, En l. 182. This is against r. 56.
  - **N-4:** *excessivus* "excessive" at `c12-v49-59` l. 108 and old-ground `c9-v32-36` ll. 95, 200, against "transporting" at D-5. D-5's ruling should reach all four sites.
- **Observations:**
  - O-1: `c13-v1-9` ¶ 17 *arguitur* "convicted", disclosed but filed under r. 56.
  - O-2: `c13-v1-9` ¶ 12 *vacatis* "idle".
  - O-3: Ps. 18:6 *exsultavit* "rejoiced" ×2 in `c14-v25-35`.
  - O-4: Prov. 23:21 rendered two ways.
  - O-5: two *intelligentia* idioms, disclosed.
