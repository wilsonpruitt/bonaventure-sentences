# Opera Omnia Indexes — Scripture & Cross-Reference (the "Vol X" plan)

> **Provenance:** Fable planning session, 2026-07-31, approved by Wilson. This file is the
> frozen score; execution (Phases 0–2 below) runs in Opus sessions. The Phase 0 pilot runs
> **before** the Pars VI grind (Wilson's timing decision). The Pars VI cold-start hand-off
> in `next-session-resume.md` is untouched and follows after.

## Context

Quaracchi's Vol X is their index volume, and `OPERA-OMNIA-TRACKER.md:45` already scopes it "likely skip." As the translation reaches works with prior English translations (Breviloquium, Itinerarium), the edition's differentiating value shifts to what no prior translation has: **indexes across the whole opera omnia** — every scripture citation, and Bonaventure's dense self-cross-referencing, resolved and navigable in both directions. This plan replaces the skipped Vol X with *generated* indexes that grow automatically as Vols V–X are translated.

Scope decided by Wilson (2026-07-31): **scripture index + self-cross-reference index**, surfaced as **browsable index pages + a cited-by panel** on chunk pages. **Deferred**: clickable inline citations in the reader, authorities index (Augustine/Aquinas/etc.), topical index rerum. **Timing: index pilot runs first**, before the Pars VI grind.

## Ground truth from exploration (what makes this design necessary)

1. **The verse is not where the citation is.** Bonaventure's body cites by ordinal word with no verse (`Ioannis decimo octavo[^2]`); Quaracchi supplies the verse in the footnote (`Vers. 18` — 2,610 occurrences). The join key is the `[^N]` anchor. A scripture index must merge body + apparatus.
2. **Everything is already transcribed** — ~30,850 apparatus entries (Tier-2 = full Quaracchi apparatus), including ~4,150 `Sent. d.` logical refs, ~2,290 `supra pag.` + ~1,270 `tom. N pag.` physical-page refs, 301 `Breviloq`, 106 `Hexaem`, 83 `Itiner`. Nothing new needs transcribing.
3. **Four addressing schemes** must be resolved: logical cross-book (`II. Sent. d. 38. a. 1. q. 2`), relative intra-book (`supra d. 12`, `infra d. 43`, `loc. cit.`, `ibid.`), physical page (`tom. III. pag. 773, nota 5`), and work-relative (`Breviloq. p. V. c. 6` — which maps 1:1 onto the vol5 chunk scheme by design).
4. **Author disambiguation is mandatory**: scholia cite Scotus/Aquinas/Alexander on the *same* Sentences loci in identical syntax (`Scot., I. Sent. d. 1. q. 2.`). A naive regex misfiles these as self-references.
5. **Physical-page refs resolve via `printed_pages` frontmatter, which build-content.mjs discards** — the extractor must read the markdown, not content.json.
6. **The index is also a QA instrument.** The 1/4 and 3/5 digit-confusion class means some committed citation digits are fragile; a resolver that flags dangling refs (`d. 13` where no such quaestio exists but `d. 15` does) mechanizes the documented remedy.

## Frozen design decisions

- **Derived, never hand-tagged.** Zero edits to the 1,994 chunk markdown files. One deterministic Python extractor, regenerated at will — per the repo's frozen rule ("never hand-carry a corpus-wide count — derive it"). Inconsistencies (English colon vs comma citations) are normalized at extraction, not by mass edit.
- **One citations ledger, many indexes.** The extractor emits a single record-per-occurrence ledger; scripture index, cross-ref index, backlinks, and QA reports are all views over it. Authority citations (Scotus etc.) are *captured* in the ledger (class `authority`) but not surfaced — they're free inventory for the deferred authorities index.
- **Latin is the keying side.** Latin citation syntax is systematic (`d. 29. a. 1. q. 2`); English punctuation drifts. Parse Latin apparatus/body; English is display-only.
- **Vulgate numbering is canonical** (it's a Vulgate-based edition; Quaracchi's own index locorum is Vulgate). Book order = Vulgate canon; Psalms keyed by Vulgate number. Display can show the familiar name (`Psalm 24 (25)`) — a display decision, not a data one.
- **Resolution granularity = chunk id.** `ad 2` / `in corp.` / `nota 5` suffixes are preserved as display text on the resolved link, not resolved sub-chunk.
- **Confidence tiers on scripture records**: (A) fully specified `Abbrev. C, V` in apparatus; (B) body ordinal-chapter joined to `Vers. N` via anchor; (C) chapter-only, no verse recoverable → indexed at chapter level, never guessed.
- **Cross-ref records classify as**: `resolved` (target chunk exists), `forward` (target is a work not yet translated — Hexaemeron, sermons; resolves automatically as the corpus grows), `dangling` (target should exist but doesn't → QA flag, candidate digit error), `authority` (governed by an author sigil — excluded from self-crossref).
- **Separate JSON artifacts.** content.json is 54 MB and imported by every page; index data goes to new files under `site/src/data/`, loaded only where needed. Split `index-scripture.json` per book if the pilot shows size problems.
- **Extractor hygiene**: glob `vol{N}/*.md` only (never recurse — `_backup-*` dirs hold 538 stale files); id parser tolerates the optional `-s\d` segment (reuse `tools/seam-screen.py`'s parser); handle both bare (`[^12]`) and page-qualified (`[^p210-1]`) apparatus labels (reuse `LABEL_RE` from `tools/audit-style-formatting.py`); consult `tools/apparatus-sigla.json` / `tools/apparatus_lexicon.py` for existing abbreviation knowledge.

## Architecture

```
vol1..vol5/*.md ──► tools/build-citations.py ──► index/citations.tsv        (ledger, committed)
                          │                          │
        tools/scripture-books.json                   ├─► tools/build-index-json.py
        (canonical table: Vulgate order,             │       ├─► site/src/data/index-scripture.json
         abbrev variants, Latin genitive             │       └─► site/src/data/index-crossref.json
         body forms, English names,                  │
         ordinal-word → number map)                  └─► manual-review/citation-qa-report.md
                                                          (dangling refs, unknown abbrevs,
                                                           unjoined Vers., pages nobody owns)
```

- **`tools/build-citations.py`** — the extractor. Per chunk: parse frontmatter (id, volume, printed_pages), build the corpus-wide printed-page→chunk map, walk Latin body + apparatus + scholion, emit ledger records: `{chunk_id, section, anchor_label, raw_text, class, normalized_target, confidence, resolution}`. Sub-parsers: scripture (forms a/b/c from exploration), logical locus, physical page, work-relative, author-sigil lookback.
- **`tools/scripture-books.json`** — the normalization table. Known variants to encode from day one: `Ps./Psalm./Psal.`, `Eccli.` (Sirach) vs `Eccle.` (Ecclesiastes), `Eph./Ephes.`, `Ioan.` vs `in Ioan.` (commentary, not the gospel), `I./II. Cor.` roman-numeral prefixes, spelled-out short books (`Nahum`), genitive/accusative body forms (`Ioannis`, `Matthaei`, `ad Romanos`, `Actuum`…), ordinal words `primo…centesimo`.
- **`tools/build-index-json.py`** — views over the ledger → the two site JSONs. Scripture: Vulgate-ordered book → chapter → verse → citing loci (chunk id, URL, ≤200-char snippet, section). Crossref: per chunk id, `outbound[]` + `inbound[]` (the backlinks).
- **Site** (no text-reader.tsx changes in this plan):
  - `/scripture` route: book list in canonical order → `/scripture/[book]`: chapter/verse listing with citing loci linked. Server components reading `index-scripture.json`; follow the existing static-export pattern (`generateStaticParams`).
  - **Cited-by panel** on the chunk page (`site/src/app/browse/[bookId]/d/[distId]/q/[qId]/page.tsx`): a server-side section below the reader listing loci that cite this chunk, from `index-crossref.json`. Keeps the 54 MB content path and the client bundle untouched.
- **Build integration**: the two Python tools run before `build-content.mjs` in the deploy recipe (documented in repo CLAUDE.md); artifacts are committed like content.json. Re-run at every pars/work deploy boundary so indexes grow with the corpus. Add a census-style assertion (ledger chunk roster == vol glob) per `tools/check-vol5-census.py`'s pattern.

## Phases

**Phase 0 — Pilot (1 session, next).** Build `scripture-books.json` + `build-citations.py`; run over **vol5 (59 chunks) + vol1 d.1–d.10** (exercises both label styles, both citation cultures, and the ordinal+`Vers.` join). Hand-verify ~50 sampled records against the chunk files (and plates where digits are suspect). Measure: % of scripture records at tier A/B/C, % of cross-refs resolved/forward/dangling/authority. Freeze parser conventions into repo CLAUDE.md § "Index conventions" — the pilot's deliverable is that frozen section plus measured rates, not coverage.

**Phase 1 — Full scripture index.** Extractor over all five volumes → ledger → `index-scripture.json` → `/scripture` pages. Check JSON size; split per book if needed. Deploy (protected, Wilson's OK).

**Phase 2 — Cross-references + cited-by.** Full cross-ref resolution (logical, relative, page, work-relative; author exclusion) → `index-crossref.json` → cited-by panel. QA report lands in `manual-review/citation-qa-report.md`; dangling refs become a scoped defect list (worked like the apparatus backlog — jobs, not a blob). Deploy (protected).

**Ongoing.** Re-run tools at each deploy boundary (one line added to the deploy recipe). Forward refs to Hexaemeron/Itinerarium/sermons resolve themselves as those works are translated — the "cited by" graph thickens for free.

**Deferred (explicitly out of scope now):** inline clickable citations in text-reader.tsx; authorities index (ledger already captures the raw material); topical index rerum (real editorial work, own plan).

## Model plan (per the prudence rubric)

Fable's part ends with this plan. **Phase 0–2 execution = Opus** (deterministic Python + site pages; the judgment-dense parsing conventions get frozen at the pilot). Ambiguous citations the parser can't classify get batched into a manual-review log for an Opus adjudication pass — never guessed inline. Token cost is modest: this is code + verification, not per-chunk LLM work; nothing near the translation grind's budget.

## Verification

- **Pilot**: hand-check the ~50-record sample; resolution-rate metrics reported; every `[^N]` join verified bidirectional on the sample.
- **Non-invasiveness**: `git status` shows no modified files under `vol*/` after any index run; `build-content.mjs` still reports 1992/1992 translated.
- **Site**: `npm run build` in `site/` succeeds (one build at a time — 8 GB machine); spot-check `/scripture`, one `/scripture/[book]` page, and one chunk page's cited-by panel in the static output; confirm content.json byte-identical.
- **Census**: ledger roster diff against `vol{N}/*.md` glob is empty.
- **QA sanity**: at least one known digit-confusion case from CLAUDE.md (e.g. the `IV Sent. d. 15` raw-read-`13` class) reproduced as a dangling-ref flag when artificially perturbed — proves the QA channel works.

## Files

**New**: `tools/build-citations.py`, `tools/scripture-books.json`, `tools/build-index-json.py`, `index/citations.tsv`, `site/src/data/index-scripture.json`, `site/src/data/index-crossref.json`, `site/src/app/scripture/page.tsx`, `site/src/app/scripture/[book]/page.tsx`, cited-by component, `manual-review/citation-qa-report.md`.
**Modified**: `site/src/app/browse/[bookId]/d/[distId]/q/[qId]/page.tsx` (panel), repo `CLAUDE.md` (frozen § Index conventions + deploy-recipe line), `OPERA-OMNIA-TRACKER.md` (Vol X row: "likely skip" → superseded by generated indexes), `next-session-resume.md` (pilot hand-off).
**Untouched**: all `vol*/ *.md`, `content.json`, `text-reader.tsx`.
