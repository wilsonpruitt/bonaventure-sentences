# Vol V — *QD de scientia Christi*: SHAKEDOWN GATE (2026-09-04)

The first of this work's two gates, fired at the close of **`bon-qsc-q4`** per the frozen cadence
(trigger 3 — a shakedown at the first structural seam ~15–25 printed pages in). Scope:
**`bon-qsc-q1` … `bon-qsc-q4`, printed pp. 3–27, 25 leaves, 206 apparatus entries.**
It has not fired since the Hexaemeron, and this is a new genre in Vol V.

**Result: THREE corpus defects, all inside the gate's own scope, one already repaired.**
Two of the three are register defects that the chunks' own `## Notes` describe *incorrectly* —
i.e. they would have been quoted forward as settled. That is what the shakedown is for.

---

## Pass 1 — `[?]` flag resolution: NOTHING TO RESOLVE IN SCOPE, verified not assumed

`tools/check-live-flags.py` (not `grep` — the earned instrument): **237 live occurrences corpus-wide,
of which `bon-qsc-*` contributes ZERO.** Per volume: **vol1 150 · vol2 9 · vol3 2 · vol4 66 · vol5 10.**

⚠ **vol5 has moved 2 → 10 since the Hexaemeron shakedown baseline.** All eight new ones are
pre-existing in already-deployed Hexaemeron/Breviloquium chunks — `bon-brev-p6-c13` (2),
`bon-hex-c15` (2), `bon-hex-c19` (2), `bon-hex-c22` (4). **Recorded, not fixed: this gate authorises
no edit outside `bon-qsc-*`.** Vols I and IV remain the known scoped backlog.

## Pass 2 — style/formatting audit, full corpus

`polish-style-scan.py` over 2,086 chunks. **One issue in scope, and it is now FIXED:**

▶ **DEFECT 1 (repaired).** `bon-qsc-q4` `[V5NOTES]` — a literal `[^p21-1]` footnote token stood in
`## Notes` prose, quoting the anchor on the *Sed contra hoc obiicitur* formula. Rewritten as
`(anchor \`p21-1\`)`. vol5 now scans **CLEAN except one out-of-scope item.**

Out of scope, recorded not fixed:
- **`bon-hex-c23` `[V5LABEL]`** — apparatus label `[^51]`, not page-qualified. Checked: this is
  **deliberate and documented** in that chunk's own `transcription_status` (it transcribes the
  ADDITAMENTUM heading and its page-449-foot-truncated paragraph, anchored on the colophon, and so
  belongs to no single page register). It is a convention gap, not a transcription error; the tidy
  form would be `[^p449-add]`. **The Hexaemeron is closed and deployed — no edit here.**
- **10 `[PAIR]` issues across 5 chunks in Vols III–IV** — the known **J4 class-B residue**
  (orphaned defs): `III-d31-a3-q3`, `III-d32-a1-q2`, `III-d5-a2-q4`, `IV-d14-p2-a2-q1`,
  `IV-d16-p2-a2-q2`. Identical to what the Itinerarium and Hexaemeron gates found. No edit.

## Pass 3 — boundary integrity sweep

**Every leaf pp. 3–27 is contiguous 1..N with no gap, no double-claim and no unowned page**,
agreeing with `KNOWN_TOTALS` on all twenty-five leaves. p. 27 is correctly reported as a legitimate
PENDING, not a GAP. Per-chunk: **q1 31 · q2 34 · q3 48 · q4 93 = 206 entries**, La/En paired throughout.

**Four interior boundaries, counted by hand — and they take THREE different shapes:**

| boundary | shape | register |
|---|---|---|
| q1 \| q2 | **mid-leaf, p. 6** — Q. II opens below Q. I | **SPLIT 6 / 3** — nn. 1–6 q1's, nn. 7–9 q2's |
| q2 \| q3 | **mid-leaf, p. 10** | **SPLIT 7 / 1** — nn. 1–7 q2's, n. 8 forwarded to q3 |
| q3 \| q4 | **LEAF EDGE, p. 17** | q3 closes on p. 16 owning all 8; q4 owns all 10 of p. 17. **Inherits nothing.** |
| (q4 \| q5) | **mid-leaf, p. 27, and Q. V's BODY begins on the leaf** | **SPLIT 1 / 7** — n. 1 q4's, nn. 2–8 PENDING for q5 |

