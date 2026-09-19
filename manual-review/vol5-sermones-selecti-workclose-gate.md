# Vol V — *Sermones selecti de rebus theologicis* WORK-CLOSE GATE (printed pp. 535–579) — AND THE CLOSE OF VOLUME V

Run 2026-09-19, after `bon-serm-tract` (`026d7e7`) and after Wilson's **rulings 6 and 7** (`b464701`). **This work has
ONE gate and no shakedown (ruling 4)**, so the whole 45-page span is audited here for the first time. **It is the last
work in Tome V: this gate closes Volume V.** Modelled on `manual-review/vol5-perfectione-evangelica-workclose-gate.md`;
pass structure and evidential standard follow it.

**Scope: FIVE chunks — `bon-serm-s1` · `s2` · `s3` · `s4` · `bon-serm-tract` — pp. 535–579 with no gap, 456 numbered
apparatus entries + 4 `tr-lumen` translator's notes.**

| chunk | division | type | pages | entries | ¶¶ | runovers (gutter / page) |
|---|---|---|---|---|---|---|
| `bon-serm-s1` | 1 | sermo | 535–538 | 33 | 16 | 1 / 0 |
| `bon-serm-s2` | 2 | sermo | 539–553 | 157 | 47 | 4 / 1 |
| `bon-serm-s3` | 3 | sermo | 553–566 | 121 | 42 | 10 / 0 |
| `bon-serm-s4` | 4 | sermo | 567–574 | 92 | 28 | 4 / 0 |
| **`bon-serm-tract`** | **5** | **tractatus** | 574–579 | 53 | 16 | 4 / 1 |
| **total** | | | **45 pp.** | **456** | **149** | **23 / 2** |

**Denominators.** Entry counts are parsed from every `[^p<page>-<n>]:` **definition** in each chunk's `## Apparatus`
(`tr-` labels excluded, as `check-vol5-apparatus.py` excludes them). ¶ counts are the numbered paragraphs of `## Latin`,
checked identical in `## English`. Runovers are the five `vol5-runover-ledger.tsv` lines. **Every census in this log is
taken over the LIVE REGION — frontmatter and `## Notes` stripped — unless it says otherwise.** The builders' predicted
totals (456 entries) were **re-derived from the files and not adopted**; they agree.

**Result: ZERO TEXT DEFECTS. Zero rendered lines changed. Four stale documentation claims corrected in two chunks'
`transcription_status` / `## Notes` (the "five of five on the Explicit" forwarding, and one Pass-A half-chunk count).
Passes 1–3 clean; all seven rulings verified as applied; all four interior boundaries match the frozen record digit
for digit. Pass 4 done. Committed locally; NOT pushed, NOT deployed.**

---

## ✏️ Repaired — stale documentation only (zero rendered text touched)

### (a) The forwarded "five of five on the Explicit" claim, withdrawn in `s3` (×2 + status) and `s4` (×1 + status)

`bon-serm-tract` measured the Tractatus's column foot on p. 579 at 4× and found **no** printed `— Explicit.` — the body
ends at *Amen.* and the full-measure colophon `EXPLICIUNT SERMONES SELECTI.` follows. **The work is FOUR of five.** The
gate re-derived it from the files: the Latin of `s1`, `s2`, `s3` and `s4` each ends `— Exᴘʟɪᴄɪᴛ.`; `tract` ends
`…pausare possimus. Amen.` then `### EXPLICIUNT SERMONES SELECTI.` CLAUDE.md § SERMONES SELECTI already carried the
correction (`3997e92`).

**But two chunks still asserted the opposite in their own records**, and not in one place each:

- `s3` `transcription_status`: *"Sermo III is the FIFTH of five units in the work to carry it"* — ⚠ **arithmetically
  impossible from a chunk built third**; it is a pilot claim restated as a count.
- `s3` Notes: *"The work's pattern is five of five: Sermones I, II, III, IV and the Tractatus all carry…"* and item 5,
  *"The `Explicit` result — now CLOSED as a question: five of five units carry it. Recorded here so the gate does not
  re-open it."*
- `s4` `transcription_status`: *"READ AT 4x: the work is five of five on the Explicit."*
- `s4` Notes item 5: *"The `Explicit` question is CLOSED — five of five, and mine was read at 4×."*

