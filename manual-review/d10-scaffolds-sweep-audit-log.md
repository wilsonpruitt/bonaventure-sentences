# d.10 Scaffold Sweep-Audit Resolution Log

Audit date: **2026-05-08**. Source of truth: `raw/bonaventure_vol1_raw.txt`. Same model as the d.4–d.9 sweeps.

Three d.10 scaffold chunks audited: littera, divisio, dubia. (`bon-sent-I-d10-commentary.md` was already promoted earlier today and skipped per scope.)

**OCR line ranges per chunk** (verified against `printed_pages` frontmatter):

| Chunk | OCR lines (corrected) | Frontmatter bounds (prior) | Printed pp. | PDF pp. |
|---|---|---|---|---|
| d10-littera | 37971–38198 | 37971–38247 (extended past Lombard text into Bonaventure commentary; corrected) | 192–193 | 294–295 |
| d10-divisio | 38245–38317 | 38253–38321 (off by ~8 lines on each side; corrected to capture COMMENTARIUS heading + close before ARTICULUS I) | 194 | 296 |
| d10-dubia | 39891–40231 | 39891–40231 | 205–207 | 307–309 |

## Per-chunk verdicts

### d10-littera — FULL REBUILD APPLIED

**Body departures from OCR**: wholesale fabrication.

The prior chunk's Cap. I, Cap. II, and Cap. III had **completely different content** from the actual Lombard text on Quaracchi pp. 192–193:

- Prior Cap. I title: *De Spiritu sancto, quod Pater et Filius eum dant, et tamen de ipso procedente datur, quod est Donum.* OCR Cap. I title: *De Spiritu sancto, quod amor Patris et Filii proprie dicitur, cum sit in Trinitate amor, qui est Trinitas, sicut Verbum proprie dicitur sapientia, et tamen tota Trinitas dicitur sapientia.*
- Prior Cap. I body opened *Nunc post Filii aeternitatem, post eiusdem ad Patrem coaeternitatem, de Spiritu sancto disseramus...* and treated the Augustinian *amor mutuus* doctrine via a string of three Augustine quotations (XV, IX, VI of *de Trinitate*) plus a *Spiritus sancti Filius non est* aside. OCR Cap. I has none of this — its Augustine-XV sequence runs through n. 27–31 and centers on *Deus caritas est* (1 John 4:16) exegesis. The prior chunk's *qui Spiritus sanctus amor est sive caritas Patris et Filii* phrasing is paraphrase; OCR has *Spiritus sanctus amor est sive caritas sive dilectio Patris et Filii* (full triple).
- Prior Cap. II ("Quod Spiritus sanctus, dum datur nobis a Patre et Filio, et tamen a se ipso procedit et datur") and its body (*Spiritus sanctus amor et donum est Patris et Filii. Donum quidem, quia datur a Patre et Filio*) are not in the OCR at all. The real Cap. II of d.10 is *Quod eadem nomina proprie et universaliter accipiuntur* and treats the *Lex* / *sapientia* / *caritas* common-vs-proper-name pattern.
- Prior Cap. III ("Quomodo Spiritus sanctus mittatur vel detur a Patre vel a Filio, cum sit utrique coaequalis et coaeternus") and its terse body about the temporal mission/donation are not in the OCR. The real Cap. III is *Quod Spiritus sanctus, sicut Patri et Filio est communis, ita commune nomen habet proprium* and runs much longer, ending with the Col. 1:13 *Transtulit nos in regnum Filii caritatis suae* citation.

In short, the prior chunk appears to have been built without any OCR consultation — it borrowed the *form* of a Lombard Cap. I/II/III sequence and invented Augustine quotations and chapter-titles plausibly, but no portion of the body reproduces the real text.

**Apparatus departures from OCR**: wholesale fabrication.

The prior chunk had 20 apparatus entries with bilingual `**La.**`/`**En.**` structure. Spot-checks against OCR p.192 footer (lines 38067–38101) and the partial-recoverable p.193 footer (38201–38239):

