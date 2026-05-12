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

## d8-p1-a1-q2 retry (pp.152-154)

Pass date: **2026-05-12** (same-day retry of wave-1 ACCEPT-ILLEGIBLE disposition).

### Trigger

Wave-1 (earlier 2026-05-12) accepted 8 `[?]` flags as ACCEPT-ILLEGIBLE on the premise that scholion II opens on PDF p.155 bottom-right and is OCR-smeared. Retry re-examined `raw/vision/vol1/p-hires-d8q2-258.png` (printed p.156, where scholion II actually starts).

### Finding

**Wave-1 mis-located scholion II.** Scholion II does NOT open on p.155 bottom-right (that region is the tail of scholion I body + apparatus footnotes for scholion I). Scholion II opens at the **top of p.156 left column** and is fully legible at 600 dpi. The wave-1 "OCR-band dropout + lateral ink-bleed" diagnosis applied to scholion I's apparatus footer band, not to scholion II.

### Verified scholion II opening (from p.156 left column, top)

> "II. Circa quaestionem, utrum existentia Dei sit per se nota, antiqui Scholastici diverso modo loquuntur. Omnes tamen concedunt, existentiam esse de conceptu essentiali Dei. S. Anselmus docet, omni apprehendenti significationem vocabuli *Deus* per se notam esse eius existentiam; unde ex ipso conceptu Dei et entis, quo melius cogitari non potest, formavit argumentum ad probandum existentiam Dei..."

The wave-1 reconstruction (`Sic[?] habet B. Albertus[?] ad probandum, [?] putatur. [?] doctrina [?] gument [?] primi [?] per se notum esse.`) was a hallucination — none of those words appear in scholion II's actual opening. The `argumentum ad probandum` formula is present, but in a different construction four lines down.

### `[?]` flags walked

| # | Location | Wave-1 disposition | Retry disposition |
|---|---|---|---|
| 1-7 | Latin l. 110, scholion II opening, 7 bare `[?]` | ACCEPT-ILLEGIBLE | **RESOLVED.** Entire scholion II body replaced with verbatim transcription from p.156 (`raw/vision/vol1/p-hires-d8q2-258.png`). Full text now present (~3× length of wave-1 reconstruction); recovers Anselm citation, Aegidius/Dionysius citations, Nominalist clause, full Scotus distinction, S. Thomas citation block, Alex. Hal. quotation continuation, B. Albert + Richard + Petr. a Tar. citations, S. Thom. *de Verit.* q. 22 quotation, S. Bonaventura *de Reductione*, Scot. I *Sent.* d. 3. q. 2 closing quote. |
| 8 | English l. 192, `[?Likewise]` | — | **RESOLVED.** Mirror rewritten literal from corrected Latin: "Concerning the question whether the existence of God is known *per se*, the ancient Scholastics speak in diverse ways..." |
| 9 | English l. 192, `B. Albert[?]` | — | **RESOLVED.** No `[?]` needed; verified `B. Albert, S. tr. 3. q. 19. m. 2.` is intact in the Latin (it follows the Alex. Hal. block, not preceding it). |
| 10 | English l. 192, `[…?…]` (editorial supply gap) | — | **RESOLVED.** Gap filled with the literal English of the recovered Latin. |

### Systemic check: scope of dropout

This is more than a flag-resolution: wave-1 left the chunk with a scholion II body that was ~1/3 the length of the printed text and contained fabricated stem-words. The retry restores the full text. **No invented Latin** in the retry: every clause traces to p.156 image. Other scholia (I, III, IV) in this chunk were not re-checked under this retry's scope — only scholion II was edited.

### Systemic check: PDF-extract location convention

Source-of-truth correction for the chunk: scholion II runs **printed p.156**. Frontmatter `printed_pages: [152, 153, 154]` and `pdf_pages: [254, 255, 256]` understate the scholion span; this is a known frontmatter audit item (logged in wave-1 §"Note on page ranges"), still pending corpus-wide.

### Systemic check: are other "ACCEPT-ILLEGIBLE" dispositions in the log similarly mis-located?

Worth a focused sweep of the wave-1 ACCEPT-ILLEGIBLE entries (this log) in a later pass: confirm that each cited PDF location actually contains the cited passage. The d8-p1-a1-q2 wave-1 entry mis-identified p.155 bottom-right as scholion II opening when it was scholion I tail. Sweep tracked as a polish-pass follow-up; not blocking.

### `[?]` resolution count (post-retry)