Each is corrected in place, with the original struck through or quoted and the correction dated. **The measured halves
stand** — `s3`'s and `s4`'s own Explicits were read at 4× and are real. ▶ **The transferable form:** *the measured half
of a sentence does not license its unmeasured half.* `s4` read ITS Explicit and wrote a sentence about FIVE; `s3` closed
a question on a member no one had read. **"Recorded so the gate does not re-open it" is the exact phrase that should make
a gate re-open it** — it marks a claim that has stopped being checked.

### (b) `s3`'s *lumen* site count

`s3`'s `transcription_status` read *"lumen occurs at five sites"*. **The built chunk has SEVEN** in the rendered Latin
body (six `lumen` + one `luminis`: Ps. 106:10 exposition, Ps. 37:11 *lumen oculorum meorum*, *usum luminis*,
*haurit lumen cognitionis*, Bernard's *lumen mentium* ×2, and p. 563's *illuminat omne lumen*). "Five" was **Pass A's
half-chunk count**, never re-derived when Pass B closed the file — the frozen *summary-sentence-is-the-least-reliable-line*
rule, caught once more. Corrected in place; the hand-off's figure of seven was right.

---

## NO DEFECTS FOUND IN THE TEXT

**Every rendered line of the five chunks came through every sweep below unchanged.** For the second work running, a
work whose register was ruled before its first chunk (rulings 1–5, 2026-09-18) and whose two chunk-raised items were
ruled off an evidence sheet before its gate (rulings 6–7) arrived with nothing to repair in the text.

---

## Wilson's seven rulings — verified AS APPLIED, not re-litigated

