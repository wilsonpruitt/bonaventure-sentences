# Vol VI — *Commentarius in librum Sapientiae*, SHAKEDOWN GATE at p. 125 (ruling 34): EVIDENCE SHEET

Compiled 2026-10-15 by a read-only agent on Wilson's go. **Nothing here is settled. Wilson rules off this sheet.**
No chunk, tool, resume note or ledger was edited; no commit, push, deploy or stash. `build-citations.py` was run into the
scratchpad (`--out`/`--qa`), and its ledger came out **byte-identical** to the tracked `index/citations.tsv`.

## ▶ ONE-SCREEN SUMMARY

| # | item | recommendation | text lines it would change |
|---|---|---|---|
| 1 | `title_la` rule for a capitulum chunk | **RATIFY c1/c2's rule, written as a procedure:** take the first heading below `Capitulum N.`; if it governs more than this chapter, go down to the heading that governs exactly this chapter; if nothing stands below, take the heading above that governs exactly this chapter | **0** |
| 2 | c1 p. 115 n. 6 `Iob 6, 2` (body = Job 6:25) | Latin as printed (ruling 9). **Add `[so printed; the verse is Job 6:25]` in the En. half** (the `bon-qpe-q4-a1` p. 182 n. 6 precedent). No `[?]`. Ledger left to the resolver docket | **1** (c1 En) |
| 3 | c2 p. 121 n. 3 `de Doctr. christ. c. 3. n. 4` (true locus I.4.4) | Same as 2: **En. bracket `[so printed; the passage is c. 4, n. 4]`** | **1** (c2 En) |
| 4 | marginal `Quaestio.` density (c1 **9**, c2 **4** by marginale count) | **Keep ruling 31.** No visible marker, no `### Quaestiones`. Optional: a standard `### Marginal quaestiones` table in each chunk's Notes from c3 on (Notes are not rendered) | **0** |
| 5 | stray `ibid. 37, 20` → crossref to p. 118 | **Record as ruling-14 artefact "2c"** on the resolver docket (it also drops Gen 37:20 from the scripture index). No text edit | **0** |
| 6a | ⚠ **DEFECT: c2 English leaves `**Contra:**` untranslated** (pp. 123, 125) against c1's "On the contrary:" and c2's own Notes | **Conform to "On the contrary:"** | **2** (c2 En) |
| 6b | c2 p. 122 *malorum* → "wicked men" (ruling 32 gives "wicked" to *iniquus*) | Optional: → "evil men" | 0 or 1 |
| 6c | c2 Sap 5:6 "hath not shone" vs Eccl's "hath not shined" (same verse, `bon-eccl-c6-v1-7`, `-c12-v1-14`) | Optional: conform to "shined" | 0 or 1 |
| 6d | c1 Vers. 16 under index label `"1-15"` | Keep (ruling 27 verbatim label; ruling 15 cost) | **0** |
| 6e | c2 heading face (`Secundo, de iustitia…` roman, not italic as c1's brief said) | Record only; already rendered correctly | **0** |
| 6f | all other ruling-32 / carried register items | Applied consistently across the four chunks (census below) | **0** |
| — | **OUT OF SCOPE, for Wilson's notice:** deployed Ecclesiastes English carries `**Contra:**` ×14 (c1–c4 chunks) and `**Sed contra:**` ×2 (`bon-eccl-prooem`) untranslated, while `c3-v1` and c5 onward use "On the contrary:" ×30 | A separate scoped decision, not this gate's | (16, deployed) |

**Minimum if every recommendation is taken: 4 English lines (2 of them a defect repair). Maximum: 6.** No Latin line changes.

---

## ▶ SCOPE (derived from `ls vol6/bon-sap-*` + frontmatter)

| chunk | div / sec | type | printed_pages | entries | `tr-` notes |
|---|---|---|---|---|---|
| `bon-sap-prooem` | 0 / 1 | prooemium | 107–109 | 22 | lumen · studium · vacare · doctrina |
| `bon-sap-prol` | 0 / 2 | expositio | 109–110 | 4 | — |
| `bon-sap-c1` | 1 / 1 | pericope `"1-15"` | 110–118 | 83 | studium · doctrina |
| `bon-sap-c2` | 2 / 1 | pericope `"1-25"` | 118–125 | 64 | vacare · lumen |
| **total** | | | **107–125, 19 pp.** | **173** | 8 |

⛔ Every census below is over the BUILT files and the RENDERED regions only (`## Latin`, `## English`, `## Apparatus`; frontmatter and `## Notes` stripped). Extracts and scripts: scratchpad `r/`, `sweep.py`, `census.py` (not in the repo).

---

## ▶ A. MECHANICAL PASSES, WITH DENOMINATORS

| pass | what it COUNTED | verdict |
|---|---|---|
| 1 `python3.11 tools/check-live-flags.py vol6` | **49 vol6 chunks** | **no live `[?]`** |
| 2 `python3.11 tools/polish-style-scan.py` | **2,168 chunks, vol1–vol6 in scope** | 11 issues / 6 chunks (10 PAIR Vols III–IV, 1 V5LABEL `bon-hex-c23`) — **ZERO in vol6** |
| apparatus `check-vol5-apparatus.py --volume=vol6` | **49 chunks, 1,020 entries, 117 known page totals**; sap chunks La = En: prooem 22 · prol 4 · c1 83 · c2 64 | **All checks passed**; p. 125 `PENDING n.4–11` (c3's, correctly unwritten) |
| census `check-vol5-census.py` | vol5 167/167 · **vol6 49/49**; vol6 57 runovers (56 gutter, 1 page) | **Rosters agree.** In scope: 9 runovers, all gutter — p.108 n.4 (prooem) · p.109 n.6 (prol) · p.110 n.3, p.113 n.5, p.114 n.4, p.115 n.7, p.116 n.7, p.117 n.5 (c1) · p.119 n.3 (c2) |
| `build-citations.py` (to scratchpad) | **2,168 chunks → 25,957 records**; ours **384** (prooem 34 · prol 0 · c1 173 · c2 177) | corpus QA **208**; **ZERO QA flags attributable to the four chunks** (the only `bon-sap` line in the QA report is `bon-sap-prol` under "chunks contributing no citation record" — informational; its 4 notes are Jerome/Isidore/*de Viris ill.* and an intra-work `Supra n. 5. 6.`). Ours: scripture A 178 · B 69 · C 106; crossref 31 (25 chunk, 6 page-multi), zero dangling/unresolvable/ambiguous |
| La/En Arabic-digit multiset, every apparatus entry | **173 entries** (22 + 4 + 83 + 64; `tr-` excluded) | **2 mismatches, both KNOWN FALSE POSITIVES** (number words): c2 p. 120 n. 2 *Sum. tertia* → "Summa 3"; c2 p. 121 n. 3 *83 Qq.* → "*Eighty-three Questions*" |
| page markers La vs En, per chunk | 3 · 2 · 9 · 8 markers | **identical lists, identical order, all four** |
| anchor order La vs En | 22 · 4 · 83 · 64 anchors | **identical sequence, all four**; no duplicates; `tr-` anchors English-only |
| site build | — | **not run** (the brief forbade touching anything; `content.json` is regenerable — run at the gate's close) |

---

## ▶ B. PASS 3 — BOUNDARY SWEEP (from the built files)

**Every printed page 107–125 owned exactly once; every register contiguous 1..N; `KNOWN_TOTALS_VOL6` matches on all 19.**

| page | total | split by chunk | seam |
|---|---|---|---|
| 107 | 10 | prooem 1–10 | **open**: prooem starts on the `### Prooemium…` display heading |
| 108 | 7 | prooem 1–7 | |
| **109** | 8 | prooem 1–5 / prol 6–8 | prooem ends *…ad studium et amorem sapientiae.* (complete); prol opens on `### Prologus S. Hieronymi…` heading |
| **110** | 7 | prol 1 / c1 2–7 | prol ends *…evidenter, id est diligenter, exprimitur.* (complete); c1 opens on `### Commentarius in librum Sapientiae.` |
| 111–117 | 11·10·11·8·8·14·12 | c1 alone | |
| **118** | 8 | c1 1–3 / c2 4–8 | c1 ends *…postremo mors impoenitentiae finalis.* (complete); c2 opens on `### Capitulum II.` |
| 119–124 | 7·9·10·9·11·10 | c2 alone | |
| **125** | 11 | c2 1–3 / (c3 4–11 PENDING) | c2 ends *…ut dicit Gregorius*³. (complete) |

Hand-offs consistent at every seam (prooem → prol nn. 6–8; prol → c1 nn. 2–7; c1 → c2 nn. 4–8; c2 → c3 nn. 4–11), each runover ledgered once, by the chunk that owns it. **No tail is ungrammatical, every incoming body opens on a printed heading, so no seam needed a plate.** Verdict: **CLEAN.**

---

## ▶ C. THE DOCKET

### (1) `title_la` — the rule c1/c2 used

**Sites:** c1 `title_la` = *Primo, de triplici iustitia hominis quoad Deum* (heading ABOVE `Capitulum I.`); c2 = *Primo retrahit ab iniustorum similitudine notando tria* (the SECOND heading below `Capitulum II.`).

**Decisive sentences.**
- c2's first heading governs two chapters, by its own divisio: *et primo, ab iniustorum similitudine retrahendo, scilicet **capitulo isto**; secundo, ad iustorum similitudinem provocando, scilicet **tertio capitulo*** — "namely in this chapter … namely in the third chapter."
- c1: `Capitulum I.` is followed directly by *(Vers. 1.). Dicit ergo: Diligite etc.* — nothing below it, so ruling 17 would give a lemma-pointer.

**What the next 17 chapters meet (raw, the 12 surviving `Capitulum N.` lines):** a class-3 heading stands directly below the capitulum line in **11 of 12** (all but I). Of those, some govern exactly the chapter — **V** *Secundo comparatur status iustorum statui iniustorum in ipso iudicio quoad tria* (L23479), **VII** *Secundo sumit rationem exhortandi ad sapientiam a suo exemplo*, **VIII**, **XII**, **XIV**, **XV**, **XVII** — and some govern a RUN of chapters, as c2's did: **XIII** *Secundo, de punitione per poenas graviores…* (its divisio: *primo… usque ad decimum sextum capitulum; secundo… a decimo sexto capitulo et deinceps*, L31742), **XVI** *Secundo determinatur de supplicio poenae culpabilium* (XVI–XIX), **XVIII** *Secundo de poenis inferentibus mortem* (*primo… capitulo isto; secundo…*, XVIII–XIX). **So c2's shape will recur at least three times.**

| option | c1 title | c2 title | cost |
|---|---|---|---|
| **(a) RATIFY c1/c2 as a procedure** (first heading below; descend if it governs a run; heading above if none below) | unchanged | unchanged | per-site reading of each divisio (the builder already reads it); XIII/XVI/XVIII take the next heading down |
| (b) first heading below the capitulum line, always (`bon-eccl-c1-v1` literal) | none below → ruling 17 → *Dicit ergo: Diligite etc.* (a lemma-pointer) | *Secundo, de iustitia hominis ad proximum agitur dupliciter* (reads as a title for cc. II–III) | 4 frontmatter lines; c2 and c3 would both carry "Secundo…" titles naming two-chapter units |
| (c) ruling 17 everywhere (divisio's first sentence after the lemma) | lemma-pointer | *Supra egit de iustitia hominis ad Deum; hic principaliter…* | 4 frontmatter lines; discards printed headings that exist |

Mechanical vs per-site: **per-site** under every option (the "governs exactly" test needs the divisio). **RECOMMENDATION: (a).** It is what the Ecclesiastes precedents already did (`c5-v1-8` took Art. 1 rather than the membrum above it; `c12-v1-14` likewise). 0 lines.

### (2) c1 p. 115 n. 6 `Iob 6, 2` vs the body's Job 6:25 — **CONFIRMED ON THE PLATE**

Plate p. 115, left register, 4×: **`Vers. 10. — Sequitur Iob 6, 2.`** — clean `2`, point immediately after, no room for a `5`. Body (p. 115 R): *Iob sexto: « Quare detraxistis sermonibus veritatis »* = Job 6:25 (Vulgate). English: *V. 10. — There follows Job 6:2.*

**Ledger:** `bon-sap-c1 apparatus:p115-6 Iob 6, 2 → Iob 6:2, confidence A, verse` — a wrong verse filed at the top confidence tier; in range, so the out-of-range channel cannot see it.

**How earlier works disposed Quaracchi verse slips (both kept the Latin as printed; the English differs):**
- `bon-qpe-q2-a1` (×3: p. 126 n. 4 `Matth. 19, 15`, p. 132 n. 1, p. 133 n. 2) — English **bare**, slip recorded in Notes only.
- `bon-qpe-q4-a1` p. 182 n. 6 `Iob 24, 5` for 26:5 — English **"Job 24:5 [so printed; the verse is Job 26:5]"**.

| option | cost |
|---|---|
| (a) leave as built (Notes only) | reader of the site sees a wrong verse unflagged; ledger wrong at A |
| **(b) En. bracket, the q4-a1 form** | 1 English line; Latin untouched (ruling 9); ledger still says 6:2 (it reads Latin only) |
| (c) `[?]` | refused — a `[?]` marks an uncertain READING; this reading is certain; it would also raise the live-flag count |
| (d) hand-fix the ledger | refused — the ledger is derived, never hand-tagged |

Per-site. **RECOMMENDATION: (b)**, and adopt the q4-a1 form as the Vol VI rule for any certain Quaracchi slip. Ledger record → resolver docket (an override list of known printed slips would be its own scoped job). **1 line.** ⚠ The three `bon-qpe-q2-a1` bare sites are the inconsistency in the deployed corpus; not this gate's.

### (3) c2 p. 121 n. 3 `I. de Doctr. christ. c. 3. n. 4` — **CONFIRMED ON THE PLATE**

Plate p. 121, left register, 3×: **`de Doctr. christ. c. 3. n. 4: Frui enim est etc.`** — clean `3`. **True locus: *De doctrina christiana* I, c. 4, n. 4** (*Frui enim est amore alicui rei inhaerere propter seipsam*); in the Maurist numbering n. 4 falls in c. 4, so the printed `c. 3. n. 4` is internally inconsistent. Corpus control: `bon-sent-III-d27-a1-q1` prints `I. de Doctr. christ. c. 4. n. 4.` for the same testimony; `c. 3. n. 4` occurs nowhere else in the corpus. Not in the ledger (an Augustine locus is an authority, excluded), so no index harm.

Options as in (2). **RECOMMENDATION: (b), En. bracket `[so printed; the passage is c. 4, n. 4]`. 1 line.**

### (4) Ruling 31 — the marginal `Quaestio.` density

**Count by MARGINALE, from the chunks' own marginalia lists (live region):** c1 **9** (p. 112 R `Quaestio 1.`, `2.` · p. 116 L `1.`, `2.` · p. 116 R `Quaestio.` · p. 116 R `1.`, `2`, `3.` · p. 117 L `Quaestio.`), c2 **4** (p. 120 L `1.`, p. 120 R `2.`, p. 123 L, p. 125 R). **13 in pp. 110–125**, against the pilot's ~5 for 129 pp. ⚠ c1's Notes heading and the resume note say "seven" for c1 — that figure matches neither the marginale count (9) nor the cluster count (5); a documentation discrepancy, no text affected. The raw saw ~1 of these 13 (it splices the marginalia), so the pilot's other four raw sites (L27296, L27910 Cap. VIII; L32876 XIV; L35800 XVII) are a floor.

**Decisive sentence (how such a paragraph reads without its marginale):** *Sed **obiicitur**, quod, secundum Augustinum, omnes appetunt vitam et beatitudinem: ergo nullus mortem vel perditionem.* / *Dicendum, quod verum est per se…* (c1 p. 116) — the objection and reply announce themselves; five of the thirteen open on a printed small-cap `Cᴏɴᴛʀᴀ:`/`Sᴇᴅ ᴄᴏɴᴛʀᴀ:`.

| option | cost |
|---|---|
| **(a) keep ruling 31** (ordinary paragraphs; marginale in Notes) | none; the reader loses the editors' "Quaestio" label, which the text's own *obiicitur…Dicendum* replaces |
| (b) visible run-in marker (e.g. `*Quaestio 1.*`) | sets editorial marginalia into the body, against the corpus-wide trim-to-Notes convention (Vols V–VI); ~2 lines per site, 26 now, ~100+ by the close |
| (c) lift to `### Quaestiones` | refused by ruling 31 itself; these are not a separate printed series (contrast Ecclesiastes' `QUAESTIONES.` heading) |
| (d) Notes convention: a `### Marginal quaestiones` table (page, column, marginale, incipit) | Notes only, unrendered; makes the count derivable for the p. 192/235 gates |

**RECOMMENDATION: (a), plus (d) from `bon-sap-c3` on** (retrofitting c1/c2 optional — their marginalia lists already carry it). **0 text lines.** Density does not argue for a change: it changes how often the convention applies, not what it hides.

### (5) The stray `ibid.` filed as a cross-reference to p. 118

c2 p. 121 n. 2: **La.** `Vers. 4; ibid. 37, 20. est seq. locus; tertius est Prov. 1, 11.` — the body anchor is *Genesis undecimo* (Gen 11:4, tier B), so `ibid. 37, 20` is **Genesis 37:20** (*Venite, occidamus eum*).
Ledger: `bon-sap-c2 apparatus:p121-2 crossref anaphor->page ibid. → bon-sap-c1+bon-sap-c2 page-multi, antecedent "pag. 118"` (taken from p. 120 n. 9). **Two effects: a phantom self-reference (shows in the page-level "Cited by" line of c1 and c2), and Gen 37:20 is absent from the scripture index** (the note's only other records are Gen 11:4 B and Prov 1:11 A).

**Characterisation:** ruling-14's missing rule (*an apparatus note's `ibid.` takes its antecedent from WITHIN the note*), in a NEW shape — the in-note antecedent is a bare `Vers. 4` whose book exists only through the body-ordinal join. Call it **artefact 2c**: cross-note anaphora, wrong target, *and* a lost record. Mechanical (resolver). **RECOMMENDATION: add to the ruling-14 docket, unscheduled; no text edit. 0 lines.**

Other resolver artefacts in scope, same docket: c1 p. 116 n. 2 `III. Sent. d. 38. q. 5. et 6.` → q5 only (`bon-sent-III-d38-a1-q6` exists; the `et N` sibling is never emitted — 0 such records corpus-wide); prooem p. 108 n. 7 `[I: Cor. 12, 8.]` (printed colon) → unnumbered bucket `Cor* 12:8` instead of I Cor; prol p. 109 n. 8 `Supra n. 5. 6.` (intra-work paragraph reference) unparsed. Checked and RIGHT: prooem p. 108 n. 4 `In nota ibid. adiecta` → `bon-hex-c6` (the note on that page).

### (6) Everything else banked, plus the register census

**(6a) ⚠ DEFECT — c2's English leaves the small-cap `Cᴏɴᴛʀᴀ:` label untranslated, twice.**

| chunk | site | Latin | English as built | c1 / house form |
|---|---|---|---|---|
| c2 | p. 123 Quaestio | `**Contra:** ad Hebraeos secundo` | `**Contra:** to the Hebrews, the second` | "**On the contrary:**" |
| c2 | p. 125 Quaestio | `**Contra:** ad Romanos quinto` | `**Contra:** to the Romans, the fifth` | "**On the contrary:**" |
| c1 | p. 116 ×2 / p. 116 | `**Sed contra:**` ×2 / `**Contra:**` | "**But on the contrary:**" ×2 / "**On the contrary:**" | — |

c2's own Notes say *"`Cᴏɴᴛʀᴀ:` → `**Contra:**` ("On the contrary:", c1's house form)"* — the claim is not what the English does. The resume's register brief to c2 named the same rule; the repo CLAUDE.md formula table gives *Sed contra / Contra → "On the contrary"*. Mechanical. **RECOMMENDATION: conform both to "On the contrary:". 2 lines.**
⚠ **Out of scope, for notice:** deployed Ecclesiastes is split the same way — English `**Contra:**` ×14 in `c1-v2-7`, `c1-v8-11`, `c1-v12-15`, `c2-v1-3`, `c2-v4-10`, `c2-v11-17`, `c4-v1-6`, `c4-v7-12`; `**Sed contra:**` ×2 in `bon-eccl-prooem`; "On the contrary:" ×30 in `c3-v1` and from `c5-v1-8` on. A 16-line cleanup in a deployed work, its own decision.

**(6b)** c2 p. 122 *vox quorumlibet **malorum** contra quemlibet iustum* → "the voice of any **wicked** men whatever". Ruling 32 assigns "wicked" to *iniquus* (c1 ×4, c2 ×1 — Gregory's *iniquorum*). One site; *malus* elsewhere → "evil". Optional → "evil men". 0 or 1 line.

**(6c)** c2 p. 124 Sap 5:6 *iustitiae lumen non luxit nobis* → "…and the lumen of justice **hath not shone** unto us"; `bon-eccl-c6-v1-7` and `bon-eccl-c12-v1-14` give "**hath not shined**" (Douay). Optional conform. 0 or 1 line. (c2's Notes cite c12 as the precedent; c6-v1-7 carries it too.)

**(6d)** c1 Vers. 16 expounded under `verses: "1-15"` — keep (ruling 27; ruling 15's accepted breadcrumb cost). c2's `"1-25"` is exact. 0 lines.

**(6e)** `Secundo, de iustitia hominis ad proximum…` is ROMAN on the plate (c1's brief said italic); c2 renders it plain `####` and the italic `Primo retrahit…` as italic `####`. Already right. 0 lines.

**(6f) Register census** (Latin body/apparatus · English body/apparatus; rendered regions):

| term | prooem | prol | c1 | c2 | verdict |
|---|---|---|---|---|---|
| *Sapientia* cap / lc → Wisdom / wisdom | 11+6 / 40+8 → 10+10 / 41+9 | 11+5 → 11+5 | 1+1 / 16+3 → 1+1 / 20+3 | 0 / 0+1 → 0 / 0+1 | follows the print; paragraph-aligned differences are elided-noun expansions or sentence-initial capitals inside quotations (e.g. *Trahitur sapientia* → "*Wisdom* is drawn"); no case divergence |
| *Sapiens* author / generic | 1 / 2 → "the Wise Man" 1 / "wise man" 1 (+ *sapientissimus* → "the wisest") | — | — | — | ✓ |
| *impi-* → impious/impiety | 0 | 0 | 8+1 → 12+1 | 7+1 → 8+2 | ✓ (excess = expansions) |
| *iniqu-* → wicked / iniquity | 0 | 0 | 9 → wicked 4, iniquity rest | 2+1 → wicked 1+1 | ✓ (+6b) |
| *iust-* → just/justice | 0 | 0 | 38+6 → 46+6 | 35+1 → 35+1 | ✓ |
| *idol-*, *simulacr-* | 0 | 0 | 0 | 0 | not reached |
| *lumen* / `tr-lumen` | 7 / ✓ | 0 | 0 / none owed | 1 (Sap 5:6) / ✓ | ✓ one note per chunk carrying the word |
| *lux* → light | 1 | 0 | 1 | 3 | ✓ |
| *poena* / *supplicium* / *poenalitas* | 0/0/0 | — | 19 / 5 / 0 → punishment | 5 / 1+1 / 1 → punishment / penalty | ✓ ruling 20 |
| *vaca-* / `tr-vacare` | 2 (*ab*) / ✓ | 0 | 0 | 1 (dative) / ✓ | ✓; never "rest" |
| *quies* / *requies* → rest | 0 | 0 | 0 (verbs only) | 1+1 / 2 → rest | ✓ pair kept apart |
| *magister* / *doctor* | 0 / 0 (Lombard *lit. Magistri* → "the Master's text" in app.) | 0 | 0 / 0+2 (→ "the learned") | 0 | ✓ |
| *doctrina* / `tr-doctrina` | 1 → teaching / ✓ | 0 | 1 → teaching / ✓ | 0 | ✓ |
| *studium* / `tr-studium` | 4+1 → study/studious / ✓ | 0 | 1 / ✓ | 0 | ✓ |
| purity triple | 0 | 0 | *pudica* (adj.) → Douay "chaste" | *immunditia* → uncleanness | not reached as nouns |
| *intellect-* / bare "intellect" | 0 / 0 | 0 | 5+1 → understanding / **0** | 1 → understanding / **0** | ✓ |
| *intelligentia* | 4 → intelligence 3; Job 32:8 → Douay "understanding" | 0 | 1+1 → intelligence | 0 | ✓ (quotation branch) |
| *fundam.* (apparatus) | 0 | 0 | 0 | 0 | ruling 5 not reached |

Other c2 choices banked by the builders (*circumvenire* "circumvent", *traductio* "exposure", *inexterminabilis*, *refrigerium* "refreshment", *nugaces* "triflers") are single-chunk and collide with nothing in c1/prooem. **No other divergence found.**

---

## ▶ D. PASS 4 (NOT this agent's) — what it would delete

| set | files | size |
|---|---|---|
| `raw/vision/vol6/p-107.png` … `p-124.png` (gate scope) | 18 | ~48 MB |
| `raw/vision/vol6/p-125.png` | 1 | ~3 MB — ⚠ **c3 opens on p. 125 and reads it FIRST; keep it, or re-extract for c3** |
| `raw/vision/vol6/p-001.png` … `p-106.png` (Ecclesiastes leftovers still on disk) | 106 | ~206 MB |
| pilot extras `idx-677…680`, `p-235…239`, `p-531…535`, `p-634` | 15 | ~12 MB |
| `/tmp/colcrop/*` (147 of 231 files carry a 107–125 page tag) | 231 | ~148 MB |
| **total** | **371** | **~417 MB** (~414 MB if p. 125 is kept) |

All gitignored and regenerable (`tools/extract-pages.py --volume vol6`, `tools/colcrop.py vol6`).