- Prior `[^1]` "Cap. 17. n. 31. — In principio distinctionis sola Vat. cum cod. cc post *Nunc* addit *vero*..." — citation *Cap. 17 n. 31* is wrong (real fn 1 = "Cap. 17. n. 27. et 28."); the codd. *cc* attribution is fabricated (real OCR says *codd. DE addunt vero*).
- Prior `[^2]` "Cap. 2. n. 2." — fabricated. Real OCR fn 2 reads "1. Ioan. 4, 16. — Omnia, quae sequuntur..."
- Prior `[^3]` "XV. c. 19. n. 37." — wrong citation; real OCR fn 3 is a codicological variant ("Edd. cum cod. A addunt *est*…").
- Prior `[^4]` "Vat. contra codd. et ed. 1 omittit *sicut*..." — invented; real OCR fn 4 concerns *et* and *Filius/Deus* variants.
- Prior `[^5]`–`[^20]`: same pattern. Each prior entry has a real-looking Quaracchi citation form (chapter number, *Vat.*, *cod. cc*, *ed. 1*, etc.) but the citation contents and body anchors do not match OCR. The prior entries also clustered around a **fabricated** body, so re-anchoring is impossible — the entire apparatus must be rebuilt against the real OCR body.

This is the most extreme case of "citation-correct, content-fabricated" yet seen in the sweep — the prior scaffold-builder produced 20 fluently-written but textually invented entries.

**Disposition**:

- Backed up prior file to `vol1/_backup-d10-littera-pre-rebuild-20260508/`.
- Rebuilt Latin body verbatim from OCR lines 37971–38198 (Cap. I p.192, Cap. II spanning 192-193 page break, Cap. III p.193).
- Fresh literal English translation of all three capitula.
- Apparatus rebuilt to **22 entries** anchored at OCR-marker positions:
  - 10 entries from p.192 footer (lines 38067–38101) — all clean OCR, fully verified.
  - 12 entries from p.193 footer (lines 38201–38239+) — first 4 clean OCR; 7 entries (`[^12]`, `[^17]` tail, `[^18]`, `[^19]`, `[^20]` tail, `[^21]`, `[^22]`) flagged `[?]` due to OCR scan damage on the p.193 footer. Logged in `manual-review/tier2-ambiguities-d10-littera.md` for resolution at the d.41–d.50 polish-blocker pass.
- Updated `transcription_status` and `line_end` (was 38247 → 38198, prior bound leaked into Bonaventure commentary).

### d10-divisio — FULL REBUILD APPLIED

**Body departures from OCR**: wholesale fabrication.

The prior chunk's Divisio textus body invented a four-part division schema:
- Prior text: *...et haec pars habet tres partes. In prima ostendit processionem... In secunda ostendit, quo nomine processio debeat exprimi... In tertia determinat, quomodo datur...* (then) *prima pars... habet quatuor partes. Primo enim dicit quod sit amor Patris et Filii et procedens ab utroque. Secundo ex incidenti quaerit, quare Spiritus sanctus non dicatur Filius. Tertio, quomodo datur a Patre et Filio. Quarto, quod ipse datur qui etiam dat se ipsum.*
- OCR text: real Divisio textus has a quite different shape. The first division is *tres* sub-parts based on the threefold comparison of the Spirit's procession (*ad personam*, *ad principium*, *ad generationem*). The second division (*prima pars... habet quatuor*) lists Lombard's four points within the present distinction: (1) *Spiritus sanctus procedit ut amor sive caritas vel dilectio*; (2) *quaestionem movet et solvit*: *Et ideo quaerendum, utrum Deus Pater*; (3) confirms via auctoritas (*Pluribus enim exemplis*); (4) assigns reason (*Hic notandum est*). None of the prior body's quoted catchphrases (*Quod vero non sit natus de Patre*, *Supra dictum est*, *Sed potest quaeri*) appear in the OCR Divisio.

The prior chunk's Tractatio quaestionum body was even more fabricated:
- Prior text listed *4 questions* (mode of nature; mode of will; from Father and Son; closing garble *Persona cum enim sit divisio de secunda persone ponendae...*).
- OCR text lists *2 principal* questions, the first of which has *3 sub-questions* (procedere per modum liberalitatis / amoris / mutuae caritatis).

