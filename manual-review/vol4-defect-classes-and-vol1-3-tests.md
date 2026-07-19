# Vol IV defect classes → cheap tests for Vols I–III

**Written 2026-07-19, after d.45–d.47.** Vol IV surfaced a run of defect classes that the three
guard-rail audits cannot see. Every one of them is a *plausible* pre-existing defect in Vols I–III,
which are **published**. This file is the inventory plus, for each class, the cheapest test that
would tell us whether it reaches back — so we can decide what to sweep without committing to a
full re-verify of 1,286 published chunks.

**Status 2026-07-19 — steps 1–3 run.**
* **§3 (missing questions) — RUN, 0 findings.** `tools/audit-promise-vs-delivery.py`.
* **§4 (dubia count) — RUN, 0 findings, but Vol III has ZERO coverage.** `tools/audit-dubia-count.py`.
* **§2 (gutter parity) — RUN, and it FAILED TO EXONERATE. The defect reaches Vols II and III,
  confirmed visually.** See `vol4-column-gutter-parity.md`. **This is now the live concern.**
* §1 notes/page calibration run. **§1b, §5 and §7 NOT run.**
No repairs are proposed anywhere in this file.

---

## The common shape

Every class below produces a **well-formed but wrong** result. That is why the audits miss them:
`audit-paraphrase`, `audit-headers` and `audit-apparatus-count` all compare *the chunk* against
*the raw OCR*, so they can only see defects where the chunk is the deficient side. When the **raw**
is what is missing or garbled, the chunk faithfully reproduces a hole and every audit reports clean.

Three of the classes below (§1, §2, §3) are of exactly that kind.

---

## §1 — OCR footer-block dropout ★ HIGHEST PRIORITY

**Found:** d.47, 2026-07-19. **Status: NEW, not previously recorded anywhere.**

The IA djvu OCR is missing the **entire apparatus** of printed pp. **972, 973, 975, 979, 981** —
the raw text runs from the last body line straight to the next `QUAESTIO` header with no footer at
all — plus a truncated block on p.980 and a dropped run-over on p.977. Five whole pages in a single
distinction. All were recovered from the 450 dpi footer bands.

**Why no audit sees it:** `audit-apparatus-count` compares raw footer-openers against chunk `[^N]:`
defs. When the raw has zero, the expected count is zero, and a chunk with zero apparatus scores a
perfect match. **The failure is invisible by construction.**

**Why it probably reaches back:** the body superscript markers survive in the OCR even when the
footer block is gone, so an OCR-first writer places anchors that bind to nothing — or, worse, silently
renumbers the surviving notes to fit. This is a strong candidate explanation for the **J4 apparatus
backlog**, specifically the 7 chunks whose English body has zero apparatus markers and the
partial-anchor cases.

### Test 1a — notes-per-page ratio (RUN 2026-07-19, results below)

Pure metadata: `apparatus defs ÷ distinct printed_pages`, per distinction. No bands, no raw, seconds
to run. Calibrated against d.45/d.46/d.47, which are band-verified and therefore trustworthy:

| band-verified | pages | defs | notes/page |
|---|---|---|---|
| IV d.45 | 18 | 149 | 8.3 |
| IV d.46 | 16 | 122 | 7.6 |
| IV d.47 | 14 | 116 | 8.3 |

Per-volume distribution over **fully**-Tier-2 distinctions:

| vol | n | median | p10 | min | max |
|---|---|---|---|---|---|
| I | 47 | 7.5 | 6.3 | **4.6** | 12.1 |
| II | 44 | 7.2 | 6.7 | 5.9 | 8.6 |
| III | 40 | 8.0 | 7.4 | 7.1 | 8.9 |
| IV | 47 | 7.8 | 6.7 | 5.7 | 9.3 |

Lowest-ratio distinctions, all fully Tier 2 — **the screen's candidate list**:

