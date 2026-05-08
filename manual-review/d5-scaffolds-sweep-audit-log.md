# d.5 Scaffolds Sweep-Audit Log

Audit date: **2026-05-08**. Source of truth: `raw/bonaventure_vol1_raw.txt` (Internet Archive djvu OCR of Quaracchi 1882, Tomus I, pt. 1). Scaffolds audited: `bon-sent-I-d5-{littera, divisio, dubia}.md`.

This continues the d.1 / d.2 / d.3 scaffold-sweep model. d.1-dubia had ALL 6 apparatus entries invented; d.2-dubia had 4 apparatus entries from wrong page anchored on wrong markers + 3 explicit placeholder stubs; d.3-littera was missing page 62 entirely. d.5 scaffolds continue the pattern with **major** structural gaps.

OCR line ranges per chunk (as backfilled, verified against printed_pages frontmatter):

| Chunk | OCR lines (claimed) | OCR lines (verified) | Printed pp. (claimed) | Printed pp. (correct) | PDF pp. (correct) |
|---|---|---|---|---|---|
| d5-littera | 25061–25619 | 25061–25618 ✓ | [108, 109, 110] ✓ | [108, 109, 110] | [210, 211, 212] |
| d5-divisio | 25620–25764 | 25620–25759 (claim overshoots into ARTICULUS I at line 25761) | [110, 111] ✓ | [110, 111] | [212, 213] |
| d5-dubia | 26999–27495 | 26999–27495 ✓ | **[118, 119, 120]** ✗ | **[119, 120, 121, 122]** | **[221, 222, 223, 224]** |

OCR page boundaries (verified by running heads + page-number numerals):

- p.108: 25061–25214 (DISTINCTIO V opening through SENTENTIARUM LIB. I. running head)
- p.109: 25215–25390 (SENTENTIARUM LIB. I. + body, ending before DISTINCTIO V. + 109 marker at 25391/25394)
- p.110: 25391–25545 (DISTINCTIO V. running head + body, ending before SENTENTIARUM LIB. I. running head at 25546)
- p.111: 25546 (top is COMMENTARIUS at 25620; running head DIST. V. ART. I. QUAEST. I. + 111 at 25676/25679)
- p.119: 26905–27048
- p.120: 27049–27196
- p.121: 27197–27350
- p.122: 27351–27495 (ends just before DISTINCTIO VI at 27496)

---

## Per-chunk verdicts

### d5-littera — REBUILD REQUIRED ⚠️ (most severe finding of d.5 sweep)

The chunk reproduces the d.3-littera "missing pages" pattern at far greater scale: it presents only ~25% of the actual Lombard text printed on pp.108–110.

**What the chunk has** (Latin body):
- Distinctio heading + opening question (OCR 25061–25075)
- Three short numbered objections (1–3) up through Augustine *de Trin.* VII citation (OCR 25083–25129) — paraphrased, not verbatim
- The *de Fide et symbolo* counter-objection + brief response (OCR 25131–25147)
- The *Altera pars solutionis* short paragraph (OCR 25148–25156)
- A two-paragraph *De processione Spiritus sancti* synthesis paragraph at the end — **this paragraph is largely composed/paraphrased, not from the OCR**

**What the chunk is missing** (Latin body):
- **All of OCR lines 25158–25608** — roughly 450 lines of Lombard's actual Latin text. This includes:
  - The continuation of the *Praedictis autem videtur contrarium* objection on pp.108–109 (OCR 25158–25218): Augustine's *de Fide ad Petrum* + *de Trinitate* XV citations on `substantia de substantia` and `sapientia de sapientia`
  - The *Solutio Magistri* on pp.109–110 (OCR 25232–25258): Magister's harmonization with Hilary IV.10
  - The *Huic vero etiam* objection from Hilary IV-V-IX-XII (OCR 25259–25313): four quotations from Hilary's *de Trinitate* IV.10, V.37, IX.51 (the long Christological passage about *forma Dei* / *natura unitatis*), and XII.14 (*innascibilis* / *unigenita natura*)
  - The *Quomodo intelligi debeat* solution (OCR 25315–25336): Hilary's *Intelligentia dictorum ex causis* + the resolution
  - **All of Cap. II — *Aliae auctoritates ab Augustino prolatae propositae*** (OCR 25402–25608): the lengthy Augustinian florilegium with extensive *contra Maximinum* II.14, II.15, and II.18 quotations, the *Filii caritatis suae* exegesis from *de Trin.* XV.19.37, the *homoousion* discussion, and the Magister's repeated harmonization formula `Filius substantia de Patre substantia`
  - **All of Cap. III — *Quare Verbum Patris dicatur Filius naturae*** (OCR 25609–25617): the very short final chapter on Hilary V's `Natura Filius est, quia eandem naturam … habet`

