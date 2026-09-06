# Vol V — *QD de mysterio Trinitatis*: SHAKEDOWN GATE (2026-09-06)

The first of this work's two gates, fired at the close of **`bon-qmt-q2-a2`** per the frozen cadence
(trigger 3 — a shakedown at the first structural seam ~15–25 printed pages in). Scope:
**`bon-qmt-q1-a1` … `bon-qmt-q2-a2`, printed pp. 45–68, 24 leaves, 176 apparatus entries.**
⚠ The seam is **p. 68, not p. 67**: `bon-qmt-q2-a2` measured the article's end on the plate and found
the index-derived span short by a leaf, and the gate moved with it (24 printed pp., still inside
trigger 3's 15–25).

**Result: ZERO corpus defects in scope.** Both questions the chunks carried in are answered here from
evidence the chunks could not see, and pass 3 turns up **one new docket item outside this work**.
This is the opposite profile to the *scientia Christi* shakedown, which found three defects — and the
reason is worth naming: **that gate's defects were register claims in `## Notes` that the text did not
keep, and this span's register claims were verified against anchor-aligned segments *before* they were
written into the notes.** The instrument that gate built was used prospectively here.

---

## Pass 1 — `[?]` flag resolution: NOTHING TO RESOLVE IN SCOPE, verified not assumed

`tools/check-live-flags.py` (not `grep` — the earned instrument): **237 live occurrences corpus-wide,
of which `bon-qmt-*` contributes ZERO.** Per volume: **vol1 150 · vol2 9 · vol3 2 · vol4 66 · vol5 10.**

**Unchanged from the *scientia Christi* shakedown baseline in every volume**, so nothing this work has
built has added a flag and nothing outside it has moved. vol5's ten remain the same pre-existing ones
in already-deployed chunks — `bon-brev-p6-c13` (2), `bon-hex-c15` (2), `bon-hex-c19` (2),
`bon-hex-c22` (4). **Recorded, not fixed: this gate authorises no edit outside `bon-qmt-*`.** Vols I
and IV remain the known scoped backlog.

## Pass 2 — style/formatting audit, full corpus

`polish-style-scan.py` over **2,093 chunks — 11 issues across 6 chunks, ZERO in scope.** vol5 alone:
1 issue, and it is not this work's.

Out of scope, recorded not fixed — **identical to the last three gates' lists, item for item**:
- **`bon-hex-c23` `[V5LABEL]`** — apparatus label `[^51]`, not page-qualified. Deliberate and
  documented in that chunk's own `transcription_status`. The Hexaemeron is closed and deployed.
- **10 `[PAIR]` issues across 5 chunks in Vols III–IV** — the known **J4 class-B residue** (orphaned
  defs): `III-d31-a3-q3`, `III-d32-a1-q2`, `III-d5-a2-q4`, `IV-d14-p2-a2-q1`, `IV-d16-p2-a2-q2`.

## Pass 3 — boundary integrity sweep

**Every leaf pp. 45–68 is contiguous 1..N with no gap, no double-claim and no unowned page**, agreeing
with `KNOWN_TOTALS` on all twenty-four leaves. p. 68 is correctly reported as a legitimate PENDING
(n. 1 owned, nn. 2–5 forwarded), not a GAP. Per-chunk: **q1-a1 54 · q1-a2 53 · q2-a1 29 · q2-a2 40 =
176 entries**, La/En paired throughout, and the per-leaf register sums to the same 176 independently.

**Four interior boundaries, counted by hand — and like the *scientia Christi* they take THREE shapes:**

| boundary | shape | register |
|---|---|---|
| q1-a1 \| q1-a2 | **mid-leaf, p. 51** — Art. II opens full measure at ~72 % | **SPLIT 5 / 1** — n. 6 forwarded |
| q1-a2 \| q2-a1 | **LEAF EDGE, p. 58 → 59** — Art. II closes two-fifths down p. 58's right column, the rest white | **does NOT forward** — q1-a2 owns all seven of p. 58, q2-a1 owns all five of p. 59 |
| q2-a1 \| q2-a2 | **mid-leaf, p. 63** — Art. II full measure below both columns | **SPLIT 2 / 8** |
| q2-a2 \| (q3-a1) | **mid-leaf, p. 68** — Quaest. III full measure on the leaf | **SPLIT 1 / 4** — nn. 2–5 PENDING |

★★ **THE LEAF-EDGE BOUNDARY IS THE ONE THAT WAS MEASURED, AND THAT IS THE FINDING.** p. 58 is the
exact shape `bon-qmt-q2-a2` later discovered the index gets wrong — an index span whose last page is
simply the page the next heading falls on. Here it is right, **and it is right because `q1-a2` put the
p. 498 rule to the plate rather than to the index**: it recorded that no part of Quaestio II stands on
p. 58 and that `QUAESTIO II.` opens at raw L18089 on p. 59. ⛔ **A leaf-edge seam is the class; being
measured is what makes it safe.** Do not infer a boundary's shape or its split ratio from the last one.

### ▶ The span-end check the chunk asked the gate for — DERIVED, and it opens a docket item

`q2-a2` asked whether any earlier Vol V chunk had been built to an index span's last page without
measuring it. Mechanical sweep of every consecutive-chunk pair in vol5: **17 leaf-edge seams exist**
(chunk N ends p. X, chunk N+1 begins p. X+1). **Twelve carry explicit boundary language in their
`## Notes`; five carry none:**

| seam | pages |
|---|---|
| `bon-brev-p2-c12` \| `bon-brev-p3-c1` | 230 → 231 |
| `bon-hex-c1` \| `bon-hex-c2` | 335 → 336 |
| `bon-hex-c23` \| `bon-hex-scholion` | 449 → 450 |
| `bon-don-c1` \| `bon-don-c2` | 461 → 462 |
| `bon-don-c2` \| `bon-don-c3` | 467 → 468 |

⚠ **This is a docket item, not a defect claim.** Absence of boundary language is not evidence of an
unmeasured span, and all five sit in works that are closed and deployed; **no edit is authorised
here.** ★ What makes it worth docketing is that the failure mode is **silent**: a span short by a leaf
loses a page of body and its share of a footer register, and the chunk still parses clean, passes the
apparatus contiguity check, passes the census and passes the style scan — as `q2-a2` proved. **The
settlement is cheap — one plate look per seam, asking only whether the outgoing unit's body reaches
the top of the incoming leaf** — and it belongs to those works' own next boundary, not to this gate.
⛔ In-scope seams: p. 58 measured (above); the *scientia Christi* p. 17 leaf edge was measured at that
work's shakedown. **Both in-work leaf edges in Vol V are accounted for.**

### ★ Two checked negatives, both mechanical

**The corpus denominator reconciles at all three stages.** Disk carries **2,094 `.md`** under
`vol1…vol5`; the scanners see **2,093** and `build-content.mjs` builds **2,092**. Both gaps are
accounted for and neither is a silent skip: `vol1/punch-list.md` is not a chunk, and
`vol1/bon-sent-I-proleg.md` is excluded **deliberately and by a documented guard** in
`build-content.mjs`. Reconciled 2092 + 1 + 1 = 2094.

**The digit-multiset sweep across all four chunks returns three mismatches and all three are the
documented false-positive class** (an ordinal correctly spelled as a word, and a title): `q1-a1`
p. 46 n. 1 `pro *minori* 3. arg.` → "for the *minor* of the third argument"; `q1-a2` p. 53 nn. 1 and 4
`83 Qq.` → "*Eighty-three Questions*". **No entry loses or gains a digit between its halves.**

## Pass 4 — disk: **DONE, ~663 MB reclaimed**

`raw/vision/vol5/` (34 plates, **104 MB**) and `/tmp/colcrop/` (293 crops, **559 MB**) deleted on
Wilson's explicit OK, both fully regenerable from the gitignored PDF via `extract-pages.py` +
`colcrop.py`. ⚠ **The vol5 plates are gone again — re-extract pp. 68–73 before `q3-a1`**, and measure
that span's END on the fresh plate before extracting the rest. `raw/vision/vol1/` is untouched
(different artifact, out of scope).

---

## Verification suite at the gate

`check-vol5-apparatus.py` **141 chunks / 2,952 entries, all checks passed** · `check-vol5-census.py`
**rosters agree 141/141**, 199 runovers (178 gutter-crossing, 21 page-crossing) ·
`polish-style-scan` **2,093 chunks, ZERO issues in scope** · `check-live-flags.py` **237 corpus-wide,
`bon-qmt-*` ZERO** · `build-content.mjs` **12 books, 2,092 questions, 2,092 translated** ·
`build-citations.py` **22,298 ledger records corpus-wide, QA total 201, of which ZERO are attributable
to any of the four chunks.**

★★ **THE CITATION PROFILE OF THIS SPAN IS THE CLEANEST IN THE CORPUS AND THE NUMBER IS DERIVED.**
The four chunks contribute **145 ledger records — 84 resolved to a chunk, 48 to a verse, 3 to a work,
3 page-multi, 2 chapter, 2 articulus, 1 distinctio, 2 excluded — and ZERO dangling, ZERO unresolvable,
ZERO ambiguous.** The corpus runs 2 % / 2 % / 2 % in those three classes; this span runs 0 / 0 / 0 on
145. ⭐ That is the measurable return on `q2-a2`'s rule — **when a citation names a target you hold,
open it** — which overturned five raw readings against the target's own `title_la` and a sixth against
our own p. 32 n. 5.

---

# The register rulings — what the shakedown was for

Two questions were handed up as questions rather than answers, one of them twice. Neither is ruled by
the chunk that raised it, and on both the gate can see something the chunk could not.

## 1. **Ps. 4:7 *Signatum est super nos lumen vultus tui* — does ruling 2's *lumen* survive inside a scripture quotation that is not Ps. 35:10?**

**The state of the text, measured not asserted.** *lux* and *lumen* occur in exactly two of the four
chunks — **`q2-a1` and `q2-a2` contain neither family in eleven leaves**, so the question is at the
same two attestations it was at when `q1-a1` raised it, and the gate owns it:

| | Latin body | English body |
|---|---|---|
| `q1-a1` | *lux* 1 · *lumen* 1 | "light" 1 · "lumen" 1 |
| `q1-a2` | *lux* 8 · *lumen* 12 | "light" 8 · "lumen" 12 |

★★ **And the totals are not the evidence — the anchor-aligned segments are.** Both chunks carry the
same anchors in the same order in Latin and English (54 and 53). Splitting both halves on the anchor
pattern and counting the two families per matched segment: **every segment that contains either family
agrees exactly, in both chunks, with no offsetting pair anywhere.** This is the instrument the
*scientia Christi* gate built after a chunk's totals reconciled perfectly while twenty sites were
wrong, and it is the first span to be measured with it prospectively. **Ruling 2 is kept, site by
site, across this span.** (One apparent excess "light" in `q1-a2`'s apparatus is Matt. 11:30's *my
burden light* — the adjective, not the noun.)

**The two sites, as they stand:**
- `q1-a1` p. 50 n. 2 → "The lumen [of thy countenance] is signed upon us," etc. — incidental.
- `q1-a2` p. 55 n. 9 → "The lumen of thy countenance, O Lord, is signed upon us." — **load-bearing**,
  and it is the anchor for the body's own *lumen divini vultus* → "the lumen of the divine
  countenance," on which the whole *Respondeo*'s account of the implanted lumen turns.

**The case for exempting it** is ruling 4's own line: a received English wording exists that a reader
will recognise — the Douay's "The light of thy countenance, O Lord, is signed upon us" — which is
exactly why Ps. 35:10 was exempted.

**The case against, and it is a distinction Ps. 35:10 does not have.** ⭐ At Ps. 35:10 the verse is
quoted *as a verse* in an argument, and no surrounding body prose leans on the word: exempting it
costs nothing. Here the note and the body are welded — **the body's *lumen divini vultus* is the
verse, five words later.** An exemption therefore has to go one of two ways, and both are worse than
keeping the rule: either the note reads "light" while its own anchor-text reads "lumen," and the
reader loses the identity the *Respondeo* is built on; or the exemption spreads into doctrinal body
prose, which is the one place ruling 2 exists to protect.

**▶ RECOMMENDATION: DO NOT EXEMPT — keep "lumen" at both sites, ruling 2 followed as written.** ⭐ And
record the *test* the two cases together produce, because it is what stops the exemption class
growing: **a received scriptural wording is exempt only where the verse is quoted as a verse and no
surrounding body prose leans on the term.** That keeps Ps. 35:10 exempt, keeps Ps. 4:7 inside the
rule, and gives the class a boundary — which is precisely what ruling 4 refused the "quotation
boundary" for lacking.

**▶ RULING (Wilson, 2026-09-06): KEEP "lumen" AT BOTH SITES. Ruling 2 followed as written, no edit.**
⚠ **AND THE EXEMPTION CLASS NOW HAS A TEST, WHICH IS THE PART TO CARRY FORWARD:** *a received
scriptural wording is exempt only where the verse is quoted as a verse and no surrounding body prose
leans on the term.* Ps. 35:10 stays exempt under it; Ps. 4:7 stays inside the rule. ⛔ Do not re-raise
Ps. 4:7 in a later chunk of this work — it is ruled, at two attestations, with the load-bearing one
in view.

## 2. **The failing impression — bracketed restoration, or reproduce the gap?**

`q2-a2` raised this as a **new defect class** and treated three sites by restoring the lost letters in
square brackets, against `q2-a1`'s p. 59 treatment, which reproduced a gap and filled nothing. The
question handed up was which treatment governs.

★★ **THE GATE'S FINDING IS THAT THE CLASS IS NOT NEW, AND THE CORPUS ALREADY TREATS IT THIS WAY.**
`bon-brev-p7-c7` p. 291 n. 7 — **built, gated, deployed** — met a two-line *wedge of lost impression*
and restored **`sit plenu[m]`, `[M]ulti codd.`, `[origin]alis`** in square brackets, deliberately
unflagged, on the reasoning that *a defect in the photograph is not a defect in Quaracchi*. A sweep of
every Latin body in vol5 finds bracketed letter-restoration in exactly one chunk (`q2-a2`'s
`plura[lit]as`), so the practice has been rare — but it is **attested, and consistent**.

⭐ **What the precedent adds is the criterion `q2-a2` had only half of.** p. 291 restored only what was
**determinate from matter printed elsewhere on the same page** (the note quotes *ut gaudium vestrum
sit plenum* itself; *textus originalis* stands twice more on the leaf). All three of `q2-a2`'s sites
meet that test — *rebu[s], si[mili]a* is Isidore's formula with *ex similibus* standing in the same
clause; *plura[lit]as* and *excl[ud]it* are determinate from the surviving traces and the sense —
**and the same chunk did NOT restore the em-dash that failed to print before `tom. III.`, which only
house usage would supply.** That asymmetry is the criterion working, not an inconsistency.

⭐ **So the diagnostic is sharper than "the flanking letters are lighter." That is the symptom; the
question it answers is WHOSE DEFECT IT IS.** Flanking letters at full strength on either side of a gap
= the forme never carried the letters (dropped or broken type) → **reproduce, never fill** (p. 58 n. 6,
p. 59 *ean-dem*). Flanking letters lighter than the rest of their own line, sloping off and recovering
= the type was set and **this copy** failed to take it → **restore in square brackets, disclosed,**
where the reading is determinate.

**▶ RECOMMENDATION: RATIFY both treatments as one two-part rule** — locate the defect (forme vs copy)
by the flanking letters, then restore only what is determinate from evidence on the same page and
reproduce everything else — **and correct the "new class" claim in `q2-a2`'s notes to cite
`bon-brev-p7-c7` p. 291 n. 7 as the precedent.** No transcription changes either way.

**▶ RULING (Wilson, 2026-09-06): BOTH TREATMENTS RATIFIED AS ONE TWO-PART RULE.** Forme defect
(flanking letters at full strength) → **reproduce, never fill**. Copy defect (flanking letters lighter
than the rest of their own line) → **restore in square brackets, disclosed, where the reading is
determinate from evidence on the same page**; everything else reproduced. No transcription changes.
✅ `q2-a2`'s `## Notes` corrected to cite **`bon-brev-p7-c7` p. 291 n. 7** as the precedent rather than
claiming a new class.

---

# Gate result

**ZERO defects in scope across all four passes, and both carried questions RULED.** One docket item
(five undocumented leaf-edge seams in closed works) recorded and not fixed; **pass 4 run, ~663 MB
reclaimed**.

| # | question | disposition |
|---|---|---|
| 1 | Ps. 4:7 *lumen* inside a scripture quotation | **ruling 2 KEPT** — no edit; exemption class given a test |
| 2 | failing impression vs compositor's blank | **both treatments RATIFIED** as one rule; the class is not new |

★★★ **THE LESSON THIS GATE ADDS TO THE LAST ONE.** The *scientia Christi* shakedown ended on *a
chunk's `## Notes` are a claim about the chunk, never a measurement of it.* This span was built after
that ruling and **its register claim survives the anchor-aligned test at every site** — so the rule
transferred, and the gate's job here was not to catch a broken claim but to answer questions the
chunks correctly refused to settle. ⭐ The one thing the chunks got wrong was a claim about the
**corpus**, not about themselves: `q2-a2` called the failing impression a new class when a deployed
Breviloquium chunk had already ruled it. **Before naming a defect class new, sweep the corpus for it —
that is cheap, and a wrongly-new class invents a convention beside an existing one.**

## The front after this gate

**`bon-qmt-q3-a1`, pp. 68–73**, inheriting **p. 68 nn. 2–5** (re-derive them down to their DIGITS, and
note that **n. 5 (Avicenna/Algazel) runs over the gutter** — that runover belongs to `q3-a1`'s ledger
line). ⛔ **Fix the END of the span on the plate BEFORE extracting plates** — the index gives `68–73`
and the index has now been wrong once in this work. The work-close gate follows at p. 115, **and the
deploy boundary is the work close** — nothing in this work has been deployed.