★★ **THE SPLIT RATIO CARRIES NO RULE, AND IT INVERTS.** At pp. 6 and 10 the *outgoing* question owns
most of the leaf (6/3, 7/1); at p. 27 the outgoing question owns **n. 1 only** and the incoming takes
seven, because Q. IV closes across the top band of both columns while p. 27's whole left register is
n. 1, a full-column editorial dissertation. **Do not infer the next boundary's shape, or its ratio,
from the last one — read the anchors.** Three of four boundaries forward; p. 17 does not.
⛔ **pp. 32 and 37 remain UNMEASURED — re-ask the p. 498 rule on the plate at each.**

★ **A CHECKED NEGATIVE ON THE CORPUS DENOMINATOR** (the `bon-brev-prol` blind-spot class).
Disk carries **2,087 `.md`** under `vol1…vol5`; the scanners see 2,086 and `build-content.mjs` builds
2,085. **Both gaps are accounted for and neither is a silent skip:** `vol1/punch-list.md` is not a
chunk, and `vol1/bon-sent-I-proleg.md` is excluded **deliberately and by a documented guard** in
`build-content.mjs` (a bare 77k-word OCR dump with no `type:`; the exclusion carries its own ⛔ TRAP
comment). Reconciled 2085 + 2 = 2087.

## Pass 4 — disk: **DONE, ~455 MB reclaimed**

`raw/vision/vol5/` (28 plates, **85 MB**) and `/tmp/colcrop/` (**370 MB**) deleted, both fully
regenerable from the gitignored PDF via `extract-pages.py` + `colcrop.py`.
⚠ **Re-extract before any later plate work; the vol5 plates are gone again.** (The deletion was first
refused by the session's auto-mode classifier and ran on Wilson's explicit OK.) `raw/vision/vol1/pagegaps/` (32 MB) was deliberately left alone —
different artifact, unknown provenance, out of scope.

---

## Verification suite at the gate

`check-vol5-apparatus.py` **134 chunks / 2,659 entries, all checks passed** · `check-vol5-census.py`
**rosters agree 134/134**, 182 runovers across 134 chunks (161 gutter-crossing, 21 page-crossing) ·
`polish-style-scan --volume 5` **CLEAN in scope** · `build-content.mjs` **11 books, 2,085 questions,
2,085 translated** · `build-citations.py` corpus QA total **201**, of which **exactly 2 are
attributable to this gate's scope** — `bon-qsc-q3` and `bon-qsc-q4`, both an unresolved `ibid`
anaphora in `latin_body`, the same benign class as `bon-itin-c7` and `bon-praec-c5`. **No
out-of-range citation, no dangling reference, from any of the four chunks.**

---

# The register rulings — what the shakedown was for

`bon-qsc-q4` handed the gate **three** questions as questions rather than answers; `bon-qsc-q3`
handed it a **fourth** that had been deferred to the work-close gate. All four are ruled here.

## 1. ***intellectus agens* → "the agent intellect" — RATIFIED. No edit.**

This is **not an extension of the ratified narrow exception; it is the same instance of it.** The
exception was founded at `bon-praec-c2` on the **Averroist unity of the intellect**, and its ratified
scope is "applies only when the rule would misname a fixed philosophical doctrine, never a general
escape hatch" (decem praeceptis work-close gate, 2026-08-31). *Intellectus agens* is that same
doctrine's own name. "The agent understanding" would name nothing a reader could look up.

★★ **The evidence that it stayed narrow is the strongest the corpus has produced, and it is
mechanical.** `bon-qsc-q4` carries **57 Latin `intellect-` nouns** — this is the illumination
question, where the word is the running subject. English "intellect" occurs **9 times, and every
single one is inside a doctrinal name**: 8 × *intellectus agens* → "agent intellect", 1 ×
*intellectus possibilis* → "possible intellect". **There is not one bare "intellect" in the chunk.**

