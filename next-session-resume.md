# Next session — Vol II **DISTINCTION 2 littera** Tier-2 (session 14 — d.2 RE-CHUNKED)

Updated 2026-05-15 at close of session 13 (d.2 re-chunk pass complete — 17 correct skeletons; d.1 fully Tier-2).

Head commit: `ee509db` — vol2 d.2 re-chunk pass session 13 (17 correct skeletons, splitlines-bug fix). Resume commit follows.

## Status

- Vol I COMPLETE (411/411 Tier-2).
- Vol II auto-chunked: 464 skeletons across d.1–d.44.
- **Vol II DISTINCTION 1 COMPLETE — all 17 chunks Tier-2** (sessions 1–12):
  - **pars 1 (9 chunks):** `d1-littera`; `d1-p1-divisio`; `d1-p1-a1-q1`/`a1-q2`/`a2-q1`/`a2-q2`/`a3-q1`/`a3-q2`; `d1-p1-dubia` (DUB I–V; p.38 apparatus backfilled session 5).
  - **pars 2 (8 chunks):** `d1-p2-divisio`; `d1-p2-a1-q1`/`a1-q2`; `d1-p2-a2-q1`/`a2-q2`; `d1-p2-a3-q1`/`a3-q2`; `d1-p2-dubia`. ART. II/III openers folded into a2-q1/a3-q1 (no standalone aN-divisio chunks); every q from a1-q1 on was a full 450 dpi PDF re-set with documented cross-chunk footer splits.
  - Verified 2026-05-15: all 17 `transcription_status` strings start `Phase C Tier 2 complete`.
- **Vol II DISTINCTION 2 RE-CHUNKED (session 13, commit `ee509db`)** — 17 correct skeletons replace the auto-chunker's mislabeled set. **0/17 Tier-2** (all honest skeletons; Tier-2 promotion starts session 14). See "Next" below.
- Site build: 2 books, 873 chunks, **428 translated** (unchanged — d.2 still skeleton).
- No deploy. Wilson's policy: hold until Vol II has meaningful Tier-2 work to show. (d.1 is now substantial — surface a deploy decision to Wilson when convenient; still his call.)

## Open [?] flags parked for d.10 polish-blocker

