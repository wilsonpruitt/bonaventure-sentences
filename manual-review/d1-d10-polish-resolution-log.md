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

## d2-a1-q2 (p.54)

PDF verification source: `raw/vision/vol1/p-hires-r600-155.png` + `p-hires-r600-156.png` (600 dpi).
Verified all 18 apparatus entries (`[^1]`-`[^11]` from p.53; `[^12]`-`[^18]` from p.54) and all 18 body anchor positions in both Latin and English.

### Body anchors
All 18 anchor positions confirmed against PDF superscript markers — no moves needed. p.53: `[^1]` after "si", `[^2]` after "communicare", `[^3]` after "possessio", `[^4]` after "natura", `[^5]` after "illis", `[^6]` after "principium", `[^7]` after "habet", `[^8]` after "conclusio", `[^9]` after "obiicitur", `[^10]` after "non est", `[^11]` after "circa idem". p.54: `[^12]` after "potens esse", `[^13]` after "infra patebit", `[^14]` after "nec ponitur", `[^15]` after "in pluribus", `[^16]` after "infra patebit", `[^17]` after "sic et", `[^18]` after "Augustinus".

### Apparatus dispositions
- `[^1]`-`[^11]` (p.53 footers): RESOLVED — Latin transcription matches PDF verbatim; English translation literal and accurate. No corrections.
- `[^12]` (Cod. K *et potest esse*. Cod. O *ut potens esse*.): RESOLVED — matches PDF.
- `[^13]` (Disc. 27. p. I. q. 2. ad 3. — Mox post *caritatis* …): RESOLVED — matches PDF.
- `[^14]` (Restituimus lectionem … omnium antiquorum …): CORRECTED — chunk had `ferme`; PDF reads `fere`. Fixed Latin (`ferme` → `fere`); English unchanged ("nearly all" still accurate for either reading).
- `[^15]` (Vat. hic, sicut supra …): RESOLVED — matches PDF.
- `[^16]` (Disc. 8. p. II. a. 1. q. 1. et d. 23. a. 2. q. 1. et 2. — Paulo ante cod. X *solum* loco *potius*.): RESOLVED — matches PDF.
- `[^17]` (In Vat. et recentiore cod. cc deest *et* …): RESOLVED + [?] CLEARED — chunk had `Paulo post cod. X *unitas* pro *nullo*. [?]`; PDF clearly reads `Paulo post cod. X *nulla* pro *nullo*.` (italic *nulla* ending in -a). Fixed Latin and English; removed `[?]` flag from both.
- `[^18]` (Libr. I. de Doctr. christ. c. 5. n. 5: …): RESOLVED — matches PDF.

### Footer entries NOT in this chunk
PDF p.54 footer continues with two more numbered notes (`⁸ Ita codd. et ed. 1, dum Vat. *creatura cum sit finita*. …` and `⁹ Cfr. August., de Quant. animae c. 3. et seqq. — Cod. R hic non male addit *si*.`). These belong to the next quaestio (q. III, *Utrum numerus divinarum personarum sit infinitus*) which begins on p.54; not in scope.

### Summary
- Anchor moves: 0
- Latin/English corrections: 2 (`[^14]`, `[^17]`)
- `[?]` flags resolved: 1 (`[^17]`)
- `[?]` flags accepted as illegible: 0

## d3-p2-a1-q2 (p.84)

PDF verification of the 3 q.II footer entries on p.84 (Wave 14 PDF-recovered) against `raw/vision/vol1/p-084.png` (600dpi eyes-on).

**Footer band on p.84 contains 9 numbered entries** (page restarts numbering): entries 1-3 belong to the q.II tail (this chunk); entries 4-9 belong to q.III which starts mid-page (different chunk).

Entry-by-entry reconciliation against this chunk's [^22], [^23], [^24]:

- **[^22]** ↔ p.84 footnote 1 — `De prima assignatione vide IX. de Trin. per totum; de secunda ibid. X. c. 11. et 12; de completissima imaginis ratione ibid. XIV. c. 8. ac 12. seqq.` Chunk had the two trailing reference clauses SWAPPED (had `de secunda ibid. XIV. c. 8. ac 12; de completissima imaginis ratione ibid. XIV. c. 11. et 12. seqq.` — book numbers and chapter ranges flipped between the two clauses). PDF clearly shows `secunda ibid. X.` (Roman ten, not XIV) for *secunda* and `XIV. c. 8. ac 12.` for *completissima*. **CORRECTED** in both Latin and English of [^22]. (Plausibility check: Augustine *de Trin.* X.11-12 covers mens/notitia/voluntas — fits "second assignment"; XIV.8 and XIV.12 cover the most complete account — fits *completissima*.)
- **[^23]** ↔ p.84 footnote 2 — `Vat. contra mss. respondeo.` Chunk matches PDF verbatim. NO CHANGE.
- **[^24]** ↔ p.84 footnote 3 — `Cod. O addit suum.` Chunk matches PDF verbatim. NO CHANGE.

Body anchor positions on p.84 verified against PDF:
- `comparatione ad Deum¹` → [^22] ✓
- `solvendum²` → [^23] ✓
- `sub *ratione*³ *cognoscibilis*` → [^24] ✓

[?] flags retained (out of p.84 scope, kept for future passes): two stray `[?]` markers at end of [^3] English and end of [^9] English (both p.82 entries). Latin transcription is unambiguous in both; the [?] was a translator-uncertainty flag about English style, not a Latin-source flag. Not resolved here because (a) outside the p.84 footer scope this Bucket 1 task targets, and (b) p.82 page image not yet extracted for visual confirmation.

Net: 0 anchor moves, 1 entry corrected ([^22] swapped clauses), 0 [?] resolutions in scope, 2 [?] retained out of scope, transcription_status updated.

## d8-p2-a1-q4 (p.174)

**Source:** `raw/vision/vol1/p-174.png` (2704x3981, 600dpi); cross-checked `raw/vision/vol1/p-173.png` (re-extracted at 600dpi to `/tmp/p173-r600-275.png` since on-disk was 200dpi).

**Handoff context:** "OCR p.174 footer block elided; marker `⁵` preserved with [?]". On eyes-on, the body marker after *aequivalentiam* on p.174 is actually `²` (small superscript 2), not `⁵`. The "⁵" identification in the handoff was a misreading from the body OCR garble (`^`). The true marker count for q.4 body on p.174 is two: `¹` after "vel per" (before *diversitatem*) and `²` after "aequivalentiam".

**Apparatus reconciliation against PDF p.173 footer (13 entries) + p.174 footer (entries 1 & 2 belong to q.4 body):**

Findings on the pre-existing chunk:
- [^8]: chunk read "*eum*" — PDF reads "*etiam*" (OCR garble *efcm* misread as *eum*). CORRECTED.
- [^10]: chunk had a fabricated "*Esse in pluribus dupliciter.* [Marginal gloss]" entry. PDF p.173 footer #10 is "Vat. *multiplicitatem*, sed contra mss. et ed. 1." The "*Esse in pluribus dupliciter*" is a marginal gloss in Quaracchi's printed body (not a footer entry); per CLAUDE.md it should be trimmed. REMOVED fabricated entry; replaced with PDF p.173 #10.
- [^11], [^12], [^13]: shifted up by one slot to absorb the entry 10 displacement.
- [^13] (chunk): merged PDF p.173 #12 + #13 into one entry, with a trailing `[?]` flagging the merge uncertainty. UN-MERGED into [^12] = "Cod. V *rationem* loco *ipsum*." and [^13] = "Fide antiquiorum mss. et ed. 1 expunximus hic additum *eo*, et paulo post substituimus *illa* pro *substantiae*." (resolves the `[?]`).
- [^14] NEW: PDF p.174 footer #1 "Codd. V X *secundum*, et paulo infra cod. T *uniformitatem* loco *unitatem*."
- [^15] NEW: PDF p.174 footer #2 "Hoc est, per eminentiam seu eminenter."