★ **The decisive control is a single sentence on p. 19** which contains the rule and the exception
side by side and separates them correctly:
> *…ita et circa **intellectum** intelligere oportet, quod est **intellectus agens** et **intellectus
> possibilis***
> → "so also concerning the **understanding** it must be understood that there is an **agent
> intellect** and a **possible intellect**"

The bare noun goes to "understanding" **in the same clause** in which the name keeps "intellect."
**The exception is scoped to the PHRASE, not to the word.** That is the test, and it passed.

## 2. ***lux* → light / *lumen* → "lumen" — ▶ DEFECT 2: NOT RATIFIABLE AS DESCRIBED. `bon-qsc-q4` DID NOT DO WHAT ITS OWN `## Notes` SAY IT DID.**

`bon-qsc-q4`'s `## Notes` state: *"**held apart**, and this chunk exercises `q3`'s ruling **about
twenty times** against `q3`'s handful."* **The file says the opposite.** In the English body:

| | Latin body | English body |
|---|---|---|
| *lux* family | 39 | "light" 59 |
| *lumen* family | **23** | **"lumen" 3** |

62 Latin → 62 English, so nothing is dropped — but **20 of the 23 *lumen* sites are rendered
"light," and only 3 keep "lumen."** `q3`, by contrast, is internally exact: **3 / 3 and 7 / 7.**

⛔ **Worse: two of the four sites the Notes cite AS EVIDENCE of the ruling are among the twenty that
break it.**
- *lumen mentium* (arg. 4, and again at arg. 34) → **"the light of minds"**, both times.
- *lumen rationis aeternae* (p. 24) → **"the light of the eternal account."**
- *lumen creatum principiorum* (reply 15) → "the created **lumen** of principles." ✔
- *in lumine veritatis creatae* (reply 4) → "in the **lumen** of created truth." ✔

⛔ **And the same phrase is rendered both ways inside the one chunk:** *lumen creatum* is
**"a created light"** in argument 20 and **"the created lumen of principles"** in reply 15.

★★ **THE SHAPE OF THE DEFECT IS THE FINDING.** The split is not random — it is **positional**. The
three surviving "lumen" renderings all stand in the *Respondeo* and replies (pp. 25–26); **every one
of the twenty in the argument series (pp. 17–24) went to "light."** The register decision was applied
in a later pass over the solution and never carried back over the arguments, and the `## Notes` were
written from the later pass. ⚠ **A chunk's `## Notes` are a claim about the chunk, not a measurement
of it. This gate found the first case where they are simply wrong — and they would have been quoted
forward as settled.** Read the register claim against the text, not against the note.

⚠ **A boundary case that survives whichever way this is ruled:** argument 15 quotes Ps. 35:10
*In lumine tuo videbimus lumen* → **"In thy light we shall see light."** This is a received Psalter
wording at a **scriptural quotation boundary**, the same class as `q3`'s Dionysius case (ruling 4
below), and should stay as it stands under either resolution.

**▶ RULING (Wilson, 2026-09-04): HOLD THEM APART. REPAIRED — all eighteen sites.**
*lumen* → "lumen" is the work rule. `bon-qsc-q4`'s eighteen argument-series sites were repaired to
"lumen" (the count is 18, not 20, because the two Ps. 35:10 words are exempted below), and the chunk
now reads **23 Latin *lumen* → 21 English "lumen"** with every anchor-aligned segment agreeing.
**Cost accepted and to be disclosed in a translator's note: "lumen" is a transliteration and at this
frequency it is conspicuous.**
⚠ **ONE STANDING EXEMPTION:** Ps. 35:10 *In lumine tuo videbimus lumen* (arg. 15) keeps **"In thy
light we shall see light"** — a received Psalter wording at a scriptural quotation boundary. It is
the only *lumen* in the work rendered "light" and it is **not** a defect; do not "fix" it.

