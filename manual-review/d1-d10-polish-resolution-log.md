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