**Apparatus state**:
- The chunk's 6 entries are insufficient to cover Lombard's d.5; OCR has roughly **30+ Quaracchi footer notes** scattered across the page-bottom blocks at OCR lines 25171–25213 (p.108 footer, 14 notes), 25339–25390 (p.109 footer, 11 notes), and 25506–25545 (p.110 footer, 14 notes).
- Of the chunk's existing 6 entries:
  - `[^1]` (Aug. V *de Trin.* c. 5, n. 6 *Quod relative dicitur*) — content authentic; in OCR this is footer note 3 at line 25175 ("*Cap. 7. n. 8, ubi: Quod autem relative pronuntiatur*"). **Quaracchi cite is c.7 n.8, not c.5 n.6** — chunk's citation may be from a different reference work, not faithful to OCR.
  - `[^2]` (Cfr. Aug. *de Trin.* I, c. 1, n. 1) — fabricated cross-reference. The OCR footer for this anchor (line 25178 `*Dist. IV. c. I.*`) reads "Dist. IV. c. I." — i.e., a back-reference to the prior distinction in Lombard, NOT to Augustine *de Trin.* I.
  - `[^3]` (Aug. VII *de Trin.* c. 1, n. 2 + extension) — content authentic to Quaracchi footer note 7 (OCR line 25187 "Cap. 1. n. 2; in quo textu...") but the chunk presents it as substantive Augustine quote, not as the textual-variant note Quaracchi actually has.
  - `[^4]` (Ibid c.1 n.2 + cross-ref to VI *de Trin.*) — partly authentic; matches OCR line 25188-9 area structure, but the cross-reference to VI *de Trin.* c. 4, n. 6 is **not in Quaracchi footer** at this position.
  - `[^5]` (*De Fide et Symbolo* c.3, n.4 + editorial gloss "post *ipse* multa sequuntur, quae a Magistro omittuntur") — the citation matches OCR line 25200 ("Num. 4. — Omnes codd. et edd., exceptis Vat. et edd. 4,9, falso sic: in libro de Fide ad Petrum"). The actual Quaracchi note is a textual-variant note about manuscript readings of the source-book attribution, NOT an editorial gloss about omitted material. **`[^5]` is fabricated.**
  - `[^6]` (Cfr. supra d. 4 q. 1 + d. 4 dub. 3 + cross-ref to d. 11 + d. 13) — fully **fabricated** cross-reference. No such Quaracchi footer note at this chunk's anchor.

**Disposition**: Body restoration + apparatus rebuild required. `transcription_status` updated to `FIRST-PASS — major body restoration + apparatus rebuild REQUIRED before Tier 2 promotion ...`.

### d5-divisio — REBUILD REQUIRED ⚠️

The chunk reproduces a smaller version of the same omission-pattern: a structurally meaningful subsection of Bonaventure's *Divisio Textus* commentary is silently dropped, and both apparatus entries are editorial fabrications.

**Body departures**:

