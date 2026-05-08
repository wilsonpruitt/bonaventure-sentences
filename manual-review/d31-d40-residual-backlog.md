# d.31–d.40 Residual Manual-Work Backlog

Extracted 2026-05-07 from `manual-review/d31-d40-polish-resolution-log.md` after Pass A (sessions 1–5) cleared. These items were either accepted-illegible or formally deferred during the polish-blocker. None block d.41+ chunking; all are addressable later as discrete one-off tasks.

Categories:
- **A. Accepted-illegible** — `[?]` glyphs left inline in chunks; would require non-OCR sources or scribal expertise
- **B. Deferred footnote renumber** — out-of-scope for polish; would touch all subsequent indices in both languages
- **C. Audit candidates** — patterns that warrant a corpus-wide regex sweep
- **D. Page-range / structural corrections** — single-chunk frontmatter or apparatus fixes

---

## A. Accepted-illegible (codex sigla + Greek script)

- **d.31 p1-a1-q3 [^7]** — `Cod. [?] hic addit` — siglum illegible in OCR
- **d.31 p2-a1-q3 scholion line 80/134** — `IV. *Sent.* d. 49. p. II. a. 2. q. [?]` — internal cross-ref quaestio number partial
- **d.31 p2-a1-q3 scholion II commentator-list** — 5 sub-flags: `S. Thom., hic q. 2 [?]`; `Petr. a Tar., hic [?]`; `Henr. Gand., [?] 71. q. 4`; `Dionys. Carth., hic q. [?]`; `Biel, hic q. [?]`
- **d.31 p2-a1-q2 [^8] Aristotle Greek excerpt** — `τὸ γὰρ καθ' ὑπερβολὴν…` IA OCR can't read Greek; PDF only reconfirms the visual reading already in the chunk
- **d.31 p2-a2-q3 [^4]** — `codd. aa l. ih [?] *concordia et pax idem*` — codex-list partial sigla
- **d.36 a1-q1 [^3] Aristotle Greek excerpt** — `καὶ γὰρ τὸ χωριστὸν…` same disposition as d.31 p2-a1-q2 [^8]

## B. Deferred footnote renumber

- **d.31 littera [^19] orphan** — body anchor at OCR-noise position; printed Quaracchi has no gloss there. `[^18]` body-anchor missing at correct position (Patripassiani clause). Renumber would touch all later indices.
- **d.31 p1-dubia missing apparatus** — PDF p. 540 fn 7 = `Cod. W adiicit Deo` keyed to `differt a se Deo` in DUB II respondeo; chunk has no apparatus block. Adding requires introducing apparatus + body anchor.
- **d.34 a1-q1 [^7]/[^8] missing body anchors** — printed Quaracchi p. 546 anchors fns 7 and 8 on `praeterea` and `termini`; chunk folds variants into omnibus `[^16]` instead.
- **d.36 a2-q2 missing body anchors for fns 4, 6, 7** — printed p. 624 anchors on body words; chunk's `[^4]/[^6]/[^7]` defs hold different content, mis-mapped.
- **d.38 dubia missing apparatus entry for p. 682 fn 1** — `Vat. cum edd. 3, 5 sub.` keyed to `dictum de¹ conditione`; dropped during chunk-build (likely cascade from p. 680 col-b OCR dropout).

## C. Corpus-wide audit candidates

- **Chunk-build wholesale apparatus block-substitution** — d.33 a1-q4 fns [^13]–[^15] had Latin unrelated to printed p. 580. Pattern: when consecutive footnotes diverge from printed, suspect block-substitution at chunk-build, not isolated OCR garbles.
- **PDF-supplement chunks need diff-check** — d.38 dubia DUB I, d.39 a1-q2 Scholion II, d.40 a4-q2 Respondeo were all wholesale paraphrase fabrications hiding behind "PDF supplement" / "OCR illegible" notes. Grep `transcription_status` for `OCR-dropped`, `PDF supplement`, `supplemented`, `dropped column`, `OCR jump` and diff each against printed Quaracchi at 600 dpi.
- **Body-`[?]...` truncations** — d.36 a1-q2 obj 1 had `tribus[?]...` where printed reads `tribus, patet etc.` Suggests chunker drops closing `patet etc.` / `et sic` clauses. Regex sweep: lines ending `[?]...` or `[?].`
- **Marginal-rubric injection** — d.35 dubia DUB VI had `quia duplici ratione[?]:` where printed has plain `quia actu cognoscit`. Likely conflated marginal rubric. Audit: inline `duplici ratione` / `triplici ratione` body phrases.
- **Column-wrap inline-quote splits** — d.36 a3-q1 [^12] split `per positionem; sed malum` as `per posi-*[tionem]. Sed malum`. Regex: `\*\[[a-z]+\]\.` and similar wrap patterns.
- **Greek-article ASCII garbles** — d.39 a2-q3 had three `tb` instances for `τὸ`. Sweep corpus for `\btb\b` in italics/scholion contexts.
- **`Auctoris` ↔ `viatoris` substitution** — d.39 a1-q2 scholion I had `pro statu Auctoris` for printed `pro statu *viatoris*`. Doctrinally significant. Grep scholion text for `Auctor` mis-readings.
- **Editorial-bracket reconstructions** — d.39 a2-q1 had `[Patet ex praedicta distinctione…]` where printed text is shorter and uses different vocabulary. Smell: editorial brackets in chunk body often mean chunker was guessing without printed access.
- **Split-italic phrase patterns** — d.32 divisio had `*se* [?] *ipso*` where printed has continuous `*se ipso*`. Regex: `\*[a-z]+\*\s*\[?\]\s*\*[a-z]+\*`.
- **Single-word OCR drops at column-bottoms** — d.40 divisio had `praedestinatio secundum [?]` missing `rem`. Recurs throughout corpus.

## D. Single-chunk structural corrections

- **d.33 a1-q4 [^15] col-break continuation** — PDF p. 580 col-a fn 4 ends "alii [...]" with continuation likely wrapping to col-b but not legible in current 600 dpi crop. Re-crop covering col-a→col-b transition would close it.
- **d.32 littera [^11] Hilary `de Trin.` IX quote** — Quaracchi prints quote ending mid-clause; annotated in chunk. Could be extended if a later edition or critical apparatus supplies the rest.
- **d.40 a4-q2 apparatus duplicates [^16]/[^19] and [^17]/[^20]** — identical defs for two pairs. Chunker artifact; cleanup pass.
- **d.40 a2-q1 frontmatter `printed_pages`** — declares [706, 707, 708, 709] but scholion II is actually on p. 710. Audit `printed_pages` on all d.40 chunks; scholion sections routinely under-counted.

---

## Disposition summary across all 5 sessions

| Session | Distinctions | Resolved | Removed | Accepted-illegible | Accepted-doc | Structural anomalies |
|---|---|---|---|---|---|---|
| 1 | d.31, d.32 | 31 | 0 | 13 | 8 | 3 |
| 2 | d.33, d.34 | 24 pairs | 1 pair | 0 | 1 pair | 4 |
| 3 | d.35, d.36 | 26 pairs | 0 | 1 pair (Greek) | 0 | 4 |
| 4 | d.37, d.38 | 5 pairs | 0 | 0 | 0 | 3 |
| 5 | d.39, d.40 | 43 (all 78 glyphs) | 0 | 0 | 0 | 11 |
| **Total** | **d.31–d.40** | **~129 dispositions** | **1** | **6 unique flags** | **9** | **25** |

Pass A polish-blocker CLEARED 2026-05-07. d.41+ chunking unblocked. This backlog is non-blocking; addressable as discrete tasks when convenient.
