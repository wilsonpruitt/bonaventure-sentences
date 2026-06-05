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
6. **Littera Magistri** (Lombard's text) for any multi-chapter distinction should be its own big Tier-2 chunk, separate from the Bonaventure commentary. See `vol1/bon-sent-I-d8-littera.md` as the template.
7. Write a re-chunking script per distinction (see `/tmp/rechunk_d8.py` pattern). Preserve frontmatter, replace only the `## Latin` body.

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

## Build and deploy

```bash
cd site
node scripts/build-content.mjs            # Regenerates src/data/content.json
npx vercel build --prod                   # Must use --prebuilt because build-content.mjs reads ../vol1/
npx vercel deploy --prod --prebuilt --archive=tgz
```

- `--archive=tgz` required (Free plan's 5000-files/day upload cap)
- **Only the project owner deploys** to the production custom domain (bonaventure.wrootpress.com). Other contributors should commit their work to a branch; owner pulls and deploys.

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
| IV | `doctorisseraphic04bona.pdf` | `bonaventure_vol4_raw.txt` | TBD | TBD | TBD |

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
