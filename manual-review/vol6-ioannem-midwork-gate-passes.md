# Vol VI *Ioannem* MID-WORK GATE (p. 371, ruling 76): passes 1–3 (read-only agent, 2026-10-27)

Run on Wilson's go (2026-10-27). No file under `vol*/` was edited; no tool, ledger, registry or resume note was touched; nothing
pushed, deployed or stashed; no plate deleted (pass 4 is not part of this run). The docket is in the separate
`manual-review/vol6-ioannem-midwork-gate-evidence-sheet.md`; findings that are register questions are there, not repeated here.

**Scope: 40 chunks, `bon-ioan-c2-v1-11` … `bon-ioan-c8-v51-59`, pp. 269–372** (p. 269 nn. 2–13 after `c1-v43-51`'s n. 1; p. 372 nn. 1–5,
nn. 6–12 pending for Cap. IX). **1,244 numbered entries + 1 unnumbered closing note `[^p357-nota]` = 1,245 defs**, + **35 `tr-` notes**
(`tr-doctrina` 24 · `tr-lumen` 8 · `tr-vacare` 3). Per chunk: c2 55/36/23 · c3 18/36/15/15/22/31 · c4 30/24/36/37/43 · c5 35/27/24/35/30/22 ·
c6 28/24/24/42/23/31/43/31 · c7 38/27/24/22/30/33 · c8 48/39 (38 + nota)/32/26/51/35. The total equals KNOWN_TOTALS pp. 270–371 (1,227)
+ p. 269 nn. 2–13 (12) + p. 372 nn. 1–5 (5) = 1,244, re-derived independently of the checker.

---

## PASS 1: live flags. **CLEAN**

`python3.11 tools/check-live-flags.py vol6` → **scanned 121 chunks in vol6; LIVE [?] FLAGS: none — checked, not assumed.**
Denominator 121 = all of vol6, the 40 in scope included.

## PASS 2: mechanical suite. **CLEAN on every tool; one convention DEFECT class found by census (→ docket § 1)**

