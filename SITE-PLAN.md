# SITE-PLAN — the full *Opera Omnia* in digital form

> **The score for the site's redesign.** Drafted 2026-11-06 (Opus), from Wilson's brief: *"we are nearing the end
> of the project … I'm trying to imagine what the full opera omnia will be in digital form, and right now it seems
> inadequate."* Execution runs phase by phase in later sessions. Each phase ends with its verification and rides a
> deploy Wilson OKs **per action**. Push ≠ deploy; the site is a CLI deploy (repo `CLAUDE.md` § "Build and deploy").

## Decisions already made (Wilson, 2026-11-06)

1. **Two primary readers, designed for equally:**
   - **the scholar who cites**: Quaracchi addresses, the Latin, the apparatus, stable links;
   - **the preacher or student who reads**: English first, a way in, Scripture as an entry point
     (*"what does Bonaventure say on John 1:5?"*). The *Collationes in Ioannem* were written for preachers, and
     Vol IX is sermons, so this reader is not an afterthought.
2. **Readable addresses**, with permanent redirects from every current address. Done **once**, before the corpus
   grows much further.
3. **Vol X is NOT transcribed.** It is Quaracchi's index volume, and the site's generated indices are its
   replacement (`INDEX-PLAN.md` already treats it this way). The scope table should say so in place of "Planned".
4. **Design for all of Tomes I–IX now**, proven on paper against the shapes still to come (Phase 5), not retrofitted
   later.

## Where the site is now (measured 2026-11-06)

The site was designed when the project was the *Sentences*, and that shape has carried on for every work since.
- **Data model** (`site/src/lib/content.ts`, built by `site/scripts/build-content.mjs`): `Book → distinctions →
  questions`. Every work is forced into it. A Vol V/VI work is a `Book` whose "distinctions" are its divisions
  (`WORKS` registry: slug, book id, `divisionLabel`, division titles). 18 books, 335 divisions, ~2,300 chunks.
- **Addresses:** `/browse/{bookId}/d/{distId}/q/{chunkId}`, e.g. `/browse/18/d/4/q/bon-cioan-c4`. "18" is an
  internal id, and `d`/`q` mean distinction and question. Also `/browse/tome/{N}`, `/scripture/{book}`, `/search`,
  `/progress`, `/about`, `/rights`, `/export`.
- **Static export** (`output: "export"`). `src/data/content.json` is **75 MB**, `index-crossref.json` 3.5 MB,
  `src/data/scripture/` 8.3 MB.
- **Reader** (`…/q/[qId]/text-reader.tsx`): parallel / Latin / English views and a page-marker mode (off / margin /
  inline). Good, and it stays.

**What's inadequate, in order of reader cost:**
1. **Previous/next stops at every division boundary.** 96 of 335 divisions hold one chunk, so they have no
   previous/next link at all. That covers every collatio of the *Hexaëmeron*, *De septem donis* and *De decem
   praeceptis*, every quaestio of *De scientia Christi*, 21 of 22 Wisdom chapters, and every *Collationes in
   Ioannem* chapter. Reading a work start to finish means going back to its index page each time.
2. **Search indexes only the first 500 characters** of each chunk's Latin and English (`src/app/search/page.tsx`).
   On a 10-page chunk that's under 5% of the text.
3. **Sentences vocabulary everywhere:** "N questions · M translated" under a *Collationes* chapter, "X of Y
   questions translated" on every card, "Distinctions" as the default heading, `d`/`q` in every address.
4. **The home page contradicts itself and the data:**
   - the intro says Vol V is complete and Vol VI is in preparation, but the scope table says V is "In
     preparation" (its gloss lists 4 of its 11 works) and VI is "Planned";
   - the paragraph above the table says "four complete, the fifth in preparation";
   - the meta description says "Currently presenting Volume I";
   - the footer appeal says "the commentary on the Sentences has never been fully translated".
5. **There is no work as an object.** No page says what a work is, where it sits in Quaracchi, what its parts
   are, or how to cite it. Tomes are the main grouping, though they are physical, not intellectual.
6. **Long chunks have no contents and no anchors.** A *Collationes* chapter holds up to ten units, and a
   *Collat. N* cross-reference lands at the top of a 10-page chunk.
