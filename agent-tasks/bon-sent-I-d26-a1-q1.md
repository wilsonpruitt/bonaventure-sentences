# Agent Task: bon-sent-I-d26-a1-q1 — full Tier-2 promotion

**Output**: rewrite `vol1/bon-sent-I-d26-a1-q1.md` to full Tier-2 standard, matching the structure of recent reference chunks (e.g. `vol1/bon-sent-I-d24-a1-q1.md`, `vol1/bon-sent-I-d25-*.md`). Backup already exists at `vol1/_backup-d26-a1-q1-pre-rebuild-20260504/`.

## Source coordinates

- **Raw OCR**: `raw/bonaventure_vol1_pt2_raw.txt`, lines **3298–3699**
- **Printed pages**: 451–454 (Quaracchi 1882, vol I)
- **PDF pages** (pt2 PDF, `raw/doctorisseraphic12bona.pdf`): printed − 410 → **41–44**
- **Word count** (Latin): ~4,151

## Structure of the chunk

1. `QUAESTIO I.` header at raw line 3298
2. Title: `Utrum in divinis ponendae sint proprietates personarum.`
3. Pro-arguments **1–7** (raw ~3298–3340, 2-column interleaved)
4. `Contra:` with arguments **1–4** (the "Ad opposi-" sidebar marker indicates 4)
5. `CONCLUSIO.` blockquote
6. `Respondeo:` body — three sub-conclusiones, marked in marginalia as *Conclusio 1 (positive)*, *De modo positionis*, *Conclusio 2*
7. `Ad illud quod obiicitur` solutiones — replies to objections **1–6** (covering Hilarius, Damascenus, summa simplicitas, essential properties, essence-self-refers, creature-self-refers); the final reply on `creatura se ipsa refertur` extends across the bottom of p. 453 and top of p. 454
8. `SCHOLION` — **four sections (I, II, III, IV)** spanning raw ~3550–3699; section IV is the bibliography listing parallel loci (Alex. Hal., Scotus, S. Thom., B. Albert., Petr. a Tar., Richard. a Med., Aegid. R., Henr. Gand., Dionys. Carth.)
9. `Apparatus`: ~15 footnote entries gathered from page-foot blocks across pp. 451, 452, 453, 454 (each printed page contributes its own footer block)

## OCR challenges (read this carefully)

The pt2 OCR is severely **two-column interleaved** on these pages — column A and column B are jammed onto single OCR lines with whitespace gaps. Reflow rule: **read left-half-of-line A, then right-half-of-line A**, sequentially down the page. Many lines are split mid-word across the column gap. Examples from this chunk:

```
"Quod autem in divinis     sit  ponere proprietates    realiter.   Sed tam generatio,
                                                                              quam spiratio est in una"
```
→ Column A: `Quod autem in divinis sit ponere proprietates`
→ Column B: `realiter. Sed tam generatio, quam spiratio est in una`

When reflowing, the marginalia tags like `Fundamenta.`, `Ad opposi-tum.`, `Conclusio 1.`, `De modo po-sitionis.`, `Conclusio 2.`, `tres modi dicendi.`, `Solutio op-positorum.`, `Improbatur.` are **editorial side-glosses** — strip them out, do not insert them into running text.

PDF crops (`tools/extract-pages.py --volume vol1 --pages 41-44 --dpi 400`) may help on garbles. **Always cross-check footnote anchor positions against the OCR-marker spacing** (the OCR preserves `Hieronymus dicit, et habetur in fine prae-` … `cedentis distinctionis ¹` style markers).

## Known textual fixes (applied silently — these are unambiguous)

- `reabler` → `realiter`
- `oportel` → `oportet`
- `Iwc` → `hoc`
- `nascil3ilitatem` → `nascibilitatem`
- `del^et` → `debet`
- `«sset` → `esset`
- `FiUus` → `Filius`
- `q^dd` → `quid`
- `proprietaUs` → `proprietates`
- `fme` → `fine`
- `etiara` → `etiam`
- `coniugaUs` / `coniugatis` → `coniugatis`
- `sanctuni` → `sanctum`
- `oranimodam` → `omnimodam`
- `oranis` → `omnis`
- `magis dilTerentiae` (scholion) → `magis differentiae`
- `aitributionis` / `atlributionis` (scholion) → `attributionis`
- `senlentiae` → `sententiae`

Flag with `[?]` and log to `manual-review/tier2-ambiguities-d26-a1-q1.md` ONLY genuine ambiguities (e.g. variant readings the apparatus itself flags, where context cannot resolve).

## Tier-2 deliverables (all required — chunk is NOT Tier-2 without all of these)

