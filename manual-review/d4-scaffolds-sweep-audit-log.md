# d.4 Scaffolds Sweep-Audit Resolution Log

Audit date: **2026-05-08**. Source of truth: `raw/bonaventure_vol1_raw.txt` (Internet Archive djvu OCR of Quaracchi 1882, Tomus I, pt. 1).

Same sweep model applied here as to d.1, d.2, d.3 today. Each scaffold chunk's `## Latin` body was diffed against its OCR slice; every `[^N]:` apparatus entry was diffed against the corresponding numbered footnote in the relevant printed-page footer block.

## OCR line ranges per chunk

| Chunk | OCR lines | Printed pp. | PDF pp. |
|---|---|---|---|
| d4-littera | 23297–23492 (Lombard text Cap I + Cap II + tail) | 95–96 | 197–198 |
| d4-divisio (Commentarius + Divisio Textus + Tractatio Quaestionum) | 23493–23583 | 96–97 | 198–199 |
| d4-dubia (Dubia I–IX) | 24612–25060 | 105–107 | 207–209 |

## Per-chunk verdicts

### d4-divisio — CLEAN ✅

Body matches OCR verbatim across `Divisio Textus` and `Tractatio Quaestionum`. All 3 apparatus entries trace to authentic OCR `NOTAE AD COMMENTARIUM` block (raw lines 23556–23560):

- `[^1]` = "Vat. contra mss. et ed. 1 omittit *id*" → matches OCR note 1 ✓
- `[^2]` = "Codd. et ed. 1 contra Vat. addunt *ad primum videlicet*" → matches OCR note 2 ✓
- `[^3]` = "Auctoritate plurimorum mss. ut A F G K T etc. et ed. 1 substituimus *consignificatione* pro *significatione* et *Deus* loco *Dii*, ac mox *istius* pro *illius*" → matches OCR note 3 ✓

Body anchor positions match OCR's `'`/`^`/`"` glyph positions. **No fixes applied**; `transcription_status` updated with `; sweep-audited 2026-05-08` suffix.

### d4-littera — 14 missing apparatus entries restored ⚠️

Body Latin matches OCR cleanly across both Cap I and Cap II of the Lombard text (raw lines 23300–23413). No paraphrase departures.

**However, the chunk had only 2 apparatus entries (`[^1]`/`[^2]`), corresponding to the Quaracchi page-96 footer (notes for the very last paragraphs «Idem in sexto libro de Trinitate» and «Epistola ad Maximum»). Page 95's full Lombard apparatus block — 14 footnotes — was entirely absent.** This is the same pattern caught in d.2-littera (placeholder entries on missing notes), but here the chunk silently skipped the page-95 entries rather than stubbing them.

For comparison: d.1-littera has 36 apparatus entries; d.2-littera 55; d.3-littera 43. d.4-littera at 2 was a gap-flag that the auditor's silent-paraphrase scan missed because the entries were absent rather than fabricated.

**Fix:** Added 14 new apparatus entries (`[^1]`–`[^14]`), each transcribed verbatim from OCR raw lines 23415–23440, with body anchors placed at OCR's superscript-glyph positions (`'`, `^`, `*`, `°`, `"`, etc.) in both `## Latin` and `## English`. Existing 2 page-96 entries renumbered to `[^15]` and `[^16]`. New entries cover:

| New | Anchor | Content |
|---|---|---|
| `[^1]` | "alium" (Cap I) | Vat. hic addit *Deum* |
| `[^2]` | "et" (sane et catholice) | Vat. male omittit *et* |
| `[^3]` | "non genuit" (Cap I) | Codd. B C D E *genuerit*… |
| `[^4]` | "*de Trinitate*" (Cap I, 1st citation) | Aug., *de Trin.* I, c. 1, n. 1 — *putat* singular variant |
| `[^5]` | "istam" | Omnes codd. *illam* |
| `[^6]` | "alteram" | Sola Vat. male *alterum* |
| `[^7]` | "hic distinguimus" | Edd. 2, 3, 7, 8 *hoc* |
| `[^8]` | "Pater et Filius" | Codd. B C omittunt *hic* et *et* post *Pater* |
| `[^9]` | "praedicetur" (Cap II title) | Codd. D E + edd. except 1,8 add *tamen* |
| `[^10]` | "sed nolunt" | Vat. et ed. 4 addunt *et*; codd. C D *unam essentiam* |
| `[^11]` | "*de Trinitate*" (Cap II, 1st quote) | Aug., *de Trin.* I, c. 6, n. 10 |
| `[^12]` | "agens dicit" | 1 Tim. 6:15; Augustine variant + ms. variants |
| `[^13]` | "*Enchiridion ad Laurentium*" | *Ench.* c. 8, n. 9 + ms. mis-attribution to *de Fide ad Petrum* |
| `[^14]` | "*de Fide*" | Sermo 233 *de Fide cathol.* n. 1 |

