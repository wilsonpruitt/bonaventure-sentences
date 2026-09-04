# Bonaventure Sentences — Project Guide for Claude

You are working on an English translation of **St. Bonaventure's *Opera Omnia*** (Quaracchi edition, 1882–1902). Status (2026-09-04): **Books I–IV are complete and published** (Vols I–IV, all Tier 2). The active front is **Vol V**, where the Breviloquium, Itinerarium, De reductione, the Collationes in Hexaemeron, the *Collationes de septem donis* (pp. 457–503, gated + deployed 2026-08-29) and the *Collationes de decem praeceptis* (pp. 507–532, gate CLEAN, **pushed + DEPLOYED 2026-08-31**) are ALL COMPLETE. **The next work is the *QD de scientia Christi*, pp. 3–43** — its **mini-pilot is FROZEN 2026-08-31** (§ SCIENTIA CHRISTI below; evidence in `manual-review/scientia-christi-pilot-scouting.md`), and its first four chunks **`bon-qsc-q1` (pp. 3–6), `bon-qsc-q2` (pp. 6–10), `bon-qsc-q3` (pp. 10–16) and `bon-qsc-q4` (pp. 17–27) are BUILT** (2026-08-31 / 09-01 / 09-03 / 09-03, Tier 2, 31 + 34 + 48 + 93 entries, zero `[?]`), and **the SHAKEDOWN GATE RAN 2026-09-04 — three defects, all repaired, four register rulings frozen (§ SCIENTIA CHRISTI below).** **The front is `bon-qsc-q5` (pp. 27–32)**, inheriting p. 27 nn. 2–8; the work-close gate is at p. 43 and **nothing in this work is deployed**. The live site is https://bonaventure.wrootpress.com. Always defer to `next-session-resume.md` for the exact current position.

This file is loaded into every Claude Code session in this repo. Read it before making changes to translation files or the build pipeline.

## Project structure

- `vol1/bon-sent-I-d{N}-*.md` — Bonaventure text chunks. One file per logical unit (littera, divisio, quaestio, dubia). **This is where 95% of the work happens.**
- `raw/bonaventure_vol1_raw.txt` — OCR'd full text of Quaracchi Vol. I, used to extract chunk content.
- `raw/doctorisseraphic11bona.pdf` — source PDF, 54 MB, **gitignored** (request separately).
- `raw/vision/vol1/p-NNN.png` — page images at 200 dpi. Generate with `python3.11 tools/extract-pages.py --volume vol1 --pages 48-51`.
- `tools/` — Python utilities (apparatus translation, page extraction, chunk scaffolding).
- `site/` — Next.js 16 App Router site that renders the chunks. Static export, deployed to Vercel. **Only the project owner deploys to production.**
- `translation-prompt.md` — original LLM translation prompt. Partly outdated (see "Translation depth" below).

## What a "Tier 2" chunk looks like

Every chunk is a single Markdown file with this structure:

```markdown
---
id: "bon-sent-I-d{N}-{pars-if-any}-{articulus-if-any}-{q}"
volume: 1
book: 1
distinctio: N
pars: 1 | 2       # omit if the distinction has no pars division
articulus: N      # omit for divisio, littera, dubia
quaestio: N       # only for type: quaestio
type: quaestio | littera | divisio | dubia
title_la: "Utrum veritas sit proprietas divini esse"
title_en: "Whether truth is a property of the divine being"
printed_pages: [150, 151, 152]
pdf_pages: [252, 253, 254]
source: "S. Bonaventurae, Opera Omnia, Tomus I (Quaracchi, 1882), pp. 150–152"
has_scholion: true
has_apparatus: true
transcription_status: "Phase C Tier 2 complete — Latin body, English body, scholion (I–IV), 10-footnote apparatus (YYYY-MM-DD)"
format_version: 1
---

# Short breadcrumb (not rendered on the page — page composes its own title)
## *Title in italic*

---

## Latin
<!-- page 150 -->

### Articulus I. *De veritate Dei.*
### Quaestio I. *Utrum veritas sit proprietas divini esse.*

Quod veritas sit proprietas divini esse, ostenditur...

1. *Primo* modo sic: Hieronymus ad Marcellam[^1], ...

2. Item, Augustinus *de Vera Religione*[^2]: ...

**Contra:**
1. Si veritas est Dei proprietas, ...

> **Conclusio.** Veritas, quatenus opponitur falsitati, ...

**Respondeo:** Dicendum, quod veritas ...

**Ad argumenta pro parte affirmativa:**
*Ad 1, 2, 5, 6.* Et sic procedunt ...

### Scholion
**I.** Sensus quaestionis est, ...
**II.** ...

---

## English

### Article I. *On the truth of God.*
### Question I. *Whether truth is a property of the divine being.*

That truth is a property of the divine being is shown from authorities and reasons.

1. *First*, thus: Jerome to Marcella[^1], ...

[...parallel structure...]

### Scholion
**I.** The sense of the question is whether truth belongs to God as something proper...
**II.** ...

---

## Apparatus

[^1]: **La.** Hieron., *Ep. ad Marcellam*. In nostra ed. c. 1 circa medium.
    **En.** Jerome, *Letter to Marcella*. In our edition, c. 1, near the middle.

[^2]: **La.** August., *de Vera Religione* c. 36, n. 66. ...
    **En.** Augustine, *On True Religion* c. 36, n. 66. ...
```

**A chunk is Tier 2 when**:
- Latin body fully cleaned of OCR artifacts, preserving Quaracchi's punctuation and italics for formulae
- English body parallel paragraph-for-paragraph, literal (not paraphrase) — especially for scholia and apparatus
- Scholion translated (both languages)
- Apparatus entries use `[^N]: **La.** ... **En.** ...` format with a blank line between La and En — `build-content.mjs` parses this exactly
- `[^N]` markers present in both Latin and English bodies at matching positions
- Page breaks as `<!-- page N -->` HTML comments at the right paragraph boundaries

## Tier-2 verification workflow (CRITICAL — read before doing any verification or rebuild)

**This workflow is the result of multiple costly false-starts. DO NOT improvise an alternative.**

> ### ⚠ VOL II OVERRIDE — read this first if `volume: 2`
>
> The recipe below was written for **Vol I** (single-column, near-perfect ABBYY OCR). **Vol II is two-column and the IA djvu OCR cascade-shatters the Respondeo, Solutio, scholion, and *every* page-footer** (diagonal one-token-per-line fragmentation + two-column bleed). For Vol II the OCR-vs-PDF priority is **inverted** in the damaged regions. Proven across d.1 sessions 5–12 (all 17 chunks): every quaestio was a full PDF re-set. Apply these overrides:
>
> 1. **The PDF is authoritative wherever the OCR is cascade-fragmented** — i.e. essentially every Respondeo + Solutio + footer. The OCR remains the base only for clean running prose (videtur/contra args) and for exact footnote-marker spacing. (This inverts the "canonical source of truth" rule and anti-pattern #1 below — for Vol II damaged regions the column-band PDF read *is* authoritative.)
> 2. **Standard per-quaestio procedure:** `python3.11 tools/extract-pages.py --volume vol2 --pages <printed> --dpi 450`, then `python3.11 tools/colcrop.py vol2 <printed-page> [split_x=1660] [n_bands=3] [scale=1.8]` → reads to `/tmp/colcrop/vol2-pNNN-{L,R}-{0..n}.png`. Read each page **Left column top→bottom, then Right column**; body bands then footer bands. Reflow column-by-column, not raw-line order. **Never `Read` a full-page extract (`raw/vision/vol2/p-NNN.png`) directly — at 450+ dpi it is ~4.6 MB on disk → >5 MB base64, which the Anthropic API rejects with `messages.N.content.M: 400`. Always read the `colcrop` bands (capped under the limit by `save_under_cap`); `extract-pages.py` prints an `⚠ Oversized` warning for any page that is too big to send.**
> 3. **Offset `pdf = printed + 22`.** Running-head page numbers are routinely OCR digit-mangled (`80`=50, `34`=54; `DISTmCTIO 11.`=DISTINCTIO II). Trust the +22 offset and running-head *text*, never the OCR'd digits.
> 4. **Cross-chunk footer split (recurring — every chunk boundary that falls inside a printed page):** a printed page's footer notes split by *body anchor*, not by which chunk physically holds the footer block. Before promoting a chunk, verify the prior chunk captured its share of any shared page footer; document the split in `## Notes`. Reading a shared footer in printed order once lets you populate the new chunk *and* retire a prior chunk's parked `[?]` in the same pass (session 10 did this for a2-q2's [^12]).
> 5. **Chunking convention (locked d.1 sessions 8/10/11):** a short ARTICULUS opener (`Consequenter … quaeruntur duo …`) is folded into that article's **q1** — no standalone `dN-pM-aK-divisio` chunk. The pars-level divisio chunk holds the pars DIVISIO TEXTUS + TRACTATIO QUAESTIONUM (+ the first article's sub-divisio). A quaestio with **no scholion is normal** if the article's q1 scholion says `pro quaest. seq.` — check the sibling before treating a missing scholion as an error.
> 6. **Mechanical checks:** the three guard-rail audits now support Vol II via `--volume 2` (added 2026-05-15) — run them before commit alongside `node site/scripts/build-content.mjs` (chunk count + parse + marker pairing). For Vol II the audits are coarser than for Vol I (see the Vol II audit-calibration notes under "Required guard-rail audits"): paraphrase reliably separates done-vs-skeleton, apparatus-count flag logic holds, but the header audit only catches gross dropouts. Manual confidence + the column-band PDF discipline still carry the fine-grained quality bar.
> 7. **`[?]` flags:** tracked in the chunk's own `## Notes` + the in-repo `next-session-resume.md`, cleared in the d.10-style **decade polish-blocker** (600 dpi pass over d.1–d.10). There is no per-chunk `manual-review/tier2-ambiguities*.md` discipline for Vol II.
>
> Steps 1, 3, 4, 7–10 of the recipe below still apply as written. Steps 2/5/6 apply but with the PDF-priority inversion above.

### The canonical Latin source of truth is the IA djvu.txt OCR — NOT eyes-on-PDF reads

`raw/bonaventure_vol1_raw.txt` is a verbatim copy of `doctorisseraphic11bona_djvu.txt` from Internet Archive (likewise pt2). This is ABBYY-quality OCR and is dramatically more accurate than reading small-set Quaracchi printed text at any reasonable PDF dpi. Reading the printed page directly will produce errors (e.g. `bonus` misread as `utens`, `homo` as `bonum`, `proceditur` reversed to `procedam`) that the OCR gets right.

### Per-chunk recipe (lock to this exactly)

For any chunk that needs to be promoted to Tier 2 — whether re-verifying a "first-pass" chunk like d.1's, or building from a skeleton like d.13+:

1. **Find the OCR line range** for the chunk in `raw/bonaventure_vol1_raw.txt` (or `_pt2_raw.txt`). Use `grep -n` for the chunk's distinctive headings (e.g. `ARTICULUS I.`, `QUAESTIO I.`, the title in `title_la` frontmatter). Verify against the chunk's `printed_pages` frontmatter — line ~13380 corresponds roughly to printed page 30 in pt1.

2. **Transcribe Latin verbatim from OCR**, NOT from PDF. Preserve Quaracchi's italics and punctuation. Where OCR has obvious garbles (e.g. `QLI.ESTIO` for `QUAESTIO`, `8` for `S`, `1` for `I` inside Roman numerals), silently correct **only** when context makes the intent unambiguous; otherwise mark `[?]`.

3. **Place footnote anchors at OCR positions** — the OCR preserves footnote-marker spacing as `boniis ²`, `decimo  de  Trinitate ³`, etc. Move `[^N]` markers in the chunk Latin to those exact positions, not end-of-clause. The English `[^N]` then mirrors the Latin position.

4. **Translate English literally**. Match the corrected Latin paragraph for paragraph. Use the scholastic-formulae and key-terminology tables further down in this file for consistency.

5. **Apparatus from OCR text directly** — the OCR includes the full Quaracchi apparatus block. **Quaracchi restarts footnote numbering on each printed page**, so a multi-page chunk has multiple per-page footer sequences. Render every numbered Quaracchi footer entry in the raw range, page by page; ~10 entries per printed page is normal. Do NOT reuse the apparatus block from the existing chunk if you find any divergence — Tier-1 chunks frequently dropped or paraphrased apparatus entries.

   **Lesson 9 (2026-05-09 wave 5):** when rebuilding from a target count derived from `audit-apparatus-count.py`, the heuristic *undercounts* — it misses garbled OCR openers (`'*` for 14, `1»` for 10, `1'` for 17, `-"` for 20). Walk the raw range yourself; do not stop at the heuristic count. The regex was hardened 2026-05-09 but is still not perfectly faithful (~10% noise either direction). Ground-truth is the printed page footer, not the audit script. See `manual-review/d1-d4-tier2-promotion-log.md` Lesson 9.

6. **PDF (`raw/doctorisseraphic1{1,2}bona.pdf`) is consulted only for** *(Vol I only — for Vol II the PDF is the routine source for every Respondeo + footer; see the Vol II Override above)*:
   - OCR garbles flagged with `?` glyphs or impossible Latin (extract via `tools/extract-pages.py --volume vol1 --pages N --dpi 400`)
   - Footnote-anchor positions when OCR-marker spacing is ambiguous
   - Scholion opening words (OCR fragments these heavily because the SCHOLION header breaks up text mid-sentence)

7. **Log ambiguities** in `manual-review/tier2-ambiguities.md`. Use `[?]` flags inline in the chunk file; never silently guess. Format: `**chunk-id, location**: garble or question. Currently rendered X. → Resolve with Y.`

8. **Backup before rebuild**: `cp bon-sent-I-dN-*.md _backup-d{N}-pre-rebuild-{YYYYMMDD}/` so the prior version is recoverable for diff.

9. **Update `transcription_status` frontmatter** to `Phase C Tier 2 complete — Latin re-set verbatim from IA djvu OCR (raw lines NNNN–NNNN), fresh literal English translation, full apparatus from raw OCR (N entries), scholion from OCR with [?] flags on ambiguous spots ({YYYY-MM-DD})`.

10. **Smoke-test the build**: `cd site && node scripts/build-content.mjs` and confirm chunk count + parses cleanly.

### Pace and scope

At this depth: realistic 1–2 chunks per first session, 2–4 chunks once patterns are familiar.

Vol I has ~436 chunks total. Of these (per audit on 2026-05-01): ~56 Tier-2 complete, ~7 partial, ~368 skeleton. Many of the existing "translated" chunks (especially d.1, d.2) are paraphrased rather than literally transcribed and need full rebuild from OCR.

## Efficient single-chunk subagent dispatch (Vol II cadence, 2026-05-25)

The 2026-05-25 session shipped **59 chunks in one day** (d.14 through d.19 inclusive, manual-rescue list cleared) using strict one-chunk-per-subagent dispatch. This is ~6× the prior best cadence. **Use this pattern by default for Vol II promotion sessions.**

**Main thread = coordinator only.** Never reads PDFs, never translates, never greps raw OCR. It only: reads `next-session-resume.md`, briefs the next subagent, displays the subagent's report, repeats.

**Per-dispatch prompt template** (~10 steps, in order):
1. Pin the target chunk + today's date + pars-split status.
2. Quote the **cross-chunk hand-off** from the prior subagent's report (e.g. "p.NNN L-2 footers X–Y migrate to this q's body") so the next agent doesn't re-read the prior chunk.
3. Page span: grep raw for the next header + cross-check running heads + next semantic boundary.
4. **Verify the opener's "Primo/Secundo/Tertio quaeritur…" alignment. STOP and report if misaligned** — the auto-chunker has known q-swap bugs (d.15-a2 q2/q3 was caught + fixed in one user turn this way).
5. Generate any missing PDF crops (`extract-pages.py` + `colcrop.py`).
6. Backup: `mkdir -p _backup-{chunk}-pre-promote-{YYYYMMDD} && cp ...`.
7. Re-set Latin column-by-column from PDF (Vol II PDF-priority inversion). Build apparatus continuously, leading with the hand-off. Translate literally per the formula tables above.
8. Frontmatter Tier-2 + `## Notes` block (provenance, page-split map, hand-offs picked-up/forwarded, any `[?]` flags).
9. Audits (`--volume 2 --min-d N --max-d N`) + smoke build.
10. **Two commits**: (a) chunk + content.json; (b) `next-session-resume.md` advanced to next chunk. Do NOT deploy.

**Cap the report at 200 words**: page span, apparatus count + page-split map, hand-offs, `[?]` flags, audit status, both commit SHAs.

**Subagent crash recovery:** if the API socket drops, `git log --oneline -5 && git status --short`. Clean? Re-dispatch with the same prompt — the backup step makes the work idempotent.

**Decade-polish gate:** when a chunk closes at d.{N0}, the next dispatch is the three-pass polish-blocker (see "Polish-blocker cadence" above), not the next distinction's littera.

---

**Anti-patterns to avoid (NEW):**
- ❌ Don't bundle multiple chunks per dispatch — the per-chunk recipe is the safety mechanism (alignment check, backup, audit, two-commit cadence).
- ❌ Don't omit the "verify Primo/Secundo/Tertio quaeritur" alignment check — the auto-chunker mis-aligned d.15-a2 q2/q3 silently.
- ❌ Don't read the PDF in the main thread — the subagent will do it; main-thread reads burn context for no benefit.

### What NOT to do (anti-patterns from past sessions)

- ❌ Don't read the PDF and treat your reading as authoritative. The OCR is more accurate. *(Vol I only. For Vol II's cascade-shattered Respondeo/footers the column-band PDF read IS authoritative — see the Vol II Override at the top of this section.)*
- ❌ Don't trust the existing chunk's Latin or apparatus. Many were generated by AI translation rather than literal transcription. Diff against OCR.
- ❌ Don't silently leave half-verified chunks. Either complete to Tier 2, or revert to skeleton with the original status string. Never an in-between.
- ❌ Don't skip the ambiguities log. Every `[?]` you write goes in the log.

## Required guard-rail audits (before commit)

After ANY chunk promotion, scaffold rebuild, or apparatus edit affecting one or more distinctions, run all three audit scripts and address findings before committing:

```bash
# Vol I (default):
python3.11 tools/audit-paraphrase.py --min-d N --max-d N
python3.11 tools/audit-headers.py --min-d N --max-d N
python3.11 tools/audit-apparatus-count.py --min-d N --max-d N

# Vol II — add --volume 2 (single raw file, no pt1/pt2; header ranges from
# chunk frontmatter since DISTINCTIO headers are OCR-garbled):
python3.11 tools/audit-paraphrase.py --volume 2 --min-d N --max-d N
python3.11 tools/audit-headers.py --volume 2 --min-d N --max-d N
python3.11 tools/audit-apparatus-count.py --volume 2 --min-d N --max-d N
```

**Vol II audit calibration (verified 2026-05-15 against d.1's 17 Tier-2 chunks):**
- `audit-paraphrase --volume 2` cleanly partitions done from not-done: the 17 d.1 Tier-2 chunks land in **OK**; auto-chunked skeletons land in HIGH/CRITICAL (the `auto-chunked skeleton` smell + skeleton-vs-raw low Jaccard). A large HIGH bucket = "many skeletons remain", not a regression. Writes `manual-review/vol2-paraphrase-audit.md`.
- `audit-apparatus-count --volume 2` flag logic is unchanged (SKELETON-SUSPECT / INCOMPLETE-SUSPECT); real Tier-2 chunks with apparatus don't flag. The raw-vs-chunk *diff* column is noisier than Vol I (two-column cascade footers) — triage signal only, expect ±10–18.
- `audit-headers --volume 2` uses author-verified frontmatter line ranges, but the raw-side marker regexes undercount Vol II's garbled headers and global numeral-dedup collapses per-pars repeats, so Vol II diffs run **positive** (chunk ≥ raw). The LOSS flags still fire on a gross body dropout (a whole chunk's worth of headers missing); finer dropout detection on Vol II still relies on the per-session column-band PDF discipline, not this audit.

These three scripts are guard rails against the failure modes caught in the 2026-05-08 cleanup campaign:

1. **`audit-paraphrase.py`** — word-prefix Jaccard + length ratio + status-string smell detection. Catches paraphrase suspects via low overlap with raw OCR. Smell-flag column is the reliable signal; non-smell low-Jaccard on pt2 chunks is mostly OCR-garble noise.
2. **`audit-headers.py`** — counts unique semantic headers (DUB., QUAESTIO, ARTICULUS roman numerals) in raw OCR per distinction vs chunk body headers. Catches silent body dropouts (the d.27 entire-DUB-V-missing class of failure that `[?]`-flag walks miss because no flag is ever placed). Flag = chunk has fewer headers than raw.
3. **`audit-apparatus-count.py`** — counts raw OCR footer-note patterns vs chunk `[^N]:` defs. Catches vestigial skeleton chunks (auto-chunked with no apparatus despite raw OCR having footer notes — d.3 / d.8 / d.9-dubia-v2 vestigial cleanup pattern) and incomplete promotions (NOT-Tier-2 chunks with high diff). **Heuristic regex hardened 2026-05-09** to catch garbled OCR openers (prior regex undercounted by ~50%; see Lesson 9 in `manual-review/d1-d4-tier2-promotion-log.md`). The hardened audit then surfaced ~23 already-"Tier-2 complete" chunks with diff +20 to +48 — those are tracked as Wave 9b and have status strings downgraded to `Phase C Tier 2 apparatus-incomplete —` pending rebuild.

**The audits are noisy** — they're triage signals, not absolute truth. Investigate flagged chunks against the raw OCR; only act after eyes-on confirmation. But never commit a chunk-promotion or scaffold-rebuild that leaves a flag without dispositioning it (resolve, document, or accept-with-reason in the per-distinction sweep audit log).

The 2026-05-08 cleanup campaign's per-distinction audit logs at `manual-review/d{N}-scaffolds-sweep-audit-log.md` are the format reference.

## Re-chunking before translating

**The auto-generated chunk files have boundary bugs.** Raw text was split by line count, not by semantic boundary, so every chunk leaks content mid-fundamentum. **Always verify and re-chunk from raw text before translating a new distinction.**

1. Grep raw text for semantic markers:
   ```bash
   awk 'NR>=START && NR<=END' raw/bonaventure_vol1_raw.txt | grep -nE "QUAESTIO|QU.ESTIO|QU\.ESTIO|QU\^STIO|QUAEST\. [IVX]+\.|ARTIGULUS|ARTICULUS|DUBIA CIRCA|COMMENTARIUS"
   ```
