# Vol V — COLLATIONES DE SEPTEM DONIS SPIRITUS SANCTI work-close polish gate (printed pp. 457–503)

Run 2026-08-29, immediately after `bon-don-c9` landed (`5589a92`). This is the work's **only**
gate: 49 printed pages, so the ~100-page trigger never fires and the work-boundary trigger
supplies it. **The shakedown trigger did not fire separately** — per the cadence frozen at the
mini-pilot, the register here is the one the Hexaemeron had just exercised over 128 pages, so a
second early gate would have bought nothing.

**Scope: nine chunks, `bon-don-c1`–`c9`, 178 ¶¶, 403 apparatus entries, pp. 457–503 with no gap.**

**Result: ZERO corpus defects in the text.** The gate's whole substantive output is the **two
register rulings** below, which are conventions and not repairs. Every other finding is a checked
negative or a pre-existing defect outside this work's pages.

---

## ★★ The two register rulings (Wilson, 2026-08-29) — the work's only carried-forward business

Neither question arose in c9's own text, so c9 could not settle either; both had been carried
deliberately since c2/c8 rather than churned chunk by chunk. **They are settled here once, for the
whole work, and they bind *De decem praeceptis*.** The full statement is in repo `CLAUDE.md`
§ SEPTEM DONIS; it is repeated in the Notes of c2, c3, c6, c7 and c9 so no reader of a chunk meets
the question without the answer.

### 1. *pietas* → **"piety" everywhere** — body prose AND inside scripture quotations

**⚠ The premise as carried forward was wrong, and the gate is where that surfaced.** Every note
from c3 onward — and the resume note — said c2's four "godliness" sites were "four incidental
occurrences, **three of them inside the Douay wording of Isaiah 11:2**." Read against the text,
the split is the **inverse**: *one* is inside the Isaiah quotation (¶ 2), and **three are
Bonaventure's own body prose** (¶ 3's *donum pietatis* against envy, ¶ 4's second petition of the
Lord's Prayer, ¶ 5's *consummatio*). So this was never a Douay-fidelity question with a bit of
spill; it was a straight **body-register inconsistency between c2 and c3/c6/c7**, wearing a
Douay costume.

★ **How the error survived four chunks:** c3 wrote the characterisation while making its own
(correct) decision, c6 and c7 quoted c3, c9 quoted c7, and the resume note quoted c9. **No one
between c3 and the gate re-read c2.** A tally that is copied forward is not a measurement, and
this is the cheapest possible instance of that — the gate's real yield.

**Ruling:** the gift keeps **one visible English root** across the work. The Douay's "godliness"
is adjusted at **Isaias 11:2** (c2 ¶ 2) and **I Tim. 4:8** (c7 ¶ 17). This is the frozen corpus
rule — *"Scripture on the Douay-Rheims base **adjusted to Quaracchi's actual Latin**"* — doing
exactly its job: Quaracchi prints *pietatis*, and the collatio is titled *De dono pietatis*.
c3's argument carried it: "godliness" has no adjective for *pius* and no adverb for *impie*,
while *piety / pious / impious / impiety* fills every slot, and c6's Part II turns on the family
through six consecutive paragraphs.

**Applied:** four sites edited, all in `bon-don-c2`'s English body. c3, c6 and c7 already conformed.

### 2. *intellectus* → **understanding**, *intelligentia* → **intelligence** — in body prose; the Douay's "understanding" stands inside a quotation

c8 holds the pair apart across 25 sites because ¶ 11 divides *intelligentia* into *memoria
praeteritorum, intelligentia praesentium, circumspectio futurorum* — a division that collapses if
both words share one English root. c7 renders *intelligentia* "understanding" at four sites.

**Ruling: c8's distinction is the work rule, and it cost ZERO edits.** c7's four sites are not
counter-examples once looked at: a Quaracchi *summarium*, the Douay quotations of **Job 28:12**
and **Ecclus. 37:20**, and one body echo of the Ecclesiasticus quotation it glosses — the printed
text's own pun, which c7 preserved deliberately. Every one of them is either editorial furniture
or inside/attached to a quotation.

