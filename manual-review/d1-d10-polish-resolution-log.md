# d.1–d.10 Polish-Blocker Resolution Log

Pass start: **2026-05-10**. PDF source: `raw/doctorisseraphic11bona.pdf` (pt1, Vol I), all crops at 600 dpi.
Pt1 PDF offset: `pdf_page = printed_page + 102`.

This log records the resolution of `[?]` flags surfaced by the d.1–d.10 rechunk pipeline (16-wave campaign closing 2026-05-10), grouped by chunk. Bucket 1 (per `next-session-resume.md`) targets ~250 inline `[?]` flags + 9 OCR-band footer dropouts.

## d6-a1-q3 (p.130)

- **Source**: `raw/vision/vol1/p-130.png` (300 dpi extract; PDF re-renders at the same effective resolution at 600 dpi via pdftoppm — image is fully legible).
- **Footer band on p.130 was elided in IA djvu OCR** for this page; the chunk previously held 7 placeholder `[?]` apparatus entries (`[^13]`–`[^19]`) referring to PDF p. 130.
- **Recovered 7 verbatim Quaracchi footer entries** by eyes-on read of the 600 dpi PDF page and mapped to body anchors as follows:

| Footer # (PDF) | Body anchor | Lemma / disposition |
|---|---|---|
| 1 | `[^13]` | "Cap. 10. n. 11: *Ars quaedam omnipotentis…*" — Augustine *de Trin.* VI, c. 10, n. 11; with adjacent Thomas *de Ver.* q. 3 a. 1 cross-reference. RESOLVED. |
| 2 | `[^14]` | "Vat. praeter fidem mss. … *ille modus producendi*" — variant note. RESOLVED. |
| 3 | `[^15]` | "Vat. *respondendum* …" — variant note. RESOLVED. |
| 4 | `[^16]` | "Supple cum codd. IZ *Filius* …" — composite variant note covering the paragraph from `quia dicunt, quod` through `imaginis`. RESOLVED. |
| 5 | `[^17]` | "Adiecimus … *in quaestione* … Iste locus invenitur in Summa dicti auctoris …" — long Altissiodorensis (William of Auxerre) *Summa aurea* citation, with verbatim Florentine Laurentian codex passage. RESOLVED. |
| 6 | `[^18]` | "Vat. cum cod. cc *quia* …" — variant note. RESOLVED. |
| 7 | `[^19]` | "Dist. 27. p. II. praecipue q. 3." — confirms the *infra* reference to d. 27 p. II q. 3 (not the previously-guessed "probably d. 27"). RESOLVED. |

### Footer note 8 on p.130 — NOT anchored in this chunk

The PDF p.130 footer band has 8 numbered notes; entries 1–7 map cleanly to body markers `[^13]`–`[^19]` of d6-a1-q3. **Footer #8** ("Multi codd. ut DFKSTVW etc. cum sex primis edd. *insufficiens* … divisio in *responsione Augustini* (ad bimembrem quaestionem Orosii: *Voluntate genuit vel necessitate*) …") concerns a textual variant in **DUB. I** (DUBIA CIRCA LITTERAM MAGISTRI), which begins on p.130 directly under q.3's scholion. That belongs to the `d6-dubia` chunk, not this one. **Per task scope ("don't touch any other chunk file")**, footer #8 is documented here for the next pass over `d6-dubia` but not anchored. ACCEPT-OUT-OF-SCOPE.

### `[?]` resolution count

- 7 `[?]` flags resolved (all 7 in apparatus `[^13]`–`[^19]`).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d6-a1-q3.md` after this pass.

### Verification

- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d6-a1-q3.md | sort | uniq -c` → each `[^N]` (N=1..19) appears exactly 3× (Latin body + English body + apparatus def).
- All three guard-rail audits scoped to d.6 run clean (see audit run below in this log).
- `cd site && node scripts/build-content.mjs` parses cleanly.

## d5-a2-q2 (pp. 118–119)

