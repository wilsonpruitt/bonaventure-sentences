# Index Phase 0 — pilot log (2026-07-31)

Execution of `INDEX-PLAN.md` Phase 0, Opus session, run before the Pars VI grind per
Wilson's timing call. **Deliverable = frozen parser conventions (now in repo
`CLAUDE.md` § "Index conventions") plus the measured rates below — not coverage.**

Pilot corpus: **vol5 (59 chunks) + vol1 d.1–d.10 (89 chunks) = 148 chunks**, chosen to
exercise both apparatus-label styles (`[^12]` vs `[^p210-1]`), both citation cultures
(Bonaventure's own vs the scholia's authority chains), and the ordinal + `Vers.` join.

## Measured rates

| | Pilot (148 chunks) | Full corpus (1,993 chunks, dry run) |
|---|---|---|
| Ledger records | 1,069 | 18,021 |
| — scripture | 308 | 7,009 |
| — crossref | 671 | 11,016 |
| — authority (captured, not surfaced) | 90 | 996 |
| Scripture tier **A** (`Abbrev. C, V`) | **271 (88%)** | 4,862 (69%) |
| Scripture tier **B** (body ordinal ⋈ `Vers. N`) | 31 (10%) | 1,620 (23%) |
| Scripture tier **C** (chapter only) | 6 (2%) | 527 (8%) |
| Crossref `chunk` (fully resolved) | **400 (60%)** | 6,674 (61%) |
| Crossref `distinctio` / `articulus` / `work` | 106 (16%) | 993 (9%) |
| Crossref `page-multi` | 45 (7%) | 1,031 (9%) |
| Crossref `unresolvable` (bare `ibid.`/`loc. cit.`) | 88 (13%) | 1,930 (18%) |
| Crossref `forward` (work not yet translated) | 20 (3%) | 31 (0%) |
| Crossref `ambiguous` | 11 (2%) | 145 (1%) |
| Crossref **`dangling`** | **1 (0.1%)** | **212 (2%)** |

Full-corpus run: **16 s**, 1.9 MB ledger. No performance work needed for Phase 1.