7. **Look-up is missing.** A scholar holding *I Sent. d. 3 p. 1 a. 1 q. 2* or *tom. VI pag. 567* can't go
   straight there, though `tools/build-citations.py` already resolves every one of these forms and already knows
   which chunk owns each printed page (`by_page`).
8. **Connections stop at Scripture and self-citation.** The authorities have no index: Augustine, Aristotle,
   Dionysius, the Gloss, the Patrologia columns. ⚠ **The ledger does NOT already hold them.** It has **1,166
   `authority` records against 19,851 scripture and 12,596 crossref**, because the extractor records an author
   mainly where one is needed to keep a citation chain straight. An authorities index is **new extraction work**
   (Phase 4). Also, `Comment. in Ioan.` references produce zero records (gate item W10), so the Commentary and the
   *Collationes* on the same Gospel don't yet link to each other.

## The shape of the edition

**Three ways in, over one set of addresses.**
- **READ.** Every work is a continuous text. A landing page gives its structure; previous/next runs through the
  whole work and then on to the next work in the tome. Long chunks get a contents box and section anchors.
  English-first for the reading reader, parallel for the scholar (the reader already has both).
- **LOOK UP.** A "go to" box takes any Quaracchi citation form to the passage. `/tome/6/page/567` resolves a
  printed page. Every page carries "cite this" with the tome and page.
- **FOLLOW.** The indices that replace Vol X: Scripture (exists), Bonaventure citing himself (exists, as cited-by
  backlinks), the authorities (new), full-text search over everything (fixed). Every cross-reference that names a
  unit inside a chunk (*Collat. 18*, *n. 12*) lands on its anchor, not at the top of the chunk.

### Address scheme (Phase 2)

**Rule: the unit segment is DERIVED from the frozen chunk id, never hand-assigned.** The chunk ids are already
permanent, so an address derived from them is too.

| content | new address | from chunk id |
|---|---|---|
| Sentences quaestio | `/sentences/1/d3/p1-a1-q2` | `bon-sent-I-d3-p1-a1-q2` |
| Sentences littera / divisio / dubia | `/sentences/1/d3/littera` · `…/divisio` · `…/dubia` | `…-d3-littera` etc. |
| Sentences distinction | `/sentences/1/d3` | (division page) |
| work chunk | `/{slug}/{unit}`: `/breviloquium/p5-c6` · `/hexaemeron/c4` · `/ioannem/c1-v1-2` · `/collationes-ioannem/c4` | id minus its prefix (`bon-brev-`, `bon-hex-`, `bon-ioan-`, `bon-cioan-`) |
| work landing page | `/{slug}`: `/breviloquium`, `/collationes-ioannem` | registry slug |
| a unit inside a chunk | `/collationes-ioannem/c4#coll-18` · `#annot-22` · `#n-12` (Quaracchi ¶ number) · `#p556-8` (a footnote) | from `### Collatio N.` / `### Annotatio N.` / ¶ heads / footnote labels |
| a tome | `/tome/6` | |
| a printed page | `/tome/6/page/567` → the owning chunk (a short list if two chunks share the page) | `by_page` |
| indices | `/scripture` (kept) · `/authorities` (new) · `/search` (kept) | |

- **Slugs are the registry's Latin slugs** (`ioannem`, `sapientiam`, `collationes-ioannem`), which are frozen in the
  data and how scholars cite the works. Each landing page shows the English title. *(Wilson can override; see
  Questions.)*
- **Redirects:** `vercel.json` **pattern rules**, one or two per book (~25 in all), not one per chunk. For example,
  `/browse/18/d/:d/q/bon-cioan-:unit` → `/collationes-ioannem/:unit`, and
  `/browse/1/d/:d/q/bon-sent-I-d:n-:unit` → `/sentences/1/d:n/:unit`. The phase's verification enumerates **every**
  old address from the last-deployed `content.json` and confirms each resolves to a 200 page. ⚠ Check at phase start
  that Vercel serves `vercel.json` redirects for a `--prebuilt` static deploy. If not, the fallback is static
  redirect stubs (meta-refresh + `rel=canonical`) generated at the old paths.