**⚠⚠ The two rulings pull opposite ways, and that is the point — do not flatten them into
"always follow the Douay" or "never."** *pietas* is **one** Latin word that needs one English
root, so the Douay yields. *intelligentia* stands **beside a contrasting Latin word**, so the
contrast is what must survive and the quotation is left alone. **The discriminator is whether the
English is carrying a Latin distinction, not whether the sentence is a quotation.**

---

## Pass 1 — `[?]` flag resolution (pp. 457–503)

**`tools/check-live-flags.py` — the gate's instrument, not `grep`. Result: ZERO live flags in all
nine chunks.** Nine consecutive Tier-2 chunks with nothing to resolve.

Corpus baseline at this gate: **vol1 150 · vol2 9 · vol3 2 · vol4 66 · vol5 10** = 237 occurrences.

★ **Vol V moved 2 → 10 since the Hexaemeron mid-work gate, and every one of the eight new
occurrences is a formally ACCEPT-ILLEGIBLE printed defect, not drift.** Verified chunk by chunk
rather than inferred from the count:

| chunk | occ. | what it is |
|---|---|---|
| `bon-brev-p6-c13` | 2 | p. 280 n. 6's broken final word (*homo non separe*) — pre-existing |
| `bon-hex-c15` | 2 | p. 400 ¶ 18, **Quaracchi's own type broken** at *resurrect* |
| `bon-hex-c19` | 2 | p. 421 ¶ 7, a **deliberate editorial lacuna** the edition declines to fill |
| `bon-hex-c22` | 4 | pp. 439 / 444, **two printed gaps** of two different kinds |

**None is an unread page or an unresolved ambiguity.** Quaracchi is never silently emended, so
these stay flagged; the number rising is the discipline working, not failing. **Vols I and IV's
150 + 66 remain the real backlog, and remain a scoped job that a gate in Vol V does not touch.**

---

## Pass 2 — full-corpus style/formatting scan

`polish-style-scan.py`, no filter, **2,075 chunks scanned**:

- **`bon-don-c1`–`c9`: CLEAN. Vol V's only issue is outside this work.**
- Corpus-wide: **11 issues / 6 chunks, all pre-existing, none in this work.**
  - `bon-hex-c23` — one `V5LABEL`, apparatus label `51` not page-qualified. Known, already
    carried on the open list; the Hexaemeron's own gate recorded it.
  - 10 `PAIR` across `III-d31-a3-q3` (1–3), `III-d32-a1-q2` (13, 14), `III-d5-a2-q4` (11),
    `IV-d14-p2-a2-q1` (15, 17), `IV-d16-p2-a2-q2` (6) — the **J4 class-B orphaned-def residue**,
    unchanged in count and membership since the Itinerarium gate five weeks ago.

**Deliberately NOT fixed: a gate over pp. 457–503 authorises no edit under `vol3/` or `vol4/`.**

---

## Pass 3 — boundary-integrity sweep

### The boundary set, counted BY HAND

⚠ `seam-screen.py` is structurally blind to leaf crossings — it reports only mid-page boundaries,
and it found **six**. The work has **eight** interior boundaries. The two it cannot see were
derived from the chunks' own spans:

| # | boundary | pages | kind |
|---|---|---|---|
| 1 | `c1` → `c2` | 461 \| 462 | **leaf crossing** |
| 2 | `c2` → `c3` | 467 \| 468 | **leaf crossing** |
| 3 | `c3` → `c4` | 473 | shared leaf |
| 4 | `c4` → `c5` | 479 | shared leaf |
| 5 | `c5` → `c6` | 483 | shared leaf |
| 6 | `c6` → `c7` | 489 | shared leaf |
| 7 | `c7` → `c8` | 493 | shared leaf |
| 8 | `c8` → `c9` | 498 | shared leaf |

★ **SIX SHARED LEAVES CONSECUTIVELY, AFTER TWO CLEAN CROSSINGS — and the shape is the
Itinerarium's cause running in reverse.** There the unit (the capitulum) was always smaller than
the leaf, so *every* boundary was mid-page. Here the unit is ~5.2 pages, i.e. **just over** a
leaf, so a boundary lands mid-leaf roughly as often as not — and once it started doing so it did
not stop. **The run of six is what built the "shared leaf ⇒ hand-off" reflex that p. 498 broke.**

