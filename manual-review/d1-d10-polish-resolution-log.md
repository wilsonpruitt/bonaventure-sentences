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