| # | ruling | how verified | result |
|---|---|---|---|
| 1 | **The Tractatus is the work's FIFTH DIVISION** | frontmatter + built `content.json` | ✅ `bon-serm-tract`: `work: sermones-selecti`, **`division: 5`, `type: tractatus`**; the build renders it **"Tractatus"** under the division title *Tractatus de plantatione Paradisi* (book 14, `divisionLabel: Sermones`); p. 574 n. 8's *annectimus* note is rendered in full. |
| 1b | **roster of FIVE — the suffix-less-slug blind spot** | every enumeration checked | ✅ **Five in every roster the gate ran:** `check-vol5-census.py` (5 ledger lines, `bon-serm-tract` present; rosters agree 167/167) · `check-vol5-apparatus.py` (pp. 574–579 owned) · `build-content.mjs` (book 14 = 5 divisions / 5 questions, all translated) · `build-citations.py` (487 records from `bon-serm-*`, `tract` included) · this gate's own boundary parse (5 chunks). **No enumeration of this work counted four.** |
| 2 | ***magister* → "teacher" throughout Sermo IV, incl. Matt. 23:10** | **live-region census, re-derived** | ✅ **`s4`: 45 *magister*-family sites = 42 in the rendered Latin body + 3 in apparatus La-halves — the frozen figure EXACTLY.** English body: **"teacher" 38 · "teaching office" 4 · "master" ZERO** — also exact. Apparatus En-halves: "teacher" 4, "master" 0. **Matt. 23:10 reads *"One is your teacher, Christ"* at ¶ 1 (p. 567) and ¶ 28**, and Matt. 23:8 at p. 572 n. 11 reads *"for one is your teacher"*. |
| 2b | **⛔ Lombard stays "the Master"** | census, whole work | ✅ **The only *Magister* = Lombard in the work is in `s3`'s apparatus, twice** (p. 556 n. 7 `IV. Sent. d. XI. text. Magistri` and p. 564 n. 2 `IV. Sent. lit. Magistri, d. XI. c. 3`) → **"the text of the Master"** both times. **ZERO Lombard sites in `s4`**, so no Lombard *Magister* was converted and the two senses never meet in one chunk. |
| 3 | **Sermones II and III built in two passes, reading as ONE chunk** | ¶ sequence, page markers, section uniqueness | ✅ **`s2`: 47 ¶¶, contiguous 1..47 in BOTH languages**; the pass boundary at ¶ 37 / p. 549 reads straight on from ¶ 36 (*Viso igitur de conditionibus regni…*). **`s3`: 42 ¶¶, contiguous 1..42 in both**; the pass boundary at ¶ 17 / p. 558 reads straight on (*Tertio praefiguravit…*). Each file has exactly one `## Latin` / `## English` / `## Apparatus` / `## Notes`. Page markers identical Latin↔English (`s2` 539–553, `s3` 553–566). **Runover ledger: no double-count** — `s2`'s five runovers are on five distinct leaves, `s3`'s ten on ten; neither ledger line repeats a page across the pass seam. |
| 4 | **ONE gate at the close, no shakedown** | — | ✅ This is it. |
| 5 | ***lumen*/*lumina* untranslated; *lux* → "light"; one `tr-lumen` note per chunk with a site** | live-region census + note presence | ✅ **Rendered-Latin-body *lumen*-noun sites: `s1` 0 · `s2` 1 · `s3` 7 · `s4` 4 · `tract` 8** (the hand-off's figures). Every one renders "lumen"/"lumina" — **Latin↔English parity exact in every chunk** (English runs +1 on a raw grep only because the anchor label `[^tr-lumen]` contains the string). ⚠ `s2`'s second raw hit is the adjective *luminosum*, and `tract`'s ninth and tenth are *luminaria* → "luminaries" — neither is a *lumen* site. **`tr-lumen` notes: `s1` NONE · `s2` ONE · `s3` ONE · `s4` ONE · `tract` ONE** — exactly one per chunk with a site, none where there is none. |
| 5b | **the two collisions, by eye** | read at the site | ✅ **`s3` p. 563 ¶ 31** *Ipse enim est lux, quae illuminat omne* ***lumen*** → "he is himself the **light** which illumines every ***lumen***". ✅ **`tract` ¶ 5** (p. 576) *ne a splendoribus* ***lucis*** *aeternae procul abscedat, universitatis* ***luminum*** *creatorum circumlustrari fulgoribus* → "…the splendours of eternal **light**… the brightnesses of the whole company of created ***lumina***" — **the sentence that makes the refused *lumina* → "lights" carve-out impossible**, and `tract`'s note says so. |
| 5c | **the verse test** | whole-work search | ⓘ **Ps. 4:7 (*Signatum est super nos lumen*) and Jas. 1:17 (*Patri luminum*) DO NOT OCCUR in this work** — both were forecast from the *perfectione* carry-in and are **unreached**, not broken. The test **was run where the work does reach it**: `s3`'s note records that **Ps. 37:11 *lumen oculorum meorum*** is Ps. 4:7-shaped and keeps "lumen" ("the light of my eyes" being no fixed English name the way "Father of lights" is). Recorded so the absence is not read as an omission. |
| 6 | ***puritas* → "purity" STANDS; *pudicitia* ZERO; *munditia* → cleanness; *castitas* → chastity** | live-region census | ✅ **`pudicit-` ZERO in all five live regions** — the ruling's premise holds. ✅ ***munditia* → "cleanness" 4/4** (`s3` 3, `s4` 1), zero "pureness" anywhere. ✅ ***castitas* → "chastity" 6/6 occurrences** (`s2` 5, `s3` 1). ✅ ***puritas* → "purity" at every site** — ⚠ **but see the count note below.** |
| 7 | ***praeceptor* → "preceptor" at `s1`'s two sites; no third** | live-region census | ✅ **p. 537** Isa. 55:4 *ducem ac* ***praeceptorem*** *gentibus* → "a leader and a **preceptor** to the Gentiles"; **p. 538** *testem… ducem et* ***praeceptorem*** → "a witness, a leader and a **preceptor**". **ZERO `praeceptor-` in `s2`, `s3`, `s4`, `tract`** — no third site. |

### ⚠ On ruling 6's "ONE site" — the ruling holds, the COUNT was low (the *perfectione* ruling-3 slip, in the other direction)

The evidence sheet gave *puritas* **one** site (`s2` p. 546, Bonelli's variant). **Over the live region the *puritas*
family has THREE occurrences, all in `s2`, all on p. 546, all rendered on the "purity" root:**

1. body ¶ 26 *Econtra in luxuria est summa* ***impuritas*** → "the highest **impurity**"
2. body ¶ 27 *Regio igitur* ***puritatis*** *sordidis et inquinatis non convenit* → "the region of **purity**"
3. apparatus p. 546 n. 9, Bonelli's *innocentia et* ***puritas*** *sive castitas* → "innocence and **purity** or chastity"

▶ **The ruling is not disturbed and is not re-opened** — every site already reads "purity", which is what Wilson ruled,
and the decisive premise (*pudicitia* ZERO, so the *perfectione* triple protects nothing here) is exactly true. ⛔ **But
the sheet counted the apparatus variant and missed the body noun two lines above it.** The *perfectione* gate's
ruling-3 count ran **high** (a whole-file grep counting Notes prose); this one ran **low** (a search that found the
variant it was looking for and stopped). **Both are the same instruction: a census for a ruling is taken over the
whole live region, body AND apparatus, and the sheet states the denominator.**

---

## The carried corpus rulings — re-verified across all five chunks (live region)

| ruling | result |
|---|---|
| **1. *intellectus* → "understanding"; bare "intellect" = defect** | ✅ **23 `intellect-` Latin occurrences** (s2 3 · s3 5 · s4 7 · tract 8). **English bare "intellect": 2, both in `s4`, both the phrase *agent intellect*** — p. 572 ¶ 18 *secundum supremam aciem* ***intellectus agentis*** → "the supreme edge of the **agent intellect**", and `s4`'s `tr-lumen` note quoting that phrase. **This is the ratified narrow exception (*scientia Christi* ruling 1, scoped to the PHRASE)** — not a defect. Zero bare "intellect" elsewhere. |
| **2. *lux*/*lumen*** | ✅ above (ruling 5). |
| **3. `contuit-`** | ✅ **ONE site**, `s4` p. 567 n. 7's apparatus, → **"contuition"**. No "intuition" substitute. |
| **5. `fundam. N` → *fundamentum N* (apparatus)** | ✅ **TWO sites in the work, both `s2`, re-derived over the BUILT files as `s2`'s Notes asked:** p. 548 n. 7 `II. Sent. d. 40. a. 1. q. 3.` ***fund.*** `4.` → "*fundamentum* 4" (a third abbreviated form, retained as printed) and p. 552 n. 4 `fundam. 3` → "*fundamentum* 3". **ZERO in `s1`, `s3`, `s4`, `tract`.** ⚠ `s4`'s apparent English hit is the Vulgate *Superaedificati super fundamentum* (Eph. 2:20) in a La-half — scripture, not ruling 5. ▶ **The pilot's raw-side census said ZERO; the built text says TWO.** |
| ***vacatio*/*quies*** | ✅ **`vaca-` ZERO in all five live regions** — the pair remains **untested in this work**. ⚠ The noun *quies* is **not** zero: `tract`'s Summarium *in paradisi* ***quiete*** → "rest" (`tract` Notes). The "Collationes close open, not settled" record stands; the standing claim that the pair is wholly absent from the *Sermones* is false and is corrected in the carry-list below. |
| ***pietas* → piety; *praeceptum*/*mandatum*/*lex*** | Carried; no conflicting rendering met on any sweep. |

---

## Pass 1 — BOUNDARIES, derived from the FILES

Ownership and register re-derived by parsing every `[^p<page>-<n>]:` definition in the five chunks — **not** read off
the chunks' claims.

### (a) Ownership and contiguity — the decisive test

**Every printed page 535–579 is owned. GAPS = []. Every page's register is contiguous 1..N with no duplicate.** Pages
owned by two chunks: **exactly two, p. 553 and p. 574**, and at each the two owners' numbers concatenate to a contiguous
1..N with no overlap and no hole. **456 numbered entries**, agreeing with `check-vol5-apparatus.py`'s page-by-page report.

| page | entries | | page | entries | | page | entries | | page | entries |
|---|---|---|---|---|---|---|---|---|---|---|
| 535 | 4 | | 547 | 12 | | 559 | 9 | | 571 | 9 |
| 536 | 9 | | 548 | 12 | | 560 | 9 | | 572 | 15 |
| 537 | 8 | | 549 | 11 | | 561 | 8 | | 573 | 15 |
| 538 | 12 | | 550 | 10 | | 562 | 11 | | **574** | **9 (7 + 2)** |
| 539 | 4 | | 551 | 13 | | 563 | 8 | | 575 | 12 |
| 540 | 10 | | 552 | 10 | | 564 | 8 | | 576 | 10 |
| 541 | 12 | | **553** | **3 (2 + 1)** | | 565 | 11 | | 577 | 13 |
| 542 | 13 | | 554 | 6 | | 566 | 6 | | 578 | 11 |
| 543 | 12 | | 555 | 14 | | 567 | 7 | | 579 | 5 |
| 544 | 11 | | 556 | 8 | | 568 | 14 | | | |
| 545 | 13 | | 557 | 11 | | 569 | 13 | | | |
| 546 | 12 | | 558 | 11 | | 570 | 12 | | | |

### (b) The four interior splits, digit for digit

| # | boundary | page | frozen record | derived from the files | verdict |
|---|---|---|---|---|---|
| 1 | `s1` \| `s2` | 539 | **LEAF EDGE** | `s1` ends p. 538 (n. 12); `s2` owns p. 539 nn. 1–4 | ✅ |
| 2 | `s2` \| `s3` | 553 | **SHARED 2/1** | `s2` nn. 1–2; `s3` n. 3 (Sermo III's anchored subtitle note) | ✅ |
| 3 | `s3` \| `s4` | 567 | **LEAF EDGE** | `s3` ends p. 566 (n. 6); `s4` owns p. 567 nn. 1–7 | ✅ |
| 4 | `s4` \| `tract` | 574 | **SHARED 7/2** | `s4` nn. 1–7; `tract` nn. 8–9 | ✅ |

**ALL FOUR MATCH THE FROZEN RECORD DIGIT FOR DIGIT — 2 leaf edges / 2 shared leaves.** ⭐ **p. 574 carries NINE entries**
(the brief's check, after `s4`'s first read stopped at n. 6 and a block-ink profile found n. 7): `s4` defines
`p574-1`…`p574-7`, `tract` defines `p574-8`, `p574-9`, and nothing stands between.

**Runover ledger across the chunk boundaries:** **p. 553 n. 3 is logged by `s3` alone** (`s2`'s ledger line ends at
p. 552 n. 4); **p. 574 nn. 8–9 belong to `tract` alone**, and `tract` logs p. 574 n. 9 as its **page-crossing** runover
into p. 575 (`s4`'s line ends at p. 570 n. 7). **No double-count at any boundary.**

### (c) Grammatical continuity — all four PASS

Every outgoing chunk's Latin closes on a complete sentence ending its unit: `s1` Boethius *…iudicis cuncta cernentis ».
— Exᴘʟɪᴄɪᴛ.* · `s2` *…in saecula saeculorum. Amen. — Exᴘʟɪᴄɪᴛ.* · `s3` *…beatissimae Mariae filius. Amen. — Exᴘʟɪᴄɪᴛ.*
· `s4` *…Quod nobis praestare etc. — Exᴘʟɪᴄɪᴛ.* — and **every incoming chunk opens on its own display heading**:
`### SERMO II.` + subtitle anchored `p539-1` · `### SERMO III.` + subtitle anchored `p553-3` · `### SERMO IV.` (unanchored) ·
`### TRACTATUS` + *de plantatione Paradisi* anchored `p574-8`. **No splice, no stranded fragment, no orphaned heading.** Subtitle
anchors, re-read from the files: **I no · II yes · III yes · IV no · Tract yes.**

### (d) The work's two ends, fixed positively

- **Start p. 535** — `s1` opens at `### SERMO I.` on p. 535. p. 533 = half-title, p. 534 = measured blank (0.0005 %, pilot).
- **End p. 579** — `tract`'s last Latin line is *…in noctibus internarum quietudinum suaviter ac secure pausare possimus.
  Amen.* followed by **`### EXPLICIUNT SERMONES SELECTI.`**, full measure. **p. 580 measured blank (0.0016 %), p. 581 the
  unnumbered volume index** — the end fixed **positively from p. 581**, never from white space (pilot and `tract`, both
  on the plate).

✅ **Pass 1 clean.**

---

## Pass 2 — THE APPARATUS AND THE TEXT

- **`tools/check-vol5-apparatus.py`** (⛔ not `audit-apparatus-count`, which is blind to Vol V): **167 chunks / 4,440
  entries, ALL CHECKS PASSED.** Every page 535–579 `ok` and contiguous; **no PENDING anywhere in the work.** Work total
  **456**, per-page map above.
- **Runover ledger** (`check-vol5-census.py`): **rosters agree 167/167; 298 runovers corpus-wide (269 gutter, 29 page).**
  This work: **25 = 23 gutter + 2 page-crossing** (p. 543 n. 12 `s2`; p. 574 n. 9 `tract`). `s1`, `s3`, `s4` are
  page-crossing-free as each claimed. All five ledger lines are comma-separated (the `bon-qsc-q3` semicolon trap absent).
- **Page markers** `<!-- page N -->`: identical list, identical order, Latin↔English, in all five chunks.
- **Numbered paragraphs**: identical 1..N in both languages in all five (16 · 47 · 42 · 28 · 16 = 149).

### ⛔ THE UNPRINTED / FRAGMENTARY FOOTNOTE-NUMERAL REGISTER — ELEVEN SITES

**No tool can see any of these.** Vol V's raw carries no footnote numerals at all, and `check-vol5-apparatus.py` sees
only the labels the builders wrote. **After Pass 4 deletes the plates, this table is the only record that survives.**
Every site was settled on the plate by **content plus sequence**, never by the blob.

| # | chunk | leaf | note | what the plate shows | settled by |
|---|---|---|---|---|---|
| 1 | `s3` | **p. 558** | n. 4 | **wholly blank** — indented entry between nn. 3 and 5, no superscript at all | sequence + content |
| 2 | `s3` | **p. 560** | n. 4 | fragment | sequence + content |
| 3 | `s3` | **p. 563** | n. 4 | fragment | sequence + content |
| 4 | `s3` | **p. 566** | n. 4 | fragment | sequence + content |
| 5 | `s4` | **p. 570** | n. 7 | top bar + descending stroke, no bowl (8×) | sequence + content |
| 6 | `s4` | **p. 573** | n. 13 | clean `1`, the `3` failed (6×) | sequence + content |
| 7 | `tract` | **p. 576** | n. 4 | fragment / unprinted | sequence + content |
| 8 | `tract` | **p. 576** | **n. 10** | **both digits gone** | sequence + content |
| 9 | `tract` | **p. 577** | n. 4 | fragment / unprinted | sequence + content |
| 10 | `tract` | **p. 578** | n. 4 | fragment / unprinted | sequence + content |
| 11 | `tract` | **p. 579** | n. 4 | fragment / unprinted | sequence + content |

**Leaves affected: 558, 560, 563, 566, 570, 573, 576 (×2), 577, 578, 579 — ten leaves, eleven numerals.** The class in
its CORRECTED form: **any numeral can fail** (`s4` proved it at n. 7 and n. 13; `tract` lost a two-digit n. 10 whole),
**but the `4` sort is eight of eleven.** ▶ **When a register seems to skip a number in this volume, look for an
unnumbered or fragmentary indented entry in the sequence position before concluding a miscount.**

✅ **Pass 2 clean.**

---

## Pass 3 — THE SUITE, EVERY DENOMINATOR READ

All run **after** the gate's documentation edits; every number unchanged from the pre-edit run.

| tool | invocation | result | denominator |
|---|---|---|---|
| live flags | ⛔ **`check-live-flags.py vol5`** (bare positional — `--volume 5` scans ZERO) | **12** occurrences | **167 chunks in vol5** |
| live flags | `check-live-flags.py` (bare) | **239** occurrences | **2,120 chunks, vol1–vol5** |
| apparatus | `check-vol5-apparatus.py` | all passed | 167 chunks / 4,440 entries |
| census/ledger | `check-vol5-census.py` | rosters agree | 167 on disk / 167 in ledger (roster of FIVE present) |
| style scan | `polish-style-scan.py` | **11 issues / 6 chunks — ZERO in `bon-serm-*`** | 2,119 chunks scanned |
| citations | `build-citations.py` | **QA 201**, unchanged | 2,119 chunks / 23,745 records |
| index | `build-index-json.py` | 75 books / 10,982 scripture cites; **1,676 chunks cited / 10,282 backlinks** | whole ledger |
| build | `cd site && node scripts/build-content.mjs` | **14 books, 2,118 questions, 2,118 translated** | — |

**Live flags.** The 239 is the baseline exactly. **This work's share is ONE paragraph, two lines** (`s3` Latin ¶ 9,
English ¶ 9) — the four p. 557 flags, **all expected and all ours**; they moved the corpus count by two, not four,
because the counter counts by line. **`s1`, `s2`, `s4` and `tract` are zero-flag.** The other ten vol5 lines are the
long-standing `bon-brev-p6-c13` / `bon-hex-c15` / `c19` / `c22` flags in already-deployed chunks.

**Style scan.** The 11 issues are the same list every recent gate recorded — `bon-hex-c23` `[V5LABEL]` (deliberate) and
ten `[PAIR]` J4 class-B residue in `III-d31-a3-q3`, `III-d32-a1-q2`, `III-d5-a2-q4`, `IV-d14-p2-a2-q1`,
`IV-d16-p2-a2-q2`. **Pre-existing, Vols III–IV + `bon-hex-c23`, deliberately NOT fixed — out of scope.**

**Citations — this work's own ledger: 487 records** from `bon-serm-*`, resolving **verse 310 · chunk 86 · chapter 57 ·
work 24 · page-multi 3 · distinctio 3 · articulus 2 · excluded 2.** **ZERO dangling · ZERO unresolvable · ZERO
ambiguous · ZERO QA flags of ours** (the QA report has not one `bon-serm-` line).

⭐ **NO FORWARD REFERENCE INTO pp. 535–579 REMAINS ANYWHERE IN THE CORPUS.** The ten corpus-wide `forward` records point
at `tom5:p1`, `tom5:p199`, `tom5:p209`, `tom5:p671`, `tom9:p689`, `tom11:p745` and `bon-sci-q4`; **no `tom5:p5xx`
target exists at all.** The last one that did (`tom5:p543`) now resolves — **wrongly** (docket 1).

**The named-work references to *de plantatione paradisi*, checked:**
- `bon-hex-c17` p. 410 n. 1 *in* ***opusculo de plantatione paradisi*** *in anima multa conveniunt cum seqq.* — **produces
  NO ledger record.**
- ⚠ **The second reference is in `bon-hex-scholion`, NOT `bon-don-c1`** as the brief and the resume carried it:
  *repetitur in* ***sermone de Plantatione paradisi infra impresso***. `bon-don-c1` contains no such phrase (whole-file
  search). The `bon-hex-scholion` reference **produces NO ledger record** either.
- **Both name `bon-serm-tract`, which is built — and the resolver is silent on both.** Docket 2.

**Inbound:** exactly **one** record anywhere in the corpus targets a `bon-serm-*` chunk, and it is the wrong one
(docket 1).

✅ **Pass 3 clean** (no defect of ours; docket items are resolver lines, not text).

---

## THE DOCKET — recorded, NOT fixed (QA lines for the resolver; no gate edits)

1. **`bon-hex-scholion` `pag. 543-555` → `bon-serm-s2` (`chunk`) — WRONG.** The printed text is *Denifle… in suo praeclaro
   Chartulario Universitatis Parisiensis pag. 543-555* — Denifle's *Chartularium*, not our tome. The bare-`pag. N`
   tome-inheritance artefact in its most damaging form: **it was a harmless `forward` until `s2` was built, and now it
   looks resolved.** ▶ **Members of the same class on this work's span** (from the chunks' Notes): `s4` p. 569 n. 8
   `Vide etiam supra pag. 314, col. II. seqq.` (a column qualifier nothing parses) · `s4` p. 571 n. 8 `supra p. 58` (bare
   `p. N`) · `tract` p. 577 n. 3 `Cfr. tom. I. pag. 2, nota 8` (**tome-qualified** — the one form that would let a
   resolver disambiguate, and nothing reads it).
2. ⭐ **Named-work references to chunks we HOLD are not parsed** — `bon-hex-c17` p. 410 n. 1 (*in opusculo de
   plantatione paradisi*) and **`bon-hex-scholion`** (*sermone de Plantatione paradisi infra impresso*) both name
   `bon-serm-tract`, now built. **The only resolver class that is silent about a target that certainly exists, is
   certainly named and is certainly built.** Same class as the *perfectione* gate's docket 2 (`p198-nota`'s
   *Breviloquium* / *Hexaëmeron* references). Highest-value resolver item on the docket.
3. **`s3`'s four p. 557 `[?]` flags — a MEASURED LIMIT OF THE WITNESS, not a defect.** p. 557 ¶ 9: *et* ***talis[?]***
   *non detur admittentibus alienam consolationem, ut* ***dicit[?]*** *Bernardus: ideo necesse est, ut qui vult*
   ***attingere[?]*** *consolationem spiritualem dimittat* ***delectationem[?]*** *carnalem.* A scan dropout: five lines,
   4–6 characters wide, blank even on aggressive stretch. ⛔ **Not resolvable from the raw** (same scan, same gaps), and
   no other chunk in the corpus quotes the passage. Each word is restored from sense and flagged in both languages.
   ⚠ **The one genuinely doubtful reading is *delectationem*: the surviving letters on the plate read `delectaction`**,
   which is not a Latin form. **Clears only against a second copy of the edition.**

---

## Pass 4 — PLATE DELETION: ✅ DONE (run last, after Passes 1–3 were clean)

| what | files | size |
|---|---|---|
| `raw/vision/vol5/*.png` (pp. 533–581) | **49** | **152 MB** |
| `/tmp/colcrop/*` (vol5 pp. 535–581 bands + this work's ad-hoc crops) | **238** | **469 MB** |
| **total** | **287** | **~621 MB** |

Both gitignored (`.gitignore:9  raw/vision/`) and **fully regenerable from the PDF** via
`tools/extract-pages.py --volume vol5` + `tools/colcrop.py vol5 <page>`. **The largest reclaim of any Vol V gate**
(*perfectione* ~420 MB).

### ⛔⛔ THE p. 535 WARNING — REPEATED HERE BECAUSE THE EVIDENCE IS NOW GONE FROM DISK

**The archive scan of p. 535 is MIRROR-REVERSED**, and its djvu OCR (raw L86902–87020) is reversed-letter garbage.
The copy that was on disk was the `ImageOps.mirror()`-restored leaf. **That copy is now deleted. Any re-extraction of
p. 535 — `extract-pages.py --volume vol5 --pages 535`, with or without `--force` — brings the MIRROR back.**
**Whoever re-extracts p. 535 must flip it with `PIL.ImageOps.mirror()` BEFORE reading a word.** After this deletion
the flip is no longer on disk to be seen; this sentence and `s1`'s `transcription_status` are the only warnings left.
Only p. 535 is affected (checked from p. 536 on by numerals and running heads).

---

## ▶ THE DEPLOY-BATCH CARRY-LIST (inherited from the *perfectione* gate + this gate; deploy-only, batched)

1. **`tr-vacare` notes owed at the two DEPLOYED *vacatio* sites** — `bon-praec-c4` and `bon-qmt-q7-a2`. Still not done.
2. **The *lumen* ruling's owed translator's note** at the first *lumen* in `bon-qsc-q3` / `bon-qsc-q4`, the `bon-qmt`
   chunks, and **`bon-qpe-q4-a3` p. 195** (the Cyprian sentence). *(The five Sermones chunks already carry theirs.)*
3. **`bon-sci-` → `bon-qsc-`** slug fix in `tools/scripture-books.json` — one line; clears `bon-don-c8`'s false forward
   (still visible in this gate's forward list).
4. **The resolver docket** above (items 1–2), plus the *perfectione* gate's open resolver items (cross-note `ibid.`
   anaphora; verbal back-references; bare-`pag. N` false hits inbound to `bon-qpe-*`).
5. **Correct the standing claim that *quies* is wholly absent from the *Sermones*** — `tract`'s Summarium has one noun
   site (*in paradisi quiete* → "rest"). The *vacatio*/*quies* pair itself is still untested here (`vaca-` ZERO).