### (a) Grammatical continuity — all eight PASS

Every receiving chunk opens on its own display heading `### COLLATIO I.`–`### COLLATIO IX.`; every
ceding chunk ends on a grammatically complete doxological close (`…qui cum Patre etc.` ×6, c5's
`…Pater et Filius et Spiritus sanctus. Amen.`, c8's `Rogabimus Dominum etc.`), and c9 ends on
`EXPLICIUNT COLLATIONES DE DONIS SPIRITUS S.`

**No cascade-merge signature anywhere.** `seam-screen.py --volume 5` independently reports
**0 tail-not-terminal suspects across all 102 vol5 mid-page boundaries.**

### (b) Footer accounting across all 47 pages — all PASS

Per-page ownership derived from the page-qualified `[^pNNN-M]` definitions, independently of
`check-vol5-apparatus.py`:

```
457  7  c1:1-7          473  8  c3:1-5 | c4:6-8    489  5  c6:1   | c7:2-5
458  9  c1:1-9          474  8  c4:1-8             490  8  c7:1-8
459 11  c1:1-11         475 10  c4:1-10            491  7  c7:1-7
460 10  c1:1-10         476 11  c4:1-11            492  9  c7:1-9
461  8  c1:1-8          477 12  c4:1-12            493  7  c7:1-6 | c8:7
462  5  c2:1-5          478  8  c4:1-8             494 10  c8:1-10
463  8  c2:1-8          479  6  c4:1   | c5:2-6    495 10  c8:1-10
464  7  c2:1-7          480 11  c5:1-11            496 11  c8:1-11
465 12  c2:1-12         481  9  c5:1-9             497  6  c8:1-6
466 11  c2:1-11         482 10  c5:1-10            498  9  c8:1-9
467  8  c2:1-8          483  7  c5:1-2 | c6:3-7    499  7  c9:1-7
468  4  c3:1-4          484  9  c6:1-9             500  8  c9:1-8
469 11  c3:1-11         485  7  c6:1-7             501  7  c9:1-7
470  7  c3:1-7          486  9  c6:1-9             502 11  c9:1-11
471 10  c3:1-10         487  9  c6:1-9             503  7  c9:1-7
472 10  c3:1-10         488  9  c6:1-9
```

**Every page's register is contiguous `1..N` with no gap, no double-claim and no unowned page**,
and every shared leaf splits between exactly the two chunks that share it. The numbers agree with
`check-vol5-apparatus.py`'s independently-derived `KNOWN_TOTALS` on all 47.

★★ **p. 498 is the load-bearing row and it reads exactly as the new rule predicts: `c8:1-9`, no
c9 share.** `COLLATIO IX.`'s heading, subtitle and (first half of its) Summarium stand on that
leaf, and it still forwards nothing, because Collatio IX's ¶ 1 does not begin until p. 499. The
rule — *a shared leaf forwards a runover only when the incoming unit's BODY reaches it* — is now
attested from **both** ends of the seam and confirmed a third time by the page map.

★ **c4's span, 473–479, is shared at BOTH ends** — the only such span in the work. Its register
runs p. 473 n. 6 → p. 479 n. 1; it both receives a hand-off and makes one.

### (c) Runover ledger — all nine chunks accounted for

`manual-review/vol5-runover-ledger.tsv` carries a line for **every one of the nine chunks** — no
chunk skipped its runover test. **19 tests in this work: 17 gutter-crossing, 2 page-crossing**
(p. 460 n. 10 within c1; p. 479 n. 6, c4 → c5). `check-vol5-census.py`: rosters agree **123/123**.

### (d) Apparatus digit-multiset sweep (the `Dieta salutis` defect family)

The cheap sweep frozen at the Hexaemeron mid-work gate — compare the multiset of Arabic digits in
each entry's `**La.**` half against its `**En.**` half — run over all **403 entries**:

**2 mismatches, both the known false positive (a numeral correctly spelled as a word), 0 defects.**
- `c8 [p494-8]`: `Homiliis 50` → "*Fifty Homilies*"; `83 Qq.` → "*Eighty-three Questions*".
- `c9 [p503-6]`: `enarrat. 2.` → "second exposition".

**401 of 403 entries match digit for digit.** No entry shows the silent-normalisation signature.

---

## Pass 4 — disk cleanup

450 dpi page images and colcrop bands are fully regenerable from the gitignored
`raw/doctorisseraphic05bona.pdf` (confirmed present before deleting) via `extract-pages.py` +
`colcrop.py`; every gutter measured in this work is recorded in repo `CLAUDE.md`.

Deleted at the close of this gate: **49 page images (162 MB) plus the colcrop bands (805 MB) —
~967 MB reclaimed.**

---

## Verification suite at the gate

| check | result |
|---|---|
| `check-live-flags.py` | **0 live flags** in `bon-don-c*`; corpus 237 (vol1 150 · vol2 9 · vol3 2 · vol4 66 · vol5 10) |
| `check-vol5-apparatus.py` | 123 chunks / **2,266 entries**, all passed; no PENDING, no GAP, no unowned page |
| `check-vol5-census.py` | rosters agree **123/123**; 168 runovers (150 gutter, 18 page-crossing) |
| `polish-style-scan.py` | this work **CLEAN**; corpus 11 pre-existing issues / 6 chunks |
| `seam-screen.py --volume 5` | 102 mid-page boundaries, **0 tail-not-terminal suspects** |
| digit-multiset sweep | 403 entries, **2 known false positives, 0 defects** |
| `build-citations.py` | 21,772 records; **this work 502 records / 0 dangling / 0 QA flags**; corpus QA total **200** |
| `build-index-json.py` | 1,637 chunks cited, 9,563 backlinks |
| `build-content.mjs` | **2,074 / 2,074 translated**, 9 books |
| `git status vol1..vol5` after index runs | **empty** — the index tools wrote nothing under `vol*/` |
| division-title registry | all **nine** collationes present in `site/scripts/build-content.mjs` |

---

## What remains open (none blocking, none of it this work's)

1. **A scripture `ibid. <ch>, <v>` keeps the right BOOK but the stale VERSE** (c7, p. 492 n. 4).
   Corpus-wide existing behaviour, not a regression. **Wilson's call whether it earns a tool pass.**
2. `bon-hex-c23`'s one non-page-qualified apparatus label (`51`).
3. The 5-chunk `PAIR` residue in Vols III–IV (pass 2).
4. Vols I and IV's `[?]` backlog — 150 and 66 occurrences; a scoped job.
5. **Vols II–IV have never been swept for the Vol I cross-reference digit class**, and a clean
   grep would not prove them sound.
6. The About page's **"What Is Known to Be Wrong"** — Wilson's to frame.
7. `d30-a1-q3`'s transposed `s`-series labels · `d37-p2-dubia` `[^6]`'s merged notes · Book IV
   `d. 2. p. I.` cite · `prol-comm` p. 24 n. 2 (jointly impossible; flag stands).
8. **⛔ The Vol I page-gap hunt stays PARKED** (Wilson, 2026-08-24). Reopening trigger: a reader
   reports a gap. Nothing else.

---

## The gate's own finding

★★ **Third consecutive work whose gate found nothing wrong with the text — and the first whose
gate found something wrong with the NOTES.** The Breviloquium's gate found wrong comments and
rejected measurements, never a wrong text; the Itinerarium's found not even a wrong comment; this
one found a **wrong tally, quoted forward through five documents** — c3's mischaracterisation of
where c2's four "godliness" sites stood, repeated by c6, c7, c9 and the resume note, and never
re-checked against c2 itself.

**That is the argument for the work-boundary gate stated exactly.** Per-commit checks catch what
is internally inconsistent *inside a chunk*; nothing but a reader with the whole work in view
catches a claim that every chunk agrees on and none re-measured. The defect was in the reasoning
about the text rather than in the text, which is why nine passes of clean tooling could not see it.

⚠ **The transferable rule: a tally that is copied forward is not a measurement.** When a note
hands a count to the next chunk, the next chunk inherits the *question*, not the *number* — and
the gate re-derives every number it is asked to rule on.
