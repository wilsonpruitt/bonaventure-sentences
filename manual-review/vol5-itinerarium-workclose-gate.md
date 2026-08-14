# Vol V — ITINERARIUM work-close polish gate (printed pp. 295–316)

Run 2026-08-14, immediately after `bon-itin-scholion` landed (`7095a62`). This is the
work's **only** gate: 24 printed pages, so the ~100-page trigger never fires and the
work-boundary trigger supplies it — per the frozen rule that a work shorter than the page
interval gets exactly one gate, **never zero**.

**Result: ZERO corpus defects.** Every finding below is either a checked negative or a
pre-existing defect outside this work's pages.

---

## Pass 1 — `[?]` flag resolution (pp. 295–316)

**Nothing to resolve: there are ZERO `[?]` flags across all ten chunks.**

This was **verified, not assumed.** A grep for `[?]` returns one hit in nine chunks and two
in the tenth, and **every one of them is prose declaring the absence** (`**[?] flags:
none.**`, `**No [?] flags.**`, and the scholion's `transcription_status` string). No chunk
carries a live flag.

★ **Recorded as a checked negative rather than skipped silently**, on the standing rule
earned at c6: otherwise the next reader cannot tell a checked "none" from an unchecked one.

Corroborating: `check-vol5-apparatus.py` reports **no PENDING, no GAP, no unowned page**
anywhere in the work.

---

## Pass 2 — full-corpus style/formatting scan

`polish-style-scan.py` (no `--volume` filter, all 2,023 chunks):

- **Vol V alone: CLEAN, 89 files.**
- **Corpus-wide: 10 issues / 5 chunks, ALL `PAIR`, ALL pre-existing and ALL outside this
  work.** `bon-sent-III-d31-a3-q3` (defs 1–3), `III-d32-a1-q2` (13, 14), `III-d5-a2-q4`
  (11), `IV-d14-p2-a2-q1` (15, 17), `IV-d16-p2-a2-q2` (6) — orphaned apparatus definitions
  anchored in neither body.

These are the **residue of the known J4 class-B backlog** (orphaned defs). Last touched
2026-07-17 and 2026-07-28, i.e. weeks before this work began. **Recorded here rather than
silently absorbed, and deliberately NOT fixed: a gate over pp. 295–316 authorises no edit
under `vol3/` or `vol4/`.** They remain a scoped job.

⚠ One `V5NOTES` violation *was* caught and fixed during the scholion's own verification
step, before commit: literal `[^` tokens in `## Notes` prose, which render as live footnote
links and steal bindings. Pass 2 running every commit is what caught it — the argument for
decoupling it from the gates, holding exactly as written.

---

## Pass 3 — boundary-integrity sweep (the pass that carries this gate)

### The boundary set, counted BY HAND

**⚠⚠ `seam-screen.py` is structurally blind to leaf crossings** — it sees only mid-page
boundaries. The Breviloquium gate's 11 crossings existed in the denominator *only* because
pass 3 counted them itself. So the set below was derived from the chunks' own page spans and
then confirmed seam by seam, not taken from the tool.

| # | boundary | shared page | kind |
|---|---|---|---|
| 1 | `prol` → `capitula` | 296 | mid-page |
| 2 | `capitula` → `c1` | 296 | mid-page |
| 3 | `c1` → `c2` | 299 | mid-page |
| 4 | `c2` → `c3` | 303 | mid-page |
| 5 | `c3` → `c4` | 306 | mid-page |
| 6 | `c4` → `c5` | 308 | mid-page |
| 7 | `c5` → `c6` | 310 | mid-page |
| 8 | `c6` → `c7` | 312 | mid-page |
| 9 | `c7` → `scholion` | 313 | mid-page |

**NINE interior boundaries — ALL mid-page, ZERO leaf crossings.**

★ **This is the mirror of the Breviloquium's Pars IV** (11 mid-page / zero crossings) and the
opposite of Pars VI (whole interior mid-page with BOTH ends at leaf edges). The cause here is
structural and worth carrying: **in a 24-page work whose unit is the capitulum, every unit is
a sub-page unit, so every neighbour pair necessarily shares a leaf.** Boundary shape stays
unpredictable work to work — but where the unit is smaller than the page, zero crossings is
the expected shape, not a lucky one.

### (a) Grammatical continuity — all nine PASS

Every receiving chunk opens on its own in-place heading (`### INCIPIUNT CAPITULA`,
`### INCIPIT SPECULATIO PAUPERIS IN DESERTO` + `### Cap. I.`, `### Cap. II.`–`### Cap. VII.`,
`### SCHOLION`), and every ceding chunk ends on a grammatically complete unit —
`EXPLICIT PROLOGUS.` · `EXPLICIUNT CAPITULA` · a closing Scripture quotation ×4 · the Moses
quotation · `ab omni opere, quod patrarat` · `EXPLICIT ITINERARIUM IN DEUM.`

**No cascade-merge signature anywhere**: not one tail fails to parse. `seam-screen.py`
independently reports **0 tail-not-terminal suspects** across all 80 vol5 mid-page boundaries.

### (b) Footer accounting across every shared page — all PASS

Per-page apparatus ownership, derived from the page-qualified `[^pNNN-M]` definitions:

```
295  8  prol:1-8            306  9  c3:1     | c4:2-9
296  6  prol:1-4 | capitula:5 | c1:6      307  9  c4:1-9
297 10  c1:1-10             308  9  c4:1-2  | c5:3-9
298  9  c1:1-9              309  8  c5:1-8
299 10  c1:1-9  | c2:10     310  9  c5:1-5  | c6:6-9
300  7  c2:1-7              311  7  c6:1-7
301  8  c2:1-8              312  9  c6:1-2  | c7:3-9
302  8  c2:1-8              313  6  c7:1-6
303  7  c2:1-2  | c3:3-7    314  0  (no register)
304  6  c3:1-6              315  0  (no register)
305  5  c3:1-5              316  0  (no register)
```

**Every page's register is contiguous `1..N` with no gap, no double-claim and no unowned
page.** Every shared page splits cleanly between exactly the chunks that share it. The
numbers agree with `check-vol5-apparatus.py`'s independently-derived `KNOWN_TOTALS` on all
nineteen pages that carry a register.

★ **p. 296 is the three-way split** — `prol` 1–4, `capitula` 5, `c1` 6 — and n. 5 is the note
recording which codices transmit the capitula table in place, which is the very evidence that
made the table a chunk. The split is doing real work, not bookkeeping.

★★ **pp. 314–316's zero is a POSITIVE result, not a missing read.** The scholion carries no
footer register on any of its three interior leaves, and p. 313's six notes are Cap. VII's
(divided by anchor across the work-unit boundary). This is Vol V's first chunk with no
apparatus at all, and the tooling was verified against the case rather than assumed.

### The work's two ends

- **Opening:** p. 293 half-title, **p. 294 MEASURED blank**, body opens p. 295 (verified at
  the 2026-08-11 mini-pilot). Nothing is inherited from the Breviloquium, which terminates at
  p. 291 with p. 292 measured blank.
- **Close:** p. 316 at *…vel saltem conferat locos a nobis in notis allegatos.*, with
  **p. 317 verified on the plate as *De reductione*'s half-title** (at the scholion's
  scouting). ✅ The long-standing "p. 317/319, span unverified" uncertainty is **closed at
  317**. **Nothing is forwarded past the work's end.**