| tool | denominator / result | verdict |
|---|---|---|
| `check-vol5-apparatus.py --volume=vol6` | header `volume: vol6 (121 chunks, 359 known page totals)`; **121 chunks, 3,784 entries, all checks passed**; in scope 40 chunks / **1,245** entries, La = En in every chunk; p. 372 `1-5 ok PENDING n.6–12` | CLEAN |
| `check-vol5-census.py` | **vol6 121 on disk / 121 in ledger; 169 runovers (162 gutter / 7 page), 92 positive / 29 negative**; "Rosters agree" | CLEAN |
| ↳ in scope | **45 runovers (42 gutter / 3 page) in 31 positive chunks; 9 negative** (`c4-v43-54`, `c5-v10-18`, `c5-v24-30`, `c5-v31-39`, `c5-v40-47`, `c6-v10-13`, `c6-v34-40`, `c7-v19-24`, `c7-v25-31`) | see Pass 3 |
| `polish-style-scan.py` | **11 issues / 6 chunks / 2,240 scanned** (`bon-hex-c23` V5LABEL + five Vol III–IV PAIR chunks); **0 in `bon-ioan-*`** — the shakedown baseline unchanged | CLEAN |
| `build-citations.py --out/--qa` (scratchpad) | **30,584 records, QA 210**; ledger **byte-identical** to `index/citations.tsv`; QA report byte-identical to `manual-review/citation-qa-report.md`; anaphora unresolved 277; coordinate ibid. 419 (honoured 320 / unresolvable 99); printed slips 6 | CLEAN |
| ↳ **attributable to this scope** | **1,474 records** (scripture 1,268: A 658 · B 357 · C 253; crossref 204: chunk 157 · page-multi 22 · unresolvable 16 · articulus 5 · work 4; authority 2). **QA flags ours: 1 of 210** — `c6-v1-9` p319-8 `Iud. 7, 13` (chapter-out-of-range; banked (9)). Outside the 210: **15** unresolved-anaphora lines ours (all `ibid. v. N`/`ibid. C, V`, also among the 99 coordinate-ibid lines); 0 printed-slip rows ours | NOTE (docketed, § 7) |
| `build-content.mjs` (site/) | **content.json: 17 books, 2,239 questions, 2,239 translated** | CLEAN |
| `build-index-json.py` (after content) | scripture 77 books / 17,186 citations; **crossref 1,771 chunks cited / 10,833 backlinks** (= `c8-v51-59`'s figure) | CLEAN |
| `git status` afterwards | only the pre-existing untracked `.claude/settings.local.json` | CLEAN |

**Page markers:** all 40 chunks have identical `<!-- page N -->` lists in Latin and English. **Anchor sequences** (numbered
labels, in order) identical La/En in all 40 (counts = the per-chunk entry counts above; `tr-` anchors English-only, Latin `tr-` = 0). **Paragraph
numbers** identical La/En in all 40 (673 numbered lines, paragraphs and numbered arguments). **No def without an anchor; no duplicate anchor; no label owned twice in vol6.**

**La/En digit multiset per entry: 14 mismatches of 1,245 — all false positives, 0 defects:**
- spelled ordinals / numbers: `83 Qq.` → *Eighty-three Questions* ×5 (p277-10, p279-4, p290-6, p293-10, p316-6); `De 1. membro` → "the first member" (p269-2, p357-6); `Orat. 4. (1. adversus Iulian.)` → "the first against Julian" (p352-6);
- English adds digits inside a gloss or a ruling-37 bracket: p303-9 ("[so printed; … are 5:19]"), p319-3 ("[… p. 318 n. 14]", banked (8)), p323-12 (*Act. 7* glossed "Acts 7"), p329-3 (*Hebr. 11* glossed), p351-7 (`[143, 7.]` repeated in the gloss);
- roman → arabic: p308-11 `d. XII … d. XV` → "d. 12 … d. 15" — house style; in scope 7 of 9 roman `d.` sites stay roman in the English (docket N4).

**Register censuses relevant to rulings** (live region; full tables in the evidence sheet § 5–6): "Holy Ghost" **0** (80(b) ✓) · *perhibere*
→ "give" throughout, "bear" only for Chrysostom's *ferre* (81(a) ✓) · *signum*/*miraculum* paragraph-aligned, 0 misses (74 ✓) · *magister*
→ "teacher", Lombard "the Master", "Master Hugh" (84 ✓) · *doctor* → "doctor" (81(b) ✓) · `tr-lumen` 8/8, `tr-doctrina` 24/24, `tr-vacare`
3/3 chunks owing them, none orphaned · *studium* contextual, no note (80(c) ✓) · *pudicitia* 0 register sites (81(d) holds) ·
*intelligentia* "intelligence" (2026-10-23 ✓) · *intellectus* "understanding" except one apparatus "intellect" (N3).

### ⚠ DEFECT CLASS (convention; English only): the scholastic formula labels drift by capitulum → docket § 1
Found by a cross-chunk label census, not by any tool. Of 108 *Respondeo* labels: "I respond" 77, **"I answer" 16** (5 Cap. VIII chunks),
**`Respondeo:` left in Latin 15** (4 Cap. IV chunks). Of 47 opposing formulae: "On the contrary" 36, **Latin `Contra:`/`Sed contra` left 7** (Cap. IV),
"Against" 2 (banked (78)), "Against this" 1, "To the contrary" 1. **Sap ruling 41 already repaired an English `**Contra:**` as a DEFECT**,
so the **22 Latin-left labels are defects by precedent**; the 20 others are drift from the CLAUDE.md formula table. Fix (if ruled):
42 English lines, Latin untouched.

### Other observations (no defect)
- Claimed entry counts in every chunk's `transcription_status`/Notes match the file (40/40) — the shakedown's 45/46 class did not recur.
- English bracket forms for printed faults have drifted into six shapes (docket N2).

## PASS 3: boundary sweep. **CLEAN — 41 seams, 104 leaves, 0 defects**

**Ownership.** Every page 269–372 is owned exactly once per note, with a contiguous 1..N register (checker; re-derived independently by
parsing every `[^pP-N]` def in vol6 against `KNOWN_TOTALS_VOL6`: no label owned twice, no gap; p. 372 PARTIAL 1–5 of 12 by design).
**`KNOWN_TOTALS_VOL6` matches the plate on all 104 leaves** — the highest printed numeral was read on every leaf (digit traps checked:
p. 355's last is 13 not 18; p. 368 R's entry is 8 not 6; p. 313's ¹⁷ ¹⁸ share a line; on p. 288 the gutter runover fills the R block, so ¹¹ is the L block's last).
34 leaves are shared by two chunks.

**Method.** Plates `raw/vision/vol6/p-269 … p-372.png` (450 dpi, 2067×2985). Read in four parallel read-only sweeps (pp. 269–294 · 295–320 ·
321–346 · 347–372) plus one check here. **Every text reading from a region crop at 0.5–1.0×** (footer bands mostly 0.55–0.75×, seam
crops 0.5–0.75×, one digit check at 0.9×, p. 302 ¶ 84 at 1.0×); **whole-page downscales (0.25–0.33×) for structure only — no apparatus
text read from them; no full page read at 450 dpi.** About 270 region crops in all (58 + 82 + 51 + 79 + 1).

| seam page | A → B | outgoing tail on the plate | incoming opening on the plate | footer split | verdict |
|---|---|---|---|---|---|
| 269 | c1-v43-51 → c2-v1-11 | …*et ideo recte filium hominis se appellat*¹. | `CAPITULUM II.` (small caps) → 1. *Et die tertio*² *nuptiae* | 1 / 2–13 | CLEAN |
| 273 | c2-v1-11 → c2-v12-17 | …*et nemo eam tollit a me.* | *Secunda manifestatio, quae facta est Iudaeis.* → 18. *Post haec*³ | 1–2 / 3–10 | CLEAN |
| 275/276 | c2-v12-17 → c2-v18-25 | …*pro defensione veritatis accenditur* ». (R runs short) | head of 276, no heading: 32. *Responderunt Iudaei* | 275 A / 276 B; 276 L head = p. 275 n. 13 (page, ledgered to A) | CLEAN |
| 277/278 | c2-v18-25 → c3-v1-2 | …*non membrorum distinctione*¹². (R runs short) | `CAPITULUM III.` → 1. *Erat autem quidam*¹ *homo* | 277 A / 278 B | CLEAN |
| 279 | c3-v1-2 → c3-v3-12 | …*non per invocationem faciebat miracula*⁵. | 7. *Respondit Iesus et dixit ei* | 1–5 / 6–13 | CLEAN |
| 282 | c3-v3-12 → c3-v13-16 | …*sed quia parva in respectu dicendorum.* | 23. *Et nemo ascendit in caelum.* | 1–2 / 3–9 | CLEAN |
| 283 | c3-v13-16 → c3-v17-21 | …*et omnis talis salvabitur*⁸. | 30. *Non enim misit Deus* | 1–8 / 9–10 | CLEAN |
| 285 | c3-v17-21 → c3-v22-26 | …*et sic veniunt peccatores per contritionem.* | 39. *Post haec venit Iesus* | — / 1–9; 285 L head = p. 284 n. 13 (page, ledgered) | CLEAN |
| 286 | c3-v22-26 → c3-v27-36 | …*tamen dandi gratiam*¹³. | 49. *Respondit Ioannes et dixit.* … *supra*¹⁴ | 1–13 / 14 | CLEAN |
| 289 | c3-v27-36 → c4-v1-6 | …*quando perfecte amantur*⁷. | `CAPITULUM IV.` → *Tertia manifestatio, quae facta est Samaritanis.* → 1. | 1–7 / 8–12 | CLEAN |
| 291 | c4-v1-6 → c4-v7-14 | …*et fons et puteus dicitur* ». | 14. *Venit mulier de Samaria* … ¹³ | 1–12 / 13–15 | CLEAN |
| 293 | c4-v7-14 → c4-v15-27 | …*amando habet, licet non perfecte.* | 28. *Dicit ad eum mulier* | 1–10 / — | CLEAN |
| 296 | c4-v15-27 → c4-v28-42 | …*et ideo non fuerunt ausi quaerere.* | 47. *Reliquit ergo hydriam suam* (no heading) | 1–12 / 13 | CLEAN |
| 300 | c4-v28-42 → c4-v43-54 | …*quia Dominus loquitur de messe gratiae.* | *Quarta manifestatio, quae facta est Galilaeis.* → 69. | 1–2 / 3 | CLEAN |
| 303 | c4-v43-54 → c5-v1-9 | …*et recusavit ire ad reguli filium*⁶. | `CAPITULUM V.` → *Secundo, de manifestatione Verbi …* → 1. | 1–6 / 7 | CLEAN |
| 306 | c5-v1-9 → c5-v10-18 | …*ab his qui quaerunt salutem.* | 19. *Erat autem Sabbatum* | 1–7 / 8 | CLEAN |
| 308 | c5-v10-18 → c5-v19-23 | …*a quo non cessat in Sabbato*¹¹. | 35. *Respondit itaque Iesus* | 1–11 / 12 | CLEAN |
| 311 | c5-v19-23 → c5-v24-30 | …*quia summe diligit*⁴. | 47. *Amen, amen dico vobis* | 1–4 / 5 | CLEAN |
| 313 | c5-v24-30 → c5-v31-39 | …*et ipse obiicit sic in primo sensu*¹⁶. | 59. *Si ego testimonium perhibeo* | 1–16 / 17–18 | CLEAN |
| 316 | c5-v31-39 → c5-v40-47 | …*gradatim ordinantur secundum dictas conditiones.* | 72. *Et non vultis venire ad me* | 1–12 / 13 | CLEAN |
| 318 | c5-v40-47 → c6-v1-9 | *Respondeo: Etsi sit minus simpliciter, non tamen Iudaeis minus, sed maius.* | `CAPITULUM VI.` → *Secundo, Filius Dei se manifestat conservatorem.* → 1. (… *Primo se manifestat conservatorem corporum.*) | 1–9 / 10–15 | CLEAN |
| 320 | c6-v1-9 → c6-v10-13 | …*Proba me, Domine, et tenta me.* | 15. *Dicit*¹² *ergo Iesus* | 1–11 / 12–14 | CLEAN |
| 322 | c6-v10-13 → c6-v14-21 | …*doctrinam et eius fructum multum*⁸. | 24. *Illi autem*⁹ *homines* | 1–8 / 9–12 | CLEAN |
| 324 | c6-v14-21 → c6-v22-33 | …*unde multa in secreto ostendit eis.* | *Secundo, manifestat se conservatorem spirituum.* → 37. | 1–6 / 7–9 | CLEAN |
| 327 | c6-v22-33 → c6-v34-40 | …*oppositae vero secundum veritatem apertam.* | 54. *Dixerunt ergo ad eum.* | 1–10 / 11–15 | CLEAN |
| 329 | c6-v34-40 → c6-v41-52 | …*Unde Christus non eos perdit, sed ipsi se.* | 65. *Murmurabant ergo Iudaei* | 1–7 / 8–12 | CLEAN |
| 332 | c6-v41-52 → c6-v53-59 | …*Et sic auctoritas valet ad propositum.* | 81. *Et panis, quem ego dabo.* | 1–4 / 5–12 | CLEAN |
| 335 | c6-v53-59 → c6-v60-72 | …*panis est, non venenum* ». | 95. *Haec dixit in Synagoga* | 1–11 / — | CLEAN |
| 338 | c6-v60-72 → c7-v1-13 | …*ut nemo glorietur de praesenti vocatione.* | `CAPITULUM VII.` → *Tertio, Filius Dei se manifestat directorem et illustratorem tripliciter.* → 1. *Post haec*⁹ | 1–8 / 9–10 | CLEAN |
| 342 | c7-v1-13 → c7-v14-18 | …*ideo tempus paschale exspectabat.* | 19. *Iam*¹⁰ *die festo mediante.* | 1–9 / 10–13 | CLEAN |
| 344 | c7-v14-18 → c7-v19-24 | …*vel discretive.* | *Pars secunda agit de doctrinae communicatione dupliciter.* → 27. | 1–15 / — | CLEAN |
| 346 | c7-v19-24 → c7-v25-31 | …*docet castitatem*⁹. | 36. *Dicebant ergo quidam ex Ierosolymis.* | 1–9 / 10–12 | CLEAN |
| 348 | c7-v25-31 → c7-v32-39 | …*et de hac dicitur Ioannis octavo.* | 47. *Audierunt autem*⁸ *Pharisaei* | 1–7 / 8–16 | CLEAN |
| 350 | c7-v32-39 → c7-v40-53 | …*in evidentia et abundantia*¹¹. | 58. *Ex illa autem*¹² *turba.* | 1–11 / 12 | CLEAN |
| 353 | c7-v40-53 → c8-v1-11 | …*ideo erraverunt*⁴. | `CAPITULUM VIII.` (full measure) → 1. *Iesus autem perrexit* … *occidere*⁵ | 1–4 / 5–6 (upper block 1–4, n. 4's schema, lower block 5–6) | CLEAN |
| 357 | c8-v1-11 → c8-v12-20 | …*damnavit Deus non hominem, sed peccatum* ». (foot of L) | head of R, no heading: 17. *Iterum ergo locutus est eis Iesus*⁷ | 1–6 / 7–9 + unnumbered *Sola ed. habet* full measure below both blocks (= `[^p357-nota]`) | CLEAN |
| 360 | c8-v12-20 → c8-v21-30 | …*insinuatur etiam nobis humani arbitrii libertas.* | 30. *Dixit ergo iterum eis Iesus.* | 1–10 / 11–14 | CLEAN |
| 363 | c8-v21-30 → c8-v31-36 | …*non de dispensatione divinae sapientiae*². | 45. *Dicebat ergo Iesus* … *ibi*³ | 1–2 (+ n. 2's schema) / 3–11 | CLEAN |
| 365 | c8-v31-36 → c8-v37-50 | …*Non erit heres filius ancillae cum filio liberae*⁵. | 54. *Scio, quia filii Abrahae estis.* … ⁶ | 1–5 (+ n. 5's schema) / 6–9 | CLEAN |
| 369 | c8-v37-50 → c8-v51-59 | …*sed honorifico Patrem meum.* | 75. *Amen, amen dico vobis.* … *ipsam*⁹ | 1–8 / 9–12 | CLEAN |
| 372 (out) | c8-v51-59 → [Cap. IX] | *Respondeo: Est iudicium condemnationis et discretionis; de primo supra*⁵*, de secundo habetur hic.* | `CAPITULUM IX.` (full measure) → *Secundo, Filius Dei se ostendit lucem et directorem miraculo potentiae.* → 1. *Et praeteriens Iesus* … inside ¶ 1 *In parte prima insinuatur mirabilis caeci illuminatio.* | 1–5 / 6–12 (n. 6 at ¶ 1 *ibi*); n. 9 runs over the gutter | CLEAN (hand-off as recorded) |

No cascade-merge splice at any seam; every outgoing tail is a complete sentence; every incoming text opens on its printed
paragraph number or heading as built (headings, italic/roman and ¶ numbers all match).

**Register heads and ledger negatives, re-derived on all 104 leaves.** LEFT and RIGHT register heads were read on every leaf 269–372
(plus pp. 294/320/346 tails against their next leaves).
- **Unnumbered LEFT heads (page runovers): exactly three — p. 276 (p. 275 n. 13), p. 285 (p. 284 n. 13), p. 298 (p. 297 n. 12)** = the
  ledger's three `:page` entries. No other LEFT head in scope is unnumbered.
- **Unnumbered RIGHT heads (gutter runovers): 42 in scope** — 269, 274, 276, 278, 280, 283, 286, 287, 288, 289, 291, 292, 294 · 295, 296, 305, 310,
  319 · 324, 326, 331, 334, 336, 338, 339, 340, 343 (lower block) · 349, 350, 352, 353 (lower), 356, 357, 358, 361, 362, 363 (upper n. 2 and lower
  n. 7), 365 (lower), 368, 369, 371 = the ledger's 42 `:gutter` entries one for one (p. 372 n. 9 is the next chunk's, already in the
  hand-off). **No unledgered runover; no ledger entry the plate does not support.**
- **The nine `-` lines are CONFIRMED:** every leaf owned by `c4-v43-54`, `c5-v10-18`, `c5-v24-30`, `c5-v31-39`, `c5-v40-47`, `c6-v10-13`,
  `c6-v34-40`, `c7-v19-24`, `c7-v25-31` opens both blocks numbered within that chunk's run of notes.
- Full-measure matter inside registers, as built: p. 315 (*Testimonia Christo exhibita*, below a short register), p. 339 n. 1, p. 343 n. 6
  (upper/lower blocks), p. 353 n. 4, p. 357 (unnumbered *Sola ed. habet*), p. 363 n. 2, p. 365 n. 5.

**For the Cap. IX builder (from the p. 372 read):** ledger `p.372 n.9:gutter`; the three p. 372 headings the raw drops are
`Capitulum IX.`, *Secundo, Filius Dei se ostendit lucem et directorem miraculo potentiae.* and, inside ¶ 1, *In parte prima insinuatur
mirabilis caeci illuminatio.* — the last is the stack's lowest (ruling 79(b)). Brief the formula labels too (docket § 1).

## Summary for the gate log
- **Pass 1 CLEAN** (121 chunks, 0 live flags) · **Pass 2 CLEAN on every tool** (apparatus 121/3,784 · census 121/169 · style 11/6/2,240, 0 ours ·
  citations 30,584 / QA 210, **1 ours**, ledger byte-identical · content 2,239/2,239 · index 1,771/10,833 · tree clean) · **Pass 3 CLEAN** (41 seams,
  104 leaves, 45 runovers re-derived = ledger, 9 negatives confirmed).
- **Defects: one CLASS, 22 sites** — English formula labels left in Latin (Cap. IV: `Respondeo:` ×15, `Contra:`/`Sed contra` ×7), defects by
  Sap ruling 41; with 20 further drift sites ("I answer" ×16, "Against" ×2, "Against this", "To the contrary") → docket § 1. **No text
  defect in Latin, apparatus digits, ownership or seams.**
- NOTEs: digit-sweep false positives 14/1,245; roman `d.` house style (N4); bracket-form drift (N2); 1 in-scope QA line already banked (9).