- **Source**: `raw/vision/vol1/p-118.png` and `raw/vision/vol1/p-119.png` (re-extracted at 600 dpi).
- **Footer band on p.119 was elided in IA djvu OCR** for raw lines 26901-26997; chunk previously held 6 placeholder `[?]` apparatus entries (`[^8]`–`[^13]`).
- **Frontmatter correction**: chunk's `printed_pages` was `[117, 118]` but actually spans `[118, 119]` — Q.II begins on p.118 (right after the q.I SCHOLION) and ends mid-p.119 (before DUBIA CIRCA LITTERAM MAGISTRI). Updated frontmatter and the `<!-- page N -->` markers; moved page-119 break to its actual location (between *plurium,* and *sic natura...* — the page-118 right-column ends "…per propagationem⁷ plu-" and p.119 starts "rium, sic natura…").
- **Body anchor correction**: `[^8]` was placed at a spurious "[?]" word after *plurium* (an OCR artefact); the actual Quaracchi `¹` on p.119 is anchored at "haec autem est generatio¹" (end of Respondeo). Repositioned `[^8]` to *generatio* in both Latin and English bodies. Removed the stray inline `[?]` glyphs that the OCR had inserted before each of `[^9]`–`[^13]`.
- **Recovered 6 verbatim Quaracchi footer entries** by eyes-on read of p.119:

| Footer # (p.119) | Body anchor | Lemma / disposition |
|---|---|---|
| 1 | `[^8]` | "Cod. O addit *et processio*." — anchor moved to *generatio* (end of Respondeo). RESOLVED. |
| 2 | `[^9]` | "Ex antiquioribus mss. adiecimus *etiam*…" — anchored at *naturam* (Reply 1). RESOLVED. |
| 3 | `[^10]` | "Hic a. 4. q. 4. ad 2." — internal cross-reference, anchored at *ostensum est* (Reply 2). RESOLVED (confirms the prior "likely cross-reference" guess was approximately right but Quaracchi cites a. 4. q. 4. ad 2., not d. 4. q. 4). |
| 4 | `[^11]` | "Vat. *dividitur*, sed absque auctoritate…" — variant note, anchored at *distinguitur* (Reply 2 second part). RESOLVED. |
| 5 | `[^12]` | "Ita multi codd. ut C L O S V W X Y…" — long variant note, anchored at *communem* (Reply 3). RESOLVED. |
| 6 | `[^13]` | "Mendum Vat. *ratio* pro *datio* ex mss. correximus…" — Quaracchi correction note, anchored at *datio* (Reply 4). RESOLVED. |

### Footer note 7 on p.119 — NOT anchored in this chunk

p.119 footer has 7 numbered notes; entries 1–6 map to this chunk. **Footer #7** ("Vat. cum cod. cc *cum universale ponitur*, sed minus bene…") anchors at *ponatur*⁷ in DUB. I (DUBIA CIRCA LITTERAM MAGISTRI) which begins lower on p.119. Belongs to a separate dubia chunk. ACCEPT-OUT-OF-SCOPE.

### `[?]` resolution count

- 6 `[?]` flags resolved (all 6 in apparatus `[^8]`–`[^13]`).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d5-a2-q2.md` after this pass.

### Verification

- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d5-a2-q2.md | sort | uniq -c` → each `[^N]` (N=1..13) appears exactly 3× (Latin body + English body + apparatus def).
- All three guard-rail audits scoped to d.5 run clean (see audit run below in this log).
- `cd site && node scripts/build-content.mjs` parses cleanly.

## d1-a3-q2 (p.42)

Bucket 1 PDF-recovery pass — IA djvu OCR for printed page 42 elided the entire footer band, leaving 3 inline `[?]` flags in the chunk body without matching apparatus entries. Reconciled against 600dpi PDF (`raw/vision/vol1/p-042.png` + 600dpi `pdftoppm -f 144 -l 144` extraction of `raw/doctorisseraphic11bona.pdf`). Footer band on p.42 main column carries notes 1–4; notes 1–3 belong to this chunk's body, note 4 is the opener of the d.2 *Dubia circa litteram Magistri* (Lib. I de Sacram. p. 8. c. 12.) on the right column — out of scope.

