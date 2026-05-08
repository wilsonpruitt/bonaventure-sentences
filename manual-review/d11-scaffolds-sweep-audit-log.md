# d.11 Scaffolds Sweep Audit Log — 2026-05-08

Audit of `bon-sent-I-d11-{divisio,littera,dubia}.md` per the d.4–d.10 sweep methodology. The two articulus-unicus quaestiones (`d11-a1-q1.md`, `d11-a1-q2.md`) are out of scope for this sweep; only the three scaffold chunks were examined.

Prior status (frontmatter): all three chunks were marked "Phase C Tier 2 complete" on 2026-05-02. The 2026-05-08 sweep was a verification pass against raw OCR, looking specifically for the wave-1 damage patterns: apparatus fabrication, body omissions, line-bound leakage, and misplaced page-break HTML comments.

## Per-chunk verdict

### bon-sent-I-d11-divisio  (declared bounds 40498–40549; corrected to 40498–40594)
**Verdict: PASS with bounds correction.**

- `## Latin` body diffs cleanly against OCR lines 40498–40543 (COMMENTARIUS heading + Lombard incipit + DIVISIO TEXTUS + TRACTATIO QUAESTIONUM). Punctuation, italics, and the four cited *ibi* lemmata match Quaracchi.
- The OCR truncates the final word of the second TRACTATIO question at `diffe-` (line 40543). Reconstruction as *differentes* is unambiguous from context (it parallels the d.11 a.1 q.2 title).
- 3-footnote apparatus verified against the on-page apparatus block at lines 40587–40594:
  - [^1] `Sequimur plures codd. ut F H T W etc. cum ed. 1 ponendo *agit* loco *agitur*.` = OCR line 40587–40588. Match.
  - [^2] `Vat. praeter fidem mss. et ed. 1 omittit *iterum*.` = OCR line 40590. Match.
  - [^3] `Vat. absque auctoritate mss. et ed. 1 *convenire* loco *nostra*.` = OCR line 40592–40593. Match.
- Anchor placements `[^1]`, `[^2]`, `[^3]` in the chunk Latin body align with the OCR superscript markers at *agit* (40508), *iterum* (40516), and *nostram* (40526–40527). All three match.
- English translation tracks Latin paragraph-for-paragraph, literal not paraphrased.
- `<!-- page 208 -->` HTML comment correctly placed at the COMMENTARIUS heading (printed page 208).
- **Bounds issue (corrected this sweep)**: declared `line_end: 40549` falls between the body and the apparatus, so the previously-declared bounds did not capture the 3-entry apparatus block at lines 40587–40594, despite the apparatus being correctly transcribed. Extended `line_end` to 40594 and updated `transcription_status` accordingly. Pre-edit frontmatter snapshot at `vol1/_backup-d11-divisio-pre-rebuild-20260508/README.md`.
- No `[?]` flags raised.

### bon-sent-I-d11-littera  (lines 40193–40495; effective body 40248–40435, apparatus 40294–40352 + 40438–40494)
**Verdict: PASS (no rebuild needed).**