- `rel=canonical`, sitemap and the JSON-LD `@id` all move to the new addresses in the same deploy.

## Phases

Each phase: build → verify (the checks listed) → Wilson's per-action OK → deploy, at most 1–2 deploys a day
(NOW.md). A phase that touches `build-content.mjs` or the `WORKS` registry must not run while a chunk builder is
active (they edit the same file). The chunk loop pauses for it, or the phase lands between chunks.

**Phase 0: the fixes that need no design (rides the held p. 634 *Collationes* deploy).**
- Previous/next across divisions within a work, then on to the next work in the tome.
  *Verify: every chunk page links forward except the last chunk of the last work in a tome.*
- Full-text search over all the text. **Pagefind**, run over the static export after `next build`. It indexes the
  rendered pages into a split index fetched on demand, so it scales to the 75 MB corpus, with filters for work,
  tome and language. Add it as a post-build step so `npx vercel build --prod` runs it.
  *Verify: a recall test, 30 phrases sampled from the second half of random chunks across all volumes, every one
  found.*
- The home page, meta description and footer brought into line with the data. Derive the scope table from the
  registry and `progress.json`, not hand-written rows. Vol V complete; Vol VI with its four works and their status;
  Vol X as "Indices: replaced by this site's generated indices", linking to them. ⚠ **The footer appeal and the
  home intro are Wilson's voice and outward-facing: draft them, and Wilson approves the wording.**

**Phase 1: work-aware reading.**
- **Unit nouns.** Add `unitLabel` (singular/plural: "question", "chapter", "pericope", "collation", "sermon") to
  each `WORKS` entry, with the Sentences default "question". Replace every "N questions · M translated" and "X of Y
  questions translated" with the work's own noun. Rename the internal `distinctions`/`questions` fields only if it
  is cheap. The display is what matters.
- **Work landing pages:** Latin and English title, genre, Quaracchi tome and page span, structure as a table of
  contents (divisions → chunks → in-chunk units), status, how to cite. **Factual headers only for now**; an
  editorial introduction per work is a separate prose decision (see Questions).
- **In-chunk contents box + anchors**, from `### ` headings, Quaracchi ¶ numbers where a work numbers them
  (Itinerarium, *Ioannem*, *Collationes*), and footnote labels. Shown when a chunk has 3+ sections or runs past ~3
  printed pages.
- **"Cite this":** author, work, Quaracchi tome, page(s), unit; the translation's name, licence (CC BY-NC 4.0, per
  memory `wroot-press-licensing`) and URL.
  *Verify: every chunk renders; anchor ids unique per page; the contents box matches the headings.*

**Phase 2: the address migration (its own deploy).** The scheme and redirects above, plus a sitemap,
`rel=canonical` and JSON-LD. *Verify: the enumerate-every-old-address check (100% → 200); internal links contain no
`/browse/…/d/…/q/` paths; the search index rebuilt on the new addresses.*

**Phase 3: look-up and landing on the unit.**
- **The go-to box:** `tools/build-citations.py` (or a sibling) emits `goto.json`, a normalized-key → address table
  for every chunk, in-chunk unit and printed page. A small client parser normalizes what a reader types (*I Sent.
  d. 3 p. 1 a. 1 q. 2* · *Brevil. p. V c. 6* · *Collat. in Ioan. coll. 18* · *tom. VI pag. 567*) into a key, using
  the same abbreviation table the ledger uses (`tools/scripture-books.json` `works`).
  *Verify: 200 ledger records with `resolution=chunk`, raw text fed to the parser, ≥98% land on the ledger's own
  target; every miss explained.*
- **`/tome/N/page/M`.**
- **Anchor-level cross-references:** the ledger gains an `anchor` column where the citation names a unit inside the
  chunk (`Collat. 18` → `#coll-18`; `n. 12` → `#n-12`), and cited-by and inline links use it.
- **Close W10:** a `works` entry for `Comment. in Ioan.` (chapter + paragraph → pericope chunk through the
  `paragraphs:` frontmatter of ruling 73), so the Commentary and the *Collationes* link to each other.

