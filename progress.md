# Translation Progress

Per-step checkbox log. Scope/effort rollup lives in `OPERA-OMNIA-TRACKER.md`;
phase definitions live in `PLAN.md`.

Last synced: 2026-04-14.

## Volume I — *Comm. in I Sent.*
- [x] Raw text scraped — pt. 1 (Dist. I–XXIII), IA: `doctorisseraphic11bona`
- [x] Chunking complete — pt. 1: 130 legacy chunks + prolegomena (131 files)
- [x] Tier 2 rebuild — d. 1–8 (70 chunks) ✅
- [ ] Tier 2 rebuild — d. 9–23 (~80 chunks remaining in pt. 1)
- [ ] Raw text scraped — pt. 2 (Dist. XXIV–XLVIII), IA: `doctorisseraphic12bona`
- [ ] Chunking complete — pt. 2
- [ ] Tier 2 rebuild — pt. 2 (~120 chunks est.)
- [ ] Quality review — pt. 1
- [ ] Quality review — pt. 2

## Volume II — *Comm. in II Sent.*
- [ ] PDF downloaded
- [ ] Raw text scraped (file exists at `raw/bonaventure_vol2_raw.txt` but is empty)
- [ ] Chunking complete (~240 chunks est.)
- [ ] Translation complete
- [ ] Quality review

## Volume III — *Comm. in III Sent.*
- [ ] PDF downloaded
- [ ] Raw text scraped (file empty)
- [ ] Chunking complete (~200 chunks est.)
- [ ] Translation complete
- [ ] Quality review

## Volume IV — *Comm. in IV Sent.*
- [ ] PDF downloaded
- [ ] Raw text scraped (file empty)
- [ ] Chunking complete (~240 chunks est.)
- [ ] Translation complete
- [ ] Quality review

## Volume V — *Opuscula Theologica Selecta*
- [ ] PDF downloaded
- [ ] Raw text scraped
- [ ] *Itinerarium mentis in Deum* translated (Phase E priority 1)
- [ ] *Breviloquium* translated (Phase E priority 2)
- [ ] *De reductione artium ad theologiam* translated (Phase E priority 4)
- [ ] *De mysterio Trinitatis* translated
- [ ] *De scientia Christi* translated
- [ ] *De perfectione evangelica* translated
- [ ] Quality review

## Volume VI — *Comm. in Sacram Scripturam* I (Eccl., Sap., Luke 1–8)
- [ ] PDF downloaded
- [ ] Raw text scraped
- [ ] Chunking complete
- [ ] Translation complete
- [ ] Quality review

## Volume VII — *Comm. in Sacram Scripturam* II + *Collationes in Hexaemeron*
- [ ] PDF downloaded
- [ ] Raw text scraped
- [ ] *Collationes in Hexaemeron* translated (Phase E priority 3)
- [ ] Comm. in Lucam 9–24 translated
- [ ] Comm. in Ioannem translated
- [ ] Quality review

## Volume VIII — *Opuscula Varia Theologica*
- [ ] PDF downloaded
- [ ] Raw text scraped
- [ ] Chunking complete
- [ ] Translation complete
- [ ] Quality review

## Volume IX — *Sermones*
- [ ] PDF downloaded
- [ ] Raw text scraped
- [ ] Chunking complete
- [ ] Translation complete
- [ ] Quality review

## Volume X — Prolegomena, indexes, apparatus criticus
- [ ] PDF downloaded
- [ ] Raw text scraped
- [ ] Scope decision: translate or skip
- [ ] Translation complete (if in scope)

## Pipeline infrastructure (Phase B)
- [x] `tools/apparatus-translate.py` v1
- [x] `tools/apparatus-sigla.json` — Vol I populated
- [x] `tools/extract-pages.py` — pdftoppm vision OCR support
- [x] `tools/build-chunk.py` — scaffold skeletons
- [ ] `tools/vision-ocr-batch.py` — batch vision OCR over page ranges
- [ ] `tools/apparatus-translate.py` v2 — 80% publication-ready target
- [ ] Sigla registries for Vols II–X
- [ ] Automated chunking for Vols II–IV raw text (decision deferred to end of Phase C)