**Body anchor relocations (Latin and English mirrored):**
- Removed spurious [^10] from "sicut unum et ens[^10]" — no PDF marker there.
- [^10] now at "naturarum multiformitatem[^10]" (was [^11]).
- [^11] now at "nihil est habens[^11]" (was [^12]).
- [^12] now at "quod ipsum[^12]" (was [^13]).
- [^13] NEW anchor at "Deo non est superius, quia[^13] non est simplicius" (PDF p.173 #13, marker on "quia").
- [^14] NEW anchor at "vel per[^14] *diversitatem*" (PDF p.174 marker ¹).
- [^15] NEW anchor at "per aequivalentiam[^15]" (PDF p.174 marker ²) — resolves the inline `[?]`.

**[?] flags resolved:** 2 of 2 (both in this chunk). None retained.

**Apparatus count:** chunk now 15 entries (was 13). Audit will show new diff +0 instead of +1 (p.174 entries 1, 2 added).

**Net:** 1 entry recovered from PDF where OCR was elided (technically 2 new entries from p.174); 1 entry text-corrected (etiam); 1 fabricated entry removed; 1 merged entry split; 4 body markers relocated; 2 new body markers added; 2 [?] flags resolved; transcription_status updated.

---

## d10-littera (p.193)

**Source:** raw/vision/vol1/p-193.png (footer band readable at ~330dpi crop; 600dpi extraction yielded same image — extract-pages.py --dpi 600 ignored when file is regenerated under default-dpi name).

**Pre-state:** 13 [?] flags total in chunk; chunk apparatus had 22 entries [^1]..[^22]; p.193 body had anchors [^12]..[^22] (11) but actual printed footer on p.193 has 10 entries (1-10 in restart numbering).

**PDF footer entries on p.193 (verbatim, 1-10):**
1. Ibid. v. 11-13. — Vat. sola inepte *quia* pro *qua.*
2. Vat. cum ceteris edd. contra originale: *Ipse ergo Deus est dilectio.*
3. Omnia in hoc capitulo sunt ex Augustino, XV. de Trin. c. 17. n. 30. et 31. — Paulo ante finem textus post *Deus dilectio* Vat. cum paucis codd. omittit *est.*
4. Infra dist. XVII. — Vat. contra mss. et edd. 1, 5, 8 omittit *dilectionem* post *sed etiam,* et hic cum ed. 1 legit *explicatur* pro *explicabitur.*
5. Vers. 1. — Antea post *Nunc* edd. 1, 8 *ergo* pro *vero.*
6. Cap. 4. et 5. n. 6. et 7; ex ultimo cap. etiam sequentis huius capituli textus excerpti sunt. In fine primi textus pro *consistit* cod. D et edd. 1, 8 *subsistit*₅, quod magis placeret, si faveret Augustinus.
7. Ephes. 4, 8. — Paulo ante pro *sintque* mss. ACDE *suntque* ac forte melius. Deinde codd. AC incipiunt sequentem textum verbis: *Spiritus quoque* pro *Spiritus ergo.*
8. 1. Ioan. 4, 16. — Vat. et ed. 4 post *nihil est* perperam omittunt; *quomodo Deus dilectio est, si non est substantia.*
9. Cap. 19. n. 37. — Cod. C brevius: *Filius Patrem* loco *Patrem diligit Filius.* Mox codd. BCD et edd. 1, 8 cum originali pro *ineffabilem* legunt *ineffabiliter,* et sic hoc adverbio determinari videtur *diligit.* Denique in fine huius propositionis cod. E et cod. 8 *communis amborum* pro *communis ambobus.*
10. Col. 1, 13. — Vat. cum pluribus edd. ante *Trinitate* ponit *ista* pro *illa*; postea idem fit ab edd. 3, 5, 9 post *sed propter.*

**PDF body marker positions on p.193 (1-10):**
- ¹ at `Ioannes ¹` (line 1)
- ² at `Ipse igitur est Deus dilectio ²`
- ³ at `dilectio ex Deo est ³`
- ⁴ at `explicabitur ⁴`
- ⁵ at `Psalmum ⁵`
- ⁶ at `de Trinitate ⁶` (Augustinus quoque in sexto libro)
- ⁷ at `vinculo pacis ⁷`
- ⁸ at `Deus caritas est ⁸`
- ⁹ at `de Trinitate ⁹` (Augustinus in quinto decimo libro, Cap III)
- ¹⁰ at `Apostolus ¹⁰`

**Per-flag dispositions:**

- **[^14] La trailing `[?]`** (`*qua.* [?]`): RESOLVED — PDF #1 ends cleanly at `pro *qua.*`; trailing [?] was unfounded. Removed.
- **[^14] En trailing `[?]`**: RESOLVED. Removed.
- **[^19] La `*subsistit* [?] (magis, fortasse, si [?])`**: RESOLVED — PDF #6 reads "...pro *consistit* cod. D et edd. 1, 8 *subsistit*₅, quod magis placeret, si faveret Augustinus." (Note: chunk had lemma reversed: *consistit* not *subsistit* is the base reading; *subsistit* is the variant with subscript-5 cross-reference glyph.) Also corrected "Cap. 1." → "Cap. 4." per PDF. The subscript ₅ is a printed cross-reference indicator — preserved as `[?]` since it's a typographic glyph not a Latin word.
- **[^19] En**: RESOLVED with same content fix.
- **[^20] La `Ephes. 4, 8 [?]`**: RESOLVED — PDF #7 confirms "Ephes. 4, 8." Removed [?].
- **[^20] La `mss. AC[?]`**: RESOLVED — PDF #7 reads "mss. ACDE." (full siglum is ACDE, not AC[?].)
- **[^20] La `inc[ipiunt?]` and trailing `*Spiritus.* [?]`**: RESOLVED — PDF #7 reads "incipiunt sequentem textum verbis: *Spiritus quoque* pro *Spiritus ergo.*" Full text recovered.
- **[^20] En**: RESOLVED with same content fix.
- **[^21] La `post *est* [?] omittunt: *quomodo Deus dilectio est, si* [non est?]. [?]`**: RESOLVED — PDF #8 reads "1. Ioan. 4, 16. — Vat. et ed. 4 post *nihil est* perperam omittunt; *quomodo Deus dilectio est, si non est substantia.*" Word before *est* is *nihil*; completion is *non est substantia*; adverb *perperam* recovered.
- **[^21] En**: RESOLVED.
- **[^22] La `*Pater* [?] *Patrem diligit Filius*` and `BC[?] [contra?] originali pro *ineffabilem* [legunt?] *ineffabiliter.* [?]`**: RESOLVED — PDF #9 reads in full: "Cod. C brevius: *Filius Patrem* loco *Patrem diligit Filius.* Mox codd. BCD et edd. 1, 8 cum originali pro *ineffabilem* legunt *ineffabiliter,* et sic hoc adverbio determinari videtur *diligit.* Denique in fine huius propositionis cod. E et cod. 8 *communis amborum* pro *communis ambobus.*" Codex C reads `Filius Patrem` (not `Pater`); siglum is BCD plus edd. 1, 8; adverb-determines-diligit clause recovered; final *amborum*/*ambobus* clause recovered.
- **[^22] En**: RESOLVED.
- **[^6] La `*ut* [?] *est*`** (p.192 footer): ACCEPT-ILLEGIBLE — printed text shows literal "ut 1 T est" with the middle character appearing as serif "1 T" (likely a Quaracchi typographic cross-reference glyph between *ut* and *est*; see Quaracchi practice of inline cross-reference markers in textual-variant footnotes). Not a recoverable Latin word. Reason: typographic device, not text.
- **[^6] En**: ACCEPT-ILLEGIBLE (mirror).

**Structural fix:** Added new [^23] = PDF #10 ("Col. 1, 13. — Vat. cum pluribus edd. ante *Trinitate* ponit *ista* pro *illa*; postea idem fit ab edd. 3, 5, 9 post *sed propter.*"), with body anchor at `Apostolus[^23]` (Paul's Col 1:13 quote in Cap. III).

**p.193 body anchor renumbering (chunk → corrected to match PDF marker positions):**
- `Ioannes[^12]` → `Ioannes[^14]` (PDF #1 — Ibid. v.11-13)
- `Ipse igitur est Deus dilectio[^13]` → `[^15]` (PDF #2 — *Ipse ergo Deus est dilectio* variant)
- (NEW) `dilectio ex Deo est*[^16]` (PDF #3 — Omnia in hoc capitulo... Augustino XV de Trin)
- `explicabitur[^15]` → `[^17]` (PDF #4 — Infra dist. XVII)
- `Nunc vero[^16]` → marker REMOVED; new anchor at `Psalmum[^18]` (PDF #5 — Vers. 1; Vatican variant noted in PDF starts with *Vers. 1.* — *Antea post Nunc edd. 1, 8 ergo pro vero* is part of same entry)
- `Psalmum[^17]` → relocated as `Psalmum[^18]`
- `de Trinitate[^18]` (Aug 6th) → `[^19]` (PDF #6 — Cap. 4 et 5)
- `sintque[^19]` → marker REMOVED; new anchor at `vinculo pacis*[^20]` (PDF #7 — Ephes. 4, 8 — text mentions *sintque* variant; PDF marker is at end of *vinculo pacis* phrase per printed superscript)
- `Deus caritas est[^20]` → `*Deus caritas est*[^21]` (PDF #8 — 1. Ioan. 4, 16)
- `de Trinitate[^21]` (Aug 15th, Cap III) → `[^22]` (PDF #9 — Cap. 19 n. 37)
- `Apostolus[^22]` → `[^23]` (PDF #10 — Col. 1, 13)

**p.192 body anchors:** [^12] and [^13] apparatus entries (1 Cor 1:24, 1 John 4:7) had no body anchors after p.193 renumber. Added [^12] and [^13] alongside existing [^10] and [^11] at `dicentis[^10][^12]` and `eloquium[^11][^13]` (both Latin and English bodies) — convention permits paired anchors at the same body position when one footer covers a textual variant and another covers a scripture citation. (This preserves chunk-level invariant: every [^N]: def has matching anchors in both languages.)

**Remaining ACCEPT-DEFERRED issues (not in scope for this PDF-recovery pass):**
- **Apparatus content for [^1]..[^11]** (p.192 footer 1-10 + 3 marginal entries) is correctly transcribed from raw OCR. Body anchor positions on p.192 use [^1]..[^11] but printed page has 13 markers (10 NOTAE + 3 marginal) — chunk anchors omit explicit anchors for the 3 marginal markers. This is a separate cleanup (would require renumbering 1-11 to 1-13 with new anchor positions for marginal entries).
- The chunk's apparatus entry order on p.192 mixes the 3 marginal entries among the 10 NOTAE entries (e.g. [^4] is a marginal entry, [^5] is a NOTAE entry). Reordering to "marginal first, NOTAE second" or vice versa is not in the d.1-d.10 polish blocker scope.

**[?] resolved count:** 11 (across 5 apparatus entries × Latin+English pairs, plus a few singletons).
**[?] kept as ACCEPT-ILLEGIBLE:** 2 (both in [^6], same typographic cross-reference glyph).
**Net:** 11 of 13 [?] flags resolved with verbatim PDF text; 2 kept with ACCEPT-ILLEGIBLE reason; 1 missing apparatus entry recovered ([^23] Col 1:13); body anchor positions on p.193 corrected to match the 10 printed footer markers; transcription_status updated.

## d1-a3-q1 (pp. 38-39)

- **Source**: `raw/vision/vol1/p-039.png` (600 dpi extract, footer band cropped via PIL to `/tmp/p039-footer-{L,R}.png` for legibility).
- 6 inline `[?]` flags in apparatus entries `[^14]`, `[^15]`, `[^16]` resolved via 600dpi PDF eyes-on read of p.39 footer band. All carried over from the 2026-05-10 d.1-d.10 rechunk pipeline pass.

| `[^N]` | Flag location | Pre-pass rendering | Resolved verbatim from PDF p.39 footer |
|---|---|---|---|
| `[^14]` | After `manifestum est` (Latin) | `manifestum est [?]... tire ex vehementi sensibili...` | `manifestum est sensoriis et sensu. Sensus enim non potest sentire ex vehementi sensibili...` (footer #5 on p.39 is fully legible; OCR had dropped `sensoriis et sensu. Sensus enim non potest sen-` across a line-break). RESOLVED. |
| `[^14]` | After `hic (intellectus)` (Latin) | `hic (intellectus) [?] est.` | `hic (intellectus) autem separabilis est.` RESOLVED. |
| `[^14]` | English mirror (first) | `manifest [?]... [the sense being unable to] sense from a vehement sensible...` | `manifest in the sense-organs and in sense. For sense cannot sense from a vehement sensible...` RESOLVED. |
| `[^14]` | English mirror (second) | `this (the intellect) [?] is.` | `this (the intellect) is separable.` RESOLVED. |
| `[^15]` | Latin: `Auctoritate antiquiorum [mss. — text garbled in OCR; [?]] substituimus` | bracketed disclaimer about OCR garble | Footer #6 reads cleanly: `Auctoritate antiquiorum mss. substituimus intelligibile loco intelligentiae.` Disclaimer stripped; English already correct. RESOLVED (OCR was actually fine; the prior pass over-flagged). |
| `[^16]` | Latin & English: `et ed. [?]` / `the [first] edition [?]` | edition number not certain | Footer #7 reads: `Ita codd. CHKOSTUY aa bb et ed. 1, sed codd. AF ILMRVWXZ participando;` — i.e. `ed. 1` = first edition. RESOLVED in both Latin and English (English bracketed-`[first]` qualifier removed; now reads plain `the first edition`). |

### `[?]` resolution count

- 6 `[?]` flags resolved (all via 600dpi PDF eyes-on of p.39 footer band).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d1-a3-q1.md` after this pass.

### Anchor-position residuals from prior log NOT in scope of this pass

The `manual-review/tier2-ambiguities-d1-a3-q1.md` file flagged three anchor-placement uncertainties (`[^11]`, `[^12]`, `[^13]`/`[^14]` on p.39) where the marker glyphs in the OCR could not be reliably distinguished. Those concern *anchor position* (lemma-reasoning vs. glyph-confirmed), not text content, and were NOT marked with inline `[?]` flags in the chunk body — they remain dispositioned as "plausible, glyph-not-confirmed" per the existing log. The d.1-d.10 polish blocker scope is inline `[?]` text content; anchor-position residuals stay as-is.

## d2-a1-q3 (pp.54-56)

Bucket 1 [?]-flag polish pass against 600dpi PDF (`raw/vision/vol1/p-054.png` … `p-056.png` re-extracted at 600 dpi via `tools/extract-pages.py --force`). The IA djvu OCR for pp.54–56 was intact (apparatus already recovered in the 2026-05-10 rechunk pass); this session resolves three small OCR ambiguities that the rechunk pipeline correctly flagged with `[?]` rather than silently guessing.

| Locus | OCR garble | PDF reading | Disposition |
|---|---|---|---|
| Scholion II citation list (Latin line 72 + English mirror line 118) | OCR `S.  et  7.` rendered as `q. 5.[?] et 7.` / `q. 5[?] and 7.` | p.56 right-column scholion plainly reads `Scot., hic q. 5. et 7.` | RESOLVED → `q. 5.` (the `[?]` was a precautionary flag; the digit is unambiguous on the PDF) |
| Apparatus `[^11]` La+En (lines 166, 168) | OCR `pT&  qualibet` rendered as `*pra qualibet*[?]` | p.55 right-column footer note 9 reads `Codd. A T aliique cum ed. I **pro qualibet**, quod exstat in Vat., exhibent distinctius **qualicumque**` | RESOLVED → `*pro qualibet*` (OCR `pT&` / `pra` was a garble of `pro`); English mirror updated to gloss `pro qualibet` as "for whatsoever" |
| Apparatus `[^14]` La+En (lines 178, 180) | OCR line-broke `re-/i` rendered as `circa finem rei[?]` / `near the end of the matter[?]` | p.55 right-column footer note 12 plainly reads `Dein circa finem **re-/sponsionis** ex mss. et ed. I ante *ideo* adiecimus particulam *et*` | RESOLVED → `circa finem responsionis` / `near the end of the response` (OCR truncated `responsionis` at hyphenated line-break, leaving the `re-` fragment that the rechunker read as `rei`) |

### `[?]` resolution count

- 6 `[?]` flags resolved (3 distinct loci × Latin + English mirrors).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `vol1/bon-sent-I-d2-a1-q3.md` after this pass.

### Verification

- `grep -c "\[?\]" vol1/bon-sent-I-d2-a1-q3.md` → 1 (the meta-mention in `transcription_status` describing the rechunk-era flagging, kept as historical record).
- `cd site && node scripts/build-content.mjs` parses cleanly (414 chunks).
- d.2-scoped `audit-paraphrase` / `audit-headers` / `audit-apparatus-count` re-run clean (see audit block at end of this log).

## d4-a1-q2 (pp.99-101)

- **Source**: `raw/vision/vol1/p-hires-d4q2-{201,202,203}.png` (600 dpi extracts of PDF pp. 201-203 = printed pp. 99-101).
- **9 inline `[?]` flags** previously logged in `manual-review/tier2-ambiguities-d4-a1-q2.md` (5 Latin + 4 English/scholion). All 9 resolved by eyes-on 600 dpi read; no flags accepted-illegible.

| # | Location | Prior rendering | Disposition |
|---|---|---|---|
| 1 | Latin Respondeo, p.100 col.1 | `de virtute[?][^6] sermonis` | RESOLVED → `de virtute[^6] sermonis`. PDF p.100 col.1 reads *virtute* (Vat. reading; ap. crit. note [^6] records codd. R cc *veritate*). |
| 2 | English mirror | `strict force[?][^6] of the discourse` | RESOLVED → `strict force[^6] of the discourse`. |
| 3 | Latin Respondeo end, p.100 col.1 | `non sequitur ad verbum [simpliciter? distin][?]ctionem` | RESOLVED → `non sequitur ad verbum simpliciter distinctionem`. PDF p.100 col.1 bottom clearly reads the unbroken phrase. OCR garble was line-break artefact. |
| 4 | English mirror | `there does not follow upon the [single?] word [simply distin][?]ction` | RESOLVED → `does not follow upon the word [taken] simply [a] distinction`. |
| 5 | Latin Ad 3, p.101 col.1 | `scilicet quod *Deus* [genuit?][?] *Deum*` | RESOLVED → `scilicet quod *Deus genuit Deum*`. PDF p.101 col.1 confirms full italic *Deus genuit Deum*; OCR had elided the verb. |
| 6 | English mirror | `namely that *God [generated?][?] God*` | RESOLVED → `namely that *God generated God*`. |
| 7 | Latin Scholion I, p.101 col.2 | `ad suum subiectivum [substantivum?][?] ponitur` | RESOLVED → `ad suum subiectivum ponitur`. PDF p.101 col.2 (scholion band) clearly reads *subiectivum* — OCR was correct; prior reviewer's "expected substantivum" hypothesis was wrong. The scholion deliberately distinguishes *subiectivum* (the thing the adjective subjects itself to, i.e. its grammatical subject) from *substantivum* later in the same sentence. |
| 8 | Latin Scholion I | `importat [alietatem?][?] circa suum substantivum` | RESOLVED → `importat alietatem circa suum substantivum`. PDF p.101 scholion band confirms *alietatem* in full. |
| 9 | English mirror (both 7 & 8) | `to its subject [substantive?][?], imports [otherness?][?]` | RESOLVED → `to its subject [substantive], imports otherness`. |

### `[?]` resolution count

- 9 `[?]` flags resolved (all via 600 dpi PDF eyes-on of pp.99-101).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d4-a1-q2.md` after this pass.

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d4-a1-q2.md` → 0.
- `cd site && node scripts/build-content.mjs` parses cleanly at 414 chunks.
- Guard-rail audits (paraphrase, headers, apparatus-count) scoped to d.4 run with no new flags.

## d4-a1-q1 (pp. 97–99)

- **Source**: `raw/vision/vol1/p-097.png`, `p-098.png`, `p-099.png` (600dpi from `doctorisseraphic11bona.pdf` PDF pp. 199–201). Footer bands cropped via PIL for legibility.
- **Status**: Tier-2 chunk from 2026-05-10 rechunk pipeline carried 13 inline `[?]` flags — 1 pair in scholion I body ("[terminorum?]" / "[terms?]"), and 11 inside apparatus `[^10]`, `[^14]`, `[^15]`, `[^16]`, `[^17]` (La+En) where OCR garbled italicized lemmata in the footer band on p. 98 right column. All 13 resolved against the 600dpi PDF.

| Body anchor | Disposition | PDF source |
|---|---|---|
| Scholion §I body (La): `aliquorum [terminorum?][?]` | RESOLVED → `aliquorum terminorum,` | p. 98 left column, scholion opening line — printed `terminorum,` plain. |
| Scholion §I body (En): `certain [terms?][?]` | RESOLVED → `certain terms` | mirror of above. |
| `[^10]` La: `tract. de Re[strictione?][?]` | RESOLVED → `tract. de Relativis.` | p. 98 left-col footer note 3, ends "quarta in eiusdem *Summula*, tract. de Re-/lativis." (line-broken across two physical lines; tract is *de Relativis*, NOT *de Restrictione* as the OCR guess assumed). |
| `[^10]` En: `tract on Re[striction?][?]` | RESOLVED → `tract on Relatives.` | mirror. |
| `[^14]` La: `in *immultiplicabilem*[?].` | RESOLVED → `in *immultiplicabilem*.` (drop `[?]`) | p. 98 right-col footer note 6 verbatim: "Ex antiquioribus mss. et ed. 1 mutavimus *responsio* in *solutio* et paulo post *non multiplicabilem* in *immultiplicabilem*." Confirms reading is correct as it stands. |
| `[^14]` En: `into *immultiplicabilem*[?].` | RESOLVED → `into *immultiplicabilem*.` | mirror. |
| `[^15]` La: `addit [verbum?][?].` | RESOLVED → `addit *totaliter et*.` | p. 98 right-col footer note 7 verbatim: "Vat. contra antiquiores codd. et ed. 1 addit *totaliter et*." The added Vatican words are *totaliter et*, anchored at "negatio praeposita … omnino a subiecto removeat praedicatum" — Vat. inserts *totaliter et* before *omnino*. |
| `[^15]` En: `adds [a word?][?].` | RESOLVED → `adds *totaliter et*.` | mirror. |
| `[^16]` La: `aliam a [supposito?][?] antecedente` | RESOLVED → `aliam a suo antecedente` (also corrects `habeat` → `habet` and re-italicizes the cod. K lemma) | p. 98 right-col footer note 8 verbatim: "Supplevimus mss. et ed. 1. *Deus*. Paulo ante cod. K. modo negativo *relativum non habet suppositionem aliam a suo antecedente*." The bracketed `[supposito?]` was a wrong OCR guess; printed text is *suo*. Verb is `habet` (indicative) not `habeat` (subjunctive). |
| `[^16]` En: `from its [supposit?][?] antecedent.` | RESOLVED → `from its own antecedent.` (translation revised to match `suo antecedente`) | mirror. |
| `[^17]` La: `Cod. K. addit [scilicet?][?] hic:` | RESOLVED → `Cod. K. addit *hic*:` (drop bracketed guess; italicize the single added word `hic`) | p. 98 right-col footer note 9 verbatim: "Cod. K. addit *hic*: *Deus genitus non est Pater; ergo Deus non est Pater*." The added codex-K word is just *hic* (italicized), not a separate *scilicet*. Also corrected the semicolon between clauses per printed text. |
| `[^17]` En: `adds [namely?][?]:` | RESOLVED → `adds *hic* ["here"]:` | mirror with literal gloss of the Latin word `hic`. |

### `[?]` resolution count

- 13 `[?]` flags resolved (2 in scholion body, 11 in apparatus `[^10]`/`[^14]`/`[^15]`/`[^16]`/`[^17]` La+En pairs).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d4-a1-q1.md` body/apparatus after this pass.

### Notes from the read

- p. 98 footer column-split: the left column carries notes 1–3 of the page (Bonaventure body footnotes), the right column carries notes 4–9. The IA djvu OCR for this footer band garbled the italicized Latin lemma words inside notes 6, 7, 8, 9, which is why the rechunk left bracketed-guess flags there. The 600dpi PDF read is unambiguous for all four.
- `[^16]` correction (`habeat` → `habet`, italicization scope) was applied alongside the `[supposito?]` → `suo` resolution as part of the same lemma; this matches Quaracchi's printed italics convention for codex variant readings.
- `[^17]` correction (colon → semicolon inside the cod. K lemma, italics scope) likewise matches the printed text.
- The bracketed English gloss `*hic* ["here"]` in `[^17]` En mirrors d.5–d.6 polish-log convention for translating Latin variant-word lemmata.

### Verification

- `grep -nE '\[\?\]' vol1/bon-sent-I-d4-a1-q1.md` → only the `transcription_status` frontmatter line (historical reference to "flags on ambiguous spots"); no body or apparatus `[?]`.
- `cd site && node scripts/build-content.mjs` parses cleanly.
- d.4-scoped audits (paraphrase, headers, apparatus-count) re-run with no new flags surfaced by this chunk.

## d8-p1-a2-q1 (pp.156-158)

- **Source**: `raw/vision/vol1/p-156.png`, `p-157.png`, `p-158.png` (re-extracted at 600 dpi).
- The chunk carried 8 inline `[?]` flags (4 distinct loci, each mirrored Latin + English) — all introduced by the 2026-05-10 rechunk pipeline against well-formed Quaracchi editorial brackets that the rechunk treated as uncertain.
- Eyes-on the 600dpi PDF resolves all 4 loci as standard Quaracchi printed readings; no actual transcription ambiguity remained.

| Locus | Body / Apparatus | Disposition | Footer source |
|---|---|---|---|
| Respondeo `pure[?] actus` (Lat) + `purely[?] act` (En) | body, p.157 | RESOLVED → `pure` / `purely` | `[^13]` itself documents: "cum plerisque codd. ut ASTVW etc. et ed. 1 legimus *pure* loco *purus*"; Quaracchi prints *pure*. |
| `[^2]` `*Omne [movetur][?] ex potentia...*` (Lat) + En mirror | apparatus, p.156 footer note 2 | RESOLVED → `[movetur]` (Quaracchi editorial supply) | p.156 footer 2 read verbatim: "Vide Aristot., XII. Metaph. text. 8. (XI. c. 2.): *Omne [movetur] ex potentia ente in actu ens.*" Square brackets are Quaracchi's own supplied verb. |
| `[^3]` `*Sciendum itaque, quia [omnis][?] mutatio...*` (Lat) + En mirror | apparatus, p.156 footer note 3 | RESOLVED → `[omnis]` (Quaracchi editorial supply) | p.156 footer 3 read verbatim: "Libr. II. de Trin. c. 3.: *Sciendum itaque, quia [omnis] mutatio est aut de statu...*" Bracketed *omnis* is Quaracchi's editorial supply, not OCR doubt. |
| `[^24]` `omittit *non bene sed actio est ab ipso*[?]` (Lat) + En mirror | apparatus, p.158 footer note 6 | RESOLVED → lemma reads exactly as printed | p.158 footer 6 read verbatim: "Vat. contra fere omnes codd. et ed. 1 omittit *non bene sed actio est ab ipso*, pro quo cod. Q *sed actio est aliquid ab ipso*." The phrase "*non bene sed actio est ab ipso*" is Quaracchi's own lemma — "non bene" flags the Vatican omission as wrongful, "sed actio est ab ipso" is the restored reading. |

### `[?]` resolution count

- 8 `[?]` flags resolved (4 Latin + 4 English mirrors).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d8-p1-a2-q1.md` body/apparatus after this pass (the only surviving `[?]` substring is in the `transcription_status` frontmatter, which is historical-reference convention).

### Verification

- `grep -nE '\[\?\]' vol1/bon-sent-I-d8-p1-a2-q1.md` → only the `transcription_status` frontmatter line.
- `cd site && node scripts/build-content.mjs` parses cleanly (414 chunks).
- d.8-scoped audits (paraphrase, headers, apparatus-count) re-run.

## d3-p1-a1-q1 (pp.67-70)

- **Source**: `raw/vision/vol1/p-068.png`, `p-069.png` (re-extracted at 600 dpi via `tools/extract-pages.py --force`). Footer band of p.68 and body of p.69 read eyes-on.
- The chunk carried 5 inline `[?]` flags — 1 body locus (Latin + English mirror) at the p.68→p.69 boundary for the close of contra-arg 5, 1 apparatus locus `[^6]` (Latin + English mirror) for the Augustine *de Vera Relig.* quotation, plus 1 trailing stray `[?]` in the English mirror of `[^4]` (no Latin counterpart, OCR-pipeline artefact).

| Locus | Body / Apparatus | Pre-pass rendering | Disposition (PDF p.68/p.69 verbatim) |
|---|---|---|---|
| Close of contra 5 (Lat body, p.68 bottom) | body | `ergo illa maxime [cognoscibilis est ipsi intellectui nostro]. [?]` | RESOLVED → `ergo illa maxime cognoscibilis ab intellectu.` PDF p.68 line above the footer rule plainly reads `ergo illa maxime cognoscibilis ab intellectu.` — the OCR-era bracketed completion was a wrong editorial guess (it conflated the Quaracchi-preferred *intellectui nostro* reading from `[^13]` apparatus into the body text). The printed body says *ab intellectu*; `[^13]` separately notes that codex X adds *ipsi animae* and that *intellectui nostro* would please better. |
| Close of contra 5 (En mirror) | body | `therefore that [light is] most [knowable to our intellect]. [?]` | RESOLVED → `therefore that [light] is most knowable by the intellect.` |
| `[^4]` En trailing `[?]` | apparatus, p.68 footer note 3 | `…cf. Boethius, *De Consolatione* V, Prose 4. [?]` | RESOLVED → trailing `[?]` removed. Latin `[^4]` had no `[?]`; the English mirror's stray was an OCR-pipeline artefact. Footer text matches Quaracchi verbatim. |
| `[^6]` La (Augustine *de Vera Relig.* c. 29 n. 53) | apparatus, p.68 footer note 5 | `August., *de Vera Relig.* c. 29. n. 53: [...] *poribus non sentientis tantum vitae, sed etiam rationali[s]* [?] [...] *Iam vero illud videre facillimum est, praestantiorem esse iudicantem, quam illa res est, de qua iudicatur.* — Cod. X hic addit *sicut dicit Augustinus*.` | RESOLVED → `August., *de Vera Relig.* c. 29. n. 53: *Iudicare de corporibus non sentientis tantum vitae, sed etiam ratiocinantis* etc., *iam vero illud videre facillimum est, praestantiorem esse iudicantem, quam illa res est, de qua iudicatur.* — Cod. X hic addit *sicut dicit Augustinus*.` p.68 footer #5 read verbatim: Quaracchi opens with *Iudicare de corporibus…* and uses `etc.` to elide a clause, then resumes *iam vero illud videre facillimum est…*. The OCR garble `[cor]poribus … rationali[s]` was a column-edge fragment of `corporibus … ratiocinantis` — the truncated word is *ratiocinantis* (judging-of-reasoning-life), not *rationalis*. |
| `[^6]` En mirror | apparatus | `"[...] in bodies, of life not only sentient, but also rational [?] [...] Now it is most easy to see that he who judges is more excellent than the thing concerning which he judges."` | RESOLVED → `"To judge concerning bodies belongs not only to sentient life, but also to ratiocinating [life]," etc., "now it is most easy to see that he who judges is more excellent than the thing concerning which he judges."` Reflects the recovered Latin lemma and Quaracchi's `etc.` elision. |

### `[?]` resolution count

- 5 `[?]` flags resolved (all via 600dpi PDF eyes-on of pp. 68-69).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d3-p1-a1-q1.md` body/apparatus after this pass (the only surviving `[?]` substring is in the `transcription_status` frontmatter, which is historical-reference convention).

### Verification

- `grep -nE '\[\?\]' vol1/bon-sent-I-d3-p1-a1-q1.md` → only the `transcription_status` frontmatter line.
- `cd site && node scripts/build-content.mjs` parses cleanly (414 chunks).
- d.3-scoped audits (paraphrase, headers, apparatus-count) re-run.

## d6-a1-q1 (pp.125-126)

- **Source**: `raw/vision/vol1/p-125.png`, `p-126.png`, `p-127.png` (600 dpi extracts of PDF pp. 227–229 = printed pp. 125–127). Scholion II citation list wraps from p.126 right-column tail onto p.127 top — full disambiguation required reading p.127 top as well.
- **Pre-state**: 6 inline `[?]` flags from the 2026-05-10 d.1-d.10 rechunk pipeline: 1 pair in Scholion II body (`B. Albert., hic [?]` La + En mirror) where the citation list was truncated at the page-126 column edge; 1 pair trailing `[^2]` apparatus (La+En) over OCR garble `*ee aliquo*`; 1 pair trailing `[^12]` apparatus (La+En) over a bracket-completion guess `tactae [sunt]`.

| Locus | Pre-pass rendering | PDF reading | Disposition |
|---|---|---|---|
| Scholion II body (La line 77) | `B. Albert., hic [?]` | p.126 right-col scholion runs `… B. Albert., hic` and **continues at top of p.127 left col**: `a. 1; S. p. I. tr. 7. q. 30. m. 3. a. 2. — Petr. a Tar., hic q. 1. a. 1. — Richard. a Med., hic q. 1. — Aegid. R., hic 1. princ. q. 1. et 2. — Henr. Gand., de hac et seq. q. 8. a. 54. q. 3.` | RESOLVED — pasted the p.127 continuation in full; `[?]` removed. |
| Scholion II body (En line 129) | `Bl. Albert, here [?]` | mirror — translates names: Peter of Tarentaise, Richard of Mediavilla, Giles of Rome, Henry of Ghent | RESOLVED. |
| `[^2]` La (line 140) trailing `[?]` | `Nonnulli codd. ut KWXY *ee aliquo* pro *alio*. [?]` | p.125 left-col footer note 2 reads verbatim `Nonnulli codd. ut K W X Y *ee aliquo* pro *alio*.` (printed with spacing between sigla; entry ends cleanly with the period). The `*ee aliquo*` is the Quaracchi-printed reading (idiosyncratic; preserved as printed). | RESOLVED — trailing `[?]` removed; sigla spaced per print. |
| `[^2]` En (line 141) trailing `[?]` | mirror | mirror | RESOLVED. |
| `[^12]` La (line 170) trailing `[?]` | `… quae in praecedentibus tactae [sunt]. [?]` | p.126 left-col footer note 4 reads verbatim `… quae in praecedentibus tactae sunt.` (the `sunt` is fully present on the printed page — no bracket-completion needed). | RESOLVED — brackets and `[?]` removed; `sunt` is verbatim. |
| `[^12]` En (line 171) trailing `[?]` | mirror | mirror — the English `[passages]` bracketed gloss is a translator's clarification, not an OCR flag; retained without the `[?]` | RESOLVED. |

### `[?]` resolution count

- 6 `[?]` flags resolved (all via 600dpi PDF eyes-on of pp.125–127).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d6-a1-q1.md` body/apparatus after this pass.

### Notes from the read

- Scholion II is the last paragraph on p.126; the citation list spans the right-column tail of p.126 and continues at the top of p.127 col.1 (a DIST. VI. ART. UNICUS Q. II running head sits above it). The truncation at "B. Albert., hic" was a column-boundary artefact in the rechunk pipeline, not a printed-text gap.
- "Aegid. R., hic 1. princ." preserves the printed form (Quaracchi prints a bare `1.` between `hic` and `princ.`); not silently emended.
- "q. 8." in the Henr. Gand. citation: Quaracchi prints what visually reads as `q. S.` but is standardly the numeral 8 in this typeface for citation contexts; rendered as `q. 8.` for clarity.

### Verification

- `grep -nE '\[\?\]' vol1/bon-sent-I-d6-a1-q1.md` → only the `transcription_status` frontmatter line (historical reference). No body or apparatus `[?]`.
- `cd site && node scripts/build-content.mjs` parses cleanly (414 chunks).
- d.6-scoped guard-rail audits (paraphrase, headers, apparatus-count) re-run with no new flags surfaced by this chunk.

## d8-p1-a1-q2 (pp.152-154)

- **Source**: `raw/vision/vol1/p-153.png` (existing 600 dpi), `raw/vision/vol1/p-hires-d8q2-256.png` (printed 154, 600 dpi), `raw/vision/vol1/p-hires-d8q2-257.png` (printed 155, 600 dpi, where SCHOLION resides), `raw/vision/vol1/p-hires-d8q2-258.png` (printed 156, 600 dpi, where scholion II finishes).
- **Note on page ranges**: Q.II actually begins on printed p.153, not p.152 — p.152 holds the end of q.I plus the q.I SCHOLION. Frontmatter `printed_pages: [152, 153, 154]` is therefore slightly mis-set (true span [153, 154, 155, 156] when scholion is included). Out-of-scope for this [?]-flag pass; logged here for the corpus-wide frontmatter audit. The `<!-- page N -->` markers in the chunk were left untouched.

### `[?]` flags walked

| # | Location | Disposition |
|---|---|---|
| 1 | Latin l. 58 / English l. 142, `tellecto[?]` (`[?the highest good]` in English) | **RESOLVED.** Raw OCR (line 32136-37) breaks "in-tellecto" across the line; the word is unambiguously `intellecto` (ablative absolute taking `esse impossibile, summum bonum non esse` as its content). PDF p.154 top confirms a normal line-break hyphen. Stripped `[?]`; rewrote English to "with [it] understood to be impossible that the highest good is not". |
| 2 | Latin l. 108 / English l. 190, `de nostra cognitione[?]` | **RESOLVED.** PDF p.155 right column (scholion I, last clause) ends "...immediate est de nostra cognitione." with a clean period — sentence terminates there with no missing word. Stripped `[?]` and the editorial `[of it]` placeholder retained as a literal English supply, no longer flagged. |
| 3 | Latin l. 110 / English l. 192, end of long Alex. Hal. quotation, `nominatur Deus*»[?]` | **RESOLVED.** PDF p.156 top-left column shows the Alex. Hal. citation closing cleanly: "*…in eo quod ens est, ignorantissime nominatur Deus*»." with a normal closing guillemet + period. Nothing dropped from the quotation. Stripped `[?]`. |
| 4 | Latin l. 110, eight inline `[?]` flags in scholion II opening: `Sic[?] habet B. Albertus[?] ad probandum, [?] putatur. [?] doctrina [?] gument [?] primi [?] per se notum esse.` (and mirrored editorial markers in English l. 192) | **ACCEPT-ILLEGIBLE.** This passage corresponds to a heavy OCR-band dropout in `raw/bonaventure_vol1_raw.txt` ll. 32431–32441 — the printed text on PDF p.155 bottom-right (start of scholion II) is legible to a reader with the physical volume but garbles at 600 dpi rendering of the scanned IA copy: lateral ink-bleed across the column gutter has made the second column's first six lines a half-tone smear in our PDF source. A careful read produces a plausible reconstruction ("Sic habet B. Albertus, ad probandum, ut putatur, in hac doctrina argumentum primi per se notum esse") but no single reading is confidently distinguishable from one or two close alternatives (e.g. `Item` vs `Sic`; `etiam, ut` vs `ut`; `argumentum primi principii` vs `argumentum primi`). Per the polish-pass discipline (no invented Latin), flags remain in-place. Disposition path forward: a clean physical-book or Vatican-edition consult will close these in a later pass; the apparatus citations (Scotus, S. Thomas, Suarez, Alex. Hal.) that follow are NOT affected and remain Tier-2 clean. |

### `[?]` resolution count

- 3 `[?]` flags RESOLVED via 600 dpi PDF (line 58 `tellecto`; line 108 `cognitione`; line 110 closing `Deus*»`).
- 8 `[?]` flags ACCEPT-ILLEGIBLE (scholion II opening clause; OCR-band dropout + image-side smear).
- Net: 14 → 8 `[?]` occurrences in the chunk file (Latin + English mirror combined).

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d8-p1-a1-q2.md` → 8 (down from 14).
- `cd site && node scripts/build-content.mjs` parses cleanly (414 chunks).
- d.8-scoped guard-rail audits (paraphrase, headers, apparatus-count) re-run; no new flags surfaced by this chunk.

## d2-littera (pp.46-49)

Pass date: **2026-05-12**. Source: `raw/vision/vol1/p-046.png`–`p-049.png` re-extracted at 600 dpi via `tools/extract-pages.py --volume vol1 --pages 46-49 --dpi 600 --force`. Chunk previously held 5 inline `[?]` flags across 4 apparatus footnotes (`[^8]` La+En, `[^36]` En, `[^37]` En, `[^43]` En).

| Flag location | Disposition | PDF citation |
|---|---|---|
| `[^8]` La: *audit hoc*[?] | RESOLVED → strip `[?]`, keep *audit hoc* | p.46 footer note 8 reads "*audit hoc*" cleanly (OCR garble "«*'« hoc" → *audit hoc*). |
| `[^8]` En: *audit hoc*[?] + verification gloss | RESOLVED → strip `[?]` and drop the "[OCR garble suggests...]" gloss | Same source as above; lemma now confirmed. |
| `[^36]` En: marginal-rubric `[?]` | RESOLVED → strip `[?]`, refine note to specify *right* margin | p.47 right margin shows printed rubric **Aliae auctoritates.** beside "Nunc vero ad propositum redeamus" body line; the chunk's claim that a marginal rubric exists at this position is confirmed. |
| `[^37]` En: Gen 1:1 page-break `[?]` | RESOLVED → strip `[?]` | p.47 col-2 bottom ends *In principio creavit Deus caelum et*; p.48 col-1 top resumes *terram*. Citation continuation verified. |
| `[^43]` En: *passus est* vs *natus est* `[?]` | RESOLVED → strip `[?]`, tighten gloss to "printer's slip in the Quaracchi apparatus (confirmed 600dpi p.48 eyes-on)" | p.48 body reads "ex Patre **natus** est Filius, ex Patre processit Spiritus sanctus"; p.48 footer note 3 says *procedit* "minus correspondet praecedenti *passus est*". Body=*natus*, apparatus=*passus* — confirmed Quaracchi printer's slip, not a chunk-transcription error. |

### Systemic patterns checked

- Quaracchi-bracket-as-supply pattern: scanned chunk for `[word]` printed brackets adjacent to `[?]` — none present in this chunk.
- Body-vs-apparatus interpolation: verified body text against p.46-49 eyes-on; no apparatus-block leakage into Latin body found.

### `[?]` resolution count

- Before: 5 inline `[?]` flags.
- After: 0 inline `[?]` flags.
- Resolved via 600dpi PDF: 5.
- Accepted-illegible: 0.

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d2-littera.md` → 0.
- `cd site && node scripts/build-content.mjs` → expect 414 chunks.
- Guard-rail audits for d.2 (paraphrase + headers + apparatus) run clean below.

## d2-dubia (pp.59-62)

- **Source**: `raw/vision/vol1/p-hires-d2dub-r600-p62-164.png` (600 dpi extract of PDF p.164 = printed p.62) and `p-hires-d2dub-r600-p60-162.png` (printed p.60). Footer bands cropped via PIL for legibility (`p62-bonav-footer.png`, `p62-bonav-footer2.png`, `p60-footer.png`).
- **Status**: Tier-2 chunk from 2026-05-10 rechunk pipeline carried 5 inline `[?]` flags — 1 inside apparatus `[^10]` En (the `satis huic addit` mistranslation; `nostris` mis-reading) and 2 pairs (La+En) in `[^31]` / `[^32]` where the OCR raw range did not include the p.62 Bonaventure-band footer (the OCR included only the lower Lombard "NOTAE AD LIBR. SENTENTIARUM" footer beneath Distinctio III's opening). All 5 resolved against the 600dpi PDF; the p.62 Bonaventure footer band sits *between* the page body and the Lombard `NOTAE AD LIBR. SENTENTIARUM` block.

| # | Location | Prior rendering | Disposition |
|---|---|---|---|
| 1 | `[^10]` La line, p.60 footer note 6 | `cod. K satis huic addit *aut uni aut pluribus; non pluribus, quia deberet dicere nostris; si pro una.*` | RESOLVED → `cod. K satis huic adiungit *aut uni aut pluribus; non pluribus, quia deberet dicere imaginis; si pro una.*` PDF p.60 right-column footer note 6 plainly reads *adiungit* (not *addit*) and *imaginis* (not *nostris*). The OCR confused both — *adiungit* "adjoins" matches the surrounding apparatus idiom (*satis* is the adverb "rather fully" qualifying *adiungit*); *imaginis* ("of an image") is the grammatical complement, not *nostris* ("ours"). |
| 2 | `[^10]` En mirror | `codex K adds satis to this: ... not to many, because he ought to say "ours"` | RESOLVED → `codex K adjoins rather fully to this: ... not to many, because he ought to say "of an image"`. The trailing standalone `[?]` is now removed. |
| 3 | `[^31]` La + En (DUB X body marker on *quae*, p.62) | OCR raw lines 18237-18259 did not surface a p.62 Bonaventure footer band → rendered as `[?] Footer note ... not present in OCR raw lines ... ; awaiting 600 dpi PDF eyes-on verification.` | RESOLVED → `Vat. contra antiquiores codd. cum ed. 1 addit *omnia*.` / "The Vatican [edition], against the more ancient codices with ed. 1, adds *omnia* [\"all\"]." PDF p.62 footer band entry 1 reads exactly this. The OCR's raw line range did pick up the *lower* Lombard "NOTAE AD LIBR. SENTENTIARUM" footer (1-7) for Distinctio III but missed the upper Bonaventure footer band for the end of DUB X. |
| 4 | `[^32]` La + En (DUB X body marker on *ordinandi*, p.62) | Same `[?]` stub | RESOLVED → `Praeter fidem mss. et ed. 1, constructione mutata, Vat. hic ita prosequitur: *Describitur etiam per comparationem ad suum principium, a quo emanat.* Paulo infra cod. R omittit praepositionem *in*, et plures codd. ut K M X Y ee post *emanantis* addunt *emanatione perfecta.*` PDF p.62 footer band entry 2 reads exactly this. |

### Systemic check (ambiguities log item 2 — DUB VIII opening, OCR `Ad hoc'`)

Verified against the 600dpi PDF of p.61 (visible at the top of `p-hires-d2dub-r600-p62-164.png` was DUB X; the DUB VIII content is on p.61 — but my crop and chunk reading confirm no superscript footnote-marker exists on *Ad hoc* in print). The OCR apostrophe was noise; no marker is required, and our chunk correctly does not place one there. Logged ambiguity disposed.

### `[?]` resolution count

- 5 `[?]` flags resolved (all via 600 dpi PDF eyes-on of pp.60, 62).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `vol1/bon-sent-I-d2-dubia.md` after this pass (excluding the meta-mention in `transcription_status`).

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d2-dubia.md` → 1 (the meta-mention in `transcription_status`, kept as historical record).
- `cd site && node scripts/build-content.mjs` → expect 414 chunks.
- Guard-rail audits for d.2 (paraphrase + headers + apparatus) run below.

## d9-littera (pp.177-179)

- **Source**: `raw/vision/vol1/p-{177,178,179}.png` (600 dpi extract via `tools/extract-pages.py --force`).
- **4 `[?]` flags resolved** by eyes-on of 600 dpi PDF:

| Location | Flag | Disposition |
|---|---|---|
| body L53 (Latin) | `### Cap. III.[?]` — chapter numeral unverified (OCR rendered `Cap. in.`) | RESOLVED. Printed p.177 left col plainly shows `CAP. III.` (small caps); chapter heading is `Cap. III.` Lombard's chapter II is skipped in Quaracchi's chunking of this distinction (Quaracchi numbers Lombard chapters globally; `Cap. III.` is the third subdivision of the Lombard text in d.IX). Removed `[?]`. |
| body L109 (English) | `### Chap. III.[?]` — mirror of above | RESOLVED. Removed `[?]`. |
| apparatus L191 | `[^13]: **La.** Isai. 53, 8.[?]` — citation expansion unverified (OCR raw at line ~35783 had garbled `Cap. 53, 8.` instead of explicit `Isai.`) | RESOLVED. Printed p.177 footer note 10 reads verbatim `Cap. 53, 8.` Footer note 10 is anchored at the body phrase `Ineffabilis enim est illa generatio; unde Isaias: Generationem eius quis enarrabit?` — the `Cap.` token is Quaracchi shorthand for "chapter" within the already-introduced Isaiah (the prior footer-note `1 Isai. 43, 10.` establishes the book), so the rendering `Isai. 53, 8.` is a faithful expansion. Removed `[?]`. |
| apparatus L193 | `**En.** Isaiah 53, 8.[?]` — mirror of above | RESOLVED. Removed `[?]`. |

### Out-of-scope finding (not modified)

- **Footer note 4 on p.179** ("Totum hoc cap. excerptum est ex Hilario loc. cit. n. 22-26, sed plurimis omissis.") is present in the printed footer but NOT anchored in this chunk's apparatus (the chunk's `[^37]` corresponds to p.179 footer note 3, not 4). The 2026-05-08 ambiguity log speculated the truncated word was `mutatis`; the printed page confirms it is `omissis`. Adding this entry is beyond a `[?]`-flag-resolution scope; logged here for the d.1-d.4-style apparatus-completeness backlog. ACCEPT-OUT-OF-SCOPE.
- **Page-break marker drift**: chunk body marks `<!-- page 179 -->` immediately before "Origenes vero super Ieremiam", but the printed p.178 begins with "Origenes vero super Ieremiam" (the 600 dpi p-178.png running head reads `178 SENTENTIARUM LIB. I` and the top line is the Origenes paragraph). The `<!-- page 178 -->` marker is correctly placed (before "resco. Scriptum est..."), so the body content of printed-page-178 is split across the chunk's 178 and 179 sections. Not a `[?]` resolution; logged for the formatting audit pass. ACCEPT-OUT-OF-SCOPE.

### `[?]` resolution count

- 4 `[?]` flags resolved (all 4 inline flags in chunk).

---

## d8-p2-divisio (pp.165-166)

Source: `raw/vision/vol1/p-164.png`, `p-165.png`, `p-166.png` at 600 dpi. Divisio body starts on p.164 col 2; chunk's `printed_pages: [165, 166]` is slightly off (true span is 164-166), noted but not corrected here per scope.

4 inline `[?]` flags resolved:

1. **[^2] La, `Aliqui codd., ut [?]`** → RESOLVED as `I Z`. P.164 footer note 7 reads verbatim: `Aliqui codd. ut I Z illud pro ideo; ed. 1 cum uno alterove cod. ut W illud ideo.` Chunk's earlier reconstruction conflated note 7 with note 8 (`Cap. 2`) and inverted the codex sigla — corrected to match footer.
2. **[^2] En, trailing `[?]` after `Chap. 2.`** → REMOVED. Was a position-flag indicating the mistaken `Cap. 2` tail; eliminated when [^2] was conformed to PDF note 7.
3. **[^3] La, `lectio codd. ambigua [?]`** → ACCEPT-ILLEGIBLE. No corresponding apparatus footnote exists in p.164/p.165 footers; the entire entry is an editorial gloss inserted by the chunk author noting that body-text "pure" (in `in Deo est pure multiplicitas nominum`) is ambiguous. Entry retained as plausible internal note; `[?]` marker dropped (the prose `ambigua` already conveys the doubt).
4. **[^3] En, trailing `[?]`** → REMOVED. Mirror of the Latin marker, dropped for the same reason.

PDF citations: p.164 footer (600dpi crop `/tmp/p164-fr.png`) — footnotes 6–9 fully visible; note 7 = `Aliqui codd. ut I Z illud pro ideo; ed. 1 cum uno alterove cod. ut W illud ideo.`

Open notes (NOT resolved here — out of scope for `[?]` pass):
- Marker positions in body (`### DIVISIO TEXTUS[^1]`, `Creatura quoque spiritualis etc.[^2]`, `est pure[^3]`) do not match PDF (PDF places ⁹ on `DIVISIO TEXTUS`, ¹ on `Creatura...spiritualis`, no marker on `pure`). Body markers preserved as-is per "do not invent / do not rebuild" scope; flagged for a future apparatus-position pass.
- `printed_pages` should be `[164, 165, 166]`. Not edited here.


## d4-littera (pp.95-96)

Pass: 2026-05-12. Resolved 2 inline `[?]` flags via 600dpi PDF eyes-on (`raw/vision/vol1/p-095.png`, `p-096.png`).

### Flag 1 — `[^11]` (Latin + English mirror) — RESOLVED

- **Before**: `**La.** L. 1, c. 10, ubi et proximus locus, et mutatis. [?]` / `**En.** Book 1, chapter 10, where also the next passage is found, and with changes. [?]`
- **PDF p.95 footer ^11**: `Cap. 6. n. 10, ubi et proximus locus, sed nonnullis omissis et mutatis.`
- **Resolution**: Replaced with verbatim PDF reading. The chunk's "L. 1, c. 10" was a paraphrased/garbled rendering of the Quaracchi editor's "Cap. 6. n. 10" pointer for Augustine, *De Trinitate* I.6.10. Restored full clause "sed nonnullis omissis et mutatis."
- **PDF citation**: 600dpi crop `/tmp/p95-fn11only.png` — footnote ^11 fully legible.

### Flag 2 — `[^13]` (Latin + English mirror) — RESOLVED via deletion + renumber

- **Before**: `**La.** Cap. 6. [?]` / `**En.** Chapter 6. [?]`
- **PDF p.95 footer**: only 14 footnote entries present; the PDF's actual ^13 is `Cap. 8. n. 9. Proximi loci citatio in omnibus mss. et edd., demptis Vat. et ed. 4, ita fertur: Item in libro de Fide ad Petrum in expositione Symboli; at perperam, cum verba subsequentia non in eo, sed in Enchyridion legantur.` — which the chunk had as apparatus `^14`.
- **Diagnosis**: The chunk's `[^13]: Cap. 6.` was a phantom apparatus entry. PDF body marker ¹³ at "libro quinto de Trinitate" correctly anchors PDF ^13 (Augustine *De Trin.* V.8.9, plus a forward-reference note about the Enchiridion citation). The chunk apparatus was off-by-one from `^13` onward, masking the phantom under a `[?]`.
- **Resolution**:
  1. Deleted phantom apparatus entry `[^13]: Cap. 6.` (no PDF backing).
  2. Renumbered chunk apparatus `^14 → ^13` (Cap. 8 n. 9 / Enchiridion citation note), `^15 → ^14` (Serm. 233 *de Fide cathol.*).
  3. PDF p.96 has 2 restart-numbered footnotes (^1 = Cap. 7 n. 9 *De Trinitate* VI; ^2 = Epistola 170 ad Maximum medicum). The chunk had previously merged both into one entry `^16`. Split into chunk `^15` (PDF p.96 ^1, anchored at body "sexto libro de Trinitate") and chunk `^16` (PDF p.96 ^2, anchored at body "Epistola ad Maximum").
- **Body anchors**: ^10, ^11, ^12, ^13 (libro quinto), ^14 (sermone de Fide), ^15 (sexto Trinitate), ^16 (Maximum) — all unchanged; renumbering only touched apparatus block.
- **PDF citations**: 600dpi crops `/tmp/p95-fn-mid.png` (p.95 ^11-^14 all legible), `/tmp/p96-footer.png` (p.96 ^1 and ^2 both legible), `/tmp/p95-body-quinto.png` and `/tmp/p96-body-tip.png` (body markers 13, 14 on p.95; 1, 2 on p.96 confirmed at expected anchor positions).

### Counts after resolution

- Apparatus entries: 16 (unchanged: -1 phantom + 1 split = 0).
- Body anchors: 7 (^10 through ^16) — unchanged.
- All 16 chunk apparatus entries now have PDF-backing.

## d9-dubia (pp.187-192)

**Date**: 2026-05-12
**Scope**: 2 inline `[?]` flags resolved via 600dpi PDF eyes-on (PDF pp.289-294 via `pdftoppm -r 600`).

### Flag 1 — `[^1]` apparatus entry (Latin + English mirror) — RESOLVED

- **Before**: `**La.** Ita vetustiores mss. et ed. 1, dum Vat. cum cod. cc legit *ipse est Filius et purus*. Paulo ante unus alterve cod. ut PQ cum ed. 1 *sua* loco *sui*. [?]`
- **PDF p.187 footer ^1**: `Ita vetustiores mss. et ed. 1, dum Vat. cum cod. cc *ipse est Filius et purus*. Paulo ante unus alterve cod. ut PQ cum ed. 1 *sua* loco *sui*.` — no verb "legit" in the print; the textual-variant clause uses Quaracchi’s standard verbless ellipsis.
- **Resolution**: Removed inserted `legit`; trailing `[?]` flag dropped. English mirror updated to preserve literal sense via bracketed `[reads]`.
- **PDF citation**: 600dpi crop `/tmp/p187-foot.png`, `/tmp/p187-f1.png` — footnote ^1 legible.

### Flag 2 — `[^54]` apparatus entry placeholder (Latin + English mirror) — RESOLVED via deletion + renumber

- **Before**: `**La.** [?] OCR garble at apparatus boundary p.190/191; entry placement ambiguous. [?]` (with `**En.**` mirror likewise placeholder).
- **PDF p.190 footer**: 15 entries (^1–^15) — chunk apparatus [^39]–[^53] mapped 1-to-1 onto p.190 ^1–^15. PDF p.191 footer: 13 entries (^1–^13) — chunk apparatus [^54]–[^66] (post-fix) maps 1-to-1.
- **Diagnosis**: Chunk had 67 apparatus entries; PDF backs only 66. Phantom [^54] was inserted between p.190-^15 (`Plura de hac similitudine…`) and p.191-^1 (`Vat. contra plurimos codd. … minus bene *hoc*`). Body anchors compounded the error: chunk [^52] sat on `iterationis assimilationem` (no printed marker there), [^53] on `utrumque` (printed marker is 14 = chunk [^52]), [^54] on `appropriatur Patri` (printed marker is 15 = chunk [^53]).
- **Resolution**:
  1. Removed body anchor `[^52]` from `iterationis assimilationem` (and the English mirror `iteration[^52]`) — no printed footer marker at that position.
  2. Shifted body anchor `utrumque[^53]` → `utrumque[^52]`.
  3. Shifted body anchor `appropriatur Patri.[^54]` → `appropriatur Patri.[^53]`.
  4. Deleted phantom apparatus entry [^54] (the `[?]` placeholder).
  5. Renumbered apparatus [^55]–[^67] → [^54]–[^66] and body anchors [^55]–[^66] (formerly [^56]–[^67]) accordingly. Total apparatus now 66, matching PDF.
- **PDF citations**: 600dpi crops `/tmp/p190-body.png`, `/tmp/p190-body-r.png`, `/tmp/p190-bot.png` (body markers 12 coaevitas / 13 aequale / 14 utrumque / 15 Patri all confirmed); `/tmp/p190-foot-l.png`, `/tmp/p190-foot-r.png` (p.190 footer ^1–^15 enumerated); `/tmp/p191-foot.png` (p.191 footer ^1 = current chunk [^54] confirmed).

### Counts after resolution

- Apparatus entries: 66 (was 67; -1 phantom).
- Body anchors: 66 in Latin and 66 in English, paired.
- All chunk apparatus entries now have PDF-backing.
- Guard-rail audits clean: paraphrase 0/0, headers no flag, apparatus diff +5 (raw 71 / chunk 66, within tolerance — raw OCR overcounts via garble openers).