- `d1-p1-a3-q1` [^21] (*vel inceptio* anchor on p. 33) — footer entry was not separately resolvable in OCR before the SCHOLION block; mapped by content match. Resolution: 600 dpi PDF extract of p. 33 and eyes-on. See `manual-review/tier2-ambiguities-II-d1-p1-a3-q1.md`.
- `d1-p1-a3-q2` — page-mapping in the apparatus crosswalk is approximate where two-column OCR linearization is ambiguous; per-footer content match is faithful, but per-page sequence numbers may be off by one in places.
- `d1-p2-divisio` [^1] — the page-38 footer note-7 anchor: OCR shows an isolated `*` at *In prima*, possibly a divisio-diagram brace rather than a footnote marker. Also the page-38 note-6/7/8 boundary (where the footer splits between p1-dubia and the divisio) rests on two-column content match. See `manual-review/tier2-ambiguities-II-d1-p2-divisio.md`.
- `d1-p1-dubia` *in octavo* — stray `\` OCR glyph after *motorem primum, in octavo* (raw 3308); no distinct page-38 note, treated as covered by note 3's *Subaudi: libro Physicorum* ([^19]). Confirm at 600 dpi (printed p. 38 = PDF p. 60).
- `d1-p2-a1-q1` [^1] — *de Gen. et Corr.* locus reads *text. 56* in the 450 dpi PDF (OCR had *text. 36*); re-confirm at 600 dpi. [^7] cross-ref *tom. I pag. 171* taken from OCR (left edge cropped in the 450 dpi extract). Both low-confidence, non-blocking. See `manual-review/tier2-ambiguities-II-d1-p2-a1-q1.md`.
- `d1-p2-a1-q2` [^8] / [^20] — [^8] (*Supple: supremi*) body anchor sits ambiguously in the two-column Sed-contra-1 (*primae differentiae generis*); [^20] (*Codd. U Y supplent ordinatur*) `°` marker fell in the cascade-damaged *ordo in formis corporalibus* sentence, content-matched to *forma elementi*. Non-blocking; re-confirm at 600 dpi. (No separate per-chunk ambiguities file yet — fold into the d.10 log.)
- `d1-p2-a2-q1` [^1] / [^13] / [^7] — [^1] single anchor after *Magister* carries Lombard + Scripture + Augustine *de Doctr. christ.* (Quaracchi note 4); re-confirm marker not repeated after *Doctrina christiana*. [^13] (*Subaudi cum cod. N Deum* → reply 4 *in laudando*) rests on the two-column p.45-footer linearization at the a2-q1/a2-q2 boundary — re-confirm p.45 footer note 1 is not q2's opener. [^7] (*quodsi non frustra facit*) marker surfaced as a stray `S` glyph (raw 3756), content-matched to Aristot. *de Caelo* p.44 note 5. All non-blocking; fold into the d.10 log.
- `d1-p2-a2-q2` [^12] **RESOLVED (session 10)** / [^4] — [^12]: ~~reply 4's *infra* vs. a3-q1 Fundamentum 1~~ resolved by session-10's 450 dpi p.47 footer read: p.47 footer notes 1–2 (`Dist. II. a. 1. q. 1.`; `Garciones... Du Cange`) are the first two footer entries and both anchor a2-q2 reply 4 (*infra*, *garcioni*); a3-q1's notes begin at footer note 3. a2-q2 [^12] assignment stands; no backfill. [^4] (still open): the Augustine Contra-1 note runs p.45 footer → runover at head of p.46 footer left column; the `...XIV. de Trin. c. 14. n. 20. — Textus seq.... «Sed illa sola [creatura est imago Dei]...»` seam rests on two-column linearization. Non-blocking; fold into the d.10 log.
- `d1-p2-a3-q1` [^12] — the *rationale Angeli est intellectuale* marker (raw 4001, right col) sits in the heavily cascade-bled reply-2/3 region; content-matched to p.48 footer note 7 (`Secundum Dionys., de Div. Nom. c. 7. § 2.`). Secure on content; eyes-on with the other p.48 markers at 600 dpi. Non-blocking; fold into the d.10 log.
- `d1-p2-a3-q2` [^16] / [^20] — [^16]: the page-50-footer note 11 opener (`Nonnulli codd. ut V aa cum Vat. hic subiungunt perfi-`) continues at the head of the page-51 footer left column (`et autem (Vat. nam perficit) non mediante potentia...`); seam rests on two-column linearization at the chunk-internal p.50↔51 boundary. [^20]: chunk's terminal clause OCR-split *Et sic patent quae-* (p.51 L) | *sita* (p.51 R), marker on *sita*; reconstructed *quaesita*, anchored to p.51 footer note 4 (`Vide Scholion ad q. 1.`) — secure (terminal clause, terminal note before the dubia's `Hic c. 4.`). Both non-blocking; fold into the d.10 log.
- `d1-p2-dubia` [^3]/[^4] / [^8] — [^3]/[^4]: DUB I's two terse I-*Sent.* self-refs (*in tractatu de voluntate* / *ostensum in primo libro*) map to consecutive p.51 footer notes `Dist. 43.` / `Dist. 43. a. 2. q. 1. et 2.`; content-order secure (videtur ref before Respondeo ref) but bare loci warrant eyes-on. [^8]: DUB II *ex forma dante bene esse* anchored to p.52 footer note 1 (the long Boethian-*opusculum* summary) by content match in the cascade-bled p.52 left column. Non-blocking; fold into the d.10 log.

## Next: DISTINCTION 2 — `d2-littera` Tier-2 (re-chunk DONE)

**The re-chunk pass is complete (session 13).** All 17 d.2 skeletons now have correct semantic boundaries; the auto-chunker's mislabeled p2/`-dup2`/`-dup3` set is gone. **Session 14 = promote `bon-sent-II-d2-littera` to Tier-2** (then `d2-p1-divisio`, then quaestiones ~1/session). Backup of the pre-rechunk set is at `_backup-d2-pre-rechunk-20260515/` (gitignored).

### d.2 chunk set (17, raw `bonaventure_vol2_raw.txt`, lines 4264–6627; d.3 starts 6628)

`d2-littera` 4264-4417 · `d2-p1-divisio` 4418-4462 · `d2-p1-a1-q1` 4463-4696 · `d2-p1-a1-q2` 4697-4912 · `d2-p1-a1-q3` 4913-5097 · `d2-p1-a2-q1` 5098-5212 · `d2-p1-a2-q2` 5213-5333 · `d2-p1-a2-q3` 5334-5449 · `d2-p1-dubia` 5450-5529 · `d2-p2-divisio` 5530-5554 · `d2-p2-a1-q1` 5555-5743 · `d2-p2-a1-q2` 5744-5886 · `d2-p2-a2-q1` 5887-6125 · `d2-p2-a2-q2` 6126-6244 · `d2-p2-a2-q3` 6245-6381 · `d2-p2-a2-q4` 6382-6500 · `d2-p2-dubia` 6501-6627.

OCR-garbled headers resolved: `DISTmCTIO 11`=DISTINCTIO II (4264); `QU.\ESTIO 11`=QUAESTIO II (4697, p1 a1 q2); `QU.\EST[0 I`=QUAESTIO I (5108, p1 a2 q1). Short ARTICULUS openers fold into each article's q1 (Vol II override step 5). Re-chunk script: `tools/rechunk_d2.py`.

> ⚠ **Vol II rechunk-script bug (fixed session 13, do NOT regress):** the Vol II raw has **1056 form feeds (`\f`)**. Python `str.splitlines()` splits on `\f` too → every line number drifts ~1055 off from `grep`/`awk` (which all boundary numbers are derived with). `rechunk_d2.py` uses `RAW.read_text().split("\n")`. **Every future Vol II rechunk script must do the same** (d.3+). The first run of `rechunk_d2.py` used `splitlines()` and silently produced chunks starting mid-d.1-dubia — caught only by eyes-on PDF cross-check.

### `d2-littera` Tier-2 — discovery complete (session 13), do the build session 14

**ONE littera chunk for the whole distinction** (id `bon-sent-II-d2-littera`, no pars suffix — the d.1 precedent: `bon-sent-II-d1-littera` covers "Pars I et II"). Lombard's d.2 text has Pars I (Cap I–III) and Pars II (Cap IV–VI) **all printed together at raw 4264–4417**; there is **no separate pars-II littera** — pars II commentary (raw 5530) follows pars I dubia directly. (The session-12 recon's "make `d2-p1-littera`… and likewise pars 2" was wrong; corrected by reading the raw.) Template: `vol1/bon-sent-I-d8-littera.md` / `vol2/bon-sent-II-d1-littera.md`.

**Printed pages: 52 (lower-left only) → 53 → 54.** `extract-pages.py --pages` takes **printed** page numbers (it applies +22 internally → `raw/vision/vol2/p-0NN.png` where NN = printed page; `colcrop.py vol2 NN` likewise uses the printed number). Crops already cached at 450 dpi: `/tmp/colcrop/vol2-p05{2,3,4}-{L,R}-{0,1,2}.png` and `raw/vision/vol2/p-05{2,3,4,5}.png`. (`p-074..076.png` were a wrong-offset extract, deleted.)

**Structure verified from the PDF column-band reads (read order = whole L column top→bottom, then whole R column):**
- **p.52 L (lower half only; upper-L + entire R col = the already-committed `d1-p2-dubia` DUB II/III):** DISTINCTIO II header → *"De Angelica itaque natura haec primo consideranda sunt: quando creata fuerit, et ubi, et qualis facta sit, dum primum conderetur: deinde qualis effecta aversione quorundam et conversione quorundam. De excellentia quoque et ordinibus et donorum differentia, et de officiis ac nominibus aliisque pluribus aliqua dicenda sunt¹."* → **CAP. I.** *De Angelis, quando facti sunt.* → *"Quaedam auctoritates² innuere videntur, «quod ante omnem creaturam creati sunt Angeli. Unde illud:…"* (continues p.53).
- **p.53 L:** Cap I tail (*…omnium creata est sapientia, omnia post ipsam facta videntur… requiramus intelligentiam veritatis. — Videtur itaque hoc esse tenendum, quod simul creata est spiritualis creatura… in principio, quia primo facta sunt.*) → **CAP. II.** *Quod nihil factum est ante caelum et terram.* (*Antea enim nihil factum est… quia non fuit tempus³, antequam esset caelum et terra. Unde Augustinus [in li]bro de Trinitate⁴…*).
- **p.53 R:** (de Trinitate⁴ tail …*antequam inciperet tempus.*) → **CAP. III.** *Quod simul cum tempore et cum mundo coepit spiritualis creatura et corporalis.* (*Simul ergo cum tempore facta est corporalis et spiritualis creatura… ut Augustinus⁵ ait «nulla creatura est ante saecula…» — Hieronymus tamen super Epistolam ad Titum… substiterunt»! His verbis quidam adhaerentes dixerunt⁶, cum mundo coepisse tempus…*).
- **p.53 (cont.):** **CAP. IV.** *Ubi Angeli mox creati fuerint.* (*Iam est ostensum, quando creata fuerit angelica natura… Unde Dominus in Evangelio ait: Videbam satanam sicut fulgur de caelo cadentem. Nec appellatur hic caelum firmamentum… quod dicitur empyreum, id est igneum a splendore, non a calore, quod statim factum Angelis est repletum…*).
- **p.54 L:** (*…quod in empyreo omnes Angeli fuerunt ante quorundam ruinam, simulque creati sunt Angeli cum caelo empyreo et cum informi materia omnium corporalium.*) → **CAP. V.** *Quod simul creata est visibilium materia et invisibilium natura, et utraque informis.* (*Simul ergo visibilium rerum materia et invisibilium natura condita est, et utraque informis fuit secundum aliquid, et formata secundum aliquid…*).
- **p.54 R:** (Cap V tail …*per terram, corporalem materiam sine omni qualitate, quae apparet in materia formata.*) → **CAP. VI.** *Quomodo dixerit lucifer: Ascendam in caelum.* (*Hic quaeri solet, si in caelo empyreo fuerunt Angeli, statim ubi facti sunt, quomodo, ut legitur in Isaia, dicit lucifer: Ascendam in caelum et exaltabo solium meum, et ero similis Altissimo? — Sed ibi caelum vocat Dei celsitudinem… id est ad aequalitatem Dei.*) → then **COMMENTARIUS IN DISTINCTIONEM II. PARS I.** (= `d2-p1-divisio`, raw 4418).

**Apparatus — cross-chunk footer split with the ALREADY-COMMITTED `d1-p2-dubia` (handle carefully, do not corrupt the committed neighbor):**
- **p.52 left-col footer notes:** `1` *In hac responsione continetur summa Boethiani opusculi…* → **d1-p2-dubia** (its [^8], DUB II Boethius — already in the committed chunk, session-12 ledger). `2` *Cfr. de hoc I. Sent. d. 28. dub. 1; Alex. Hal., S. p. I. q. 17. m. 4; B. Albert., S. p. I. tract. 6. q. 26. m. 1. a. partic. 1; Aegid. R., hic circa lit. dub. 7.* → **d2-littera "auctoritates²"**. `3` *Alluditur ad verba Magistri, hic c. 6: Pro exemplo ergo futurae societatis…* → d1-p2-dubia DUB III. `4` *Plures codd. ut H K P Q cc et ed. 1 in omni fideli… respondetur pro redditur… responderi pro reddi.* → d1-p2-dubia DUB III. **So only note 2 anchors d2-littera on p.52.** The littera's own first marker *"aliqua dicenda sunt¹"* has no p.52 footer entry visible — its apparatus likely continues on p.53; verify p.53 footer head, flag `[?]` if unresolved and park for d.10.
- **p.53 left-col footer notes 1–7 (all anchor d2-littera body):** `1` Eccli. 18, 1 → *Salomonis¹* (Qui vivit in aeternum creavit omnia simul). `2` *Nempe Gen. ad lit. l. c. 1. n. 2. 3, c. 3. n. 7. 8, c. 4. n. 9; et XI. de Civ. Dei, c. 33. in fine.* → *Augustinus super Genesim²*. `3` *Cfr. I. Sent. d. XXX. c. 1, et ibid. Comment. S. Bonav. dub. 2. — Subinde pro antequam codd. priusquam.* → *non fuit tempus³*. `4` *Libr. V. c. 16. n. 17.* → *libro de Trinitate⁴*. `5` *De Gen. ad lit. V. c. 19. n. 38. — Codd., excepto D, et edd., exc. 1, 8, post creatura addunt creata. — Sequens locus Hieronymi est in eius Comment. ad c. 1. v. 3.* → *Augustinus⁵* ("nulla creatura…") + the Hieronymus-Titus quote. `6` *Cfr. August., XI. de Civ. Dei, c. 6.* → *dixerunt⁶*. `7` *Cod. A hic interserit Hugo, et revera Magister haec et…* → (anchor TBD on p.53 read; likely the Hugo/Magister textual note near Cap IV).
- **p.54 footer: NOT yet read** — read p.54 L-2 and R-2 footer bands first thing session 14 (the `NOTAE AD LIBR. SENTENTIARUM` editorial block lives here per the session-12 recon: *Praecedentia codd. nostri non numerant tanquam capitulum…*; *Isidorus, I. Sentent. (sive de Summo Bono) c. 10. n. 4…*; *Gen. 1, 1…*). These anchor the littera (Cap V/VI) — NOT d1-p2-dubia.
- Footnote numbering **restarts per printed page**; renumber the chunk 1–N continuously and document the p.52→p.53→p.54 crosswalk in `## Notes`. Per CLAUDE.md "Before promoting any chunk, verify the prior chunk's last printed page footer was fully captured" — `d1-p2-dubia` already has its p.52 share (session 12). No backfill of the committed chunk expected, but confirm note 1/3/4 are present there before finalizing.

- **Discipline carries forward unchanged:** full 450 dpi PDF re-set (`tools/extract-pages.py` + `tools/colcrop.py`), Latin verbatim from IA djvu OCR base + PDF-authoritative for shattered regions/footers (Vol II override), literal English, page-by-page apparatus crosswalk with documented cross-chunk footer splits, `[?]` flags parked for the d.10 polish-blocker, two-commit-per-session cadence (chunk + resume). Vol II offset: **PDF = printed + 22** (but `extract-pages`/`colcrop` take the **printed** number directly). **Pre-commit:** `node site/scripts/build-content.mjs` + `python3.11 tools/audit-{paraphrase,headers,apparatus-count}.py --volume 2 --min-d 2 --max-d 2` + marker-pairing one-liner.

`tools/colcrop.py` (committed session 8) is the PIL column-band cropper: `python3.11 tools/colcrop.py vol2 <printed-page> [split_x=1660] [n_bands=3] [scale=1.8]` → `/tmp/colcrop/vol2-pNNN-{L,R}-{0..n}.png`. Read L column top→bottom then R column; footer bands are the bottom band of each column.

### Apparatus / PDF discipline (carry forward — proven sessions 6–7)

Session 7 (q2, ~2160 words, pp. 41–43) confirmed: for any large quaestio the IA OCR cascade-fragments the Respondeo and *all* page-footers. The reliable workflow: `python3.11 tools/extract-pages.py --volume vol2 --pages <printed> --dpi 450`, then a PIL helper that crops each page into left/right column bands (top+bottom) plus footer bands, `resize` ~1.7–2.2×, and Read each crop. Reflow column-by-column (whole left column of a page, then whole right). Footnote numbering **restarts every printed page** — keep a per-page→chunk crosswalk and document it in `## Notes`. Page-footer split convention (notes follow body anchors, not the chunk that physically holds the footer text) still applies — always check the last page's footer vs. the next chunk.

### Workflow per CLAUDE.md (locked-in)

> ⚠ For Vol II this list is **modified by the CLAUDE.md "VOL II OVERRIDE"** (top of the Tier-2 verification workflow section). Specifically step 2: the OCR is the base only for clean prose + footnote-marker spacing; the 450 dpi column-band PDF read is authoritative for the (near-universal) cascade-shattered Respondeo/Solutio/footers. Read the override before starting d.2.

1. Find OCR line range; verify boundaries against raw.
2. Latin verbatim from raw OCR, NOT from PDF — *Vol II: except cascade-damaged regions, where the PDF is authoritative (see override above).*
3. `[^N]` anchors at OCR positions, not end-of-clause.
4. English literal, paragraph-for-paragraph.
5. Apparatus walked page-by-page from raw OCR footers.
6. Log `[?]` flags inline; resolve at decade polish-blocker (d.10).
7. Pre-commit: `node site/scripts/build-content.mjs` + the 3 audits `--volume 2` + marker-pairing one-liner.

### Lessons confirmed by sessions 2–4 (carry forward)

- **Trim marginal glosses aggressively** (`Ad oppositum`, `Fundamenta`, `Conclusio`, `Solutio`, `Distinctio`, `Notandum`, `Triplex productio`, `Determinatio trium productionum`, `Epilogus`, `Dupliciter relatio`, `Aliter`, `Eliditur error 1/2/3`, etc.). Don't render them as headings or text.
- **Apparatus marker renumbering is fine** — chunk-internal sequence 1–N is more readable than Quaracchi's per-page restart. Document the page-by-page crosswalk in `## Notes`.
- **Page-break markers** go in the chunk at the printed-page running-head or page-number boundary; if OCR ate a running head, mark `<!-- page N -->` position as `[?]` rather than guessing.
- **Don't try to resolve subtle OCR ambiguities eyes-on-OCR alone** — the d.10 polish pass + 600dpi PDF clears them in seconds.
- **Watch for column-linearization page-spillover** — session 4 caught a "missing" page-30 footer at the top of the next chunk's OCR window. Always glance at the next chunk's first ~20 lines if a footer reference seems short.
- **Cross-chunk footer split is now a confirmed recurring pattern (session 5, page 38).** When a printed page's footer block sits at a chunk boundary, its notes split by *body anchor*, not by which chunk physically contains the footer text. Session 5: page-38 footer notes 1–6 anchored in `d1-p1-dubia`'s page-38 body (DUB III tail/IV/V) but that chunk had only captured pp. 36–37 footer; notes 7–8 anchored in `d1-p2-divisio`. **Before promoting any chunk, verify the prior chunk's last printed page footer was fully captured for the body it holds on that page.** Same convention as `d1-p1-divisio` (notes 1–4 in next chunk's footer). Backfilling a committed Tier-2 chunk is acceptable and expected when this is found — renumber its sequence continuously and document in its Notes + `transcription_status`.
- **Vol II rechunk = `split("\n")`, never `splitlines()` (session 13).** 1056 form feeds in the Vol II raw shift `splitlines()` indices ~1055 off from grep/awk. Symptom: chunks start mid-previous-distinction. Always eyes-on PDF-verify the first chunk's opening line against its intended semantic header after any rechunk.
- **`extract-pages.py --pages` / `colcrop.py` take the PRINTED page number** (the +22 offset is applied internally; output is `p-{printed}.png` / `vol2-p{printed}-…`). Don't pre-convert to PDF page — session 13 wasted an extract doing that.
- **Vol II audit scripts DONE (2026-05-15, commit `76da3e7`)**: all three accept `--volume 2`. Run before each commit alongside the smoke build: `python3.11 tools/audit-{paraphrase,headers,apparatus-count}.py --volume 2 --min-d N --max-d N`. Calibration (verified on d.1's 17 Tier-2 chunks): paraphrase cleanly separates done (→OK) from skeleton (→HIGH/CRITICAL); apparatus-count flag logic intact (0 false flags on real chunks; diff column noisy ±10–18 — triage only); header audit is **coarse for Vol II** (positive diffs, catches only gross whole-chunk dropouts — fine-grained dropout detection still rests on the per-session column-band PDF pass). See CLAUDE.md "Required guard-rail audits" → Vol II calibration block. (`build-content.mjs` is still the parse/marker-pairing check.)

### Pace

- Session 4: 5 short-to-medium chunks in one extended session when apparatus is OCR-clean.
- Session 5: 1 divisio chunk + a cross-chunk apparatus backfill (page-38 footer found mis-split). Cross-chunk corrections cost ~1 chunk-equivalent of effort — budget for them when a chunk boundary falls inside a printed page.
- Session 6: `d1-p2-a1-q1` solo focused session — dense ~1190-word quaestio (pp. 39–40), full 450 dpi PDF pass.
- Session 7: `d1-p2-a1-q2` solo focused session — **largest chunk in d.1** (~2160 words, pp. 41–43, 23 apparatus entries), entire chunk re-set against PDF. A ~2000-word quaestio with heavy cascade damage is a full session on its own; do not bundle.
- Session 8: `d1-p2-a2-q1` solo focused session — ~1300-word quaestio (pp. 43–45, 13 apparatus entries) + re-chunk decision (absorb ART. II opener) + two cross-chunk footer splits (pp. 43, 45) verified against a1-q2's committed crosswalk. Re-chunk + dual cross-chunk split adds ~½ chunk-equivalent over a clean mid-size quaestio. Added `tools/colcrop.py`.
- Session 9: `d1-p2-a2-q2` solo focused session — ~870-word quaestio (pp. 45–47, 13 apparatus entries), full PDF re-set, two cross-chunk footer splits (p.45 note 1 → a2-q1; p.47 notes 3–7 → a3-q1) + a page-45→46 footnote runover folded into [^4]. Mid-size quaestio with two clean cross-chunk splits ≈ one focused session. Two q2-style chunks (a2-q1 + a2-q2) fit in a single working stretch when each is ~900–1300 words and cascade damage is footer-localized — but the dual cross-chunk bookkeeping is the real cost, not word count.
- Session 10: `d1-p2-a3-q1` solo focused session — ~1060-word quaestio (pp. 47–49, 12 apparatus entries) with a *triplex-opinio* Respondeo + three-part scholion, fully two-column-shattered; full 450 dpi PDF re-set. The p.47 cross-chunk footer split (notes 1–2 → a2-q2, 3–7 → a3-q1) was the prior session's open [?] — reading the footer in source order both populated a3-q1 and **retired a2-q2's [^12] flag** in the same pass. Resolving a downstream chunk's flag while building the next chunk is efficient — read shared footers in printed order once and assign both directions.
- Session 11: `d1-p2-a3-q2` solo focused session — ~1330-word quaestio (pp. 49–51, **20 apparatus entries** — the largest apparatus count in d.1 pars 2) with a *triplex-modus* Respondeo, fully two-column-shattered; full 450 dpi PDF re-set. No scholion (a3-q1's covers it — saved a translation pass; always check the prior chunk's scholion for *«pro quaest. seq.»* before assuming a missing scholion is an error). Three sequential cascade sessions (a2-q1→a2-q2→a3-q1→a3-q2) confirm the steady-state cadence: one heavily-damaged ~1000–1300-word quaestio per focused session, ~12–20 apparatus entries, the cross-chunk footer bookkeeping (not word count) being the dominant cost.
- Session 12: `d1-p2-dubia` (DUB I–III, ~750 words, pp. 51–52, 12 apparatus entries) — **closed distinction 1**. A 3-doubt dubia block ≈ a mid quaestio in effort (less videtur/contra scaffolding, but the same cross-chunk footer bookkeeping: p.51 notes 1–4 → prior a3-q2, p.52 NOTAE block → next d.2). Sessions 8–12 cleared all of d.1 pars 2 (8 chunks) at a steady ~1 chunk/session; expect the same for d.2's quaestiones once its re-chunk pass is done. **Realistic d.2 estimate:** the re-chunk + littera + divisio is ≥1 session before the first quaestio, then ~1 quaestio/session.
- Session 13: **d.2 re-chunk pass** — full structure mapping (17 chunks, both pars, OCR-garbled headers resolved) + caught/fixed the `splitlines()` form-feed bug + regenerated 17 correct skeletons + read all littera source pages (pp.52–54 PDF column bands, structure + cross-chunk footer split with committed `d1-p2-dubia` fully documented above). Stopped at the clean re-chunk boundary rather than half-build the littera (CLAUDE.md "complete to Tier-2 or leave skeleton"). Confirms the resume estimate: the re-chunk discovery alone (with a tooling-bug fix + a 3-page cross-chunk apparatus analysis) is a legitimate full session. Session 14 starts the littera Tier-2 with zero discovery left — just read p.54 footer, then transcribe/translate/apparatus/commit.

### Distinction 1 — COMPLETE (sessions 1–12, all 17 chunks Tier-2)

| Chunk | Raw lines | Session |
|---|---|---|
| d1-littera | (pars 1) | 1 |
| d1-p1-divisio | | 1 |
| d1-p1-a1-q1 … a3-q2 (6 q) | | 2–4 |
| d1-p1-dubia (DUB I–V) | | 4 (p.38 backfill 5) |
| d1-p2-divisio | 3321–3378 | 5 |
| d1-p2-a1-q1 | 3382–3502 | 6 |
| d1-p2-a1-q2 | 3503–3670 | 7 |
| d1-p2-a2-q1 | 3672–3817 | 8 |
| d1-p2-a2-q2 | 3818–3924 | 9 |
| d1-p2-a3-q1 | 3925–4048 | 10 |
| d1-p2-a3-q2 | 4049–4186 | 11 |
| d1-p2-dubia | 4187–4263 | 12 |

**Distinction 1 is closed.** All 17 chunks Tier-2; site build 428 translated. The d.1 `[?]` flags above remain parked for the **d.10 polish-blocker** (resolve d.1–d.10 in one 600 dpi pass once d.10 ships; see CLAUDE.md "Polish-blocker cadence"). Next work = **distinction 2** (see "Next" section above): fresh re-chunk pass, then littera + divisio, then quaestiones at ~1/session.

## Polish-blocker (after d.10 ships)

1. `[?]` flag resolution — Vol II d.1–d.10 only.
2. Style/formatting audit — full corpus (Vol I + Vol II).
3. Resolution log at `manual-review/II-d1-d10-polish-resolution-log.md`.

## Tools cheat sheet

```bash
# Inspect raw chunk range
awk 'NR>={start} && NR<={end}' raw/bonaventure_vol2_raw.txt

# Vol II offset: pdf_page = printed + 22
python3.11 tools/extract-pages.py --volume vol2 --pages {printed_pages}

# Chunker warnings
python3.11 tools/auto-chunk-volume.py 2 --dry-run 2>&1 | awk '/WARNINGS/,/Chunk list/'

# Smoke build
cd site && node scripts/build-content.mjs
```

Vol II offsets: see CLAUDE.md table (`pdf = printed + 22`). No deploy until meaningful Vol II Tier-2 work to show.