```
vol1 d.38  16pp  74 defs  4.6      vol2 d.41  24pp 142 defs  5.9
vol1 d.39  19pp  98 defs  5.2      vol1 d.35  20pp 124 defs  6.2
vol4 d.19  19pp 109 defs  5.7      vol4 d.34  15pp  93 defs  6.2
vol1 d.37  34pp 201 defs  5.9      vol2 d.30  28pp 177 defs  6.3
```

**Read this as a screen, not a verdict.** Genuine variation is real: a page of dense *littera* carries
fewer notes than a page of argument, and Vol I is a different physical layout from II–IV. The tight
per-volume medians (7.2–8.0) are what make the low tail interesting. **Vol I d.38 at 4.6 and d.39 at
5.2 sit far below every band-verified baseline and below their own volume's p10 — those two are worth
one spot-check each against the printed page.** That is ~2 pages of band reading to find out whether
this class reaches Vol I at all, which is the cheapest possible answer to the question.

Note also that **Vol III's floor is 7.1** — the tightest, highest distribution in the corpus. That is
weak positive evidence that Vol III (the most recently written, and live) is *not* broadly affected.

### Test 1b — direct raw-side detector (not yet built)

Stronger and still cheap: for each printed page, ask whether the raw range contains **any** footer-opener
pattern while the body carries superscript markers. Body-markers-present + zero-footers is the exact
dropout signature, and unlike 1a it localises to the page rather than the distinction.

**Blocked for most of the corpus — see §7.** It needs per-chunk `line_start`/`line_end` to map pages
to raw ranges, and those are missing from 246/464 Vol II and 368/412 Vol III Tier-2 chunks.

---

## §2 — Column-gutter parity (band mis-split)

**Found:** d.46, 2026-07-18. Written up in `vol4-column-gutter-parity.md`.

`colcrop.py`'s default split is wrong for every page in the d.46–d.47 range; the true gutter alternates
by printed-page parity (odd ≈1480–1585, even ≈2096–2201). The even-page failure is loud. **The odd-page
failure is silent** — it shaves the right column's first character off every line, and a careful writer
reconstructs it into plausible Latin. Three of four d.46 batch-1 writers reported clean runs on clipped
pages.

**Reaches back?** Vol I is single-column — **not applicable**. Vols II and III are the same two-column
edition as IV, so **applicable in principle**, and every chunk in them was written against a guessed
split.

### Test 2 — measure, don't re-read

Run the gutter-measurement snippet (in the parity write-up) across a **sample** of Vol II and Vol III
pages and compare the measured value to the split those sessions actually used (1660 for vol2/vol3 per
CLAUDE.md). Cheap: extraction + measurement only, no model reading, no band reading. If the measured
gutters cluster near 1660, the volumes are fine and this closes. If they alternate by parity, it does
not close, and the follow-up is a sampled re-verify — sized only after the measurement says so.

**Do the measurement before assuming anything.** It is the one test here that can *exonerate* two whole
volumes for a few minutes of compute.

### ✘ RUN 2026-07-19 — DID NOT EXONERATE. Both volumes are affected.

Measured against the 1660 default those sessions used: **Vol II odd pages ≈1539 (121 px too far
RIGHT), Vol III odd pages ≈1533 (127 px too far RIGHT)**. Too-far-right is the **silent** direction —
the R band starts inside the right column and shaves the opening characters off every line.
Confirmed by eye on Vol III p.601: `nomen`→`iomen`, `fides`→`ides`, `perfectio`→`ectio`,
`credit`→`redit`. 1–4 characters lost per line, and the residue still reads as plausible Latin.
Full write-up and the suggested sampling step in `vol4-column-gutter-parity.md`.

---

## §3 — Garbled QUAESTIO headers hiding whole questions

**Found repeatedly:** d.42 `a3-q3`, d.46 `a2-q4` (`QUAESTiO IV.`), d.47 `a2-q3` (`QUAESTIO ni.`),
d.48 `a2-q3` (`QUAESTIO lU.`), d.49 s2-a4-q2 (`QU.\ESTIO II.`). **Five lost questions in nine
distinctions.** In each case the sibling chunk's range silently swallowed the missing one.

