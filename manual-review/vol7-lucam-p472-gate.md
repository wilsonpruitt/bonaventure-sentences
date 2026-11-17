# Vol VII — *Commentarius in Evangelium S. Lucae*, p. 472 GATE (printed pp. 381–472; Cap. XV – Cap. XVIII complete) — CLOSED

**STATUS: CLOSED 2026-11-17.** Docket ruled by Wilson in one sitting ("Approve all", 2026-11-17: every ⭐ recommendation of the evidence sheet adopted as written, including the four the sheet marked as his own judgment — § 1 *puer* "child(ren)"; § 3 *supplicium* → "penalty" per `CLAUDE.md:3502`, re-opening ruling 87's *supplicium* clause; the ~25 pre-interval lines go in now; D-3's scope clause in ruling 32's row) → Vol VII rulings 93–104 in `manual-review/vol7-pilot-setup.md` § *LUCAM* p. 472 GATE. **60 English lines changed: 35 in 13 interval chunks + 25 in 14 pre-interval chunks (one of the 60 is a `tr-` definition), plus Notes records in 28 chunks; no line in any `## Latin` body, `**La.**` half or frontmatter changed.** Four manifest cells corrected in three rows. Ruling 32's *intellectus* row gains a scope clause; ruling 54 a clarifying sentence; ruling 18 the passive form; ruling 87's *supplicium* clause is struck and replaced. **`CLAUDE.md:3502` stands; no CLAUDE.md change.** F11–F12 join the queued tool job, which stays QUEUED, NOT RUN. The live `[?]` (p. 122 n. 11) stays open. **No push, no deploy.**

Ruling 14 placed this gate at p. 472 (close of c. 18). This close makes no recommendation about the deploy.

**Procedure (the p. 288 / p. 381 gates'):** a read-only agent compiled the evidence sheet, `manual-review/vol7-lucam-p472-gate-evidence-sheet.md` (censuses over the rendered region of all 101 chunks and over Vols V–VI where a corpus precedent decided, the decisive sentence, alternatives with costs, a ⭐ per item, and fourteen "found by the sheet" items F1–F14); a second read-only agent ran Passes 1–3 into `manual-review/vol7-lucam-p472-gate-passes-draft.md` (both committed at `69dd6f9`). Both documents are kept as the evidence record and are summarised here, not repeated. Wilson ruled in one sitting; the edits, the re-run and Pass 4 then closed the gate. Every file was backed up before editing (no repo backup convention exists for a gate close; copies in the session scratchpad, `p472-backups/`).

**Scope: the 19 chunks of pp. 381–472** (`bon-luc-c15-v1-7` → `bon-luc-c18-v28-43`; XV 5 · XVI 4 · XVII 5 · XVIII 5), **1,195 numbered apparatus entries, 14 `tr-` notes**; censuses over all 101 *Lucam* chunks (pp. 3–472, 5,624 entries, 79 `tr-` notes). **p. 472 nn. 8–12 belong to the next interval** (Cap. XIX ¶ 1, unbuilt; checker `PENDING n.8,9,10,11,12`).

---

## PASS 1 — live flags: **AS EXPECTED**

`check-live-flags.py vol7` → 101 chunks, **2 occurrences = one flag, La + En: `bon-luc-c5-v12-16` p. 122 n. 11** (*A C G E [?]*). Same after the edits. Stays open (rulings 59, 73, 90, 102). Zero `[?]` in the 19 interval chunks.

## PASS 2 — mechanical suite: **CLEAN** (figures below, § CLOSE)

## PASS 3 — read-through / consistency: **NO NEW DEFECT beyond the sheet's; D-1..D-7 CONFIRMED**

La/En parity in every ¶ of all 101 chunks (anchors 5,624 = 5,624; page markers; ¶ numbers; `####`; guillemets ¶ by ¶; verse tags); 14 interval `tr-` notes all paired, no new id; no page gap, overlap or abutment pp. 381–472 (19 shared seams); hand-offs agree on every shared page and on p. 472's PENDING. No false Notes self-claim. The passes draft's findings are the sheet's: **N-1 = F2, N-2 = F3, N-3 = F4, R-1 = F10, O-1 in § 1**; O-2 is recorded with item [276] and O-3 is a record (ruling 103).

## PASS 4 — plate cleanup: **NOTHING TO DELETE**

This close read no plate and made no crop. p. 472 serves the next interval's first chunk; whether to delete the pp. 381–471 plates is Wilson's call, not done here.

---

## THE DOCKET — RULED 2026-11-17, "Approve all"

| # | item(s) | ruling | lines applied | recorded |
|---|---|---|---|---|
| § 1 | item 12 [239], F5, passes O-1: *puer* in the children pericope | **"child(ren)"** through `c18-v15-17` ¶¶ 29–33; the three "servant" verses keep the Douay; ruling 54 clarified | 12 | 93 |
| § 3 | item 14 / D-4 [166, 190, 225, 272], F1: *poena* / *supplicium* | `e810ccc` ratified; **the house rule `CLAUDE.md:3502` restored, *supplicium* → "penalty"**; ruling 87's clause replaced | 16 + 11 pre | 94 |
| F2 / F3 | *poena* "penalty" (N-1); *poena* "pains" (N-2) | → "punishment" (6 regions); "pains" kept, a recorded sense exception | 1 + 5 pre; 0 | 95 |
| F4, F6, F7, F9 | *impie*; *simulatio*; *infidelitas*; `tr-praeceptor` | "impious one"; "dissembling" (+ 8 pre); "faithlessness"; Douay claim struck | 1; 2 + 8 pre; 2; 1 | 96 |
| D-3 + F8 | *intellectus / affectus* | ratified; **scope clause into ruling 32's row**; the two pre-interval formula sites → "intellect" | 0 + 2 pre | 97 |
| § 2 + F14 | item 13 / D-2: Ps. 35:10; John 8:12 | ratified as built (the split by design; John 8:12 exempt, unit = the member ¶¶ 65–66) | 0 + Notes | 98 |
| § 4 + F10 | item 15 / D-5: *pietas* | inventory ratified; ¶ 21 kept literal; `tr-pietas` on the adjective ratified; ¶ 22 → **¶ 21** amended | 0 + Notes | 99 |
| § 5 + A | item 4 / D-1: manifest; items 1–3, 5–6 | **four cells applied**; boundaries and titles ratified | doc | 100 |
| D-7, D-6, 16–19, 21, C | Luke 17:19 / 18:42; *Ducange*; the ratify batches | ratified; ruling 18 gains the passive; *segnitia* NOT changed (left to Wilson's word) | 0 | 101 |
| B, E, F, G, H | corrigenda (none); slips; `[so printed]`; readings; collection change | ratified; Deut. 27:26 as printed; the live `[?]` stays open; H banked | 0 | 102 |
| F13; O-2, O-3 | *mirus*; passes observations | recorded; three further *infidelitas* sites found while applying, not edited | 0 | 103 |
| T + F11, F12 | J-1 13 wrong edges; J-4 10 sites; J-5; J-12 row p. 405 n. 10 | folded into the one job; **QUEUED, NOT RUN** | 0 text | 104 |

### Lines changed (git diff)

| file | English / En. lines | Notes | Latin / La. lines |
|---|---|---|---|
| `vol7/bon-luc-c18-v15-17.md` | 12 (§ 1: ¶¶ 29, 29 cont., 30, 31, 32, 33; p. 458 nn. 2, 12, 15, p. 459 n. 12, p. 460 nn. 1, 2 **En.** — 56 "boy(s)" → "child(ren)") | 1 gate paragraph (item (239)) | **0** |
| `vol7/bon-luc-c16-v22-31.md` | 5 (§ 3: ¶ 47, ¶ 48, ¶ 54, ¶ 58 ×2 lines; 6 sites) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c17-v20-30.md` | 3 (§ 3: ¶ 49, ¶ 50, ¶ 52; 5 sites) | 1 gate paragraph (D-4 ratified; item (166)) | **0** |
| `vol7/bon-luc-c17-v1-4.md` | 2 (§ 3: ¶ 1, ¶ 5) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c17-v31-37.md` | 2 (§ 3: ¶ 58, ¶ 59) | 1 gate paragraph (Ps. 35:10 record) | **0** |
| `vol7/bon-luc-c18-v28-43.md` | 2 (§ 3: ¶ 52, ¶ 55) | 1 gate paragraph (John 8:12 unit; D-7; [276]) | **0** |
| `vol7/bon-luc-c18-v1-8.md` | 1 (§ 3: p. 452 n. 1 **En.**) | 1 gate paragraph (O-1; [201]) | **0** |
| `vol7/bon-luc-c18-v9-14.md` | 1 (§ 3: ¶ 22) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c15-v1-7.md` | 2 (F6: ¶ 1, ¶ 5) | 1 gate paragraph (manifest cell) | **0** |
| `vol7/bon-luc-c16-v9-18.md` | 2 (F7: ¶ 17, ¶ 19) | item (88) and two other "¶ 22" amended in place, struck wording kept (F10); 1 gate paragraph | **0** |
| `vol7/bon-luc-c16-v1-8.md` | 1 (F2: p. 405 n. 3 **En.**) | 1 gate paragraph (manifest cells) | **0** |
| `vol7/bon-luc-c18-v18-27.md` | 1 (F4: ¶ 44) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c17-v11-19.md` | 1 (F9: the `tr-praeceptor` definition) | 1 gate paragraph (D-7) | **0** |
| `vol7/bon-luc-c16-v19-22.md` | 0 | 1 gate paragraph (F3 sense exception; Ps. 35:10 record) | **0** |
| `vol7/bon-luc-c12-v49-59.md` (pre-interval) | 4 (§ 3 ¶ 87 ×2 sites + F2 on the same line; F2 ¶ 86, p. 335 nn. 9, 13 **En.**) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c12-v1-7.md` (pre-interval) | 2 (§ 3: ¶ 8, 6 sites incl. the elided *spirituale*) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c13-v1-9.md` (pre-interval) | 2 (§ 3: ¶ 1, ¶ 2 ×2 sites) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c13-v22-30.md` (pre-interval) | 3 (§ 3: ¶¶ 48, 59, 63) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c9-v37-45.md`, `c10-v4-16`, `c14-v16-24` (pre-interval) | 1 each (§ 3: ¶ 83; p. 260 n. 6 **En.**; ¶ 49) | 1 gate paragraph each | **0** |
| `vol7/bon-luc-c1-v18-25.md` (pre-interval) | 1 (F2: p. 18 n. 6 **En.**) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c9-v57-62.md` (pre-interval) | 4 (F6: ¶¶ 102–105) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c6-v39-49.md` (pre-interval) | 2 (F6: ¶¶ 99, 105) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c6-v1-11.md`, `c9-v1-9` (pre-interval) | 1 each (F6: ¶ 6 ×2 sites; ¶ 7) | 1 gate paragraph each | **0** |
| `vol7/bon-luc-c1-v39-45.md`, `c1-v46-56` (pre-interval) | 1 each (F8: ¶ 71; ¶ 96) | 1 gate paragraph each | **0** |

**60 English lines: 35 in 13 interval chunks + 25 in 14 pre-interval chunks.** By item — interval: § 1 12, § 3 16, F2 1, F4 1, F6 2, F7 2, F9 1 (= 35, the sheet's figure); pre-interval: § 3 11, F2 5, F6 8, F8 2, less one line shared by § 3 and F2 (`c12-v49-59` ¶ 87) (= 25, the sheet's "~25"). The sheet's "12 interval chunks" is 13 by file count; its line total is exact. Classified from `git diff -U0`: 62 modified lines = the 60 English lines + 2 Notes lines in `c16-v9-18` (F10); every other `+` line is an appended gate paragraph (28) or its blank separator. **0 `+` lines carry `**La.**`; the `## Latin` body, every `**La.**` half and the frontmatter of all 101 files compare identical with the pre-edit backups (script).** Each site was read with its Latin before the edit; every edit was an exact-match replacement on its own line.

**Also changed (doc):** `manual-review/lucam-chunk-manifest.tsv` (four cells, ruling 100); `manual-review/vol7-pilot-setup.md` (ruling 32's *intellectus* row: the scope clause; ruling 54: the clarification; ruling 18: the passive; ruling 87: the *supplicium* clause struck and replaced; rulings 93–104). No CLAUDE.md line touched.

### The *supplicium* record (ruling 94)

The register line every builder of the interval carried, "*supplicium* 'punishment' / 'torment' by sense (ruling 87; never 'penalty')", **came from the orchestrator's briefs for chunks 14–19 of stage 5 and from the `e810ccc` correction's framing, not from any ruling.** Ruling 87 ratified "*supplicium*" as one item of a batch of ruling-20 / 28 splits and said nothing about "never 'penalty'"; the p. 381 docket did not put `CLAUDE.md:3502` or Vol VI ruling 59 before Wilson. **The house rule `CLAUDE.md:3502` (*poena* → "punishment"; *supplicium* → "penalty") stands and now governs every site of the work.** After the edits: 45 Latin *supplicium* sites in all 101 chunks, every one rendered "penalty" (per-unit alignment: 0 short), and no unit renders *poena* "penalty" (0 units with "penalt-" whose Latin lacks *supplicium* / *poenalitas*). Five "penalt-" remain for *poenalitas* / *poenalis* (`c1-v18-25`, `c4-v1-13`, `c4-v38-44` ×2, `c9-v32-36`), which `CLAUDE.md:3502` calls other words; recorded, not touched.

### Manifest (ruling 100)

| row | cell | old | new |
|---|---|---|---|
| `bon-luc-c15-v1-7` | `headings` | `capitulum@381;t4@381L;t4@382L;t4@383R` | `capitulum@381;t4@381L;t4@382L;t4@383R;t4@383R` |
| `bon-luc-c16-v1-8` | `headings` | `capitulum@402;t4@402L;t4@402R` | `capitulum@402;t4@402L;t4@402R;t4@402R` |
| `bon-luc-c16-v1-8` | `title_la` | `Primo, de pietate humana quoad opera corporalia tripliciter.` | `Exemplum parabolicum pietatis providae.` |
| `bon-luc-c17-v20-30` | `headings` | `t3@437L;t4@437R;t4@439L` | `t3@437L;t4@437R;t4@437R;t4@439L` |

`bon-luc-c16-v1-8`'s `title_la_source` is unchanged (`rubric-t4 p.402R`, now naming the lower 402R t4, the `c18-v18-27` convention). Span, END, confidence: unaffected. Ruling 34's limit kept: these are a gate's cell edits.

### Records (no text effect)

- **F3:** `c16-v19-22` p. 417 n. 12 "pains" is a disclosed sense exception (ruling 95).
- **F13:** *mirus* "wonderful" / "marvellous" work-wide; no row made (ruling 103).
- **F14:** the Ps. 35:10 "inconsistency" is the test working (ruling 98).
- **Not applied, sheet left it open:** *segnitia* "slackness" (`c16-v9-18` ¶ 31, [93]) — the sheet's star is followed by "or record — Wilson's word" and the summary calls it optional; stands "sloth", carried.
- **Found while applying, not on the docket, not edited (ruling 103):** *infidelitas* "infidelity" at `c7-v24-35` ¶ 57 ×2 and `c8-v34-39` p. 207 n. 11 **En.**; "unbelief" at `c7-v17-23` ¶ 37 and `c1-v18-25` p. 18 n. 6 — the sheet's F7 census missed these five; for a later docket under ruling 71. The `transcription_status` strings of `c15-v1-7`, `c18-v15-17`, `c18-v28-43` keep the build's "simulation" / "boys" / "torment" (frontmatter, not rendered).

### Tool job (rulings 76, 92, 104): recorded, NOT run

J-1..J-12 with this interval's sites folded in: **J-1 now 13 wrong edges** (T-b's twelve + F11 p. 386 n. 8); **J-4 10 sites** (F12); J-5 + p. 399 n. 1 etc.; J-6 +3; J-3 p. 471 n. 6; J-12 + the p. 405 n. 10 `CROSSREF_SLIPS` row. One bounded job; `tools/build-citations.py` only, then `build-citations.py` → `build-index-json.py`; no chunk file. Baseline below (QA 213, anaphora unresolved 427).

### Manifest stage 6 and the front

**Stage 6 is NOT drawn.** Stage 5 (`21637e0`) ends at `bon-luc-c18-v28-43`; the manifest has no next row. **The next step is drawing manifest stage 6** (Cap. XIX ¶ 1 on p. 472, below the full-measure `CAPITULUM XIX.`, through the p. 540 gate, ruling 2; every boundary read on a 300 dpi crop, in its own commit). **It needs Wilson's go.**

### Deploy

Nothing deployed, nothing pushed by this close. Push and deploy are each Wilson's own OK. `index/authorities.tsv` still lacks the Cap. XV–XVIII rows (a regeneration owed before the next deploy, Wilson's call; not run here).

---

## CLOSE — suite re-run after the edits (2026-11-17), against the baseline

| check | after the edits | baseline (passes draft) | difference |
|---|---|---|---|
| live flags | **vol7 101 chunks, 2 occurrences = 1 flag** (`c5-v12-16` p. 122 n. 11) | same | none |
| `check-vol5-apparatus.py --volume=vol7` | **101 chunks, 5,624 entries, all checks passed** (p. 472 `1-7 ok PENDING n.8,9,10,11,12`) | same | none |
| `check-vol5-census.py --volume=vol7` | **vol7 101/101 on disk and in ledger; 253 runovers (220 gutter / 33 page; 95 positive, 6 negative)**; "Rosters agree" | same | none |
| `polish-style-scan.py --volume 7` | **CLEAN (vol7, 101 files)** (one V5NOTES hit in this close's own `c17-v11-19` gate paragraph fixed before the final run) | same | none |
| `validate-chunk.py` (the 28 touched chunks) | **28 × "1 checked, 0 failed"** | OK | none |
| `build-citations.py` | **2,419 chunks; 46,767 records; QA 213**; anaphora 2,361 + 86, **unresolved 427**; coordinate ibid. 487 (384 / 103); printed slips 23, 0 stale; `index/citations.tsv` and `manual-review/citation-qa-report.md` **unchanged** (`git status` clean for both) | same | none: the ledger is built from the Latin halves, and the edits are English / Notes only |
| `build-content.mjs` → `build-index-json.py` → `build-content.mjs` | **19 books, 2,418 / 2,418 translated** (both runs); **crossref 1,901 cited / 11,445 backlinks**; goto 2,418 / 5,457; authorities 89 / 437 / 18,989 | same | none |
| re-counts (rendered region) | *supplicium*: 45 Latin sites, 0 rendered "punishment" / "torment"; *poena* "penalt-": 0 units; English "simulation": 0 (the 4 regex hits are *assimulationes*, *simulationes* in Latin italic, and "dissimulation" ×2); `c16-v9-18` "infidelity": 0; `c18-v15-17` "boy(s)": 0 (60 "child(ren)"); `c18-v18-27` "wicked one": 0 | — | as ruled |

Only `site/src/data/*` and `site/public/goto.json` (gitignored) were rewritten by the build steps; `git status` after the suite shows only the files this close edited (and the untracked `.claude/settings.local.json`, not committed). `vercel build` was not run; nothing was deployed.

**Front: drawing manifest stage 6** (Cap. XIX – the p. 540 gate). Needs Wilson's go. No push, no deploy.
