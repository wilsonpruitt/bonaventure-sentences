# d.2 Sweep-Audit Resolution Log

Audit date: **2026-05-08**. Source of truth: `raw/bonaventure_vol1_raw.txt` (Internet Archive djvu OCR of Quaracchi 1882, Tomus I, pt. 1). All d.2 chunks span OCR lines 15794–18259 (printed pp. 46–62, PDF pp. 148–164).

This is the same sweep model used for d.1 (which surfaced 30+ wholesale fabrications in apparatus). Each chunk's `## Latin` body was diffed against its OCR slice, and every `[^N]:` apparatus entry was diffed against the corresponding numbered footnote in the OCR footer block for the relevant printed page.

**OCR line ranges per chunk** (verified against `printed_pages` frontmatter):

| Chunk | OCR lines | Printed pp. | PDF pp. |
|---|---|---|---|
| d2-littera | 15794–16313 | 46–49 | 148–151 |
| d2-divisio (Commentarius + Tractatio Quaestionum) | 16314–16494 | 49–50 | 151–152 |
| d2-a1-q1 | 16495–16889 | 50–52 | 152–154 |
| d2-a1-q2 | 16890–17108 | 52–54 | 154–156 |
| d2-a1-q3 | 17109–17359 | 54–56 | 156–158 |
| d2-a1-q4 | 17360–17785 | 56–58 | 158–160 |
| d2-dubia | 17786–18259 | 59–62 | 161–164 |

## Per-chunk verdicts

### d2-a1-q1 — CLEAN ✅

Body matches OCR verbatim. Apparatus entries 1–18 all map to authentic OCR footer notes:

- p.51 footer fns 1–11 (raw lines 16644–16712) → chunk `[^1]`–`[^10]` (chunk's `[^4]` consolidates OCR fns 4+5)
- p.52 footer fns 1–8 (raw lines 16822–16867) → chunk `[^11]`–`[^18]`

`transcription_status` promoted to canonical Tier-2 string. **No fixes applied**.

### d2-a1-q2 — CLEAN ✅

Body matches OCR (lines 16890–17108). All 13 apparatus entries trace to authentic OCR footer notes on p.53 (raw lines 16970–17019). No paraphrase divergences in either body or apparatus. **No fixes applied**; promoted to Tier 2.

### d2-a1-q3 — CLEAN ✅

Body matches OCR. 12 apparatus entries map cleanly to OCR footer notes on p.55 (raw lines 17131–17162) and p.56 (raw lines 17267–17317). The chunk's `[^6]` is a deliberate cross-reference back to `[^5]` because the same OCR footer note 5 is anchored at two body positions (`omnes personae` and `sed hoc est inconveniens`); the OCR's footer note 5 reads "*Vat. contra mss. et ed. 1. hic et circa flnem argumenti post si dicersis ponit et loco sed*" — the *hic et circa finem* explicitly authorizes two anchors. Acceptable per project convention. **No fixes applied**; promoted to Tier 2.

### d2-a1-q4 — 1 fix applied

Body matches OCR (lines 17360–17785). 11 apparatus entries map to authentic OCR notes on p.56 (raw lines 17437–17464), p.57 (raw lines 17584–17604), and p.58 (raw lines 17608–17783). Chunk `[^11]` consolidates OCR fns 8+9 — content authentic, structurally compressed.

**Fix:** `[^1]` originally read `Ioan. 16, 13 (recte 16, 15)` with English `John 16:13 [recte 16:15]`. The "(recte 16, 15)" gloss is **not in Quaracchi** — OCR raw line 17437 reads simply "loan. 16, 13: Omnia quaecumque habet Pater mea sunt." The editorial correction was added by a prior pass; though factually correct (the verse is John 16:15), it is not in the source apparatus. Reverted to verbatim OCR; promoted to Tier 2.

**Apparatus departures fixed**: 1.

### d2-divisio — 2 fixes applied

The divisio chunk (Bonaventure's *Commentarius in Distinctionem II* + *Divisio Textus* + *Tractatio Quaestionum*, raw lines 16314–16494) had **substantive body departures from OCR**:

1. **Body word substitution**: chunk read *rationalem* / *rationaliter* in two places (line 16410 and 16415 of OCR). OCR main text reads *rationabilem* / *rationabiliter*; *rationalem* is a codd. I cc variant noted in chunk apparatus `[^3]` itself, but the chunk had silently adopted the variant in the body. Reverted to OCR main-text reading.

2. **Omitted clause**: chunk's "Et patet ordo. Prius enim est credere, quam intelligere, et similiter prius est intelligere..." — OCR (line 16418) reads "Et patet ordo. Prius enim **et verius est eam credere quam intelligere; multi enim credunt, qui non intelligunt;** et prius similiter est intelligere quam sermone exprimere." A 13-word clause about "many believe who do not understand" had been silently dropped. Restored.

Apparatus content (entries `[^1]`–`[^6]`) checked against OCR's NOTAE block (raw lines 16389–16395 + page-bottom footer of page 49) — all authentic; `[^6]` consolidates three OCR notes (Vat construction inversion, *pars* supply, *Secundo vero specialiter* note) but content matches. No apparatus rebuild needed.

**Body paraphrase departures fixed**: 2 (one word substitution + one omitted clause). **Apparatus**: clean. Promoted to Tier 2.

### d2-littera — 3 fixes applied

The Lombard text (raw lines 15794–16313, printed pp. 46–49). Body matches OCR closely. Apparatus has 55 entries spanning footnotes from pp. 46, 47, 48, 49.

**Fixes:**

1. **`[^6]` body word**: chunk apparatus read "August., l. de Trin. c. 3. n. 5, sed circa principium ***aliud*** additum est a Magistro." OCR raw line 15905 reads "*scilicet* additum est a Magistro." Reverted *aliud*→*scilicet* and adjusted the English accordingly.

2. **`[^14]` placeholder replaced**: was `*[placeholder for repeated apparatus number in source; see [^13]]*`. The body anchors `[^13]` (on *de Fide ad Petrum*) and `[^14]` (on *usian*) point to OCR fns 13 (Fulgentius/Ruspensi attribution) and 14 (Greek *ousía* / *homousion* error) respectively. The chunk had previously placed OCR fn 14's content at `[^13]` and left `[^14]` as a stub. Filled in `[^14]` with the authentic *ousía / homousion* note from OCR raw lines 15930–15931, with a parenthetical noting the redundancy with the (correctly) reused content at `[^13]`.

3. **`[^16]` placeholder replaced**: was `*[see [^15]]*`. OCR has fn 15 (the *primo/primum* variant) and fn 16 (Vat addition of *magis*) as separate notes; chunk had collapsed both into `[^15]` and stubbed `[^16]`. Trimmed `[^15]` to just the *primo/primum* content and filled `[^16]` with the *magis* addition from OCR raw line 15936.

**Body paraphrase departures fixed**: 1. **Fabricated/placeholder apparatus entries replaced**: 2. Promoted to Tier 2.

### d2-dubia — APPARATUS REBUILD REQUIRED ⚠️

The dubia chunk reproduces this audit's most serious find. Body Latin matches OCR (raw lines 17865–18258). But the apparatus is **structurally fabricated**, replicating the exact pattern caught in d.1 (which had 30+ wholesale fabrications):

**Misalignment**: The chunk's apparatus entries `[^1]`–`[^4]` cite content from the **page 61 footer** (DUB. VII–IX notes — raw lines 18173–18206), but the body markers `[^1]`–`[^4]` are anchored in **DUB. I–II content on page 59**:

- `[^1]` body anchor at "philosophicis" in DUB. I → real OCR p.59 fn 1 (raw line 17908) is the *philosophicis vs physicis* variant note. Chunk apparatus says "Cod. K addit *substantiae*" — which is actually OCR p.61 fn 1 (raw line 18173).
- `[^2]` body anchor at "occasione" in DUB. I → real OCR p.59 fn 2 (raw line 17927) is about Vat. addition *hoc autem possibile est fieri in via*. Chunk says "Plura de hac re vide d. 31..." — actually OCR p.61 fn 2.
- `[^3]` body anchor at "etiam" in DUB. II → real OCR p.59 fn 3 (raw line 17933) is the *etiam adiecimus* note. Chunk says "Codd. F X et edd. 4, 5 *videtur*" — actually OCR p.61 fn 3.
- `[^4]` body anchor at "comprehendi nisi immensa" in DUB. II → real OCR p.59 fn 4 (raw line 17937) is about Vat. textual corruption. Chunk says "De ista sententia Magistri cfr. infra d. 24..." — actually OCR p.61 fn 4.

**Explicit placeholders**: Three apparatus entries are literal stubs:

- `[^5]`: `*[Editorial note about the "glue of affection" metaphor; cross-reference pending final verification against p. 60 apparatus block.]*`
- `[^8]`: `*[Cross-reference to apparatus on substance vs. person; pending final verification.]*`
- `[^13]`: `*[See [^10] on the dispersione / dispositione variant.]*`

**Disposition**: The body Latin is faithful and translation correct, but the apparatus needs to be **rebuilt from scratch** against the actual OCR footer-note sequence:

- DUB. I → DUB. VI body anchors should reference OCR p.59 fns 1–4 + p.60 fn 1 + p.61 fns 1–2.
- DUB. VII → DUB. X body anchors should reference OCR p.61 fns 3–9 + p.62 fns 1–2.

This is a 1–2 hour task that cannot safely be done as a quick edit during a sweep audit. The chunk's `transcription_status` has been updated to flag the rebuild requirement explicitly:

```
FIRST-PASS — apparatus rebuild REQUIRED before Tier 2 promotion
(sweep audit 2026-05-08 found apparatus entries [^1]-[^5] citing
p.61 footer content but anchored on DUB. I-II body which is on p.59;
entries [^5], [^8], [^13] are explicit placeholders; misalignment
exposes the same fabrication pattern caught in d.1 dubia).
Latin body itself matches OCR.
```

Apparatus rebuild should track these OCR raw-line ranges:

| Body anchor | OCR footer note | Raw lines |
|---|---|---|
| DUB. I `philosophicis` | p.59 fn 1 (philosophicis vs physicis; long Itin. mentis cross-ref) | 17908–17926 |
| DUB. I `occasione` | p.59 fn 2 (Vat addition; cum/post variants) | 17927–17932 |
| DUB. II `etiam` | p.59 fn 3 (etiam adiecimus; cod. dd addit eam) | 17933–17936 |
| DUB. II `immensa` | p.59 fn 4 (Vat textual corruption) | 17937–17940 |
| DUB. II `recidit` | p.60 fn 1 (recidit pro recedit; Vat. continuation) | 18039–18044 |
| DUB. III `Damascenus` | p.60 fn 2 (Damascene De Fide orth. I.9 quote) | 18045–18051 |
| DUB. III `quod` | p.60 fn 3 (Cod R *qui*; operatione/opere) | 18052–18054 |
| DUB. IV `hoc` | p.60 fn 4 (Greek *haec* construction in codd.) | 18055–18056 |
| DUB. IV `et natura` | p.60 fn 5 (cross-ref d.22 q.3, Alex. Hal.) | 18058–18060 |
| DUB. V `pro persona` | p.60 fn 6 (Cod K addition) | 18062–18068 |
| DUB. V `et relationem` | p.60 fn 7 (mss. non favent retention; Cod R variant) | 18070–18075 |
| DUB. V `aliter exponit Hilarius` | p.60 fn 8 (Aug./Hilar. quotes) | 18077–18079 |
| DUB. V `et` | p.60 fn 9 (et adiectum) | 18081 |
| DUB. VI `diversitatem` | p.61 fn 1 (Cod. K addit substantiae) | 18173 |
| DUB. VI `naturae` | p.61 fn 2 (Plura de hac re d.31) | 18175 |
| DUB. VII `videntur` | p.61 fn 3 (Codd. F X edd. 4,5 *videtur*) | 18177 |
| DUB. VII `infra melius patebit` | p.61 fn 4 (cfr. infra d.24 a.2 q.1) | 18179 |
| DUB. VII `disparatione` | p.61 fn 5 (long ms variant note: dispersione/dispositione/dispensatione) | 18181–18184 |
| DUB. VII `talis` | p.61 fn 6 (Vat. contra mss. *taliter*) | 18186 |
| DUB. VIII `quod` | p.61 fn 7 (quod adiectum) | 18188 |
| DUB. VIII `Matthaei ultimo` | p.61 fn 8 (Vers. 19) | 18190 |
| DUB. VIII `consignificatione` | p.61 fn 9 (modo adiectum + Vat creavit deletion) | 18192–18196 |
| DUB. VIII `Proverbiorum octavo` | p.61 fn 10 (Vers. 25; Brescia 1496 + patristic citations) | 18198–18207 |
| DUB. VIII `appropriatione, ut ibi` | p.61 fn 11 (Gen. 1, 1; Vat. omittit *ut*) | 18209–18210 |
| DUB. VIII `Isaiae sexto` | p.61 fn 12 (Vers. 3) | 18212 |
| DUB. VIII `Psalmus` | p.61 fn 13 (66, 6) | 18212 |
| DUB. VIII `Galatas quarto` | p.61 fn 14 (Vers. 4) | 18212 |
| DUB. VIII `Genesis decimo octavo` | p.61 fn 15 (Vers. 2; Vat. apparuerant; Alex. Hal. cross-ref) | 18214–18218 |
| DUB. IX `Matthaei decimo septimo` | p.61 fn 16 (Vers. 3) | 18220 |
| DUB. IX `et clarius` | p.61 fn 17 (Vat. desideratur *et*; long Aug./Thomas/Lyranus etc. cross-refs) | 18222–18234 |
| DUB. X `quae non conveniunt` | p.62 fn 1 (likely about *quae*; not visible in OCR slice) | (verify in PDF) |
| DUB. X `ordinandi` | p.62 fn 2 (Vat. construction change + cod. R/K M X Y ee variants) | 18253–18254+ |

The chunk's existing apparatus already has authentic content for many of these (the "Plura de hac re vide d. 31...", "Codd. F X et edd. 4, 5 *videtur*", etc., are real OCR notes — they're just attached to the wrong body anchors). A careful rebuild will reuse most of the existing translated text but realign anchors and slot in the missing p.59–60 content.

## Summary table

| Chunk | Verdict | Body departures fixed | Apparatus departures fixed | Pending |
|---|---|---|---|---|
| d2-littera | Tier-2 promoted | 1 (fn 6 *aliud*→*scilicet*) | 2 (placeholder [^14], [^16] replaced with real OCR content) | — |
| d2-divisio | Tier-2 promoted | 2 (rationalem→rationabilem; restored omitted clause) | 0 | — |
| d2-a1-q1 | CLEAN — Tier-2 promoted | 0 | 0 | — |
| d2-a1-q2 | CLEAN — Tier-2 promoted | 0 | 0 | — |
| d2-a1-q3 | CLEAN — Tier-2 promoted | 0 | 0 | — |
| d2-a1-q4 | Tier-2 promoted | 0 | 1 (removed «recte 16, 15» editorial gloss not in Quaracchi) | — |
| d2-dubia | APPARATUS REBUILD REQUIRED | 0 (body clean) | — (structural rebuild needed; flagged in transcription_status) | rebuild ~30 apparatus entries against OCR raw lines 17908–18254+ |

**Totals:**

- Total body paraphrase departures fixed across d.2: **3** (1 in littera, 2 in divisio).
- Total fabricated/placeholder/misnumbered apparatus entries replaced: **3** (1 in q4, 2 in littera).
- Major structural finding: **d2-dubia apparatus is fundamentally misaligned + has 3 placeholder stubs** — needs whole-apparatus rebuild before promotion (queued, not done in this sweep).
- `[?]` flags newly added: **0** — all fixes were resolvable from OCR without ambiguity.

Backups for chunks edited: `vol1/_backup-d2-{divisio,littera,a1-q4,dubia}-pre-rebuild-20260508/` (gitignored).

Build smoke-test passed after edits: `Built content.json: 1 book(s), 422 questions, 350 translated`.

## Pattern observation

The d.2 sweep confirms the d.1 pattern: chunks that *look* Tier-2 (formal `**La.**`/`**En.**` apparatus structure, parallel-paragraph body) often have either silent body paraphrase (d2-divisio) or fabricated/misaligned apparatus (d2-dubia). The four quaestiones (q1–q4) in d.2 turned out to be substantively faithful, which is unlike d.1 where even the quaestiones had wholesale fabrication. The litterae and dubia/divisio scaffolds appear to have been generated by a different, lower-fidelity pipeline than the quaestiones in d.2 — worth noting for any future d.3, d.4 audits.
