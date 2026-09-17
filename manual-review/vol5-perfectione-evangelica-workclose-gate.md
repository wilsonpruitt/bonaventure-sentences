# Vol V — *QD de perfectione evangelica* WORK-CLOSE GATE (printed pp. 117–198)

Run 2026-09-17, immediately after `bon-qpe-q4-a3` landed (the work's last chunk) and after Wilson's
**seven work-close register rulings** were taken and applied (`b50fb91`). **This work has ONE gate: Wilson
declined the shakedown on 2026-09-15**, so the whole 82-page span is audited here for the first time.
Modelled on `manual-review/vol5-mysterio-trinitatis-workclose-gate.md`; pass structure and log format follow it.

**Scope: ten chunks, `bon-qpe-q1` … `bon-qpe-q4-a3`, pp. 117–198 with no gap, 689 apparatus entries**
(688 numbered + the unnumbered `p198-nota`).

| chunk | pages | entries | | chunk | pages | entries |
|---|---|---|---|---|---|---|
| `q1` | 117–124 | 69 | | `q3-a2` | 171–175 | 35 |
| `q2-a1` | 124–133 | 74 | | `q3-a3` | 175–179 | 40 |
| `q2-a2` | 134–155 | 170 | | `q4-a1` | 179–183 | 36 |
| `q2-a3` | 156–165 | 82 | | `q4-a2` | 183–189 | 51 |
| `q3-a1` | 166–171 | 55 | | `q4-a3` | 189–198 | 77 |
| | | | | **total** | **82 pp.** | **689** |

**Result: ZERO TEXT DEFECTS · ONE FALSE LIVE FLAG, repaired (a bare `[?]` inside an English gloss of the
EDITORS' own query mark) · one stale Notes line brought up to date. Passes 1–3 clean, all seven rulings
verified present in the text, all eleven boundaries match the frozen record digit for digit. Pass 4 done,
~420 MB reclaimed. Committed locally; NOT pushed, NOT deployed.**

---

## ▶ FINDING 1 (repaired) — `bon-qpe-q3-a3` p. 179 n. 3: the corpus's ONE live `[?]` in this work, and it was ours by accident

`check-live-flags.py` — the instrument, not `grep` — reported **238 live occurrences corpus-wide against the
mysterio baseline of 237, and the one new occurrence was in this work**: `bon-qpe-q3-a3`'s English apparatus at
p. 179 n. 3.

The entry renders Quaracchi's own editorial queries: the Latin prints `E *pronitates* [*proniores?*] *rebelliones,*
D *per vires* [*?*] *rebelliones.*` — the `[?]` is **the editors' mark, not our flag**, and the chunk's `## Notes`
say exactly that and declare the rendering as `[*proniores?*]`, `[*?*]`. But the English side's closing gloss read
`("rebellions through the powers [?]")` — a **bare** `[?]`, against the chunk's own declared form.

⚠ **So the chunk documented the convention and then broke it in one parenthesis**, and the cost was not cosmetic:
it made the chunk's frontmatter and Notes claim of "zero `[?]` flags" **false to the instrument that a gate's
Pass 1 runs**. Nobody reading the text is misled; the gate is.

**Repair:** English gloss → `("rebellions through the powers [*?*]")`, matching the Latin and the chunk's own
declaration. A line added to `q3-a3`'s Notes recording the normalisation and pointing here. **No reading changed,
no Latin touched.** Corpus live-flag count **238 → 237**, i.e. back to the mysterio baseline exactly, with
**`bon-qpe-*` at ZERO**.

▶ **Transferable rule, now in `q3-a3`'s Notes: an editor's printed query mark must carry the italic bracketed form
at EVERY occurrence, including inside an English gloss. One plain `[?]` anywhere makes a Tier-2 chunk's
"zero flags" claim false.** ⭐ This is the *mysterio* gate's lesson in a new dress: a claim a chunk makes about
its own register is worth exactly as much as the sweep that tests it, and the chunk that writes the convention
down is not thereby the chunk that keeps it.

## ✏️ Stale documentation, corrected — `bon-qpe-q2-a1`'s *dominium* bullet

`q2-a1`'s Notes still called "ownership" *the working rendering* and ended **"Wilson's call at the gate."** —
written before the gate, true then, false now: Wilson ruled it on 2026-09-17 (ruling 2, the split by sense).
The bullet now records the ruling, names the other half (`q4-a1` p. 181 → "lordship"), and states that the
rendering above it **stands unchanged**. **Zero rendered text touched** (`## Notes` is not rendered).

## NO DEFECTS FOUND IN THE TEXT

Every other sweep below came back clean on the first honest run. **The work that had seven register rulings taken
on it the same morning arrived at its gate with nothing to repair** — which is the point of taking the rulings
before the gate rather than inside it.

---

## The seven work-close rulings — spot-checked in the text, as ruled

| # | ruling | verified | result |
|---|---|---|---|
| 1 | **purity triple** *pudicitia*/*puritas*/*munditia* → purity / pureness / cleanness | per-chunk Latin↔English parity, paragraph by paragraph | ✅ **PASS.** `q3-a1` *pudicit-* 29 → "purity" 26 + *impudicit-* 3 (**18 paragraphs, 18 paragraphs, per-paragraph counts identical**); `q3-a3` *pudicit-* 4→purity 4, *purit-* 4→**pureness 4**, *mundit-* 3→cleanness 3; `q3-a2` *mundit-* 1→cleanness 1. **No "pureness" leaks outside the 4 ruled sites.** |
| 1b | ***castitas* → chastity** (kept off the triple) | census | ✅ **PASS, exact parity in every chunk:** `q2-a1` 3/3 · `q3-a1` 1/1 · `q3-a2` 8/8 · `q3-a3` 9/9 · `q4-a2` 2/2. |
| 1c | ***purus* (I Tim. 1:5) → "pure heart"**, Douay, adjective not in the triple | grep | ✅ **PASS** — the adjective never renders as a triple member. |
| 2 | ***dominium* SPLIT: "lordship" at `q4-a1` p. 181** | read at the site | ✅ **PASS.** p. 181 *quantum ad dominium potentiae seu praesidentiae* → **"as to *lordship of power* or presidency"**, in the *Respondeo*'s threefold superiority. |
| 2b | ***dominium* → "ownership" at `q2-a1` p. 131** | read at the site | ✅ **PASS.** reply 3 *non quantum ad dominium* → **"not as to *ownership*"**, and *absque dominio et proprietate* → "without ownership and property". |
| 2c | **NO remaining "ownership of power"** | grep, whole work | ✅ **PASS — ZERO occurrences.** |
| 3 | ***ius canonicum* → "canon right"**, the *ius*/*lex* figure held | grep + read | ✅ **PASS at every RENDERED site.** ⚠ **The count wants a word** (below). |
| 5 | ***Antistes* → "Prelate"**, capitalised, one site | read at the site | ✅ **PASS.** `q4-a3` p. 194 Conclusio *summum et primum Antistitem* → "the highest and first **Prelate**", against **eight lower-case "prelate"** (*praelatus*) in the same chunk — the capital carries the distinction exactly as ruled. |
| 6a | ***necessitas tentionis* → "necessity of holding"** | read at the site | ✅ **PASS.** `q4-a2` p. 186 reply 1: *duplex est necessitas: una est* coactionis, *et altera* tentionis → **"necessity is twofold: one is of *coercion,* and the other of *holding.*"** ⓘ The English **distributes the genitive across the sentence** rather than printing the phrase contiguously — that is the Latin's own shape, and the ruled pair (coercion / holding) is intact. |
| 6b | ***ordo dignativus* → "the order of deigning"** | read at the site | ✅ **PASS.** `q4-a2` p. 186 *ordinis dignativi, qui currit secundum legem gratiae* → "the order of **deigning,** which runs according to the law of grace". |
| 4 | **"conjugal continence" kept as printed, NO note** | grep | ✅ **PASS.** 16 sites in `q3-a1`; **no `tr-` note anywhere in the work touches it.** The only `tr-` notes in the work are `q2-a2`'s three *vacare* notes (the disclosed mechanism). |
| 7 | **the pp. 155–156 ADDITAMENTUM is NOT transcribed** | live-region scan of `q2-a2` + `q2-a3` | ✅ **PASS.** `q2-a2` p. 155 n. 8 prints the editors' description in both languages (*novem auctoritates… non genuinum*); **`q2-a3`'s live region mentions it ZERO times** and neither chunk transcribes the nine authorities. Register unaffected: p. 155 = 8 (all `q2-a2`'s), p. 156 = 5 (all `q2-a3`'s). |

### ⚠ On ruling 3's "eight `ius canonicum` sites" — the ruling holds, the NUMBER is a string count

CLAUDE.md's ruling 3 says *"only the eight ius canonicum read unidiomatically."* **In the RENDERED text there are
three**: `q4-a3` Latin p. 189 opener (*per ius canonicum*), p. 191 (*Item, hoc ipsum ostenditur per ius canonicum*)
and p. 195's Epilogus (*iuri canonico*) — against **three** English "canon right", one to one, and **zero
"canon law" in any rendered line** (the only "canon law" string in the work is inside `q4-a3`'s `## Notes`,
explaining the refusal). The "eight" is the count of the string `ius canonicum` **across the whole file**, which
includes the frontmatter `transcription_status` and the Notes bullets that quote it.

▶ **The ruling is not disturbed and is NOT re-opened here** — the four-member Epilogus chain (*legi naturae* ·
*legi scriptae* · *iuri pontificio* · *iuri canonico* → "the law of nature · the written law · pontifical right ·
canon right") is present and intact, which is the sentence the ruling was made for. ⛔ **But a ruling recorded with
a site count taken by `grep` over a whole chunk file counts its own prose.** ▶ **Rule for the evidence sheet at the
next work-close gate: every census on the sheet must be taken over the LIVE REGION (frontmatter and `## Notes`
stripped), and the sheet should say so.** This is the mysterio gate's *"write the regex against the noun"* finding
one level up: write the regex against the **rendered text**.

## The carried corpus rulings — re-verified across all ten chunks

| ruling | result |
|---|---|
| **1. *intellectus* → "understanding"** | ✅ **ZERO bare "intellect" in all ten LIVE regions.** ⚠ A whole-file grep returns 2 per chunk and they are **all Notes prose** (bullets of the form *"Zero bare 'intellect' over pp. …"*) — the same trap as the mysterio gate's *intellectualis*, sprung from the other side. The mini-pilot's forecast of "*intellect-* 4 over the band" was a whole-file count. |
| **2. *lux* → light / *lumen* → "lumen"** | ✅ **HOLDS, and the mysterio gate's exposed shape was hit and survived.** Per-chunk census: `q2-a1` lux 0 / lumen 1 → "lumen" 1 · `q3-a1` lux 2 / lumen 0 → "light" 2 (Luke 16:8 *filii lucis* → "the children of light") · **`q3-a2` lux 0 / lumen 1 → "light"** · `q4-a3` lux 1 / lumen 1 → "light" 1 + "lumen" 1. ⭐ **`q3-a2` is EXACTLY the shape the mysterio gate warned about** (zero *lux*, one *lumen*, "light" in the English) **and it is NOT a defect**: the site is Augustine quoting Jas. 1:17, *gratiarum actio* ***Patri luminum*** → **"Father of lights"**, the Douay wording, precedent `bon-don-c1`, and **the chunk's Notes record the exemption by name.** The distinguishing test is the mysterio one: *is it a received scriptural wording, and did the chunk say so?* Both yes. ⚠ `q4-a2`'s two English "light"s are `lightens` ×2 and `slight` — regex noise, not sites. |
| **2b. The Cyprian sentence** | ✅ `q4-a3` p. 195 meets ruling 2 **on both sides in one sentence**: *multi radii sunt, sed unum* ***lumen*** → "many rays but one **lumen**"; *Ecclesia Dei* ***luce*** *perfusa* → "the Church of God, suffused with **light**." The work's only bare "lumen" in 82 printed pages — recorded so it is never read as a lapse. |
| **3. `contuit-`** | ✅ **HOLDS at the work's ONE rendered site** — `q2-a1` p. 129 *idoneus est ad **contuitionem** sublimium* → "most fit for the **contuition** of sublime things" (the mini-pilot's forecast site). No "intuition"/"gaze"/"beholding" substitute anywhere. ⚠ The other whole-file hits are Notes prose. |
| **5. `fundam. N` → *fundamentum/fundamenta N* (apparatus)** | ✅ **HOLDS at ALL NINETEEN sites across the work.** Latin retains `fundam.` as printed at every site; the English expands, italicised, at every site — `q1` p. 122 n. 6 · `q2-a1` ×3 · `q2-a2` ×8 · `q2-a3` p. 158 n. 11 · `q3-a1` p. 168 n. 12 · `q3-a2` p. 174 n. 4 (external, Vol II) · `q4-a1` p. 181 n. 2 (external) · `q4-a2` p. 184 n. 2 (external) · `q4-a3` ×2 (both inside `p198-nota`, both quoted). **No "foundation"/"ground" renders a `fundam. N` reference anywhere.** ⚠ The English form is ***fundamentum* 15**, italic — a regex written as `fundamentum\s+\d` finds **none of them**. Write it against the italic. |
| ***vacatio* → leisure / *quies* → rest** (ratified at the mysterio gate) | ✅ The work's only *vacare* sites are in `q2-a2`, which carries the **three approved `tr-vacare` notes**. `q3-a3`, `q4-a1`, `q4-a2`, `q4-a3` have zero *vaca-*/*quie-*/*otium* sites; `q2-a3` renders *otium/otiositas* → "idleness", correctly kept off the *vaca-* family. |

## Pass 1 — `[?]` flag resolution: ZERO in scope, VERIFIED not assumed

A bare `grep '\[?\]'` over the ten chunks returns **32 hits** (q1 3 · q2-a1 3 · q2-a2 5 · q2-a3 3 · q3-a1 3 ·
q3-a2 4 · q3-a3 4 · q4-a1 3 · q4-a2 2 · q4-a3 2) — **every one of them frontmatter or `## Notes` prose** of the
form *"zero `[?]` flags"*, which is precisely why `check-live-flags.py` exists.

`check-live-flags.py`, before the repair: **238 live occurrences corpus-wide, ONE of them `bon-qpe-q3-a3`**
(Finding 1). **After the repair: 237 corpus-wide — the mysterio baseline to the unit — and `bon-qpe-*` ZERO,
per chunk, all ten.** Vol V alone: 10 live flags, all in already-deployed chunks (`bon-brev-p6-c13` 2,
`bon-hex-c15` 2, `bon-hex-c19` 2, `bon-hex-c22` 4), unchanged.

## Pass 2 — style/apparatus suite

- **`check-vol5-apparatus.py`: 162 chunks / 3,984 entries, ALL CHECKS PASSED** — the known-good baseline exactly.
  **Every printed page 117–198 is present, `ok`, and contiguous 1..N** (p. 116 is absent because it is blank —
  plate-verified; p. 199 is the Breviloquium half-title). **No PENDING remains anywhere in the work.**
  `KNOWN_TOTALS[198] = 3` behaves as designed: `p198-nota` owns no numeral and is not counted there.
- **`polish-style-scan.py`: 11 issues / 6 chunks / 2,114 scanned — ZERO in `bon-qpe-*`.** The identical list the
  last five gates recorded: `bon-hex-c23` `[V5LABEL]` (deliberate) + ten `[PAIR]` J4 class-B residue in Vols III–IV
  (`III-d31-a3-q3`, `III-d32-a1-q2`, `III-d5-a2-q4`, `IV-d14-p2-a2-q1`, `IV-d16-p2-a2-q2`).
  ⚠ **Pre-existing, OUTSIDE this work, and deliberately NOT fixed here — out of scope.**
- **`check-vol5-census.py`: rosters agree 162/162**, 273 runovers (246 gutter-crossing, 27 page-crossing;
  122 chunks positive, 40 negative). This work's page-crossing runovers — **p. 136 n. 8, p. 138 n. 10
  (`q2-a2`), p. 181 n. 7 (`q4-a1`)** — are the three their chunks documented; `q2-a3`, `q3-a*`, `q4-a2` and
  `q4-a3` are page-crossing-free as they claimed.
- **`build-citations.py` → QA 201** (unchanged; the ledger is byte-identical to the committed one — the gate's two
  edits touched a gloss and a Notes bullet, neither a citation). **`build-index-json.py` run after it**:
  scripture 75 books / 10,615 citations; crossref **1,674 chunks cited, 10,193 backlinks, 3.13 MB**.
- **`build-content.mjs`: 13 books, 2,113 questions, 2,113 translated** — the baseline.

## Pass 3 — BOUNDARY INTEGRITY: nine interior boundaries + both ends, re-derived from the files

Ownership and register re-derived by parsing every `[^p<page>-<n>]:` **definition** in the ten chunks — not read
off the chunks' claims.

| # | boundary | page | frozen record | derived | verdict |
|---|---|---|---|---|---|
| 1 | `q1` \| `q2-a1` | 124 | **5/0 body-only** | `q1` nn. 1–5, `q2-a1` none | ✅ |
| 2 | `q2-a1` \| `q2-a2` | 134 | **0/8** | `q2-a1` ends p. 133, `q2-a2` nn. 1–8 | ✅ |
| 3 | `q2-a2` \| `q2-a3` | 156 | **LEAF EDGE 0/5** | `q2-a2` ends p. 155, `q2-a3` nn. 1–5 | ✅ |
| 4 | `q2-a3` \| `q3-a1` | 166 | **LEAF EDGE 0/10** | `q2-a3` ends p. 165, `q3-a1` nn. 1–10 | ✅ |
| 5 | `q3-a1` \| `q3-a2` | 171 | **3/5** | `q3-a1` nn. 1–3, `q3-a2` nn. 4–8 | ✅ |
| 6 | `q3-a2` \| `q3-a3` | 175 | **1/9** | `q3-a2` n. 1, `q3-a3` nn. 2–10 | ✅ |
| 7 | `q3-a3` \| `q4-a1` | 179 | **4/5** | `q3-a3` nn. 1–4, `q4-a1` nn. 5–9 | ✅ |
| 8 | `q4-a1` \| `q4-a2` | 183 | **1/7** | `q4-a1` n. 1, `q4-a2` nn. 2–8 | ✅ |
| 9 | `q4-a2` \| `q4-a3` | 189 | **1/5** | `q4-a2` n. 1, `q4-a3` nn. 2–6 | ✅ |

**ALL NINE MATCH THE FROZEN RECORD DIGIT FOR DIGIT — 7 shared-leaf forwards / 2 leaf edges.**

**(a) Ownership and contiguity, the decisive test.** Across the ten chunks: **every printed page 117–198 is owned,
with ZERO gaps and ZERO pages owned twice except the five shared leaves above, where the two owners' numbers
concatenate to a contiguous 1..N with no overlap and no hole.** Derived, not asserted:
gaps in 117–198 = **[]**; pages with a non-contiguous register = **none**. **689 entries in all**, agreeing with
`check-vol5-apparatus.py`'s page-by-page report and with each chunk's own footer accounting.

**(b) Grammatical continuity — all nine PASS.** Every outgoing chunk's Latin closes on a complete sentence ending
its last unit (`q1` *…habitus viles et abiectos.* · `q2-a1` *…altissimum et stabile fundamentum.* · `q2-a2`
*…terrestrium et infernorum. Amen.* · `q2-a3` *…ad opera manualia sunt astricti.* · `q3-a1` *…in quaestione
sequenti plenius patefiet.* · `q3-a2` *…plenius apparebit.* · `q3-a3` *…virginitas paradisum.* · `q4-a1`
*…felicitatis aeternae.* · `q4-a2` *…rectitudo ordinis observetur.*), and **every incoming chunk opens on its
own heading** — `### Quaestio II. *De paupertate.*` · `### Articulus II. *De paupertate quoad mendicitatem*` ·
`### Articulus III. *Utrum pauperes validi…*` · `### Quaestio III. *De continentia.*` · `### Articulus II. *De
continentia viduali…*` · `### Articulus III. *De sanctimonia virginali.*` · `### Quaestio IV. *De obedientia.*` ·
`### Articulus II. *Utrum sit consonum…*` · `### Articulus III. *De obedientia summo Pontifici debita.*`
**No splice, no stranded fragment, no orphaned heading.**

**(c) The work's two ends.** **Start p. 117** — `q1` opens at the display heading with the anchored proemium
(n. 1 = the work's textual note, codd. E D I); p. 116 blank, plate-verified; the start was fixed positively from
p. 117's `DE PERFECTIONE EVANGELICA` heading. **End p. 198** — `q4-a3`'s last Latin line is reply 16's
*…qui nos tanquam pastor deducat et reducat ad* **ovile** *summi Pastoris*[^p198-3], followed by **[^p198-nota]**,
the unnumbered 1890s papal-primacy dissertation, anchored after the body's final word in both languages.
**NO COLOPHON.** The end was fixed **positively from p. 199 (the Breviloquium half-title, gathering signature 26)**,
never from white space — re-verified on the plate before `q4-a3` was built. ✅ **Eleven of eleven.**

## Supplementary sweeps

**Citations — the work's own ledger: 701 records** (scripture 511, crossref 189, authority 1), resolving as
**verse 478 · chunk 161 · chapter 33 · page-multi 17 · work 4 · distinctio 3 · articulus 2 · excluded 1 ·
unresolvable 1 · forward 1**. **ZERO dangling, ZERO ambiguous.** **ZERO QA flags of ours** — the corpus QA report
contains not one `bon-qpe-` line.

- The **one unresolvable** is `q1` p. 119 n. 3 `ibid. d. 42. a. 3. q. 2` — the docketed cross-note `ibid.`
  anaphora class (carry-list item 10), not a defect.
- The **one forward** is `q3-a1` p. 167 n. 12 `pag. 671, nota 9` → `tom5:p671`, a Vol V page not yet chunked.
  **It is a forward OUT of the work, not into it.**
- ⭐ **NO forward reference into pp. 117–198 remains anywhere in the corpus.** The eleven corpus-wide forwards
  point at `tom5:p1`, `tom5:p199`, `tom5:p209`, `tom5:p543`, `tom5:p671`, `tom9:p689`, `tom11:p745` and
  `bon-sci-q4` — **not one lands in 117–198.** The work is closed to the corpus.
- **32 inbound records from 24 already-deployed chunks** resolve into this work (Breviloquium ×10, Hexaemeron ×8,
  *de reductione* ×3, *septem donis* ×4, Itinerarium ×3, *decem praeceptis* ×2, *scientia Christi* ×2) —
  **none live until deploy.**

## Docketed, not fixed — resolver classes and artefacts (QA lines, NOT text edits)

Carried into the gate by the chunks and **left exactly where they were**; none is a text defect and none is fixed
by a pattern change.

1. **Cross-note / cross-author `ibid.` anaphora — 8 sites:** `q1` p. 119 nn. 1–2 · `q3-a2` p. 173 n. 1, p. 174 n. 3 ·
   `q4-a1` p. 179 n. 6, p. 181 n. 4, p. 182 n. 2 · `q4-a3` p. 191 n. 2 (a canon *ibid.*), p. 193 n. 1.
   **Same class the mysterio gate docketed**; the fix is author governance for `ibid.`/`loc. cit.`, which touches
   the frozen inheritance rules and every volume. **A scoped job with its own before/after diff.**
2. ⭐ **NAMED-WORK references to chunks we HOLD are not parsed** — `q4-a3`'s `p198-nota` names *Breviloquium
   p. VI. c. 10. et c. 12* and *Hexaëmeron sermo 22*; `bon-brev-p6-c10`, `bon-brev-p6-c12` and `bon-hex-c22` are
   all built and deployed and **none produces a record.** ⛔ **The only class where the resolver is silent about a
   target that certainly exists and is certainly named.** Highest-value resolver item on the docket.
3. **Verbal back-references not parsed:** `supra q. 1.` (`q2-a1`) · `supra q. 2. a. 3. ad 12.` (`q4-a2`) ·
   `quaest. praeced.` / `art. praeced.` / `infra a. 3. solut. ad 11.` (`q3-a2`) · `loc. cit. in praeced. nota` (`q1`) ·
   `Quaest. de mysterio Trin. q. N. a. M.` (`q1` p. 123 n. 1).
4. **Bare-`pag. N` tome-inheritance FALSE HITS, inbound, all WRONG:** `bon-qsc-q4` p. 25 n. 9 and p. 27 n. 1
   (`pag. 186`) · `bon-hex-c7` (`pag. 149`) · `bon-don-c8` (`pag. 154`) · `bon-hex-c9` (`(tom. 12. pag. 178)` = Surius) ·
   `bon-hex-c6` (`(pag. 180)` = Jourdain). ⚠ **These are a DIFFERENT residue from the tome-inheritance bug the
   mysterio gate fixed** — that one lost the tome of a bare page after `tom. IV.`; these attach a bare `pag. N`
   printed with no tome at all to the citing volume. Governance, not a pattern.
5. **`page-multi` right-page / owner-unpicked (correct but unresolved, NOT wrong):** `bon-brev-p4-c1` `pag. 183,
   nota 3` (Anselm) → `q4-a1`+`q4-a2` · `bon-itin-c1` `pag. 179, nota 9` → `q3-a3`+`q4-a1` · `q4-a3`'s own
   `tom. IV. pag. 497` and `tom. II. pag. 464`. Own oddity: `ed. Maurin. tom. 3. pag. 448` resolves into our
   p. 448 — a Maurist page, wrong.
6. **Out of scope, still open from the mysterio gate:** `bon-don-c8`'s *de Scientia Christi q. 4.* is emitted as
   `forward` to slug `bon-sci-q4` — the works table's slug is wrong (`bon-qsc-`). **One line in
   `scripture-books.json`; still not done.** Visible in this gate's forward list.

## Textual dispositions owed to the gate — both SETTLED, neither by the gate

7. **The pp. 155–156 ADDITAMENTUM** — settled by **Wilson's ruling 7**: not transcribed, left as `q2-a2` p. 155
   n. 8 describes it. Verified above. **The gate does not re-open it.**
8. **The p. 131 *ab [ip]so* restoration** (`q2-a1`, a failing impression restored by measurement — flanking 77–103
   against line 46–59, no ghost; borderline). **Stands as built.** The restoration is bracketed in the text and
   documented in the chunk's Notes; the gate found no evidence against it and the plate is now deleted
   (Pass 4), so **re-litigating it would cost a re-extraction.** ▶ **Not a defect; recorded as accepted.**

## Pass 4 — disk: ✅ DONE, ~420 MB reclaimed

| what | files | size |
|---|---|---|
| `raw/vision/vol5/*.png` (pp. 117–199) | **83** | **279 MB** |
| `/tmp/colcrop/*` | **60** | **141 MB** |
| **total** | **143** | **~420 MB** |

Both gitignored (`.gitignore:9  raw/vision/`) and **fully regenerable from the PDF** via
`tools/extract-pages.py --volume vol5` + `tools/colcrop.py vol5 <page>`. **Deleted.** Both directories now 0 files,
0 B. ⚠ **This is the largest reclaim of any Vol V gate so far** (mysterio: ~222 MB) because this work is 82 printed
pages and its last chunk pulled a 10-page span.

## Verification suite at the gate (all re-run AFTER both edits)

`check-vol5-apparatus.py` **162 chunks / 3,984 entries, all passed** · `check-vol5-census.py` **rosters agree
162/162, 273 runovers (246 gutter, 27 page)** · `check-live-flags.py` **237 corpus-wide, `bon-qpe-*` ZERO** ·
`polish-style-scan.py` **11 issues / 6 chunks / 2,114 scanned, ZERO in scope** · `build-citations.py` **QA 201,
23,258 ledger records** · `build-index-json.py` **1,674 chunks cited / 10,193 backlinks** ·
`build-content.mjs` **13 books, 2,113 / 2,113 translated**.

## ▶ THE DEPLOY-BATCH CARRY-LIST (deploy-only; do these at the NEXT deploy boundary, batched)

1. **Add the approved `tr-vacare` note to the two DEPLOYED *vacatio* sites** — `bon-praec-c4` and
   `bon-qmt-q7-a2`. Owed since the mysterio gate's ratification; **still not done.**
2. **Write the *lumen* ruling's owed translator's note at the first *lumen*** in `bon-qsc-q3` / `bon-qsc-q4` and
   the `bon-qmt` chunks — **and now at `bon-qpe-q4-a3` p. 195**, the work's only bare-"lumen" site, where the
   Cyprian sentence puts *lumen* and *luce* six lines apart and a reader without the note will read the pair as
   an inconsistency.
3. **Fix the works-table slug `bon-sci-` → `bon-qsc-`** in `scripture-books.json` (docket item 6) — one line,
   clears `bon-don-c8`'s false forward.
4. ⚠ **`cited-by.tsx`'s `MAX_SHOWN = 25`** still hides the corrected Vol III/IV → Vol II backlinks on
   `bon-sent-II-d7-p2-a2-q1` (38 inbound). **Existing design, noted at the mysterio deploy, not a fault** —
   listed here only so it is not re-discovered as a deploy regression.

## The gate's own finding

⭐⭐ **A work whose register was ruled on the morning of its gate arrives at the gate with nothing to repair.**
The *scientia Christi* gate repaired a five-way rendering; the *mysterio* gate repaired an unrecorded *lumen* and
a resolver bug; **this gate repaired one stray punctuation mark inside a gloss.** The difference is not luck and
not the translator — it is Wilson's procedure from 2026-09-17: **one read-only agent compiles an evidence sheet
first, Wilson rules from the sheet, the rulings are applied, and THEN the gate runs.** The gate's job shrinks from
*discovering* the register to *verifying* it, which is a far cheaper and far more reliable thing to do.

⛔ **And the one thing that still slipped through it was a COUNT, not a judgement** — ruling 3's "eight sites" was
a whole-file `grep` that counted the chunk's own prose (three sites are rendered). The ruling is right; the number
on the sheet is not. ▶ **Every census on an evidence sheet must be taken over the LIVE REGION, and the sheet must
say so.** The same slip produced Finding 1's mirror image: a chunk that wrote its convention down in `## Notes`
and then broke it in a rendered gloss, where nothing but `check-live-flags.py` would see it.

▶ **For the Sermones selecti and for Vols VI–X: run the evidence sheet before the work is finished, not after,
and run it live-region-only.**

## Status

**Committed locally. ⛔ NOT PUSHED. ⛔ NOT DEPLOYED.** Both are Wilson's hard stops and he gives each separately.
`build-citations.py` and `build-index-json.py` have **both been run**, in that order, so the deploy recipe can
start at `cd site && node scripts/build-content.mjs`. ⚠ Live-state claims in this log are DATED and expire.