**Reading the numbers.** The two corpora differ where you would expect. The pilot's
tier-A share is higher because Vol V's apparatus is uniformly modern and fully
specified; Vols II–IV carry more of Bonaventure's body-ordinal citation, which is why
tier B triples corpus-wide. `forward` is a Vol V artifact (its nine untranslated works
own most of that volume's printed pages) and nearly vanishes across a corpus that is
otherwise complete.

## Verification

- **815 mechanical claims checked across the whole pilot ledger, 0 failures** — every
  `chunk`-resolved target exists on disk; every `page`-resolved target really carries
  that printed page in its own `printed_pages`; every `page-multi` / `ambiguous` /
  `articulus` member exists; every tier-A/B verse record is well-formed.
- **50-record hand-verification sample** → `citation-pilot-sample.md` (frozen snapshot,
  `--sample 50 --seed 7`). Regenerate with the same seed to reproduce.
- **QA-channel proof** (the plan's explicit verification item). Perturbing a citation's
  digits in the documented confusion classes makes it flag, and the true reading does not:

  | citation | class | result |
  |---|---|---|
  | `IV. Sent. d. 15. p. I. a. 1. q. 1` | true reading | `chunk` → `bon-sent-IV-d15-p1-a1-q1` |
  | `IV. Sent. d. 13. …` | perturbed 5→3 | **`dangling`** |
  | `IV. Sent. d. 45. …` | perturbed 1→4 | **`dangling`** |

- **Non-invasiveness**: `git status` over `vol1..vol5` is empty after every run;
  `build-content.mjs` still reports **1992 questions / 1992 translated**;
  `site/src/data/content.json` byte-identical; `check-vol5-census.py` and
  `check-vol5-apparatus.py` both still green (59 chunks / 487 entries / rosters agree).

## Corpus findings the index surfaced (NOT fixed here — zero edits to `vol*/`)

**1. `bon-brev-p4-c8`, p. 249 n. 6 — `III. Sent. d. 17. a. 4. q. 3.` cannot resolve.**
Vol III d.17 has **two** articles (*De voluntate Christi*, 3 qq.; *De oratione Christi*),
so there is no `a. 4`. The chunk's own `## Notes` record that this citation's digits were
read off the plate and called "every digit correct" — but that check verified the glyphs
and sense-checked *d. 17* only; **nobody checked whether the target exists.**
`a. 1. q. 3` is *De illarum voluntatum concordia vel controversia* — exactly the doctrine
the citing note is about (the Hugh quotation on Christ's two wills). **A 1→4 candidate in
the documented confusion class.** Needs a band read; do not edit on this reasoning alone.

**2. `bon-sent-I-d10-a1-q2` `[^4]` reads `Vers. 3.`; the quotation is Rom 5:5.**
The body sets `ad Romanos quinto[^4]: «Caritas Dei diffusa est in cordibus nostris»`,
which is Romans **5:5**; the note supplies verse **3**. The sibling `[^3]` (`Vers. 22.`
for John 17:22) is correct, so the anchor pairing is sound and only this digit is in
doubt — **a 3↔5 candidate.** Found by reading the tier-B join against the quoted text,
a channel the plan did not anticipate (see the convention frozen in CLAUDE.md).

**3. Corpus-wide there are 212 dangling cross-references (2%)** in the full-corpus dry
run. That is the scoped defect list Phase 2 is supposed to produce; it is **not** worked
here. Treat it the way the apparatus backlog was treated — as jobs, not a blob.

## Parser defects found and fixed during the pilot

Each was found by reading real output against the chunk file, and each is now a comment
in `tools/build-citations.py` at the line that fixes it.

1. **Subset indexing.** Resolution must index the whole corpus even when emitting a
   subset, or the rest of the corpus reads as dangling (72% → 27% at a stroke).
2. **Omitted articulus.** `IV. Sent. d. 15. p. I. q. 1` means `p1-a1-q1`; Quaracchi drops
   a coordinate that is unambiguous in the print. Unstated coordinates are wildcards,
   and a unique survivor resolves.
3. **`dub. N` is sub-chunk.** One `-dubia` chunk holds all a distinction's dubia, so the
   number is display text, not a match coordinate. It had made every `dub. N` dangling.
4. **`tom.` inheritance.** `tom. II. pag. 50, nota 1. et pag. 177, nota 5` states the
   tome once; the bare second page was being measured against the citing volume.
5. **`ibid. pag. N` is a tome marker, not a locus** — it was emitting a duplicate locus
   record pointing at the wrong target.
6. **`supra`/`infra` must not inherit a book**; `ibid. d. N` must.
7. **Colon is not a clause boundary** — it introduces quoted matter still belonging to
   the author just named, and splitting on it misfiled Albert's own numbering as
   Bonaventure's.
8. **`;` separates loci of the SAME author**, so the chain lookback must not stop there
   (whereas `—`, `Cfr.`, `Vide` do).
9. **Chain continuations.** A chain states `Sent.` once and then lists distinctions bare
   (`… II. Sent. d. 2. …; d. 14. …`). Two of three loci in such notes were invisible;
   recovering them added ~9% recall.
10. **Parenthetical asides don't govern.** `… d. 16. per totam (cfr. I. Sent. d. 3 …), …;
    d. 25. p. I.` — the parenthetical moved the continuation into the wrong book.
11. **Inheritance follows the nearest preceding locus of ANY form**, including
    `supra`/`infra`, not just `N. Sent.` ones.
12. **Author governance changes hands mid-note.** The discriminator is whether a siglum
    stands *between* the inherited locus and the continuation (`— B. Albert., hic a. 1.
    et d. 46. a. 11.` = Albert's) or before it (`Aristot., … idem recurrit infra d. 8 …
    et d. 37` = Bonaventure's own). Getting this wrong loses real self-references to the
    authority class in one direction and fabricates them in the other.
13. **Frontmatter ids are quoted.** An id carrying literal `"` can never match a target
    the tool constructs, so work-relative refs silently resolved as `forward` even when
    the chunk was on disk.
14. **`Num. N` without a verse is *numerus*, not Numbers** — see the convention below.
15. **Body-form false positives.** `actuum secundorum` matched as Acts 2 (prefix match on
    the ordinal); fixed with a trailing letter-boundary plus a capitalisation requirement,
    since several body forms are homographs of ordinary Latin nouns.

## Known, measured gaps (deliberately not built)

- **`et p. II. a. 1. q. 3.` continuations** — a chain member that repeats neither `Sent.`
  nor `d.`, continuing the previous distinction with a new pars. Rarer than the `d. N`
  form; left for Phase 2 with eyes open.
- **Sentence-initial `Ibid.`** is not matched (the scanner is case-sensitive). In the
  cases inspected it referred to a patristic *work*, not a Sentences locus, so excluding
  it is the safer default — but it is now a deliberate choice, not an accident.
- **Pars-level citations** (`d. 25. p. I.` with no question) resolve to the distinction;
  the pars survives as display text on the link.
- **Authority citations of non-Sentences works** (Seneca *Epist.*, Anselm *de Processione*,
  Aristotle *de Anima*) are not in the ledger at all — only Sentences-form authority refs
  are. A chunk can therefore hold 18 apparatus entries and contribute zero records; four
  pilot quaestiones do. **The deferred authorities index has substantially more raw
  material than the ledger's `authority` count suggests.**

## Next

Phase 1 (full scripture index → `/scripture` pages) and Phase 2 (cross-refs + cited-by).
`tools/build-index-json.py` is not written yet — the pilot deliberately stopped at the
ledger, since the ledger is what the conventions had to be frozen against.