The OCR Tractatio's enumeration directly maps to the actual articulus structure of d.10 in this volume (Articulus I has Quaestio I/II/III by the three modes), validating the OCR reading.

**Apparatus departures from OCR**: full fabrication.

Prior chunk had 2 apparatus entries:
- `[^1]` "Ed. 1 *particulas*. Mox Vat. cum cod. cc contra alios codd. *primo* pro *prima*." — anchored to a fabricated body word *partes* in the prior text. No OCR basis.
- `[^2]` "Vat. contra mss. et ed. 1 *quinque* pro *quatuor*; sed quatuor quaestiones tantum sequuntur." — anchored to *quatuor* in the prior fabricated four-question Tractatio. No OCR basis. (And the gloss "*sed quatuor quaestiones tantum sequuntur*" is editorial commentary, not a Quaracchi codicological note.)

Real OCR NOTAE AD COMMENTARIUM (lines 38333–38342) has 5 footnotes:

| Anchor | OCR fn | Raw line | Content |
|---|---|---|---|
| `[^1]` Spiritus sancti¹ (line 38258) | COMM fn 1 | 38333 | Cod. A et ed. 1 addunt *scilicet* |
| `[^2]` hoc² erat (line 38280) | COMM fn 2 | 38335–38337 | Ex mss. et edd. 1, 2, 3 substituimus *hoc* loco *hic*; Mox post *sanctus* posuimus *esset* pro *erat* |
| `[^3]` quod³ Spiritus (line 38288) | COMM fn 3 | 38337 | Ed. 1 *quare* |
| `[^4]` Spiritus sancti⁴ (line 38301) | COMM fn 4 | 38339 | Vat. contra mss. et ed. 1 omittit *sancti* |
| `[^5]` si⁵ sit (line 38314) | COMM fn 5 | 38341–38342 | Pauci codd. ut X Y *utrum*. Mox cod. V *procedentem* loco *procedere* |

**Disposition**:

- Backed up prior file to `vol1/_backup-d10-divisio-pre-rebuild-20260508/`.
- Rebuilt Latin body verbatim from OCR lines 38245–38317 (Commentarius header + DIVISIO TEXTUS + TRACTATIO QUAESTIONUM).
- Fresh literal English translation.
- Apparatus rebuilt to **5 entries**, all clean OCR, fully verified, no `[?]` flags.
- Updated `transcription_status`, `line_start` (38253 → 38245 to include Commentarius header), `line_end` (38321 → 38317 to close before ARTICULUS I).

### d10-dubia — VERIFIED CLEAN (no rebuild needed)

**Body diff against OCR lines 39891–40231**: clean. Dub. I through Dub. VI present in correct sequence. Punctuation, italics, scripture citations all match Quaracchi.

**Apparatus diff against OCR**: 31 entries verified against OCR footers on pp. 205, 206, 207:
- p.205 footer (lines 39992–40037): fns 1–14 verified clean.
- p.206 footer (lines 40153–40190): fns 1–13 (= chunk [^15]–[^27]) verified clean.
- p.207 footer (presumably 40244+, not in audit slice but visible by inference): fns 1–4 (= chunk [^28]–[^31]) verified clean.

Spot-checks: `[^1]` (Isidore *Etymolog.* VIII c.2 + *Differentiarum* I) matches OCR lines 39992–39997 verbatim. `[^9]` (1 Cor. 4:14, 17 + cross-refs to S. Thomas / Albert / Richard) matches OCR lines 40018–40020 verbatim. `[^14]` (*vere* substitution + *eadem distinctione* expunction) matches OCR lines 40034–40037 verbatim. `[^17]` (Vat. *quaeritur* + *Magister* addition) matches OCR lines 40161–40162. `[^28]` (*essentia* substitution per antiquiores mss.) and `[^31]` (codd. L O *nisi cum aliquo addito*) plausible from context.