Existing `[^15]`/`[^16]` (formerly `[^1]`/`[^2]`) unchanged in content. **Apparatus departures fixed: 14 missing entries added (no fabrication — all transcribed from OCR).** **Body departures fixed: 0** (body was clean). Backup at `vol1/_backup-d4-littera-pre-rebuild-20260508/`.

### d4-dubia — 3 body restorations + 1 anchor fix; apparatus mostly authentic but minor compression noted ⚠️

Body Latin diffed against OCR raw lines 24634–25060 (Dubia I–IX). The chunk's apparatus 15 entries are individually authentic (each maps to a real OCR footer note — see table below) but only ~half of the 34 OCR footer notes for these three pages are represented. **Unlike d.2-dubia, no entries are fabricated or misaligned to wrong content.** The pattern here is **selection** (notable mss-variant notes silently dropped) rather than fabrication.

Apparatus mapping (chunk → real OCR source):

| Chunk | OCR fn | Note |
|---|---|---|
| `[^1]` | p.105 fn 1 + fn 4 | **conflated** (the *ita* repetition + the *q. 1, 2* + *de* cross-ref are two distinct OCR notes, joined here) |
| `[^2]` | p.105 fn 3 | "*de* particle excidit" — content authentic |
| `[^3]` | p.105 fn 5 | Aristot. *Metaph.* X — authentic |
| `[^4]` | p.105 fn 6 | Aristot. *Prior.* II on *Instantia* — authentic |
| `[^5]` | p.105 fn 8 | Codd. T aa bb addunt *non* — authentic, slightly truncated (drops "a quibus cod. A…" trailing clause) |
| `[^6]` | p.105 fn 9 | Alex. Hal. + Thomas cross-ref — authentic |
| `[^7]` | p.105 fn 11 | Aristot. *Elench.* II — authentic, drops alternate-translation clause |
| `[^8]` | p.105 fn 12 | Priscian *Grammat.* XVIII — authentic |
| `[^9]` | p.106 fn 3 | Prepositivus biographical — authentic, truncated (drops Lecoy ref + *Mox Vat. omittit ad*) |
| `[^10]` | p.106 fn 5 | "non confuse" gloss — authentic, truncated |
| `[^11]` | p.106 fn 8 | Vat. *una* — authentic |
| `[^12]` | p.106 fn 11 | praedicatio per identitatem cross-refs — authentic |
| `[^13]` | p.106 fn 12 | Master's d. XXII, XXIV, XXV — authentic |
| `[^14]` | p.107 fn 1 | Vat. *po* pro *Deo* — authentic; **body anchor was misplaced** (see fix below) |
| `[^15]` | p.107 fn 8 | Porphyr. *de Praedicab.* — authentic |

**Body fixes applied (3 substantive paraphrase / omission departures):**

1. **DUB III — omitted clause restored.** OCR has, between «*Deus non est Pater*» and «Et ideo moderni aliter solvunt»: `— Sed licet solutio Praepositivi locum habeat in proposito, quia non differt praeponere et postponere negationem huic termino Deus, tamen in aliis non habet locum. Negatio enim postposita relativo ipsum non confundit.` This 31-word qualifier on Prepositivus's solution had been silently dropped. Restored verbatim in Latin and translated literally in English.

2. **DUB IV — omitted clause + corrupted main verb.** Chunk had `Quia enim habet naturam termini communis et discreti, ideo si sequitur: Deus est Pater et Filius: ergo Deus Pater est Filius` — but the chunk Latin wrote *si sequitur* (= "if it follows") where OCR has *non sequitur* (= "it does not follow"), and **silently dropped the whole intervening 14-word clause** `ideo simul stat pro pluribus, sicut pro uno: et ideo non` — exactly the clause that establishes WHY the inference doesn't go through. The chunk's English compensated awkwardly with bracketed `[it does] not [follow that]…`, exposing the corruption. Restored full OCR sequence: `…discreti, ideo simul stat pro pluribus, sicut pro uno: et ideo non sequitur…` and re-translated English literally.