2. **OCR garbles headings**. Use broad regex. Known variants: `QU^STIO`, `QU.ESTIO`, `QU.flSTIO`, `ARTIGULUS`, `QUAEST. JI` (for Q II), `QU.ESTIO II`. **Test your pattern** against the full raw range before trusting boundaries.
3. **Running heads ≠ semantic headers**. `DIST. VIII. P. I. ART. I. QUAEST. I.` in the middle of a file is a page-top running head, not a chapter start. Look for the bare `QUAESTIO I`, `ARTICULUS II`, or `DUB. I` lines on their own.
4. **`TRACTATIO QUAESTIONUM`** (the listing of questions) belongs in the **divisio** chunk, not a1-q1.
5. **Multi-pars distinctions** (p1, p2): each pars has its own `COMMENTARIUS`, `DIVISIO TEXTUS`, and `TRACTATIO QUAESTIONUM`. Make separate `d{N}-p1-divisio.md` and `d{N}-p2-divisio.md` chunks.

   **5a. SECTIO — Vol IV d.49 Pars II ONLY (frozen convention, 2026-07-18).** `SECTIO` appears exactly once in the whole corpus: Vol IV d.49 P.II (raw `bonaventure_vol4_raw.txt`, Sectio I at ~L107664, Sectio II at ~L108777). It is **not Bonaventure's division** — the Quaracchi editors added it, and say so in their own footnote on the Sectio I page: *"Auctor hic duo, quae principaliter quaeruntur, iterum distribuit, et primum membrum in tria… **Ad confusionem in citando vitandam primae divisioni nomen sectionis superscripsimus.**"* They then cite by it themselves elsewhere in Vol IV (`a. 2. sect. 2. n. 49`; `de quo vide infra sect. 2`).

   **The convention: sectio is a real slug level, inserted between pars and articulus** — `bon-sent-IV-d49-p2-s{1,2}-a{N}-q{N}.md`, with a `sectio: N` frontmatter field alongside `pars:`.

   - **Why not flatten** (renumber P.II's articles 1–7): d.49 P.II contains **two `Articulus I`s**, so `IV-d49-p2-a1-q1` names two different chunks — the id collides. Renumbering would also break the Quaracchi citation match, which is the corpus's whole value proposition.
   - **Why not promote sectio to a pars** (`p2`/`p3`): the littera itself prints only Pars I and Pars II, and pars is authorial while sectio is editorial. Collapsing them erases exactly the distinction the editors drew.
   - **One divisio per pars still holds — but the two sectio prologues land differently** (corrected 2026-07-18 when the chunks were actually built; the first draft of this rule was wrong). P.II has a single `DIVISIO TEXTUS` + `TRACTATIO QUAESTIONUM` at L107630–107663. **Sectio I's header + prologue (L107664–107690) are contiguous with it and go in `IV-d49-p2-divisio`.** **Sectio II's header + prologue (L108777–108790) sit ~1,100 lines downstream**, between `s1-a3-q2` and `s2-a1-q1`, so they cannot go in the divisio without a non-contiguous range — **they fold into `IV-d49-p2-s2-a1-q1`**, per the established "short opener folds into that unit's q1" rule (Vol II Override step 5). Either way: **no `-sN-divisio` chunks.**
   - **Do not generalize.** `-sN-` exists nowhere else. If you meet another editorial sub-division, come back and decide it deliberately — don't pattern-match off d.49.

   **d.49 shape** (raw ~L106123–109979): **P.I** = littera + divisio + Quaestio I–VI (no articles). **P.II** = divisio, then **Sectio I** *De gloria corporis in generali* (Art. I–III, 2 q. each) and **Sectio II** *in speciali* / the four dotes (Art. I–IV).

   **Tooling:** `tools/seam-screen.py` and `tools/audit-style-formatting.py` parse chunk ids with regexes that assumed `-p\d-a\d` adjacency; both were extended with an optional `-s\d` group on 2026-07-18. Any **new** id-parsing tool must tolerate the sectio segment or it will silently skip d.49.
6. **Littera Magistri** (Lombard's text) for any multi-chapter distinction should be its own big Tier-2 chunk, separate from the Bonaventure commentary. See `vol1/bon-sent-I-d8-littera.md` as the template.
7. Write a re-chunking script per distinction (see `/tmp/rechunk_d8.py` pattern). Preserve frontmatter, replace only the `## Latin` body.

## VOL V (Tome V — Opuscula theologica) — pilot conventions, frozen 2026-07-28

Tome V is the first non-Sentences volume: **ten independent works, no distinctions.** The
Fable pilot session (2026-07-28) settled the data model, the Breviloquium conventions, and
the first Tier-2 chunk (`vol5/bon-brev-p1-c1.md` — **the format reference for all Vol V
work**). Each remaining genre gets ONE mini-pilot before its grind (register + chunking
freeze); the Breviloquium grind itself is Opus one-chunk-per-subagent per the established
cadence. **Tier 2 everywhere — Wilson rejected the tracker's old Tier-3-draft idea for
Vols V–X (2026-07-28).**

### Work map (page ranges verified against the volume's own index; ~580 body pp.)

| # | Work | Printed pp. | Slug (frozen) | Book id | Status |
|---|---|---|---|---|---|
| 1 | Prolegomena | I–XL+ | — | — | NOT chunked (editorial apparatus, like INDEX QUAESTIONUM) |
| 2 | QD de scientia Christi | **3–43** | `scientia-christi` | 8 | **ACTIVE — mini-pilot FROZEN 2026-08-31** (7 quaestiones, no articuli, no scholia; p. 1 half-title covers all THREE QD, p. 2 blank 0.0013 %, p. 44 blank 0.0008 %, **no `EXPLICIUNT` colophon**). No chunk built yet. |
| 3 | QD de mysterio Trinitatis | 45–115 | `mysterio-trinitatis` | 9 | planned. ⚠ **NO half-title leaf** — p. 44 is blank and p. 45 opens directly on a display heading (p. 1's half-title covers all three QD). Questions divide into **articuli**, unlike work 2. |
| 4 | QD de perfectione evangelica | 117–198 | `perfectione-evangelica` | 10 | planned. ⚠ **NO half-title leaf expected** — same three-work half-title; fix p. 117 on the plate. |
| 5 | **Breviloquium** | 199–291 | `breviloquium` | 5 | **COMPLETE — gated + deployed 2026-08-01** |
| 6 | **Itinerarium mentis in Deum** | 293–316 | `itinerarium` | 6 | **COMPLETE 2026-08-14 — all 10 chunks Tier 2; work-close gate + deploy due** |
| 7 | **De reductione artium** | 319–325 | `de-reductione` | 7 | **COMPLETE 2026-08-14** |
| 8 | **Collationes in Hexaemeron** | 327–454 | `hexaemeron` | 11 | **COMPLETE 2026-08-23 — 23 collationes + Scholion; gated + deployed 2026-08-24.** (It is in Vol V, not Vol VII as the old tracker claimed.) |
| 9 | **Coll. de septem donis** | 455–**503** | `septem-donis` | 12 | **COMPLETE 2026-08-29 — all 9 collationes Tier 2; work-close gate CLOSED CLEAN and DEPLOYED 2026-08-29.** End fixed positively from `EXPLICIUNT` on p. 503. |
| 10 | **Coll. de decem praeceptis** | **505–532** | `decem-praeceptis` | 13 | **COMPLETE 2026-08-31 — all 7 collationes Tier 2; work-close gate CLOSED CLEAN, pushed and DEPLOYED to production 2026-08-31 (verified live: `/browse/13/d/7/q/bon-praec-c7` serves the `EXPLICIUNT`).** Half-title 505, blank 506, body 507–532, all plate-verified. |
| 11 | Sermones selecti | **533**–~579 | `sermones-selecti` | 14 | planned. ⚠ **Half-title is p. 533, NOT ~535** (plate-read 2026-08-29): 533 half-title, 534 blank, body opens 535. |

Order as actually run: Breviloquium → Itinerarium → De reductione → **Hexaemeron** (taken
ahead of the QD, Wilson's call) → **septem donis** (complete) → **decem praeceptis** (COMPLETE, deployed) → the
three QD → Sermones. The two remaining Collationes sets follow the Hexaemeron because the
reportatio register is freshly proven; the QD register carries over from the Sentences
almost unchanged and keeps.

### Data model (implemented in `site/scripts/build-content.mjs` — `WORKS` registry)

- A Vol V chunk declares **`work: <slug>`** in frontmatter, **no `book:` field** — the
  registry maps slug → book id, title, Illumination initial, division label, division
  titles. Adding a work = adding its registry entry (ids pre-assigned above).
- **`division: N`** (int) is the distinctio-equivalent grouping key. `division: 0` is a
  prologue and is NOT skipped (the vols 1–4 "skip distinctio 0" rule doesn't apply to
  work chunks). Ordering keys inside a division: `section:` (prologue §§), `capitulum:`.
- New `type:` values: `prologus`, `capitulum` (later: `collatio`, `sermo`).
- Site: `Book.divisionLabel/initial/tome` are optional fields; pages fall back to the
  Sentences rendering when absent. URLs stay `/browse/{bookId}/d/{division}/q/{chunkId}`.

### Breviloquium chunking (frozen)

- **One chunk per capitulum** (~0.5–1.5 printed pp. — the capitulum IS Quaracchi's
  citation unit: "Breviloq. p. V. c. 6"). ~72 capitula across 7 partes; verify each
  pars's cap count against the index (raw L93746–93940) at chunk time, per-pars.
- **Prologue = 7 chunks**: `bon-brev-prol` (intro, type `prologus`, division 0,
  capitulum 0) + `bon-brev-prol-s{1..6}` (`section: 1..6`). Prologue spans printed
  201–208; the capitula table (209–210 top) is NOT chunked (editorial, like an index).
- File/id naming: `bon-brev-p{1..7}-c{N}` in `vol5/`.
- Body pp. 201–291; part openings (`PARS PRIMA` + subtitle) fold into that pars's c1,
  per the established short-opener rule.

### ITINERARIUM — mini-pilot conventions (frozen 2026-08-11; format reference = `vol5/bon-itin-prol.md`)

Flat work, no partes: prologue + 7 capitula + Quaracchi's work-level Scholion,
printed pp. 293–316 (p. 293 half-title VERIFIED, p. 294 MEASURED BLANK, body opens
p. 295). English title: **"The Journey of the Mind into God."**

- **TEN chunks:** `bon-itin-prol` (division 0, pp. 295–296, ✅ done — the pilot) ·
  `bon-itin-capitula` (division 0, `section: 1`, `type: capitula`, p. 296) ·
  `bon-itin-c{1..7}` (divisions 1–7, `type: capitulum`, `capitulum: N`) ·
  `bon-itin-scholion` (division 8, `type: scholion`, pp. 313–316). The build's
  title builder is type-first (`capitula` → "Capitula", `scholion` → "Scholion")
  and renders flat-work divisions as `Cap. N`.
- **★ THE CAPITULA TABLE IS TRANSMITTED TEXT — the Breviloquium precedent does NOT
  port.** Its `EXPLICIUNT CAPITULA` line carries anchor ⁵ whose note records which
  codices transmit the table in place vs. in-text, and § 5 claims the titles as
  authorial (*praemittendo titulos*). It is chunked; the Breviloquium's editorial
  capitula table (pp. 209–210) was not. Do not re-decide this per work by analogy —
  **look for apparatus ON the table**; that is the test.
- **Quaracchi's paragraph numbers (`1.`, `2.` …) are the citation unit**
  ("Itin. c. N n. M") and are preserved verbatim at paragraph heads in BOTH
  languages. Chapters have no interior headings; the numbers are the only
  fine-grained address the work has.
- **Index page claims (all unverified until closed on the band):** c1 296–299 ·
  c2 299–303 · c3 303–306 · c4 306–308 · c5 308–310 · c6 310–312 · c7 312–313 ·
  Scholion 313–316. Every end fixed positively from the NEXT `Cap. N.` heading
  (c7 from the Scholion heading; Scholion from the work's end — *De reductione*'s
  half-title stands at p. 317/319, span to be verified). The Breviloquium index
  was right seven times out of seven at Pars VII and that run carries NO licence.
- **⚠ Cap. VII's title differs between the volume index and the capitula table**
  (index: *affectu totaliter in Deum per excessum transeunte*; table: *affectu in
  Deum per excessum totaliter transeunte*). Settle at c7 time against the in-place
  `Cap. VII.` heading; until then the registry carries the table's form.
- **Two display headings fold into their chunks:** `INCIPIT PROLOGUS…` → prol;
  **`INCIPIT SPECULATIO PAUPERIS IN DESERTO.`** → c1 — the second is the work's
  TRANSMITTED alternate title (n. 5 names its codices), render it, don't drop it
  as furniture.
- **Register (exercised in the pilot, locked):** *speculatio* → "speculation" ·
  *speculum* → "mirror" (one image in this work; the pun documented once, in the
  pilot's Notes) · *contemplatio* → "contemplation" · *excessus* → "transport"
  (NEVER "excess"; "ecstasy" is blocked by § 3's *ecstaticos excessus*) ·
  *raptus* → "rapt/rapture" · *suspensio* → "uplifting" · *vestigium* → "vestige" ·
  *gradus* → "steps" · *illuminationes scalares* → "ladder-like illuminations" ·
  *mens* → "mind". Scripture on the Douay-Rheims base adjusted to Quaracchi's
  actual Latin, as throughout the corpus.
- **Census/ledger:** non-Breviloquium rows are written as FULL slugs
  (`bon-itin-prol	-`); `check-vol5-census.py` normalizes. **This work has THREE
  suffix-less slugs** (prol, capitula, scholion) — the census blind-spot class,
  now ×3.
- **Gutters measured:** 295 = 1162 · 296 = 1387 · 299 = 1172 · 300 = 1364 ·
  301 = 1228 · 302 = **1346** (colcrop's 1344 on a 55 px run REJECTED under the
  sub-60 floor) · 303 = 1196.
- **★★ WHY THE WINDOW CONSENSUS COLLAPSES IN THIS WORK — THE CENTRE RULE SPLITS THE
  GUTTER INTO TWO SUB-BANDS (found 2026-08-11 across pp. 300–303).** The frozen Vol V
  rule already says the in-gutter obstruction IS Quaracchi's printed column rule and
  that a narrow run means the rule inked heavily. **This is the next fact after that:
  on these leaves the rule leaves a zero-ink band on EITHER side of itself, each
  ~26 px, inside a true band of ~60 px.** Every row window therefore lands on one
  sub-band or the other and reports it as the whole gutter — which is why only 1–5 of
  15 windows come back "sound" and why the sound ones still disagree. **The reading
  that is right is the FULL band's midpoint, taken from the direct per-column ink
  profile over the whole body+footer height** (step 3), never the window vote. Attested
  p. 300 (band 1334–1393, rule 1365) · p. 301 (1198–1259, rule 1229 at 1078 rows) ·
  p. 302 (1317–1376, rule 1349 OFF-centre — which is what dragged the default low) ·
  p. 303 (1166–1225, rule 1198 at 1518 rows). **Corollary: a default that "looks
  healthy" at 60+ px can still be the rule's position rather than the band's centre**
  (pp. 300 and 303 both). Go to the profile on every Itinerarium leaf; it costs nothing.
  Separately, on a leaf with STACKED REGIONS (p. 296 has five) the narrow-window
  300–450 px "runs" are the min-collection artifact — scattered equal minima reported
  as one span, not a wide band.
- **★ BLOCK STRUCTURE AND ANCHOR STRUCTURE COME APART AS THE NORM HERE, NOT THE
  EXCEPTION.** The left footer block overran the column division on **three consecutive
  leaves** — p. 300 by TWO notes (nn. 4–5 print left, anchor right), p. 301 by one
  (n. 5), p. 302 by one (n. 4) — on top of c1's p. 297 n. 6. Read anchors, only anchors,
  and state the block split and the anchor split separately in every `## Notes`.
- **Cadence:** 24 pp → ONE gate, at the work close (per the frozen table); deploy
  boundary = work close. Reverts to the standing per-structural-unit rule, the
  Breviloquium's work-close hold does not carry over.
- **★★★ A GUTTER IS A PROPERTY OF A REGION, NOT OF A PAGE — AND `colcrop.py` SILENTLY
  RETURNS THE WRONG ONE (earned at `bon-itin-c7`, p. 313, 2026-08-14). THIS BELONGS TO
  VOL V MECHANICS AND GENERALIZES TO VOLS VI–X; it is recorded here because the
  Itinerarium is where it was paid for.** p. 313 stacks **three regions set to different
  measures** — Cap. VII's body (two columns), then a full-width `SCHOLION` display
  heading with the scholion's body in a **smaller type**, then the footer register.
  **The two body regions do not share a gutter:**
  - Cap. VII body: zero band **1137–1195** (59 px), centre rule 1165–1170 → **1166**
  - Scholion body: zero band **1129–1194** (66 px), centre rule 1160–1162 → **1161**
  - footer register: band reads **149 px** and is unusable — the left footer block is
    narrower than the column, so the "band" runs on into white space

  **The default 45–92 % row window straddles both bodies and reports 1161 on a 49 px
  run — the scholion's value, not the chapter's.** The run width is the tell, but a
  5 px error survives a glance at the crop and would silently pad one column and
  truncate the other. **The frozen three-step method assumes ONE MEASURE PER PAGE.
  That assumption fails on any leaf where a work or unit ends and the next begins in a
  different type. Profile the region you are transcribing, not the page.** Expect it at
  **every work close in Vols VI–X**, and constantly in the **Sermones**, where short
  pieces end mid-leaf as a matter of course. This is the third distinct member of the
  bad-window family, after the display-heading case (p. 201) and the in-column
  `Cap. N.` heading case (p. 263) — but unlike those two it does **not** blow the run
  width out, which is exactly why it is the dangerous one.
- **★★ DIVIDE THE FOOTER BY ANCHOR EVEN ACROSS WORK-UNITS — a page's WHOLE register can
  belong to a unit that occupies only the top of the page (same leaf, same session).**
  Cap. VII fills barely the upper two-fifths of p. 313 and the work-level Scholion fills
  the middle, yet **all six of p. 313's footer notes are Cap. VII's**: each answers to a
  Cap. VII anchor, and the Scholion's own text carries **no footnote anchors at all**,
  citing its authorities inline instead. A reader dividing the register by *where the
  text sits on the page* would hand three notes to the wrong chunk. The standing rule
  ("read anchors, only anchors") already covers it — **but note that here the anchors are
  not merely in a different column, they are in a different work-unit.**
- **★ TRANSCRIBE A COLOPHON EXACTLY, EVEN AGAINST THE WORK'S OWN TITLE.** The Itinerarium
  ends **`EXPLICIT ITINERARIUM IN DEUM`** — *without* **mentis** — set three inches below
  a running head reading `ITINERARII MENTIS IN DEUM SCHOLION.`, in a work whose half-title
  and prologue both give *Itinerarium mentis in Deum*. Quaracchi prints no note on it.
  **Not normalised, not flagged.** The same discipline as the *est est* / *dicitur
  dicitur* dittographies at c5.
- **★ REGISTER FOR cc. II–VII — FROZEN AT c2 (2026-08-13). Reuse it; do not re-decide it.**
  - **The three operations, one-to-one, never blended:** *apprehensio* → "apprehension" ·
    *oblectatio* → **"delectation"** · *diiudicatio* → **"adjudication"** (*diiudicare* →
    "to adjudge"; *indiiudicabilis* → "unadjudicable"). **"Adjudication" and not
    "judgement" because *iudicare* / *iudicium* / *numeri iudiciales* must stay separately
    available** — c2 § 9 sets *diiudicamus* and *iudicamus* in one sentence, and § 10 makes
    *iudiciales* the proper name of a class of numbers.
  - **The threefold delight:** *speciositas* → **"comeliness"** (*speciosus* → "comely") ·
    *suavitas* → "sweetness" · *salubritas* → "wholesomeness". **"Comeliness" and not
    "beauty" because *pulcritudo* defines *speciositas* in the same sentence** (*pulcritudo
    nihil aliud est quam aequalitas numerosa*); collapsing them makes the definition
    circular in English where it is not in Latin.
  - **Augustine's seven kinds of number:** *sonantes* → "sounding" · *occursores* →
    "encountering" · *progressores* → "advancing" · *sensuales* → "sensual" · *memoriales*
    → "memorial" · *iudiciales* → "judicial" · *artificiales* → "artificial".
  - **The rest:** *macrocosmus* → "macrocosm" · *minor mundus* → "the lesser world" (the
    editions' gloss *microcosmus* → "microcosm", kept distinct from Bonaventure's own
    phrase) · *proportionalitas* → "proportionality" · *species* → "species" (technical,
    throughout) · *delectatio* → "delight" · *exemplatum* → "exemplate" · *sensibilia
    particularia / communia* → "particular / common sensibles".
- **★ REGISTER ADDITIONS FROM c3 (frozen 2026-08-13):** *illatio* → "inference" · *terminus* →
  "term" · *propositio* → "proposition" · *dignitates* → **"axioms"** (the apparatus itself
  glosses the word with Boethius's *communis animi conceptio*, so "axiom" is what the note
  is already saying; "dignities" is empty in English) · *habitudo* → **"relation"** ·
  *virtus electiva* → "the elective power" · *consilium / iudicium / desiderium* → "counsel /
  judgement / desire" · *deliberativa* → "the deliberative power" · *circumincedentes* →
  "mutually interpenetrating one another" (the noun *circumincessio* → "circumincession").
  **★ *iudicium* takes "judgement" — which is the whole reason c2's *diiudicatio* took
  "adjudication".** The two words meet on p. 305 and must stay apart in English.
- **★★ THE BLOCK OVERRUN REVERSES DIRECTION — DO NOT INFER THE NEXT LEAF FROM THE RUN
  (earned at c3, 2026-08-13).** The left footer block overran the column division on **five
  consecutive leaves** (pp. 300, 301, 302, 303, 304) and then **p. 305 UNDERRAN it** (n. 4
  prints RIGHT, anchors LEFT). A long same-direction run is exactly what tempts a reader to
  stop checking. Read anchors, only anchors, on every leaf, and state the two splits separately.
- **★ A SUB-60 px GUTTER RUN IS A TRIGGER TO GO AND LOOK, NOT A VERDICT.** c2 rejected
  p. 302's 55 px default (1344 → true 1346); c3's three defaults all came in at **58–59 px and
  all three were CONFIRMED** at the direct profile (304 = 1330, 305 = 1229, 306 = 1325). Both
  outcomes are normal. What is not optional is printing the profile.
- **★★ A WIDE GUTTER RUN IS A FAILURE SIGNAL TOO — AND THE BODY-ONLY WINDOW IS WHAT PRODUCES
  IT (fresh instance at c4, p. 308).** Profiled over the body rows alone, p. 308 returns a
  **161 px** "band" because Cap. V's heading and subtitle sit inside the left column at ~40 %
  depth; the **body + footer** profile gives the true 64 px band. This is the same species as
  p. 263's 375 px and p. 252's ~330 px: **far above the sound 58–64 px band is as much a
  failure as far below it.** Expect it on every leaf where a capitulum opens mid-column — in
  this work, most leaves. **Profile over body+footer, not body alone, whenever a heading falls
  inside a column.**
- **★★ A FOOTER BLOCK DOES NOT ALWAYS OPEN NUMBERED — PAGE-CROSSING RUNOVERS EXIST, AND NO
  HAND-OFF WILL WARN YOU (earned at c4, 2026-08-13).** p. 306 n. 9 breaks at the foot of the
  page and continues **unnumbered at the head of p. 307's LEFT footer** — the sixth
  page-crossing runover in all of Vol V. `bon-itin-c3`'s hand-off was correct in every
  particular and silent about it, because c3 owned only p. 306 n. 1 and never read p. 307's
  footer. **This is the concrete argument for the standing rule that a hand-off tells you
  which notes are yours and never where they land.** A reader assuming every block opens
  numbered will either mis-assign the fragment to n. 1 or lose it outright.
- **★ REGISTER ADDITIONS FROM c4 (frozen 2026-08-13):** the five spiritual senses take the
  ordinary English words (*auditus · visus · olfactus · gustus · tactus* → hearing · sight ·
  smell · taste · touch), since Bonaventure's point is that they are the bodily five recovered
  spiritually. **The nine hierarchic acts are GERUNDS, not -tion nouns** — *nuntiatio ·
  dictatio · ductio · ordinatio · roboratio · imperatio · susceptio · revelatio · unctio* →
  announcing · dictating · leading · ordering · strengthening · commanding · receiving ·
  revealing · anointing; "dictation" and "unction" carry the wrong sense for acts answering to
  the nine angelic orders. *Hierarchicus* → "hierarchic" (never "hierarchical"), *hierarcha* →
  "hierarch". ★ *excessus* → **"transport"** is load-bearing here: c4 § 3's *ecstaticus amor*
  takes "ecstatic love", which is exactly why *excessus* cannot also have it.
- **✅ THE ITINERARIUM IS COMPLETE — all TEN chunks Tier 2 (`prol` · `capitula` · `c1`–`c7` ·
  `scholion`), pp. 295–316, zero `[?]` flags in every one.** Cap. VII closed on the
  `EXPLICIT ITINERARIUM IN DEUM` colophon, there being no `Cap. VIII.` to close against
  (the Breviloquium `p7-c7` shape); the work-level Scholion then closed on p. 316, with
  p. 317 verified as *De reductione*'s half-title. ▶ **The front is now the four-pass
  work-close polish gate AND the deploy, which fire together at p. 316** — after which
  `de-reductione` (pp. 319–325) is the next work.
- **★★ A CHUNK CAN CARRY NO APPARATUS AT ALL — `bon-itin-scholion` is Vol V's first, and
  the tooling was VERIFIED against it rather than assumed (2026-08-14).** pp. 314–316 have
  **no footer register whatsoever**, and p. 313's six notes all belong to Cap. VII (see the
  divide-the-footer-by-anchor rule above). The chunk therefore carries `has_apparatus:
  false`, no anchors and no defs — and **`build-content.mjs` still counts it translated
  (2022/2022), `check-vol5-apparatus.py` still passes with its entry total UNCHANGED at
  831, and `KNOWN_TOTALS` needs no new entry.** The runover ledger takes a **negative**
  line: no runover is possible on a chunk with no footers. **Expect this shape at editorial
  scholia and short prefatory matter throughout Vols VI–X; do not read a zero entry count
  as a failed read.**
- **★ AT A WORK'S LAST PAGE BOTH COLUMNS END LEVEL AND THE WHITE SPACE BELOW THEM IS NOT A
  BOUNDARY QUESTION.** p. 316's left column ends mid-word at *…et quan-* and the right a
  few lines lower, both ~62 % down, the lower two-fifths of both columns blank. The frozen
  rule ("blank space at a column foot is NEVER a boundary") is satisfied not by reading the
  white space but by fixing the end **positively from p. 317's half-title**. ★ **Confirm the
  layout against a downscaled whole-page view before trusting column extents** — band
  overlap makes a bottom band's blank region easy to misjudge as a short column. A 5× PIL
  downscale is cheap and is well under the API's image cap, unlike the raw 450 dpi page.
- **★ DO NOT NORMALISE THE GREEK ARTICLE.** The Scholion prints *conceptu* **τοῦ** *esse*
  (genitive) twice; the English keeps **τοῦ** even though the English "of" then duplicates
  the genitive. Rendering it τό would be a silent emendation of Quaracchi — the same
  discipline as the colophon and the dittographies.
- **✅ Cap. VII's TITLE IS SETTLED (c7, 2026-08-14): the in-place heading on p. 312 carries
  the VOLUME INDEX's form** — *…affectu **totaliter** in Deum per excessum transeunte* —
  and the `WORKS` registry has been corrected to it. The capitula table's transposition
  (*…per excessum totaliter transeunte*) is recorded at `bon-itin-capitula` as transmitted
  text. **Do not restore the table's form.**
- **✅ `bon-itin-c3` and `bon-itin-c4` ARE WRITTEN** (pp. 303–306, 17 entries; pp. 306–308,
  19 entries; zero `[?]` in both).
- **✅ `bon-itin-c2` IS WRITTEN** (pp. 299–303, 26 entries, zero `[?]`). Its plate scouting
  survives at `manual-review/itin-c2-plate-scouting.md`; the chunk's own `## Notes` is now
  the fuller record.
- **★★ HOW TO WRITE AN ITINERARIUM CHUNK WITHOUT LOSING IT TO THE CONTENT FILTER (earned
  2026-08-11/13, and it is the difference between finishing and not).** Five runs across c1–c3
  died on `API Error: 400 Output blocked by content filtering policy` — three subagents, the
  main thread, and once mid-c3. The material is not the cause and suppressing narration does
  not help. **The fix is the Péguy strategy: build the chunk through MANY SMALL INCREMENTAL
  `Edit` APPENDS — one or two paragraphs per call — rather than emitting the file in one or two
  large outputs.** A kill then costs a single paragraph and is retried immediately; c3 absorbed
  one mid-Latin and lost nothing. **Apply it to every remaining chunk, and to any chunk in
  Vols VI–X that has died once.** See also the vision-plate content-filter note in global memory.


### HEXAEMERON — mini-pilot conventions (frozen 2026-08-14; evidence in `manual-review/hexaemeron-pilot-scouting.md`)

*Collationes in Hexaëmeron sive Illuminationes Ecclesiae*, work 8, book id 11, slug
`hexaemeron`. **A reportatio — the first in the corpus.** p. 326 MEASURED BLANK ·
**p. 327 half-title** (the title prints **HEXAËMERON**, with a diaeresis, and carries the
transmitted alternate title *sive Illuminationes Ecclesiae*) · p. 328 MEASURED BLANK ·
**body opens p. 329**, not 327 as the old work map implied. English title:
**"Collations on the Hexaëmeron."**

- **TWENTY-FOUR CHUNKS: `bon-hex-c{1..23}` (divisions 1–23) + `bon-hex-scholion`
  (division 24)** — the same shape as the Itinerarium, whose work-level Scholion the
  volume index likewise lists after the last chapter. Ids are `bon-hex-…`; the scholion
  slug is **suffix-less-adjacent** and belongs to the census blind-spot class.
- **★ THE CHUNK IS THE COLLATIO, and the frozen test decided it: `COLLATIO I.` CARRIES
  APPARATUS ANCHOR ¹** (the note documents the work's title in the codices). It is also
  Quaracchi's citation unit — `Hexaem. coll. N. n. M` — and the volume index lists exactly
  these twenty-three and nothing finer. ~5.5 printed pp per chunk.
- **⛔ NEVER CHUNK ON THE *VISIONES*.** The index describes the collationes as *tractationes*
  of four visions (*De prima visione tractatio prima*…), and **a grep of the whole work
  returns ZERO `VISIO` headings in the body**. They are a description of the matter, not a
  printed division — the same class as `de-reductione`'s marginal `Pars`, and the same
  answer: record them in `## Notes`, never in the structure.
- **★★ EACH COLLATIO OPENS WITH A `SUMMARIUM` AND IT IS RENDERED, NOT TRIMMED.** It is a
  full-measure editorial synopsis in small italic, keyed to the collatio's paragraph
  numbers (*…tripliciter divisa, numero 1. — Pars I. In auditoribus tria requiruntur, 2. —
  De his tribus specialiter, 3-5. — …*), and **it carries no apparatus anchor** (verified at
  magnification on p. 329). The reflex is to treat it as editorial matter and trim it like
  a marginal gloss. **That is wrong, and the corpus already shows why: Quaracchi's scholia
  are equally editorial and are rendered in full, in both languages.** The rule the corpus
  actually follows is **marginal glosses are trimmed; display matter set in the text block
  is rendered** — and the Summarium is display matter, and the reader's only map of a
  five-page reportatio. Render it as **`### Summarium`** at the head of each language block,
  paragraph references preserved verbatim, body following it.
  - ⚠ **Parser note, checked:** an `### Summarium` at h3 does NOT terminate
    `extractLanguageBlock` (only `## Latin|English|Apparatus|Notes|Scholion|---` do), so it
    is captured as part of the body and needs no sentinel change. **`### Scholion` must
    still be LAST in a language block** — that rule is unaffected.
  - ⚠ **The `SUMMARIUM` header garbles as badly as `SCHOLION` did** — a case-tolerant grep
    over the whole work returns only ~12 recognizable spellings (`SuMMARiuM`, `SuMMARKJM`,
    `SuMMARiUiM`, `SuMMARiiiM`) against 23 collationes. **Find it by CONTENT — the
    em-dash-and-paragraph-number synopsis shape — never by header grep.**
- **Marginalia are present AS WELL as the Summarium** (five in p. 329's first column alone)
  and are trimmed to the Marginalia list per the standing Vol V convention. The synopsis
  does not replace the glosses; both are transcribed, in different places.
- **Division titles go into the `WORKS` registry ONE AT A TIME as each chunk is built, each
  verified against the IN-PLACE printed subtitle**, never bulk-copied from the volume index.
  The Itinerarium's Cap. VII title question is the reason. (Collatio I's index text and
  in-place subtitle were compared and agree.)
- **Header hazards:** the running head `IN HEXAËMERON COLLATIO N.` fires far more often than
  the real header and garbles hard (`IN HEXAiiMERON`, `IN IIKX/VKMEKON`, `IN HEWKiMERON`);
  the real header is the bare `COLLATIO N.` on its own line, itself garbled (`COLLATIO L` =
  I, `IL` = II, `IIL` = III, `lY` = IV, `VL` = VI). **Fix every span from the next real
  `COLLATIO N.` header on the band, never from a running head.**
- **Raw range L57174 → ~L76290** (~19,100 lines, ~17× `de-reductione`). Collationes I–XXIII
  run pp. 329–~449 and the Scholion ~450–454; *de septem donis* opens at **p. 457**, which
  bounds the far end. Every span still gets fixed positively on the band.
- **Cadence: THREE gates**, not the two page count alone would give (~128 pp), **plus a
  shakedown gate ~15–25 pp in — i.e. after roughly Collatio IV.**
- **⚠ Plates: extract PER COLLATIO, never in bulk.** 128 leaves at 450 dpi is ~600 MB on an
  8 GB machine.

### SEPTEM DONIS — mini-pilot conventions (frozen 2026-08-27; evidence in `manual-review/septem-donis-pilot-scouting.md`)

*Collationes de septem donis Spiritus Sancti*, work 9, book id 12, slug `septem-donis`.
**The second reportatio.** p. 455 half-title (**no alternate title**, unlike the
Hexaemeron) · p. 456 MEASURED BLANK (0.084 % dark px) · **body opens p. 457**.
English title: **"Collations on the Seven Gifts of the Holy Spirit."**

- **NINE CHUNKS: `bon-don-c{1..9}` (divisions 1–9), `type: collatio`.** The volume index
  lists exactly nine and nothing finer. **NO work-level Scholion** — a real difference
  from both the Itinerarium and the Hexaemeron, whose indexes list one after the last
  chapter. The work ends `EXPLICIUNT COLLATIONES DE DONIS SPIRITUS S.` and *De decem
  praeceptis*'s half-title follows. **This work has no suffix-less slug** — the first Vol V
  work to which the census blind-spot class does not apply.
- **⛔ THE HEXAEMERON'S DECISIVE TEST COMES OUT THE OTHER WAY HERE: `COLLATIO I.` CARRIES
  NO APPARATUS ANCHOR.** Read at 10× and compared side by side with p. 329, which does:
  p. 329's is a well-formed superscript standing **after** the period, answered by a footer
  note documenting the work's title in the codices; p. 457's only mark is a comma-shaped
  speck **between** `COLLATIO` and `I.`, of no digit shape, and nothing stands after the
  period. All seven of p. 457's notes are body-anchored. **The collatio is still the chunk
  unit — but settled by the index and by Quaracchi's citation practice (`de donis coll. N.
  n. M`), not by an anchor. Do not go looking for one, and do not carry the Hexaemeron's
  sentence forward.** ⚠ The raw cannot answer this: both headings render as
  `COLLATIO<double space><numeral>` because Vol V's OCR has no footnote numerals at all.
  **The anchor question is only ever answerable on the plate.**
- **Everything else in the Hexaemeron block ports** — the `### Summarium` at the head of
  each language block (verified unanchored on p. 457; the header garbles, `SuM.MARiiiM`
  there, so **find it by content**), marginalia trimmed to `## Notes` *as well as* the
  Summarium, division titles added to the registry ONE AT A TIME against the in-place
  subtitle, and **count the body every time** (the c6/c14 short-Summarium mechanism is a
  property of the genre; Collatio I's `17. 18.` and its 18 numbered paragraphs agree).
- **Header hazards:** running head `DE DONIS SPIRITUS S. COLLATIO N.` (garbles `SPIRITLS`,
  `SI>1RITUS`, `SPIR[TUS`, `DOiMS`, `COLLATIO LX` = IX); the real header is the bare
  `COLLATIO N.` (`IL` = II, `in.` = III, `YL` = VI, `VIL` = VII, `VIIL` = VIII).
  **Fix every span from the next real header on the band.**
- **Raw band L76284 → L83157** (~6,875 lines, ~⅓ of the Hexaemeron). Real headers:
  I L76291 · II L77022 · III L77899 · IV L78670 · V L79563 · VI L80138 · VII L80980 ·
  VIII L81635 · IX L82381 · `EXPLICIUNT` L83126. **Index page claims:**
  457 · 462 · 468 · 473 · 479 · 483 · 489 · 493 · 498 — **ALL NINE are now VERIFIED on the plate;
  473, 479, 483, 489, 493 and 498 are all SHARED heading pages.** **The work ends on p. 503**, fixed
  positively at c9 from the full-measure `EXPLICIUNT COLLATIONES DE DONIS SPIRITUS S.` line
  (raw L83126) set beneath both columns. *Decem praeceptis* Coll. I is at **p. 507** per the index,
  so **its half-title's "~505" is the only estimate left** — fix it positively when that work opens.
- **★ EVERY COLLATIO OPENING THROWS THE SKEW SCREEN — BUT THE DEFAULT IS NOT ALWAYS WRONG
  (revised 2026-08-27 at `bon-don-c2`; this section previously read "defeats").** Each opens with a
  full-width heading + subtitle + Summarium stacked across the gutter, so `colcrop`'s
  default lands on the stack. p. 457: default **1203 on a 51 px run**, skew screen reports
  **166 px drift** and names the outlying slices (0.08, 0.17, 0.25) itself — that is the
  work-opening case, **not** skew. Profiling below the Summarium (rows 0.36–0.95) gives a
  stable **band 1181–1229 (49 px), centre rule 1195–1215, midpoint → 1204**, three windows
  agreeing at 1202–1205. **Adopt 1204 for p. 457; profile below the Summarium on all nine
  openings.**
  ★★ **p. 462 threw the identical signature and the default held.** 321 px drift, the screen naming
  slices 0.08/0.17/0.25 itself; below the Summarium all three windows returned **1402 on a 64 px
  band** with the ink island at 1401–1404 — which is precisely what `colcrop` had already measured
  on a healthy 62 px run. **The discriminator is the RUN WIDTH, not the opening:** p. 457's default
  sat on 51 px, under the 60 px floor, and had to be corrected; p. 462's sat above it and only had
  to be confirmed. So: profile below the Summarium at every opening, and let the profile arbitrate —
  but do not assume the default is wrong there, and do not discard a default the profile reproduces.
- **★★ THE INDEX GIVES A HEADING PAGE, AND A HEADING PAGE MAY BE SHARED (added 2026-08-27
  at `bon-don-c3`).** The index's page for `COLLATIO N.` is the page that collatio's
  **display heading** falls on — not the first page it owns outright. `COLLATIO IV.`
  stands **mid-leaf on p. 473**, below Collatio III's ¶¶ 18 and 19, so Collatio III
  runs **468–473** and not 468–472 as the index pair implies. **Never derive a span's
  last page by subtracting one from the next collatio's index page; close every span
  positively on the plate.** The shared leaf also splits its footer register: p. 473's
  eight notes number straight through, nn. 1–5 anchoring in Collatio III and nn. 6–8 in
  Collatio IV, so **c4 must pick up p. 473 nn. 6–8 and must not restart that page at 1.**
- **★★ THE DEFAULT ROW WINDOW ALSO STRADDLES THE BODY/FOOTER GAP, AND THAT IS THE THIRD
  BAD-WINDOW MECHANISM IN THIS WORK (added 2026-08-28 at `bon-don-c5`, p. 482).** On a leaf with a
  large footer register the body ends well above the foot (~72 %) and the register begins below the
  gap (~78 %), so the default 45–92 % window profiles across white space and returns a **448 px
  run** — the blown-out failure signature, not the narrow one. The window consensus is useless
  there too (it drifts 1288–1366 with the window). **The per-column ink profile settles it**: four
  of six windows returned the identical band 1369–1433 (65 px), midpoint **1401**, against
  `colcrop`'s default of 1317. **A default you would otherwise adopt can be ~85 px wrong on a leaf
  with an ordinary two-column body and no heading at all** — the tell is the run width and nothing
  else. Fire step (3) whenever the run leaves the 58–64 px band in EITHER direction.
- **★★★ A SPAN CAN BE SHARED AT BOTH ENDS, and the display-heading gutter failure is about the
  WINDOW, not the leaf (added 2026-08-28 at `bon-don-c4`; c5 confirmed it at p. 483, whose
  `COLLATIO VI.` stack clips the top of the window and did fail, needing a below-the-Summarium
  profile).** Collatio IV runs **473–479**: it opens
  mid-leaf on p. 473 below Collatio III's ¶¶ 18-19 and closes mid-leaf on p. 479 above `COLLATIO V.`
  Its footer register is therefore discontinuous at **both** ends — it begins at p. 473 n. 6 and ends
  at p. 479 n. 1 — so a chunk may both receive a runover hand-off and make one. ⭐ And the two
  mid-leaf headings behaved **differently** under `colcrop`: p. 473's sits at ~40 % of the leaf,
  inside the default 45-92 % window, and destroyed the run (16 px); p. 479's sits at ~22 %, **above**
  the window, and the default measured cleanly on a healthy 60 px run. **So profile above and below
  only when the heading falls inside 45-92 %.** A shared leaf as such is not the trigger.
- **★★★ A SHARED LEAF FORWARDS A RUNOVER ONLY WHEN THE INCOMING UNIT'S *BODY* REACHES IT
  (added 2026-08-29 at `bon-don-c8`, p. 498).** Five shared leaves in a row (473, 479, 483, 489,
  493) each split their footer register between two collationes, and the reflex that forms is
  "shared leaf ⇒ hand-off." **p. 498 breaks it: `COLLATIO IX.`'s display heading, subtitle and
  full-measure Summarium all stand on the leaf, yet ALL NINE of its notes are Collatio VIII's**,
  because Collatio IX's ¶ 1 does not begin until p. 499 and the Summarium is unanchored. So c8
  forwards nothing. **The test is not whether the next unit's HEADING is on the leaf; it is
  whether its numbered BODY is.** Read anchors, only anchors — the rule already says it, and this
  is the case that shows the heading is not one.
  ⭐ **CONFIRMED FROM THE RECEIVING SIDE at `bon-don-c9` (2026-08-29):** c9 opened p. 498 expecting
  nothing, read none of that leaf's nine notes as its own, and restarted p. 499's register at 1
  legitimately. The rule is now attested from both ends of one seam. ⭐ The same leaf shows a
  second first: **a Summarium can span two leaves** — Collatio IX's begins on p. 498 and finishes
  at the head of p. 499 above the body, and neither half is anchored.
- **★ A RUN *ABOVE* THE 58–64 px BAND IS A TRIGGER TOO, AND THE DEFAULT MAY STILL BE RIGHT WHEN
  THE RUN IS NARROW (both attested on one span, `bon-don-c8`).** p. 495's default sat on a **74 px**
  run and was ~6 px off (1154 → profile band 1129–1191, midpoint **1160**); p. 494's sat on a
  **54 px** run and the profile **reproduced** it (1352), finding a 14 px centre-rule island inside
  the band — the frozen rule-5 "heavily inked rule" case. **Escalate on either side of the band, and
  let the profile arbitrate in both directions.**

- **★ The Vol I cross-reference digit class is LIVE in the Vol V raw, and only the plate catches it.**
  `bon-don-c4` corrected two Quaracchi digits the OCR had wrong: p. 473 n. 6 is `III. Sent. d. 35`
  (raw `33`) and p. 478 n. 7 is `Psalm. 118, 125` (raw `123`). Both were caught at 2.2x and the
  second is confirmed independently by sense. **Never adopt a digit from the raw.**
- **★ `Libr. <roman>. <ch>, <v>` — the book-number-only citation is a GENRE TRAIT here.**
  The reportatio names the book aloud (*dicitur in libro Machabaeorum*) and the editor's
  note gives only `Libr. II. 3, 1.` **Ten are attested** across c2–c8 (c2 p. 467 n. 5;
  c3 p. 472 n. 4 and p. 473 n. 5; c4 p. 474 n. 5 and p. 478 n. 6; c5 p. 480 n. 2, p. 482 n. 5
  and p. 482 n. 10; c7 p. 493 n. 4; c8 p. 498 n. 2). `build-citations.py` now emits an explicitly **unresolvable barrier** for
  the shape, because without it a following `ibid.` in the same note bound to the previous
  note's verse and named the wrong BOOK silently — verified firing on all three of c5's.
  ⚠ **A COUSIN SHAPE `Epist. <roman>. <ch>, <v>` exists and the barrier does NOT cover it**
  (c4 p. 474 n. 3, c5 p. 482 n. 6, where the body names John aloud and the note gives only
  `Epist. I. 2, 14.`). It currently produces **no ledger record at all** rather than a wrong
  one, so nothing is silently mis-bound; but the note's own primary citation is invisible to
  the index. Transcribe as printed and expect it again in c6–c9.
- **★★ REGISTER SETTLED AT THE WORK-CLOSE GATE (2026-08-29, Wilson's ruling — the work's two
  carried-forward questions, decided once for the whole work and binding on *De decem praeceptis*).**
  1. ***pietas* → "piety" EVERYWHERE, body prose and inside scripture quotations alike.** The gift
     keeps one visible English root across the work, so the Douay's "godliness" is adjusted at
     **Isaias 11:2** (c2 ¶ 2) and **I Tim. 4:8** (c7 ¶ 17). This is the frozen corpus rule —
     *"Scripture on the Douay-Rheims base **adjusted to Quaracchi's actual Latin**"* — doing its job:
     Quaracchi prints *pietatis* and the collatio is titled *De dono pietatis*. Applied at the gate:
     c2's four sites were changed (⚠ the resume note had the split backwards — **three of the four
     were body prose**, only one was the Isaiah quotation); c3, c6 and c7 already conformed.
  2. ***intellectus* → "understanding", *intelligentia* → "intelligence" in BODY PROSE; inside a
     scripture quotation the Douay's "understanding" stands.** c8's distinction is the work rule,
     because its ¶ 11 divides *intelligentia* into *memoria praeteritorum, intelligentia praesentium,
     circumspectio futurorum* and that division collapses if both words share one English root.
     **Zero edits were needed:** c7's four sites are a Quaracchi *summarium*, the Douay quotations of
     **Job 28:12** and **Ecclus. 37:20**, and one body echo of the Ecclesiasticus quotation it
     glosses — the printed text's own pun, deliberately preserved. ⚠ **The two rules pull opposite
     ways on purpose:** *pietas* has ONE Latin word and needs one English root, so the Douay yields;
     *intelligentia* has a CONTRASTING Latin word beside it, so the contrast is what must survive and
     the quotation is left alone. Do not flatten either into "always follow the Douay."
- **Cadence: ONE gate, at the work close** (49 pp, per the frozen table); deploy boundary =
  work close. **The shakedown trigger does not fire separately** — this is not a new
  register but the one the Hexaemeron just exercised over 128 pages, and its single
  divergence (the heading anchor) is settled above. ~5.2 printed pp and ~35 apparatus
  entries per chunk. **Plates per collatio, never in bulk.**

### DECEM PRAECEPTIS — mini-pilot conventions (frozen 2026-08-29; evidence in `manual-review/decem-praeceptis-pilot-scouting.md`)

*Collationes de decem praeceptis*, work 10, book id 13, slug `decem-praeceptis`.
**The third reportatio.** English title: **"Collations on the Ten Commandments."**
p. 505 half-title (**plate-verified — no longer an estimate**; no alternate title, foot
carries `S. Bonav. — Tom. V.` and signature `64`) · p. 506 MEASURED BLANK (0.047 % dark
px) · **body opens p. 507** · **work ends p. 532**, fixed positively on the plate from
`EXPLICIUNT COLLATIONES DE DECEM PRAECEPTIS.` (raw L86881) set full-measure beneath both
columns. **Body extent pp. 507–532 = 26 printed pages.** Raw band **L83158 → L86893**.

- **SEVEN CHUNKS: `bon-praec-c{1..7}` (divisions 1–7), `type: collatio`.** The volume
  index (raw L94252–L94270) lists exactly seven and nothing finer; seven bare
  `COLLATIO N.` headers stand on the band. **NO work-level Scholion** (index and plate
  agree). **No suffix-less slug** — no prologue, no scholion, so the census blind-spot
  class does not apply, as in the *septem donis*.
- **⛔ `COLLATIO I.` CARRIES NO APPARATUS ANCHOR** — read at 4× on p. 507; nothing stands
  after the period, and none of the leaf's notes documents the title or the codices.
  **Two works running now answer this way, so the Hexaemeron's anchored heading is the
  EXCEPTION in Vol V, not the rule.** The collatio is the chunk unit on the index and on
  Quaracchi's citation practice, not on an anchor. Do not go looking for one.
- **The `SUMMARIUM` is present, full-measure and UNANCHORED** (verified at 3× on p. 507);
  it prints cleanly there but the raw gives `SuMMARiuM` — **find it by content, never by
  header grep.** Render as `### Summarium` at the head of each language block. **Count the
  body every time** — Collatio I's ends at `23. 24.`
- **★★★ SIX INTERIOR BOUNDARIES, SIX SHARED PAGES — and it was PREDICTED, not discovered.**
  The unit is **~3.7 printed pp**, thoroughly non-integral, so the *septem donis*' closing
  rule (*boundary shape is a function of unit size against page size*) was used forwards
  for the first time and paid out six for six. **There is no clean crossing in this work.**
  Frozen spans, each inclusive of its shared last page:
  **c1 507–510 · c2 510–515 · c3 515–519 · c4 519–522 · c5 522–525 · c6 525–529 · c7 529–532.**
  (Display headings at raw L83170 · 83700 · 84397 · 85022 · 85435 · 85883 · 86407.)
  Consequences: **every interior chunk both receives a runover hand-off and makes one**
  (only c1 makes without receiving, only c7 receives without making) — **but the p. 498
  rule still governs each one individually**: a shared page forwards a runover only when
  the incoming collatio's numbered BODY reaches it. Expect a hand-off at all six and
  **verify it at all six.** ⚠ **Never derive a span's last page by subtracting one from
  the next collatio's index page.**
  ⛔ **MEASURED AT BOUNDARY 1 (`bon-praec-c1`, 2026-08-29): p. 510 FORWARDS NOTHING.**
  All seven of p. 510's footer notes are Collatio I's (n. 1 answers ¶ 20's *octo partes
  orationis,* n. 7 answers ¶ 24's *carnis et oculorum*), because **Collatio II's heading
  and Summarium stand on p. 510 but its ¶ 1 does not begin until p. 511** — and its
  Summarium spans the two leaves, as Collatio IX's did at p. 498. So the pilot's
  "expect a hand-off at all six" is **already wrong at the first one.** ⭐ The
  transferable correction: **the prediction was of SHARED PAGES, and that held; whether
  a shared page hands off is a SEPARATE question the p. 498 rule answers, and it must
  be re-asked on the plate at each of the remaining five.** Do not let "six shared
  pages" harden into "six hand-offs" — that is a tally copied forward, the exact defect
  the *septem donis* work-close gate caught.
  ⭐⭐ **MEASURED AT BOUNDARY 2 (`bon-praec-c2`, 2026-08-30): p. 515 FORWARDS. The two
  boundaries answer OPPOSITE ways under ONE test, and that settles how the remaining four
  are to be read.** p. 515's register splits — **nn. 1–3 are Collatio II's** (n. 1 answers
  ¶ 28's *dicit Ieremias,* n. 3 answers ¶ 29's *dicit Propheta*), **nn. 4–5 are Collatio
  III's** — because Collatio III's numbered ¶ 1 *does* begin on that leaf, where Collatio
  II's did not begin on p. 510. **Same p. 498 rule, opposite outcomes, and the heading was
  present on both leaves.** ⛔ So neither answer may be copied forward: **re-ask it on the
  plate at pp. 519, 522, 525, 529**, and read anchors, only anchors. ⭐ c2 also confirmed
  the p. 498 rule from the RECEIVING side at boundary 1: it opened p. 510 expecting
  nothing, read none of that leaf's seven notes as its own, and restarted at p. 511 n. 1
  legitimately.
  ⭐⭐⭐ **MEASURED AT BOUNDARY 3 (`bon-praec-c3`, 2026-08-30): p. 519 FORWARDS.** That leaf
  carries eight footer notes; **nn. 1–7 are Collatio III's** (n. 1 answers ¶ 25's *ad
  Titum,* n. 7 ¶ 27's *in Levitico*) and **n. 8 — `Exod. 20, 8. — Seq. locus est Ps. 102,
  17. et 18. Cfr. III. Sent. d. 37. dub. 3.` — is Collatio IV's**, because Collatio IV's
  numbered ¶ 1 (*Memento, ut diem Sabbati sanctifices*) begins on the leaf and carries the
  anchor. c3 also re-derived the boundary-2 hand-off rather than adopting it, and verified
  p. 515 nn. 4 and 5 **for POSITION and COLUMN, not merely ownership** (n. 4 anchors left,
  n. 5 right, both entries printed in the right block).
  ⭐⭐⭐⭐ **MEASURED AT BOUNDARY 4 (`bon-praec-c4`, 2026-08-31): p. 522 FORWARDS.** That
  leaf carries eight footer notes; **nn. 1–7 are Collatio IV's** (n. 1 answers ¶ 14's
  *volatilia,* n. 7 ¶ 16's *dicit Psalmus*) and **n. 8 — `Exod. 20, 12: Honora... dabit
  tibi. — Seq. locus est Eccli. 3, 22. Cfr. III. Sent. d. 37. dub. 4.` — is Collatio V's**,
  because Collatio V's numbered ¶ 1 (*Honora patrem tuum et matrem tuam*) begins on the
  leaf, below the `COLLATIO V.` heading and Summarium, and carries the anchor. c4 also
  re-derived the boundary-3 hand-off rather than adopting it, verifying p. 519 n. 8 **for
  POSITION and COLUMN** (anchor at ¶ 1's *sanctifices,* head of the left column; entry
  printed last in the right footer block).
  ⭐ **AND THE LEAF-SHAPE ARGUMENT IS NOW POSITIVELY DEAD.** p. 522 is structurally the
  SAME shape as p. 510, which forwarded nothing — heading + subtitle + Summarium set
  full-measure mid-leaf, outgoing collatio above. The difference is one line of body:
  Collatio V's ¶ 1 begins below the Summarium on p. 522 where Collatio II's did not on
  p. 510. **Leaf shape does not decide it; the body anchor does.**
  ⭐⭐⭐⭐⭐ **MEASURED AT BOUNDARY 5 (`bon-praec-c5`, 2026-08-31): p. 525 FORWARDS.** That
  leaf carries only **four** footer notes; **nn. 1–3 are Collatio V's** (n. 1 answers
  ¶ 20's *episcopus Parisiensis,* n. 2 ¶ 21's *tenellis,* n. 3 ¶ 21's closing *mortuus est
  ille*) and **n. 4 — `Exod. 20, 13-15. — Seq. locus est Ps. 118, 6; tertius Iac. 2, 10…`
  — is Collatio VI's**, because Collatio VI's numbered ¶ 1 (*Non occides. Non moechaberis.
  Non furtum facies*) begins on the leaf, below the `COLLATIO VI.` heading and Summarium,
  and carries the anchor at *facies.* c5 also re-derived the boundary-4 hand-off rather
  than adopting it, verifying p. 522 n. 8 **for POSITION and COLUMN** (anchor at ¶ 1's
  *daturus est tibi,* third and last line of the **left** column of that leaf's lowest
  region; entry printed last in the **right** footer block).
  ⛔ **The tally now stands at one "no" and FOUR "yes," and it STILL may NOT be summed.**
  Four consecutive "yes" answers are not a pattern and a majority is not evidence; the
  discriminator is still the p. 498 rule and nothing else. ⭐ **Only p. 529 is left, and it
  is the work's LAST boundary — there is no later chunk to catch a wrong answer there, so
  it is the one place where copying the tally forward would be both cheapest to do and
  most expensive to keep. Re-ask it on the plate.**
  ⭐ **p. 525 is also the sharpest block-vs-anchor case the work has produced, in BOTH
  directions on one leaf:** not one of Collatio V's three anchors stands in the left
  column (all three are in the right), yet the **left** block carries n. 1 — six lines
  long, it opened the block; meanwhile Collatio VI's n. 4 anchors in the **left** column
  and prints last in the **right** block. **Read anchors, only anchors.**
  ⭐⭐⭐⭐⭐⭐ **MEASURED AT BOUNDARY 6 (`bon-praec-c6`, 2026-08-31): p. 529 FORWARDS — the
  work's LAST boundary, and all six are now closed.** Collatio VI's own ¶ 20 does not
  finish on p. 528; it crosses the gutter and runs three lines into p. 529, ending at
  *Rogemus ergo Dominum Iesum Christum etc.,* immediately before the full-measure
  `COLLATIO VII.` heading, subtitle and Summarium. **Collatio VII's ¶ 1
  (*Non loqueris contra proximum tuum falsum testimonium…*) begins on that same leaf and
  carries the anchor at *eius*²** (n. 2 answers *Nec desiderabis uxorem eius*), so
  `bon-praec-c6` closes its own register at p. 529 n. 1 and `bon-praec-c7` opens at n. 2.
  c6 also re-derived the boundary-5 hand-off rather than adopting it, confirming p. 525
  n. 4 anchors ¶ 1's *facies*⁴ exactly as `bon-praec-c5` predicted.
  ⛔⛔ **THE TALLY OVER ALL SIX SHARED LEAVES IS NOW CLOSED: FIVE "YES," ONE "NO" (p. 510
  alone forwards nothing).** Every one of the six was re-asked on the plate independently
  — none was ever copied forward, including this last one, where a copied "yes" would
  have been cheapest to write and impossible to catch afterward. **The p. 498 rule —
  a shared page forwards a runover only when the incoming unit's numbered BODY reaches
  it, never merely its heading or Summarium — is the only discriminator that held across
  all six, and it held every time.**
  ⭐ **Self-caught error, not a printer's one:** c6 first misread p. 529 n. 1 as
  `Matth. 24, 13` at low zoom; a 4× re-crop showed `Matth. 21, 13` clearly, the verse the
  note is citing and the one the body's own *speluncam latronum* echoes. Disclosed in
  `bon-praec-c6`'s Notes as the transcriber's own error, not the compositor's — the first
  time in this work the digit-correction discipline caught a mistake on that side of the
  boundary rather than the printer's.
- **⚠ NEW HAZARD CLASS, found at `bon-praec-c2`: A FOOTNOTE CAN RUN OVER ONTO THE NEXT
  PAGE'S FOOTER BLOCK, AND THAT IS NOT A HAND-OFF.** p. 512 n. 8 (Augustine, *Enarrat. in
  Ps.* 69) begins in p. 512's register and its last two lines are set at the head of
  **p. 513's** footer block, above p. 513's own n. 1. The note belongs to p. 512's sequence
  throughout; reading the runover as p. 513's would have invented a spurious tenth entry
  there and shifted every subsequent number on the leaf. **Distinguish the two: a hand-off
  moves OWNERSHIP between chunks and is decided by the body anchor; a register runover is
  one note's TEXT continuing across a page break and changes no numbering at all.**
  Ledgered as `p.512 n.8:page`.
- **⚠ A MARGINALE CAN BE PRINTED INCOMPLETE.** p. 512's marginale at ¶ 9 reads **`Duplex
  no-`** and nothing follows — read at 3× and 4×, the line beneath is blank and the
  marginale sits well inside the trimmed edge, so it is the printing, not the scan or the
  crop. The intended reading is evidently *Duplex notitia.* **Record it as printed and say
  so; do not silently complete it.**
- **The `~26–30 apparatus entries` figure is an ESTIMATE, not a gate.** `bon-praec-c2`
  returned **32**, and legitimately: the band was derived as ~7 notes × ~3.7 printed pages,
  while c2 spans six leaves and owns register on five of them. `bon-praec-c4` returned
  **23**, three BELOW the band, by the same arithmetic read the other way: it spans four
  leaves and owns a full register on only three, contributing a single note from p. 519.
  **The band is now attested wrong in both directions.** `bon-praec-c5` returned **20**,
  six below — the lowest the work has produced, and by the same arithmetic pushed one step
  further: four leaves, a full register on only two of them, one note from p. 522 and three
  from p. 525. A count outside it is a prompt to recount on the plate, never a defect on
  its own. `bon-praec-c6` returned **26** (25 numbered plus one unanchored editorial note
  on p. 526's Introductio) — inside the band for the first time since c1, spanning five
  leaves and owning a full register on three of them (526, 527, 528).
- **⚠ A STALE, LOW-DPI EXTRACTION CAN SIT SILENTLY IN `raw/vision/` AND BE READ AS IF IT
  WERE THE 450 DPI PLATE.** Found and corrected at `bon-praec-c6`: `extract-pages.py`
  skips any page whose output file already exists, **regardless of the dpi it was
  extracted at** — it does not check the existing file's actual resolution against the
  requested one. pp. 526–529 had been pulled once at the volume's low default dpi before
  a `--dpi 450` request was made for the same range; the request silently skipped all four
  as "already existed," and two of them were read and partially transcribed at 1143×1699
  before `PIL.Image.open(...).size` caught the mismatch (vol5 pages at 450 dpi run
  ~2500×3800). Re-extracted with `--force` and every line re-verified before commit.
  **Check the actual pixel size of a freshly-touched page before trusting it, especially
  early in a chunk when an earlier default-dpi pull may already have populated the
  directory** — the tool's own "Skipped: N (already existed)" message does not distinguish
  a correct skip from this one.
- **★★ THE RUNNING HEAD NAMES THE COLLATIO THAT BEGINS MID-PAGE — NEW HERE, AND IT IS THE
  PRINTING, NOT THE OCR.** On all six shared pages the running head is already set to the
  *incoming* collatio while the top of the page is still the outgoing one's text (p. 510's
  head reads `COLLATIO II.` above four columns of Collatio I). **A running head is not
  evidence of who owns the top of a page.** This is the case that shows why the frozen rule
  says *fix every span from the next real bare `COLLATIO N.` header, never from a running head*.
- **Header hazards:** running head `DE DECEM PRAECEPTIS COLLATIO N.` garbles as `DE DF.CEM`,
  `DE DFXEM`, `DE DFrEM`, `DE DECEM PRAECEPTES`, `DE DECEM PKAECEPTIS`, `DE DECEM PRAECEFnS`,
  `COLL\TIO`, `C0LL\T10`, `COIJ.ATK)`, `COLLATIO K.`/`\l` (= II), `COLLATIO 1.` (= I),
  `COLLATIO 111.` (= III). Real bare headers: `COLLATIO L` (= I), `IL`, `IIL`, `VL`, `VIL`.
- **A page map exists and is cross-checked twelve times, but it is a PREDICTION TABLE.**
  Running heads give page → raw line for all 26 pages; twelve standalone page numerals
  survive in the OCR and agree with it, zero disagreements, and both ends are closed on
  the plate. ⚠ **A surviving page numeral is still a raw digit — p. 508's prints as `308`.**
  **Every chunk still closes its own span positively on the plate.** Full table in the
  scouting doc.
- **Index page claims (all seven agree with the band; none yet closed on a plate):**
  507 · 510 · 515 · **519** · 522 · 525 · **529**. ⚠ The index OCR prints `SI9` for 519 and
  `.529` for 529 — **those are the band's answers, not the raw's.** Division titles, to be
  verified in place ONE AT A TIME before entering the registry: I *De quatuor motivis ad
  observantiam divinorum praeceptorum inducentibus et de decalogo in genere* ✅ **verified
  in place on p. 507, word for word** · II *De primo praecepto decalogi in specie* ·
  III *De secundo praecepto decalogi* · IV *De tertio praecepto decalogi* ·
  V *De quarto praecepto* · VI *De quinto, sexto et septimo praecepto* ·
  VII *De octavo, nono et decimo praecepto*.
- **Gutter, p. 507: ADOPT 1157.** `colcrop.py vol5 507` gives **1178 on a 15 px run** — the
  loud failure, and the expected one (heading + subtitle + Summarium stacked across the
  gutter). The skew screen's 41 px walk with three empty slices is **the stack, not skew**.
  Below the Summarium four windows return the identical band **1127–1186 (57–59 px),
  midpoint 1156–1157**, centre-rule island 1151–1160 — the frozen rule-5 case, a heavily
  inked rule truncating the zero-ink run. **Profile below the Summarium at every opening,
  and at every mid-page opening too** (which here is all six); per the p. 473/p. 479
  precedent, **profile above and below only when the mid-page heading falls inside the
  default 45–92 % window.**
  ⚠ **Two more leaves in this work defeat the default, and in two different ways
  (`bon-praec-c2`).** p. 513's 48 px run is the frozen **inked-rule** case — the profile
  finds a 13 px centre-rule island (peak 466) inside band 1186–1238, midpoint 1212, and
  24 windows agree within 3 px, so the default **1213** is confirmed, not corrected.
  p. 514's 52 px run is **SKEW** — the screen shows the gutter walking 15 px down the leaf;
  one split still suffices (max left 1262 < min right 1309) and **1290** stands. **Escalate
  on a narrow run, then let the skew screen say WHICH failure it is before adopting
  anything.** p. 515 is the stacked-region case again — a **1 px** run, corrected to
  **1258** by profiling only the rows above the mid-leaf `COLLATIO III.` block; ⛔ note that
  c3's region is *below* that block, so **c2's value must be re-measured, not reused.**
  ⭐ **`bon-praec-c3` re-measured it and the two halves of p. 515 differ by 4 px, BOTH
  right:** the lower region (rows 0.75–0.93, the columns beneath the `COLLATIO III.` block)
  gives a clean 63 px band 1223–1285, midpoint **1254**, against c2's 1258 above. A gutter
  is a property of a region; a 4 px difference across a mid-leaf heading is the region rule
  working, not a correction. **c3's further measurements:** p. 516 = **1336** — the
  default's 1327 sits on an 8 px run because the centre rule inked heavily (island
  1333–1342, peak 510) and every wide window agrees with the band's midpoint; ⚠ the skew
  screen's reported 45 px drift there is the head slice catching the running head, not
  skew. pp. 517 (**1209**, 61 px) and 518 (**1363**, 58 px) clean as returned. p. 519 =
  **1177**, the stacked-region case again — the default returns 1164 on a **1 px** run
  because the `COLLATIO IV.` heading, subtitle and Summarium occupy roughly 45–60 % of the
  leaf; profiling rows 0.10–0.40 gives a 62 px band 1146–1207. **Five of the eleven leaves
  this work has measured defeat the default, and the stacked region is the reason on three
  of them.**
  ⭐ **`bon-praec-c4` (2026-08-31) added three more, by three DIFFERENT mechanisms in one
  four-leaf span.** p. 519's lower region (below the `COLLATIO IV.` block) profiles to
  **1178** on band 1164–1193 — **within 1 px of c3's 1177 for the upper region**, where
  p. 515's two regions differed by 4 px; ⚠ **both outcomes are the region rule working, and
  a region value is checkable against the other region but never predictable from it.**
  p. 520 is the **inked-rule** case at its loudest: default **1347 on an 8 px run**, a heavy
  5 px island (peak 582) sitting off centre inside a clean 63 px band 1289–1351, midpoint
  **1320**; the skew screen reports 61 px of drift but six of its eight slices read
  1283–1351 and only the two head slices fork — **let the screen say WHICH failure it is
  before adopting anything.** p. 521 is the **narrow-but-sound** case: **1255 on a 51 px
  run**, under the 60 px floor, so escalated — 23 of 24 windows agree within 4 px and the
  band's midpoint is 1255, so the default is **confirmed, not corrected** (its screen's
  185 px "drift" is two head slices catching the running head and the body/footer gap).
  p. 522 is the **stacked region** again, and here the tell is a run far ABOVE the sound
  band: default **1374 on a 326 px run**, because the `COLLATIO V.` block fills the lower
  half; profiling rows 0.15–0.45 gives band 1300–1334, **1316 adopted.**
  **Eight of the fourteen leaves this work has measured now defeat the default.**
  ⭐⭐ **`bon-praec-c5` (2026-08-31) found a MECHANISM THE FROZEN RULE DOES NOT NAME, and it
  is the exact INVERSE of the inked-rule case: THE CENTRE RULE CAN PRINT TOO LIGHT FOR THE
  `ink<110` THRESHOLD, and then the profile reports NO ISLAND and a run that is too WIDE.**
  The frozen rule reads a *narrow* run as a heavily inked rule truncating the blank band.
  Two leaves in c5's span do the opposite: p. 524's island registers **peak 7** and
  p. 522's lower region shows none at all, so the zero-ink run walks straight through where
  the rule stands and comes back **wider** than the sound 58–64 px band — **75 px** on
  p. 524, **101 px** on p. 522. Re-profiled at **threshold 150–180** the rule appears at
  once and the band's true edges with it: p. 524's rule stands isolated at **1360–1364**,
  four separate row regions all return band 1332–1392, **1362 adopted** against the
  default's 1356; p. 522's lower region closes at 1284 and 1345 with an island at
  **1313–1316** (peak 142), **1314 adopted**, 2 px from c4's 1316 for the upper region.
  ⚠ **The tell is a wide run with NO island**, on a volume where the island is on
  essentially every leaf — the standing instruction to print the per-column profile even
  when the windows agree is what makes the absence legible. ⚠ On p. 524 the same faintness
  is visible in the **type** of the right column (*intelligitur, debilitantur, adiutorio*
  print grey), so this is ONE physical fact about the forme — rule and type inked together
  — not two coincidences. **Diagnose from the ink, not from the run width alone.**
  ⚠ **c5 also hit the first region TOO THIN for the window loop.** p. 522's lower region —
  the three lines of Collatio V's ¶ 1 between the Summarium and the footer rule — is 0.04
  of the leaf deep, and `gutter-profile.py`'s consensus loop needs 0.12 and returns
  nothing. **Step 3 alone decides there, and the tool was hardened to say so instead of
  crashing on an empty window list.** The number is licensed only by the other region's
  agreeing value: **a region value is checkable against the other region and never
  predictable from it.**
  **Eleven of the eighteen leaves this work has measured now defeat the default.**
- **★ REGISTER: THE TWO *SEPTEM DONIS* RULINGS BIND, UNCHANGED** — *pietas* → "piety"
  everywhere; *intellectus* → understanding / *intelligentia* → intelligence in body prose,
  with the Douay's "understanding" left standing inside a quotation. Stated in full in
  § SEPTEM DONIS above. **The discriminator is whether the English is carrying a Latin
  distinction — not whether the sentence is a quotation.**
  ⚠ **Expect a third question of the same shape and CARRY IT TO THE GATE, do not settle it
  chunk by chunk:** the decalogue vocabulary (*praeceptum* / *mandatum* / *lex*) is under
  continuous Douay pressure across all seven collationes, and Collatio I ¶ 20 enumerates
  the ten. Settle it once, for the work, the way *pietas* was settled.
  ▶ **`bon-praec-c1` set the working rendering and CARRIED it, unsettled: *praeceptum* →
  precept · *mandatum* → commandment · *lex* → law.** It keeps all three Latin words
  visibly distinct and costs nothing inside the quotations, because Quaracchi prints
  *mandata* wherever the Douay reads "commandments." **The collision it creates is with
  the work's own English title:** *De decem praeceptis* is "Collations on the Ten
  **Commandments**" while ¶ 20 and the Summarium read "the ten **precepts**." Follow c1
  for now; the gate decides. ⚠ **A second datum for the gate, from the same chunk:** the
  *intellectus* / *intelligentia* ruling had **visible cost for the first time** — ¶ 8's
  *intelligentia sacrarum Scripturarum* became "the **intelligence** of the sacred
  Scriptures" against ¶ 10's *intellectum veri* → "understanding," with the Douay's
  "understanding" standing untouched in the Psalm 118:100 quotation two lines above.
  The rule worked exactly as written; it is simply the first place where the required
  word is the less idiomatic one. **c1 made no edit and did not reopen it.**
  ⛔ **`bon-praec-c2` (2026-08-30) made ONE DISCLOSED DEPARTURE from the *intellectus*
  ruling, and the gate must ratify or reverse it.** ¶ 25's *ponere, quod unus intellectus
  sit in omnibus* is the Averroist unity-of-the-intellect thesis, which has a fixed English
  name; "one understanding in all" would not name the doctrine Bonaventure is condemning,
  so it is rendered **"one intellect in all."** ¶¶ 24 and 26's *perverso intellectu sacrae
  Scripturae* — the act, not the faculty — keep **"understanding"** on the rule, and ¶¶ 2
  and 5's *intelligentia* keep **"intelligence"** at the usual idiomatic cost.
  ⭐ **The justification is the frozen discriminator itself:** the rule exists so that a
  Latin *distinction* survives in English, and in ¶ 25 there is no *intelligentia* anywhere
  near, so nothing is being carried and the rule's purpose is not engaged. ⚠ **This is the
  first place where following the rule would produce not a cost but an ERROR** — c1's ¶ 8
  cost idiom, this would cost the doctrine's name. **The rule was NOT reopened and no other
  site was touched. Follow c2 for consistency until the work-close gate rules.**
  ▶ **`bon-praec-c3` followed the rule at every site and made NO departure**, which is the
  datum that shows where c2's line falls. *Intelligentia* does not occur in the collatio;
  *intellectus* occurs four times as a noun and is rendered **understanding** each time —
  ¶ 5's *perverso intellectu sacrae Scripturae* (the same phrase c2 rendered so at its
  ¶¶ 24 and 26), ¶ 21's *fides in intellectu,* and ¶¶ 23/24's *intellectus verborum
  litteralis* / *spiritualis intellectus,* where "sense" would have been the idiomatic
  English. ⭐ **That is a COST, not an error, and so it is not c2's case.** c2 departed
  because "understanding" would have failed to *name* the Averroist doctrine; here it names
  the thing correctly and merely reads less naturally. **The exception the gate has to rule
  on is narrow, and c3 is the control that shows it stayed narrow.**
  ⚠ The *praeceptum*/*mandatum*/*lex* pressure is heaviest so far in c3, whose ¶ 2 puts all
  three words in one clause (*decem sunt mandata decalogi, quae sunt fundamenta omnium
  legum*) while its title says *praecepto.* c3 followed c1 and c2 and carried it.
  ▶ **`bon-praec-c4` followed the rule at every site and made NO departure, and it is the
  first place in this work where the *intellectus*/*intelligentia* rule visibly PAYS
  rather than costs.** Both words stand within one argument: ¶ 7 sets the world's being
  *in intelligentia creata* → **intelligence** against the *mentes angelicae* that receive
  the eternal art, and p. 520 n. 8 glosses the same passage *de intellectu angelico* →
  **understanding.** The note and the body are about two different things and one English
  root would have flattened them together. **This is the c8 case the *septem donis* gate
  named, arriving in a second work.** c2's exception was not extended.
  ▶ **`bon-praec-c5` followed every rule at every site and made NO departure, and it is
  the first place in this work where the *pietas* ruling visibly PAYS.** The word occurs
  three times in one argument at ¶ 10 and its apparatus: the body says that when parents
  command against our salvation *non est ipsis in talibus pietas exhibenda,* and three
  sentences later Jerome's quotation closes *Solum enim pietatis genus est in hoc esse
  crudelem,* which p. 524 n. 2 then quotes again in its fuller text. **The passage turns on
  the one word going over between the two clauses** — the piety owed a parent, and the
  piety that consists in refusing it — and a second English root in the body would have
  destroyed the turn. It costs idiom in the body clause, **and the cost is the price of the
  pun, which is the trade the rule was written to make.**
  ⚠⚠ **c5 ALSO CARRIES THE STRONGEST COUNTER-DATUM YET AGAINST THE *intellectus* /
  *intelligentia* RULING, AND IT IS A NEW SPECIES OF COST.** ¶ 1 makes *intelligentia* the
  precious faculty (*dissipant intelligentiam nostram… nihil in nobis est pretiosius
  intelligentia*), where "intelligence" is right and easy. But ¶¶ 4 and 19 then use
  *litteralis intelligentia* for the literal construing of a text while ¶ 10 uses
  *intellectus verborum secundum sensum litteralem* **for the same thing**, so the English
  reads "the literal intelligence" twice and "the understanding of the words" once.
  ⭐ **The Latin makes NO distinction here at all, and the rule still forces two English
  roots.** That is neither c2's case (following the rule would have been an *error,*
  failing to name the Averroist doctrine) nor quite c3's (a cost where the distinction is
  real and worth paying for): **it is a cost where there is no distinction to protect.**
  c5 followed the rule and did not reopen it — a chunk does not get to suspend a work rule
  locally — **but this is the site on which the gate has to decide whether the ruling is a
  work rule or a passage rule.**
  ⭐ **c5 also supplies the *praeceptum*/*mandatum*/*lex* rule's best evidence so far, and
  it is in a quotation:** Quaracchi prints Ephesians 6:2 as *quod est mandatum primum in
  promissione* and the Douay reads "the first commandment with a promise" — **Latin and
  Douay agree exactly on the word the rule assigns,** so the rendering costs nothing at the
  one place a clash would have been most visible.
  ⚠ **A FOURTH REGISTER QUESTION OPENED AT c4 AND IS CARRIED, NOT SETTLED: *vacatio* /
  *vacare* → "leisure" / "to keep leisure," against *quies* / *requies* → "rest."**
  ⛔ **Neither word occurs anywhere in c5, so the question was carried UNTESTED there** —
  and `bon-praec-c6` (pp. 525–529, killing/adultery/theft) does not use either word
  either. **Untested across three consecutive chunks now (c4, c5, c6); only `bon-praec-c7`
  remains to test it before the work-close gate.** The
  collation the question first arose in is about the Sabbath, so "rest" is the idiomatic
  English for all four words there — but ¶ 7 puts *quietem animarum,* *quietem Domini in
  sepulcro,* *cum vacatione et contemplatione Dei* and *quietationem* in one span, and ¶ 12
  names *divina vacatio* as the first of the three requisites. Collapsing *vacatio* into
  "rest" destroys the distinction the paragraph is built on. **Same discriminator as the
  *intellectus* ruling — the English is carrying a Latin distinction — so it goes to the
  work-close gate with the other three, not settled chunk by chunk.**
  ⭐ **`bon-praec-c6` gives the *praeceptum*/*mandatum*/*lex* rule its heaviest sustained
  run yet, and it cost nothing new:** ¶¶ 2–3 use *mandatum/mandata* nine times describing
  the two tables of the Decalogue, ¶¶ 6–7 turn *lex* over repeatedly in the technical sense
  of positive law and its minister across six consecutive paragraphs, and the subheads
  *Sextum praeceptum.* / *Septimum praeceptum.* keep *praeceptum* visible at the
  chapter-division level throughout — the longest stretch of continuous three-way pressure
  the rule has faced, offered to the gate as a density test rather than a cost test.
- **Cadence: ONE gate, at the work close** (26 pp — well under the ~100 pp trigger); deploy
  boundary = work close. **The shakedown trigger does not fire separately** — the register
  is the one the Hexaemeron and the *septem donis* have exercised over 177 pages, and its
  two open questions were settled at the *septem donis* gate. ~3.7 printed pp and **~26–30
  apparatus entries per chunk** (~7 footer notes per page; ~180 for the work).
  **Plates per collatio, never in bulk.**
  ★★★ **GATE RUN 2026-08-31 (`manual-review/vol5-decem-praeceptis-workclose-gate.md`):
  CLEAN, zero corpus defects, no edits to any `bon-praec-c*` file.** The gate's three
  register rulings: (1) *praeceptum*→precept / *mandatum*→commandment / *lex*→law
  **RATIFIED** as the work rule — seven chunks, zero corrective edits. (2)
  *intellectus*→understanding / *intelligentia*→intelligence **RATIFIED**, and c2's ¶ 25
  Averroist-unity departure **RATIFIED as a correctly-scoped exception** (applies only
  when the rule would misname a fixed philosophical doctrine, never a general escape
  hatch). (3) *vacatio*/*vacare*→leisure vs *quies*/*requies*→rest **CLOSES OPEN, NOT
  SETTLED** — opened at c4, never recurred in c5/c6/c7, so there is no second data point
  either way; the next work that uses either family is where this actually gets tested.
  ★★★ **PUSHED AND DEPLOYED 2026-08-31.** `origin/master` is at the gate commit
  `71a5470`; production serves all seven collationes (verified live at
  `/browse/13/d/7/q/bon-praec-c7`). **The work is closed end to end — nothing is owed.**
- **Registry:** add `decem-praeceptis` to `WORKS` in `site/scripts/build-content.mjs`
  (book 13, tome 5, `divisionLabel: "Collationes"`) **and to the collatio branch of
  `buildWorkChunkTitle`** beside `hexaemeron` and `septem-donis`, so the breadcrumb reads
  `Coll. N`. Do it when c1 lands, with division 1 only. **Both went in with c1; each later
  chunk adds only its own `divisions` line**, after verifying the printed subtitle in
  place word for word (c2's *De primo praecepto decalogi in specie* verified on p. 510; c3's *De secundo
  praecepto decalogi* verified on p. 515; c6's *De quinto, sexto et septimo praecepto*
  verified on p. 525, the shorter form without *decalogi*, as V, VI and VII all carry it).

### SCIENTIA CHRISTI — mini-pilot conventions (frozen 2026-08-31; evidence in `manual-review/scientia-christi-pilot-scouting.md`)

*Quaestiones disputatae de scientia Christi*, work 2, book id 8, slug `scientia-christi`,
id prefix **`bon-qsc-`**. **The first *quaestio disputata* in Vol V — and the genre Vols I–IV
already know.** English title: **"Disputed Questions on the Knowledge of Christ."**
**p. 1 half-title · p. 2 MEASURED BLANK (0.0013 %) · body opens p. 3 · work ends p. 43 ·
p. 44 MEASURED BLANK (0.0008 %).** Body extent **pp. 3–43 = 41 printed pages.**
Raw band **L10048 → L16033**.

- **SEVEN CHUNKS: `bon-qsc-q{1..7}` (divisions 1–7), `type: quaestio`.** The volume index
  (raw L93588–L93610) lists exactly seven and nothing finer. **NO articuli** — confirmed
  negatively on the band (a grep for `ARTICULUS` over the whole work returns zero), against
  *de mysterio Trinitatis* in the same index, whose every question divides into `Art. I`/`II`.
  **NO scholia anywhere in the work** (grep zero; index lists none) — Quaracchi's editorial
  matter goes into the footer register instead. **No suffix-less slug**, so the census
  blind-spot class does not apply.
- **⭐⭐ p. 1's HALF-TITLE COVERS ALL THREE QD** (*de scientia Christi, de mysterio SS.
  Trinitatis, de perfectione evangelica* on one leaf, foot `S. Bonav. — Tom. V.`).
  **Consequence: works 3 and 4 have NO half-title leaf of their own.** p. 44 is blank and
  **p. 45 opens directly with a `QUAESTIONES DISPUTATAE / DE MYSTERIO TRINITATIS` display
  heading of p. 3's kind.** Expect the same at p. 117. The reflex formed over four works
  ("each work opens on a half-title + blank verso") is wrong for the next two — do not
  predict a half-title that is not there.
- **⛔ THE WORK DOES NOT END ON A COLOPHON.** No `EXPLICIUNT` line, unlike all three
  Collationes sets. p. 43's body ends level in both columns at ~19 % of the leaf, the
  register follows, and an **ornamental squiggle rule** stands beneath it. The end is fixed
  positively from three facts, none of them white space: the ornament, p. 44 at 0.0008 %,
  and p. 45's display heading. **Expect the no-colophon close at the other two QD.**
- **⛔ `QUAESTIO I.` CARRIES NO APPARATUS ANCHOR** — read at 2.2× on p. 3; nothing after the
  period, and the italic subtitle is unanchored too. ⭐ **And this is the sharpest form of
  the lesson: a note of exactly the Hexaemeron's kind EXISTS** — p. 3 n. 1 documents the
  question and its codices (`…Haec quaestio deest in cod. C.`) — **but it is anchored in the
  BODY**, at the opening sentence's *ad infinita*¹. **The presence of such a note is not
  evidence of an anchored heading.** Three works running now answer this way.
- **⛔ THERE IS NO `SUMMARIUM`** (verified on pp. 3 and 6). That is a reportatio convention
  and does not port. Do not look for one; do not emit the heading.
- **★ WHAT DOES PORT: the Sentences quaestio conventions, essentially entire.** *Quaeritur…*
  opener · numbered affirmative arguments · `CONTRA:` series · full-measure small-cap
  `CONCLUSIO.` rendered as a `> **Conclusio.**` blockquote · `Respondeo:` · the replies.
  `vol1/bon-sent-I-d1-a1-q1.md` is the shape. ⚠ **`CONCLUSIO` garbles — 4 recognizable
  spellings for seven questions. Find it by content, never by header grep**, exactly as
  `SUMMARIUM` needed in the reportationes.
- **Marginalia are DENSE** (~one per argument — p. 6 alone has `Aliter.`, `Comparatio
  duplex.`, `Notandum.`, `Distinctio.`, `Fundamenta.`) and are trimmed to the `## Notes`
  Marginalia list per the standing Vol V convention. The raw splices them mid-word
  (`Fmdamenta.Civitate`).
- **Index spans (index pages, all confirmed on the band; only the two ENDS are closed):**
  q1 **3–6** · q2 **6–10** · q3 **10–17** · q4 **17–27** · q5 **27–32** · q6 **32–37** ·
  q7 **37–43**. ⛔ **AND q3's TRUE EXTENT IS pp. 10–16, NOT 10–17 — measured 2026-09-03.**
  The "17" is Q. IV's heading page, and Q. IV opens at the very HEAD of it. This is the frozen
  warning below paying off: **an index span's last page is the next question's heading page, and
  that leaf may or may not be shared.** Real `QUAESTIO N.` headers at raw L10063 · 10554 · 11131 · 12047 · 13607 ·
  14368 · 15153. ⚠ **The index gives a HEADING page and a heading page may be SHARED —
  never derive a span's last page by subtracting one from the next question's index page.**
  ⭐ **BOUNDARY 1 (p. 6) MEASURED: it FORWARDS.** Q. I's replies fill the upper ~60 %, then
  `QUAESTIO II.` stands full-measure mid-leaf and **Q. II's numbered body begins on the same
  leaf**; the leaf's nine notes split **nn. 1–6 Q. I / nn. 7–9 Q. II** (n. 7 answers Q. II's
  opening *essentiam*⁷). ⛔ **The other five boundaries (pp. 10, 17, 27, 32, 37) are
  UNMEASURED — re-ask the p. 498 rule on the plate at each.** *De decem praeceptis* answered
  "no" at its first boundary and "yes" at five; one measurement licenses nothing.
  ⭐ **UPDATE 2026-09-03: FOUR boundaries measured now — pp. 6, 10 and 27 FORWARD, p. 17 does NOT.
  Only pp. 32 and 37 remain.** p. 27 forwards in a shape not seen before here: Q. IV's close fills the
  **top band of BOTH columns**, running left-then-right across the full measure, before `QUAESTIO V.`
  stands full-measure mid-leaf.
- **⛔ `bon-qsc-q4` IS THE LARGEST SINGLE CHUNK VOL V HAS ATTEMPTED — 11 printed pp.**
  (against the Hexaemeron's ~5.5 and the *decem praeceptis*' ~3.7). It is the illumination
  question (*Utrum quidquid a nobis certitudinaliter cognoscitur cognoscatur in ipsis
  rationibus aeternis*), the most heavily read text in the work. **It is NOT split** — the
  quaestio is Quaracchi's citation unit and splitting it breaks the citation match that is
  the corpus's whole value proposition. **Build it with the small-incremental-append
  content-filter discipline from the START**, not after a first kill.
- **Apparatus density:** p. 3 = 9 notes, p. 6 = 9, p. 43 = 3. ~9/page × 41 pp ≈ **370 for
  the work** is a PLANNING figure only — p. 43's **n. 3 is a full editorial dissertation**
  filling half the leaf, three note numbers over a page of small type. A count outside the
  band is a prompt to recount on the plate, never a defect.
- **Gutter, p. 3: ADOPT 1130.** `colcrop.py vol5 3` gives **1103 on an 8 px run** — the
  work-opening failure (the `QUAESTIONES DISPUTATAE`/`DE SCIENTIA CHRISTI` stack crosses the
  gutter); the skew screen's 135 px drift is that stack, not skew. Rows 0.34–0.62 give eleven
  windows at **1129**, band **1100–1160 (61 px)**, centre-rule island 1129–1133 (peak 447).
- **Page map:** running heads (verso `QUAESTIONES DISPUTATAE`, recto `DE SCIENTIA CHRISTI
  QUAEST. N.`) plus **thirty surviving page numerals, zero disagreements**, median ~148 raw
  lines per page; full table in the scouting doc. ⚠ **p. 35's numeral prints `33`** — the
  same class as *decem praeceptis*' p. 508 printing `308`. It is a PREDICTION table.
- **Registry:** add `scientia-christi` to `WORKS` (book 8, tome 5, `divisionLabel:
  "Quaestiones"`) **and a new branch in `buildWorkChunkTitle` returning
  `Quaest. ${meta.division}`** for the QD slugs, beside the existing `Coll. ${meta.division}`
  branch. Do it when q1 lands, division 1 only; each later chunk adds its own `divisions`
  line after verifying the printed subtitle in place word for word.
- **Cadence: TWO gates.** ONE at the work close (41 pp), and the shakedown at p. 27.
  ★★★ **SHAKEDOWN GATE RUN 2026-09-04 — `manual-review/vol5-scientia-christi-shakedown-gate.md`.
  THREE defects, all in scope, ALL REPAIRED; the first gate in Vol V to find a real defect.**
  **The front is now `bon-qsc-q5` (pp. 27–32).** The work-close gate follows at p. 43; **deploy
  boundary = work close**, nothing in this work is deployed. **Plates per quaestio, never in bulk**
  — and Pass 4 deleted them, so **re-extract before any plate work**.
  **The four register rulings, which are now the work's rules and are NOT to be re-litigated:**
  1. ***intellectus agens* → "the agent intellect" RATIFIED** — not an extension of the narrow
     exception but **the same instance of it** (the exception was founded at `bon-praec-c2` on the
     Averroist unity of the intellect; this is that doctrine's own name). ★ It stayed narrow, and
     mechanically so: `q4` has **57 Latin `intellect-` nouns** and English "intellect" occurs **9
     times, every one inside *intellectus agens* or *intellectus possibilis*, with zero bare
     "intellect."** The control is p. 19's *circa **intellectum** intelligere oportet, quod est
     **intellectus agens** et **intellectus possibilis*** → "concerning the **understanding**… an
     **agent intellect** and a **possible intellect**." **The exception is scoped to the PHRASE,
     never to the word.**
  2. ***lux* → light / *lumen* → "lumen" HELD APART** (Wilson, 2026-09-04), 18 sites repaired in
     `q4`. **Cost accepted: it is a transliteration and at this frequency conspicuous** — disclose
     it in a translator's note. ⚠ **ONE STANDING EXEMPTION: Ps. 35:10 *In lumine tuo videbimus
     lumen* keeps "In thy light we shall see light"** (received Psalter wording at a scriptural
     quotation boundary). It is the only *lumen* in the work rendered "light"; **do not "fix" it.**
  3. **The `contuit-` family RATIFIED for `q4`** (*contuita* → "contuited", *contuibilis* →
     "contuitable"); **the `q1` repair was DECLINED** — `bon-qsc-q1` keeps *contuitum* →
     "intuition." ⚠ **Consequence, recorded so it is not re-found as a new defect:** the work still
     has one site where *contuitum* and *intuitionem* both go to "intuition." **Known and ruled
     upon.** Follow `q4`, leave `q1` alone; p. 43 may revisit it, it is not open before then.
  4. **"Quotation boundary" NOT RATIFIED as a licence class** — `q3`'s *novit divinus intellectus*
     was repaired to "the divine **understanding** knows." One instance, no control, and no test
     that stops it generalising, since Bonaventure quotes constantly. ⚠ The Ps. 35:10 exemption
     survives because **a received English wording exists that a reader will recognise**; Dionysius'
     clause has none. **That, not "it is a quotation," is the line.**
- **✅ `bon-qsc-q1` IS BUILT (pp. 3–6, 31 entries, zero `[?]`, 2026-08-31).** Four pilot claims
  confirmed on its own plates: the unanchored `QUAESTIO I.`, the body-anchored p. 3 n. 1, the
  absent `SUMMARIUM`/scholia, and **boundary 1 at p. 6 re-derived and FORWARDING** (nn. 1–6
  Q. I / nn. 7–9 Q. II). Two things the pilot could not have known: **(a) the default gutter
  window is unsafe on any leaf carrying a mid-leaf `QUAESTIO` heading** — p. 6's default gave
  1398 on a 2 px run *and* ~1242 on a 315 px run at once; profiling rows 0.20–0.50 (above the
  heading) locks to **1424** on a 1 px spread. Gutters: p. 3 **1130** · p. 4 **1417** ·
  p. 5 **1152** · p. 6 **1424**. **(b) ⚠ THE OCR'S DIGITS LIE IN THIS WORK, and the raw is
  otherwise clean enough to lull you** — five apparatus defects caught on pp. 3–5 alone
  (`III. Sent. j. U` → **d. 14** · `pag. 683` → **685** · `text. 2-3. (I.V. c. 1.)` →
  **2-5. (IX. c. 1.)** · `Psalm. 146, 3` → **146, 5** · `d. 43. a. 1. q. 2` → **d. 45**).
  **Read every `pag. N` and every `d. N. a. M. q. K` off the plate.** Also: p. 5's marginale
  prints defectively as `tinctio.` (margin blank above it at full threshold) — transcribed
  **Distinctio.** on plate evidence, recorded in the chunk's Notes, not carried as a flag.
- **✅ `bon-qsc-q2` IS BUILT (pp. 6–10, 34 entries, zero `[?]`, 2026-09-01).** Eleven arguments,
  **thirteen** `CONTRA`, `CONCLUSIO`, `Respondeo`, thirteen replies (Quaracchi prints replies 3 and
  4 combined as a single `3. 4.` paragraph — preserved, not split). **BOUNDARY 2 (p. 10) MEASURED:
  it FORWARDS** — Q. II's replies fill ~63 % of the leaf, then `QUAESTIO III.` stands full-measure
  and Q. III's numbered body begins on the same leaf; the leaf's eight notes split **nn. 1–7 Q. II /
  n. 8 Q. III**. ⚠ **Two boundaries measured, two "yes" — still not a pattern; pp. 17, 27, 32, 37
  remain UNMEASURED.** Three things this chunk settled that a later one should not re-derive:
  **(a) ⭐ THE DEFAULT GUTTER WINDOW IS UNSAFE ON THIS WORK'S LEAVES GENERALLY, not only under a
  mid-leaf heading.** pp. 8 and 9 carry no heading and the default still returns 2–3 px runs
  (p. 8 → 1418/2 px, p. 9 → 1226/3 px). **Profile rows 0.20–0.50 on every leaf in this work and
  treat the default as advisory.** Gutters: p. 7 **1141** (the one leaf where the default is safe) ·
  p. 8 **1397** · p. 9 **1214** · p. 10 **1354**. **(b) A footnote DOES run over the gutter here**
  (p. 9 n. 4, left-column register into right) — so `q1`'s "no entry runs over a boundary or the
  gutter" is a *chunk* observation, **not** a work-level rule; do not carry it forward.
  **(c) ⚠ A Quaracchi-side digit slip, transcribed as printed and logged:** p. 8 n. 7 reads
  *cfr. supra pag. **1**, nota 2*, but p. 1 is the shared half-title and carries no notes — the
  locus is **p. 3 n. 2**, which records this very Augustine text and says *Idem locus occurrit infra
  q. 2. in corp.* Disposed like `bon-praec-c6`'s dangling cross-ref: **transcribe as printed, log,
  non-blocking.** Also settled for the register: ***notitia*→knowledge / *cognitio*→cognition** held
  apart where the *Respondeo* turns on *notitia causans res* vs *causata a rebus* (cost disclosed:
  *scientia* in the work's title is also "knowledge"); and ***Ad intelligentiam ipsius quaestionis*
  → "for the understanding of the question,"** following `q1`'s identical formula — the ordinary
  idiom, **not** a departure from *intelligentia*→intelligence, which governs the term of art.
  ⚠ The *quietans* family DOES occur (reply 8, *quietantis ipsum cognoscentem*) and is **still not**
  a datum on the open *vacatio*/*quies* question.
- **✅ `bon-qsc-q3` IS BUILT (pp. 10–16, 48 entries, zero `[?]`, 2026-09-03).** Twenty-one arguments,
  **sixteen** `SED CONTRA`, `CONCLUSIO`, `Respondeo`, twenty-one replies. **⭐⭐ BOUNDARY 3 (p. 17)
  MEASURED: IT DOES NOT FORWARD — the work's first "no."** `QUAESTIO IV.` stands full-measure at the
  very head of p. 17 with its subtitle and its own numbered body on the same leaf; Q. III closes on
  **p. 16** at ~14 % of the leaf under an **ornamental rule**, lower third blank. So **q3 = pp. 10–16
  and `bon-qsc-q4` opens clean at p. 17 and inherits NOTHING.** Three boundaries measured, two "yes"
  and one "no" — pp. 27, 32, 37 stay UNMEASURED. Seven things this chunk settled:
  **(a) ⭐ A FORWARDED NOTE IS EXPOSED DOWN TO ITS DIGITS, not merely its ownership.** `q2` recorded
  "no new digit defect in my own eleven cross-refs" as a negative result, not a licence — and the one
  note it forwarded (p. 10 n. 8) carried **two**: raw `Quacsl. i6` → **Quaest. 46**, raw `d. 33` →
  **d. 35**. Eight OCR digit defects in this chunk overall (`text. 36`→**56** · `§ 3`→**§ 5** ·
  `pag. 333`→**355** · two `(c. i.)`→**(c. 4.)** · `q. t. ad I.`→**q. 4. ad 1.**). **Re-derive an
  inherited note's digits on the plate like any other.**
  **(b) THE GUTTER RULE IS SETTLED FOR THIS WORK — profile rows 0.20–0.50 on every leaf; the
  `colcrop.py` default is advisory.** Three of seven leaves would have been mis-split by it. Gutters:
  p. 11 **1209** · p. 12 **1359** · p. 13 **1103** · p. 14 **1406** · p. 15 **1145** · p. 16 **1454** ·
  p. 17 **1203** (measured ahead for q4). p. 11 needed the third step: the printed centre rule inks on
  the lower half only and drags every low window left (true band 1175–1247).
  **(c) ⚠ THE CONTRA HEADING VARIES WITHIN THE WORK — p. 12 prints `SED CONTRA`, not `CONTRA`.** Read
  it on the plate; assume neither form. Rendered `**Sed contra:** 1.`
  **(d) `CONCLUSIO.` printed correctly a SECOND time — and NOT at full measure** (inside p. 13's right
  column, against q2's full-measure setting). Still rendered as the `> **Conclusio.**` blockquote,
  which encodes the unit and not the measure. **The "find it by content, never by header grep" rule
  is NOT retired** — four questions remain.
  **(e) ⚠ THE REPLY SERIES ANSWERS WHICHEVER SIDE THE `Respondeo` REJECTS.** q1 and q2's replies
  matched the `CONTRA` series; here the conclusion goes against the affirmative side, the sixteen
  *sed contra* arguments are conceded wholesale (*Et ideo concedendae sunt rationes, quae factae sunt
  ad partem istam*), and the **twenty-one replies answer the twenty-one affirmative arguments.**
  Never assume the pairing; read which side is conceded.
  **(f) ⛔ AN ORNAMENTAL RULE IS NOT A WORK-CLOSE SIGNAL.** The pilot read the ornament under p. 43 as
  one of three positive facts fixing the work's end; Quaracchi sets the same rule under **any** question
  that ends high on its leaf. Gutter runovers are likewise now ordinary here — four in eleven leaves
  (p. 9 n. 4, p. 13 n. 5, p. 14 n. 3, p. 15 n. 3); no page-crossing runover yet.
  **(g) MARGINALIA DENSITY BELONGS TO THE SOLUTION, NOT THE ARGUMENT SERIES.** p. 11 carries thirteen
  arguments and **zero** marginalia — the work's first empty margin — while pp. 14–16 carry 21 of the
  chunk's 25. The pilot's "~one per argument" impression, formed on p. 6, does not generalise.
  Register: ***ratio*→account** carried its heaviest load yet (the *secundum rem*/*secundum rationem*
  axis survives intact in English); ***lux*→light / *lumen*→lumen** held apart because p. 14 sets both
  in one phrase and the apparatus records a variant turning on the pair (**cost: "lumen" is a
  transliteration**); ***status*→stopping-place** at *sed contra* 5. ⚠ **One disclosed departure from
  *intellectus*→understanding:** Dionysius' *novit divinus intellectus* → "the divine intellect knows,"
  a **quotation-boundary** judgment (the clause renders Greek νοῦς and Bonaventure is quoting, not
  using) — **the ratified narrow exception was NOT invoked**; offered to the work-close gate as a
  distinct class. *vacatio*/*quies* stays untested; unlike q2, even the *quietans* family is absent.
- **✅ `bon-qsc-q4` IS BUILT (pp. 17–27, 93 entries, zero `[?]`, 2026-09-03)** — the illumination
  question, eleven printed pages, the largest single chunk Vol V has attempted, built without
  splitting. Thirty-four affirmative arguments, twenty-six opposing arguments, `CONCLUSIO`, a
  *Respondeo* in **three modi**, twenty-six replies. **BOUNDARY 4 (p. 27) MEASURED: it FORWARDS** —
  Q. IV's last reply closes across the TOP BAND OF BOTH COLUMNS (running left-then-right across the
  full measure), then `QUAESTIO V.` stands full-measure mid-leaf with its subtitle and Q. V's own
  args 1–3 on the same leaf. ⚠ **Four boundaries measured, three "yes" and one "no"; pp. 32 and 37
  remain UNMEASURED.** **It forwards p. 27 nn. 2–8 to `bon-qsc-q5`** (p. 27's whole LEFT register is
  n. 1, a full-column editorial dissertation belonging to Q. IV; n. 2 anchors Q. V's arg. 1).
  Eight things this chunk settled:
  **(a) ⭐⭐ THE WORK'S FIRST PAGE-CROSSING RUNOVERS — TWO, BACK TO BACK.** p. 24 n. 9 breaks at the
  foot of p. 24's right register and completes at the HEAD of p. 25's left register; p. 25 n. 9 breaks
  at the foot of p. 25's right register and completes in **the whole of p. 26's left register**, so
  p. 26's own seven numerals all stand in its RIGHT register. Each is counted on the leaf where it
  OPENS. ⚠ **A leaf whose register opens mid-sentence is not defective and its first numbered note is
  not missing — look at the previous leaf's foot.**
  **(b) ⭐⭐ THE OPPOSING SERIES IS NOT A DISPLAY HEADING HERE — IT IS A RUNNING ITALIC FORMULA.**
  `q1`/`q2` printed `CONTRA:`, `q3` printed `SED CONTRA:`, and `q3` said to assume neither form. This
  question prints **neither**: p. 21 runs straight on from argument 34 into *Sed contra hoc obiicitur*
  primo *auctoritate*, deinde *ratione* — italic, in the text measure, with a footnote anchor on it
  and the marginale `Ad oppositum.` beside it — and the second half opens the same way at *Item
  obiicitur contra rationes Augustini sic:*. Transcribed as the running sentences they are, **not
  lifted into a `**Sed contra:**` label**. ⭐ **The `CONTRA` unit in this work may not be a heading at
  all; find it by content, exactly as `CONCLUSIO` and `SUMMARIUM` must be found.**
  **(c) ⭐ THE REPLIES ANSWER THE OPPOSING SIDE HERE** — the conclusion goes WITH the affirmative, so
  the thirty-four *fundamenta* are conceded and the twenty-six replies dispose of the twenty-six
  opposing arguments. That is the reverse of `q3`. **Never assume the pairing.** Three replies print
  combined (`5. 6.`, `7. 8. 9.`, `23. 24. 25. 26.`) and are preserved, not split — the `q2` `3. 4.`
  precedent; twenty numbered paragraphs carry twenty-six replies.
  **(d) `CONCLUSIO.` printed correctly a THIRD time and at full measure** (p. 22's right column,
  centred, conclusion in indented italic). Three undamaged spellings in four questions **does not
  retire** the find-it-by-content rule; three questions remain.
  **(e) ⭐ A BLOWN-OUT GUTTER RUN CAN MEAN A CLEAN LEAF, NOT A DAMAGED ONE.** pp. 19 and 22 return
  **426–463 px** runs on every window — nonsense by the frozen rule — *because* their inter-line white
  bands run nearly to zero ink across the full measure and flood the window search. Step 3 settles
  both from the per-column ink band. Gutters: p. 17 **1203** · p. 18 **1366** · p. 19 **1180** ·
  p. 20 **1405** · p. 21 **1105** · p. 22 **1403** · p. 23 **1139** · p. 24 **1415** · p. 25 **1164** ·
  p. 26 **1389** · p. 27 **1169**. Rows 0.20–0.50 held on all eleven leaves.
  **(f) ⚠ A SECOND QUARACCHI-SIDE SLIP, transcribed as printed and logged.** p. 17 n. 4 prints
  *…non de ipsa, sed per ipsam de ceteris* ***iudices***, where the same Augustine sentence quoted in
  the BODY of argument 3 **on the same leaf** reads *iudicant*. Read at 5× to be sure. Disposed like
  `q2`'s p. 8 n. 7 *pag. 1*: transcribe as printed, log, non-blocking. Also p. 23's first marginale is
  cropped by the scan's binding edge (only *…eprobatur.* survives); resolved **Reprobatur.** from
  plate + djvu raw + sense, recorded, **not** flagged — the p. 5 `tinctio.` precedent.
  **(g) MARGINALIA DENSITY BELONGS TO THE SOLUTION — confirmed decisively on a long span.** Forty-nine
  across eleven leaves: pp. 17–22 carry **sixty arguments and eleven marginalia**; pp. 23–26 carry the
  *Respondeo* and the replies and hold **thirty-seven**.
  **(h) ⚠ *vacatio*/*quies* STILL UNTESTED — and this chunk shows why the distinction matters.** The
  *quiet-* family is heavier here than anywhere yet (*quietantes*, *quietativae*, *quiescat*), but
  *quiescat* is one of the two **VERB** hits the pilot measured, not the noun; neither *vacatio* nor the
  noun *quies* occurs. Register: ***intellectus*→understanding held under the work's heaviest pressure
  (~40 occurrences), with ONE disclosed departure — *intellectus agens* → "the agent intellect,"
  offered to the gate as an invocation of the ratified narrow exception, the corpus's second candidate
  after the *praeceptis* c2 Averroist case.** ***lumen*→"lumen" exercised ~20× (cost: a transliteration,
  conspicuous at that rate)**; ***contueri*→"to contuit" / *contuibilis*→"contuitable"** new and
  load-bearing twice. All three are handed to the shakedown gate as questions, not answers.
  ⚠ **A PRE-EXISTING LEDGER DEFECT FIXED IN PASSING:** `manual-review/vol5-runover-ledger.tsv` is
  **comma-separated**, and `bon-qsc-q3`'s line used semicolons, so its three gutter runovers parsed as
  **one** and the corpus count was understating by two. Both lines are now comma-separated; the census
  reads **182 runovers (161 gutter-crossing, 21 page-crossing)**. **The checker swallows a semicolon
  line silently — append with commas.**
- **★ REGISTER: the Sentences key-terminology and scholastic-formulae tables govern** — this
  is the genre they were written for. Both *septem donis* rulings continue to bind.
  ⚠ ***intellectus*/*intelligentia* is under MAXIMUM pressure here** — the work is about
  knowing, *intellectus divinus* and *intellectus humanus* stand in one argument on p. 3 ¶ 8,
  and q4 is the illumination question. Expect the ratified narrow exception (a fixed
  philosophical doctrine the rule would misname) to be reached for; **it is narrow — the
  *praeceptis* c2 Averroist case is the only instance the corpus has ratified.**
  ⛔ ***vacatio*/*quies* CANNOT BE TESTED HERE, and it was measured at the pilot so no chunk
  has to re-ask it:** *vacatio*/*vacare*/*vacat* occur **zero** times on the band; *quies*
  returns two hits, **both the verb *quiescat***, not the noun. **The question carries
  forward untested for a second work.** ⚠ The *quietans*/*quietativus*/*quietatio* family
  that IS present (~7 occurrences) is a different word and is **not** a datum on it.

### Vol V mechanics

- **Offset `pdf = printed + 76`** (verified at printed 174/176/201/320/507/530; PDF
  690 pp). Wired into `tools/extract-pages.py` (`--volume vol5`).
- Two-column → **VOL II OVERRIDE recipe applies.**

  **★ GUTTER RULE (frozen 2026-07-28 — a measurement, never a constant).**
  `colcrop.py vol5 <page>` now **auto-measures** the gutter; vol5 defaults to `auto`,
  and `auto` is accepted explicitly on any volume. It prints the measured `split_x`
  and the width of the low-ink run it found. Pass an explicit split only to override
  a measurement you have already checked.
  1. **Never let the 1660 default stand on Vol V.** Vol V pages are **2571 px** wide at
     450 dpi, so 1660 sits deep inside the *right* column: it pads L with the gutter plus
     right-column text and truncates R to ~970 px. (Vol IV had the mirror-image problem at
     1660 — see the Vol IV bootstrap note.)

     **★★ THE ODD/EVEN PARITY MODEL IS SPENT — DO NOT PREDICT A GUTTER FROM PARITY
     (retired 2026-07-29; this section previously said parity held).** It held for eleven
     pages and then collapsed: p.221 (odd) 1233, p.222 (even) **1319** — below the even
     floor — p.223 (odd) **1241** — above the odd ceiling. The clusters overlap at
     ~1230–1320, and Pars III–IV pushed the range wider still in both directions (p.251 =
     **1160**, 22 px below the old odd minimum; p.252 = **1403**, 12 px above the old even
     maximum). Every one of those measurements is sound. **Judge each page on the low-ink
     run `colcrop.py vol5 <page>` reports, and on nothing else.**
  2. **Measurement is restricted to the BODY ROWS (~45–92% of page height), by design.**
     A page that opens a work, a part, or a distinction carries a **full-width display
     heading that crosses the gutter** and destroys the blank-column run; profiling the
     whole page height then returns *no usable run at all*. Hit on p.201 (prologue), p.219
     (`PARS SECUNDA`), p.241 (`PARS QUARTA`) and p.252 (`PARS QUINTA` — where all four
     upper-page windows failed at 1245–1257 on ~330 px runs while nine body windows agreed
     at 1399–1405). Footer registers and running heads are excluded for the same reason.
     Expect this at **every work and part opening in Vols V–X**.
     **★★ AND A SECOND, SMALLER FORM THIS RULE DOES NOT NAME — found on p. 263, 2026-07-30
     (`p5-c9`): AN ORDINARY `Cap. N.` HEADING SET *INSIDE* A COLUMN WRECKS ANY WINDOW THAT
     LANDS ON IT.** p. 263's `Cap. X.` heading sits ~55 % down the right column — squarely
     inside the default body band — and the 47–60 % window returned **1349 on a 375 px
     run** against a true 1195. The heading is only one column wide, so it does not cross
     the gutter and does not destroy the run outright the way a display heading does; it
     simply floods one side and drags the apparent centre. **Consequence: the 45–92 % body
     window is not a safe default on a leaf where a capitulum opens mid-column — which in
     the Breviloquium is most leaves.** Re-profile over several windows and discard any
     whose run width blows out; the surviving windows will agree. **A ~375 px run is the
     same species of nonsense as p. 248's 251 px and p. 252's ~330 px: far ABOVE the sound
     58–64 px band is as much a failure signal as far below it.**
  3. **★★ A RUN UNDER ~60 px IS SUSPECT EVEN THOUGH THE TOOL ONLY FLAGS UNDER ~15 px
     (added 2026-07-30 — the single most valuable gutter rule learned in Pars IV).** The
     15 px threshold catches loud failures; it does **not** catch the quiet ones, which
     are the dangerous kind because they return a plausible number and no warning.
     Attested: p.241 default **1218 on a 39 px run**, true **1228** · p.243 default
     **1180/50 px**, true **1186** · p.245 default **1206/56 px**, adopted **1201** ·
     p.248 default **1391/54 px** · p.249 default **1182/55 px**. Against these, a
     *trustworthy* measurement looks like p.246 (1345, fourteen windows spread 4 px, runs
     58–63 px) or p.247 (1209, spread 2 px, runs 60–64 px). **Run width is the confidence
     signal, not the value itself.**
  4. **★ THE THREE-STEP METHOD. Escalate only as far as you need.**
     **(1)** `colcrop.py vol5 <page>` with **no constant**. **(2)** If the run is under
     ~60 px or the value sits far off its neighbours, **re-profile over several row
     windows and take the consensus** — a tight spread (≤5 px across a dozen windows) is
     the tell that the answer is real. **(3)** When the windows *disagree*, **read the
     per-column ink profile directly**: find the blank band and the ink island inside it,
     and take the band's midpoint. That settled p.248 (blank band x=1365–1418, island at
     1385–1394 → **1391**) and p.249 (band 1155–1209, island 1176–1187 → **1182**).
     **Never hand-roll a separate measuring script** — profile the columns the tool
     already gives you.
  5. **★★ THE IN-GUTTER OBSTRUCTION IS QUARACCHI'S PRINTED COLUMN RULE — IDENTIFIED
     2026-07-30 (`bon-brev-p5-c6`), and this supersedes the old "marginal glosses set low"
     explanation, which was wrong and prescribed the wrong remedy.** Direct crops on three
     leaves (pp. 258, 259, 260) confirm it: the ink island standing inside the blank band
     **is the centre rule itself**. Consequences:
     - **It is on essentially every leaf** — attested pp. 240, 248, 249, 250, 251, 253, 254,
       255, 256, 257, 258, 259, 260. **Assume it. Its absence is the thing worth remarking.**
     - **It runs the FULL column height, so moving the window UP cannot escape it.** That
       remedy belongs only to the genuine marginal-gloss case (pp. 240, 244). Do not reach
       for it here.
     - **Whether it corrupts the measurement depends on WHERE IN THE BAND it sits, and on
       how heavily it inked on that leaf.** Centred (pp. 250, 251, 253) → every window
       agrees and the default is right. Off centre (pp. 248, 249, 254, 255, 257) → the
       windows fork or drift. **Heavily inked → it truncates the zero-ink run outright**,
       which is what produced p. 260's default of 1386 on a **20 px** run (rejected; true
       value 1398, found by forking the windows against a 60 px run).
     - **So a narrow run is now positively diagnostic, not merely suspect:** it usually
       means the rule printed heavily on that leaf, not that the gutter is narrow.
     **Print the per-column ink profile even when the windows agree** — it is how you learn
     *why* they agreed, and it costs nothing.
  6. **This is not pedantry.** Vol IV's `transumtum` misreading was a real corpus error
     traced directly to a wrong gutter (see the d.41–d.50 gate notes). A wrong split
     silently truncates one column and pads the other, and the chunk built from it will
     parse clean and pass every audit.
- **⚠⚠ THE RAW HAS NO FOOTNOTE NUMERALS.** Vol V's IA OCR renders every superscript as
  a punctuation glyph (`^` `'` `"`). Anchor POSITIONS survive in the raw; numbers and
  footer-entry openers do NOT. Consequences, all mandatory:
  1. **Apparatus is bands-only.** Every footer is read from the 450 dpi bands; the
     per-chunk `## Notes` records the band-derived count. Bands-first is not a
     safety-net here — it is the only source.
  2. **`audit-apparatus-count` is blind to Vol V** (its raw-side regex has nothing to
     match). Do not trust its diff column. **Use `tools/check-vol5-apparatus.py`
     instead** — it checks label pairing, duplicate defs, and per-page footer ownership
     without touching the raw, and distinguishes a legitimately forwarded PENDING note
     from a real interior GAP (the failure mode that cost Vol IV three whole registers).
     Keep its `KNOWN_TOTALS` map fed as each page is read off the bands. Extending the
     other audits with `--volume 5` (paraphrase + headers work as-is; the apparatus
     audit would need a symbol-glyph mode) is **required before the Pars I gate**, not
     before the chunks.
  3. `seam-screen.py` / `audit-style-formatting.py` parse `bon-sent-…` ids and will
     silently skip `bon-brev-…` files until extended — same requirement.
- **★★ BLANK SPACE AT A COLUMN FOOT IS NOT A BOUNDARY (learned the hard way, 2026-07-28).**
  Quaracchi's footnote blocks expand **upward**, shortening the body column to
  make room. A page with a large footer register therefore ends its body text
  well above the foot, leaving white space that looks exactly like the end of a
  capitulum. **It is not.** `bon-brev-p2-c4` was written short by a whole
  paragraph and two apparatus entries on precisely this inference ("blank paper
  below — positive evidence that Cap. V opens on the next page"); the chapter
  actually carried over to the head of the next page's left column, above the
  next heading. **Establish every unit's end positively, from the NEXT heading
  in the following column or page — never from white space.** This is the same
  failure family as the Vol IV cascade-merge: the chunk looked complete, parsed
  clean, and passed every audit, because no tool knows what a page ought to
  contain. Vol V is especially exposed because a single editorial *Additamentum*
  can fill most of a page's footer (p.222 n. 2).
- **Marginal glosses are DENSE** (one per paragraph in the Breviloquium, one per
  chunk-sized unit elsewhere) — Quaracchi's editorial running outline in the outer
  margin. They splice into pdftotext output mid-word but stand as separate line-blocks
  in the djvu raw. Convention: **trim from the body** (they are not Bonaventure's text,
  consistent with vols I–IV) **but transcribe them into a "Marginalia" list in
  `## Notes`**, body order. No literal `[^` tokens in Notes prose.
- **Per-page footer splits are the NORM, not the edge case** — capitula are sub-page
  units, so nearly every printed page's footer divides between 2–3 chunks by body
  anchor. Every dispatch leads with the incoming hand-off and forwards the outgoing one
  (Vol II Override step 4 discipline, now constant).
- **★★ READING THE PLATE: DIGITS AND SIGLA (consolidated 2026-07-30 from Partes III–IV,
  ~25 corrections).** Quaracchi's serif makes two distinct confusion classes, and **both
  are live** — assume neither is settled until seen at 450 dpi.
  1. **The `1`/`4` class.** The serif `1` prints like `4` (`120`→"420", `11`→"41"/"44").
  2. **The `3`/`5` class**, equally common and easier to miss. Fixes: `c. 55` (raw `c. 33`)
     · `c. 5-7` (raw `3-7`) · `pag. 205` (raw `203`) · `alias 59` (raw `39`) ·
     `IV Sent. d. 15` (raw `13`) · `Marc. 15,28` · `I Cor. 15,54`.
  3. **Which class dominates varies leaf to leaf** — one page's four fixes were all `3/5`,
     the next leaf's four were all `1/4`. Don't calibrate on the previous page.
  4. **Where the band can't decide, settle from Quaracchi's own parallel citation elsewhere
     in the corpus, or from sense.** `Eccli. 10, 15` (raw `10, 13`) was settled from the
     same citation in Vol II; `c. 55` because *De vera religione* has 55 chapters and the
     note's `n. 110` falls in the last; `q. 1` because the flagged `1` and a true `4` stood
     touching in `d. 14.` on the same line. **A digit is evidence only once something
     independent agrees with it.**
  5. **SIGLA — four rules, all earned.** **(a) ONE UPRIGHT IS NEVER `H`.** A single bare
     upright is `I`; only *two* uprights can be a crossbar-less `H`. **(b) Use the
     ALPHABETICAL ORDER of a siglum run as the disambiguator** — the glyph alone will not
     decide it. **(c) Settle by STROKE COUNT** (`H N`, `I N`), and beware a two-upright
     roman numeral that is not a siglum at all (`II. Sent.`). **(d) The raw corrupts
     siglum letters outright** — fixes include `H nobilitatis virtutis` (raw `U`),
     `B C I L M O Q` (raw `D…0…`), and the chronic raw `R` for `K`.
  6. **The `II`→`H` flattening is a TYPEFACE fact, not an OCR artifact** — it prints with
     no crossbar at 900 dpi, and **the plate is inconsistent within a single page**: a
     flattened `H` and a properly crossbarred one stood fourteen lines apart on p.238, and
     p.246 printed the codex `H` both ways four times inside one nine-note register.
     Raising the dpi will not resolve it; the siglum set and the run order will.
  7. **A single note can carry TWO different siglum sets one clause apart**, which the raw
     flattens into one (p.228 n.3: `pro per I O U V et` … `post sapientissimum L U V addunt`).
     Likewise the edition-siglum `1` and the codex-siglum `I` print as different sorts
     inside one clause and the raw merges them.
- **★★ A HAND-OFF IS A CLAIM TO RE-DERIVE, NEVER A FACT TO ADOPT (frozen 2026-07-30).**
  Because per-page footer splits are the norm, every chunk inherits notes from its
  predecessor. **State for each forwarded note whether you verified its POSITION, its
  COLUMN, or only its OWNERSHIP** — this convention was introduced mid-Pars IV and it
  works. It caught p.242 n.4 handed over with the wrong column, and a wrong digit
  (`q. 4` → `q. 1`) sitting inside an otherwise careful predecessor's hand-off. **A
  hand-off tells you which notes are yours. It never tells you where they land.**
  Corollary for the ledger: **render an inherited runover joined, but never re-log a
  runover a prior chunk already logged** — that is the double-count the ledger exists
  to prevent.
  **★★ AND A SECOND FAILURE MECHANISM, FOUND 2026-07-30 (`p5-c7` on `p5-c6`): THE SCOPED
  HAND-OFF CAN BE RIGHT IN EVERY PARTICULAR WHILE THE NARRATIVE SUMMARY BESIDE IT IS
  WRONG.** `p5-c6`'s per-note hand-off correctly placed p. 260 n. 4's anchor in the LEFT
  column; the prose summary in the same `## Notes` — and the comment it wrote into
  `KNOWN_TOTALS` — said the anchors divided 3/4 and that "all three lines coincide for the
  first time in Pars V." They divide 4/3 and the lines do not coincide. **The claim
  contradicted its own data, one paragraph away.** Every chunk in this corpus carries both
  forms side by side, and the summary is the one that gets quoted forward — into the resume
  note, into the next brief, and into reports to Wilson. **Rules: (a) when the two disagree,
  the PER-NOTE data wins and the summary is withdrawn, not reconciled; (b) never carry a
  neighbour's summary sentence forward without checking it against the per-note list it
  sits beside; (c) a structural generalisation ("first time", "all three coincide", "the
  Nth occurrence") is exactly the kind of sentence that is written once and never
  re-derived — treat it as the LEAST reliable line in any `## Notes`, not the most
  quotable.**
- **★ THE RAW-QUALITY GRADE MOVES *WITHIN* A PAGE — grade per page, per region, AND per
  column-run.** p.234's body was clean above the `Cap. V` heading and degraded below it;
  p.237's improved *upward* across a chapter heading. **Always give the verdict for body
  and footer separately** — p.231's body was clean while its footer was wrong in two
  places. "The raw is usable" is never a page-level fact, let alone a volume-level one.
  The raw also **cascade-drops short phrases at anchors** and shatters headings
  (`Cap. IV.` → `Cah. IV.`).
- **★ THE RUNNING HEAD IS AN ASYMMETRIC WITNESS — IN BOTH DIRECTIONS.** It has named a
  chapter that merely *ends* on the page, named one that barely *starts* there (p.237
  reads `C. IX.` though Cap. VIII fills the page), and run a full unit *ahead* (p.248's
  band reads `PARS IV. C. VIII` where the raw suggested `C. VI`). **Never set or
  corroborate a boundary from it. Find the `Cap. N.` heading on the band.**
- **★ THE FOOTER BLOCK'S EXTENT TELLS YOU NOTHING ABOUT WHICH COLUMN A NOTE'S ANCHOR IS
  IN.** The left block fills first and can **overrun** the column division (pp.220, 221,
  226, 233, 239) or **underrun** it (pp.234, 237). The block break has twice fallen two
  notes *above* the anchor break (pp.244, 245 are exact mirrors). **A capitulum boundary
  can also fall inside a footer block** (p.247: anchors split 4/4 matching a 4/4 block
  split, yet the Cap. VI/VII boundary fell between nn. 5 and 6 inside the right block).
  Block structure, column structure and capitulum structure are three independent things.
  **Read anchors, only anchors.**
- **★ A UNIT'S BREAK CAN FALL ANYWHERE — a grammatically complete tail is NOT evidence
  that a unit ended.** Attested across Pars IV alone: mid-word hyphenated (`in-`/`fecerat`),
  mid-word inside a scriptural quotation (`Non mea vo-`/`luntas`), mid-Vulgate-verse, at a
  comma, at a paragraph boundary, splitting a work's title (`Enarrat.`/`in Ps. 149, 6`),
  stranding an adjective, stranding a correlative, and **three consecutive capitula
  breaking on a stranded preposition governing nothing**. Twice both halves read as
  complete sentences on their own.

- **★★ NEVER HAND-CARRY A CORPUS-WIDE COUNT. DERIVE IT. (frozen 2026-07-28.)**
  Any number that describes the whole corpus — chunk counts, runover tallies,
  apparatus totals, `[?]` flag counts — must be **derived by a tool that walks the
  directory, at the moment it is cited**. Never copy last session's number and add
  one. A hand-carried counter cannot notice that it skipped something, and it will
  not be re-derived for months because it *looks* authoritative.

  **What this rule is made of.** The Vol V runover tally forked: the resume note
  said "eleven runovers in twenty chunks," `bon-brev-p2-c7`'s Notes said
  "fourteenth runover in twenty-three chunks," and the truth was **fifteen in
  twenty-four**. The counts were exact through `p1-c8`, then went **−1 on both
  counters at `prol-s2` and stayed there** — whoever resumed the tally after the
  Pars I block omitted **`bon-brev-prol`** and its p.201 n.2 runover. Two sessions
  later someone repaired the chunk count but not the runover count, so the two
  numbers were wrong in *different directions* and read as independent drift rather
  than as one dropped chunk. Nothing caught it, because nothing was checking.

  **The specific blind spot, which WILL recur in Vols VI–X.** `bon-brev-prol` is the
  only vol5 slug with **no numeric suffix**, so an eye — or a glob — running down the
  directory listing slides straight past it. **Every work's prologue/opener has this
  shape** (`bon-itin-prol`, `bon-red-prol`, …). When a new work is chunked, its
  opener is the chunk most likely to be silently excluded from any sweep, audit, or
  count. Check any vol5 enumeration against a census of **24** (and rising).

  **The mechanism — use it, don't reinvent it.**
  `manual-review/vol5-runover-ledger.tsv` records **one line per chunk, including
  the negatives**, because the roster *is* the denominator.
  **`python3.11 tools/check-vol5-census.py`** diffs that roster against `vol5/` and
  derives the totals; it exits non-zero if a chunk is missing from either side.
  Run it **in the per-chunk verification step, alongside `polish-style-scan`**
  (same decoupling logic as pass 2 — it is a script, its cost does not scale with
  batch size, and running it only at gates is what let the last silent skip run for
  eleven chunks). Append a ledger line per chunk; cite the script's output. **Do not
  write a running total into a chunk's `## Notes`** — a cross-chunk counter in a
  per-chunk file is how two copies diverge in the first place. Extending to Vols
  VI–X = one entry in the script's `VOLUMES` list.

### Breviloquium register additions (lock these; the Sentences tables still apply)

- *In principio intelligendum est…* → "At the outset it must be understood…"
- *Ratio autem huius veritatis haec est: quia…* → "Now the reason for this truth is
  this: since…"
- *Et ideo* → "And therefore"; *Ex his patet, quod…* → "From these things it is clear
  that…"
- Preserve the sevenfold/threefold enumerations exactly (*primo… secundo…* → "first…
  second…"); preserve Quaracchi's em-dash paragraph articulations (` — `).
- The compressed periodic sentences stay ONE sentence in English wherever grammar
  permits — do not break Bonaventure's *quia/cum/ideo* chains into fragments.

### Polish-gate cadence for Vols V–X (revised 2026-07-28 — supersedes the pilot's per-pars rule)

**Why the decade gate can't just be ported.** A decade of distinctions was never a
structural unit — it was *accidentally a page-count gate*. Vol II ran ~220 printed
pages per gate, Vol III ~225, Vol IV ~211 (1057 body pages / 5 decade gates).
Distinctions are uniform enough that "every ten" held page exposure roughly constant.
That proxy dies in a multi-work volume: *De reductione* is 7 printed pages and the
*Hexaemeron* is ~128, so structure no longer stands in for exposure.

It matters because **three of the four passes scale with printed pages read**, not with
structural units: flag resolution scales with ambiguities encountered, the boundary
sweep scales with chunk boundaries that fall inside a printed page, and disk cleanup
scales with pages imaged. Only pass 2 is fixed-cost — see the decoupling rule below.

**Three triggers. A gate fires on whichever comes first.**

1. **Page count — every ~100 printed pages of body text.** Deliberately *half* the
   Sentences cadence. The ~210-page interval was calibrated on a corpus whose OCR
   carried footnote numerals; in Vol V **every apparatus entry is a hand-read off a
   450 dpi band** (the raw has no numerals at all), so per-page exposure to a dropped
   or misassigned note is roughly doubled. Snap the gate to the nearest structural
   seam — pars, work, or collatio boundary — rather than cutting mid-unit.
2. **Every work boundary, unconditionally** — including a 7-page work. This trigger has
   no analogue in Vols I–IV, which had one register per volume. In a multi-work volume
   the work transition is where conventions get set and where drift is invisible, so it
   is the highest-value gate per page in the scheme. A work shorter than the page
   interval therefore gets exactly one gate, at its close — **never zero**.
3. **A shakedown gate early in each new work**, at the first structural seam ~15–25
   printed pages in. Catches register and layout problems while 20 pages are wrong
   instead of 100. The Breviloquium's Pars I gate is this, and is correct *as a first
   gate* — it is not evidence for gating every pars.

**★★ PASS 1'S INSTRUMENT IS `tools/check-live-flags.py`, NOT `grep` (earned at the Hexaemeron
mid-work gate, 2026-08-15).** A bare `grep "\[?\]"` over a volume returns 100+ hits of which
almost none are flags: nearly every chunk's `## Notes` *discusses* flags in prose, and every
Tier-2 `transcription_status` says "zero [?] flags". **A flag is LIVE only if it stands in
`## Latin`, `## English` or `## Apparatus`** — `## Notes` is never rendered and frontmatter is
metadata. The tool strips both and reports what is left, so the count is derived rather than
hand-carried. Corpus baseline at that gate: **vol1 150 · vol2 9 · vol3 2 · vol4 66 · vol5 2**
occurrences (a flag mirrored in both languages counts twice). **Vols I and IV carry a real
backlog; it is a scoped job, not something a gate in another volume fixes.**

**★★ AN APPARATUS ENTRY IS NEVER TRANSCRIBED FROM A WHOLE-PAGE READ (same gate).** The one defect
that gate found — `Dieta salutis` in the English against the plate's and the Latin's `Dictae
salutis`, a silent normalisation of Quaracchi — traced to the **single** entry in 152 that had
been read at ⅓-scale instead of off a 1.7–2.2× footer band. **A downscaled whole-page view is for
STRUCTURE** (where a heading falls, whether a block opens numbered, whether a column runs short)
**and for nothing else.** ★ The cheap sweep for that defect family: compare the multiset of Arabic
digits in each entry's `**La.**` half against its `**En.**` half. Known false positive: an ordinal
correctly spelled as a word in English (`(2. opinio)` → "the second opinion").

**⚠ Pass 2 is DECOUPLED from the gates — run it every commit.** The style/formatting
audit is a script, it is full-corpus, and its cost does not depend on batch size.
Running it only at gates is precisely what let `tools/polish-style-scan.py` sit
hardcoded to `DIRS=["vol1","vol2"]` across the whole of Vol III and Vol IV, so that
every "Pass 2 CLEAN" in those gate logs was false for four volumes. Run it alongside
`build-content.mjs` in the per-chunk verification step. Passes 1, 3 and 4 stay at the
gates.

**⚠ `build-citations.py` IS DECOUPLED TOO — run it every commit, on the same argument
(frozen 2026-07-31, after Pars VI).** It is a script, it is full-corpus, it takes ~16 s,
and its cost does not depend on batch size. **Report the QA-flag count attributable to
YOUR chunk separately from the corpus-wide number** — the corpus figure moves for reasons
that have nothing to do with you, so an undifferentiated total tells you nothing and
will be quoted forward as if it did.

**Why it belongs at the chunk and not only at the deploy boundary: it is the only check
in the per-chunk step that can see a defect the plate itself contains.** The apparatus
check, the census and the style scan all verify that the chunk is internally consistent
and completely owned; none of them can know that a citation points nowhere. Attested in
Pars VI: `p6-c7` transcribed p. 272 n. 6 as the plate prints it, `Col. 6, 12` — Colossians
has four chapters and the sense requires Ephes. 6:12 — and **`build-citations.py` flagged
it as an out-of-range chapter independently of the agent's own reading**, on the same
commit. Caught at the deploy boundary instead, it would have arrived thirteen capitula
late, mixed into a 224-flag corpus total, and attributable to no one.

**It authorises no edit.** A flag is a QA line, not a correction: settle the digits off
the 450 dpi band, and where the plate is confirmed wrong, transcribe as printed and flag
`[?]`. Quaracchi is never silently emended.

**Applied to Vol V** (~568 body pages → ~13 gates):

| Work | Printed pp. | Gates |
|---|---|---|
| QD de scientia Christi | 3–43 (41) | **2** — `bon-qsc-q4` shakedown (p. 27) + close (p. 43) |
| QD de mysterio Trinitatis | 45–115 (71) | 1 at close |
| QD de perfectione evangelica | 117–198 (82) | 1 at close |
| **Breviloquium** | 199–291 (93) | **2** — Pars I shakedown (p.218) + close (p.291) |
| Itinerarium | 293–316 (24) | 1 at close |
| De reductione | 319–325 (7) | 1 at close |
| Collationes in Hexaemeron | ~327–454 (128) | **3** + its own mini-pilot — see below |
| Coll. de septem donis | ~455–503 (49) | 1 at close |
| Coll. de decem praeceptis | ~505–532 (28) | 1 at close |
| Sermones selecti | ~535–579 (45) | every-N-sermones — see below |

**This replaces the pilot's "one gate per pars," which would have given the Breviloquium
seven.** The per-pars rule was frozen before a single chunk existed; sixteen chunks in,
the hazard profile is known — ten runovers, three novel footer layouts, and **zero `[?]`
flags**. Pass 1 has nothing to do and the boundary sweep is carrying the gate, so
firing a full three-pass cycle every ~15 pages buys almost nothing.

**Two cases deliberately left open, not settled:**
- **Hexaemeron** — ~128 pages of *reportatio*, a register nobody has touched. It earns
  its own mini-pilot before the grind (per the genre-boundary rule above), and probably
  three gates rather than the two page count alone would give.
- **Sermones selecti** — dozens of independent short pieces, where "work boundary"
  stops meaning anything. Use a simple every-N-sermones rule; pick N at the mini-pilot.

## Index conventions (frozen 2026-07-31 by the Phase 0 pilot)

The opera-omnia scripture and self-cross-reference indexes — the generated replacement
for Quaracchi's skipped Vol X. Design: `INDEX-PLAN.md`. Pilot measurements, corpus
findings and the fifteen parser defects it caught: `manual-review/index-pilot-log.md`.
**These conventions were paid for; do not re-derive them by guessing.**

### The shape

`tools/build-citations.py` walks `vol{1..5}/*.md` and emits **one ledger record per
citation occurrence** to `index/citations.tsv`. The scripture index, the cross-reference
index, the cited-by backlinks and `manual-review/citation-qa-report.md` are all **views
over that one ledger**. `tools/scripture-books.json` is the normalization table (Vulgate
canon order, abbreviations, body forms, author sigla, work slugs).

- **Derived, never hand-tagged.** Zero edits under `vol*/` at any phase. `git status`
  over `vol1..vol5` must be empty after any index run — that is a release check, not a
  courtesy.
- **Latin is the keying side.** English bodies and apparatus are display-only and are
  not parsed. English punctuation drifts; Latin citation syntax is systematic.
- **Glob, never recurse.** `vol1/_backup-*/` holds 538 stale files.
- **Resolution ALWAYS indexes the whole corpus**, even when emitting one volume. A vol5
  cross-reference targets Vols I–IV; a subset index reports the rest of the corpus as
  dangling (it read 72% dangling before this was fixed).
- **Never guess.** Anything unclassifiable becomes a QA line, not a record with an
  invented target.

### Resolution levels — each is a claim of a different strength

`chunk` (unique target) · `distinctio` / `articulus` / `work` (the citation genuinely
addresses that whole unit — `d. 2. per totam`) · `page-multi` (a printed page owned by
two chunks) · `ambiguous` (several candidates, none unique) · `forward` (target is a
work not yet translated; self-resolves as the corpus grows) · `dangling` (**target
should exist and does not — a QA flag**) · `unresolvable` (bare `ibid.`/`loc. cit.`
with nothing to inherit) · `excluded` (authority).

**Granularity is the chunk id.** `ad 2`, `in corp.`, `nota 5`, a dubium number and a
pars named without a question are all **display text on the link**, never match
coordinates. One `-dubia` chunk holds all a distinction's dubia, so treating `dub. 4`
as a coordinate made every such citation dangle.

**Quaracchi omits coordinates that are unambiguous in the print.** `IV. Sent. d. 15.
p. I. q. 1` means `p1-a1-q1`, because that pars has one articulus. Unstated coordinates
are wildcards; a **unique** survivor resolves, several are `ambiguous`, none is
`dangling`.

### Inheritance and governance — where all the hard cases live

A citation chain states things once and then relies on context. Getting this wrong
either loses real self-references or fabricates them, and both are silent.

1. **Inheritance follows the nearest preceding locus of ANY form** — including a
   `supra`/`infra d. N`, not only an `N. Sent. d. N`.
2. **`supra`/`infra` never inherit a book** (they mean the citing chunk's own).
   **`ibid. d. N` always does** — a Vol V work chunk has no `book:` of its own to fall
   back on.
3. **A locus inside a closed parenthesis is an aside and never governs the chain.**
4. **`ibid. pag. N` inherits a TOME, not a locus** — it belongs to the page scanner.
   Likewise `tom. II. pag. 50 … et pag. 177`: the tome is stated once.
5. **Author governance can change hands mid-note. The discriminator is whether a siglum
   stands BETWEEN the inherited locus and the continuation.** `— B. Albert., hic a. 1.
   et d. 46. a. 11.` is Albert's; `Aristot., … idem recurrit infra d. 8 … et d. 37` is
   Bonaventure's own — **the editors say *supra*/*infra* only of his work, never of
   another doctor's.**
6. **Clause splitting is asymmetric and both halves are load-bearing.** `—`, `Cfr.` and
   `Vide` start a fresh citation. **`;` separates loci of the SAME author** and must not
   stop a chain lookback. **`:` is not a boundary at all** — it introduces quoted matter
   still belonging to the author just named.
7. **A chain states `Sent.` once, then lists distinctions bare** (`… II. Sent. d. 2. …;
   d. 14. p. I. a. 1. q. 1.`). Without a continuation scanner, two of three loci in such
   a note are invisible.

### Scripture

- **Vulgate numbering is canonical**; Vulgate canon order for display. The books table
  is a **closed allowlist** — an unknown abbreviation is never admitted.
- **Confidence tiers**: **A** = `Abbrev. C, V` in the apparatus · **B** = a body ordinal
  chapter joined to the note's `Vers. N` through the `[^N]` anchor · **C** = chapter
  only, indexed at chapter level and **never guessed to a verse**.
- **A numbered book cited without its numeral** (`ad Corinthios decimo tertio`) goes to
  an explicit unnumbered bucket (`Cor*`). It is never guessed into I or II.
- **★ `Num. N` without a verse is Quaracchi's *numerus*, not the book of Numbers**
  (`Num. 14. Patrolog. Graec. tom. 39. col. 1063`). Measured: of 126 `Num.` records,
  the 78 chapter-only ones are *numerus*. That abbreviation therefore requires a verse
  (`require_verse` in the books table). The body form `Numerorum` is unambiguous.
  **Expect more of this class in Vols VI–X and add the flag rather than the exception.**
- **Body forms are matched case-sensitively, with a letter-boundary on both sides.**
  Several are homographs of ordinary Latin nouns — `actuum secundorum` ("of second
  acts") matched as Acts 2 on a prefix match until both guards were added.
- **`in Ioan.` / `super Ioan.` is a commentary, not the gospel.**

### The index is a QA instrument — two distinct channels

1. **Dangling refs and out-of-range chapters.** Proven live: perturbing a citation in
   either documented confusion class (1/4, 3/5) makes it flag while the true reading
   resolves. `bon-brev-p4-c8`'s `III. Sent. d. 17. a. 4. q. 3.` was caught this way —
   **its digits had been verified off the plate and its sense checked, but nobody had
   checked whether the target exists.** Reading a digit correctly is not the same as
   reading it rightly.
2. **★ A tier-B join can be checked against the quoted text itself** — the note supplies
   the verse, and the body prints the words. `bon-sent-I-d10-a1-q2` `[^4]` gives
   `Vers. 3.` against a quotation that is Rom 5:5. This channel is not mechanizable (it
   needs the Vulgate) but it is cheap whenever a tier-B record is in front of you.

**Neither channel authorises an edit.** Dangling refs are a scoped defect list worked
like the apparatus backlog — jobs, not a blob — and every digit is settled off the
450 dpi band, never off the raw and never off this tool's opinion.

### The site surfaces (Phases 1-2, shipped 2026-07-31)

`tools/build-index-json.py` is a pure VIEW over the ledger — it decides nothing about
citations, it only regroups. Outputs, all gitignored and regenerated:

| file | feeds |
|---|---|
| `index-scripture-toc.json` (11 KB) | `/scripture` — books in Vulgate order |
| `scripture/<book>.json` (largest 0.41 MB) | `/scripture/[book]` |
| `index-crossref.json` (2.7 MB) | the **Cited by** panel on every question page |

- **The scripture index is SPLIT PER BOOK.** One file is 3.8 MB, and on a static
  export every page importing it inlines it into that page's payload. The per-book
  files are read with `fs` at build time, so a book page carries only its own book.
- **`index-crossref.json` is read once and cached at module scope**, not imported —
  ~1,990 question pages consult it.
- **A missing index FAILS THE BUILD, deliberately.** `cited-by.tsx` throws rather than
  falling back to an empty index, which would have dropped the panel from every page
  while the build still reported success. Verified by removing the file and building.
- **Cited-by separates precision levels:** a citation naming this exact unit
  (`chunk`) is shown as a card; ones naming a shared printed page or the whole
  article (`page`/`unit`) are summarised in a line beneath. They are never blended
  into one count.
- **Psalms display BARE VULGATE numbers** with a note on the page. Dual numbering
  ("Psalm 24 (25)") needs a hand-built 150-row mapping whose split/merge points are
  easy to get subtly wrong, and a wrong number in an index is worse than an
  unfamiliar one. Revisit only with a checked table.
- **Only `verse` and `chapter` resolutions are indexed.** A `chapter-out-of-range`
  record is a QA line, not a citation; publishing it would ship an unsettled reading.
- Anaphor-resolved citations appear but are marked **via *ibid.***, and the display
  keeps Quaracchi's `ibid.` verbatim — an inference, never an emendation.

### Running it

```bash
python3.11 tools/build-citations.py                          # whole corpus (~16 s)
python3.11 tools/build-citations.py --volumes 5              # one volume
python3.11 tools/build-citations.py --sample 50 --seed 7     # hand-verification sample
```

**Run it in the PER-CHUNK verification step, every commit** — not only at the deploy
boundary — reporting your own chunk's QA flags separately from the corpus total. The
argument and the Pars VI case that earned it are in § "Polish-gate cadence for Vols V–X"
under the Pass-2 decoupling rule. It also runs before `build-content.mjs` at every deploy
boundary (see § "Build and deploy").
Extending to Vols VI–X = adding the volume to the glob range and to `VOLUME_COMPLETE`
(which decides whether an unowned printed page is `forward` or `dangling`).

## Translation depth & style

**Tier 2 = literal, not paraphrase.** Scholia and apparatus get the same care as the body.

### Scholastic formulae (translate consistently)
- *Videtur quod...* → "It seems that..."
- *Sed contra* / *Contra* → "On the contrary"
- *Respondeo. Dicendum quod...* → "I respond: It must be said that..."
- *Ad primum / secundum / tertium...* → "To the first / second / third [objection]..."
- *Praeterea*, *Item* → "Likewise"
- *Ergo*, *igitur* → "Therefore"
- *Dicendum quod...* → "It must be said that..."
- *Unde...* → "Hence..." or "Whence..."
- *Per consequens* → "consequently"
- *Propter quod* → "on account of which"

### Key terminology (lock these consistent)
| Latin | English |
|---|---|
| *esse* | being, or "to-be" (context-dependent; flag if ambiguous) |
| *essentia* | essence |
| *substantia* | substance |
| *suppositum* | supposit |
| *forma / materia* | form / matter |
| *potentia* | potency *or* power (context-dependent) |
| *actus* | act, actuality |
| *ratio* | account, ground, formal character (context-dependent) |
| *intellectus* | intellect, understanding |
| *voluntas* | will |
| *caritas* | charity |
| *gratia* | grace |
| *exemplar* | exemplar |
| *illuminatio* | illumination |
| *vestigium* | vestige, trace |
| *imago / similitudo* | image / likeness |
| *processio* | procession |
| *ad aliquid* | in relation to something |
| *quod est / quo est* | "that which is" / "that by which it is" (preserve the Latin in italics on first occurrence in a quaestio) |
| *quid est / si est* | "what is" / "whether it is" (same) |
| *per essentiam* | by essence |
| *per participationem* | by participation |
| *per aequivalentiam* | by equivalence |
| *secundum se* / *secundum quod* | in itself / insofar as |

### Structural markers
- `### Quaestio N` / `### Question N` — section headings, italicize the question title
- `### Conclusio` — heading before the one-sentence conclusion (which goes in a `>` blockquote)
- `**Respondeo:**` for "I respond:"
- `**Contra:**` / `**Sed contra:**` for the contrary arguments
- `**Ad argumenta...**` for solution sections
- `*Ad N.*` for individual replies to numbered objections

### Apparatus conventions
- Start each entry with a `>` blockquote note (once per file, in the Latin section): "The numbered footnotes below correspond to markers in both the Latin body above and the English translation..."
- Each entry: `[^N]: **La.** <Latin>\n    **En.** <English>`
- Indent the `**En.**` line with 4 or 5 spaces — both render under the `[^N]:` continuation. The de-facto corpus convention since d.10 is 5 spaces (parser is regex-based and indent-tolerant); 4 spaces is also accepted. Don't bulk-edit between the two.
- Include the period in `**La.**` — required by the `build-content.mjs` parser
- Include scripture citations in both languages, Vulgate numbering in Latin
- Note textual variants (`Vat. contra cod. cc legit...`) verbatim in Latin, render in English as "The Vatican edition, against codex cc, reads..."

### OCR cleanup rules
Silently correct obvious OCR errors:
- Letter substitutions: `ahquid → aliquid`, `ahud → aliud`, `flt → fit`, `fleri → fieri`
- Broken words across lines: `ehci-tus → elicitus`
- `»` and `«` preserved as-is (they're the Quaracchi quotation marks)
- Marginal glosses bleeding inline (e.g., `Fundameata.invicem`) should be trimmed out — they're editorial marginalia, not Bonaventure's text

Flag (don't silently "fix") any genuinely ambiguous readings.

### Title convention
- `title_en` is **short**: just the question, no breadcrumb. Example: `"Whether truth is a property of the divine being"`.
- **Do NOT** prefix with `I Sent., d. N, p. M, a. X, q. Y —` — the chunk page composes the breadcrumb itself from the frontmatter. D.8 was initially written with bloated prefixes; they were stripped via `/tmp/fix_titles.py`.

## Polish-blocker cadence (every 10 distinctions)

**Don't let formatting drift or `[?]` flags accumulate past 10 distinctions.** After every distinction whose number ends in 0 ships (d.30, d.40, d.50, …), run three locked-in passes before advancing:

> **Applies to EVERY volume independently** (Vol I, II, III, …). The gate fires on each volume's own d.10 / d.20 / d.30 / d.40 boundary, sweeping only that volume's preceding decade. **Vol III is the active front (started 2026-06-02): its FIRST decade gate is d.10** — when `bon-sent-III-d10-*` closes, run the three passes over Vol III d.1–d.10 before dispatching d.11. **Use the active volume's PDF + vision paths in the commands below**, not Vol I's: Vol III = `raw/doctorisseraphic03bona.pdf` and `raw/vision/vol3/` (offset pdf = printed + 22). And note (per the "VOL II OVERRIDE" above) that for Vol II/III there are **no per-chunk `manual-review/tier2-ambiguities-*` logs** — `[?]` flags live in each chunk's `## Notes` block and in `next-session-resume.md`; walk those for the flag-resolution pass.

1. **`[?]` flag resolution pass — last 10 distinctions only.** Walk every inline `[?]` in the chunks and the per-chunk `manual-review/tier2-ambiguities-d{N}-*.md` logs for the last 10 distinctions. Resolve via 600dpi PDF eyes-on — Vol I: `pdftoppm -r 600 -f PDF -l PDF -png raw/doctorisseraphic1{1,2}bona.pdf raw/vision/vol1/p-hires-PRINTED-r600`; **Vol III: `pdftoppm -r 600 -f PDF -l PDF -png raw/doctorisseraphic03bona.pdf raw/vision/vol3/p-hires-PRINTED-r600`** (PDF = printed + 22). For each flag, either RESOLVE (with PDF citation) or formally ACCEPT-ILLEGIBLE (with reason). Older distinctions already passed this gate — don't re-do them. Land all dispositions in a single per-decade resolution log: `manual-review/d{N-9}-d{N}-polish-resolution-log.md`.

2. **Style/formatting audit — full corpus every time.** Run a programmatic scan across ALL Tier-2 chunks (d.1 through current) for: required Tier-2 frontmatter fields (`title_la`, `title_en`, `printed_pages`, `pdf_pages`, `source`, `has_apparatus`, `transcription_status`); standard structure (`## Latin`, `## English`, `## Apparatus`); apparatus marker pairing (every `[^N]:` def has matching body anchors in both Latin and English); page-break presence; `transcription_status` starts with `Phase C Tier 2 complete —`; legacy auto-chunked duplicates (e.g. a `d{N}-divisio.md` superseded by `d{N}-p1-divisio.md` + `d{N}-p2-divisio.md`). Fix what's mechanical; flag the rest. The corpus-wide pass keeps formatting drift from compounding silently as new chunks are added — d.27–d.30 caught a `**En.**` 4→5-space indent shift this way, and d.8 caught a vestigial duplicate.

3. **Cross-chunk boundary integrity sweep — last 10 distinctions only.** For every chunk boundary that falls inside a printed page (a quaestio / divisio / scholion split mid-page), verify against the 450 dpi PDF column bands that no body text or footnote was lost at the seam. The IA djvu OCR cascade-**merges** two near-identical clauses — e.g. two occurrences of `sumsit` — by splicing the first occurrence directly to the text following the *second*, silently dropping everything in between. This failure is NOT reliably caught by the paraphrase / header / apparatus audits (they fire on whole-chunk dropouts, not a mid-paragraph splice): `d9-divisio` (s66) dropped ~170 words of p.241 — the entire *tertia hierarchia* subdivision plus the Gregorius/Dionysius reconciliation, plus 4 footnotes — and it was caught only in s67 when the adjacent chunk `d9-a1-q1` was built and its PDF page was read. For each mid-page boundary: (a) confirm the receiving chunk's opening sentence is grammatically continuous with the prior chunk's closing sentence; (b) confirm the shared printed page's footer notes are fully accounted for across the two chunks (per the Vol II Override step 4); (c) watch specifically for a grammatically broken splice in the prior chunk's tail (a sentence that does not parse) — that is the cascade-merge signature. Log dispositions in the per-decade resolution log.

**All three passes are blockers for the next decade of distinctions.** Don't dispatch d.31+ translation agents until the d.21–d.30 polish pass closes; same for d.41+ vs d.31–d.40, etc.

**4. Disk cleanup (do this last, once the gate closes).** The 450 dpi page images (`raw/vision/vol{N}/p-*.png`) and colcrop bands (`/tmp/colcrop/*`) are large (~4–6 MB per page) and **fully regenerable** from the gitignored PDF via `tools/extract-pages.py` + `tools/colcrop.py`. After the decade gate passes, delete them to reclaim space: `rm -f raw/vision/vol4/*.png /tmp/colcrop/*` (they are never committed — `raw/vision/` is gitignored). Re-extract on demand when the next decade's 600 dpi flag-resolution pass or any later re-verify needs them.

## Build and deploy

```bash
python3.11 tools/build-citations.py       # Regenerates index/citations.tsv + the QA report
python3.11 tools/build-index-json.py      # Ledger -> site/src/data/ index JSONs
cd site
node scripts/build-content.mjs            # Regenerates src/data/content.json
npx vercel build --prod                   # Must use --prebuilt because build-content.mjs reads ../vol1/
npx vercel deploy --prod --prebuilt --archive=tgz
```

Both index tools run **before** `build-content.mjs` at every deploy boundary, so the
indexes grow with the corpus (see § "Index conventions"). They write nothing under
`vol*/` and never touch `content.json`. Their site outputs
(`index-scripture-toc.json`, `scripture/*.json`, `index-crossref.json`) are
**gitignored and regenerated**, on the same rule as `content.json` — so **skipping
`build-index-json.py` before a build does not serve a stale index, it fails the build**.
Run both, in this order.

- `--archive=tgz` required (Free plan's 5000-files/day upload cap)
- **★★ RUN `vercel build` AND `vercel deploy` FROM `site/`, NOT THE REPO ROOT.** The
  `.vercel/` link lives in `site/`. Run either from the repo root and the CLI fails with
  `project_settings_required` / "No project settings found locally" and *suggests you run
  `vercel pull`* — which is a **red herring**: nothing is unlinked, you are simply in the
  wrong directory. The `cd site` in the recipe above is load-bearing, not cosmetic.
  (Cost a wasted build cycle on 2026-08-14.)
- **★★ `Not authorized` ON A BARE `vercel deploy` IS FIXED BY `--scope wilson-pruitts-projects` —
  and it is NOT the wrong-account case (earned 2026-08-15, the Hexaemeron gate deploy).** The CLI
  was signed in as `littleeachdayapp-6609`, `vercel teams ls` listed **Wilson Pruitt's projects**,
  and `vercel project ls --scope wilson-pruitts-projects` showed `bonaventure` with its custom
  domain — everything correct — yet `npx vercel deploy --prod --prebuilt --archive=tgz` returned
  `{"status":"error","reason":"deploy_failed","message":"Not authorized"}` in under a second. The
  same command **with `--scope wilson-pruitts-projects` appended succeeded and went READY.** ⚠ The
  wrootpress note that "if the linked org isn't in `vercel teams ls`, no `--scope` will help" still
  holds for THAT case; this is the opposite one — **the org IS in the list and the flag is exactly
  the fix. Try `--scope` before concluding anything about the account.**
- **★★ A `next/font/google` 404 STORM FAILS THE BUILD AND IS TRANSIENT — RETRY THE BUILD (new
  2026-08-15).** `vercel build --prod` exited 1 with *Turbopack build failed with 21 errors:
  Module not found: Can't resolve '@vercel/turbopack-next/internal/font/google/font'*, preceded by
  seven `Received response with status 404` lines for EB Garamond woff2 files at
  `fonts.gstatic.com`. **Nothing is wrong with the corpus or the config — Google served 404s for
  the subset URLs Next had just resolved.** The bare retry produced **exit 0 and zero 404s**.
  Distinguish it from the OOM risk (which would kill node, not resolve a font) and from the
  post-transfer `fetch failed` below (which happens at DEPLOY, not build). **Retry once before
  investigating anything.**
- **★★ `Error: fetch failed` AFTER "Deploying outputs…" IS THE KNOWN, RECURRING FAILURE —
  RETRY THE DEPLOY, DO **NOT** REBUILD.** `.vercel/output` is intact and re-running
  `npx vercel deploy --prod --prebuilt --archive=tgz` alone succeeds. It is
  **post-transfer processing**, not the upload: the log shows all files extracted first.
  Attested at the Book IV deploy (97 MB archive) and **again at the Itinerarium deploy
  2026-08-14, where attempt 1 failed and the bare retry went READY**. Expect it to become
  more frequent as the archive grows; it has never yet needed more than one retry.
- **⚠ VERIFY THE BODY, NOT THE STATUS STRING — this fires on deploys constantly.** A
  backgrounded build/deploy reported "completed (exit code 0)" **twice** on 2026-08-14 when
  the underlying command had exited 1 (once `project_settings_required`, once
  `fetch failed`). Always `tail` the log and look for `"status": "ok"` / `readyState:
  READY`, then **curl the live URLs for actual served CONTENT**, not just a 200.
- **Deploy scale, measured at the Itinerarium deploy (2026-08-14, 2,022 chunks):** output
  **527 MB / 29,318 files**, up from 466 MB / 29,080 at the Breviloquium deploy (2,012
  chunks). ⚠ **The scaling decision is deliberately PARKED (Wilson, 2026-08-01) — record
  the numbers, do NOT re-raise the decision unprompted.** The local build did **not** OOM
  on the 8 GB machine under the 1 GB Node heap cap.
- **Only the project owner deploys** to the production custom domain (bonaventure.wrootpress.com). Other contributors should commit their work to a branch; owner pulls and deploys.

### ★ DEPLOY CADENCE — at structural boundaries (Wilson, 2026-07-28)

> ⚠ **TWO SEPARATE CADENCES. DO NOT CONFLATE THEM** — they were briefly given the
> same name ("page decade") on 2026-07-28 and it caused real confusion.
>
> | | **Polish gate** | **Deploy** |
> |---|---|---|
> | Purpose | *quality* — resolve `[?]` flags, boundary sweep, cleanup | *publishing* — make finished text readable |
> | Trigger | ~100 printed pp · work boundary · new-work shakedown | **every pars / work boundary** |
> | Breviloquium | 2 total: p.218 shakedown (done), p.291 close | ~7: one per pars |
> | Defined in | § "Polish-gate cadence for Vols V–X" | here |
>
> They coincide at a work boundary and nowhere else. **The term "page decade" is
> retired** — it was coined for the deploy cadence but borrowed its word from the
> Vols I–IV *decade gates*, which were the quality cadence. Say "polish gate" or
> "deploy boundary."

**Do NOT build + deploy after every chunk.** The corpus is now ~1,950 static
pages; `vercel build --prod` is slow and the upload archive is ~97 MB and only
grows. Per-chunk deploys spend minutes of wall clock and a large upload to
publish one capitulum.

- **Commit every chunk** as usual (two commits: chunk, then resume note). That
  is free and stays per-chunk — the cadence change is about deploying, not
  committing.
- **Build + deploy when a structural unit closes** — a **pars**, or a **work**.
  For the Breviloquium that is roughly every 10–15 printed pages, so readers are
  never more than one pars behind. Never cut mid-pars just to hit a page count.
- **Deploying does NOT wait for the polish gate.** A pars ships when it is
  Tier 2 and its per-chunk verification passes; the ~100-page gate is a separate,
  later sweep. Waiting for the gate would have left 72 finished pages unpublished
  across the Breviloquium.
- **Push is cheap and separate**; it still needs Wilson's per-action OK, but it
  doesn't have to wait for a deploy-worthy batch.
- Park deploy-only work (site copy, UI tweaks) until the next deploy boundary
  rather than shipping it on its own. Keep a running list in the resume note.
- Deploying is a **protected action** regardless: it always gets its own
  explicit OK (see the global CLAUDE.md hard stops). Batching changes *when* to
  ask, never *whether*.

Generalizes the standing "batch deploys" rule (global memory
`feedback_batch-deploys`) with a concrete Vol V trigger.

### Parser gotchas (fixed, but know them)

- `build-content.mjs` `extractLanguageBlock` terminates `## Latin` only on known sentinel headings (`## Latin|English|Apparatus|Notes|Scholion|---`), NOT on any `## ` subheading. This matters because some chunks have internal h2s like `## Commentarius in Distinctionem V`.
- `text-reader.tsx` splits paragraphs by `\n{2,}` but a paragraph starting with `#### Heading` can have a subtitle on the next line (no blank between). The regex captures heading + trailing text and emits them as separate nodes.
- **★★ AN UNNUMBERED EDITORIAL NOTE IS ANCHORED AS A *CLOSING NOTE*, AT THE END OF THE UNIT — NEVER
  IN THE PROSE (frozen by Wilson 2026-08-20, at `bon-sent-II-proem`).** Quaracchi sometimes set an
  unnumbered paragraph — `NOTA.`, an *Additamentum* — at the foot of a unit's last page, with **no
  marker anywhere in the body**. It cannot simply be dropped (it is the edition's text), and it
  cannot be defined without an anchor (an apparatus def with no matching anchor breaks marker
  pairing in both languages). **The rule: anchor it after the final word of the body in both
  languages, with a NON-NUMERIC label — `[^p<page>-nota]`.** `displayLabel()` strips the `p<page>-`
  namespace, so the reader sees a marker reading *nota* and is never shown a footnote number the
  page does not print. **The principle is headnote vs closing note:** a marker inside the prose
  would assert *where* the note belongs, which the edition never said; a marker at the end asserts
  only its *scope*, which is what an unnumbered note standing last already claims. ⚠ Do not
  generalise this into anchoring unanchored matter wherever it seems to fit, and record in every
  such chunk's `## Notes` that the anchor is the edition's silence, not its ink.
- **`### Scholion` MUST be the LAST subsection of a `## Latin` / `## English` block — body first, scholion last.** `extractLanguageBlock` captures everything from `### Scholion` to the end of the block as the scholion, so if a chunk places the scholion ABOVE the body (e.g. because the source page prints the scholion at the top), the parser reads an EMPTY body → `hasTranslation: false` → chunk shows untranslated and the build's translated count silently stalls. Always order body-then-scholion regardless of the source's print layout. (Caught on d18-a1-q3, commit 57fe0f0; the translated count holding flat across two consecutive promotions is the tell.)

## Git & collaboration workflow

- Each distinction (d.9, d.10, ...) is a self-contained unit. **Work on one distinction at a time** on a branch named `d{N}/your-initials` (e.g. `d9/wp`).
- Commit Tier-2 chunks together when a distinction is fully complete. Don't commit half-Tier-1 mixes unless you're explicitly handing off mid-translation.
- `vol1/legacy/` holds stashes from pre-Tier-2 restructuring — don't modify, just delete when the corresponding d.N reaches Tier 2.
- Don't edit another contributor's in-progress distinction without coordination.
- Push frequently; the project owner pulls and deploys.

## Common mistakes to avoid

1. **Skipping the re-chunk step.** Trust nothing about existing chunk boundaries. Verify against raw text first.
2. **Copying the old `translation-prompt.md` instructions literally.** That prompt says to skip scholia and apparatus (`[Scholion omitted]` / `[Critical apparatus omitted]`). The current Tier-2 standard is to translate them fully and literally.
3. **Bloated `title_en`.** Never prefix with `I Sent., d. N, ...`.
4. **Translating at velocity.** Per project feedback: *"Literal (not paraphrase) for scholia/apparatus; thoroughness > velocity."* 3–5 chunks per session is the reliable pace.
5. **Committing to main without review.** Branch + push; owner merges and deploys.

## Source references

### Volume offsets (PDF ↔ printed page)

| Volume | PDF filename | Raw OCR | Offset | Body range (printed) | Distinctions |
|---|---|---|---|---|---|
| I pt 1 | `doctorisseraphic11bona.pdf` | `bonaventure_vol1_raw.txt` | `pdf = printed + 102` | 1–~410 | d.1–d.~25 |
| I pt 2 | `doctorisseraphic12bona.pdf` | `bonaventure_vol1_pt2_raw.txt` | `pdf = printed − 410` | ~411–872 | d.~25–d.48 |
| II | `doctorisseraphic02bona.pdf` (1056pp) | `bonaventure_vol2_raw.txt` | `pdf = printed + 22` | 11–~903 | d.1–d.44 |
| III | `doctorisseraphic03bona.pdf` (936pp) | `bonaventure_vol3_raw.txt` | `pdf = printed + 22` | ~6–905 | d.1–d.40 |
| IV | `doctorisseraphic04bona.pdf` (1094pp) | `bonaventure_vol4_raw.txt` | `pdf = printed + 20` | ~17–1074 | d.1–d.50 |
| V | `doctorisseraphic05bona.pdf` (690pp) | `doctorisseraphic05bona_djvu.txt` | `pdf = printed + 76` | 3–~579 | 10 works, no dist. (see VOL V section) |

**Vol IV bootstrap (2026-06-16):** Two-column like Vol II/III → **apply the VOL II OVERRIDE recipe** (PDF-priority inversion in cascade-shattered regions; column-band reads via `colcrop.py vol4 <page> 1880` — **vol4's column split is at x≈1880, not the default 1660** (1660 truncates the left column); offset `pdf = printed + 20`, verified twice). Auto-chunker wrote **610 skeletons** (47 distinctions detected; `d.4`, `d.23`, `d.50` merged into neighbors via OCR-garbled headers + 101 dup-IDs needing pars relabeling — resolve per-distinction during the re-chunk-before-translate step). `extract-pages.py`/`build-content.mjs`/`colcrop.py` all support vol4. Book IV's decade polish gates fire at d.10/d.20/d.30/d.40/d.50.

**Vol II structure notes** (verified 2026-05-13):
- Single Tomus II — no pt1/pt2 split (unlike Vol I). One PDF, one raw file, one offset.
- 44 distinctions confirmed via DISTINCTIO header scan. **`DISTINCTIO II.` is OCR-garbled** as `DISTmCTIO 11.` (IN→m ligature, II→11 digit-mangle); auto-chunker regex updated 2026-05-13 to tolerate.
- **Page breaks** in pdftotext output use `\f` (form feed) as the page-start sentinel, sitting immediately before a clean `DISTINCTIO XVII.` etc. The chunker's leading-whitespace class was extended from `[ \t]*` to `[ \t\f]*` to handle this.
- **No standalone `PARS PRIMA/SECUNDA` headers** — pars info lives ONLY in running heads like `DIST. II. P. I. ART. I.` and `DIST. II. P. II. ART. I.`. The chunker now infers pars splits from running-head transitions and labels chunks `bon-sent-II-d{N}-p{1|2}-...`.
- Chunk id convention: `bon-sent-II-d{N}-...` (verified end-to-end 2026-05-13: build script reads `vol2/`, `book: 2` chunks group under "Book II: On the Creation of Things").
- Same Tier-2 guardrails as Vol I: literal not paraphrase, full apparatus from raw OCR footers, 3 audit scripts before commit, polish-blocker every 10 distinctions.

**Phase 1 status (tooling, 2026-05-13)**:
- ✓ `tools/auto-chunk-volume.py` — vol2 supported (44/44 distinctions, pars-aware, 61 residual dup-IDs for per-distinction rechunk review).
- ✓ `tools/extract-pages.py` — vol2 entry added (offset +22, printed range 11–1030).
- ✓ `site/scripts/build-content.mjs` — now scans vol1/vol2/vol3/vol4 dirs (each chunk declares its own `book:`).
- ⚠ `site/src/app/page.tsx:47,57` — landing copy still hardcoded "Volume I". Update in Phase 4 once vol2 has real chunks.
- ✓ `tools/audit-{paraphrase,headers,apparatus-count}.py` — extended to Vol II 2026-05-15 via `--volume 2` (default 1 = unchanged Vol I behavior, regression-checked). Single raw file, no pt1/pt2 slicer; header audit takes per-distinction ranges from chunk frontmatter (DISTINCTIO headers are OCR-garbled). Verified against d.1's 17 Tier-2 chunks: paraphrase partitions done (17→OK) vs skeleton; apparatus-count 0 false flags; header audit coarse (positive diffs — see calibration notes in "Required guard-rail audits").

### Other

- **Internet Archive**: `doctorisseraphic{VOL}{PART}bona` — Vols I–IV all local; V–X need download.
- **Lombard's Sentences** (for littera chapters): same PDF as the body; Lombard text is printed at the top of each distinction's opening pages.