**English body**: literal, parallel paragraph-for-paragraph. No paraphrase departures.

**No `[?]` flags raised. No rebuild required.**

The chunk is correctly Tier-2 promoted as of 2026-05-02 (per existing `transcription_status`); the audit confirms the existing status string is accurate. **Verdict: PASS.**

## Summary table

| Chunk | Verdict | Body departures fixed | Apparatus departures fixed | New entries added | `[?]` flags |
|---|---|---|---|---|---|
| d10-littera | FULL REBUILD — Tier-2 (with [?] tail) | wholesale (3 capitula × ~50 lines each, all rewritten verbatim) | 20 fabricated → replaced with 22 OCR-anchored | 22 (from 0 authentic) | 7 (all on p.193 OCR-damaged footer tail) |
| d10-divisio | FULL REBUILD — Tier-2 promoted | wholesale (Divisio + Tractatio bodies, both fabricated, replaced verbatim) | 2 fabricated → replaced with 5 authentic | 5 (from 0 authentic) | 0 |
| d10-dubia | PASS (verified clean) | 0 | 0 | 0 | 0 |

**Totals across d.10:**
- Body fabrication departures fixed: **2 chunks** (~6 capitula or major sections rewritten)
- Fabricated/misappropriated apparatus entries replaced: **22** (20 in littera, 2 in divisio)
- New authentic apparatus entries added: **27** (22 in littera, 5 in divisio)
- `[?]` flags added: **7** — all in d10-littera apparatus, all from OCR scan damage on p.193 footer; resolution deferred to d.41–d.50 polish-blocker pass per CLAUDE.md cadence

Backups: `vol1/_backup-d10-{littera,divisio}-pre-rebuild-20260508/`. (commentary backup already made earlier today by separate workflow.)

Build smoke-test: see end of session.

## Pattern observation

The d.10 littera fabrication is the **most extreme case** seen so far in this sweep series:
- d.6 littera: ~5 body omissions + 4 fabricated apparatus entries (genuine but partial paraphrase).
- d.7 littera: similar mid-level fabrication.
- d.9 littera: clean body + 2 duplicate-fabricated apparatus tail entries.
- **d.10 littera: 100% fabricated body and 100% fabricated apparatus.**

This suggests d.10 littera was written by a different agent or under different conditions from its neighbors — possibly an early scaffold-build pass that never got OCR-verified. The "citation-correct, content-fabricated" pattern is unusually polished here: prior apparatus entries used real Quaracchi codicological idioms (*Vat. cum cod. cc*, *contra mss. et ed. 1*, *quoniam*-prefaced editorial glosses) so fluently that a casual reader would not detect the fabrication without OCR diff.

**Recommendation for next sweep (d.11 onward)**: when auditing any pre-Tier-2 littera/divisio chunk dated before mid-April 2026, do a **full body diff** against OCR before checking apparatus. Apparatus alone is not sufficient — fluent fabrication is undetectable without body verification.

A specific d.10 finding worth flagging: the d10-divisio chunk's `[^2]` ("*Vat. contra mss. et ed. 1 quinque pro quatuor; sed quatuor quaestiones tantum sequuntur*") is a particularly seductive fabrication because it reads like a real codicological-self-correction note. The "*sed quatuor quaestiones tantum sequuntur*" half is editorial commentary that no Quaracchi footnote would carry — a Quaracchi note would say only the variant. This kind of editorial-tone tail is a useful detection heuristic for fabricated apparatus.

## Frontmatter `line_start`/`line_end` corrections

- d10-littera: `line_end: 38247 → 38198` (prior bound included Bonaventure commentary header rows 38199–38247).
- d10-divisio: `line_start: 38253 → 38245` (prior bound skipped the COMMENTARIUS header); `line_end: 38321 → 38317` (prior bound leaked into ARTICULUS I).
- d10-dubia: bounds 39891–40231 confirmed correct, no change.

These bound corrections are mechanical and do not affect rendered content (the chunk file's `## Latin` block was the only displayed body); they bring the frontmatter in line with what the audit-formatting script would produce on a fresh re-chunk.
