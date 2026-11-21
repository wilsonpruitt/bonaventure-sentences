# Vol VII — *Commentarius in Evangelium S. Lucae*, p. 540 GATE (printed pp. 472–540; Cap. XIX – Cap. XXI complete; Pars II closes) — CLOSED

**STATUS: CLOSED 2026-11-20.** Docket ruled by Wilson in one sitting ("Approve all", 2026-11-20: every ⭐ recommendation of the evidence sheet adopted as written, including the six the sheet marked as his own judgment, items 105–110) → Vol VII rulings 105–130 in `manual-review/vol7-pilot-setup.md` § *LUCAM* p. 540 GATE. **18 lines changed in 8 chunks (7 interval chunks + `c17-v11-19`): 17 English / definition lines + 1 blank line in a Latin body — the sheet's total exactly.** No Latin word, no `**La.**` half, no frontmatter field and no manifest row changed. Ruling 32's table gains three scope clauses (*cultus*, *arguere*, *ortus*); ruling 69's parenthesis is corrected in place, struck text kept. Notes records in 20 chunks. The tool job stays QUEUED, NOT RUN. The live `[?]` (p. 122 n. 11) stays open. **No push, no deploy, no plate deleted.**

Ruling 14 placed this gate at p. 540 (Pars II closes). This close makes no recommendation about the deploy.

**Procedure (the p. 472 gate's):** a read-only agent compiled the evidence sheet, `manual-review/vol7-lucam-p540-gate-evidence-sheet.md` (items 105–130, censuses over the rendered region of the 18 interval chunks and, for consistency questions, all 119), and ran Passes 1–4 into `manual-review/vol7-lucam-p540-gate-passes-draft.md` (both committed at `a024cc4`; the draft's N-1..N-4 are items 119, 120, 121, 110, its R-1 item 122). Both documents are the evidence record and are summarised here, not repeated. Wilson ruled in one sitting; the edits, the re-run and this record then closed the gate. Every file was backed up before editing (session scratchpad, `g540a/bak/`); each target line was re-read against the sheet's "before" and every edit was an exact-match replacement asserted unique on its line. **No item was stopped: every "before" matched.**

**Scope: the 18 chunks of pp. 472–540** (`bon-luc-c19-v1-10` → `bon-luc-c21-v28-38`; XIX 7 · XX 5 · XXI 6), **898 numbered apparatus entries, 13 `tr-` notes**; censuses over all 119 *Lucam* chunks (pp. 3–540, 6,522 entries, 92 → 93 `tr-` notes). **p. 540 nn. 2–10 belong to the next interval** (Cap. XXII ¶ 1, unbuilt; checker `PENDING n.2,3,4,5,6,7,8,9,10`).

---

## PASS 1 — live flags: **AS EXPECTED**

`check-live-flags.py vol7` → 119 chunks, **2 occurrences = one flag, La + En: `bon-luc-c5-v12-16` p. 122 n. 11** (*A C G E [?]*). Same after the edits. Stays open (rulings 59, 73, 90, 102, 124). Zero `[?]` in the 18 interval chunks; three `[so printed]`, all English-side, ratified (ruling 124).

## PASS 2 — mechanical suite: **CLEAN** (figures below, § CLOSE)

## PASS 3 — read-through / consistency: **N-1..N-4 and R-1 found; D-1..D-6 CONFIRMED (D-1, D-4 wider than recorded)**