- `## Latin` body Cap. I–II diffs cleanly against OCR lines 40248–40435. Punctuation, italics, biblical quotations, and the long Symbol-of-Constantinople quotation all match Quaracchi.
- `## English` body literal and parallel paragraph-for-paragraph; biblical quotations rendered with appropriate italics and italicization of *Filioque*; Augustine quotation block correctly nested.
- 18-footnote apparatus verified against the two on-page apparatus blocks:
  - [^1]–[^9] at OCR p.207 NOTAE block (lines 40294–40352). All nine entries match: Augustine *De Trin.* XV.28.45 reference, Rom 8:9 *ibi/alibi* note, Ioan 15:26, Rom 8:11 *Christum/Iesum*, Matth 10:20, Ioan 14:26 + 15:26, the *integre/integram* note with Abelard cross-reference, the four Councils with dates, and the Greek-Symbol textual variant including the `Τὸ πνεῦμα τὸ ἅγιον` Greek block.
  - [^10]–[^18] at OCR p.208 NOTAE block (lines 40438–40494). All nine entries match: Gal 1:8–9 with Vulgate variants, Tract. 98 in Ioan., Gal 4:6 + Ioan 16:13, Athanasian Creed *Quicumque*, Didymus *Patrolog. Graec.* tom. 39 col. 1063, *consolatione/consolatore* note, Cyril Epist. 17, the long Chrysostom *In Symbolum Apostolorum* note (Antwerp 1614 Keerbergius edition reference, Homil. I + II incipit details, BD codices and 1 Cor 12:11 cross-reference), and the closing 1 Cor 15:33 + Phil 2:11 reference.
  - No fabricated apparatus content. No paraphrase. The Greek-script characters render verbatim.
- Footnote anchor positions verified against OCR superscript markers across the body:
  - [^1] *comprobatur* (40257), [^2] *Et alibi* (40260), [^3] *in Evangelio* (40261), [^4] *ubi legitur* (40263), [^5] *Christus dicit* (40265), [^6] *Et in alio loco* (40267), [^7] near *integre* (see note below), [^8] *celebrata sunt* (40308–40309), [^9] *glorificandum* (40325), [^10] *Galatas* (40370), [^11] *Augustinus* (40373), [^12] *Apostolus dicit* (40391), [^13] *Symbolo fidei* (40404), [^14] *de Spiritu sancto* (40408), [^15] *Item* (40414), [^16] *ait* (40420), [^17] *Symboli* (40425), [^18] *bonos mores* (40431).
  - **Minor anchor-drift on [^7]**: chunk places marker mid-clause at `fidem integre[^7] continente`; OCR superscript actually sits after the immediately following Patre-procedit quote (~line 40307 `Patre procedif`). Both positions refer to the same Quaracchi note ("Paulo ante pro *integre* Vat. cum nonnullis edd. *integram*..."), so the apparatus entry is not mis-anchored to a different referent. Left as-is per the d.9-littera precedent ("minor anchor drift not fabrication").
- `<!-- page 207 -->` and `<!-- page 208 -->` HTML comments correctly placed at the *Cap. I* opening and immediately after *etc.* at the close of the *vivificatorem* quotation, matching the printed-page boundary at OCR line 40326 (printed page 207 ends mid-paragraph in the Symbol gloss).
- No `[?]` flags raised.

### bon-sent-I-d11-dubia  (lines 41693–41932; effective body 41698–41857, apparatus 41771–41812 + 41923–41932)
**Verdict: PASS (no rebuild needed).**

- `## Latin` body Dub. I–IV diffs cleanly against OCR lines 41698–41857. All four dubia present, with the cross-page break (printed pages 217→218) at OCR line 41818 correctly carried by the chunk's `<!-- page 218 -->` HTML comment between Dub. III's first response paragraph and the *Praeterea, alia est ratio* paragraph.
- `## English` body literal and parallel; the Anselm quotation in [^8] correctly transcribed in both languages with `«…»` quotation marks; the technical scholastic terminology (*ratione materiae*, *ratio proprii*, *ratio primi principii*) preserved on first occurrence.
- 17-footnote apparatus verified against the two on-page apparatus blocks:
  - [^1]–[^12] at OCR lines 41771–41812 (page 217 footer). All twelve match: *principalia* supplevimus, Cap 21:21 Glossa + Lyra cross-reference, the four Acts citations (1:15ff / 2:2ff / 15:6ff / 21:18ff with the *toleranda/tolerandum* ed. 1 variant), the *Pro Deo!* / *et quaeritur* Vatican variant, Anselm *De Concordia* q.3 c.6 with its two-block quotation, the *praeterea/propterea* + *intellexerunt/intellexerint* + *praesumptuosa/praesumptuosorum* triple-variant note, the Vatican-marginal-note reformability gloss, the *quare non/quaeritur ratio* variant, and the *immo alias* Vatican-omission note.
  - [^13]–[^17] at OCR lines 41923–41932 (page 218 footer, immediately after the Dub. IV body). All five match: *illud/aliquid/aliquem* triple-variant, the *tunc* addition in Z + ed. 1, *et loqui* addition in bb, John 16:13, and *vel/sive* substitution.
  - No fabricated apparatus content. No paraphrase.