1. **OCR lines 25692–25718 omitted** — Bonaventure's four-part division of the **second pars** of d.5 (the part on essentia in ratione *principii*, beginning *Ita etiam non est dicendum*). OCR sub-divides this into: *prima* (essentia non generat), *secunda* (auctoritates contrariae at *Praedictis videtur esse contrarium*), *tertia* (Hilarii auctoritates at *Huic vero etiam contrarium videtur esse*), *quarta* (explanatio per verba Hilarii at *Sed quia haec verba sane vult*). Chunk skips this entirely.
2. **OCR lines 25719–25734 omitted** — the four-part division of the **third pars** (*Dicitur quoque, et frequenter in sacra Scriptura legitur*), which Bonaventure breaks into *prima* (auctoritates), *secunda* at *His verbis praemissis*, *tertia* at *Ostenditur quoque ex illis verbis*, *quarta* at *Et hoc ita debere intelligi*.

The omission is structurally meaningful — these sub-divisions are exactly what Bonaventure's *Divisio Textus* exists to provide. A reader of the chunk currently sees only the first-pars sub-division and so receives a misleadingly truncated picture of Bonaventure's analysis.

**Apparatus state**:

Both `[^1]` (Cfr. supra d.4 *Divisio textus*) and `[^2]` (cross-ref forward to a.2 q.1/q.2 of this same distinction) are **editorial cross-references with no Quaracchi footer-note source**. The OCR for the divisio body (lines 25620–25759) contains no footer-note anchors for the chunk's marker positions; the page-110/111 footers (around lines 25645–25674) belong to Lombard's text on the upper part of the same physical page, not to Bonaventure's *Commentarius* below.

**Recommended for the rebuild**: switch `has_apparatus: true` → `false` and remove the `## Apparatus` block + body markers, OR retain only with explicit "(editorial cross-reference, not from Quaracchi)" tagging. Project convention to date has been to remove rather than tag, so removal is preferred.

**Other corrections applied during this audit**:
- `line_end: 25764` → `25759` (claimed bound overshot into the ARTICULUS I heading at 25761).

`transcription_status` updated to `FIRST-PASS — body restoration + apparatus rebuild REQUIRED ...`.

### d5-dubia — REBUILD REQUIRED ⚠️ (apparatus + body verification)

The chunk lists 11 dubia (I–XI) corresponding correctly to OCR Dub I–XI at lines 26999–27439. However:

**Frontmatter errors**:
- `printed_pages: [118, 119, 120]` is **wrong**. Verified against OCR running heads + page-number numerals: actual coverage is `[119, 120, 121, 122]`. PDF pages correspondingly `[221, 222, 223, 224]`.
- Page-break HTML comments in the body were `<!-- page 118 -->`, `<!-- page 119 -->`, `<!-- page 121 -->`. None matched OCR page-breaks. Mechanically corrected to `<!-- page 119 -->` (start), `<!-- page 121 -->` (between Dub III and Dub IV — approximate; true OCR break is mid-Dub II response at line 27049, but Dub III is wholly on p.120 so this placement preserves a clean Dub-boundary marker for now), `<!-- page 122 -->` (mid-Dub VIII, before "notat intercisionem" — matches OCR break at line 27351). **The page-120 ↔ page-121 boundary fall mid-Dub-IV, not at the Dub-III/Dub-IV boundary**: a pure-OCR rebuild should re-place these.

**Body departures (silent abbreviation)**:

- **Dub II objection** (chunk's *Item secundo obiicitur contra secundam rationem...*) departs from OCR (lines 27065–27075) in three ways:
  1. Chunk: "obiicitur" / OCR: "dubitatur"
  2. Chunk's quotation of Lombard reads "...esset utique genitor eius **rei**, quae ipse est"; OCR has "esset utique genitor eius **quod** ipse est" (no *rei*) followed by Bonaventure's added gloss "*quia essentia dicit quid commune, sicut et hoc nomen Deus*" — **all of which is dropped**.
  3. The chunk omits the closing sentence of the objection: "Similiter videtur hic: Pater generat Deum: ergo etc., pari ratione nec in proposito."
- **Dub II response** is dramatically condensed: OCR lines 27077–27106 contain (a) the *unitas rationis quae admittit distinctionem et quantum ad rem et quantum ad modum* gloss with the *homo esse ab homine / duos esse homines* example (lines 27081–27084); (b) the *unitas rei / distinctivum quod importat distinctionem ut modum* gloss with the *Deus de Deo / non Deus est alius a Deo* example (lines 27086–27091); (c) the closing "loquitur de communi a parte vocis significantis" qualifier (lines 27102–27105). **All three are silently dropped from the chunk's response.**
- Similar abbreviation patterns are likely in Dub III, IV (which has chunk's "Praeterea, deficit ab insufficienti..." block missing — OCR 27223–27229), and Dub VIII–XI. A full body diff is queued with the apparatus rebuild rather than executed in this sweep.

**Apparatus state** — chunk has 10 entries; OCR pp.119–122 footers contain ~42 numbered notes:

- p.119 footer (lines 27021–27046): 7 notes
- p.120 footer (lines 27144–27188): 11 notes
- p.121 footer (lines 27304–27343): 11 notes
- p.122 footer (lines 27441–27493): ~13 notes

Per-entry assessment of the existing 10:

| Entry | Anchor | Verdict | Notes |
|---|---|---|---|
| `[^1]` | Dub IV (Joachim/Lateran IV) | **Authentic** | Matches OCR p.121 fn 6 (line 27321 "Vide supra a.1.q.1.Scholion"). Chunk's text is a tighter paraphrase but content traces. |
| `[^2]` | Dub V (Hilary II.11) | **Suspicious / unverifiable** | OCR has no explicit footer at this anchor; chunk's "Hilarius II *de Trin.* n. 11" appears to be an editorial cite-completion. The cite itself is plausibly correct (the Lombard quotation `Nihil habet Filius...` is from Hilary IV.10 in OCR — see d5-littera at OCR line 25260 — not II.11; chunk's cite may even be **wrong**). Flag for PDF eyes-on. |
| `[^3]` | Dub V (Alex. Hal. cross-ref) | **Authentic** | Matches OCR p.121 fn 8 (line 27329-27330) verbatim. |
| `[^4]` | Dub VII (comitari/consociare ms variants) | **Authentic** | Matches OCR p.121 fn 11 (lines 27337-27341). |
| `[^5]` | Dub IX (Aug. *de Trin.* XV.19.37 *Filii caritatis suae*) | **Authentic** | Matches OCR p.122 fn 2 (lines 27449-27451). |
| `[^6]` | Dub IX (Richardus *de amore gratuito*) | **Partially fabricated** | The "Textum Richardi vide supra d. 2, q. 4" half is OCR p.122 fn 4 (line 27459); the appended "De *amore gratuito* cfr. Richard. a S. Vict., *de Trin.* III, c. 2" is **not in Quaracchi** — editorial gloss. |
| `[^7]` | Dub X (Prov. 8 verses 24-25) | **Partially fabricated** | "Vers. 24–25" matches OCR p.122 fn 7 (line 27468); the appended "De Sapientia in Prov. 8 ut figura Filii Dei vide late S. Bonav. infra d. 27, p. II, q. 2" is **fabricated** cross-reference. |
| `[^8]` | Dub X (Anselm *Monolog.* c.42 + Aristot. *de Gen. anim.*) | **Authentic** | Matches OCR p.122 fn 8 (lines 27471-27479) verbatim, including Aristotle cross-ref. |
| `[^9]` | Dub XI (Anselm *Monolog.* c.8) | **Authentic** | Matches OCR p.122 fn 13 (line 27493 "Cap. 8") — chunk expands abbreviation to full citation, acceptable. |
| `[^10]` | Dub XI (cfr. infra d.8 p.II dub.2 + *ordinaliter* gloss) | **Fully fabricated** | No such note in OCR p.122 footer block (lines 27441–27493). The whole entry is invented. |

**Missing apparatus** (real Quaracchi footer notes the chunk does not surface):
- Dub I objection: OCR p.119 fn 7 (line 27044, *cum universale ponitur* variant) belongs at "ponatur pro relativo".
- Dub I response: OCR p.119 fn 6 (line 27039, *datio* / *quoniam* variants) belongs at the Respondeo opening.
- Dub II objection: OCR p.119 fn 5 (line 27032, the long *quod si generatio communicat substantiam* variant) belongs at the *eius quod ipse est* citation; OCR p.120 fn 1 (line 27144, *quod*/*et* variant) belongs at "tunc enim videretur **et** notaretur"; etc.
- Dub II response: OCR p.120 fn 5 (line 27159, *secundum / distinctivum* variant) belongs at the *recipit distinctivum* clause.
- Dub III objection: OCR p.120 fn 7 (line 27168, the long *causa* definition note citing Aristotle Phys. II + Metaph. II/V) belongs at "causa enim est cuius esse sequitur aliud"; OCR p.120 fn 8 (line 27174, *locutio*/*solutio* variant) at "praedicta locutio".
- Dub III response: OCR p.120 fn 11 (lines 27183–27188, the long *sapientia bene supponit pro relativo* restoration) belongs at the closing of the response.
- Dub IV objection: OCR p.121 fn 1 (line 27304, *ibi* transposition) at "et ita est ibi quaternitas"; OCR p.121 fn 2 (line 27310, *et* particle restoration) at "et unus est Deus".
- Dub IV response: OCR p.121 fn 5 (line 27318, *quia* / *ideo* / *et sic* variants) at "et ideo ignoranter Ioachim..."
- Dub V objection: OCR p.121 fn 7 (line 27323, *ergo* restoration) at "ergo cum essentiam acceperit"
- Dub VI objection: OCR p.121 fn 9 (line 27332, *sanctum* addition) at "ad Spiritum sanctum"
- Dub VII objection: OCR p.121 fn 10 (line 27334, *aliud*/*dicendum* variants) at "Si tu dicas..."
- Dub VIII response (page break): OCR p.122 fn 1 (lines 27441-27445, the *cum*/`et` + *invariabile* / *invariabilitatem* variants) at "et illud nunc semper est et invariabile"
- Dub IX objection: OCR p.122 fn 3 (line 27453, *Ad* / *quod propter* variant) at "Si propter hoc..."
- Dub X objection: OCR p.122 fn 5 (line 27461, *quia*/*quod* variant) at "sicut dicit Augustinus, **quod**"; OCR p.122 fn 6 (lines 27463-27465, *de signiflcatione genitivi* cross-ref to d.3 p.II dub.3) at "ex vi declarationis essentiae"
- Dub XI objection: OCR p.122 fn 10 (line 27484, *de* / *ex* variant) at the *ex aliquo* clause; OCR p.122 fn 11 (line 27487, *ergo* / *simili modo* variant) at "ergo cum non habeat materiam"; OCR p.122 fn 12 (lines 27490-27493, *creatum* / *creatura* variant + the long *Item quod est ex nihilo, est vertibile* deletion note) at "est creatum: ergo etc."

The body anchors `[^1]` through `[^10]` are misnumbered relative to OCR fn order (OCR has authentic content the chunk has labeled `[^1]–[^9]` at the wrong dubia) but the **content** of `[^1], [^3], [^4], [^5], [^8], [^9]` is authentic and reusable — only `[^2], [^10]` are fully invented and `[^6], [^7]` are partly invented.

**Disposition**: Apparatus rebuild required. Same scale as d2-dubia (~30 entries). `transcription_status` flagged accordingly.

---

## Mechanical fixes applied this sweep (no rebuild executed)

- **d5-littera**: `transcription_status` updated; backup at `vol1/_backup-d5-littera-pre-rebuild-20260508/`. No body or apparatus edits applied — too large to do safely in the sweep window.
- **d5-divisio**: `line_end: 25764` → `25759`; `transcription_status` updated; backup at `vol1/_backup-d5-divisio-pre-rebuild-20260508/`. No body or apparatus edits applied.
- **d5-dubia**: `printed_pages: [118, 119, 120]` → `[119, 120, 121, 122]`; `pdf_pages: [220, 221, 222]` → `[221, 222, 223, 224]`; `source` string updated; page-break HTML comments renumbered (`<!-- page 118 -->` → `<!-- page 119 -->` at start; `<!-- page 119 -->` → `<!-- page 121 -->` at the Dub III/IV boundary; the misplaced `<!-- page 121 -->` between Dub IV/V removed; new `<!-- page 122 -->` inserted mid-Dub VIII at "diversa nunc" / "diverse nows" boundary, in both Latin and English bodies); `transcription_status` updated; backup at `vol1/_backup-d5-dubia-pre-rebuild-20260508/`.

## Summary table

| Chunk | Verdict | Body departures (counted) | Fabricated apparatus entries | [?] flags added |
|---|---|---|---|---|
| d5-littera | REBUILD REQUIRED | ~450 OCR lines of Latin missing (entire Cap. II + Cap. III + most of Cap. I after the first ~10 paragraphs); existing body is largely paraphrased rather than verbatim | 3 fully fabricated (`[^2]`, `[^5]`, `[^6]`); 3 paraphrased-from-real-content with citation issues (`[^1]`, `[^3]`, `[^4]`); ~25+ real Quaracchi footer notes never captured | 0 (rebuild deferred) |
| d5-divisio | REBUILD REQUIRED | ~40 OCR lines silently omitted (pars-II + pars-III sub-divisions); body otherwise faithful | 2 fully fabricated (`[^1]`, `[^2]`); chunk likely should switch to `has_apparatus: false` | 0 (rebuild deferred) |
| d5-dubia | REBUILD REQUIRED | Multiple silent abbreviations confirmed in Dub II (3 separate omissions); same pattern likely in Dub III–XI but not exhaustively diffed in this sweep; printed_pages frontmatter wrong; page-break markers wrong | 1 fully fabricated (`[^10]`); 2 partly fabricated (`[^6]`, `[^7]`); 1 suspicious cite (`[^2]`); ~30 real Quaracchi footer notes never captured | 0 (rebuild deferred) |

**Totals (this sweep)**:
- Body paraphrase / omission departures **identified** (not yet fixed): ~500+ OCR lines of dropped Latin text across the three chunks; multiple confirmed abbreviation episodes in d5-dubia Dub II; mass omission in d5-littera Cap. II + Cap. III.
- Body paraphrase departures **fixed**: 0.
- Fabricated apparatus entries **identified**: 6 fully fabricated + 5 partly fabricated/suspicious across the three chunks.
- Fabricated apparatus entries **replaced**: 0 (rebuild deferred per d2-dubia model).
- Frontmatter / structural fixes applied: d5-divisio line_end correction; d5-dubia printed_pages + pdf_pages + source + page-break HTML comments.
- `[?]` flags added inline: 0 (none needed — every divergence is resolvable from OCR; the work is volume, not ambiguity).

## Pattern observation

The d.5 sweep deepens the d.1/d.2/d.3 pattern: scaffold chunks (littera, divisio, dubia) at the front of Volume I were generated by a **lower-fidelity pipeline** that (a) silently abbreviates Latin bodies, (b) fabricates apparatus cross-references that *look* like Quaracchi footer notes but are not in the OCR, and (c) sometimes ships radically truncated pages — d.3-littera dropped page 62 entirely; d.5-littera drops two whole capitula and most of the Augustinian florilegium on `substantia / essentia` that is the heart of Lombard's distinction.

Specifically for d.5, the surviving short body in d5-littera covers only the first reason-against-essentia-generation triad and the *de Fide et symbolo* counter-objection, then jumps to a synthetic *De processione Spiritus sancti* paragraph that is composed for narrative closure rather than transcribed from OCR. The Lombard text continues for ~3× more material than what the chunk represents.

This is the most severe scaffold gap surfaced so far — recommend prioritising d.5 in the next rebuild wave alongside d2-dubia (which is similarly queued).

## Build smoke-test

To run after this sweep's mechanical edits:

```
cd site && node scripts/build-content.mjs
```

Expected: build passes; chunk count unchanged; no `[^N]:` parser errors. (Mechanical edits are confined to frontmatter + page-break comments + transcription_status strings + one `<!-- page 122 -->` insertion in each body — none of these touch apparatus parser surface area.)
