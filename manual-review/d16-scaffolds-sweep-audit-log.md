# d.16 scaffolds sweep audit log (2026-05-08)

Sweep covering the 3 scaffold chunks listed in the d.16 audit task:
`bon-sent-I-d16-{divisio, littera, dubia}.md`. (The 3 quaestio chunks `bon-sent-I-d16-a1-{q1,q2,q3}.md` exist alongside but are out of scope for this scaffold-focused sweep.)

Auditor methodology: per-chunk, verify chunk bounds against `raw/bonaventure_vol1_raw.txt`, diff `## Latin` body against the OCR slice, diff every apparatus entry against the OCR's `NOTAE AD LIBRUM SENTENTIARUM` / `NOTAE AD COMMENTARIUM` blocks, verify anchor positions, watch for fabricated citations, body omissions, line_start leakage, and misplaced page-break HTML comments.

Build smoke-test: `cd site && node scripts/build-content.mjs` → "Built content.json: 1 book(s), 422 questions, 350 translated". Clean.

## Bound sanity check (against raw OCR)

- d.15 last line: 50414 (`citur Dcitalis quaui Diviirilalis.`) — d.15-p2-dubia tail.
- 50417: `DISTINCTIO XVI.` (d.16 starts).
- 50624: `COMMENTARIUS IN DISTINCTIONEM XVI.` (boundary littera→divisio).
- 50747: blank line after divisio's TRACTATIO listing.
- 51766: `DUB. I.` (d.16-dubia starts).
- 51998: blank line after Dub. V respondeo.
- 51999: `DISTINCTIO XVII.`

All 3 chunk frontmatter line_start/line_end values verified against raw OCR. No leakage across distinction boundaries.

## Per-chunk verdicts

### bon-sent-I-d16-littera.md — CLEAN

- **Bounds**: `line_start: 50417, line_end: 50623`. OCR slice opens with `DISTINCTIO XVI. — De missione Spiritus sancti, quae fit duobus modis, visibiliter et invisibiliter` (line 50417) and runs through Hilary's *de Trinitate* IX block ending `…diligenter nota pieque intellige.` at 50621. Clean boundary; the apparatus block at 50642–50676 (NOTAE AD LIBR for p. 277) belongs to littera's apparatus and is correctly extracted.
- **Latin body**: word-for-word match against OCR for cap. I (276) and cap. II (277). Augustine block-quotes (*de Trin.* II,5,10; II,6,11; IV,19,26; I,7,14; II,1,2) and Hilary's *de Trin.* IX (n. 54) opened/closed correctly; biblical italicizations preserved (*Pater maior me est*, *Donavit ei nomen…*, *Verbum caro factum est*, *Ego et Pater unum sumus*). Page break `<!-- page 277 -->` (line 41) corresponds to OCR running head transition at raw 50546 (mid-cap I → cap II rubric appears one page-block later in OCR stream). Clean.
- **Apparatus** (20 entries):
  - [^1]–[^10] match OCR notes 1–10 of `NOTAE AD LIBR. SENTENTIARTJM` at raw 50504–50545 (printed p. 276 apparatus). Spot-checked [^1] (`Vat. cum aliis edd., exceptis 1, 8, contra codd. *dicto*…`), [^2] (the long *invisibiliter/a* / *sive dari* / *visibiliter* compound), [^7] (`Cap. 19. n. 26. — Locus Scripturae est Gal. 4, 4.`), [^10] (`Ioan. 1, 14.`). All ✓.
  - [^11]–[^20] match OCR notes 1–10 of the p. 277 NOTAE AD LIBR block at raw 50642–50676. Spot-checked [^15] (long *Epist. 170 (olim 66) n. 9* with Maximus-medicus annotation and Hebr. 2,9 tail), [^16] (Cap. 7. n. 14 with the *in*-before-*natura* discussion), [^19] (`Num. 54. — Textus Scripturae est Ioan. 10, 30.`), [^20] (the *donati* vs *donantis* note). All ✓.
  - [^20] inserts an editorial bracketed `[legunt *donati*]` because the OCR is broken at that point (`omnes codd. et edd. 6,8,9 Vat. cum aliis edd. male legit donantis.` — verb missing for the *codd.+edd.* clause). Bracket disclosure is correct editorial practice; not a fabrication.
