# Vol V — COLLATIONES DE DECEM PRAECEPTIS work-close polish gate (printed pp. 507–532)

Run 2026-08-31, immediately after `bon-praec-c7` landed (the work's last chunk). Per the frozen Vol
V cadence table this is the work's **only** gate: 26 printed pages, well under the ~100-page
trigger, so the work-boundary trigger supplies it alone. **The shakedown trigger does not fire
separately** — the register here is the one the Hexaemeron and the *septem donis* have exercised
over 177 pages, and the *septem donis* gate (2026-08-29) already settled the two questions carried
over from that work. Modelled on `manual-review/vol5-septem-donis-workclose-gate.md`.

**Scope: seven chunks, `bon-praec-c1`–`c7`, pp. 507–532 with no gap, 187 apparatus entries.**

**Result: CLEAN. Zero corpus defects in the text.** The gate's substantive output is the **three
register rulings** below — two ratifications and one deliberately left open, none a repair.

---

## ★★★ The three register rulings (this gate, 2026-08-31)

### 1. *praeceptum* → precept / *mandatum* → commandment / *lex* → law — RATIFIED as the work rule

Set at `bon-praec-c1` and carried unbroken through all seven chunks, including through its densest
tests: c3 ¶ 2 (*decem sunt mandata decalogi, quae sunt fundamenta omnium legum*, all three words in
one clause), c5's Ephesians 6:2 Douay quotation (*quod est mandatum primum in promissione*, where
Douay and Quaracchi agree exactly on the word the rule assigns), and c6's Sixth–Seventh
Commandment run (¶¶ 2–3's nine occurrences of *mandatum/mandata*, ¶¶ 6–7's six-paragraph run of
*lex* in the technical sense, and the *Sextum praeceptum.* / *Septimum praeceptum.* subheads).
**Seven chunks, zero corrective edits, zero collisions with the plate.** The only cost the rule
ever exacted is cosmetic and was disclosed at c1: the work's own English title reads "Collations
on the Ten **Commandments**" while ¶ 20 and the Summarium read "the ten **precepts**" — both
correct renderings of two different Latin words (the title glosses *decem praeceptis* generically,
¶ 20 glosses the same word technically against *mandatum*), not a contradiction internal to the
rule.

**Ruling: RATIFY.** Zero cost across seven chunks, including at three deliberately hostile density
tests, is the strongest evidence this corpus has offered for adopting a convention outright rather
than carrying it. No reason found to reverse it.

### 2. *intellectus* → understanding / *intelligentia* → intelligence, with c2's ONE disclosed departure — RATIFIED, departure RATIFIED as a correctly-scoped exception

The base rule (frozen at the *septem donis* gate, item 2 above) held at every site in c1, c3, c4,
c5, c6 and c7 — six of seven chunks, no departure. The one exception is `bon-praec-c2` ¶ 25:
*ponere, quod unus intellectus sit in omnibus* is the Averroist unity-of-the-intellect thesis, a
doctrine with a fixed English name, and "one understanding in all" would not name it — so c2
rendered it "one intellect in all." No *intelligentia* stands near ¶ 25 to create a distinction the
rule exists to protect, so the rule's purpose was not engaged there.

`bon-praec-c3` is the control that shows the exception stayed narrow: its own *perverso intellectu
sacrae Scripturae* (¶ 5), the same phrase c2 renders so at ¶¶ 24 and 26 on the rule, took
"understanding" without departure — a cost (less idiomatic English), not an error, and so not c2's
case. `bon-praec-c4` and `bon-praec-c5` (¶ 1 vs ¶¶ 4/19) each showed the rule paying — protecting a
real distinction the note or the argument is built on — confirming the rule's purpose is live
elsewhere in the same work that produced the one exception.

**Ruling: RATIFY both.** The base rule stands; c2's departure is ratified as a correctly-scoped
exception that applies only when the rule would misname a fixed philosophical doctrine — never as
a general escape hatch. `bon-praec-c5`'s ¶¶ 4/19/10 counter-datum (two English roots forced onto a
single undistinguished Latin sense, *litteralis intelligentia* / *intellectus … secundum sensum
litteralem*) is real cost with no distinction to protect, but it is a passage-level oddity, not
grounds to reopen the work rule: it cost idiom, not accuracy, and no other chunk reproduced it.
Flag it for awareness in any future work that reuses this pair, but it does not unseat the rule
here.

### 3. *vacatio*/*vacare* → leisure vs *quies*/*requies* → rest — OPEN QUESTION, NOT SETTLED, NO SECOND DATA POINT

Opened at `bon-praec-c4` ¶¶ 7 and 12, where *quietem animarum, quietem Domini in sepulcro, cum
vacatione et contemplatione Dei, quietationem* and *divina vacatio* all stand in one short span and
a single English root for both families would destroy the distinction the paragraph is built on.
**Neither word occurs again in c5, c6, or c7 — the entire remainder of the work, four consecutive
chunks total including c4 itself.** Confirmed directly against the built text:

```
grep -c "vacatio\|vacare\|quies\|requies" vol5/bon-praec-c{5,6,7}.md   →   0 in each
```

**Ruling: record as an OPEN QUESTION THAT NEVER GOT A SECOND DATA POINT.** The distinction observed
at c4 was real where it occurred and the rendering used there ("leisure" vs "rest") is sound for
that passage, but the work ran out of text before the question could be tested a second time, so
there is no accumulated evidence for or against treating it as a work-wide rule. **Do not mark this
settled.** A future work that uses either family again (Sermones selecti, a plausible next work per
the resume file's work map) is the next place this can actually be tested, and should be, from
scratch rather than by assuming c4's single instance generalizes.

---

## Pass 1 — `[?]` flag resolution (pp. 507–532)

**`tools/check-live-flags.py` — the gate's instrument, not `grep`. Result: ZERO live flags in all
seven `bon-praec-c*` chunks.**

Corpus baseline at this gate: **vol1 150 · vol2 9 · vol3 2 · vol4 66 · vol5 10 = 237 occurrences**
— identical to the *septem donis* gate's baseline. All ten of vol5's occurrences are pre-existing,
formally ACCEPT-ILLEGIBLE printed defects already itemized at that gate (`bon-brev-p6-c13` ×2,
`bon-hex-c15` ×2, `bon-hex-c19` ×2, `bon-hex-c22` ×4) — none in `decem-praeceptis`, none new. Seven
consecutive Tier-2 chunks with nothing to resolve; no 600 dpi re-extraction was needed.

---

## Pass 2 — full-corpus style/formatting scan

`polish-style-scan.py`, no filter, **2,082 chunks scanned**:

- **`bon-praec-c1`–`c7`: CLEAN.** No `PAIR`, `V5LABEL`, or any other class fired in this work.
- Corpus-wide: **11 issues / 6 chunks, all pre-existing, none in this work** — the identical 11
  issues carried since the *septem donis* gate (`bon-hex-c23`'s one `V5LABEL`; the 10-entry `PAIR`
  residue across `III-d31-a3-q3`, `III-d32-a1-q2`, `III-d5-a2-q4`, `IV-d14-p2-a2-q1`,
  `IV-d16-p2-a2-q2`). Count and membership unchanged.

**Confirmed `DIRS` already covers `vol5`** (`tools/polish-style-scan.py` line 34:
`DIRS = ["vol1", "vol2", "vol3", "vol4", "vol5"]`) — the vol3/vol4 blindness this scan was built to
catch does not apply here; it was already fixed 2026-07-28.

---

## Pass 3 — cross-chunk boundary integrity sweep, all SIX interior shared-leaf boundaries

The boundary set is fixed and already measured chunk-by-chunk during the build: **c1 507–510 · c2
510–515 · c3 515–519 · c4 519–522 · c5 522–525 · c6 525–529 · c7 529–532**, six interior boundaries,
all six on shared printed pages (510, 515, 519, 522, 525, 529) — an unusual work where every
interior boundary is mid-leaf, none a clean crossing.

### (a) Grammatical continuity — all six PASS

Verified by reading the actual Latin text on both sides of every boundary, not by trusting the
chunks' own Notes:

| # | boundary | ceding chunk's close | receiving chunk's open |
|---|---|---|---|
| 1 | c1→c2, p.510 | c1 ¶24 ends on a complete sentence (*…quae sint decem praecepta et penes quid accipiantur.*) | c2 opens `### COLLATIO II.` / Summarium, fresh heading |
| 2 | c2→c3, p.515 | c2 ¶28–29 end on complete sentences (*Alias, volente Altissimo, plenius prosequemur.*) | c3 opens `### COLLATIO III.` / Summarium |
| 3 | c3→c4, p.519 | c3 ¶26–27 end on a complete sentence (*Patet modo, quibus modis assumitur nomen Dei in vanum.*) | c4 opens `### COLLATIO IV.` / Summarium |
| 4 | c4→c5, p.522 | c4 ¶15–16 end on a complete sentence (Ps. quotation) | c5 opens `### COLLATIO V.` / Summarium |
| 5 | c5→c6, p.525 | c5 ¶20–21 end on a complete sentence (*…sed mala morte mortuus est ille.*) | c6 opens numbered ¶1 directly, no fresh `COLLATIO` heading on its own file (heading fell in c5's span) |
| 6 | c6→c7, p.529 | c6's own ¶20 crosses the gutter from p.528 and finishes on p.529 at a complete clause (*…Rogemus ergo Dominum Iesum Christum etc.*) | c7 opens `### Summarium` then numbered ¶1, fresh heading |

**No cascade-merge splice defect anywhere** — no sentence is broken across a boundary, and every
ceding chunk's last sentence is grammatically and semantically terminal. Independently confirmed by
`tools/seam-screen.py --volume 5`: reports the same six mid-page boundaries (p.510, 515, 519, 522,
525, 529) among vol5's 108 total mid-page boundaries, with **0 tail-not-terminal suspects
corpus-wide**.

### (b) Footer note accounting at all six shared leaves — all PASS, split matches the chunks' own Notes exactly

Directly extracted every `[^pNNN-n]` label on each of the six shared pages and cross-tabulated by
owning chunk:

| page | owned by | split |
|---|---|---|
| p.510 | c1 only | nn. 1–7, **all c1's — the one "no" boundary** (c2's heading and Summarium stand on the leaf but its ¶ 1 does not begin there) |
| p.515 | c2, c3 | nn. 1–3 c2's, nn. 4–5 c3's |
| p.519 | c3, c4 | nn. 1–7 c3's, n. 8 c4's |
| p.522 | c4, c5 | nn. 1–7 c4's, n. 8 c5's |
| p.525 | c5, c6 | nn. 1–3 c5's, n. 4 c6's |
| p.529 | c6, c7 | n. 1 c6's, nn. 2–6 c7's |

This matches the frozen record in repo `CLAUDE.md` § DECEM PRAECEPTIS at every one of the six
boundaries (the "five yes, one no" tally: p.510 forwards nothing; pp.515/519/522/525/529 all
forward). **No note lost, duplicated, or misnumbered** — confirmed independently by
`tools/check-vol5-apparatus.py`, which reports every page in the 507–532 span with a contiguous
`1..N` register and `ok` status, and by `tools/check-vol5-census.py`, which reports vol5 rosters
agreeing (130/130 chunks) with the run's own runover ledger carrying a line for all seven
`bon-praec-c*` chunks (`bon-praec-c1`: p.508 n.7:gutter, p.509 n.8:gutter · `bon-praec-c2`:
p.512 n.3:gutter, p.512 n.8:page · `bon-praec-c4`: p.521 n.4:gutter · c3/c5/c6/c7: none).

### (c) Internal consistency of the chunks' own per-chunk documentation

Cross-checked the six chunks' `## Notes` sections against each other and against direct plate/text
evidence rather than accepting any single chunk's account at face value:

- Each boundary's forwarding verdict was independently re-derived by the **next** chunk before
  being adopted (c2 re-derives boundary 1 from the receiving side; c3 re-derives boundary 2; c4
  re-derives boundary 3; c5 re-derives boundary 4; c6 re-derives boundary 5) — no tally was ever
  copied forward without a fresh plate read, matching the pattern the *septem donis* gate's own
  finding ("a tally that is copied forward is not a measurement") warns against. **This work's own
  build discipline already avoided that failure mode**, and this gate's independent extraction in
  (b) above confirms every one of the six chunk-reported splits against the actual file contents,
  not merely against the chunks' own prose claims about themselves.
- The one register runover hazard this work introduced (`bon-praec-c2`'s p.512 n.8, whose last two
  lines print at the head of p.513's footer block without moving ownership) is a same-page
  phenomenon, not a chunk-boundary one, and does not touch any of the six interior boundaries
  above; it is already correctly excluded from the p.512/513 boundary count because p.512/513 is
  not one of the work's six shared-leaf boundaries (both pages belong entirely to c2).

**No discrepancy found between any chunk's documented boundary reasoning and the built text.**

---

## Supplementary sweeps (matching the *septem donis* gate's rigor)

### Digit-multiset sweep (the `Dieta salutis` defect family)

Compared the multiset of Arabic digits in each entry's `**La.**` half against its `**En.**` half,
over all **187 apparatus entries** in `bon-praec-c1`–`c7`:

**2 mismatches, both the known false positive (a Latin roman numeral rendered as an Arabic digit in
English), 0 defects.**
- `bon-praec-c7 [p529-5]`: Latin `d. XXXVIII.` (roman) → English "d. 38" (Arabic) — the digit "38"
  exists only on the English side because Quaracchi printed the Latin in roman numerals here.
- `bon-praec-c7 [p529-6]`: same mechanism — Latin's `d. XXXVIII.` (roman) beside a same-note
  Arabic `d. 38.` (already matched) produces one extra "38" on the English side.

**185 of 187 entries match digit for digit.** No entry shows the silent-normalisation signature.

### `build-citations.py` (decoupled, run on the same argument as every commit)

`bon-praec` contributes **212 citation records**, of which **1 is a `dangling` QA flag**:
`bon-praec-c6 [p528-9]`, `IV. Sent. d. 25. a. 4. q. 3.` — Book IV distinctio 25 has only an
articulus 1 in the built corpus (`bon-sent-IV-d25-a1-q1..q4`), so "a. 4" does not resolve. This is
transcribed exactly as Quaracchi prints it (the note goes on, two sentences later, to cite the same
distinction correctly as "d. 25. a. 1. q. 3."), so it reads as a genuine digit-confusion candidate
in Quaracchi's own text, not a transcription error — **the same class of finding the *Itinerarium*
and *Breviloquium* work-close gates already logged elsewhere and left open, not authorising an edit
here.** Corpus-wide QA total moved 200 → 201 since the *septem donis* gate, entirely attributable to
this one new record.

---

## Pass 4 — disk cleanup

**Deleted:**
- `raw/vision/vol5/p-505.png` through `p-532.png` (28 files, **84 MB**) — the printed-page range
  this work's build touched, confirmed present and complete before deletion, gitignored, fully
  regenerable via `extract-pages.py --volume vol5 --dpi 450` from `raw/doctorisseraphic05bona.pdf`
  (confirmed present).
- `/tmp/colcrop/*` (202 files, **408 MB**) — every file in the directory matched this work's page
  range (507–530); confirmed no file belonged to another page/work before deleting the whole
  directory contents. Fully regenerable via `colcrop.py`.

**~492 MB reclaimed.** `git status` confirms nothing tracked was touched by either deletion (both
paths are gitignored).

---

## Verification suite at the gate

| check | result |
|---|---|
| `check-live-flags.py` | **0 live flags** in `bon-praec-c*`; corpus 237 (vol1 150 · vol2 9 · vol3 2 · vol4 66 · vol5 10) |
| `check-vol5-apparatus.py` | 130 chunks / 2,453 entries, all passed; pp. 507–532 all `ok`, contiguous registers |
| `check-vol5-census.py` | vol5 rosters agree 130/130; runover ledger carries all 7 `bon-praec-c*` lines |
| `polish-style-scan.py` | this work **CLEAN**; corpus 11 pre-existing issues / 6 chunks, unchanged |
| `seam-screen.py --volume 5` | 108 mid-page boundaries incl. all 6 of this work's; **0 tail-not-terminal suspects** |
| digit-multiset sweep (187 entries) | **2 known false positives (roman-numeral class), 0 defects** |
| `build-citations.py` | this work 212 records / **1 dangling QA flag** (pre-existing-class, non-blocking); corpus QA total 201 (was 200 at the *septem donis* gate) |
| direct footer-note extraction, all 6 shared leaves | split matches `CLAUDE.md`'s frozen record exactly at all six |

---

## What remains open (none blocking, none of it this work's)

Carried unchanged from the *septem donis* gate, plus one addition:

1. A scripture `ibid. <ch>, <v>` keeps the right book but the stale verse (`bon-don-c7`, p.492 n.4)
   — corpus-wide existing behaviour, Wilson's call whether it earns a tool pass.
2. `bon-hex-c23`'s one non-page-qualified apparatus label (`51`).
3. The 5-chunk `PAIR` residue in Vols III–IV.
4. Vols I and IV's `[?]` backlog — 150 and 66 occurrences; a scoped job.
5. Vols II–IV have never been swept for the Vol I cross-reference digit class.
6. The About page's "What Is Known to Be Wrong" — Wilson's to frame.
7. `d30-a1-q3`'s transposed `s`-series labels · `d37-p2-dubia` `[^6]`'s merged notes · Book IV
   `d. 2. p. I.` cite · `prol-comm` p. 24 n. 2.
8. The Vol I page-gap hunt stays PARKED. Reopening trigger: a reader reports a gap.
9. **NEW: `bon-praec-c6 [p528-9]`'s dangling cross-reference to `IV. Sent. d. 25. a. 4. q. 3.`** —
   transcribed exactly as printed, genuine digit-confusion candidate in Quaracchi's own text, not a
   transcription defect; leave as-is pending a future targeted digit-confusion pass.

---

## The gate's own finding

Third-consecutive-work pattern from the *septem donis* gate does not repeat here in the same
shape: this gate found **nothing wrong with the text and nothing wrong with the chunks' own
Notes** — every boundary claim in `CLAUDE.md` § DECEM PRAECEPTIS checked against direct extraction
from the built files and held exactly, digit for digit, note for note, at all six shared leaves.
The work's own build discipline (re-deriving every boundary from the receiving side rather than
adopting the prior chunk's tally, explicitly disclosed at c2 through c6) already did the work a
gate exists to catch, so this gate's yield is the three register rulings rather than a caught
error. **That is a clean result, not a wasted gate** — per CLAUDE.md's own rule, a work-boundary
gate fires unconditionally regardless of whether the preceding build already got everything right,
because there is no way to know that in advance of the read.

**Verdict: CLEAN. No edits made to any `bon-praec-c*` file. The work is ready to deploy, pending
Wilson's go-ahead.**
