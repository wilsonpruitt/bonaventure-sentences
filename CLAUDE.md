# Bonaventure Sentences — Project Guide for Claude

You are working on an English translation of **St. Bonaventure's *Opera Omnia*** (Quaracchi edition, 1882–1902). Status (2026-06-01): **Vol I (Book I, 48 dist.) and Vol II (Book II, 44 dist.) are fully Tier-2 and published.** The active front is **Vol III** (Book III, 40 dist.); Book IV has 50 dist. The live site is https://bonaventure.wrootpress.com. Always defer to `next-session-resume.md` for the exact current position.

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
| 2 | QD de scientia Christi | 3–43 | `scientia-christi` | 8 | planned |
| 3 | QD de mysterio Trinitatis | 45–115 | `mysterio-trinitatis` | 9 | planned |
| 4 | QD de perfectione evangelica | 117–198 | `perfectione-evangelica` | 10 | planned |
| 5 | **Breviloquium** | 199–291 | `breviloquium` | 5 | **ACTIVE — pilot done** |
| 6 | Itinerarium mentis in Deum | 293–316 | `itinerarium` | 6 | planned (next after Breviloquium) |
| 7 | De reductione artium | 319–325 | `de-reductione` | 7 | planned |
| 8 | Collationes in Hexaemeron | ~327–454 | `hexaemeron` | 11 | planned — **NOTE: it is in Vol V, not Vol VII as the old tracker claimed** |
| 9 | Coll. de septem donis | ~455–503 | `septem-donis` | 12 | planned |
| 10 | Coll. de decem praeceptis | ~505–532 | `decem-praeceptis` | 13 | planned |
| 11 | Sermones selecti | ~535–579 | `sermones-selecti` | 14 | planned |

Suggested order after Breviloquium: Itinerarium → De reductione → the three QD (register
carries over from the Sentences almost unchanged) → Collationes (new reportatio register,
own mini-pilot) → Sermones.

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
     1660 — see the Vol IV bootstrap note.) Measured values so far: p.210=1350, 211=1175,
     212=1335, 213=1126, 214=1397, 215=1163, 216=1385, 217=1180, 218=1377, **219=1171**.
     **Parity alternation holds** (odd 1126–1180, even 1335–1397) but drifts up to ~54 px
     within each cluster — which is exactly why the per-page measurement is not optional.
  2. **Measurement is restricted to the BODY ROWS (~45–92% of page height), by design.**
     A page that opens a work, a part, or a distinction carries a **full-width display
     heading that crosses the gutter** and destroys the blank-column run; profiling the
     whole page height then returns *no usable run at all*. Hit on p.201 (prologue) and
     again on p.219 (`PARS SECUNDA`). Footer registers and running heads are excluded for
     the same reason. Expect this at **every work opening in Vols V–X**.
  3. **A run narrower than ~15 px means the measurement FAILED** — the tool flags it.
     Re-measure over a narrower row window and confirm visually before use. A value far
     outside the page's parity cluster is equally suspect. This is not pedantry: Vol IV's
     `transumtum` misreading was a real corpus error traced directly to a wrong gutter
     (see the d.41–d.50 gate notes).
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
- Quaracchi's serif `1` prints like `4` (`120`→"420", `11`→"41"/"44"). Cross-check any
  digit read against a second occurrence on the page before recording it.

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

**⚠ Pass 2 is DECOUPLED from the gates — run it every commit.** The style/formatting
audit is a script, it is full-corpus, and its cost does not depend on batch size.
Running it only at gates is precisely what let `tools/polish-style-scan.py` sit
hardcoded to `DIRS=["vol1","vol2"]` across the whole of Vol III and Vol IV, so that
every "Pass 2 CLEAN" in those gate logs was false for four volumes. Run it alongside
`build-content.mjs` in the per-chunk verification step. Passes 1, 3 and 4 stay at the
gates.

**Applied to Vol V** (~568 body pages → ~13 gates):

| Work | Printed pp. | Gates |
|---|---|---|
| QD de scientia Christi | 3–43 (41) | 1 at close |
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
cd site
node scripts/build-content.mjs            # Regenerates src/data/content.json
npx vercel build --prod                   # Must use --prebuilt because build-content.mjs reads ../vol1/
npx vercel deploy --prod --prebuilt --archive=tgz
```

- `--archive=tgz` required (Free plan's 5000-files/day upload cap)
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