| Body anchor | Disposition | Footer source |
|---|---|---|
| `Huiusmodi enim [?]` | RESOLVED → `[^25]` | p.42 footer note 1: *Subaudi cum cod. R virtutes. Mox plures antiquiores codd. ut ACFGKLORSUYZ ee post pulcritudinem loco qua habent quia.* |
| `superbae sunt et inflatae [?]` | RESOLVED → `[^26]` | p.42 footer note 2: *August., XIX. de Civ. Dei, c. 25: Virtutes, cum ad se ipsas referuntur nec propter aliud expetuntur, etiam tunc inflatae ac superbae sunt.* |
| `anima ipsam [?] diligit` | RESOLVED → `[^27]` | p.42 footer note 3: *Lapsum librariorum Vat. ponentium ipsa pro ipsam correximus ope mss. et ed. 1.* |

### Verification

- Before: 24 apparatus entries, 3 unresolved `[?]` body flags, 0 footer entries from p.42.
- After: 27 apparatus entries (24 unchanged + 3 new from p.42), 0 unresolved `[?]` body flags. (One `[?]` remains in `[^15]` English on a translator-side editorial guess about the bracketed Vatican lemma — out of Bucket 1 scope, p.41 not p.42.)
- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d1-a3-q2.md | sort -t^ -k2 -n | uniq -c` → each `[^N]` (N=1..27) appears exactly 3×.
- d.1-scoped audits (paraphrase, headers, apparatus-count) re-run; build-content.mjs parses cleanly.


## d3-littera (p.66)

Bucket 1 PDF recovery against `raw/vision/vol1/p-066.png` (600dpi from `doctorisseraphic11bona.pdf` PDF p.168). The IA djvu OCR for p.66 elided the entire footer band; the chunk had skeleton placeholders for footer notes 43–45 with `[?]` flags. Recovery also addressed older `[?]` flags from p.62, p.63, and p.65.

**Resolutions (per [?] flag):**

- **`vol1/bon-sent-I-d3-littera.md` line 86 (Latin), `in anima[?] substantialiter`** — RESOLVED. PDF p.65 right column shows plainly "in anima substantialiter existunt" with no marker between *anima* and *substantialiter*. The `[?]` was an OCR-suspicion flag, not a real ambiguity. Removed.
- **line 165 (English mirror)** — RESOLVED. Same as above; `[?]` removed.
- **`[^2]` La/En `Codd. CDE et[?] (OCR truncated)`** — RESOLVED. PDF p.62 left-column footer shows body footnote 2 begins directly with "Praeter fidem mss. et ed. 1, ..." — the leading "Codd. CDE et" was leakage from the *separate* `NOTAE AD LIBR. SENTENTIARUM` apparatus band (note 2 of which truncates at the page-bottom edge as "² Codd. C D E *et.*"). Stripped the spurious prefix from `[^2]`; corpus-wide `NOTAE AD LIBR.` entries are not part of d3-littera (they belong with COMMENTARIUS chunks). Also corrected obvious OCR `emananlis` → `emanantis` already done.
- **`[^8]` La/En `omisso[?]`** — RESOLVED. PDF p.63 left-column footnote 1 reads: "Cod. A omittit *exiguum*; Codd. B C D E et ed. 1, omisso *vestigium* et transpositis verbis, satis bene legunt *Trinitatis indicium vel exiguum*, accepto *vel* pro *saltem* vel pro *etiam*." Filled in `vestigium`.
- **`[^43]` La/En** — RESOLVED. PDF p.66 left-column footnote 1: "Cap. 1, n. 1." (Augustine *de Trin.* lib. IX cap. 1 n. 1, anchor on "in libro nono *de Trinitate*").
- **`[^44]` La/En** — RESOLVED. PDF p.66 left-column footnote 2 (very long): "Cap. 1, n. 4. — Auctor huius libri, S. Fulgentius, multo fusius de his tractat, in quo textu codd. CDE addendo *non* et mutando *sed in si* sic legunt: *Rursus quidem Trinitas non esset vera...* Sed haec lectio duplicem suppositionem et argumentationem confundit. In fine textus Vat. *fuissent quoque naturae* pro *fuissent naturarum quoque*." Anchor on "*de Fide ad Petrum*".
- **`[^45]` La/En** — RESOLVED. PDF p.66 left-column footnote 3: "Loc. cit.; auctoritas sequens ibid. n. 6." Anchor on "praedicat esse Trinitatem".
- **NEW `[^46]` La/En** — RESOLVED. PDF p.66 left-column footnote 4: "Cap. 1. n. 1." This is a Quaracchi note that the previous chunk version had treated as un-anchored; the closing "Augustinus in primo libro *de Trinitate*: «Nulla res est, quae se ipsam gignat, ut sit»." is in fact footnoted in the Quaracchi text. Inserted `[^46]` body anchor in both Latin and English at "in primo libro *de Trinitate*[^46]:".

**Counts:**
- Before: 45 apparatus entries (3 placeholder, 4 with `[?]`); 5 `[?]` flags total (2 body, 2 in [^2]/[^8] La+En, 6 in [^43]-[^45] La+En).
- After: 46 apparatus entries (all substantive); 0 `[?]` flags.
- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d3-littera.md | sort -t^ -k2 -n | uniq -c` → each `[^N]` (N=1..46) should appear exactly 3×.