La/En parity in every ¶ of the 18 (anchors 898 = 898 in order; page markers; ¶ numbers; `####` 16 = 16 = the manifest's cells; guillemets ¶ by ¶; verse tags 126); 13 interval `tr-` notes paired, no new id; 18 shared seams, hand-offs contiguous; old ground byte-unchanged since `3114828`. N-1 *poena* "penalty" ×2 (item 119); N-2 Job 36:13 "provoke" (item 120); N-3 paragraph shape (item 121); N-4 `c21-v5-11` without `tr-praeceptor` (item 110); R-1 the 518L position (item 122).

## PASS 4 — plate cleanup: **REPORTED, NOTHING DELETED (deletion OWED, Wilson's OK)**

`raw/vision/vol7/` holds 462 plates, 1,807 MB. This interval's are **pp. 472–539, 68 files, ~269 MB**: deletable now the gate is closed (ruling 130), but a deletion is a hard stop and Wilson has not given it. The command, for his yes: `rm raw/vision/vol7/p-{472..539}.png` (every one regenerable: `python3.11 tools/extract-pages.py --volume vol7 --pages N --dpi 300`). pp. 540–541 stay (manifest stage 7); the eight pilot / Corrigenda leaves stay; pp. 88–471 (384 files, 1,517 MB) also left to Wilson. This close read no plate.

---

## THE DOCKET — RULED 2026-11-20, "Approve all"

| # | item | ruling | lines applied |
|---|---|---|---|
| 105 | D-1 [365]: *virtus* in `c19-v29-35` | **"power" at the eight sites** (ruling 47 applied); ¶ 52 *doctrina virtutum* stays; + `c21-v25-27` *resistendi virtus* ×2 | 5 + 2 |
| 106 | item 12 / D-3 [416]: Luke 16:8 | **both kept**, a ruling-28 split; recorded in `c16-v1-8` and `c20-v27-40` | 0 |
| 107 | item 13 / D-4 [459]: *excidium* | **split kept, scoped**: "overthrow" only where *destructio* stands under *excidium* (`c21-v20-24` ¶¶ 28, 35); *eversio* "overturning" the cost | 0 |
| 108 | item 18 [426]: *simulatio* in `c20-v41-47` | **"dissembling" in the prose; the lemma keeps the Douay's "Feigning"** | 4 |
| 109 | items 2, A-1: ruling 39's nine promotions; Cap. XXI 4(c) | **ratified as built; 4(c) not taken** | 0 |
| 110 | D-2 [443], N-4: `tr-praeceptor` | **clause struck at `c17-v11-19`; ruling 69 corrected; note added at `c21-v5-11` ¶ 12** | 1 + 2 |
| 111 | item 14 / D-5 [428]: *cautela* | **"caution"**; the one "wariness" conformed | 1 |
| 112 | item 15: *cultus* | ratified; **scope clause into ruling 32's row** | 0 |
| 113 | item 17: *arguere* logical | ratified "argue"; **clause into ruling 32's row** | 0 |
| 114 | item 16 [407]: *denarius* | "penny" kept; the echo's loss recorded | 0 |
| 115 | item 20 [476]: *ortus* of trees | "birth" ratified; **the offered clause into ruling 32's row** (the sheet's third table clause) | 0 |
| 116 | item 19: *claritas* / *splendor* | ratified | 0 |
| 117 | item 21: the 13 `tr-` notes; *lumina* | ratified as placed; rule not narrowed | 0 |
| 118 | item 22: *intellectus / intelligentia* | ratified | 0 |
| 119 | N-1: *poena* "penalty" ×2 | **"punishment"** (`CLAUDE.md:3502`) | 2 |
| 120 | N-2: Job 36:13 | **"prove"**, the Douay | (in 108's four) |
| 121 | N-3: paragraph shape | **blank line inserted** above Latin ¶ 16 of `c20-v10-18`; four English breaks recorded; validator check queued | 1 |
| 122 | D-6, R-1: 518L position | **~0.53**; two records corrected | doc |
| 123–127 | Batches A–H | ratified (E–G as transcribed); H banked | 0 |
| 128 | records | below | 0 |
| 129 | tool items | folded into J-1..J-12; **QUEUED, NOT RUN** | 0 text |
| 130 | plates | pp. 472–539 deletable; **deletion owed, Wilson's OK** | — |

### Lines changed (git diff)

| file | English / En. / def lines | Notes | Latin / La. lines |
|---|---|---|---|
| `vol7/bon-luc-c19-v29-35.md` | 5 (105: ll. 91, 99, 111, 113, 298 — 8 "virtue" → "power") | register line amended in place; 1 gate paragraph | **0** |
| `vol7/bon-luc-c21-v25-27.md` | 2 (105: ll. 70, 160 "strength" → "power" of resisting) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c20-v41-47.md` | 4 (108 + 120: ll. 96, 98, 106, 108 — 7 "feigning / feignedly" → "dissembling / dissemblingly"; "provoke" → "prove") | the "Kept as the Douay" Job 36:13 entry amended in place; 1 gate paragraph | **0** |
| `vol7/bon-luc-c21-v5-11.md` | 2 (110: l. 80 anchor; 1 new `[^tr-praeceptor]` definition) | 1 gate paragraph | **0** |
| `vol7/bon-luc-c17-v11-19.md` | 1 (110: l. 347, the "last *praeceptor*" clause struck) | Provenance amended in place; 1 gate paragraph | **0** |
| `vol7/bon-luc-c20-v27-40.md` | 2 (119: ll. 94, 196 "penalty" → "punishment") | item (414) and the Provenance "~0.36" amended in place (122); 1 gate paragraph | **0** |
| `vol7/bon-luc-c20-v19-26.md` | 1 (111: l. 82 "wariness" → "caution") | 1 gate paragraph | **0** |
| `vol7/bon-luc-c20-v10-18.md` | 0 | 1 gate paragraph | **1 blank line** (121: above ¶ 16; no word) |
| the other 10 interval chunks + `c16-v1-8` | 0 | 1 gate paragraph each | **0** |

**18 lines in 8 chunks = the sheet's 18 / 8.** By item: 105 7, 108 + 120 4, 110 3, 111 1, 119 2, 121 1. Classified from `git diff -U0 -- vol7`: 21 modified lines = the 16 modified text lines + 5 Notes lines amended in place (`c19-v29-35` 1, `c20-v27-40` 2, `c20-v41-47` 1, `c17-v11-19` 1); added lines = the new definition and its blank separator, the Latin blank line, and 20 appended gate paragraphs with their separators. **Frontmatter, every `**La.**` half and the `## Latin` body of all 20 touched files compare identical with the pre-edit backups (script); `c20-v10-18`'s Latin differs only by the one blank line.**

**Also changed (doc):** `manual-review/vol7-pilot-setup.md` (ruling 32's *cultus*, *arguere* and *ortus* rows gain scope clauses; ruling 69's parenthesis struck and corrected in place; rulings 105–130 appended); `manual-review/lucam-chunk-manifest-notes.md` § Stage 6 l. 980 (518L ~~518.36~~ 518.53, with the shifted section lengths ~2.0 / ~1.7). **The manifest TSV is unchanged.** No CLAUDE.md line touched. No tool regenerates anything from the rulings file (the p. 472 close ran none; `build-content.mjs` reads it and was run).

### Re-counts after the edits (rendered region)

- `c19-v29-35`: *virtus* "virtue" at the eight ruling-105 sites **0**; the one remaining "virtues" is ¶ 52 *doctrina virtutum* (right). `c21-v25-27` "strength of resisting" **0**.
- `c20-v27-40` *poena* "penalt-" **0**.
- "wariness" for *cautela*: **0** in all 119 chunks.
- "feigning" in `c20-v41-47`'s rendered region: **only the two Luke 20:47 lemma sites** (¶ 56 "*Feigning long prayer*", p. 520 n. 1 **En.**); **0 in prose**; "feignedly" 0.
- Job 36:13: **"dissemblers and crafty men prove the wrath of God" at both sites** (`c20-v19-26` ¶ 26, `c20-v41-47` ¶ 56).
- `tr-praeceptor`: anchored at `c21-v5-11` ¶ 12 and defined (7 definitions in Vol VII, was 6; `tr-` notes 92 → 93); **the "last *praeceptor*" clause is gone from `c17-v11-19`'s definition** (the phrase survives only struck, in that chunk's Provenance).

