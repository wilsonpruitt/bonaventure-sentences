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
| Crossref **`dangling`** | **1 → 0 after the fix below** | **212 → 211** |

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
- **Both corpus findings settled at the plate** and corrected; the pilot corpus now
  reports **0 dangling / 0 QA flags**. Guard-rails re-run after the edits:
  `check-vol5-apparatus` 59 chunks / 487 entries all passed · `check-vol5-census`
  rosters agree · `polish-style-scan` unchanged at 10 issues / 5 chunks, none of them
  an edited chunk (all pre-existing Vol III–IV) · `build-content.mjs` 1992/1992.
- **QA-channel proof** (the plan's explicit verification item). Perturbing a citation's
  digits in the documented confusion classes makes it flag, and the true reading does not:

  | citation | class | result |
  |---|---|---|
  | `IV. Sent. d. 15. p. I. a. 1. q. 1` | true reading | `chunk` → `bon-sent-IV-d15-p1-a1-q1` |
  | `IV. Sent. d. 13. …` | perturbed 5→3 | **`dangling`** |
  | `IV. Sent. d. 45. …` | perturbed 1→4 | **`dangling`** |

- **Non-invasiveness of the TOOL**: `git status` over `vol1..vol5` is empty after every
  extractor run — it never writes to the corpus. (Two chunk files *were* edited in this
  session, by hand, to correct the findings below; that is translation work, not the
  index run.) `build-content.mjs` still reports **1992 questions / 1992 translated**.
  **⚠ CORRECTION (2026-07-31, later the same day): an earlier version of this log, and
  of the resume note, claimed `site/src/data/content.json` was verified "byte-identical"
  via `git status`. That check was VACUOUS — `content.json` is gitignored
  (`site/.gitignore:8`), so `git status` reports it clean no matter what it contains.**
  The substantive claim still holds by other evidence (the extractor opens no file under
  `site/`, and `build-content.mjs` reports the same 1992/1992 before and after), but the
  evidence originally cited did not support it. Recorded rather than quietly fixed —
  this repo's standing hazard is exactly a verification sentence being quoted forward.

## Corpus findings the index surfaced — ✅ BOTH SETTLED AT THE PLATE 2026-07-31

Both were band-read at 450 dpi and 8×, and **both turned out to be OUR transcription
errors, not Quaracchi's** — so both were corrected rather than preserved as cruces.
(The third possible outcome, a sound plate that the sense argues with, would have been
logged as a crux and left standing; cf. this corpus's preserved full stop at p. 249.)

**1. ✅ `bon-brev-p4-c8`, p. 249 n. 6 — `a. 4.` → `a. 1.` (CORRECTED).**
Read on `vol5-p249-R-2` against the `4` of `d. 48.` standing on the line above. The
disputed glyph is a **single upright with an angled flag and a closed stem — no
crossbar, no triangular counter**; the `48` beside it is unmistakably crossbarred with an
open counter. A `1` by this repo's own discriminator. Sense agrees independently: Vol III
d.17 has **two** articles, so `a. 4` cannot exist, and `a. 1. q. 3` is *De illarum
voluntatum concordia vel controversia* — the concord-of-wills doctrine the Hugh quotation
is about. The chunk's `## Notes` had called this register "every digit correct"; **that
verdict is now withdrawn in the chunk itself.**

**2. ✅ `bon-sent-I-d10-a1-q2` `[^4]` — `Vers. 3.` → `Vers. 5.` AND `cod. V` → `cod. U`
(CORRECTED, two errors in one entry).**
Read on `vol1-p197-L-2` (printed p. 197, pdf 299). The digit sets a **flat horizontal top
bar over a single lower bowl** — a `5`; a `3` would set two rounded lobes. Independent
agreement: the anchor sits on `ad Romanos quinto[^4]: «Caritas Dei diffusa est in
cordibus nostris»`, which is Rom **5:5**. **The siglum was wrong too and nothing had
flagged it** — the plate reads `U` (rounded bottom, two serifed uprights), not `V`.
Logged in `d1-d10-polish-resolution-log.md` as a post-gate correction.

**Loop closed:** re-running the extractor after both corrections gives the pilot corpus
**0 dangling and 0 QA flags** (was 1 and 1), and the tier-B record now reads `Rom 5:5`.

### What these two cost, and what they change

- **Finding 1 is a new failure mode for the guard-rails: glyph-correct but target-wrong.**
  The original check verified the glyphs and sense-checked the *distinction*; nothing
  asked whether the *article* exists. No audit could catch it, because no audit knew what
  the corpus contains. The index does. **Reading a digit correctly is not the same as
  reading it rightly.**
- **Finding 2 shows the tier-B channel is worth running deliberately, not incidentally.**
  Both halves of that entry were wrong and both had passed the d.1–d.10 decade gate.
  **Vol I d.1–d.10 deserves a targeted re-sweep of tier-B records against their
  quotations** before further Vol I work — that is a scoped job, not a re-gate.
- **A block-level "clean" verdict is a summary.** p. 249's register was graded the
  cleanest in Pars IV, and its one wrong digit sat inside the sentence saying so —
  a fresh instance of this repo's own rule that the narrative summary is the least
  reliable line in any `## Notes`.

**3. Corpus-wide there are 211 dangling cross-references** in the full-corpus dry run
(212 before finding 1 was fixed). That is the scoped defect list Phase 2 is supposed to
produce; it is **not** worked here. Treat it the way the apparatus backlog was treated —
as jobs, not a blob.

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