6. ⚠ `cited-by.tsx` `MAX_SHOWN = 25` — existing design, listed only so it is not re-discovered as a regression.

---

## The gate's own finding

⭐⭐ **THE SERMONES SELECTI IS CLOSED, AND WITH IT VOLUME V.** Ten works, pp. 3–579, every page owned.

⭐ **For the third gate running, a work ruled before it was built arrived with nothing to repair in the text.** The
*scientia Christi* gate repaired a five-way rendering; the *mysterio* gate an unrecorded *lumen* and a resolver bug; the
*perfectione* gate one punctuation mark in a gloss; **this gate repaired no rendered line at all.**

⛔ **What it did repair is the same thing the last gate warned about, one level up: claims about the whole work written
by a chunk that had measured only its part.** Four of them, in two chunks, all saying "five of five" — and one of them
explicitly **closed the question so the gate would not re-open it**. And the two census slips it found run in opposite
directions — ruling 6's *puritas* count was **low** (the sheet found the variant and missed the body noun), where the
*perfectione* ruling-3 count ran **high** — but they are one rule: **a census is taken over the whole live region, body
and apparatus, and the denominator is written beside the number.**

▶ **For Vols VI–X:** a chunk's `## Notes` may state what it measured; **a sentence about the whole work belongs to the
gate**, and any such sentence in a chunk should be treated by the next gate as a claim to re-derive, not a finding.

## Status

**Committed locally. ⛔ NOT PUSHED. ⛔ NOT DEPLOYED.** Both are Wilson's hard stops, given separately. `build-citations.py`
and `build-index-json.py` have **both been run**, in that order, so the deploy recipe can start at
`cd site && node scripts/build-content.mjs`. ⚠ Live-state claims in this log are DATED 2026-09-19 and expire.