### Runovers

The ledger's page-crossing total for the corpus is **7, unchanged by this work's close**; two
of them fall inside the Itinerarium (p. 306 n. 9 → p. 307, found at c4; p. 308 n. 9 → p. 309,
found at c5). Both were logged once, by their finders, and neither is double-counted. The
scholion takes a **negative** ledger line — no runover is possible on a chunk with no footers.
`check-vol5-census.py`: rosters agree **89/89**, 73 runovers across 89 chunks.

---

## Pass 4 — disk cleanup

450 dpi page images and colcrop bands are fully regenerable from the gitignored PDF
(`extract-pages.py` + `colcrop.py`, gutters for pp. 295–316 all recorded in repo CLAUDE.md
and in the scouting files). Deleted at the close of this gate: **25 page images (77 MB) plus the colcrop bands (14 MB) — ~91 MB reclaimed.**

---

## Verification suite at the gate

| check | result |
|---|---|
| `check-vol5-apparatus.py` | 89 chunks / **831 entries**, all passed; no PENDING, no GAP |
| `check-vol5-census.py` | rosters agree **89/89**; 73 runovers (66 gutter, 7 page-crossing) |
| `polish-style-scan.py` | vol5 **CLEAN** (89 files); corpus 10 pre-existing PAIR issues in vols III–IV |
| `seam-screen.py --volume 5` | 80 mid-page boundaries, **0 tail-not-terminal suspects** |
| `build-content.mjs` | **2022 / 2022**, 6 books |
| `build-citations.py` | 19,613 records; scholion 35 records / **0 dangling** / 0 QA flags; corpus QA total unmoved at **226** |

## What remains open (none of it blocking, none of it this work's)

1. **QA job 0** — `build-citations.py` resolves an anaphor whose antecedent is an *authority*
   into a fabricated self-reference. Scoped; authorises no `vol*/` edit.
2. The named harmless false positive — Latin *ibidem* in body prose read as a citation
   anaphor. No record is emitted, so nothing is fabricated.
3. The 5-chunk `PAIR` residue in Vols III–IV recorded under pass 2.
4. ~248 dangling cross-refs and ~173 unresolved anaphora, corpus-wide, already a scoped job.

## The gate's own finding

★★ **The gate found nothing wrong with the text, and that is the second consecutive work of
which this is true** (the Breviloquium's gate: 68 boundaries, every finding a wrong *comment*
or a rejected *measurement*, **not one a wrong text**). Here there was not even a wrong
comment. The difference from Vols I–IV, where gates routinely found dropped registers, is
**bands-first apparatus reading plus `check-vol5-apparatus.py` running every commit** — by
the time a gate runs, the defect class it was invented to catch has already been caught.
The gate is now confirming work, not repairing it. **That is an argument for keeping the
cadence, not for relaxing it** — the per-commit checks are what made it cheap.
