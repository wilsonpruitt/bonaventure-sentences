# Vol V — *QD de scientia Christi* WORK-CLOSE GATE (printed pp. 3–43)

Run 2026-09-05, immediately after `bon-qsc-q7` landed (the work's last chunk). Per the frozen Vol V
cadence table this work carries **two** gates: the shakedown at p. 27 (run 2026-09-04,
`manual-review/vol5-scientia-christi-shakedown-gate.md`, three defects all repaired) and **this
one, at the work close**. Modelled on `manual-review/vol5-decem-praeceptis-workclose-gate.md`.

**Scope: seven chunks, `bon-qsc-q1`–`q7`, pp. 3–43 with no gap, 323 apparatus entries.**

| chunk | pages | entries |
|---|---|---|
| `bon-qsc-q1` | 3–6 | 31 |
| `bon-qsc-q2` | 6–10 | 34 |
| `bon-qsc-q3` | 10–16 | 48 |
| `bon-qsc-q4` | 17–27 | 93 |
| `bon-qsc-q5` | 27–32 | 39 |
| `bon-qsc-q6` | 32–37 | 39 |
| `bon-qsc-q7` | 37–43 | 39 |
| **total** | **41 pp.** | **323** |

**Result: ONE DEFECT, repaired — a citation-formula inconsistency in the apparatus that no single
chunk could have seen.** All four frozen register rulings verified mechanically across all seven
chunks and all four HOLD. The shakedown covered q1–q4 only; **q5, q6 and q7 had never been audited
against the rulings before this gate**, and this gate is where that happened.

---

## ▶ DEFECT 1 (repaired) — `fundam. N` is rendered FIVE WAYS at FIVE apparatus sites

The Latin locus-formula `fundam. N` occurs at five apparatus sites across the work and is rendered
five different ways in the English halves:

| site | Latin | English as built |
|---|---|---|
| `bon-qsc-q3 [p16-7]` | `a. 1. q. 2. fundam. 1.` | "a. 1, q. 2, **ground 1**" |
| `bon-qsc-q4 [p23-7]` | `cfr. supra fundam. 8.` | "compare above, **fundamentum 8**" |
| `bon-qsc-q4 [p25-5]` | `Vide supra fundam. 2. et 3.` | "See above, **fundamenta 2 and 3**" |
| `bon-qsc-q5 [p28-3]` | `q. 1. fundam. 1.` | "q. 1, **first ground**" |
| `bon-qsc-q7 [p40-1]` | `in cuius 4. fundam. … in 2. fundam.` | "in whose **4th ground** … in the **2nd ground**" |

**No chunk's `## Notes` records any ruling on this** — it is undocumented drift, not a disclosed
decision, which is what makes it a defect rather than an accepted cost. And **no single chunk could
have caught it**: each of the five chunks holds exactly one site (q4 holds two, and q4's two agree
with each other). It is visible only from the work close, which is what this gate is for.

### The convention was found in the corpus, not invented here

Counted by language block over Vols I–IV rather than by raw grep, because a bare grep cannot tell
an English rendering from the Latin body text it also matches:

| register | `fundamentum N` retained | English-word form | digit-ordinal form |
|---|---|---|---|
| **English APPARATUS halves** | **~135** | 4 | 0 |
| English BODY | ~22 | ~20 | 0 |

**In the apparatus the corpus convention is decisive (~97 %): retain the Latin `fundamentum N`.**
`bon-qsc-q4`'s two sites are already on it. The other three are off it, and **two of the three forms
("ground N", "Nth ground") have ZERO precedent anywhere in the corpus apparatus.**

⚠ **The body register is genuinely mixed corpus-wide (~22 vs ~20) and is NOT this gate's business.**
No body text was touched. The ruling below is scoped to the apparatus, where the corpus actually
has a convention to conform to.

### Repair applied — three sites, four strings

- `bon-qsc-q3 [p16-7]`: "q. 2, ground 1." → "q. 2, **fundamentum 1**."
- `bon-qsc-q5 [p28-3]`: "q. 1, first ground." → "q. 1, **fundamentum 1**."
- `bon-qsc-q7 [p40-1]`: "in whose 4th ground" → "in whose **fundamentum 4**"; "in the 2nd ground XI,
  c. 10, n. 3" → "in **fundamentum 2**, XI, c. 10, n. 3"

⛔ **The DIGITS at `q7 [p40-1]` were not touched and were never in doubt** — that note is the work's
1-vs-4 calibration control (*Quaest. 1, in cuius 4. fundam.*, both glyphs four words apart, settled
at 5×). **The defect was the rendering FORM, not the reading.** No plate work was required, and
none was done.

### ★ RULING 5 (new, this gate) — in the APPARATUS, `fundam. N` → `fundamentum N` / `fundamenta N`

Conform to the corpus apparatus convention. **Scoped to the apparatus register only**; the body
register stays as each chunk built it, because the corpus has no convention there to conform to.
Carry to *de mysterio Trinitatis* and *de perfectione evangelica*.

---

## The four frozen rulings — all four HOLD, verified mechanically across all seven chunks

### 1. *intellectus agens* → "the agent intellect", scoped to the PHRASE — HOLDS, and cleanly

**14 English "intellect(s)" in the seven bodies; all 14 sit inside *agent intellect* or *possible
intellect*; ZERO bare "intellect" anywhere in the work.** q1 6 · q2 11 · q3 1 · q4 37 · q5 6 · q6 9 ·
q7 10 Latin `intellect-` nouns against those 14 English survivals — every other one went to
"understanding."

⚠ **A measurement trap worth recording, because it nearly manufactured a defect:** a first pass
reported "2 bare intellect in q7." Both were false — *the possible* **intellect** and *the* agent
**intellect** carry markdown italic markers *between* the adjective and the noun, which broke the
lookbehind. **A regex that reads English prose has to be written against the MARKUP, not against the
prose.** Same class as this gate's plural miss below.

### 2. *lux* → light / *lumen* → "lumen", with the Ps. 35:10 exemption — HOLDS

Counted by block, Latin against English, over bodies and apparatus separately:

| | La *lux* | En "light" | La *lumen* | En "lumen" |
|---|---|---|---|---|
| bodies, all 7 | 80 | 84 | 30 | 29 |
| apparatus, all 7 | 15 | 13 | 11 | 11 |

Every residual reconciles, and none is a defect:
- **q4 body ±2 is exactly the standing Ps. 35:10 exemption** — *In lumine tuo videbimus lumen* (arg. 15,
  p. 18) → "In thy light we shall see light", two *lumen* deliberately rendered "light", disclosed in
  q4's own `## Notes`. **Verified in place, not assumed from the note.**
- **q6 body +2 "light"** — the two pronoun expansions (*illam* / *illa* → "that light") q6's Notes
  already documented.
- **q3 apparatus, 2 *lux* + 1 *lumen* with neither word in the English** — `[^p14-2]` is a
  variant-reading note (*eiusdem lucis et eiusdem luminis*), and Quaracchi's manuscript variants are
  quoted **untranslated** in the English half. Correct practice, false positive.

⚠ **The second measurement trap, and the more dangerous one:** the first pass appeared to show q5
rendering 4 Latin *lumen* with only 1 English "lumen" — which would have read as ruling 2 failing in a
chunk the shakedown never covered. **It was a missing plural.** The work renders *lumina* /
*luminum* as "**lumens**", and `\blumen\b` does not match it. ★ **A ruling that appears BROKEN in
exactly the chunks a prior gate did not cover is the case to re-measure before believing** — the
prior's blind spot makes a false positive there feel like a finding.

### 3. The `contuit-` family — HOLDS, and q1's known exception is intact

7 Latin `contu-` sites in q4–q6, **7 English "contuit-"**: q4 2/2 · q5 1/1 · q6 4/4. `bon-qsc-q1`'s
single site (*per universalem et plenarium contuitum* → "a universal and full **intuition**") stands
**untouched**, exactly as the shakedown ruled when it DECLINED that repair. Re-verified in place.

### 4. "Quotation boundary" is not a licence class — HOLDS, mechanically

This follows from ruling 1's result rather than needing its own sweep: **a quotation-boundary licence
would have produced a bare "intellect" outside the ratified phrase, and there are zero in the work.**
q7's Dionysius quotation (*nostrum intellectum*) went to "understanding", refusing the licence at the
one site in the work where it would have applied.

### 5. *vacatio* / *quies* — CLOSES AS UNTESTABLE, confirmed at the close

Carried from the shakedown. Six consecutive chunks with the noun *quies* never once present and
*vacatio*/*vacare* absent from the work entirely. **Not untested — untestable on this text.** Carry to
*de mysterio Trinitatis* / *de perfectione evangelica*; do not re-open it here.

---

## Pass 1 — `[?]` flag resolution (pp. 3–43)

`tools/check-live-flags.py` — the gate's instrument, not `grep`. **ZERO live flags in all seven
`bon-qsc-*` chunks**, as each chunk claimed and as this gate verified rather than accepted.

Corpus baseline: **237 occurrences (vol1 150 · vol2 9 · vol3 2 · vol4 66 · vol5 10)** — identical to
the *septem donis* and *decem praeceptis* gate baselines. All ten vol5 occurrences are the
pre-existing ACCEPT-ILLEGIBLE printed defects already itemized (`bon-brev-p6-c13` ×2, `bon-hex-c15`
×2, `bon-hex-c19` ×2, `bon-hex-c22` ×4). **None in `scientia-christi`, none new.** Seven consecutive
Tier-2 chunks with nothing to resolve; no 600 dpi re-extraction needed.

---

## Pass 2 — full-corpus style/formatting scan

`polish-style-scan.py`, no filter, **2,089 chunks scanned**:

- **`bon-qsc-q1`–`q7`: CLEAN.** No `PAIR`, `V5LABEL` or any other class fired in this work.
- Corpus-wide: **11 issues / 6 chunks, all pre-existing, none in this work** — the identical 11
  carried since the *septem donis* gate (`bon-hex-c23`'s one deliberate `V5LABEL`; the 10-entry
  `PAIR` residue across `III-d31-a3-q3`, `III-d32-a1-q2`, `III-d5-a2-q4`, `IV-d14-p2-a2-q1`,
  `IV-d16-p2-a2-q2`). **Count and membership unchanged.**

★ **Denominator reconciled, not assumed** — three tools report three numbers and all three are right:
**2,090** files on disk (top-level `.md` in vol1–vol5, what `check-live-flags.py` scans) · **2,089**
scanned by `polish-style-scan.py` and `build-citations.py`, whose `bon-*.md` glob correctly drops
`vol1/punch-list.md` · **2,088** built by `build-content.mjs`, which additionally excludes
`vol1/bon-sent-I-proleg.md` under a documented guard. **No silent skip at any step.**

---

## Pass 3 — cross-chunk boundary integrity, all SIX interior boundaries

The boundary set is fixed: **q1 3–6 · q2 6–10 · q3 10–16 · q4 17–27 · q5 27–32 · q6 32–37 · q7
37–43** — six interior boundaries, **five on shared printed pages (6, 10, 27, 32, 37) and one a clean
leaf edge (17)**.

### (a) Grammatical continuity — all six PASS

Verified against the actual Latin on both sides, not against the chunks' own Notes. `seam-screen.py
--volume 5` independently reports this work's five shared-leaf boundaries among vol5's 113 mid-page
boundaries, with **0 tail-not-terminal suspects corpus-wide**.

| # | boundary | ceding chunk's close | receiving chunk's open |
|---|---|---|---|
| 1 | q1→q2, p. 6 | *…patet responsio ex principali solutione*[^p6-6] — terminal | *Supposito, quod Deus cognoscat infinita, quaeritur…* |
| 2 | q2→q3, p. 10 | *…in nullo egreditur extra rationem cognoscentis et cognoscibilis.* | *Supposito, quod Deus cognoscat res per similitudines exemplares…* |
| 3 | q3→q4, p. 17 | q3 closes on **p. 16** under an ornamental rule — clean leaf edge | `QUAESTIO IV.` full-measure at the head of p. 17 |
| 4 | q4→q5, p. 27 | *…qui est summus amator aeternitatis.* | *Postquam habitum est de sapientia Christi secundum quod Verbum…* |
| 5 | q5→q6, p. 32 | *…Et sic patet responsio omnium obiectorum.* | *Supposito, quod anima Christi sit sapiens…* |
| 6 | q6→q7, p. 37 | *…non tamen totaliter comprehendit.* | *Quaeritur, utrum anima Christi comprehendat omnia…* |

**No cascade-merge splice defect anywhere.** Every ceding close is grammatically and semantically
terminal; every receiving open is a fresh *Quaeritur* / *Supposito* question opener.

### (b) Footer-note accounting at all six boundaries — all PASS, split matches the frozen record exactly

Every `[^pNNN-n]` label extracted directly from the built files and cross-tabulated by owning chunk —
**not** read off any chunk's prose:

| page | owned by | split | ratio |
|---|---|---|---|
| p. 6 | q1, q2 | nn. 1–6 q1 / nn. 7–9 q2 | **6/3** |
| p. 10 | q2, q3 | nn. 1–7 q2 / n. 8 q3 | **7/1** |
| p. 17 | q4 only | nn. 1–10 all q4 | **leaf edge** |
| p. 27 | q4, q5 | n. 1 q4 / nn. 2–8 q5 | **1/7** |
| p. 32 | q5, q6 | n. 1 q5 / nn. 2–9 q6 | **1/8** |
| p. 37 | q6, q7 | nn. 1–3 q6 / nn. 4–7 q7 | **3/4** |

**Matches `CLAUDE.md` § SCIENTIA CHRISTI at every one of the six, digit for digit.** ⭐⭐ **And the
frozen finding survives its own close: NO TWO OF THE SIX SPLIT ALIKE** — 6/3 · 7/1 · leaf edge · 1/7 ·
1/8 · 3/4, with pp. 27, 32 and 37 sharing one printed *shape* (a closing reply across the top band of
both columns, then a full-measure `QUAESTIO` heading mid-leaf) and yielding three different ratios.
**Count the register; never infer the split from the shape.**

`check-vol5-apparatus.py` reports **all 41 pages of the span with a contiguous `1..N` register and
`ok` status, and no page left PENDING** — p. 37's hand-off, the last one open in the work, cleared
with q7. **No note lost, duplicated or misnumbered.**

### (c) The chunks' own documentation against the built text

Each boundary was re-derived by the **receiving** chunk from the plate before being adopted (q2
re-derives boundary 1, q3 boundary 2, q5 boundary 4, q6 boundary 5, q7 boundary 6) — no tally copied
forward, the failure mode the *septem donis* gate warned about. **This gate's independent extraction
in (b) confirms all six against file contents, not against the chunks' claims about themselves. No
discrepancy found.**

---

## Supplementary sweeps

### Digit-multiset sweep — all **323** apparatus entries

Latin half's digit multiset against the English half's, every entry in the work.

**Before the Defect 1 repair: 4 mismatches, 0 defects. After: 3 mismatches, 0 defects.** All three
surviving are false positives, and — the point worth carrying — **not one of them is the
roman-numeral class that produced both of the *decem praeceptis* gate's false positives:**

- `q1 [p5-6]` and `q4 [p20-5]` — Latin `83 Qq.` → English "*Eighty-three Questions*"; the numeral is
  spelled out because the title is conventionally given in words. **Number-spelled-as-title class.**
- `q4 [p23-3]` — Latin `S. 1. q. 89. a. 1.` → English "*Summa* I, q. 89, a. 1"; an Arabic `1` rendered
  as the roman `I` for the Prima pars. **The exact INVERSE of the decem-praeceptis class** (there,
  roman in Latin → Arabic in English).

★ **The sweep's false-positive families are work-dependent.** Three classes here, none shared with
the previous work's two. **Never carry a prior gate's false-positive list forward as a filter** —
classify this work's mismatches from scratch, or a real defect hides inside an inherited "known" bucket.

### `build-citations.py`

Corpus **22,153 ledger records; QA total 201 dangling — UNCHANGED from the *decem praeceptis* gate's
201.** **`scientia-christi` contributes ZERO dangling cross-references and zero out-of-range
scripture**, and no `bon-qsc-*` chunk appears in the "no citation record" section. 41 printed pages
and 323 apparatus entries added not one dangling reference — the strongest citation result of any Vol
V work to date.

### ⭐⭐ CLOSING THIS WORK RETIRED SIX FORWARD-REFERENCES IN FOUR ALREADY-DEPLOYED WORKS

The committed `index/citations.tsv` was stale (2,086 chunks — it predates `q5`). Rebuilding it added
**73 records** from q5/q6/q7 and, more importantly, **resolved six cross-references in four earlier
Vol V works that had been unresolvable placeholders** (`tom5:pNN`, resolution class `forward`) because
their target pages did not yet exist in the corpus:

| citing chunk | reference | now resolves to |
|---|---|---|
| `bon-brev-p1-c6 [p215-5]` | *supra pag. 39, nota 7* | `bon-qsc-q7` |
| `bon-hex-c12 [p386-2]` | *pag. 35, nota 2* | `bon-qsc-q6` |
| `bon-hex-c20 [p426-4]` | *supra pag. 37, nota 7* | `bon-qsc-q6`+`q7` (page-multi) |
| `bon-hex-c20 [p426-6]` | *ibid.* (anaphor) | `bon-qsc-q6`+`q7` (page-multi) |
| `bon-itin-c2` | *pag. 33, nota 5* | `bon-qsc-q6` |
| `bon-red` | *supra pag. 29, nota 6* | `bon-qsc-q5` |

⚠ **This is deploy-relevant, and it is the reason the regenerated index belongs in the gate commit.**
The Breviloquium, Hexaemeron, Itinerarium and De reductione are **all already live**, and six of their
apparatus cross-references currently resolve to nothing in production. **They start working the moment
this work deploys** — the fix ships with `scientia-christi`, not with those works.

★ **The general lesson: a work's citation value is not only what IT cites, but what the corpus can
finally cite INTO it.** A forward-reference is retired by the arrival of its target, so the gate that
closes a work should always rebuild the index and look for what *other* works just gained.

The work's only two rows anywhere in the QA report are in **unresolved anaphora** (`bon-qsc-q3` and
`bon-qsc-q4`, one `ibid` each in the Latin body) — the pre-existing corpus-wide behaviour class
(~180 instances), not a defect and not this work's to fix.

⚠ **`bon-qsc-q2 [p8-7]`'s known Quaracchi-side slip is NOT in that count and stays as-is** — Quaracchi
prints *cfr. supra pag. 1, nota 2* where p. 1 is the shared half-title carrying no notes and the locus
is p. 3 n. 2. Transcribed exactly as printed, logged at q2, non-blocking, disposed exactly like
`bon-praec-c6`'s dangling cross-ref.

---

## Pass 4 — disk: ⚠ **NOT DONE — BLOCKED, AWAITING WILSON**

Identified and verified, **not deleted**: the deletion was refused by the session's permission
classifier and was deliberately not worked around.

- `raw/vision/vol5/p-037.png` … `p-043.png` — **7 files, 23 MB**
- `/tmp/colcrop/*` — **62 files, 115 MB**

**~138 MB to reclaim.** Both sets are q7's leftovers **only** — every one of the 69 files is a
pp. 37–43 artifact, confirmed file by file; nothing belongs to another page or work. Both paths are
gitignored (`git check-ignore`: `.gitignore:9:raw/vision/`) and **zero files are tracked**, so
neither deletion can touch anything under version control. Both are fully regenerable from
`raw/doctorisseraphic05bona.pdf` (confirmed present, 75 MB) via `extract-pages.py --volume vol5
--dpi 450` + `colcrop.py`.

⛔ **This is the only outstanding item in the gate.** It does not block the deploy — no built content
depends on it — but the plates should not be left lying around against the work's own
"plates are deleted after each chunk" discipline.

---

## Verification suite at the gate (all re-run AFTER the Defect 1 repair)

| check | result |
|---|---|
| `check-live-flags.py` | **0 live flags** in `bon-qsc-*`; corpus 237 (vol1 150 · vol2 9 · vol3 2 · vol4 66 · vol5 10), unchanged |
| `check-vol5-apparatus.py` | **137 chunks / 2,776 entries, all passed**; pp. 3–43 all `ok`, contiguous, none PENDING |
| `check-vol5-census.py` | **rosters agree 137/137**; 190 runovers (169 gutter-crossing, 21 page-crossing) |
| `polish-style-scan.py` | this work **CLEAN**; corpus 11 pre-existing issues / 6 chunks, unchanged |
| `seam-screen.py --volume 5` | 113 mid-page boundaries incl. this work's 5 shared leaves; **0 tail-not-terminal suspects** |
| digit-multiset sweep (323 entries) | **3 false positives (three distinct classes), 0 defects** |
| `build-citations.py` | this work **0 dangling**; corpus QA total **201, unchanged** |
| direct footer-note extraction, all 6 boundaries | split matches the frozen record exactly at all six |
| `build-content.mjs` | **11 books, 2,088 questions, 2,088 translated** — builds clean after the repair |

---

## What remains open (none blocking, none of it this work's)

Carried unchanged from the *decem praeceptis* gate:

1. A scripture `ibid. <ch>, <v>` keeps the right book but the stale verse (`bon-don-c7`, p. 492 n. 4).
2. `bon-hex-c23`'s one non-page-qualified apparatus label (`51`) — deliberate, documented.
3. The 5-chunk `PAIR` residue in Vols III–IV.
4. Vols I and IV's `[?]` backlog — 150 and 66 occurrences; a scoped job.
5. Vols II–IV have never been swept for the Vol I cross-reference digit class.
6. The About page's "What Is Known to Be Wrong" — Wilson's to frame.
7. `d30-a1-q3`'s transposed `s`-series labels · `d37-p2-dubia` `[^6]`'s merged notes · Book IV
   `d. 2. p. I.` cite · `prol-comm` p. 24 n. 2.
8. `bon-praec-c6 [p528-9]`'s dangling `IV. Sent. d. 25. a. 4. q. 3.` — as printed, non-blocking.
9. The Vol I page-gap hunt stays PARKED. Reopening trigger: a reader reports a gap.

Added by this work, both non-blocking and both transcribed-as-printed:

10. `bon-qsc-q2 [p8-7]`'s *cfr. supra pag. 1, nota 2* — Quaracchi-side slip, true locus p. 3 n. 2.
11. The `contuitum`/"intuition" site at `bon-qsc-q1` — **ruled upon at the shakedown, not open.**

---

## The gate's own finding

**A gate's real yield is what no chunk could see from inside itself.** The four register rulings all
held, every boundary claim held digit for digit, the citation ledger took 41 pages without a single
dangling reference — and the one defect found was invisible at chunk scale by construction: five
sites, five renderings, **one per chunk**, each locally defensible and collectively incoherent. The
shakedown gate could not have caught it either, because at p. 27 only two of the five sites existed
and they were q4's two, which agree with each other and with the corpus.

⭐ **The methodological finding is about the gate's own instruments, and it fired twice in one
session.** Both near-misses were the measuring tool, not the text: a regex that could not see italic
markup inside a ratified phrase, and one that could not see an English plural. **Both would have been
reported as ruling violations in exactly the three chunks no prior gate had audited** — where a false
positive is most believable, because the blind spot makes it feel like the expected place to find
something. The rule that saved both: **when a ruling appears to break precisely where you had no
prior coverage, re-measure the instrument before believing the finding.**

**Verdict: ONE DEFECT, FOUND AND REPAIRED. The text is otherwise clean.** Three apparatus strings
changed across three files; no body text touched; no plate work required. **The work is ready to
push and deploy, pending Wilson's go-ahead — and Pass 4's ~138 MB deletion is still owed.**