- Footnote anchor positions verified against OCR superscript markers across the body:
  - [^1] *quatuor principalia* (41706), [^2] *super Actus* (41707), [^3]–[^6] each on the four *Actuum* book citations (41708–41712), [^7] *Pro Deo!* (41728), [^8] *Anselmus* (41731), [^9] *propterea* (41739), [^10] *abolenda esset* (41749), [^11] *quaeritur ratio* (41757), [^12] *immo alias* (41761), [^13] *super illum* (41836), [^14] *quia* (41841), [^15] *habet esse* (41847), [^16] *Non loquetur a semetipso* (41851), [^17] *dominium vel* (41855). All seventeen match.
- `## Notes` block contains a substantive doctrinal summary (dub III genitive-of-origin reduction, dub IV *arbitrium = auctoritas*) — this is editorial commentary by the project, not a transcription artifact, and was left intact.
- No `[?]` flags raised.

## Totals

| Chunk | Body diff | Apparatus diff | Anchor positions | Bounds | [?] flags raised | Verdict |
|---|---|---|---|---|---|---|
| d11-divisio | clean | 3/3 match OCR | 3/3 match | corrected (40549→40594) | 0 | **PASS** |
| d11-littera | clean | 18/18 match OCR | 17/18 exact, 1 minor drift | clean | 0 | **PASS** |
| d11-dubia | clean | 17/17 match OCR | 17/17 match | clean | 0 | **PASS** |

## Anomalies

1. **Divisio bounds leakage** (corrected this sweep): the previously-declared `line_end: 40549` excluded the 3-entry apparatus block at lines 40587–40594, despite that apparatus being correctly transcribed in the chunk. This is line-bound bookkeeping drift, not a content error. Frontmatter `line_end` now reads 40594, and `transcription_status` notes the correction.
2. **Littera [^7] minor anchor drift**: marker placed mid-clause at *integre* rather than after the immediately following *Patre procedit* quote; both positions refer to the same Quaracchi variant note. Same disposition as d.9-littera precedent: left as-is.
3. **No fabrication, no body omissions, no misplaced page-break comments** detected across any of the three chunks.

## Build smoke-test

`cd site && node scripts/build-content.mjs`:

```
Built content.json: 1 book(s), 422 questions, 350 translated
```

Clean.

## Backups

- `vol1/_backup-d11-divisio-pre-rebuild-20260508/` — README capturing pre-edit frontmatter snapshot for the only substantive change (divisio `line_end` extension).
- d11-littera and d11-dubia received only `transcription_status` annotation appendages (audit-PASS notes); no body or apparatus changes, so no body backup was taken.

## Comparison with wave-1 (d.4–d.10)

Whereas wave 1 surfaced extensive damage (apparatus fabrication, page omissions, line-bound leakage), d.11 emerges substantially cleaner:

- **No fabricated apparatus entries** in any of the three chunks (contrast d.9-littera [^34]/[^35] and d.9-dubia [^61]).
- **No body omissions** (contrast d.4 / d.5 missing-paragraph patterns).
- **One minor bounds correction** (divisio, mechanical), no leakage into adjacent distinctions.
- **One minor anchor drift** (littera [^7]), well within the d.9-precedent tolerance.

This pattern is consistent with d.11 having been re-set fresh from OCR on 2026-05-02 rather than carried over from a Tier-1 paraphrase. Recommend treating d.11 as audit-cleared.