**Why no audit sees it:** `audit-headers` counts headers in the raw with the same regex family that
missed the garbled header in the first place, so raw and chunk are wrong in the same direction.

### ✔ RUN 2026-07-19 — `tools/audit-promise-vs-delivery.py` — **0 findings, all four volumes**

Built and run. **No missing question was found anywhere in the corpus.** Two independent checks:

**Check A — GAP in the delivered question sequence.** Needs only chunk filenames. This is the exact
signature of the mid-article losses (d.47 a2-q3 left disk holding q1, q2, q4).
**Coverage 100% — 436/436 articles across all four volumes. Zero gaps.** This is a *complete*
result, not a sample: no article anywhere in Vols I–IV has a hole in its question sequence.

**Check B — running head outruns the delivered maximum.** Catches losses at an article's *tail*
(d.46 a2-q4, d.42 a3-q3, d.49 s2-a4-q2), which leave no gap. Uses the running head as an
independent witness: Quaracchi names the structural position on nearly every page, so a question
spanning any page top leaves a trace even when its own header is garbled beyond grepping.
**Zero findings within coverage — but coverage is partial:**

| vol | articles | with running-head witness | blind |
|---|---|---|---|
| I | 87 | 45 (52%) | 42 |
| II | 119 | 90 (76%) | 29 |
| III | 81 | 67 (83%) | 14 |
| IV | 149 | 120 (81%) | 29 |

**The blind spots are structured, not random: they are overwhelmingly `a1`**, the first article of a
distinction — its questions often begin on the page carrying the `DISTINCTIO` header, whose running
head reads `DIST. N.` or `DIST. N. DIVISIO TEXTUS` with no ART/QUAEST component. A tail loss in an
`a1` would be invisible to both checks (Check A only sees *within* an article). Full blind-spot list
is reproducible from the tool.

**Validation.** The detector was validated against a known true positive before being trusted: with
`d47-a2-q3` temporarily hidden it reported
`d.47 a.2 disk=[1,2,4] — GAP q[3] missing`, and reported it again after the parser fix below.

**A first-run false-positive worth recording.** The initial version flagged 6 positions, *all of them
artifacts of my own numeral parsing*: `ART. l.` (lowercase L for I) parsed as Roman **50**,
`ART. UNICUS` was unhandled, and bare page numbers in numeral-less heads (`... QUAEST. 131`) parsed
as question numbers. Fixed with slot-aware parsing — articles/questions never exceed ~12 in this
corpus, so out-of-range values are now reported as unparseable rather than guessed. **430 running
heads corpus-wide remain unparseable and are listed, never guessed**; recovering some of them is the
cheapest way to raise Check B's coverage.

**What this does and does not settle.** It settles that the *mid-article* loss class — the one that
hit d.47 and d.48 — does not exist anywhere in Vols I–III. It does **not** settle tail losses in the
114 unwitnessed articles. Raising that would need either the unparseable-head recovery above or the
`line_start` backfill (§7).

### Test 3 — the promise-vs-delivery count-check, mechanised (original design note)

This is the check that caught all five, and it is **fully mechanisable from the raw alone**:
every article opener states its own question count (*"Et circa hoc quaeruntur quatuor"*), and every
question opens with an ordinal (*Primo/Secundo/Tertio/Quarto quaeritur*). Compare the **promised**
count against the **delivered** chunk count per article, corpus-wide.

Needs only the raw plus chunk ids — **no line ranges, no bands.** Runnable against Vols I–III today.
**This is the highest value-per-effort test in this document**: it targets outright missing text rather
than degraded text, and a hit is unambiguous — there is no judgement call about whether a question exists.

---

## §4 — Cased `DuB.` undercounting dubia

**Found:** d.45 — 9 dubia printed, only 3 greppable; six were cased `DuB.` and invisible.