- **No fabrication detected.** Bilingual `**La.**`/`**En.**` structure consistent. Indent 4 spaces.
- **Anchors**: all 20 markers at OCR-corresponding positions in body. Spot-checked [^1] (after *donatio*), [^4] (after *eis* in the Augustine quote), [^17] (after `Filius sit` before *minor Patre*), [^20] (after `donati` before *confessione*). All ✓.
- `transcription_status` already dated 2026-05-02. Re-affirmed under 2026-05-08 sweep — **no rewrite needed**.

### bon-sent-I-d16-divisio.md — TWO MINOR APPARATUS FIXES

- **Bounds**: `line_start: 50624, line_end: 50747`. OCR slice opens with `COMMENTARIUS IN DISTINCTIONEM XVI.` (line 50624) and runs through `Tertio quaeritur, quibus modis facta sit.` at 50745. Boundary clean.
- **Latin body**: word-for-word match against OCR. The four-tier division (visibilis/invisibilis → visibilem missionem + dubitationem → assignat duplicem modum + altera → tres partes of the dubitatio) and the TRACTATIO QUAESTIONUM listing (3 questions: *quid sit* / *ad quid utilis* / *quibus modis facta sit*) all match OCR verbatim. Page break `<!-- page 278 -->` at line 41 corresponds to OCR running head `278 SENTENTIARUM LIB.` after raw 50548 (the OCR layout in this column places the p. 278 head two paragraph-clusters into the divisio body).
- **Apparatus** (8 entries):
  - [^1] matches OCR's cross-page continuation note 1 from p. 277 `NOTAE AD COMMENTARIUM` (which spans into p. 278 column). Verbatim.
  - [^2]–[^7] match OCR notes 1–6 of p. 278 NOTAE AD COMMENTARIUM at raw 50722–50741.
  - [^8] matches OCR note 7 (`Ex vetustioribus mss. et ed. 1 restituimus *quaeritur*. Paulo post in principio quaestionis restituimus ex codd. et ed. 1 verba: Circa primum proceditur sic, quae desunt in Vat.`). Verbatim.
  - **Two minor textual divergences corrected on 2026-05-08**:
    1. **[^4]** had `ita propositionem **exhibet**: *Similiter secunda pars*, *in qua*, et paulo infra ponit *quae habet hanc dubitationem*` — OCR (raw 50734–50736) reads `ita propositionem **incipit**: Simititer secunda pars , in qua, et paulo infra ponit *quae habet* loco *et habet haec dubilatio*`. Chunk had switched the verb (`exhibet`/`incipit`) and **synthesized** the second lemma `*quae habet hanc dubitationem*` from what OCR presents as a *loco*-construction (`*quae habet*` reads in place of `*et habet haec dubitatio*`). Corrected to match OCR exactly. English follow-through updated.
    2. **[^5]** had `*Haec autem pars, in qua quaestionem prosequitur*` — OCR (raw 50738) reads `*Haec autem pars, in qua **hanc** quaestionem prosequitur*`. Chunk had dropped `hanc`. Restored.
  - These are **paraphrase-class** errors (verb selection + minor lemma drift), not fabrication: the Vat./mss./ed. 1 textual claim was correct, only the wording of the embedded Vat. lemma was off. Treated as polish, not rebuild.
- **No further fabrication detected.** Anchor placements all correct.
- `transcription_status` updated 2026-05-08 to record the [^4]/[^5] fixes against raw lines 50734–50738.
- **Backup**: `vol1/_backup-d16-divisio-pre-rebuild-20260508/bon-sent-I-d16-divisio.md` written before edit.

### bon-sent-I-d16-dubia.md — CLEAN