### Records (item 128; no text effect)

- **Page-crossing runovers in the interval are FIVE, not the resume's three:** p. 478 n. 14, p. 485 n. 15, **p. 488 n. 11** (`c19-v29-35`), p. 507 n. 15, **p. 513 n. 14** (`c20-v27-40`). Interval runovers 32 = 27 gutter + 5 page (253 → 285).
- **D-1 is eight sites on five lines**, not ¶ 50's two (ruling 105); **D-4 is six "destruction" against two "overthrow"**, one of the six inside `c21-v20-24` (ruling 107).
- **Ruling 69's "one *Praeceptor* left in the work, Luke 17:13" was wrong** — corrected in place (ruling 110).
- **`c20-v27-40`'s (414) "read at ~0.36"** repeated stage 6's figure; the plate has ~0.53 (ruling 122). The same chunk's Provenance carried the same figure; amended with it.
- **The resume's T-e list enumerates 10 of the interval's 15 newly unresolved anaphors;** the total 427 → 442 is right. The full 15 (sheet J-9): p. 480 n. 2 · 492 n. 1 · 496 n. 9 · 497 nn. 5, 13 · 499 n. 12 · 502 n. 4 · 503 n. 10 · 518 n. 9 · 521 n. 11 · 525 nn. 5, 10 · 530 n. 6 · 533 n. 10 ×2.
- **`c20-v41-47`'s Notes listed Job 36:13 under "Kept as the Douay"** while the English had "provoke"; true now (ruling 120), entry amended in place.
- **`c21-v5-11`'s (443) "ruling 69 owes no note here"** misread ruling 69 (ruling 110).
- **Superseded word in a status string:** `c20-v41-47` `transcription_status` keeps "the feigning of virtues" (frontmatter, not rendered; ruling 103's practice).
- **Carried again, not on this docket, not edited (ruling 103's five old-ground lines):** *infidelitas* "infidelity" at `c7-v24-35` ¶ 57 ×2 and `c8-v34-39` p. 207 n. 11 **En.**; "unbelief" at `c7-v17-23` ¶ 37 and `c1-v18-25` p. 18 n. 6, against ruling 71.
- **p. 538 n. 10's *infra c. 22. n. 2. et 10*** is to be checked when Cap. XXII is built.

### Tool job (rulings 76, 92, 104, 129): recorded, NOT run

J-1..J-12 with this interval's sites folded in (ruling 129): **J-1** + 8 wrong edges + 1 doubtful; **J-1 / D4** three page-split body ordinals with no record (`c21-v28-38` ¶¶ 50, 54, 57); **J-3** p. 511 n. 1, p. 510 n. 4, p. 524 n. 3; **J-4** 13 accusative *notam N* sites; **J-9** 15 unresolvable (427 → 442); J-6 / D5, J-11 as tabled; **new:** a `validate-chunk.py` check failing a numbered paragraph with no blank line above it (ruling 121). One bounded job; `tools/build-citations.py` (and that one validator check) only, then `build-citations.py` → `build-index-json.py`; no chunk file. Report → fix → report. Baseline: QA 213, anaphora unresolved 442.

### Manifest stage 7 and the front

**Stage 7 is NOT drawn.** Stage 6 ends at `bon-luc-c21-v28-38`; the manifest has no row past it, and **p. 540 nn. 2–10 are PENDING for Cap. XXII**. **The next step is drawing manifest stage 7** (Cap. XXII ¶ 1 on p. 540, below `CAPITULUM XXII.` and `Pars III.`, → the work close at p. 604, ruling 2; every boundary read on a 300 dpi crop). **It needs Wilson's go.** Then the build to the work close, then the Appendix (ruling 7).

### Deploy

Nothing deployed, nothing pushed by this close. **The live site is through p. 381.** Push and deploy are each Wilson's own OK. `index/authorities.tsv` still lacks the Cap. XV–XXI rows (a regeneration owed before the next deploy, Wilson's call; not run here).

---

## CLOSE — suite re-run after the edits (2026-11-20), against the baseline

| check | after the edits | baseline (passes draft) | difference |
|---|---|---|---|
| live flags | **vol7 119 chunks, 2 occurrences = 1 flag** (`c5-v12-16` p. 122 n. 11) | same | none |
| `check-vol5-apparatus.py --volume=vol7` | **119 chunks, 6,522 entries, all checks passed** (p. 540 `1-1 ok PENDING n.2..10`) | same | none |
| `check-vol5-census.py --volume=vol7` | **vol7 119/119 on disk and in ledger; 285 runovers (247 gutter / 38 page; 112 positive, 7 negative)**; "Rosters agree" | same | none |
| `polish-style-scan.py --volume 7` | **CLEAN (vol7, 119 files)** (one V5NOTES hit — a literal bracket-caret in this close's own `c21-v5-11` gate paragraph — fixed before the final run) | same | none |
| `validate-chunk.py` (the 20 touched chunks) | **20 × "1 checked, 0 failed"** | 18 × OK | none |
| `build-citations.py` | **2,437 chunks; 48,221 records** (scripture 33,480 · crossref 13,574 · authority 1,167); **QA 213**; anaphora 2,372 + 86, **unresolved 442**; coordinate ibid. 492 (388 / 104); printed slips 23, 0 stale; `index/citations.tsv` and `manual-review/citation-qa-report.md` **unchanged** (`git status` clean for both) | same | none: the ledger is built from the Latin halves; the edits are English / Notes (and one blank Latin line) only |
| `build-content.mjs` → `build-index-json.py` → `build-content.mjs` | **19 books, 2,436 / 2,436 translated** (both runs); **crossref 1,917 cited / 11,533 backlinks**; goto 2,436 / 5,525; authorities 89 / 437 / 18,989 | same | none |

Only `site/src/data/*` and `site/public/goto.json` (gitignored) were rewritten by the build steps; nothing regenerated and tracked changed, so there is no regenerated output to commit (as at `3114828`). `git status` after the suite shows only the files this close edited (and the untracked `.claude/settings.local.json`, not committed). `vercel build` was not run; nothing was deployed; no plate was deleted; no `git stash`.

**Front: drawing manifest stage 7** (Cap. XXII ¶ 1 on p. 540 → the work close at p. 604). Needs Wilson's go. No push, no deploy.