### ✔ RUN 2026-07-19 — `tools/audit-dubia-count.py` — 0 findings, but read the coverage

Each dubia chunk compared against **its own raw line range**, case-insensitively. **0 findings.**
Coverage is the real story: **vol1 55/55 (100%) · vol2 17/49 (35%) · vol3 0/42 (0%) · vol4 29/63 (46%)**.
**Vol III is entirely unexamined** — it has no line ranges at all, so this is not a clean result for
Vol III, it is *no* result. Four separate false-positive batches were found and fixed before the
output was trusted (drifting distinction attribution; three different chunk header conventions —
`Dub. I.`, `Dub. I`, `Dubium I.`; and Vol I's two raw files having file-specific line numbers).
Also established that **d.48 has SEVEN dubia**, not the three that are greppable.

---

## §5 — Article PRAENOTATA dropped at the header↔QUAESTIO seam

**Found:** d.42 Art. I — the definition, species and opinions on p.868 fell between the `ARTICULUS`
header and `QUAESTIO I` and were dropped entirely. d.47 confirmed the same structural spot carries
Article II's whole four-question listing, which the TRACTATIO does *not* duplicate.

### Test 5 — does each article's q1 contain its article header?

Grep every `aN-q1` chunk body for its `ARTICULUS` header and the opener text that should precede
`QUAESTIO I`. A q1 that jumps straight to the question is a candidate dropout. Pure text, runnable
today, though it needs a tolerance for distinctions that legitimately chunk the opener elsewhere.

---

## §6 — Marker binding order: column vs reading

**d.20 lesson:** Quaracchi numbers footers in **column** order while anchors fall in **reading** order,
so a body legitimately runs 1, 3, 2, 4 — and relabelling by position corrupts the text.
**d.47 finding:** on pp.973, 979 and 980 the markers bind in **straight reading order**.

So the order is **not constant across the corpus**, and neither rule can be applied blind. The a1-q3
writer noted that content-matching alone would have mis-bound two near-identical John 3 citations on
p.973 had the order been assumed.

### Test 6 — no cheap mechanical test

Honest answer: this one cannot be screened from text. It is caught only by binding each anchor to the
note whose *content* matches, per page, at band time. The mitigation is procedural, not detective:
**state in CLAUDE.md that the order varies and must be determined per page** rather than presented as
the d.20 rule. Worth doing regardless of any sweep.

---

## §7 — Prerequisite: missing `line_start` blocks the raw-range tests

Tier-2 chunks with no `line_start` frontmatter:

| vol | missing / total Tier-2 |
|---|---|
| I | **2 / 410** |
| II | 246 / 464 |
| III | 368 / 412 |
| IV | 319 / 594 |

Promotion sessions dropped the range fields (the known `rechunk_d23.py` bug, generalised). This blocks
**Test 1b** and any future page↔raw mapping on most of Vols II–IV. Vol I is effectively complete and
can be tested today.

Backfilling ranges is mechanical — match each chunk's opening line against the raw — and would unlock
the sharper detectors. Worth costing separately before committing to it.

---

## Suggested order, cheapest and most decisive first

1. **§3 count-check** across Vols I–III — mechanical, unambiguous hits, targets *missing text*.
2. **§4 `DuB.` re-grep** — minutes, same category of loss.
3. **§2 gutter measurement** on a sample of Vols II/III — can exonerate two volumes outright.
4. **§1a spot-check** of Vol I d.38 and d.39 against the printed page — ~2 pages to learn whether the
   footer-dropout class reaches Vol I at all.
5. **§6 CLAUDE.md wording fix** — no sweep, just stop teaching a rule that is only sometimes true.
6. **§7 line_start backfill** — only if 1–4 turn up enough to justify the sharper tests.

Steps 1–4 are all screens and measurements: no repairs, no rewrites, and each one can come back
"clean, this does not reach back," which is the outcome worth buying first.