**Phase 4: the authorities index (new extraction; one conventions pilot first).**
- The judgement-dense part: an **authority normalization table**. Author sigla → canonical author; work titles →
  canonical work (Augustine's ~100 works under their many Quaracchi abbreviations); locus forms (book/chapter, PL/PG
  column). This is a conventions pilot in the `INDEX-PLAN.md` Phase 0 mold, frozen before any volume run. Then
  deterministic extraction over the La halves of every apparatus entry, ledger class `authority` filled out, and
  `/authorities` pages (by author → work → locus → the citing chunks).
  ⚠ **Big-token hard stop:** price the full pass after the pilot, before running it.
  *Verify: a hand-checked sample per volume; the scripture and crossref counts unchanged.*
- The `INDEX-PLAN.md` "Deferred" list (inline clickable citations in the reader; the *index rerum*) stays deferred
  unless Wilson promotes it.

**Phase 5: paper-test the model against Tomes VII–IX (before their pilots, not after).**
- **VII, the Luke commentary:** expected to be the *Ioannem* shape (pericope + quaestiones). Confirm the
  `pericope` unit, `paragraphs:` and the landing page carry over unchanged.
- **VIII, the further opuscula:** expected to be **many short works in one tome**. The tome page must work as a
  catalogue (grouped, with a one-line gloss each), and a one- or two-chunk work still gets a landing page.
- **IX, Sermones:** the new shape. A preacher's way in is **the liturgical calendar** (Sunday/feast) and the
  sermon's **thema verse**, so expect frontmatter fields like `liturgical_day:` and `thema:` decided at its pilot,
  and a calendar index beside the Scripture index. ⚠ This is the one place the second reader changes the data
  model. The Vol IX mini-pilot decides it; this plan only reserves the space.
  *Output: a short addendum to this file (the shapes checked, anything the scheme can't hold), no code.*

## Model plan (per `reference_model-prudence-rubric`)

This plan is the score. **Phases 0–3 are pattern-following execution:** Opus for the reader and data-model work,
Sonnet adequate for Phase 0's copy and labels. **Two places need real judgement:** the Phase 4 authority
normalization pilot, and the Phase 5 sermon model (folded into the Vol IX pilot). The rest should not need it.

## Answered (Wilson, 2026-11-06)
- **Q1 slugs → LATIN** (`/ioannem`, `/sapientiam`, `/collationes-ioannem`); English titles shown on each landing page.
- **Q2 home intro + footer appeal → written by a Bonaventure scholar** Wilson commissions, not drafted by Claude.
  Phase 0 still corrects the FACTS (scope table, meta description), but leaves the prose slots for the scholar's
  text. ⚠ The footer's donation tier labels (`$10 — a distinction`, `$100 — a decade`) are Sentences-shaped too.
  The labels are text, but they sit on live Stripe Payment Links: change the wording only, never the links, and
  only with Wilson's OK.

## Questions for Wilson (none blocks Phase 0) — Q1 and Q2 answered above

1. **Slug language.** Latin registry slugs (`/ioannem`, `/sapientiam`), as recommended, or English (`/john`,
   `/wisdom`)? Latin matches how the works are cited and is already frozen in the data. English reads more
   easily for the second reader.
2. **The home intro and footer appeal:** you write them, or I draft and you approve?
3. **Work introductions:** factual headers only (recommended for now), or a short editorial introduction per work?
   The second is real prose, at ~30 works by the end, and it's your voice.
4. **Phase order after 0:** as written (1 → 2 → 3 → 4), or the address migration (2) first, so nothing new is built
   on old addresses? Recommend **2 right after 0**: every later phase then builds on the final addresses.

## Files this plan will touch

`site/src/app/**` (routes, home, layout), `site/src/lib/content.ts`, `site/scripts/build-content.mjs` (`WORKS`
`unitLabel`), `site/vercel.json` (new: redirects), `site/package.json` (Pagefind), `tools/build-citations.py`
(`anchor` column, `goto.json`, W10 `works` entry, authorities), `tools/scripture-books.json`, `INDEX-PLAN.md` (Vol X
decision + Phase 4 cross-reference), repo `CLAUDE.md` (a § "Site conventions" once Phase 2 freezes the scheme).