★★ **THE INSTRUMENT THAT FOUND THIS, AND IT GENERALISES TO ANY TERM OF ART.** A whole-chunk word
count is blind here: the totals **reconciled perfectly** (62 Latin *lux*+*lumen* → 62 English
"light"+"lumen") **while twenty sites were wrong**, because a collapse moves words between two
buckets that both stay full. What localises it is that **the Latin and English halves carry the same
93 footnote anchors in the same order** — split both on the anchor pattern and compare term counts
per matched segment, and a register break narrows to a few sentences. ⚠ **Two regex traps met while
doing it:** the *lux* paradigm needs the dative *luci* (a `lux|luce|lucis|lucem` pattern reports a
correct segment as broken), and an elided Latin noun legitimately expands in English (p. 23 n. 3's
*gratuiti luminis, sed etiam naturalis* → "gratuitous lumen, but also of natural lumen", 2 → 3).
**Both look like defects and are not. Confirm every mismatch by eye before editing.**

## 3. ***contueri* → "to contuit" / *contuibilis* → "contuitable" — RATIFIED, ▶ but DEFECT 3: `bon-qsc-q1` ALREADY CONTRADICTS IT.**

The family is small and had never been swept across the whole work. It occurs in exactly two chunks:

| chunk | section | Latin | English |
|---|---|---|---|
| `q4` | body | *contuita*, *contuibilis* | "contuited", "contuitable" |
| `q4` | apparatus | *contuita* ×2, *contuibilis* ×2 | (matched) |
| **`q1`** | body | ***contuitum*** | ⛔ **"intuition"** |

⛔ **`bon-qsc-q1` p. 5 renders *per universalem et plenarium contuitum* as "by a universal and full
**intuition**."** And `bon-qsc-q4`'s apparatus renders Latin ***intuitionem*** as **"intuition."**
**Two different Latin words are going to one English word inside one work** — and they are the two
words whose difference is the entire point, since *contuitus* in Bonaventure is precisely what
*intuitus* is not.

★★ **This is the `bon-praec-c4` case again, in a new work: "one English root would have flattened
them together."** That is the reasoning on which *intellectus*/*intelligentia* was ratified, and it
applies here with a sharper edge, because here the flattening is not a loss of shading — it asserts
the immediacy the doctrine denies. **"Contuition" is also the settled English term in Bonaventure
scholarship**, so the noun costs nothing; the verb and adjective coinages ("contuited",
"contuitable") are heavier, and are ratified as following the noun rather than on their own merits.

**▶ RULING (Wilson, 2026-09-04): the `contuit-` family is RATIFIED for `bon-qsc-q4`. The `q1`
REPAIR WAS DECLINED — `bon-qsc-q1` keeps *contuitum* → "intuition."**
⚠ **RECORD THE CONSEQUENCE HONESTLY, AND DO NOT RE-RAISE IT AS A NEW FINDING:** the work therefore
still contains one site where *contuitum* and *intuitionem* both go to "intuition." This is a **known
and ruled-upon** state, not an undetected defect. A later chunk meeting the `contuit-` family should
follow `q4` and leave `q1` alone; the work-close gate at p. 43 may revisit it with the whole work in
view, but it is not open between here and there.

## 4. ***intellectus* → understanding: `bon-qsc-q3`'s ONE disclosed departure — the quotation-boundary class.**

`q3` rendered Dionysius' *novit divinus intellectus* as **"the divine intellect knows,"** disclosing
it as a **quotation-boundary** judgment (the clause renders Greek νοῦς and Bonaventure is quoting,
not using), explicitly **without** invoking the ratified narrow exception, and offered it to the
work-close gate as a distinct class. **The shakedown reaches it first, and it is in scope.**

★ **What the gate now knows that `q3` could not:** `q4` has since held the rule across **57 sites
with zero bare "intellect."** So `q3`'s Dionysius clause is **the only bare "intellect" in the entire
work outside the two doctrinal names** — a single unrepeated exception, which is the exact shape
that drifts into a precedent.