**Right-column footer notes on p.66 (NOT in this chunk):** the right-column has `NOTAE AD COMMENTARIUM 1` plus right-column body footer notes 2, 3, 4. These belong to the d.3 COMMENTARIUM chunk (separate file), not to d3-littera. Out of Bucket-1 scope for this file.

**Audits:** d.3-scoped paraphrase/headers/apparatus-count re-run after edits. `cd site && node scripts/build-content.mjs` parses cleanly.

## d7-divisio (p.134)

Source: PDF page 236 = printed p.134, 600dpi crops at /tmp/p134-r600-236.png (left-col body crops + bottom footer-band crop).

The chunk's 8 apparatus entries match the 8 footer notes on p.134 verbatim (notes 9-10 in the IA OCR footer block belong to the QUAESTIO I body that begins on p.134 column 2 / continues to p.135 — correctly NOT included in the divisio chunk).

Anchor decisions (verified eyes-on vs PDF):
- `[^1]` after `exponens ipsam` — KEEP. PDF: `exponens ipsam ¹, ibi: Quomodo ergo`.
- `[^2]` after `Haec est` — KEEP. PDF: `Haec est ² secunda pars`.
- `[^3]` after `Et` — KEEP. PDF: `Et ³ ad hanc quaestionem`.
- `[^4]` after `intelligatur` (second occurrence, "Si vero intelligatur") — KEEP. PDF: `Si vero intelligatur ⁴ passive`.
- `[^5]` after `Si` (in "Si in activa") — KEEP. PDF: `Si ⁵ in activa, hoc potest esse`.
- `[^6]` after `generat` (in "aliquis generat") — KEEP. PDF: `aliquis generat ⁶, tamen hunc sensum`.
- `[^7]` after `Filio` (in "communicet Filio") — KEEP. PDF: `communicet Filio ⁷ potentiam`.
- `[^8]` after `univocum` — KEEP. PDF: `posse univocum ⁸`.

[?] flags resolved:
- Body `[potentia][?]` (Latin) and `[the power][?]` (English) in "in secunda, utrum [potentia] generandi sit in Filio" — RESOLVED to `potentia` / `the power` (no brackets, no [?]). PDF p.134 left column line ~10 shows `utrum potentia generandi sit in / Filio` clearly and unambiguously; the IA OCR dropped the word at a column-line break.
- Footnote 5 trailing `[?]` after `gerundivum.` (both La and En) — RESOLVED (removed). PDF footer band shows the entry ending cleanly at `gerundivum.` with no further text. The trailing `[?]` was a precautionary marker from the from-scratch pipeline that visual inspection rejects.

[?] flags retained: none.

Net: 0 anchor moves, 0 entry rewrites, 2 [?] flag resolutions, transcription_status updated.