1. **YAML frontmatter** — preserve `id`, `volume`, `book`, `distinctio`, `articulus`, `quaestio`, `type`, update:
   - `title_la: "Utrum in divinis ponendae sint proprietates personarum."`
   - `title_en: "Whether properties of the persons are to be posited in divine matters"`
   - `printed_pages: [451, 452, 453, 454]`
   - `pdf_pages: [41, 42, 43, 44]`
   - `source: "S. Bonaventurae, Opera Omnia, Tomus I (Quaracchi, 1882), pp. 451–454"`
   - `has_apparatus: true`
   - `has_scholion: true`
   - `transcription_status: "Phase C Tier 2 complete — Latin re-set verbatim from IA djvu OCR pt2 (raw lines 3298–3699), fresh literal English translation, full apparatus from raw OCR (N entries) gathered across pp. 451–454 footers, scholion (I–IV) translated literally from OCR (2026-05-04)"`
   - `format_version: 1`

2. **Latin body** (under `## Latin`) — verbatim from OCR, deinterleaved, with:
   - `<!-- page 451 -->`, `<!-- page 452 -->`, etc. comments at page boundaries
   - `### QUAESTIO I. *Utrum in divinis ponendae sint proprietates personarum.*`
   - Numbered objections 1–7
   - `**Contra:**` block with numbered counter-arguments
   - `### Conclusio` heading then `> ` blockquote with the conclusio Latin
   - `**Respondeo:**` block
   - `**Ad argumenta:**` (or use `*Ad 1.*`, `*Ad 2.*` etc. for individual replies)
   - `### Scholion` then `**I.** ... **II.** ... **III.** ... **IV.** ...`
   - `[^N]` markers placed at OCR-marker positions in running text

3. **English body** (under `## English`) — paragraph-for-paragraph parallel, literal not paraphrase. Use the scholastic-formula and key-terminology tables from in-repo `CLAUDE.md`. Mirror `[^N]` positions exactly. Mirror page-break comments.

4. **Apparatus** (under `## Apparatus`) — each entry as:
   ```
   [^N]: **La.** <Latin verbatim from OCR footer>

       **En.** <Literal English translation>
   ```
   - Blank line between `**La.**` and `**En.**`
   - 4-space indent on `**En.**` line (markdown list-continuation)
   - Period in `**La.**` is required for the parser
   - Renumber consecutively across all four page footers (1–N)
   - Translate `Vat. cum cod. cc legit...` style apparatus entries fully into English ("The Vatican edition, with codex cc, reads...")

5. **Scripture & cross-refs**: preserve Vulgate numbering in Latin; in English use modern referencing only if the Latin specifies it.

6. **Ambiguities log** — write any `[?]` flags to `manual-review/tier2-ambiguities-d26-a1-q1.md` (create the file). Format:
   ```markdown
   # d.26 a1 q1 — Tier-2 ambiguities
   - **Location**: brief description of issue. OCR rendered X. Best read: Y.
   ```

7. **Smoke test**: after writing, run `cd site && node scripts/build-content.mjs` and confirm:
   - exit code 0
   - chunk parses cleanly (no apparatus parser errors)
   - chunk count remains 436 (unchanged from current state)

## Workflow order (lock to this — do not improvise)

1. Read raw OCR lines 3298–3699 from `raw/bonaventure_vol1_pt2_raw.txt`
2. Reconstruct Latin body by deinterleaving columns A/B
3. Identify `[^N]` anchor positions from OCR-marker spacing
4. Write Latin body (steps 2+3 → file)
5. Translate English literally, paragraph-for-paragraph
6. Translate scholion sections I–IV literally
7. Extract apparatus entries from each printed-page footer block (search OCR for the band of small-text footnotes after each main page block)
8. Translate apparatus literally; assemble into renumbered list
9. Update YAML frontmatter
10. Write ambiguities log
11. Run build smoke test, confirm clean

## Anti-patterns (DO NOT do these)

- ❌ Paraphrase scholion or apparatus — Tier-2 requires literal
- ❌ Skip apparatus entries because "this one is just a manuscript variant" — translate all
- ❌ Insert marginalia tags (`Fundamenta.`, `Conclusio 1.`, etc.) into the running text body — those are editorial side-glosses
- ❌ Read PDF as authoritative over OCR — OCR is more accurate; PDF only for fn-anchor positions and scholion openings
- ❌ Trust the existing chunk file's content — it's auto-chunked Latin only, no English yet, no proper structure
- ❌ Silently guess at unclear words — flag `[?]` and log

## On completion

Report:
- Word counts (Latin + English)
- Apparatus entry count
- Scholion section count
- Any `[?]` flags written and where
- Build smoke test result
- One-line summary suitable for commit message
