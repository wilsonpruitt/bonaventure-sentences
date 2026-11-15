# Vol VII — *Commentarius in Evangelium S. Lucae*, p. 288 GATE (printed pp. 188–288; Cap. VIII–XI v. 13 complete) — CLOSED

**STATUS: CLOSED 2026-11-15.** Docket ruled by Wilson in one sitting ("Approve all", 2026-11-15: every ⭐ recommendation of the evidence sheet — D-1..D-4 as specified, the "Found by the sheet" fix F1 and the records F2–F12, the register items as recommended, all batches ratified — and the defect found by Passes 1–3) → Vol VII rulings 63–76 in `manual-review/vol7-pilot-setup.md` § *LUCAM* p. 288 GATE. **14 English lines changed across 6 chunks (D-1, D-2, F1, the passes defect, *infidelitas*), plus Notes records in 9 chunks; no line in any `## Latin` body or `**La.**` half changed; no manifest cell changed.** Ruling 32's table gains one row (*excessus*) and two clauses on its *vacare* row; the repo CLAUDE.md's Itinerarium *excessus* line gains a one-clause scope note. One tool job queued (ruling 76, J-1..J-11; supersedes ruling 62's numbering). The live `[?]` (p. 122 n. 11) stays open. **No push, no deploy.**

Ruling 14 placed this gate at p. 288 (c. 11 v. 13). This close makes no recommendation about the deploy.

**Procedure (the p. 188 gate's):** a read-only agent compiled the evidence sheet, `manual-review/vol7-lucam-p288-gate-evidence-sheet.md` (censuses over the rendered region, the decisive sentence, alternatives with costs, a ⭐ per item, and twelve "found by the sheet" items F1–F12); a second read-only agent ran Passes 1–3 into `manual-review/vol7-lucam-p288-gate-passes-draft.md` (both committed at `c96b40d`); manifest stage 4 (`c478c25`) was drawn alongside. Both documents are kept as the evidence record and are summarised here, not repeated. Wilson ruled in one sitting; the edits, the re-run and Pass 4 then closed the gate.

**Scope: the 22 chunks of pp. 188–288** (`bon-luc-c8-v1-10` → `bon-luc-c11-v5-13`; VIII 7 · IX 8 · X 5 · XI 2), **1,185 numbered apparatus entries, 15 `tr-` notes**; censuses over all 63 *Lucam* chunks (pp. 3–288, 3,200 entries, 49 `tr-` notes), and over Vols V–VI where a corpus precedent decided (*excessus*). **p. 288 nn. 4–11 belong to the next interval** (`bon-luc-c11-v14-26`, unbuilt; checker `PENDING n.4,5,6,7,8,9,10,11`).

---

## PASS 1 — live flags: **AS EXPECTED**

`check-live-flags.py vol7` → 63 chunks, **2 occurrences = one flag, La + En: `bon-luc-c5-v12-16` p. 122 n. 11** (*A C G E [?]*). Same after the edits. Stays open (ruling 73). Exit 0 (the p. 188 draft records 1; tool behaviour only).

## PASS 2 — mechanical suite: **CLEAN** (figures below, § CLOSE)

## PASS 3 — read-through / consistency: **ONE NEW DEFECT (fixed), D-1 CONFIRMED (fixed)**

La/En parity in every ¶ of all 63 chunks (anchors 3,200 = 3,200; page markers; ¶ numbers; guillemets ¶ by ¶; verse tags); 15 interval `tr-` notes all paired; no page gap or overlap pp. 188–288; hand-offs agree on all 21 shared pages. **New defect:** `c9-v32-36` ¶ 69 Ambrose *praedica post consummationem* "proclaim" against ruling 30 → fixed (ruling 66). **D-1** confirmed and fixed (ruling 63). Observations: the *infidelitas* split (`c10-v4-16` ¶ 19 "unbelief"), folded into item 24 [99] and conformed (ruling 71); `c9-v10-17` ¶ 19 *dilectio* "love" = the sheet's F1, conformed (ruling 64); old-ground `c3-v21-22` page markers 81–84 against `printed_pages` 81–85 (the p. 84 n. 14 runover), a non-defect as at the p. 88 and p. 188 gates.

## PASS 4 — plate cleanup: **NOTHING TO DELETE**

This close read no plate and made no crop. The `raw/vision/vol7/` plates (pp. 189–290) are left as they are; pp. 288–290 serve the next interval's first chunk. Whether to delete the pp. 189–287 plates now that their interval is closed is Wilson's call; not done here.

---

## THE DOCKET — RULED 2026-11-15, "Approve all"

| # | item(s) | ruling | lines applied | recorded |
|---|---|---|---|---|
| D-1 + F2 | `c8-v49-56` `(V. N.)` → `(Vers. N.)`; its stale Notes claim | Applied; Notes amended, struck wording kept | 8 | 63 |
| D-2 + F3 | `c9-v1-9` "appointed" → "designated" (two sites, not one) | Applied | 2 | 63 |
| F1 | *dilectio* "love" outside a verse | "dilection" work-wide outside a Douay verse | 2 | 64 |
| A, B, C | 1–14, 25: boundaries, manifest, structure; p. 252 Corrigenda; ruling-20 adjustments (Luke 11:2 "Sanctified" incl.) | Ratified; Matt. 6:9 / Luke 11:2 split recorded; preview look added to ruling 23's | 0 + Notes | 65 |
| passes | `c9-v32-36` ¶ 69 *praedica* "proclaim" | → "preach" (ruling 30) | 1 | 66 |
| 15 + D-3 + F4 | *excessus* | Kept as built; `tr-excessus` kept; ruling 32 row; CLAUDE.md scope note | 0 + Notes | 67 |
| 17 + F6 | absolute *vacare*; Ps. 45:11 | Ratified; ruling 32 *vacare* row extended; Ps. 45:11 split recorded | 0 + Notes | 68 |
| 16 + F7 | ruling 49's forward clause; Isa. 30:20 | Discharged at `c8-v40-48`; standing text of `tr-praeceptor`; "master and preceptor" ratified; Isa. 30:20 split recorded | 0 + Notes | 69 |
| 18–23 + D-4 + F8–F10 | *cognitio*, `tr-lumen`, *claritas*, human *pietas* (→ p. 381), *virtus*, cross-chunk splits | Ratified; D-4 no edit | 0 | 70 |
| 24 [99] | house words; *infidelitas* | Ratified with F1; `c10-v4-16` ¶ 19 "unbelief" → "faithlessness" | 1 | 71 |
| E | 26 citation slips | Ratified as transcribed (r.57 class) | 0 | 72 |
| F | 27–29 `[so printed]`; the live `[?]` | Ratified; **`[?]` stays open** | 0 | 73 |
| G, H | 30–32 readings as printed; 33–34 collection change | Ratified; banked | 0 | 74 |
| F4, F5, F9, F11, F12 | records and docket errors | Recorded (below) | 0 | 75 |
| T | J-1..J-11 (ruling 62's T-1..T-9 merged with the interval's sites) | One tool job, QUEUED, NOT RUN | 0 | 76 |

### Lines changed (git diff)

| file | English / En. lines | Notes lines | Latin / La. lines |
|---|---|---|---|
| `vol7/bon-luc-c8-v49-56.md` | 8 (¶¶ 88, 89, 90, 92, 93, 94, 95, 98: `(V. 49.).` … `(V. 56.).` → `(Vers. 49.).` … `(Vers. 56.).`) | 1 amended in place (the "`(Vers.` 8 = 8" claim, struck wording kept) + 1 gate paragraph | **0** |
| `vol7/bon-luc-c9-v1-9.md` | 2 (¶ 1 "*Now he appointed* etc." → "*Now he designated* etc."; p. 216 n. 9 **En.** "the Lord appointed" → "the Lord designated") | 1 gate paragraph | **0** |
| `vol7/bon-luc-c9-v10-17.md` | 1 (¶ 19 "the perfection of love" → "the perfection of dilection") | 1 gate paragraph | **0** |
| `vol7/bon-luc-c10-v1-3.md` | 1 (p. 253 n. 2 **En.** "the two commandments of love" ×2 → "… of dilection" ×2) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c9-v32-36.md` | 1 (¶ 69 "proclaim after consummation" → "preach after consummation") | 1 amended in place (builder's item (90), struck wording kept) + 1 gate paragraph | **0** |
| `vol7/bon-luc-c10-v4-16.md` | 1 (¶ 19 "no excuse for unbelief" → "no excuse for faithlessness") | 1 gate paragraph (F8 recorded) | **0** |
| `vol7/bon-luc-c11-v1-4.md` | 0 | 1 gate paragraph (item 7 split, F6) | **0** |
| `vol7/bon-luc-c9-v57-62.md` | 0 | 1 gate paragraph (F7) | **0** |
| `vol7/bon-luc-c9-v28-31.md` | 0 | 1 gate paragraph (item 15, F4) | **0** |

**14 English lines across 6 chunks.** The sheet estimated 12 across 4 (D-1 8, D-2 2, F1 2); Passes 1–3 added one (¶ 69 *praedica*), and the *infidelitas* observation, folded into item 24 [99] as approved, added one (`c10-v4-16` ¶ 19). Each site was read with its Latin before the edit; the edits were made by exact-match replacement, one asserted occurrence per line (`c10-v1-3` p. 253 n. 2: two asserted on one line), and each line asserted to stand in `## English` or an apparatus **En.** half.

**Also changed (doc):** `manual-review/vol7-pilot-setup.md` (ruling 32's table: the *excessus* row, the *vacare* clauses; rulings 63–76); `CLAUDE.md` (one scope clause beside the Itinerarium "NEVER 'excess'" line, ruling 67: that rule is the mental / contemplative *excessus*; the measure-exceeded sense takes "excess"). No other CLAUDE.md line touched.

### Docket errors and records the sheet found (no text effect)

- **F4:** the *excessus* split is not "across two chunks"; it is inside `c9-v28-31` (¶ 47 "transport" / ¶ 54 + Luke 9:31 "excess"), by sense. `c9-v32-36` ¶ 62 agrees with ¶ 47.
- **F5:** item 13's Luke 8:1 "evangelizing" was already ruled by ruling 18; `c10-v38-42` ¶ 66 *regnum Dei evangelizandum* follows it under ruling 29's echo clause.
- **F9:** the cross-chunk ruling-28 splits are wider than item 23 listed: Luke 22:26–27 "ministereth" also `c6-v39-49` ×2, `c9-v46-56` ×2, "serveth" also `c3-v21-22`, `c4-v38-44`, `c7-v24-35` ×2; John 6:2 "miracles" also `c6-v12-19`, "signs" also `c9-v1-9`; Dan. 12:3 "instruct" also `c8-v11-21`; Isa. 58:7 "Deal" also `c3-v10-14`. All ruling 20 working site by site; no edit (D-4).
- **F10:** *cognitio* "knowledge" at 5 of 16 interval sites (`c8-v22-25` ¶ 41 ×2, `c11-v5-13` ¶ 24, `c8-v26-33` p. 205 n. 2, `c8-v40-48` p. 212 n. 3); no *notitia* / *scientia* beside them; no conformation.
- **F11:** p. 201 n. 6 *tom. III. pag. 555, nota 7* (`c8-v22-25`) is the `page-multi`-with-*nota* class and was not on the docket's list; added to J-5.
- **F12:** (a) Luke 9:1 "power and authority" is the Douay's own pair (DRC), not an adjustment; ruling 47's tie-break is the Douay. (b) The docket's tool numbers collided with ruling 62's (docket T-6 = ruling 62's T-2 family; docket T-7 = ruling 62's T-6 family); resolved by the J-numbering (ruling 76).
- **Passes draft, corrected here:** it called the ¶ 69 *praedica* "undisclosed"; the builder's item (90) in `c9-v32-36`'s Notes names the rendering beside *praedicatores* "preachers", without naming it a departure. Amended in place.
- **Outside the gate's reach (recorded, not edited):** Vol V carries three "excess" sites against its own Itinerarium rule — `bon-brev-p5-c6` *in caliginem et excessum* + p. 260 n. 3 **En.**; `bon-praec-c4` p. 521 n. 4 **En.** "mental excesses" (where `bon-itin-prol` ¶ 3 reads "mental transports"). For a later Vol V errata list.

### Manifest stage 4

**Drawn at `c478c25`** (Cap. XI v. 14 – Cap. XIV, pp. 288–381, **19 rows**; XI 4 · XII 5 · XIII 5 · XIV 5). **Its 7 `low` rows (three decisions: the `c11-v14-26` / `c11-v27-32` / `c11-v33-41` / `c11-v42-54` sibling-t4 cuts; `c12-v1-7` / `c12-v8-12`; `c12-v13-34` kept whole) are settled at build time by ruling 39's procedure:** each builder reads its boundary plates and promotes its own row's `confidence` cell, or STOPS and reports. The p. 381 gate falls at ¶ 69 / `CAPITULUM XV.` on p. 381.

### Tool job (ruling 76): recorded, NOT run

J-1..J-11 as one bounded Sonnet job after the gate, order and scope in the sheet § T and ruling 76 (wrong edges first: J-1 the two wrong *ibid. / loc. cit.* bindings, p. 183 n. 6 and p. 263 n. 11; J-2 the p. 237 n. 8 misreads). `tools/build-citations.py` only, then `build-citations.py` → `build-index-json.py`; no chunk file, no `tools/authorities.json`. **The J-numbering supersedes ruling 62's T-1..T-9 and the docket's T-numbers; the crosswalk is in ruling 76.** Baseline below (QA 213, anaphora unresolved 379).

### Deploy

Nothing deployed, nothing pushed by this close. **The deploy of 2026-11-15 (`dpl_HvqZTb6cavhRgDmA5JDeafXUj7nQ`, pp. 3–288) predates these edits, so the 14 changed lines are NOT live until the next deploy** — which, like the push, is Wilson's own OK.

---

## CLOSE — suite re-run after the edits (2026-11-15), against the baseline

| check | after the edits | baseline (passes draft) | difference |
|---|---|---|---|
| live flags | **vol7 63 chunks, 2 occurrences = 1 flag** (`c5-v12-16` p. 122 n. 11) | same | none |
| `check-vol5-apparatus.py --volume=vol7` | **63 chunks, 3,200 entries, all checks passed** (p. 288 `1-3 ok PENDING n.4–11`) | same | none |
| `check-vol5-census.py` | **vol7 63/63 on disk and in ledger; 178 runovers (153 gutter / 25 page; 62 positive, 1 negative)** | same | none |
| `polish-style-scan.py --volume 7` | **CLEAN (63 files)**; unscoped 11 issues / 6 chunks / 2,381 scanned, zero in vol7 | same | none |
| `build-citations.py` (`--out` / `--qa` to the scratchpad) | **42,717 records; QA 213**; anaphora 2,321 + 86, **unresolved 379**; coordinate ibid. 477 (374 / 103); printed slips 23, 0 stale; both outputs **byte-identical** to `index/citations.tsv` and `manual-review/citation-qa-report.md` (`cmp`) | same | none, as predicted: the ledger is built from the Latin halves, and the edits are English / Notes only |
| `tools/build-authorities.py` | **2,381 chunks; 44,993 apparatus entries; 18,490 authority records** (98.1 % to a work); `index/authorities.tsv` unchanged (`git status` clean) | 18,490 (via `build-index-json.py`) | none |
| `build-index-json.py` | **crossref 1,862 cited / 11,238 backlinks**; goto 2,380; authorities 89 / 436 / 18,490 | same | none |
| `node site/scripts/build-content.mjs` (before and after `build-index-json.py`) | **19 books, 2,380 / 2,380 translated** | same | none |
| `validate-chunk.py` (all 63) | **63 × "1 checked, 0 failed"** | 63 OK | none |
| `c8-v49-56` verse tags | **`(Vers.` 8 La = 8 En; `(V. N` body tags 0** | En 0 `(Vers.` / 8 `(V.` | D-1 applied |

`vercel build` was not run; nothing was deployed.

**Front: `bon-luc-c11-v14-26`** (manifest stage-4 row 1, `low`; ¶¶ 36–57, pp. 288–295; p. 288 nn. 4–11 are its). **The interval pp. 288–381 needs Wilson's go and a burn OK before any builder is dispatched.** No push, no deploy.