- **Bounds**: `line_start: 51766, line_end: 51998`. OCR slice opens with `DUB. I.` (line 51766) and runs through `…sed illud verbum est additum in consuetudinem disputantium.` at 51996. Boundary clean (next line is `DISTINCTIO XVII.` at 51999).
- **Latin body**: All 5 dubia (DUB. I–V) match OCR verbatim. The Augustine-Trin / Hebr. 2,9 / Hilary-IX-54 textual scaffolding tracks OCR exactly. Embedded *expositio*-style citations (italicized lemmata, *maior et minor* / *alius et alius* / *paulo minus*) preserved. Page break `<!-- page 286 -->` at line 46 sits between Dub. III's objection cluster and its respondeo, correctly mapping to the OCR running head `286 SENTENTIARUM LIB. I.` between raw 51895 and 51899.
- **Apparatus** (18 entries):
  - [^1]–[^7] match OCR notes 1–7 of the first apparatus block at raw 51820–51843 (printed p. 285 apparatus). Spot-checked [^1] (`Auctoritate antiquiorum mss. et ed. 1 removimus *Dei*…`), [^3] (`Cod. I *intelligendo*; cod. dd *utraque obiectio…*`), [^7] (the long Hebr. 2,9 / Lyrano *natura humanae mentis* / Vat. *super omnes* compound). All ✓.
  - [^8]–[^18] match OCR notes 1–11 of the second apparatus block at raw 51950–51985 (printed p. 286 apparatus). Spot-checked [^8] (Lyranus *Minor ergo Angelis corpore*… long quotation), [^10] (the seven cross-references to Albert / Thomas / Petr. a Tar. / Richard a Med. / Aegid. R. / Dionys. Carth.), [^16] (`Ita vetustiores codd. cum ed. 1, dum Vat. cum recentiore cod. cc *auctoritatem* ponit, sed perperam, quia auctoritas est terminus medius conclusionis eliciendae. Cod. dd *minoritatem*, bene…`), [^18] (`Vat. contra plurimos codd. et ed. 1 *consuetudine*. — De hoc et praecedenti dubio agunt B. Albert., hic a. 13; S. Thom., Petr. a Tar. et Richard., hic in expos. textus.`). All ✓.
- **No fabrication detected.** Bilingual structure consistent; anchors placed at OCR-corresponding positions. Cross-references in [^4] (`Cfr. hic q. 3. ad 1. et 2.`), [^12] (`vide supra d. 8. p. I. dub. 4.`), [^14] (`Vide supra d. 13. dub. 4. et d. 15. p. I. q. 1. ad 2. et 3, ac infra d. 20. a. 1. q. 2. ad 4, et d. 27. p. I. q. 2. ad 3.`) all match OCR exactly.
- **Trailing `## Notes` section** with `[Notes pending]` line (174–176) is harmless scaffolding (no `## Scholion` since `has_scholion: false`). Build parser is heading-sentinel-driven and correctly stops `## Apparatus` extraction without confusion.
- `transcription_status` already dated 2026-05-02. Re-affirmed under 2026-05-08 sweep — **no rewrite needed**.

## Cross-cutting checks

- **Fabricated apparatus replaced**: 0. The two divisio fixes ([^4] verb + [^4] lemma synthesis, [^5] dropped *hanc*) are paraphrase-class drift, not invention — the underlying Vat./mss. textual claim and footnote anchor were already correct.
- **Authentic apparatus added** beyond what was previously in chunks: 0. All 3 chunks already at full apparatus from the 2026-05-02 rebuild; this sweep only verifies fidelity and applies micro-corrections.
- **Body omissions detected**: 0.
- **line_start leakage across distinction boundaries**: 0. d.15 ends at 50414; d.17 starts at 51999. All 3 chunks' bounds sit cleanly within 50417–51998.
- **Misplaced `<!-- page N -->` HTML comments**: 0. All page-break comments map to OCR running-head transitions.
- **`[?]` flags in chunks**: 0 newly introduced; 0 pre-existing. No `manual-review/tier2-ambiguities-d16-*.md` files needed for the scaffold sweep.

## Structural anomalies

- None requiring intervention. The d.16 scaffold trio (littera + divisio + dubia) holds up cleanly against the wave-1+2 baseline. The 2026-05-02 build is high-quality, with only the two divisio apparatus polish fixes flagged in this sweep. d.16 is **NOT** a member of the d.10-littera-fabrication-cluster; this is a healthy post-2026-05-02 fresh-OCR rebuild.

## Backups

- `vol1/_backup-d16-divisio-pre-rebuild-20260508/bon-sent-I-d16-divisio.md` (pre-2026-05-08 polish state, preserved before the [^4]/[^5] textual corrections).
- The pre-existing `vol1/_backup-d16-pre-rebuild-20260502/` directory (containing the pre-2026-05-02 rebuild state of all 6 d.16 chunks) remains in place untouched.

## Conclusion

Wave 1 (d.4–d.9) damage patterns — apparatus fabrication, body omissions, line_start leakage, misplaced page-break comments — are **NOT present in d.16 scaffolds**. The d.10-style "polished fabrication using real Quaracchi codicological idioms" pattern is **NOT present**. The 2026-05-02 rebuild was high-quality; only two minor apparatus polish corrections (one paraphrased verb + one dropped word) needed in `bon-sent-I-d16-divisio.md`. No commits made.

Build smoke-test: passes (422 questions, 350 translated, no parser errors).