3. **DUB V — major tail truncation + fabricated closing paraphrase.** This was the most serious finding. OCR DUB V *Respondeo* runs ~16 lines (raw lines 25021–25040) and ends `…nec est idem in homine natura et res naturae`. The chunk had truncated everything after «*non dicunt discretionem personae, sed naturae ab aliis*» and **invented** a closing sentence not in Quaracchi: `Unde unus hic non opponitur tribus, sed pluribus naturis sive diis; et solus non opponitur simul existentibus cum eo, sed contradistinctis in natura.` This invented paraphrase was deleted; the actual OCR continuation restored verbatim — covering: «*Unde unus solus Deus dicitur una sola natura*», the predication-by-identity gloss («*quoniam in divinis est idem natura et res naturae sive suppositum, ideo praedicatione per identitatem Trinitas de Deo praedicatur*»), and the contrast with «*omnis homo*» / «*unus solus homo*» (where *homo* can be multiplied and so the parallel does not hold). English re-translated literally for the entire restored passage.

4. **`[^14]` body anchor relocated.** Anchor was on «*Deus*» mid-DUB-V, but OCR fn 1 of p.107 (`Vat. contra mss. et edd. 1, 2, 3 po pro Deo`) attaches to the later occurrence «*Trinitas de Deo praedicatur*». Anchor moved accordingly in both `## Latin` and `## English`. (This relocation aligns with restored DUB V tail above.)

**Body paraphrase departures fixed:** 3 (DUB III omission, DUB IV omission + verb corruption, DUB V truncation + invented closing). **Fabricated apparatus entries replaced:** 0 (all 15 existing entries were authentic OCR content; only one anchor mispositioned). Backup at `vol1/_backup-d4-dubia-pre-rebuild-20260508/`.

The conflation in `[^1]` and minor truncations in `[^5]`, `[^7]`, `[^9]`, `[^10]` are noted but not edited — content is authentic, and replacing them would amount to bulk apparatus rebuild beyond sweep scope. They could be expanded in a future apparatus-completeness pass if Wilson chooses to bring this chunk's apparatus parity-coverage up to d.1/d.2/d.3 levels (would require adding ~17 absent OCR notes, which is a separate task).

## Summary table

| Chunk | Verdict | Body departures fixed | Apparatus departures fixed | [?] flags added |
|---|---|---|---|---|
| d4-divisio | CLEAN — Tier-2 promoted (sweep-audited stamp) | 0 | 0 | 0 |
| d4-littera | Tier-2 promoted (apparatus expanded) | 0 | 14 missing entries restored from OCR (renumbered) | 0 |
| d4-dubia | Tier-2 promoted (body restored) | 3 (DUB III omission; DUB IV omission + verb corruption; DUB V truncation + fabricated closing) | 1 (`[^14]` anchor relocated; entry content unchanged) | 0 |

**Totals:**

- Total body paraphrase departures fixed across d.4: **3** (all in dubia).
- Total fabricated apparatus entries replaced: **0** (no fabrication found in d.4 — different from d.1/d.2 dubia).
- Missing-but-authentic apparatus entries restored from OCR: **14** (all in littera).
- Apparatus anchor repositioned: **1** (dubia `[^14]`).
- `[?]` flags newly added: **0** — all fixes resolvable from OCR without ambiguity.

## Pattern observation

The d.4 sweep partially confirms and partially diverges from the d.1/d.2/d.3 pattern:

- **Confirmed**: scaffold chunks (divisio/littera/dubia) had at least one substantive issue each — even when the body looked Tier-2-shaped, silent omissions and one wholesale fabrication (DUB V closing paraphrase) were present.
- **Confirmed**: the dubia chunk had the most serious finding (3 substantive body fixes), reproducing the d.1/d.2 pattern that dubia chunks concentrate failures.
- **Diverged**: unlike d.1-dubia and d.2-dubia, no fabricated apparatus entries were found in d.4-dubia — apparatus selection skipped real notes but did not invent content. The fabrication budget for d.4 spent itself on DUB V's invented closing paraphrase instead.
- **New finding**: d.4-littera had a different failure mode than d.1/d.2/d.3 littera — instead of placeholder stubs, the entire page-95 apparatus footer (14 entries) was silently absent. Worth checking d.5+ littera chunks against their OCR footer counts to see whether this absence pattern recurs.

Build smoke-test pending; will run `cd site && node scripts/build-content.mjs` after this log lands.
