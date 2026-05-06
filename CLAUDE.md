# Bonaventure Sentences — Project Guide for Claude

You are working on an English translation of **St. Bonaventure's *Opera Omnia*** (Quaracchi edition, 1882–1902). Current scope: Volume I (*Commentarius in I Sententiarum*). The live site is https://bonaventure.wrootpress.com.

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

### The canonical Latin source of truth is the IA djvu.txt OCR — NOT eyes-on-PDF reads

`raw/bonaventure_vol1_raw.txt` is a verbatim copy of `doctorisseraphic11bona_djvu.txt` from Internet Archive (likewise pt2). This is ABBYY-quality OCR and is dramatically more accurate than reading small-set Quaracchi printed text at any reasonable PDF dpi. Reading the printed page directly will produce errors (e.g. `bonus` misread as `utens`, `homo` as `bonum`, `proceditur` reversed to `procedam`) that the OCR gets right.

### Per-chunk recipe (lock to this exactly)

For any chunk that needs to be promoted to Tier 2 — whether re-verifying a "first-pass" chunk like d.1's, or building from a skeleton like d.13+:

1. **Find the OCR line range** for the chunk in `raw/bonaventure_vol1_raw.txt` (or `_pt2_raw.txt`). Use `grep -n` for the chunk's distinctive headings (e.g. `ARTICULUS I.`, `QUAESTIO I.`, the title in `title_la` frontmatter). Verify against the chunk's `printed_pages` frontmatter — line ~13380 corresponds roughly to printed page 30 in pt1.

2. **Transcribe Latin verbatim from OCR**, NOT from PDF. Preserve Quaracchi's italics and punctuation. Where OCR has obvious garbles (e.g. `QLI.ESTIO` for `QUAESTIO`, `8` for `S`, `1` for `I` inside Roman numerals), silently correct **only** when context makes the intent unambiguous; otherwise mark `[?]`.

3. **Place footnote anchors at OCR positions** — the OCR preserves footnote-marker spacing as `boniis ²`, `decimo  de  Trinitate ³`, etc. Move `[^N]` markers in the chunk Latin to those exact positions, not end-of-clause. The English `[^N]` then mirrors the Latin position.

4. **Translate English literally**. Match the corrected Latin paragraph for paragraph. Use the scholastic-formulae and key-terminology tables further down in this file for consistency.

5. **Apparatus from OCR text directly** — the OCR includes the full Quaracchi apparatus block (typically 20+ footnotes per chunk-page). Pull each entry from raw lines and translate. Do NOT reuse the apparatus block from the existing chunk if you find any divergence — Tier-1 chunks frequently dropped or paraphrased apparatus entries.

6. **PDF (`raw/doctorisseraphic1{1,2}bona.pdf`) is consulted only for**:
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

### What NOT to do (anti-patterns from past sessions)

- ❌ Don't read the PDF and treat your reading as authoritative. The OCR is more accurate.
- ❌ Don't trust the existing chunk's Latin or apparatus. Many were generated by AI translation rather than literal transcription. Diff against OCR.
- ❌ Don't silently leave half-verified chunks. Either complete to Tier 2, or revert to skeleton with the original status string. Never an in-between.
- ❌ Don't skip the ambiguities log. Every `[?]` you write goes in the log.

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

**Don't let formatting drift or `[?]` flags accumulate past 10 distinctions.** After every distinction whose number ends in 0 ships (d.30, d.40, d.50, …), run two locked-in passes before advancing:

1. **`[?]` flag resolution pass — last 10 distinctions only.** Walk every inline `[?]` in the chunks and the per-chunk `manual-review/tier2-ambiguities-d{N}-*.md` logs for the last 10 distinctions. Resolve via 600dpi PDF eyes-on (`pdftoppm -r 600 -f PDF -l PDF -png raw/doctorisseraphic1{1,2}bona.pdf raw/vision/vol1/p-hires-PRINTED-r600`); for each flag, either RESOLVE (with PDF citation) or formally ACCEPT-ILLEGIBLE (with reason). Older distinctions already passed this gate — don't re-do them. Land all dispositions in a single per-decade resolution log: `manual-review/d{N-9}-d{N}-polish-resolution-log.md`.

2. **Style/formatting audit — full corpus every time.** Run a programmatic scan across ALL Tier-2 chunks (d.1 through current) for: required Tier-2 frontmatter fields (`title_la`, `title_en`, `printed_pages`, `pdf_pages`, `source`, `has_apparatus`, `transcription_status`); standard structure (`## Latin`, `## English`, `## Apparatus`); apparatus marker pairing (every `[^N]:` def has matching body anchors in both Latin and English); page-break presence; `transcription_status` starts with `Phase C Tier 2 complete —`; legacy auto-chunked duplicates (e.g. a `d{N}-divisio.md` superseded by `d{N}-p1-divisio.md` + `d{N}-p2-divisio.md`). Fix what's mechanical; flag the rest. The corpus-wide pass keeps formatting drift from compounding silently as new chunks are added — d.27–d.30 caught a `**En.**` 4→5-space indent shift this way, and d.8 caught a vestigial duplicate.

**Both passes are blockers for the next decade of distinctions.** Don't dispatch d.31+ translation agents until the d.21–d.30 polish pass closes; same for d.41+ vs d.31–d.40, etc.

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

- **Quaracchi 1882 Vol. I**: `doctorisseraphic11bona.pdf` in `raw/` (gitignored). PDF page = printed page + 102 for Vol. I pt. 1.
- **Internet Archive**: `doctorisseraphic{VOL}{PART}bona` — Vol I pt 1 is local; other volumes need download.
- **Lombard's Sentences** (for littera chapters): same PDF; Lombard text is printed at the top of each distinction's opening pages.