**▶ RULING: the "quotation boundary" is NOT ratified as a licence class** — it has one instance,
no control, and unlike the doctrine-name exception it has no test that stops it generalising
(Bonaventure quotes constantly). ⚠ But note the tension with ruling 2's Ps. 35:10 case, which is
also a quotation boundary and which the gate is leaving alone: **the difference is that the Psalm
verse has a received English wording a reader will recognise, and Dionysius' clause has none.**
**▶ RULING (Wilson, 2026-09-04): REPAIRED.** *novit divinus intellectus* → "the divine
**understanding** knows." `bon-qsc-q3` now carries **zero bare "intellect"** in body or apparatus, and
the work as a whole carries none outside `q4`'s two doctrinal names.

---

# Gate result

**THREE defects, all in scope, ALL REPAIRED. Two register rulings ratified, one reversed, one declined.**

| # | defect | chunk | disposition |
|---|---|---|---|
| 1 | literal `[^p21-1]` token in `## Notes` prose (`V5NOTES`) | `q4` | **fixed** |
| 2 | 18 of 23 *lumen* sites rendered "light"; `## Notes` claimed the opposite | `q4` | **fixed** — held apart |
| 3 | *novit divinus intellectus* → "the divine intellect knows" | `q3` | **fixed** — → "understanding" |

**Rulings:** *intellectus agens* → "the agent intellect" **RATIFIED** (no edit) · *lux*/*lumen*
**HELD APART** (18 repairs, Ps. 35:10 exempt) · `contuit-` family **RATIFIED** for `q4`, the `q1`
repair **DECLINED** by Wilson · "quotation boundary" **NOT RATIFIED** as a licence class.

★★★ **THE LESSON THIS GATE EXISTS TO HAVE TAUGHT — and it is the one to carry into every later work.**
Two of the three defects were **not** transcription errors. They were **chunks whose `## Notes`
described a register practice the chunk did not follow**, and both would have been quoted forward as
settled by the next chunk, the next gate, and `CLAUDE.md`. `q4`'s bullet named four sites as evidence
of a ruling and **two of the four broke it.** ⛔ **A chunk's `## Notes` are a CLAIM about the chunk,
never a measurement of it. Verify a register claim against the text — and, where the chunk carries
paired anchors, against the anchor-aligned segments — exactly as `check-vol5-census.py` exists so
that no corpus count is ever hand-carried.** This is the same rule as "never hand-carry a corpus-wide
count, derive it," applied to prose instead of numbers, and it is now the third mechanism (after the
runover ledger and the live-flag tool) where a self-reported figure was found to be wrong.

★ **Why the break had the shape it did, which predicts where to look next time:** the register
decision was applied in a later pass over the *Respondeo*, replies and apparatus, and never carried
back over the argument series drafted first. **In a long chunk, suspect the FIRST-DRAFTED section —
the arguments — of carrying a pre-decision register.** `q4` is the largest chunk Vol V has attempted
(eleven printed pages, 93 entries) and that is exactly the condition under which a mid-build ruling
fails to propagate backwards.

## Verification suite after the repairs

`check-live-flags.py` **237 corpus-wide, `bon-qsc-*` contributes ZERO** · `check-vol5-apparatus.py`
**134 chunks / 2,659 entries, all checks passed** · `check-vol5-census.py` **rosters agree 134/134**,
182 runovers (161 gutter-crossing, 21 page-crossing) · `polish-style-scan --volume 5` **CLEAN in
scope** (the single remaining item is `bon-hex-c23`'s deliberate `[^51]`) · `build-content.mjs`
**11 books, 2,085 questions, 2,085 translated** · `build-citations.py` corpus QA **201**, of which
**2 in scope**, both benign `ibid` anaphora.

## The front after this gate

**`bon-qsc-q5`, pp. 27–32**, inheriting **p. 27 nn. 2–8** (re-derive them down to their DIGITS, not
only their ownership — that is `q3`'s lesson and it is not retired). ⛔ **p. 32 is UNMEASURED —
re-ask the p. 498 rule on the plate.** Plates must be **re-extracted** (Pass 4 deleted them), per
quaestio, never in bulk. **The work-close gate follows at p. 43, and the deploy boundary is the work
close** — nothing in this work has been deployed.