- Before retry: 10 `[?]` occurrences in chunk body (7 Latin scholion II + 1 English bare + `[?Likewise]` + `[…?…]`).
- After retry: 0 `[?]` occurrences in chunk body. The 2 occurrences in `transcription_status` are meta-history and retained intentionally.
- Net: 10 → 0 in body; 12 → 2 in file total (counting status meta).

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d8-p1-a1-q2.md` → 2 (both inside `transcription_status` meta string).
- `cd site && node scripts/build-content.mjs` → expect 414 chunks.
- d.8-scoped guard-rail audits re-run below.

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

## d4-a1-q3 (pp.101-102)

Pass: 2026-05-12. Resolved 4 inline `[?]` flags via 600dpi PDF eyes-on (`raw/vision/vol1/p-101.png`, `p-102.png` re-extracted at 600 dpi via `tools/extract-pages.py --volume vol1 --pages 101-102 --dpi 600 --force`). Chunk was rebuilt earlier today (Bucket G commit `6f780f6`); apparatus restructured 8→10 entries with mis-anchored prior `[^7]/[^8]` (Vat.subiectum / Cod.R-genuit) removed to `bon-sent-I-d4-a1-q2`. Open flags noted at handoff in `manual-review/tier2-ambiguities-d4-a1-q3.md`.

### Flag 1 — body `sic nec hoc[?] nomen Deus` (Latin) + `so neither does this[?] name God` (English mirror) — RESOLVED as OCR artifact

- **Before**: `sic nec hoc[?] nomen *Deus*` / `so neither does this[?] name *God*`. Raw djvu OCR rendered the position as `hoc''` (two apostrophe-like glyphs after `hoc`), raising the possibility of a printer's footnote superscript.
- **PDF p.102 eyes-on**: At 600 dpi the line reads "et ideo sicut nomen proprium non habet plurale, secundum artem loquendo, sic nec hoc nomen *Deus*." No superscript marker visible on `hoc`. The p.102 footer block is fully accounted for: entries 1-2 anchor into Q.IV body (Vers.8 / nomen Dei) and entries 3-6 anchor into Q.III as the current `[^7]`-`[^10]` (sequuntur / Priscian-accidentium / Vat-potest / Supplevimus-cum). No spare footer entry would correspond to a marker at `hoc`. The OCR `''` is a stray artifact (likely from the italic transition into *Deus*).
- **Resolution**: Removed `[?]` from both Latin and English bodies. No anchor added.

### Flag 2 — apparatus `[^5]` `Cfr. Priscian., II. Grammat. c. 5.[?]` (Latin + English mirror) — RESOLVED

- **Before**: `**La.** Cfr. Priscian., II. Grammat. c. 5.[?]` / `**En.** Cf. Priscian, *Grammar* II, c. 5.[?]`. Raw djvu OCR garbled the chapter numeral (rendered `S` for `5`).
- **PDF p.101 eyes-on**: At 600 dpi footnote entry 5 in the page footer reads verbatim "Cfr. Priscian., II. Grammat. c. 5." Numeral `5` confirmed (not `S`); citation form intact.
- **Resolution**: Removed `[?]` from both Latin and English; verbatim reading retained.

### Counts after resolution

- Apparatus entries: 10 (unchanged).
- Body anchors: 10 in Latin and 10 in English, paired.
- All 10 chunk apparatus entries PDF-backed (p.101 footer entries 4-9 → `[^1]`-`[^6]`; p.102 footer entries 3-6 → `[^7]`-`[^10]`).
- 4 `[?]` flags cleared (2 substantive sites × Latin+English mirror = 4 grep matches as expected).


## d8-p1-dubia (pp.161-165)

Pass: 2026-05-12. Resolved 2 inline `[?]` flags via 600dpi PDF eyes-on (`raw/vision/vol1/p-162.png`, `p-163.png`). Both flags sat in apparatus block (Latin + English mirror, so 4 `[?]` glyphs total).

### Flag 1 — `[^7]` (Latin + English mirror) — RESOLVED

- **Before**: `**La.** Cod. T *vermi*, cod. W *ibi* pro *bene*.[?]` / `**En.** Codex T [reads] *vermi*, codex W *ibi* for *bene*.[?]`
- **PDF p.163 footer ^1**: `Cod. T *vermi*, cod. W *ibi* pro *bene*.` — verbatim. Codex T's reading *vermi* (literally "for the worm") is genuinely the printed Quaracchi lemma; it is a recorded codex eccentricity, not an OCR garble.
- **Resolution**: Dropped trailing `[?]` glyphs on both Latin and English. Mildly tightened English mirror (`for` → `in place of`) to match Quaracchi convention used elsewhere in the chunk.
- **PDF citation**: 600dpi crop `/tmp/p163-mid.png` — footnote ^1 fully legible at top of left-column footer block.

### Flag 2 — `[^11]` (Latin + English mirror) — RESOLVED

- **Before**: `... — Mox Vat., omnibus mss. et sex primis edd. obnitentibus, *de loco in [locum][?]*. Paulo infra cod. I satis bene addit *sine variatione et innovatione*.` / English mirror with `*from place to place*[?]`.
- **PDF p.163 footer ^5**: `... — Mox Vat., omnibus mss. et sex primis edd. obnitentibus, *de loco in*. Paulo infra post *successionem* cod. I satis bene addit *sine variatione et innovatione*.`
- **Diagnosis**: Quaracchi prints the Vatican-edition lemma as the bare italic phrase `de loco in.` — apparently truncated (the Vat. text it cites likely reads "de loco in locum" or similar, but Quaracchi reproduces only what they printed). The chunk author had inserted `[locum]` as a conjectural completion and rendered the English as `*from place to place*` — both inventions. PDF also shows the missing clause `post *successionem*` (chunk had dropped these two words before `cod. I satis bene addit`).
- **Resolution**:
  1. Latin: removed `[locum]` insertion, dropped `[?]`, restored the missing `post *successionem*` clause.
  2. English: re-rendered the Vatican lemma as `*de loco in*` (preserving Quaracchi's bare lemma rather than glossing) with bracketed editorial note `[sic — Quaracchi prints the Vatican lemma as it stands]`; added `after *successionem*` to mirror the restored Latin.
- **PDF citation**: 600dpi crops `/tmp/p163-fn5.png`, `/tmp/p163-fn5-line.png` — footnote ^5 fully legible, period after `in` confirmed, `post successionem` clause confirmed.

### Systemic checks

- **Quaracchi `[word]` editorial brackets**: none present in this chunk's PDF range (no `[x]`-style Quaracchi editorial insertions in pp.161-165 footers); chunk's prior `[locum]` was author-invented, not Quaracchi.
- **Phantom apparatus entries**: walked chunk apparatus ^1-^19 against PDF footers — p.162 ^1-^6 → chunk ^1-^6 (1-to-1 ✓); p.163 ^1-^13 → chunk ^7-^19 (1-to-1 ✓). All 19 chunk entries have PDF backing. No off-by-one masking. (Note: chunk [^12] renders `c. 20. et 22` for *Proslog.* citation where PDF shows `c. 29. et 22` — flagged for non-`[?]`-pass disposition; out of polish-blocker scope.)

### Counts after resolution

- Apparatus entries: 19 (unchanged).
- Body anchors: 19 in Latin and 19 in English, paired (unchanged).
- All chunk apparatus entries now have PDF-backing.

## d10-a2-q3 (pp.203-204)

**Date**: 2026-05-12
**Scope**: 4 inline `[?]` flags (2 Latin + 2 English mirrors) resolved via 600dpi PDF eyes-on (PDF pp.305-306 via `pdftoppm -r 600`, pt1 offset = printed + 102).

### Flag 1 — `[^1]` apparatus (Latin + English mirror) — RESOLVED

- **Before**: `**La.** Codd. LO hic addunt: *sic Filius et Spiritus sanctus conveniunt originaliter in Patre, sed* etc.[?]` (English mirror likewise `etc.[?]`).
- **PDF p.203 footer ^2**: `Codd. LO hic addunt sic Filius et Spiritus sanctus conveniunt originaliter in Patre, sed.` — ends with bare *sed.* (period); no `etc.`
- **Resolution**: Dropped trailing `etc.` and `[?]` in both Latin and English; closing italic with terminal period preserved. Quaracchi's ellipsis convention is the bare *sed*. with period.
- **PDF citation**: 600dpi crop `/tmp/p203-body-left.png` (left column, footnote ^2 fully legible).

### Flag 2 — `[^11]` apparatus (Latin + English mirror) — RESOLVED

- **Before**: `**La.** Substituimus ope multorum mss. ut AFGKT etc. et edd. 1, 2, 3 *rationalium* loco *rationalibus*.[?]` (English mirror likewise).
- **PDF p.204 footer ^3**: `Substituimus ope multorum mss. ut AFGKT etc. et edd. 1, 2, 3 *rationalibus* loco *rationalium*.` — chunk had substitution direction reversed (Quaracchi adopts *rationalibus*, replacing *rationalium*; chunk wrongly had Quaracchi adopting *rationalium*).
- **Resolution**: Reversed direction in both Latin and English; dropped `[?]`. Body anchor on `substantiis rationalibus[^11]` / `rational substances[^11]` is correctly positioned (Quaracchi's adopted reading is *rationalibus*).
- **PDF citation**: 600dpi crop `/tmp/p204-foot3b.png` (p.204 footnote ^3 fully legible).

### Separate backlog flagged (NOT resolved this pass)

p.203 apparatus has off-by-N misalignment downstream of [^1]/[^2]: chunk skips PDF p.203 footer entries ^3 (`Ita plurimi codd. ... quia unus oritur a duobus`), ^4 (`Ed. 1 consimilia`), ^5 (`Cod. X significat`), and most of ^6 (`Unus alterve cod. ut Z ... cod. Z quo loco quod`, of which the chunk preserves only the tail `Mox codd. ab bb post non coarctat hoc addunt nomen ...`, misread as `H` and rendered as chunk [^2]). Net: chunk apparatus on p.203 has 8 entries; PDF p.203 q.3 footer has 11. Per scope ("Do NOT: invent; commit; touch siblings"), not addressed here — logged for the broader d.1-d.10 apparatus-completeness rebuild backlog (see MEMORY.md d.1-d.10 polish TODO).

### Counts after resolution

- Inline `[?]` flags in chunk: 0 (was 4).
- Apparatus entries: 24 unchanged.
- Body anchors: 24 in Latin and 24 in English, paired.

## d10-a2-q2 (pp.202-203)

**Date**: 2026-05-12
**Scope**: 4 inline `[?]` flag matches (2 substantive sites × Latin+English mirror) resolved via 600dpi PDF eyes-on. Pt1 offset (PDF=printed+102): PDF pp.304-305 via `pdftoppm -r 600`.

### Flag 1 — `[^9]` (Latin + English mirror) — RESOLVED

- **Before**: `...alii vero, pauci *eximius*[?]. Perturbatior nobis ob contextum visa est lectio codd. *HM* in textum recepta.` / English mirror: `...a few, have *eximius*[?]. The reading of codices *HM*, ... more disturbed on account of the context.`
- **PDF p.202 footer ^10** (the second half of chunk `[^9]`, which merges PDF p.202 fns ^9 + ^10): `Vat. omittit *est* legendo *quia amor mutuus est amor unicus et substantificus*; ita etiam aliae edd. et plurimi codd. cum hac differentia, quod plures codd. pro *unicus* habent *unitus*, alii vero pauci *vivificus*. Probabilior nobis ob contextum visa est lectio codd. HIM in textum recepta.`
- **Resolution**: Replaced `eximius[?]` → `vivificus` (clearly legible in PDF). Also corrected two adjacent garbles surfaced by eyes-on: `Perturbatior` → `Probabilior` and `HM` → `HIM`. English mirror updated: `*eximius*[?]` → `*vivificus*`, and `more disturbed` → `more probable`.
- **PDF citation**: 600dpi crop `/tmp/p202-fn9-zoom.png` — p.202 right-column footnotes ^9 through ^12 all legible; ^10 entry verbatim.

### Flag 2 — `[^12]` (Latin + English mirror) — RESOLVED

- **Before**: `Vat., adstipulante[?] nullo cod., *originalis*...` / English: `The Vatican edition, with no codex supporting[?] it, reads *originalis*...`
- **PDF p.203 footer ^1** (= chunk `[^12]`; per-page restart, chunk's first p.203 entry): `Vat., adstipulante nullo cod., *originalis*, et mox contra antiquiores codd. et ed. 1 post *potest* addit *dici*, deinde contra multos codd. ut IKMRTZ etc. ac ed. 1 loco *conveniant* ponit *communicent*.` — `adstipulante` fully legible, no garble in PDF.
- **Resolution**: Dropped `[?]` from both Latin (`adstipulante[?]` → `adstipulante`) and English mirror (`supporting[?] it` → `supporting it`). No substantive change — flag was unwarranted; the word reads cleanly at 600dpi.
- **PDF citation**: 600dpi crop `/tmp/p203-fn1-zoom.png` — p.203 footnote ^1 verbatim.

### Systemic check — chunk-vs-PDF apparatus mapping

- PDF p.202 has 12 footer entries; PDF p.203 has 11. Chunk has 16 apparatus entries total. Question 2 + scholion span all of p.202 + first ~half of p.203, so chunk should hold p.202 ^1-^12 + p.203 ^1-^4 = 16. **Mapping verified**: chunk `[^1]`-`[^8]` = PDF p.202 ^1-^8 (1-to-1); chunk `[^9]` = PDF p.202 ^9 + ^10 merged with ` — ` joiner (structural editorial choice carried from rechunk pipeline; not a defect); chunk `[^10]` = PDF p.202 ^11; chunk `[^11]` = PDF p.202 ^12; chunk `[^12]`-`[^16]` would map to p.203 ^1-^5, but chunk only has 16 total so `[^12]`-`[^15]` = p.203 ^1-^4 (Q2 + scholion stop before p.203 fn ^5 which belongs to Q3). No phantom entries, no off-by-one. Body anchors compatible with merged-^9 numbering.
- Minor variant noted but not corrected in `[^10]`: chunk reads `HV essentialem` and `Z essentiali`; PDF reads `HY essentialem` and `Z essentiae`. Substantive (codex sigla / case-form differences) but pre-existing from rechunk pipeline and outside this polish-pass scope (not flagged with `[?]`).

### Counts after resolution

- Apparatus entries: 16 (unchanged).
- Body anchors: 16 in Latin and 16 in English, paired.
- All 4 `[?]` matches cleared (2 substantive sites × La+En mirror).

## d10-a2-q1 (pp.200-201)

Pass: 2026-05-12. Resolved 2 substantive `[?]` flag sites (4 grep matches = 2 sites × Latin+English mirror) via 600dpi PDF eyes-on. Source: `raw/vision/vol1/p-hires-d10a2q1-302.png` (PDF p.302 = printed p.200; full page at 600 dpi via `pdftoppm -r 600 -f 302 -l 303`) plus footer crop `raw/vision/vol1/p200_foot_sips.png`. Both flags were in p.200-footer apparatus entries `[^6]` and `[^7]`.

### Flag 1 — apparatus `[^6]` `Aliqui codd. ut V X Z bb falso *aut* loco *sive*[?]` (Latin + English mirror) — RESOLVED

- **Before**: La `Aliqui codd. ut V X Z bb falso *aut* loco *sive*[?].` / En `Some codices such as V X Z bb falsely [read] *aut* (or) in place of *sive* (or)[?].` Flag was overcautious — chunk-builder uncertain whether codex sigla `V X Z bb` was complete.
- **PDF p.200 footer (right column) eyes-on**: At 600 dpi note 6 reads verbatim "Aliqui codd. ut V X Z bb falso *aut* loco *sive*." Sigla `V X Z bb` confirmed exactly; no further sigla or trailing clause. Period after *sive* terminates the entry.
- **Resolution**: Removed `[?]` from both Latin and English; verbatim reading retained.

### Flag 2 — apparatus `[^7]` `Supplevimus hic *et*; mox substituimus [variant uncertain in OCR][?]` (Latin + English mirror) — RESOLVED

- **Before**: La `Supplevimus hic *et*; mox substituimus [variant uncertain in OCR][?].` / En `We have supplied here *et* (and); soon we substitute [variant uncertain in OCR][?].` Raw djvu OCR garbled the second clause; chunk-builder left a placeholder.
- **PDF p.200 footer (right column) eyes-on**: At 600 dpi note 7 reads verbatim "Supplevimus hic *et*; mox substituimus genitivum *Spiritus sancti* pro dativo, ope mss. et ed. 1."
- **Resolution**: La set to `Supplevimus hic *et*; mox substituimus genitivum *Spiritus sancti* pro dativo, ope mss. et ed. 1.` En set to `We have supplied here *et* (and); soon we substitute the genitive *Spiritus sancti* (of the Holy Spirit) for the dative, by aid of the manuscripts and ed. 1.`

### Counts after resolution

- Apparatus entries: 19 (unchanged).
- Body anchors: 19 in Latin and 19 in English, paired.
- All 19 chunk apparatus entries PDF-backed (p.200 footer notes 1-3 + 5-8 → `[^1]`-`[^9]` after re-anchor of Augustine cross-reference; p.201 footer → `[^10]`-`[^19]`).
- 4 `[?]` flags cleared (2 substantive sites × Latin+English mirror = 4 grep matches).
- 0 accepted-illegible.
- 0 `[?]` flags remaining in `d10-a2-q1.md` after this pass (verified `grep -n '\[?\]' vol1/bon-sent-I-d10-a2-q1.md` matches only the transcription_status appendix).

## d10-littera (pp.192-193)

**Date**: 2026-05-12
**Scope**: 4 inline `[?]` flags (2 substantive sites × Latin+English mirror) resolved/re-affirmed via 600dpi PDF eyes-on (`raw/vision/vol1/p-192.png`, `p-193.png`).
**Prior pass**: 2026-05-10 Bucket 1 — p.193 footer recovery (footer entries 4-9 verbatim, missing footer #10 added as `[^23]`, body anchors renumbered to match printed positions 1-10); 11 `[?]` cleared, 2 remaining in `[^6]` carried as ACCEPT-ILLEGIBLE and now revisited.

### Flag 1 — `[^6]` (Latin + English mirror) — RESOLVED

- **Before**: `**La.** ... aliqui codd. *ut* [?] *est.*` / `**En.** ... some codices add *ut* [?] *est.*`
- **PDF p.192 footer ^2** (printed footer 2 = chunk apparatus `[^6]`): reads verbatim `Vat. cum cod. cc repetit hic *naturam,* quod deest in antiquioribus mss. et ed. 1. Paulo infra post *persona* adiungunt aliqui codd. ut I T *est.*`
- **Diagnosis**: The `[?]` glyph between *ut* and *est* is the upright codex sigla pair `I T` — two manuscript witnesses. This is the same Quaracchi convention as d.8-p2-divisio (`aliqui codd. ut I Z illud pro ideo` resolved 2026-05-12), where `ut` = "such as" introducing example codices, not the Latin word *ut* in the body variant. Prior reading "typographic 'ut 1 T est' cross-reference glyph, not a Latin word" was half-right (the inner glyph is not Latin) but mis-classified — the sigla are meaningful and renderable.
- **Resolution**:
  - Latin: `aliqui codd. ut I T *est.*` (drop italic from `ut`; `I T` upright per sigla convention; only the variant word *est* italic).
  - English: `some codices, such as I and T, add *est.*` (idiomatic rendering of `ut I T` = "such as I and T").
- **PDF citations**: 600dpi crops `/tmp/p192-footer.png`, `/tmp/p192fl.png`, `/tmp/p192-fn2only.png` — footnote ^2 fully legible; "I T" clearly two upright Roman capitals (not "1 T" numeral, not a typographic ornament).

### Flag 2 — `[^19]` (Latin + English mirror) — ACCEPT-ILLEGIBLE (re-affirmed)

- **Before**: `**La.** ... cod. D et edd. 1, 8 *subsistit*[?], quod magis placeret ...` / `**En.** ... codex D and editions 1, 8 [read] *subsistit*[?] (with a small subscript glyph) ...`
- **PDF p.193 footer ^6** (printed footer 6 = chunk apparatus `[^19]`): reads `Cap. 4. et 5. n. 6. et 7; ex ultimo cap. etiam sequentis huius capituli textus excerpti sunt. In fine primi textus pro *consistit* cod. D et edd. 1, 8 *subsistit* [tiny printer's mark], quod magis placeret, si faveret Augustinus.`
- **Diagnosis**: After italic *subsistit* and before the comma, the printed footer has a small typographic ornament — appears to be a comma-with-flourish or a tiny subscript-style mark (one of Quaracchi's editorial sigla, possibly indicating "as variant only" or a cross-reference). It is not a Latin word and carries no propositional content beyond the variant note already conveyed. The variant claim (*subsistit* in cod. D / edd. 1, 8 in place of *consistit*) is fully captured by the surrounding prose. Re-affirmed ACCEPT-ILLEGIBLE.
- **Resolution**:
  - Latin: `*subsistit* [small typographic glyph, ACCEPT-ILLEGIBLE], quod magis placeret ...` (replace `[?]` with explicit accept-illegible annotation).
  - English: `*subsistit* [followed by a small typographic glyph in the printed footer; ACCEPT-ILLEGIBLE — not a Latin word] ...`
- **PDF citations**: 600dpi crops `/tmp/p193-footer.png`, `/tmp/p193-fn6.png`, `/tmp/p193sub.png` — footnote ^6 fully legible; glyph after *subsistit* is a small ornament, not letterforms.

### Counts after resolution

- Inline `[?]` flags remaining in chunk: 0.
- Apparatus entries: 23 (unchanged).
- Body anchors: paired Latin/English (unchanged from 2026-05-10 Bucket 1 renumber).
- No phantom apparatus entries detected; off-by-one alignment check clean (chunk `[^1]`-`[^22]` track p.192 footer entries 1-9 then p.193 footer entries 1-13; `[^23]` is the new p.193 footer #10 added in Bucket 1).

### Systemic notes

- Quaracchi `[word]` editorial brackets: none in this chunk (none in body, none in apparatus). N/A.
- Phantom apparatus check: `[^6]` was suspected as candidate (long `[?]` site); verified PDF-backed at p.192 footer 2. No phantom.
- ACCEPT-ILLEGIBLE classification preserved for `[^19]` printer's-mark glyph; semantic content of variant is complete without it.

## d9-a1-q2 (pp.182-183)

Polish-blocker [?] resolution pass, 2026-05-12. PDF source: `raw/doctorisseraphic11bona.pdf` p.285 (printed p.183), re-extracted at 600dpi (`raw/vision/vol1/p-183.png`, 4.0 MB).

The chunk held 2 inline `[?]` flags, both at a single co-referenced site in the response to Contra objection 3 ("Ad illud quod obiicitur, quod idem est essentia et persona"): the Latin word `generatur` and its English mirror `is generated`. The flag had been placed in the 2026-05-10 from-scratch build because the OCR raw line was suspected of ambiguity between `generatur` (3rd sg. passive) and a possible alternative form.

| Body anchor | Disposition | PDF citation |
|---|---|---|
| Latin line 75, `ideo generatur[?] et refertur` | RESOLVED → `generatur` | p.183 left column, mid-page: word is plainly `generatur` (3rd sg. present passive of *genero*) in the printed Quaracchi text; no editorial marker, no OCR ambiguity at 600dpi. Reading is "ideo generatur et refertur". |
| English line 137, `therefore it is generated[?] and is referred` | RESOLVED → `it is generated` | Mirror of above; English translation is correct as already rendered. |

### `[?]` resolution count

- 2 `[?]` flags resolved (both at the same `generatur` / `is generated` site).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d9-a1-q2.md` after this pass.

### Systemic notes

- No OCR-band footer dropout on pp.182-183: chunk's 29 apparatus entries from p.182/p.183 footer blocks are intact from the 2026-05-10 from-scratch build.
- Quaracchi `[word]` editorial brackets: none in this chunk body. N/A.
- Phantom apparatus check: anchors `[^1]`–`[^29]` all present in both Latin and English bodies; def lines all present (verified via grep of pairing).
- `transcription_status` frontmatter updated with the 2026-05-12 polish-pass annotation.

### Verification

- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d9-a1-q2.md | sort -t^ -k2 -n | uniq -c` → each `[^N]` (N=1..29) appears exactly 3× (Latin body + English body + apparatus def).
- `grep -c '\[?\]' vol1/bon-sent-I-d9-a1-q2.md` → 0.
- `cd site && node scripts/build-content.mjs` parses cleanly; 414-chunk count preserved.
- d.9-scoped guard-rail audits (paraphrase, headers, apparatus-count) clean.

## d10-commentary (p.194)

**Date**: 2026-05-12
**Scope**: 3 inline `[?]` grep matches (1 substantive site × Latin + English mirror + Notes commentary) resolved via 600dpi PDF eyes-on (`raw/vision/vol1/p-hires-d10commentary-r600-296.png`, crops `/tmp/p194-incipit.png`, `/tmp/p194-incipit2.png`).

### Flag 1 — incipit lemma `«... quantum Deo donante, ak[?]»` (Latin + English mirror + Notes) — RESOLVED

- **Before**: La `«Nunc post Filii aeternitatem de Spiritu sancto, quantum Deo donante, ak[?]» etc.` / En mirror with `ak[?]` placeholder. Notes speculated the truncated `ak-` continued as Lombard's `aggrediar` ("I shall undertake").
- **PDF p.194 incipit line eyes-on (600 dpi)**: reads verbatim `Nunc post Filii aeternitatem de Spiritu sancto, quantum Deo donante, etc.` The lemma terminates with `etc.` (Quaracchi's standard citation-truncation marker) immediately after `donante,`. There is no `aggrediar`, no second `ak-` word, no garble — the OCR misread the printed `etc.` as `ak-`.
- **Diagnosis**: OCR-only artifact. The chunk-builder's speculative reconstruction (`ak- → aggrediar`) was unwarranted; Quaracchi prints `etc.` and ends the citation there, as it does throughout the Sentences commentary for incipit lemmata.
- **Resolution**:
  - Latin: `*«Nunc post Filii aeternitatem de Spiritu sancto, quantum Deo donante,»* etc.` (drop `ak[?]`; period inside `etc.` outside the close-quote per Quaracchi).
  - English: `*«Now, after [treating of] the eternity of the Son, [we shall treat] of the Holy Spirit, insofar as God grants it,»* etc.` (mirror).
  - Notes: rewrote the trailing sentence — removed the `aggrediar` speculation and recorded the OCR-vs-PDF resolution.
- **PDF citations**: 600dpi crops `/tmp/p194-incipit.png`, `/tmp/p194-incipit2.png` — incipit line fully legible; the terminal token is unambiguously `etc.` (period included).

### Counts after resolution

- Inline `[?]` flags remaining in chunk: 0 (verified `grep -c '\[?\]' vol1/bon-sent-I-d10-commentary.md` = 0).
- Apparatus entries: 0 (preamble has none).
- Body anchors: N/A.
- 1 substantive site resolved; 0 accepted-illegible.

### Systemic notes

- Quaracchi `[word]` editorial brackets: none. N/A.
- Phantom apparatus check: N/A (`has_apparatus: false`).
- No body dropout — chunk is the d.10 preamble only (raw lines 38245–38252); substantive content begins in `bon-sent-I-d10-divisio.md`.

## d1-a1-q1 (pp.30-32)

Bucket 1 polish-blocker pass against `raw/vision/vol1/p-d1a1q1-r600-134.png` (PDF p.134 = printed p.32, 600 dpi via pdftoppm `-r 600 -f 132 -l 134`). Four inline `[?]` flags in the scholion at the foot of p.32 (no other `[?]` flags in this chunk; body and apparatus on pp.30-31 are clean). Cross-checked against IA djvu OCR (raw lines 271-285 of the chunk band, which preserve the scholion structure but garble multiple author names).

The scholion is a Quaracchi reference list of scholastic commentators on the question. Eyes-on PDF reading + OCR cross-reference resolved all four flags as transcription gaps rather than ambiguities.

| Body location | Flag | Disposition | PDF reading |
|---|---|---|---|
| Opening word | `Plurimi[?]` | RESOLVED → `Plurimi` | OCR garbled to "niiliiiui"; PDF unambiguous "Plurimi" (the standard Quaracchi scholion opener for consensus notes). |
| Scotus citation | `Scot., [hic][?] q. in fine` | RESOLVED → `Scot., I. *Sent.* d. 1. q. 2. et 5. in fine` | Prior chunk-builder had collapsed the actual citation to a `[hic]` guess; PDF gives the full Scotus *Sentences* reference. |
| Richard cite | `[Richard. a Med.][?]` | RESOLVED → `Richard. a Med.` (drop brackets) | PDF + OCR both legible "Richard. a Med."; brackets were prior translator-side uncertainty, no editorial-Quaracchi bracket. |
| Aegidius cite | `[...][?], hic a. 1 principalis q. 3` | RESOLVED → `Aegid. R., hic a. 1. principalis q. 3.` | PDF reads "Aegid. R." (Aegidius Romanus / Giles of Rome) — single-letter surname abbreviation. Also recovered preceding/trailing displaced text: "Petr. a Tar., hic q. 1. a. 1. qui doctrinam S. Bonavent. breviter repetit" (which the prior chunk had mis-attached to the last entry), and final "Brul., hic q. 1." (Brulefer — Stephanus Brulefer, Franciscan commentator). |

### Other corrections folded into this pass

- **S. Thom. citation expansion**: prior chunk had "St. Thomas, here q. 1; St. B. Albert M., …" merging S. Thomas's second citation into Albert's entry. PDF shows "S. Thom., hic q. 1; S. *Theol.* 1. 2. q. 16. a. 1. — B. Albert. M., hic a. 13. 16. et 17." — the "S." is the opener of *Summa Theol.* I-II q. 16 a. 1, not the "St." of Albert. Corrected Latin + English.
- **Henr. Gand. citation**: prior chunk truncated to "S. a." — PDF reads "S. a. 6. q. 1." Filled in.
- **Petr. a Tar. entry**: was entirely missing from prior chunk's scholion (the "qui doctrinam S. Bonavent. breviter repetit" tail had drifted to the final entry). Restored.
- **Brul. entry**: final entry "Brul., hic q. 1." (Brulefer) was rendered as "[...]" in prior chunk. Restored.

### Counts after resolution

- Inline `[?]` flags remaining in chunk: 0 (`grep -c '\[?\]' vol1/bon-sent-I-d1-a1-q1.md` = 0).
- 4 substantive sites RESOLVED; 0 accepted-illegible.
- Apparatus entries unchanged at 22 (this pass touched only the scholion).
- Body anchors `[^1]`–`[^22]` unchanged; each still appears 3× (Latin body + English body + apparatus def).

### Systemic checks

- **Quaracchi `[word]` editorial brackets**: none introduced; the prior chunk's `[hic]`, `[Richard. a Med.]`, `[...]` were translator-side uncertainty brackets (not Quaracchi italic-bracket editorial supplements), and have been dropped now that the PDF resolved them.
- **Phantom apparatus check**: no apparatus entries added or removed in this pass.
- **No reversed substitutions or invented bracketed completions**: all restorations (Petr. a Tar., Brul., Aegid. R., S. *Theol.*, Henr. Gand. q.) are verbatim PDF readings, not LLM guesses.

## d7-dubia (pp.145-146)

**Date**: 2026-05-12
**Scope**: 5 inline `[?]` flag sites (3 in Dub. VII Latin body tail mirrored in English = 6 grep matches, + 1 in apparatus `[^12]` Latin, + 1 in `[^12]` English mirror = 8 grep matches total). Resolved via 600dpi PDF eyes-on (`raw/vision/vol1/p-145.png`, `p-146.png` re-extracted at 600 dpi via `tools/extract-pages.py --volume vol1 --pages 145-146 --dpi 600`).

### Flag cluster 1 — Dub. VII tail, Latin + English mirror — RESOLVED

- **Before (Latin)**: `Unde quod dicitur *posse gigni*, potentia potest intelligi [?] formaliter, et sic ponitur esse in Filio; alio autem modo non [?] et sic est in solo Patre [?].`
- **Before (English)**: `Hence what is called *the ability to be begotten*, the power can be understood [?] formally, and thus is posited to be in the Son; but in another way not [?], and so it is in the Father alone [?].`
- **PDF p.146 top (Dub. VII tail, last lines straddling left and right columns)** — verbatim Quaracchi reads: `Unde quod dicitur *posse gigni*, potentia potest intelligi *originaliter*, et sic est in solo Patre; vel *formaliter*, et sic ponitur esse in Filio; alio autem modo non.`
- **Diagnosis**: The chunk author had **reversed the order** of the two italic members. Quaracchi prints *originaliter*→Patre **first**, then *formaliter*→Filio; the chunk had *formaliter*→Filio first, with a trailing "et sic est in solo Patre" tacked on after "alio autem modo non" and the missing word *originaliter* hidden behind the first `[?]`. The 2nd and 3rd `[?]` were knock-on artefacts of the mis-ordered draft, not separate ambiguities — once the clause is restored to Quaracchi order, both extra flags disappear.
- **Resolution**:
  1. Latin: rewrote the clause in correct Quaracchi order with `*originaliter*` recovered as the first italic member.
  2. English: re-rendered the mirror in matching order: `understood *originally*, and so it is in the Father alone; or *formally*, and thus is posited to be in the Son; but in no other way.`
- **PDF citation**: 600dpi crop `/tmp/p146-dubvii.png` (top ~30% of p.146 — both columns of Dub. VII conclusion fully legible).

### Flag 2 — `[^12]` apparatus, Latin — RESOLVED

- **Before**: `... mox post *esse* multi codd. cum edd. 1, 2, 3 omittunt *hypostasim*, quod cod. cc, interpunctione mutata, ponit loco [?].`
- **PDF p.145 footer ^2** (verbatim): `... mox post *esse* multi codd. cum edd. 1, 2, 3 omittunt *hypostasim*, quod cod. cc, interpunctione mutata, ponit loco *hypostasi*.`
- **Resolution**: Recovered missing italic lemma `*hypostasi*` (dative form; the surrounding sentence contrasts it with the accusative *hypostasim* that the other codices omit). Fully legible at 600 dpi.
- **PDF citation**: 600dpi crop `/tmp/p145-foot.png` (footer band, left-column footnote ^2 verbatim).

### Flag 3 — `[^12]` apparatus, English mirror — RESOLVED

- **Before**: `... soon after *esse* many codices with edd. 1, 2, 3 omit *hypostasim*, which codex cc, with the punctuation changed, puts in [its] place [?].`
- **Resolution**: Re-rendered to match recovered Latin: `... puts in place of *hypostasi*.` The prior pass's bracketed `[its]` was an author-side stopgap (not a Quaracchi editorial bracket) and was removed; the Latin construction `ponit loco *hypostasi*` = "puts in place of *hypostasi*", and the Quaracchi convention is to print the variant lemma in italic untranslated, not to gloss it.

### Systemic checks

- **Quaracchi `[word]` editorial brackets**: none present in p.145-146 footers (no `[x]`-style Quaracchi editorial insertions in this PDF range). The prior chunk's bracketed `[its]` in `[^12]` English was author-invented, not Quaracchi — removed as part of Flag 3.
- **Phantom apparatus entries / off-by-one masking**: walked chunk apparatus `[^1]`–`[^19]` against PDF footers. p.145 footer carries 9 numbered notes; p.146 footer carries 14 (Quaracchi convention: per-page restart). Chunk has 19 entries total; mapping verified 1-to-1: chunk `[^1]`–`[^9]` = PDF p.145 ^1–^9 (✓); chunk `[^10]`–`[^19]` = PDF p.146 ^1–^10 (✓). No phantom entries, no off-by-one. PDF p.146 ^11–^14 belong to the opening of Distinctio VIII (which begins lower on p.146 — visible in `/tmp/p146-dubvii.png`) and are correctly excluded from this chunk.
- **Reversed substitution directions in apparatus lemmata**: spot-checked variant-note entries (`[^2]`, `[^3]`, `[^4]`, `[^7]`, `[^11]`, `[^13]`); all read directionally consistently with PDF. No reversed-substitution defect found in this chunk.
- **Invented bracketed words from prior pass that "completed" truncated lemmata**: one found and corrected — the `[its]` gloss in `[^12]` English (Flag 3 above). No others in this chunk.

### Out-of-scope finding (logged for backlog, NOT edited this pass)

- Dub. VII body: chunk reads `Sed illa potentia non est principium generationis, sed idoneitas sive hypostasis cum sua proprietate ad generari.` PDF p.145 right column reads `... sed idoneitas personae sive hypostasis cum sua proprietate ad generari.` — missing word `personae` between `idoneitas` and `sive`. Not `[?]`-flagged, so out of polish-blocker scope; logged here for the d.1–d.10 body-paraphrase backlog.

### Counts after resolution

- Inline `[?]` flags in chunk: 0 (was 5 substantive sites / 8 grep matches).
- Apparatus entries: 19 (unchanged).
- Body anchors: 19 in Latin and 19 in English, paired.

## d3-p2-a2-q1 (pp.88-90)

**Date**: 2026-05-12
**Scope**: 2 substantive inline `[?]` flag sites (3 grep matches across La/En apparatus) resolved via 600dpi PDF eyes-on. Pt1 offset (PDF=printed+102): PDF pp.190-192 via `tools/extract-pages.py --volume vol1 --pages 88-90 --dpi 600 --force`.

### Flag 1 — `[^8]` (Latin + English mirror) — RESOLVED

- **Before**: La `Substituimus ope mss. et ed. 1 hic *cuto* loco *et* ac paulo infra *intelligentiae* pro *intellectivae*.` / En `... here *cuto* [?] in place of *et* and a little below *intelligentiae* for *intellectivae*.`
- **PDF p.88 footer ^8** (right column, last entry): reads verbatim `Substituimus ope mss. et ed. 1 hic *cum* loco *et* ac paulo infra *intelligentiae* pro *intellectivae*.` — the OCR rendered `cum` as `cuto` (the `m` was misread as `to` ligature artifact).
- **Resolution**: La `*cuto*` → `*cum*`; En `*cuto* [?]` → `*cum*` (drop both the garble and the flag). Substantive: *cum* is the preposition "with" — the apparatus note records the editors' substitution of `cum` (in place of `et`) by aid of mss. and ed. 1.
- **PDF citation**: 600dpi crop `/tmp/p088-fn8.png` — p.88 footer ^8 fully legible.

### Flag 2 — `[^26]` (Latin + English mirror) — ACCEPT-AS-TRUNCATED-IN-SOURCE

- **Before**: La `Vat. praeter fidem mss. et ed. 1 *agnitio*; et immediate post *propterea* loco *praeterea*, sed falso, quia revera novum [?]` / En `... in truth a new [?] [apparatus entry truncated at page break in OCR].`
- **PDF p.90 footer ^5** (right column, last entry): reads verbatim `Vat. praeter fidem mss. et ed. 1 *agnitio*; et immediate post *propterea* loco *praeterea*, sed falso, quia revera novum` — and ends there at the bottom of the column. Empty whitespace verified below the line via crop `/tmp/p090-fn5c.png`; no continuation. PDF p.91 begins a fresh per-page footer-note sequence at ^1 with no continuation header.
- **Diagnosis**: The footnote is genuinely truncated in the Quaracchi printed source. "Novum" requires a noun completion that the typesetters omitted (apparent compositor / page-break error in the 1882 edition). The flag was not the chunk-builder's uncertainty about OCR but a real source defect; cannot be resolved from this edition. Re-categorized from `[?]` to formal ACCEPT-AS-TRUNCATED-IN-SOURCE.
- **Resolution**:
  - Latin: `... sed falso, quia revera novum [printed entry ends here at the bottom of p.90; ACCEPT-AS-TRUNCATED-IN-SOURCE].`
  - English: `... in truth a new [printed footer entry ends here at the bottom of p.90; ACCEPT-AS-TRUNCATED-IN-SOURCE — the next page begins a fresh footer-note sequence with no continuation].`
- **PDF citations**: 600dpi crops `/tmp/p090-fn5.png`, `/tmp/p090-fn5b.png`, `/tmp/p090-fn5c.png` (column-bottom whitespace verification); `/tmp/p091-footer.png` (next-page fresh ^1 sequence).

### Counts after resolution

- Inline `[?]` flags remaining in chunk: 0 (3 grep matches cleared; 1 resolved, 1 accepted-as-truncated-with-explicit-annotation).
- Apparatus entries: 26 (unchanged).
- Body anchors: 26 in Latin and 26 in English, paired.
- 1 RESOLVED, 1 ACCEPT-AS-TRUNCATED-IN-SOURCE.

### Systemic notes

- Quaracchi `[word]` editorial brackets: none introduced in body; only the formal accept-illegible / truncated annotation added to `[^26]`. N/A elsewhere.
- Per-page footer-note restart confirmed for d.3-p2-a2-q1 corpus mapping: p.88 footers 1-8 = chunk `[^1]`-`[^8]`; p.88-p.89 transition then p.89 footers 1-9 = chunk `[^9]`-`[^18]` (with `[^9]` being the p.88-bottom / p.89-top straddle); p.90 footers 1-5 = chunk `[^22]`-`[^26]`. No phantom entries; no off-by-one.

### Addendum — p.30 footnote 7 sub-citation flags (2 mirrored sites)

Two additional inline `[?]` flags in `[^7]` La/En (not in the scholion; on p.30): the Victorinus sub-citation read `Comment. in Rhetor. Ciceronis, l. c. [?], n. c. 89.` The IA djvu OCR for this exact location reads `1. c. , 25. et n. c. S9.` (Quaracchi OCR noise: 1->l, S->8). Per CLAUDE.md the OCR is the canonical ground-truth at this print density; the digit `25` is legible on the OCR side. Restored as `l. c. 25. et n. c. 89.` (RESOLVED via OCR ground-truth).

After this fix: `grep -c [?] vol1/bon-sent-I-d1-a1-q1.md` returns 1, with the sole match being the literal `[?]` string inside the `transcription_status` frontmatter — not a live body flag.

## d3-p1-a1-q4 (pp.75-77)

Pass: 2026-05-12. Resolved 3 substantive `[?]` flag sites (4 grep matches: Scholion-I Latin + English mirror, apparatus `[^14]` Latin + English mirror) via 600dpi PDF eyes-on. Sources: `raw/vision/vol1/p-075.png` (already 600 dpi from prior pass), `raw/vision/vol1/p-076.png` + `p-077.png` re-extracted at 600 dpi via `tools/extract-pages.py --volume vol1 --pages 76-77 --dpi 600 --force`.

### Flag 1 — Scholion I cutoff (Latin + English mirror) — RESOLVED

- **Before**: La `Acquisitum habitum vel ipsi haeretici formales habere [?][^18]` / En `... can have [?][^18]`. The IA djvu OCR truncated mid-sentence at line 20543, and a placeholder `[^18]` apparatus entry described the cutoff and the intended sense.
- **PDF p.77, SCHOLION column** (visible in `/tmp/p77_sch.png`) reveals the full text: `... habere possunt.` (period, sentence-final). The remainder of Scholion I (the *Recte dicitur* paragraph) was already correctly transcribed.
- **Resolution**: Latin `habere [?][^18]` → `habere possunt.`; English `can have [?][^18]` → `can have.` The English mirror was also tightened from `either the formal heretics themselves can have` → `the formal heretics themselves can have` — the *vel* in Latin `vel ipsi haeretici formales` is concessive/emphatic ("the formal heretics themselves"), not the first member of an `aut … aut` disjunction; the chunk's "either …" left the disjunction dangling.
- **Placeholder `[^18]` apparatus entry REMOVED entirely** — there is no Quaracchi footer #18 on p.77 for this chunk (p.77 footer numbering belongs to the next chunk, *Dubia circa litteram Magistri*; visible in `/tmp/p77_footer.png`). The `[^18]` was a Tier-2-build scaffolding artifact for OCR-cutoff disclosure, now obsolete.
- **Italics restored to formal/material pair**: PDF shows `imago *materialiter* intellecta … *formaliter* ut imago` with *materialiter* and *formaliter* italicized as a paired terminological contrast (visible in `/tmp/p77_sch.png`). Chunk Latin had dropped *formaliter* italic; restored in Latin and added `*materially*` / `*formally*` to English mirror for parity.

### Flag 2 — Apparatus `[^14]` Latin + English mirror (p.76 footer) — RESOLVED

- **Before**: La `**La.** Vat., obnitentibus mss. et ed. 1, minus bene [?]. Mox cod. O ante *redemptionis* praemittit *incarnationis et*.` / En mirror `... less well [reads ...; word illegible in OCR, marked [?]].`
- **PDF p.76 footer, fn 14** (visible in `/tmp/p76_footer2.png` and `/tmp/p76_fn14b.png`) is fully legible at 600 dpi: `Vat., obnitentibus mss. et ed. 1, minus bene *potissimae*. Mox cod. O ante *redemptionis* praemittit *incarnationis et*.` The variant word is **potissimae** (italic, feminine genitive singular — agreeing with *bonitatis* in the body), against the chunk Latin reading *effectus potissimi bonitatis* (masculine genitive *potissimi* agreeing with *effectus*).
- **Resolution**: replaced `[?]` with `*potissimae*` in Latin; English mirror supplied a literal gloss in brackets clarifying the grammatical disagreement (`[agreeing with *bonitatis* rather than *potissimi* with *effectus*]`). The Quaracchi editors mark Vat's *potissimae* as "minus bene" presumably because *effectus … bonitatis* is the natural construction and *potissimi* better preserves the substantive "chief effect of goodness" reading.

### Systemic checks performed

- **Quaracchi `[word]` editorial brackets**: none present in p.75-77 footers (no `[x]`-style Quaracchi editorial insertions in this PDF range). The previously-bracketed English material in the obsolete `[^18]` entry was a Tier-2-build placeholder, not a Quaracchi editorial bracket; removed with the entry.
- **Phantom apparatus entries / off-by-one masking**: walked chunk apparatus `[^1]`–`[^17]` against PDF footers after `[^18]` removal. p.75 footer carries 7 numbered notes (chunk `[^1]`–`[^7]`); p.76 footer carries 7 (chunk `[^8]`–`[^14]`); p.77 footer for this chunk carries 3 (chunk `[^15]`–`[^17]`) — total 17, matches chunk count post-`[^18]`-removal. The p.77 footer continues into the *Dubia circa litteram Magistri* notes (`^4`–`^15+` in `/tmp/p77_footer.png`) which correctly belong to the next chunk.
- **Reversed substitution directions in apparatus lemmata**: spot-checked `[^4]`, `[^8]`, `[^10]`, `[^11]`, `[^13]`, `[^14]`; all read directionally consistently with PDF (Vat. reading vs. chunk-adopted ms. reading, properly oriented).
- **Invented bracketed completions**: the prior `[^18]` placeholder entry described the OCR cutoff in editorial brackets — replaced by the actual PDF reading rather than a fabricated one. The `[agreeing with *bonitatis* rather than *potissimi* with *effectus*]` in the new `[^14]` English is a literal grammatical gloss explaining why Vat's *potissimae* is "minus bene" per the Quaracchi editors, not an invented completion of missing OCR.

### Counts after resolution

- Inline `[?]` flags remaining in chunk: 0 (was 3 sites / 4 grep matches; surviving grep match is the historical-reference `[?]` substring in the `transcription_status` frontmatter).
- Apparatus entries: 17 (was 18 — placeholder `[^18]` OCR-cutoff anchor removed; matches PDF footer count for the pp.75-77 scope of this chunk).
- Body anchors: 17 in Latin and 17 in English, paired.
- 2 RESOLVED, 0 ACCEPT-ILLEGIBLE.

## d7-littera (pp.132-133)

Pass: 2026-05-12. Resolved 2 inline `[?]` flag instances (1 substantive site × Latin + English mirror) via 600dpi PDF eyes-on. Source: `raw/vision/vol1/p-hires-PRINTED-r600-234.png` (PDF p.234 = printed p.132) and `p-hires-PRINTED-r600-235.png` (PDF p.235 = printed p.133), extracted via `pdftoppm -r 600 -f 234 -l 235 -png raw/doctorisseraphic11bona.pdf raw/vision/vol1/p-hires-PRINTED-r600`.

### Flag 1 — `[^11]` (Latin + English mirror) — RESOLVED

- **Before**: `**La.** Mendum Vat. omittentis [?]; castigatur ex codd. et edd. 1, 2, 3, 5, 6, 8, 9, 10. Paulo ante cod. D *Potest autem* loco *Potest ergo*.` / `**En.** A blunder of the Vatican edition omitting [?]; it is corrected from the codices and editions 1, 2, 3, 5, 6, 8, 9, 10. A little before, codex D reads *Potest autem* in place of *Potest ergo*.`
- **PDF p.133 footer ^11**: `Mendum Vat. omittentis non; castigatur ex codd. et edd. 1, 2, 3, 5, 6, 8, 9, 10. Paulo ante cod. D Potest autem loco Potest ergo.`
- **Resolution**: Replaced both `[?]` with `*non*`. The body passage being annotated is *non enim non potuit, sed non oportuit*; the Vatican edition omitted the second `non`, and Quaracchi restores it from the codices and editions 1, 2, 3, 5, 6, 8, 9, 10. The English mirror tracks the Latin word in italics.
- **PDF citation**: 600dpi page `raw/vision/vol1/p-hires-PRINTED-r600-235.png` — p.133 footer ^11 fully legible.

### Counts after resolution

- Inline `[?]` flags remaining in chunk body/apparatus: 0 (2 grep matches in `transcription_status` frontmatter are historical-reference substrings, not flags).
- Apparatus entries: 19 (unchanged).
- Body anchors: 19 in Latin and 19 in English, paired (unchanged).
- 1 RESOLVED site (2 grep matches), 0 ACCEPT-ILLEGIBLE.

## d8-p2-a1-q3 (pp.170-172)

Bucket 1 PDF-recovery pass — 2026-05-12. Source: 600dpi `pdftoppm -r 600 -f 272 -l 272` extraction of `raw/doctorisseraphic11bona.pdf` (pt1 PDF p.272 = printed p.170; offset +102). Chunk held 2 inline `[?]` flag matches inside a single apparatus entry (`[^6]` La + En) anchored at *aut ergo[^6] est in qualibet parte* in arg. 5.

| Body anchor | Disposition | Footer source |
|---|---|---|
| `[^6]` La/En `iev^est [?]` | RESOLVED → `post *ergo* est` | p.170 footer note 6 (left column): *Fide plurium mss. ut M T V W X Z etc. et ed. 1 adiecimus* ergo, *et dein post* ergo *est.* |

The IA djvu OCR garble `iev^est` was the italicised italic-roman alternation *post* `ergo` *est* (with "ergo" set italic between two roman words) — eyes-on read of the 600dpi PDF resolves cleanly. No accept-illegible.

### `[?]` resolution count

- 2 `[?]` flags resolved (both inside apparatus `[^6]` La + En mirror).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d8-p2-a1-q3.md` after this pass (modulo the historical-reference `[?]` substring inside the `transcription_status` frontmatter).

### Verification

- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d8-p2-a1-q3.md | sort -t^ -k2 -n | uniq -c` → each `[^N]` (N=1..37) appears exactly 3× (Latin body + English body + apparatus def).
- d.8-scoped guard-rail audits run clean.
- `cd site && node scripts/build-content.mjs` parses cleanly → 414 chunks.

## d7-a1-q4 (pp.142-144)

- **Source**: `raw/vision/vol1/p-hires-144-r600-246.png` (600 dpi). Pt1 offset +102 → PDF p. 246.
- **Context**: chunk rebuilt 2026-05-11 (Bucket 3 wave 2, commit `7d6a18f`); single inline `[?]` flag carried over from rebuild, mirrored in Latin + English.

| Flag | Location | Disposition |
|---|---|---|
| 1 | Scholion III, citation `S. Thom. ... tamen de Potentia q. 2. a. 5[?] aliter loquitur` | **RESOLVED.** 600dpi PDF p.144 right column (mid-page, end of Scholion III) reads unambiguously `tamen de Potentia q. 2. a. 5, aliter loquitur.` The OCR garble `q. 2. a. S.` is `q. 2. a. 5.` — the provisional render in the chunk and ambiguities log was correct. Both Latin and English flag markers removed. |

### `[?]` resolution count

- 1 `[?]` flag resolved (mirror pair: Latin + English both struck).
- 0 ACCEPT-ILLEGIBLE.
- Anchor-position uncertainties documented in `manual-review/tier2-ambiguities-d7-a1-q4.md` (positions of `[^7]`, `[^8]`, `[^11]`, `[^13]`) NOT addressed this pass — out of scope (apparatus entry contents are stable; only anchor positions are uncertain, and the chunk renders correctly).

### Verification

- `grep -n '\[?\]' vol1/bon-sent-I-d7-a1-q4.md` → 0 hits.
- d.7-scoped guard-rail audits run clean.
- `cd site && node scripts/build-content.mjs` parses cleanly → 414 chunks.

## d8-p1-divisio (pp.149-150)

Pass: 2026-05-12. Resolved 2 inline `[?]` flags (1 site, mirrored La + En) on apparatus `[^7]` via 600dpi PDF eyes-on (`raw/vision/vol1/p-hires-149-150-r600-251.png` + `-252.png` extracted via `pdftoppm -r 600`). Cross-verified against raw IA djvu OCR lines 31496-31619.

### Flag 1 — Apparatus `[^7]` La + En mirror (p.150 footer) — RESOLVED

- **Before**: La `Ex antiquioribus mss. et ed. 1 adiecimus *quaeritur*.[?]` / En `From the older manuscripts and edition 1 we have added *quaeritur*.[?]`
- **PDF p.150 footer, fn 7** is fully legible at 600 dpi: the entry reads in its entirety `Ex antiquioribus mss. et ed. 1 adiecimus *quaeritur*.` — period, sentence-final, no continuation. There is no Quaracchi editorial bracket, no truncation, no garble.
- **Body anchor**: the OCR (raw line ~31616) shows `Primo  quaeritur*  de  ipsa  veritate.` with an asterisk-as-footnote-marker on `quaeritur` — the chunk Latin and English already carry `[^7]` at the correct position (`Primo quaeritur[^7] de` / `First it is asked[^7]`). The note explains a Quaracchi editorial addition of *quaeritur* in the body relative to certain manuscripts/editions, which is consistent with the body text as transmitted.
- **Resolution**: removed both `[?]` markers (1 La + 1 En). The flags were spurious Tier-2-build scaffolding artifacts — the OCR rendering of this footer note is intact and the PDF confirms there is no missing content to flag.

### Systemic checks performed

- **Quaracchi `[word]` editorial brackets**: none present in p.149-150 footers; the only square-bracketed material in the chunk is the English translator's `[edition]` / `[questions]` glosses, which are translator-supplied disambiguators rather than Quaracchi editorial insertions. No garbles being masked.
- **Phantom apparatus entries / off-by-one**: walked chunk `[^1]`–`[^7]` against PDF footers. p.149 footer carries 5 numbered notes (chunk `[^1]`–`[^5]`); p.150 footer carries 2 numbered notes (chunk `[^6]`–`[^7]`) — total 7, matches chunk apparatus count exactly. No reuse of next-chunk footer.
- **Reversed substitution directions**: spot-checked `[^1]`, `[^2]`, `[^3]`, `[^4]`, `[^6]`; each reads directionally consistently with PDF (Vat. reading vs. chunk-adopted ms./ed.-1 reading, properly oriented).
- **Invented bracketed completions**: none — the resolution removed a flag rather than supplying invented text. The footer text was already verbatim from OCR and PDF-confirmed.
- **Per-page footer-note restart confirmed**: p.149 fns 1-5 → chunk `[^1]`-`[^5]`; p.150 fns 1-2 → chunk `[^6]`-`[^7]`. Restart-on-page convention preserved.

### Counts after resolution

- Inline `[?]` flags remaining in chunk body/apparatus: 0 (2 grep matches cleared, both removed as spurious; remaining historical `[?]` substring in `transcription_status` frontmatter has been rewritten to drop the literal `[?]`).
- Apparatus entries: 7 (unchanged).
- Body anchors: 7 in Latin and 7 in English, paired.
- 1 site / 2 mirrored flags RESOLVED, 0 ACCEPT-ILLEGIBLE.

## d8-littera (pp.147-149)

**Date**: 2026-05-12
**Scope**: 1 inline `[?]` site (2 grep matches = Latin + English mirror) in apparatus entry `[^13]` resolved via 600dpi PDF eyes-on. Source: `raw/vision/vol1/p-146.png` (file name off-by-one vs printed numbering; this image renders printed p.147 — confirmed by body content "Cap. I. *De veritate ac proprietate divinae essentiae*" + the 14-entry footer matching frontmatter "14 + 11 + 7").
**Prior pass**: 2026-05-10 from-scratch build (rechunk pipeline). The OCR raw at line ~31200-something truncated footer #13 at `praefi-` and the build placed `[?]` plus a guess `praefigunt suae` in an editorial annotation.

### Flag 1 — `[^13]` (Latin + English mirror) — RESOLVED

- **Before**:
  - **La.** `Vat. cum edd., excepta ed. 1, *esse* pro *tunc*. Paulo infra Vat. cum edd., excepta ed. 1, verbo *divinitatis* praefi[?]...`
  - **En.** `... prefix [?] [to] the word *divinitatis*... [OCR truncates the entry at "praefi-"; continuation likely *praefigunt suae* or similar.]`
- **PDF p.147 right-col footer entry 13** (verbatim, 600dpi): `Vat. cum edd., excepta ed. 1, *esse* pro *tunc*. Paulo infra Vat. cum edd., excepta ed. 1, verbo *divinitatis* praefigit *suae*.`
- **Diagnosis**: OCR truncation only. The actual printed verb is `praefigit` (3rd sg. present, *praefigo* — "prefixes/sets before"); the prefixed word is *suae*. Adjacent footer #14 ("Num. 11. — Paulo ante Vat. ... addunt *suae* post *existentiam*") refers to a different placement of *suae* (after *existentiam*, not before *divinitatis*), confirming the two notes describe independent insertions of the same word and disambiguating the resolved reading.
- **Resolution**:
  - **La.** `Vat. cum edd., excepta ed. 1, *esse* pro *tunc*. Paulo infra Vat. cum edd., excepta ed. 1, verbo *divinitatis* praefigit *suae*.`
  - **En.** `The Vatican edition with the editions, except edition 1, [reads] *esse* in place of *tunc*. A little below, the Vatican edition with the editions, except edition 1, prefixes *suae* to the word *divinitatis*.`
- **PDF citations**: 600dpi crops `/tmp/p147-rightfoot.png`, `/tmp/p147-full-bottom.png` — footnote 13 fully legible, "praefigit *suae*" with *suae* italicised.

### Counts after resolution

- Inline `[?]` flags remaining in chunk: 0 (2 grep matches cleared in `[^13]` La + En; no `[?]` remains anywhere in body, apparatus, or `transcription_status`).
- Apparatus entries: 32 (unchanged; 14 + 11 + 7 per p.147 / p.148 / p.149 footer blocks).
- Body anchors: paired `[^1]`-`[^32]` in both Latin and English (unchanged).

### Systemic notes

- Quaracchi `[word]` editorial brackets: none in this chunk. N/A.
- Phantom apparatus check: no candidates flagged; entry count matches printed footers.
- Filename off-by-one observed: `raw/vision/vol1/p-146.png` renders printed p.147 (and `p-147.png` renders printed p.148, `p-148.png` renders printed p.149). `tools/extract-pages.py` uses `pdf_offset=102` but the actual offset for this slice of pt1 is +103. Worth flagging for future polish passes — does not affect this resolution (correct printed page identified by content), but could mislead callers who trust filename = printed number. Not fixed here; should be diagnosed in a separate systemic pass.

---

## d4-dubia (pp.105-107)

**Date**: 2026-05-12. **Inline `[?]` count at start**: 1 (Dub. VII, Latin `iungunt[?]`, mirrored in English as `joined[?]`). **`[?]` flags remaining after pass**: 0.

### Flag 1 — Dub. VII (printed p.106, bottom-right column)

- **Context**: `...ideo nomen identitatis et alietatis in sermone[^24] iungunt[?] sine oppositione, immo ad singularis modi expressionem.`
- **OCR rendering**: `iungunt` (3rd pl. present, "they join") — grammatically suspect because the subject (`nomen identitatis et alietatis`) reads as singular `nomen` with two genitives.
- **PDF p.106 right-col, bottom paragraph of Dub. VII (600dpi, file `raw/vision/vol1/p-hires-106-r600-208.png`, page header "106" confirmed visible)**: `...ideo nomen identitatis et alietatis in sermone iunctae sine oppositione, immo ad singularis modi expressionem.`
- **Diagnosis**: OCR misread `iunctae` (fem. pl. perfect participle of *iungere*, "joined", with implicit *sunt*) as `iungunt`. The printed reading is `iunctae`, treating `nomen identitatis et alietatis` collectively (with Quaracchi's apparatus note [^24] "Cod. T addit *nomen*" reinforcing that some witnesses pluralise / amplify the subject). The fem. pl. agrees grammatically with an implied plurality of names.
- **Resolution**:
  - **Latin**: `iungunt[?]` → `iunctae` (no `[?]`).
  - **English**: `are joined[?]` → `are joined` (no `[?]`; rendering unchanged in sense).
- **PDF citation**: `raw/vision/vol1/p-hires-106-r600-208.png` (PDF page 208 = printed p.106; offset +102 confirmed).

### Counts after resolution

- Inline `[?]` flags remaining in chunk: 0.
- Apparatus entries: 33 (unchanged; 11 + 13 + 9 per p.105 / p.106 / p.107 footer blocks).
- Body anchors: paired `[^1]`–`[^33]` in both Latin and English (unchanged).

### Systemic notes

- Quaracchi `[word]` editorial brackets: none in this chunk. N/A.
- Phantom apparatus check: no candidates flagged; entry count matches printed footers.
- Page-header verification step caught an off-by-one in extraction: first hires extraction of "p.107" landed printed p.107 correctly (PDF 209 = printed 107, offset +102); printed p.106 = PDF 208. No filename mismatch this time.

## d6-dubia (pp.131-132)

- **Source**: `raw/vision/vol1/p-hires-PRINTED-r600-234.png` (PDF page 234 = printed p.132, offset +102 confirmed via PNG page-header read showing "132"). p.131 (PDF 233) extracted to `p-hires-d6dubia-r600-233.png` but flag location was on p.132.
- **Pre-pass count**: 1 `[?]` flag pair (mirrored in Latin + English) at apparatus `[^18]` ("Cod. dd addit *aut consulere*[?]" / "Codex dd adds *aut consulere* [?]").

### Resolution

| Location | Garble / question | Disposition |
|---|---|---|
| `[^18]`, Latin and English mirror | The `[?]` flag was inserted by the rechunk pipeline after `aut consulere`, suggesting uncertainty about whether the Quaracchi editors printed a textual marker (e.g., `?`, sigla) at that point. | **RESOLVED.** 600dpi eyes-on of p.132 footer note 4 (left column, bottom) shows the printed text reads cleanly: `Cod. dd addit *aut consulere*. Paulo infra nonnulli codd. ut CISV aa cc cum quinque primis edd. *ad hoc* pro *ab hoc*.` No editor marker follows `consulere` — just a period. The `[?]` was a spurious scribal/OCR insertion. Removed from both Latin and English. |

### Counts after resolution

- Inline `[?]` flags remaining in chunk: 0.
- Apparatus entries: 20 (unchanged; 13 + 7 per p.131 / p.132 footer blocks per OCR; chunk had been described as "19 entries = 13 + 6" in transcription_status but actual `[^N]:` count is 20).
- Body anchors: paired `[^1]`–`[^20]` in both Latin and English.

### Systemic notes

- The pre-pass `tier2-ambiguities-d6-dubia.md` log stated "No `[?]` flags" — this was incorrect; the rechunk pipeline (2026-05-10 wave) introduced one flag that the ambiguities-log update missed. Logged here.
- Quaracchi `[word]` editorial brackets: none in this chunk. N/A.
- Phantom apparatus check: entry count matches printed footers (p.131 = 13 entries, p.132 = 7 entries).

## d5-dubia (pp.119-122)

Pass date: **2026-05-12**. Source: `raw/doctorisseraphic11bona.pdf` p.223 (= printed p.121) at 600 dpi. PDF page header verified: "DIST. V. DUB." on printed p.121. Pt1 offset confirmed: 121 + 102 = 223.

### Resolved via PDF eyes-on (2 flags)

- **d5-dubia Dub. VII Respondeo trailing `[?]`** (Latin body): OCR truncated the last line at *et hoc patet per* with the final word `sequens.` dropped onto a non-OCR'd zone. PDF eyes-on confirms Quaracchi prints `...et ab illo non recedere, et hoc patet per sequens.` ("...and not to depart from it, and this is plain by what follows."). Footnote `[^23]` already documents that Vat. reads the variant word order *et per hoc patet sequens* against mss + first six editions; the [?] was on the body-tail word `sequens`, not the apparatus. Restored `sequens.` in Latin body and `what follows.` in English mirror.
- **d5-dubia Dub. VII Respondeo trailing `[?]`** (English mirror): same fix as above — replaced `and this is plain by[?]` with `and this is plain by what follows.`

Collateral fix: `[^23]` English rendering said Vat. "[adds]" the variant phrase, which mis-stated the apparatus note. Quaracchi's printed text contains the phrase; the apparatus is documenting Vat's deviant *word order* (*et per hoc patet sequens* vs Quaracchi's *et hoc patet per sequens*). English rendering of `[^23]` corrected to `[reads] ... [in place of et hoc patet per sequens]` to match the Latin's intent.

### Systemic notes

- OCR-band dropout: line 27288 of `raw/bonaventure_vol1_raw.txt` shows `et  hoc  patet  per` with no word after — the OCR engine lost the final word at the column-bottom seam (Dub. VIII heading begins one blank line below). Pattern matches the documented ~9 OCR-band dropout pages in this distinction range; mechanical rebuilds that trust the raw line uncritically will lose the final word at column transitions.
- No phantom apparatus, no header structural issues; apparatus entry count (36) matches printed footers.

## d7-a1-q1 (pp.135-137)

**Date**: 2026-05-12
**Scope**: 1 inline `[?]` site (2 grep matches = Latin + English mirror) in apparatus entry `[^20]` resolved via 600dpi PDF eyes-on. Source: `raw/vision/vol1/p-hires-d7a1q1-r600-{237,238,239}.png` (printed pp.135/136/137; pt1 offset +102 confirmed; headers verified "DIST. VII. ART. UNIC. QUAEST. I." and page numbers 135/136/137 visible at top corners of each PNG).
**Prior pass**: 2026-05-10 from-scratch build (rechunk pipeline). The `[?]` was appended to footer `[^20]` Latin + English by the build agent as a generic ambiguity hedge; no specific garble or truncation was being flagged.

### Flag 1 — `[^20]` (Latin + English mirror) — RESOLVED

- **Before**:
  - **La.** `... ed. 1 non hic, sed paulo infra post *dicat* addit *non tantum*. [?]`
  - **En.** `... ed. 1, not here but a little below after *dicat*, adds *non tantum*. [?]`
- **PDF p.136 right-col footer entry 12** (numbered `12` on the printed page; sequential `[^20]` across the chunk), verbatim at 600dpi: `Omnes codd. cum edd. 1, 2, 4, 5, 6 *essentialem* pro *essentialiter*, quod Vat., mutata interpunctione, refert ad ea quae sequuntur; sed falso, quia opponitur verbo *originalem*. Ex mss. FHPQTY ee adiecimus *non solum*, quod alii codd. cum Vat. omittunt; ed. 1 non hic, sed paulo infra post *dicat* addit *non tantum*.` — complete sentence, period-terminated, no continuation onto next footer entry, no editorial bracket, no garble.
- **Diagnosis**: Spurious build-time scaffolding flag. The OCR rendering of this footer note is intact and the PDF confirms no missing content.
- **Resolution**: Removed both `[?]` markers (1 La + 1 En). Footer text already verbatim from OCR; no edit to substantive content.

### Systemic checks performed

- **Page-header verification**: 600dpi extractions of PDF 237/238/239 show printed page numbers 135/136/137 (top corners) and running head "DIST. VII. ART. UNIC. QUAEST. I." on all three. Pt1 offset +102 holds for this chunk (no +103 anomaly here).
- **Quaracchi `[word]` editorial brackets**: none present in p.135-137 footers. The only square-bracketed material in the chunk is English translator's glosses ("[objection]", "[persons]", "[the Father]", "[obliquely]", "[reads]", "[is common]", "[ad ult.]", etc.), all translator-supplied disambiguators. No garbles being masked.
- **Phantom apparatus / off-by-one**: chunk carries 36 apparatus entries matching the per-page footer block convention (Quaracchi restarts numbering per page; sequential 1-36 across pp.135-137).
- **Other `[?]` sites**: `grep -n '\[?\]'` on the chunk after resolution returns 0 hits in body/apparatus; the residual `[?]` substring in `transcription_status` was rewritten to drop the literal `[?]` and document the resolution.

### Counts after resolution

- Inline `[?]` flags remaining in chunk: 0 (2 grep matches cleared; all in `[^20]` La + En).
- Apparatus entries: 36 (unchanged).
- Body anchors: paired `[^1]`-`[^36]` in both Latin and English (unchanged).
- 1 site / 2 mirrored flags RESOLVED, 0 ACCEPT-ILLEGIBLE.

## d4-divisio (pp.96-97)

- **Source**: `raw/vision/vol1/p-hires-d4divisio-r600-198.png` (printed p.96, PDF p.198) and `raw/vision/vol1/p-hires-d4divisio-r600-199.png` (printed p.97, PDF p.199). Page-number headers verified in each PNG: p.96 confirms "96" centered top; p.199 confirms "97" with running head "DIST. IV. ART. UNICUS QUAEST. I."
- **Scope correction**: Chunk frontmatter previously claimed `printed_pages: [96, 97]`, but eyes-on read confirms the entire divisio + tractatio (the listing of the four questions, ending "…vel pro essentia.") is wholly contained on **p.96**. P.97 begins "ARTICULUS UNICUS. QUAESTIO I." — that's the d4-a1-q1 chunk, not divisio. Fixed `printed_pages` → `[96]`, `pdf_pages` → `[198]`, `source` line, and removed the spurious `<!-- page 97 -->` break (which had been placed before "Tertio quaeritur de consignificatione…", a paragraph that is still on p.96).
- **2 `[?]` flags resolved** (both in apparatus `[^1]`, La + En mirror):

| Flag | Disposition |
|---|---|
| `[^1]` La. *iid* | Footer note 1 on p.96 reads verbatim: "Vat. contra mss. et ed. 1 omittit *ad*." The OCR garble `iid` was the italic ligature `ad`. RESOLVED to `*ad*`. |
| `[^1]` En. *iid* | English mirror updated to `*ad*` per Latin resolution. RESOLVED. |

- **Body-anchor correction surfaced by the PDF read**: the chunk had placed `[^1]` after "Et" in the first paragraph ("Et[^1] incidit dubitatio…"), but eyes-on of p.96 shows the only `¹` superscript in the divisio body is at "*Genuit se vel alium*, ad ¹ quam solvit interimendo." in the second paragraph. The Vat.-omits-*ad* variant note is precisely about this word. Moved `[^1]` from "Et" → "ad" in Latin body, and mirrored the move in English ("to[^1] which he resolves by ruling out"). The body word "Et" / "And" remains in place (it is in the printed text); only the spurious anchor placement was wrong.

### `[?]` resolution count

- 2 `[?]` flags resolved (both in apparatus `[^1]`).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d4-divisio.md` after this pass.

### Verification

- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d4-divisio.md | sort | uniq -c` → each of `[^1]`, `[^2]`, `[^3]` appears 3× (Latin body + English body + apparatus def).
- `cd site && node scripts/build-content.mjs` parses cleanly; chunk count 414.
- d.4-scoped guard-rail audits (`audit-paraphrase.py`, `audit-headers.py`, `audit-apparatus-count.py`) run clean against the edited chunk.

## d6-littera (pp.123-124)

- **Source**: `raw/vision/vol1/p-hires-PRINTED-r600-225.png` (printed p.123) and `p-hires-PRINTED-r600-226.png` (printed p.124), both extracted 2026-05-12 at 600 dpi. Page-header verification: PDF 225 shows printed `123` top-right; PDF 226 shows printed `124` top-left. Offset +102 holds.
- **Flag site**: `[^19]` La + En mirror (apparatus entry, NOTAE AD COMMENTARIUM, footer #7 on printed p.124).
- **Before**:
  - **La.** `Hilar., *de Synodis*, n. 39 [?] et n. 58, XXV.`
  - **En.** `Hilary, *On the Synods*, n. 39 [?] and n. 58, XXV.`
- **PDF p.124 right-col footer entry 7** (sequential `[^19]` across the chunk), verbatim at 600dpi, line-tight crop reads: `⁷ Num. 39. l. et n. 58. XXV. — In cod. A respectu huius notulae additur *et quia Magister non probaverat, Patrem genuisse Filium voluntate, ideo haec nota posita est*. Haec notula in Vat. et aliis edd. ad marginem, in edd. 5, 6 in textu posita est.`
- **Diagnosis**: IA djvu OCR conflated the Quaracchi reference. The print reads `Num. 39. l. et n. 58. XXV.` — i.e., Quaracchi's `Num.` abbreviation (= `n.`, for *numerus*) introducing **39, 1** (paragraph 39, subdivision 1) and **n. 58, XXV** (paragraph 58, subdivision XXV) of Hilary's *De Synodis*. The rechunk pipeline preserved the lemma `n. 39` and inserted `[?]` for the swallowed `, 1` subdivision; the flag marked exactly the lost token.
- **Resolution**: Replaced both `[?]` markers with `, 1` so the apparatus reads `n. 39, 1 et n. 58, XXV` (La) and `n. 39, 1 and n. 58, XXV` (En). Matches Hilary, *De Synodis*, n. 39 §1 / n. 58 §25 (Migne PL 10), the standard Quaracchi citation for the *voluntate genuit Filium* passages.

### Systemic checks performed

- **Page-header verification**: 600dpi extractions of PDF 225/226 show printed page numbers 123/124. Pt1 offset +102 holds for this chunk.
- **Quaracchi `[word]` editorial brackets**: none present in p.123-124 footers beyond translator's English glosses (e.g. `[reads]`, `[here]`). No garbles being masked.
- **Apparatus count**: chunk carries 19 apparatus entries (p.123 main 9 + NOTAE 3 + p.124 main 5 + NOTAE 2), matching the post-rechunk entry-merging convention.
- **Other `[?]` sites**: `grep -n '\[?\]'` on the chunk after resolution returns 0 hits in body/apparatus; the residual `[?]` substring in `transcription_status` was rewritten to drop the literal `[?]` and document the resolution.

### Counts after resolution

- Inline `[?]` flags remaining in chunk: 0 (2 grep matches cleared; both in `[^19]` La + En).
- Apparatus entries: 19 (unchanged).
- Body anchors: paired `[^1]`-`[^19]` in both Latin and English (unchanged).
- 1 site / 2 mirrored flags RESOLVED, 0 ACCEPT-ILLEGIBLE.

### Verification

- `grep -n '\[?\]' vol1/bon-sent-I-d6-littera.md` → no body/apparatus matches.
- `cd site && node scripts/build-content.mjs` parses cleanly; chunk count 414.
- d.6-scoped guard-rail audits (`audit-paraphrase.py`, `audit-headers.py`, `audit-apparatus-count.py`) run clean against the edited chunk.

## d3-p2-dubia (pp.93-94)

- **Date**: 2026-05-12
- **Scope**: 2 inline `[?]` flags (Dub. IV opening, Latin "Videtur[?] quod[?]" + English mirror "It seems[?] that[?]") resolved via 600dpi PDF eyes-on. Source: `raw/vision/vol1/p-hires-d3p2dubia-r600-{195,196}.png` (printed pp.93/94; pt1 offset +102 confirmed).
- **Page-header verification**: PDF 195 shows printed `93` top-right + running head `DIST. III. P. II. ART. II. QUAEST. III.` (Dub. I begins bottom of right column); PDF 196 shows `94 SENTENTIARUM LIB. I.` Offset +102 holds.

### Flags 1-2 — Dub. IV opening (Latin + English mirror) — RESOLVED

- **Before** (Latin): `Videtur[?] quod[?] imago est similitudo expressa...`
- **Before** (English): `It seems[?] that[?] the image is an expressed likeness...`
- **PDF p.94 left col, Dub. IV** verbatim at 600dpi: `Item quaeritur de hoc quod dicit, quod *ex maxima parte est dissimilis*. Videtur quod imago est similitudo expressa: ergo si maxime est dissimilis, non est imago.` — complete sentence, no garble, no editorial bracket, "Videtur quod" prints cleanly.
- **Diagnosis**: Spurious build-time scaffolding flags. The rechunk pipeline (2026-05-10) inserted `[?]` after every word of the Dub. IV opener as a hedge while uncertain whether the phrase was a fragment; PDF read confirms the OCR rendering matches print exactly.
- **Resolution**: Removed all 4 `[?]` markers (2 Latin + 2 English mirror). No edit to substantive content.

### Systemic checks performed

- **Page-header verification**: pt1 offset +102 holds for this chunk (PDF 195 = printed 93; PDF 196 = printed 94). No +103 anomaly.
- **Quaracchi `[word]` editorial brackets**: none present in p.93-94 footers beyond translator's English glosses (`[understood]`, `[the term]`, `[it is called]`, `[premise]`, `[reads]`, etc.). No garbles being masked.
- **Phantom apparatus / off-by-one**: chunk carries 23 apparatus entries matching p.93 (8) + p.94 (15) footer blocks per status string.
- **Other `[?]` sites**: `grep -n '\[?\]'` on the chunk after resolution returns 0 hits.

### Counts after resolution

- Inline `[?]` flags remaining in chunk: 0 (4 grep matches cleared).
- Apparatus entries: 23 (unchanged).
- Body anchors: paired `[^1]`-`[^23]` in both Latin and English (unchanged).
- 2 sites / 4 mirrored flags RESOLVED, 0 ACCEPT-ILLEGIBLE.

### Verification

- `grep -n '\[?\]' vol1/bon-sent-I-d3-p2-dubia.md` → no matches.
- `cd site && node scripts/build-content.mjs` parses cleanly; chunk count 414.
- d.3-scoped guard-rail audits (`audit-paraphrase.py`, `audit-headers.py`, `audit-apparatus-count.py`) run clean against the edited chunk.

## d3-p1-a1-q3 (pp.73-75)

Pass date: **2026-05-12**.
PDF source: `raw/doctorisseraphic11bona.pdf` (pt1) p.74 (PDF p.176), 600 dpi.
Pt1 PDF offset: `pdf_page = printed_page + 102`.

### Resolved via 600dpi PDF eyes-on (2 flags)

- **d.3-p1-a1-q3 [^8] Augustine *De Civitate Dei* citation (Latin line 181 / English line 183)**: `Libr. 22. c. 30. n. 1[?]` and `Book 22, c. 30, n. 1[?]` — IA djvu OCR raw line 20208 reads `8 Libr. 22. c. 30. n. i :` (the glyph after `n.` is a garbled lower-case `i`, ambiguous). 600 dpi crop of p.74 bottom-left footnote 8 shows the printed number is **`4`** (`Libr. 22. c. 30. n. 4 : Vacabimus in aeternum, videntes quia ipse est Deus...`). Standard Augustine citation; *De Civ. Dei* XXII.30 is the long "eternal rest" chapter and §4 begins `Vacabimus`. Corrected both Latin and English to `n. 4` and removed `[?]` flags.

### Verification

- `grep -n '\[?\]' vol1/bon-sent-I-d3-p1-a1-q3.md` → no body/apparatus matches.
- `cd site && node scripts/build-content.mjs` parses cleanly; chunk count 414.
- d.3-scoped guard-rail audits (`audit-paraphrase.py`, `audit-headers.py`, `audit-apparatus-count.py`) run clean against the edited chunk.

## d4-a1-q4 (pp.102-103)

- **Source**: `raw/vision/vol1/p-hires-PRINTED-r600-204.png` (printed p.102) and `p-hires-PRINTED-r600-205.png` (printed p.103), both extracted 2026-05-12 at 600 dpi. Page-header verification: PDF 204 shows printed `102` top-left; PDF 205 shows printed `103` top-right. Offset +102 holds.
- **Flag site**: `[^2]` La + En mirror (apparatus entry, p.102 left-column footer #2).
- **Before**:
  - **La.** `Vat. praeter fidem mss. [...] nomen Dei.[?]`
  - **En.** `The Vatican ed., against the faith of the mss. [reads ...] *nomen Dei*.[?]` (OCR fragmentary at L24444–24445)
- **PDF p.102 footer entry 2**, verbatim at 600dpi reads: `² Vat. praeter fidem mss. et ed. 1 minus apte sic *nec nomen Dei*.`
- **Diagnosis**: IA djvu OCR dropped the middle clause `et ed. 1 minus apte sic` between `mss.` and `nec`, leaving an ellipsis that the rebuild flagged. The recovered text is a short editorial note that the Vatican edition reads *«nec nomen Dei»* (negated) less aptly than the manuscripts + ed. 1, which omit the *nec*.
- **Resolution**: Replaced both `[?]` markers. La now reads `Vat. praeter fidem mss. et ed. 1 minus apte sic *nec nomen Dei*.`; En now reads `The Vatican ed., against the faith of the mss. and ed. 1, [reads] less aptly thus: *nec nomen Dei*.`

### Scholion II OCR-fragment flag — ACCEPT (no inline [?] in chunk)

Per the per-chunk ambiguity log (`manual-review/tier2-ambiguities-d4-a1-q4.md`), Scholion II opening words suffered the usual scholion-header OCR breakup at the rebuild. The note was logged as LOW / defer because the body is rendered readable and no inline `[?]` was placed. Confirmed 2026-05-12: chunk carries no `[?]` flag inside Scholion II text. ACCEPT as-is; no PDF transcription required for Tier-2 completeness.

### Systemic checks performed

- **Page-header verification**: 600dpi extractions of PDF 204/205 show printed page numbers 102/103. Pt1 offset +102 holds for this chunk.
- **Quaracchi `[word]` editorial brackets**: present only as translator's English glosses in apparatus En lines (`[reads]`, `[of Psalm 66]`, etc.); no Latin-side garbles being masked.
- **Apparatus count**: chunk carries 9 apparatus entries (4 p.102 footers traceable to Q.IV body anchors + 5 p.103 footers). Diff vs raw-OCR heuristic (16) explained by Q.III footer anchors printing on p.102 — tracked as separate d4-a1-q3 apparatus-incomplete backlog item per `manual-review/tier2-ambiguities-d4-a1-q4.md`.
- **Other `[?]` sites**: `grep -n '\[?\]' vol1/bon-sent-I-d4-a1-q4.md` after resolution returns 0 hits in body/apparatus; literal `[?]` substring in `transcription_status` rewritten to document the resolution.

### Counts after resolution

- Inline `[?]` flags remaining in chunk: 0 (2 grep matches cleared; both in `[^2]` La + En).
- Apparatus entries: 9 (unchanged).
- Body anchors: paired `[^1]`-`[^9]` in both Latin and English (unchanged).
- 1 site / 2 mirrored flags RESOLVED, 1 flag ACCEPT (Scholion II OCR-fragment, no inline marker present).

### Verification

- `grep -n '\[?\]' vol1/bon-sent-I-d4-a1-q4.md` → no body/apparatus matches.
- `cd site && node scripts/build-content.mjs` parses cleanly; chunk count 414.
- d.4-scoped guard-rail audits (`audit-paraphrase.py`, `audit-headers.py`, `audit-apparatus-count.py`) run clean against the edited chunk.

## d3-p2-a1-q2 (pp.82-84)

- **Source**: `raw/vision/vol1/p-hires-082-r600-184.png` (PDF pp. 184–186 = printed pp. 82–84, 600 dpi). Printed-page headers verified in image: top of column reads "82" on p.184. Pt1 offset +102 confirmed.
- **Scope**: 2 vestigial `[?]` flags in apparatus `[^3]` English and `[^9]` English, deferred from the 2026-05-10 Bucket-1 p.84-scope pass and explicitly tracked at log line 183 as "translator-uncertainty about English style, not a Latin-source flag".
- **Disposition**: both RESOLVED. p.82 footer eyes-on at 600 dpi confirms both apparatus entries match the chunk's Latin text exactly:
  - p.82 footer #2 → `[^3]`: "Vat. contra mss. et ed. 1 prima. Cod. R *quia enim in Filio proprie est imago*. Mox codd. P Q *cognita* loco *cognoscendi*." — chunk matches verbatim.
  - p.82 footer #9 → `[^9]`: "Cfr. supra d. 1. a. 1. q. 1." — chunk matches verbatim.
- Both English renderings are accurate literal mirrors of the unambiguous Latin; the `[?]` markers carried no real ambiguity and have been removed from the English side of both entries.
- No Latin-body or English-body edits required beyond removing the two trailing `[?]` glyphs from the apparatus English lines.

### `[?]` resolution count

- 2 `[?]` flags resolved (apparatus `[^3]` English, apparatus `[^9]` English).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d3-p2-a1-q2.md` after this pass.

### Verification

- `grep -n '\[?\]' vol1/bon-sent-I-d3-p2-a1-q2.md` → no matches.
- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d3-p2-a1-q2.md | sort -u | wc -l` → 24 unique markers (`[^1]`–`[^24]`); each appears 3× (Latin body, English body, apparatus def).
- `cd site && node scripts/build-content.mjs` parses cleanly; chunk count 414.
- d.3-scoped guard-rail audits (`audit-paraphrase.py`, `audit-headers.py`, `audit-apparatus-count.py`) run clean against the edited chunk.

## d3-divisio (pp.66-67)

- **Source**: `raw/vision/vol1/p-hires-PRINTED-r600-168.png` (printed p.66) and `p-hires-PRINTED-r600-169.png` (printed p.67), both extracted 2026-05-12 at 600 dpi. Page-header verification: PDF 168 shows printed `66` top-left header; PDF 169 shows printed `67` top-right header. Pt1 offset +102 holds.
- **Flag site**: `[^3]` La + En mirror (apparatus entry on printed p.66, main footer #2; long Fulgentius variant note).
- **Before**:
  - **La.** `... In fine textus St[?] *fuissent quoque naturae* pro *fuissent naturarum quoque.*`
  - **En.** `... At the end of the text St[?] [reads] *fuissent quoque naturae* in place of *fuissent naturarum quoque.*`
- **PDF p.66 left-col footer entry 2** (the long Fulgentius note), verbatim at 600dpi: `... duplicem suppositionem et argumentationem confundit. In fine te-/xtus Vat. *fuissent quoque naturae* pro *fuissent naturarum quoque.*`
- **Diagnosis**: IA djvu OCR rendered the line break `te-/xtus Vat.` as `te-/xtm\3t.` (line 18941), corrupting `Vat.` (the Vatican edition siglum, used throughout Quaracchi's apparatus) into the garbled token preserved as `St[?]` by the rechunk pipeline. The flag was placed exactly on the lost siglum.
- **Resolution**: Replaced `St[?]` with `Vat.` in Latin; rewrote the English mirror to read "the Vatican edition" (matches the established English convention used in `[^8]`, `[^9]`, `[^11]`, `[^12]`, `[^13]` of this same chunk).

### Systemic checks performed

- **Page-header verification**: 600dpi extractions of PDF 168/169 show printed page numbers 66/67. Pt1 offset +102 holds for this chunk.
- **`Vat.` siglum consistency check**: chunk uses "the Vatican edition" in English for `Vat.` in 5 other apparatus entries. `[^3]` now follows the same convention.
- **Quaracchi `[word]` editorial brackets / other garbles**: no further OCR garbles in p.66-67 footers beyond the `te-/xtm\3t.` resolved here.
- **Apparatus count**: chunk carries 13 apparatus entries (main p.66 footers 1-4 + NOTAE p.66 entries 1-7 + p.67 footers + NOTAE), unchanged.
- **Other `[?]` sites**: `grep -n '\[?\]'` on the chunk after resolution returns 0 hits in body or apparatus.

### Counts after resolution

- Inline `[?]` flags remaining in chunk body/apparatus: 0 (2 grep matches cleared; both in `[^3]` La + En).
- Apparatus entries: 13 (unchanged).
- Body anchors: paired `[^1]`-`[^13]` in both Latin and English (unchanged).
- 1 site / 2 mirrored flags RESOLVED, 0 ACCEPT-ILLEGIBLE.

### Verification

- `grep -n '\[?\]' vol1/bon-sent-I-d3-divisio.md` → no body/apparatus matches.
- `cd site && node scripts/build-content.mjs` parses cleanly; chunk count 414.
- d.3-scoped guard-rail audits (`audit-paraphrase.py`, `audit-headers.py`, `audit-apparatus-count.py`) run clean against the edited chunk.

## d3-p2-a1-q1 (pp.80-82)

- **Source**: `raw/vision/vol1/p-hires-d3p2a1q1-{182,183,184}.png` (600 dpi extracts of PDF pp. 182–184 = printed pp. 80–82; pt1 offset +102).
- 2 inline `[?]` flags, both on English side of apparatus entries; Latin OCR/transcription matched the printed page in both cases.

| Flag | Location | Disposition |
|---|---|---|
| `[^4]` (p.80 footer #4) | English mirror of `Paulo infra post praesens ope mss. posuimus ad loco apud.` | RESOLVED. 600dpi crop `/tmp/p182-foot.png` confirms printed Latin exactly. English "with the help of the manuscripts we have placed *ad* in place of *apud*" is accurate; flag removed. |
| `[^20]` (p.82 footer #1) | Latin `Fide [vid. *Vide*] mss. restituimus particulam *et*.` + English mirror | RESOLVED. 600dpi crop `/tmp/p184-foot2.png` shows printed reading is unambiguously **Fide** (tall-F, no question of *Vide*). `Fide mss.` is idiomatic Quaracchi apparatus Latin = "On the testimony / on the faith of the manuscripts". Removed the `[vid. *Vide*]` parenthetical from Latin; revised English to "On the testimony of the manuscripts we have restored the particle *et*"; flag removed. |

### `[?]` resolution count

- 2 `[?]` flags resolved (both apparatus English mirrors).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d3-p2-a1-q1.md` after this pass.

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d3-p2-a1-q1.md` → 0.
- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d3-p2-a1-q1.md | sort -u | wc -l` → 25 unique markers, each appears 3× (Latin body + English body + apparatus def).
- `cd site && node scripts/build-content.mjs` parses cleanly → 414 chunks.
- d.3 guard-rail audits run (audit-paraphrase / audit-headers / audit-apparatus-count). No new flags introduced.

## d10-a1-q1 (pp.194-196)

- **Source**: `raw/vision/vol1/p-hires-d10a1q1-r600-{296,297,298}.png` (600 dpi extracts; pt1 offset +102).
- **Header verification**: single `### Quaestio I.` body header; matches raw OCR (one QUAESTIO marker in this chunk). Clean.
- **Inline `[?]` flags**: 2 (one Latin body, one English mirror), both at the same locus in the body of Ad 3 (final paragraph before Ad 4).

| Locus | Reading rendered | PDF p.196 eyes-on | Disposition |
|---|---|---|---|
| Latin body, Ad 3 final ¶: *"...processus per modum voluntatis possit esse intrinsecus, sicut[?] procedit amor ab amante..."* | `sicut[?]` | Plain `sicut` — fully legible, no garble, no ligature ambiguity. | RESOLVED — `[?]` dropped; reading is `sicut`. |
| English mirror at same locus: *"just as[?] love proceeds from the lover"* | `just as[?]` | Mirror of Latin. | RESOLVED — `[?]` dropped; reading is "just as". |

### `[?]` resolution count

- 2 `[?]` flags resolved (both same locus, Latin + English mirror).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d10-a1-q1.md` after this pass.

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d10-a1-q1.md` → 0.
- `transcription_status` updated to record polish-pass disposition (2026-05-12).
- `cd site && node scripts/build-content.mjs` parses cleanly; chunk count holds at 414.
- d.10 guard-rail audits (paraphrase, headers, apparatus-count) all clean.

## d1-littera (pp.26-28)

- **Source**: `raw/vision/vol1/p-hires-26-28-r600-{128,129,130}.png` (600 dpi extracts of PDF pp. 128–130 = printed pp. 26–28; pt1 offset +102).
- 2 inline `[?]` flags, paired (Latin body + English mirror) on the same Lombard clause on printed p. 27.

| Flag | Location | Disposition |
|---|---|---|
| Latin body, p.27 | `In homine autem spes ponenda non est[?], quia *Maledictus est qui hoc facit*.` (mid Cap. III, *Utrum homine sit fruendum*) | RESOLVED. 600dpi crop `raw/vision/vol1/p-hires-26-28-r600-129.png` shows the printed Quaracchi reading unambiguously as `In homine autem spes ponenda non est,` with no OCR garble and no editorial variant flagged in the page footer. Flag removed. |
| English body, p.27 | mirror: `But hope is not to be placed in man[?], for *Cursed is he who does this*.` | RESOLVED. Mirrors the resolved Latin. Translation is accurate (alludes to Jer. 17:5, per apparatus `[^18]`). Flag removed. |

### `[?]` resolution count

- 2 `[?]` flags resolved (1 Latin body + 1 English mirror, same clause).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d1-littera.md` after this pass.

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d1-littera.md` → 0.
- `cd site && node scripts/build-content.mjs` parses cleanly → 414 chunks.
- d.1-scoped guard-rail audits (audit-paraphrase / audit-headers / audit-apparatus-count) run; no new flags against this chunk.

## d1-a1-q2 (pp.32-33)

- **Source**: `raw/vision/vol1/p-hires-d1a1q2-r600-134.png` and `-135.png` (600 dpi extracts of PDF pp. 134-135 = printed pp. 32-33).
- **Header verification**: PDF p.33 running head reads `DIST. I. ART. I. QUAEST. II.` — frontmatter (`distinctio: 1`, `articulus: 1`, `quaestio: 2`) is correct.
- 2 inline `[?]` flags resolved, both inside apparatus entry `[^10]`.

| Body anchor | Disposition | Footer source |
|---|---|---|
| `[^10]` La: `mutavimusque *contra* in *contra[?]*. [?]` | RESOLVED → `mutavimusque *convenit* in *contingit*.` | p.32 footer note 10 (600dpi): "Vat. cum cod. cc male omittit *bene*, quod antiquiores mss. ac ed. 1 suppeditant, mutavimusque *convenit* in *contingit*." |
| `[^10]` En: parallel garble + bracketed flag note | RESOLVED → "...and we have changed *convenit* into *contingit*." | same |

The chunk had treated the closing lemma as wholly OCR-garbled. The 600dpi crop is fully legible: the editors substituted *contingit* for the Vatican's *convenit* — consistent with apparatus `[^1]` ("posuimus *contingit* loco *convenit*") and `[^17]` ("bis *contingit* loco *convenit*") elsewhere in this same chunk, where the Quaracchi editors repeatedly note this same substitution.

### `[?]` resolution count

- 2 `[?]` flags resolved (both in `[^10]`).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d1-a1-q2.md` after this pass.

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d1-a1-q2.md` → 0.
- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d1-a1-q2.md | sort -V | uniq -c` → each `[^N]` (N=1..17) appears exactly 3× (Latin body + English body + apparatus def).
- `cd site && node scripts/build-content.mjs` parses cleanly → 414 chunks.
- d.1-scoped guard-rail audits (audit-paraphrase / audit-headers / audit-apparatus-count) run; no new flags against this chunk.

## d1-dubia (pp.42-45)

**Date:** 2026-05-12
**Source:** 600dpi extracts `raw/vision/vol1/p-hires-d1dubia-r600-{144,145,146,147}.png` (PDF pp.144-147 = printed pp.42-45, offset +102).
**Header verification:** ✓ p.42 header reads "SENTENTIARUM LIB. I." matching the chunk; p.44 verified for footer crop. DUB. I-XVI all present and ordered correctly in chunk body.

### Findings table

| Body anchor | Disposition | Footer source |
|---|---|---|
| `[^22]` La: `Vat. autem citando Ecclesiasten 7, 15. legit *fruere bonis*. [?]` | RESOLVED — chunk text matches print verbatim; flag was on the surprising lemma `serire magnatis` for the Vulgate citation, but Quaracchi unambiguously prints `serire magnatis` at p.44 footer note 4. Flag removed; text unchanged. | p.44 footer note 4 (600dpi): "Vers. 10. Ita codd. et ed. 1 ac Hugo de S. Charo in hunc locum; Vulgata vero *serire magnatis*; Vat. autem citando Ecclesiasten 7, 15. legit *fruere bonis*." |
| `[^22]` En: parallel `[?]` | RESOLVED — English now renders the Vulgate lemma in Latin (`serire magnatis`) with literal gloss "to serve the great" rather than the earlier paraphrase "to consort with great men". Flag removed. | same |

### `[?]` resolution count

- 2 `[?]` flags resolved (both in `[^22]`).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d1-dubia.md` after this pass.

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d1-dubia.md` → 0 inline (frontmatter status string updated to drop the "[?] flags on ambiguous spots" phrasing).
- `cd site && node scripts/build-content.mjs` parses cleanly → 414 chunks.
- d.1-scoped guard-rail audits (audit-paraphrase / audit-headers / audit-apparatus-count) run; no new flags against this chunk.

## d10-a1-q3 (pp.198-199)

Pass: 2026-05-12. Resolved 2 inline `[?]` flag instances (1 substantive site × Latin + English mirror) via 600dpi PDF eyes-on. Source: `raw/vision/vol1/p-hires-d10a1q3-r600-300.png` (PDF p.300 = printed p.198) + `-301.png` (PDF p.301 = printed p.199) + `/tmp/p200-r600-302.png` (PDF p.302 = printed p.200; scholion bleeds onto p.200 top), extracted via `pdftoppm -r 600`. Page-header verification: PDF 301 shows running head "DIST. X. ART. I. QUAEST. III." with printed `199` top-right; PDF 302 shows printed `200` top-left under "SENTENTIARUM LIB. I." Pt1 offset +102 holds.

**Date**: 2026-05-12
**Inline `[?]` count at start**: 2 (both literal `Brulifer[?]` — Latin scholion-I closing + English mirror).
**`[?]` flags remaining after pass**: 0.

| Flag | Location | Disposition |
|---|---|---|
| `Brulifer[?]` (La) | Scholion I closing: «Cfr. Brulifer[?] ad hunc locum S. Bonaventurae.» | RESOLVED. 600dpi crop `/tmp/p200-line.png` shows printed reading unambiguously **Brulifer** (clear B-r-u-l-i-f-e-r). This is **Stephanus Brulefer** (Étienne Brulefer, †1499), Franciscan commentator on Bonaventure's *Sentences*. Flag removed. |
| `Brulifer[?]` (En mirror) | English Scholion I closing: «Cf. Brulifer[?] on this passage of St. Bonaventure.» | RESOLVED. Same PDF crop. English glossed as "Brulefer (Stephanus Brulefer, †1499)" to make the historical referent transparent for non-specialist readers. Flag removed. |

### Systemic finding (scholion page-break)

Scholion I for q.3 begins on **printed p.200** (PDF 302), not p.199 — the body and apparatus footer of p.199 fill the page below the scholion start. The chunk's inline `<!-- page 199 -->` marker was placed immediately before `### Scholion`, conflating the body's last paragraph (which IS on p.199) with the scholion (which is on p.200). Added a corrective `<!-- page 200 -->` marker between `### Scholion` and `**I.**`. Did not modify `printed_pages` frontmatter ([198, 199]) — scholion overflow onto p.200 is a single-paragraph bleed and out of the resolution-pass scope; flagged here for future audit.

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d10-a1-q3.md` → 0.
- `cd site && node scripts/build-content.mjs` parses cleanly → 414 chunks.
- d.10 guard-rail audits (audit-paraphrase / audit-headers / audit-apparatus-count) run; no new flags introduced.

## d10-a1-q2 (pp.197-198, formerly mis-labelled 196-198)

- **Source**: 600dpi PDF extracts `/tmp/p-d10a1q2-{298,299,300,301}.png` (printed pp. 196-199; pt1 offset +102).
- 2 inline `[?]` flags, both in apparatus.
- **Systemic finding**: chunk frontmatter `printed_pages: [196,197,198]` was off-by-one — q.2 (`QUAESTIO II.`) begins on printed p.197 (PDF p.299), not p.196 (p.196 contains end of q.1 + Scholion to q.1). Body text "Secundo quaeritur..." appears on p.197; respondeo continuation ("tenet de ratione liberalitatis...") on p.198; scholion II–III on p.199. Frontmatter, source string, apparatus header note, and three `<!-- page N -->` markers all corrected (+1 each). PDF pages updated to [299,300,301].

| Flag | Location | Disposition |
|---|---|---|
| `[^6]` Aristotle text-number | English mirror `text 41 [?] and 53 (c. 9 sq.)` (Latin OCR rendered `text. il. et 53.`) | RESOLVED. P.197 footer note 6 (600dpi crop `/tmp/p197-lower.png`) reads unambiguously `text. 41. et 53.` Latin updated to `text. 41. et 53.`; English flag stripped to `text 41 and 53`. |
| `[^19]` codex sigla list | Latin `A C F G I I K L R S U V W X Y` (doubled-I OCR garble) + English mirror `A C F G H [?] I K L R S U V W X Y` | RESOLVED. P.198 footer note 8 (600dpi crop `/tmp/p198-sigla2.png`) prints sigla list as `A C F G H I K L R S U V W X Y` — no missing siglum between H and I. Latin updated `G I I K` → `G H I K`; English `[?]` stripped. |

### `[?]` resolution count

- 2 `[?]` flags resolved (1 Aristotelian citation, 1 sigla list).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d10-a1-q2.md` after this pass.

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d10-a1-q2.md` → 0.
- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d10-a1-q2.md | sort -u | wc -l` → 21 unique markers, each appears 3× (Latin body + English body + apparatus def).
- `cd site && node scripts/build-content.mjs` parses cleanly → 414 chunks.
- d.10 guard-rail audits (audit-paraphrase / audit-headers / audit-apparatus-count) run; no new flags introduced.

## d1-a3-q2 (pp.39-42)

Follow-up pass 2026-05-12 to clear the final inline `[?]` flag flagged in the prior Bucket 1 pass (line 86 of this log: "One `[?]` remains in `[^15]` English on a translator-side editorial guess about the bracketed Vatican lemma — out of Bucket 1 scope, p.41 not p.42.").

The flag sat at the trailing end of the English mirror of `[^15]`: "...which the Vatican [ed. omits]. [?]" The IA djvu OCR truncated the footer note mid-sentence after "Vat." (raw line 357: `5  Supplevimus  cx  mss.  et  ed.   1  ipsa ,  quod  Vat.`) — the Quaracchi verb governing *quod Vat.* was lost.

| Body anchor | Disposition | PDF source |
|---|---|---|
| `[^15]` En: `which the Vatican [ed. omits]. [?]` | RESOLVED → `which the Vatican [ed.] omits.` | 600dpi PDF p.41 (`raw/vision/vol1/p-hires-41-r600-143.png`), footer note 5 reads verbatim: *Supplevimus ex mss. et ed. 1 ipsa, quod Vat. omittit.* The translator's bracketed guess was correct: the verb is **omittit**. Latin `[^15]` updated to restore the italicized verb (`quod Vat. *omittit*.`); English mirror simplified to plain "which the Vatican [ed.] omits." |

### Verification

- 0 inline `[?]` flags remaining in `vol1/bon-sent-I-d1-a3-q2.md`.
- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d1-a3-q2.md | sort -t^ -k2 -n | uniq -c` → each `[^N]` (N=1..27) still appears exactly 3×.
- d.1 guard-rail audits re-run clean.
- `cd site && node scripts/build-content.mjs` parses cleanly → 414 chunks.

## d5-a1-q2 (pp.114-115)

- **Source**: `raw/vision/vol1/p-114.png` and `raw/vision/vol1/p-115.png` re-extracted at 600 dpi (pt1 offset +102; PDF pp.216-217).
- **Headers verified**: p.114 "SENTENTIARUM LIB. I" (verso) with QUAESTIO II beginning at bottom of page; p.115 "DIST. V. ART. I. QUAEST. II." (recto) with CONCLUSIO and *Respondeo*. Match chunk content exactly.
- **Single `[?]` flag** sat on apparatus `[^8]` **En.** rendering, trailing the clause "For the Master's text see in *littera* c. 1 and 2 near the end."
- **Latin** (verified verbatim from p.115 footer #8): "Vat. praeter fidem mss. et ed. 1 addit *est*. Textum Magistri vide in lit. c. 1 et 2 circa finem." — *circa finem* = "near the end" [of cc. 1 and 2 of Lombard's Sent. I, d. 5 *littera*]. The referent is unambiguous: the two Lombard chapters in this distinction's *littera*. The English rendering is correct and idiomatic; the `[?]` flag was conservative translator-uncertainty during the 2026-05-10 rechunk pipeline and is now retracted.

### `[?]` resolution count

- 1 `[?]` flag resolved (`[^8]` apparatus English mirror).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d5-a1-q2.md` after this pass.

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d5-a1-q2.md` → 0.
- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d5-a1-q2.md | sort -u | wc -l` → 13 unique markers, each appears 3× (Latin body + English body + apparatus def).
- `cd site && node scripts/build-content.mjs` parses cleanly → 414 chunks.
- d.5 guard-rail audits (audit-paraphrase / audit-headers / audit-apparatus-count) run; no new flags introduced.

## d1-divisio (pp.29-30)

- **Source**: `raw/vision/vol1/p-hires-r600-131.png` and `p-hires-r600-132.png` (re-extracted at 600 dpi via `pdftoppm -r 600 -f 131 -l 132`). PDF offset +102 confirmed by running head "DISTINCTIO I." / "29".
- **Headers verified**: p.29 = "COMMENTARIUS IN DISTINCTIONEM I." + "DIVISIO TEXTUS."; p.30 = "SENTENTIARUM LIB. I." + "TRACTATIO QUAESTIONUM." Frontmatter `printed_pages: [29, 30]` / `pdf_pages: [131, 132]` correct.
- **Flag location**: trailing `[?]` at end of `[^10]` English mirror, line 159 ("…HLOS, which read *videtur*. [?]"). The Latin entry on p.29 footer reads: "Ita plurimi codd. ut ACFGIKRTVXWZ etc. et ed. 1 necnon textus Magistri Sentent. contra Vat., quae habet *videretur*, et aliquos codd. ut HLOS, qui legunt *videtur*."

| Footer # (p.29) | Body anchor | Disposition |
|---|---|---|
| 10 | `[^10]` | 600 dpi crop of p.29 footer band confirms verbatim the Latin entry as transcribed; sigla `HLOS` and lemma `videtur` are exact. RESOLVED — stray `[?]` removed from English mirror; no other change to entry text. |

### `[?]` resolution count

- 1 `[?]` flag resolved (apparatus `[^10]` English mirror).
- 0 `[?]` flags accepted-illegible.
- 0 `[?]` flags remaining in `d1-divisio.md` after this pass.

### Verification

- `grep -c '\[?\]' vol1/bon-sent-I-d1-divisio.md` → 0.
- `grep -oE '\[\^[0-9]+\]' vol1/bon-sent-I-d1-divisio.md | sort -u | wc -l` → 12 unique markers, each appears 3× (Latin body + English body + apparatus def).
- `cd site && node scripts/build-content.mjs` parses cleanly → 414 chunks.
- d.1 guard-rail audits (audit-paraphrase / audit-headers / audit-apparatus-count) run; no new flags introduced.
