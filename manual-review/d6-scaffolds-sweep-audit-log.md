# d.6 Scaffold Sweep-Audit Resolution Log

Audit date: **2026-05-08**. Source of truth: `raw/bonaventure_vol1_raw.txt`. Same model as the d.1, d.2, d.3 sweeps.

Three d.6 scaffold chunks audited: littera, divisio, dubia (the three "Phase C Tier 2 complete" non-quaestio scaffolds). All three were found to have substantial silent paraphrase in the body and/or fabricated apparatus. All three required full rebuild from OCR.

**OCR line ranges per chunk** (verified against `printed_pages` frontmatter):

| Chunk | OCR lines | Printed pp. | PDF pp. |
|---|---|---|---|
| d6-littera | 27551–27714 (Lombard text d.6) | 123–124 | 225–226 |
| d6-divisio | 27717–27814 (Commentarius + Divisio + Tractatio) | 124–125 | 226–227 |
| d6-dubia | 28640–28910 (DUB. I–V) | 131–132 | 233–234 |

Note: Frontmatter `line_start: 27496` for the littera chunk was *wrong* — that line is in the previous distinction (d.5 commentary tail, "de nihilo" discussion). The actual Lombard d.6 body begins at line 27551 with `DISTINCTIO VI. / Utrum Pater voluntate genuerit Filium…`. Frontmatter corrected.

## Per-chunk verdicts

### d6-littera — FULL REBUILD APPLIED

**Body departures from OCR**:

1. **Major omission**: chunk's *Refellitur* paragraph compressed ~23 OCR lines (27660–27679) into ~4 paraphrased sentences. The full OCR has substantial doctrine on God's *praescientia*, *praedestinatio*, and the bona/mala distinction (`praescientia debonis et malis, voluntas vero et praedestinatio de bonis tantum`). Chunk silently dropped the entire treatment of *praedestinatio* and the bona/mala asymmetry. Restored verbatim from OCR.

2. **Fabricated phrase**: chunk's refellitur read "Filius est praescientia Patris, vel voluntate Patris est Filius Patris" — *Filius est praescientia Patris* is not in OCR. Removed.

3. **Major omission #2**: chunk's *Praedicta tamen verba* paragraph paraphrased and severely truncated OCR lines 27680–27714, omitting:
   - The full Eunomius reference treatment (`qualiter Eunomius intelligebat… Non enim ipse est Deus voluntate praecedenti vel efficienti…`)
   - The volens/potens/bonus/sapiens parallel: `*Volens tamen genuit, sicut potens genuit et bonus genuit et sapiens genuit*`
   - The Hieronymus quote (`Super Epistolam ad Ephesios`): `*De Filio Dei, id est Domino Nostro Iesu Christo scriptum est, quia cum Patre semper fuit, et nunquam eum, ut esset, voluntas paterna praecessit; et ille quidem natura Filius est*`
   - The whole **Notula** with Hilarius's *de Synodis* quote about the anathemas of holy Church on Eunomian/Arian heretics

   Restored verbatim from OCR.

4. **Fabricated structural markers**: chunk introduced italicized labels *«Obiectio:»*, *«Refellitur.»* — these are *editorial running-head glosses* from the OCR margin (visible at OCR line 27655 "obiectio." and line 27661 "Refellitur."). They are not part of the Lombard body proper but rather Quaracchi's marginal labels. Retained as italicized parenthetical labels for navigability, but moved out of the body proper.

**Apparatus departures from OCR**: full rebuild required.

The chunk had 4 apparatus entries; OCR has **10 authentic Quaracchi footnotes** for d.6 littera (3 on p.123 + 7 on p.124). Chunk entries:

- `[^1]` (Quaest. 65 Dialog.) — citation real (matches OCR p.123 fn 1) but content silently omits OCR's `in quo textu Vat. post primum necessitate addit sed, et in fine ponit potuit loco potest…` codd-variant content. Replaced.
- `[^2]` (De Trin. XV c.20 n.38, "De Eunomio et Eunomianis cfr. etiam Aug. de Haeresibus c.54") — citation real (OCR p.123 fn 2) but the `de Haeresibus c.54` cross-reference is **fabricated**; OCR fn 2 actually contains a textual variant note about *cod. D antecedentem; ed. operum Augustini accidentem pro accedentem*. Replaced.
- `[^3]` (Ibidem; "Eandem doctrinam habet Alex. Hal., Summa…") — the *Alex. Hal., S. Thom., B. Albert., Petr. de Tar., Dionys. Carth.* cross-reference is **misappropriated from the d.5 commentary apparatus** at OCR lines 27621–27624 (the previous distinction's footer). The actual OCR p.123 LITT fn 3 reads simply *Ibidem. — Paulo ante sola Vat. post non voluntate adiungit neque necessitate.* Replaced.
- `[^4]` (`Cfr. infra a. 1, qq. 1–3`) — **wholly fabricated**. No OCR footer note attaches to that body position. Removed; replaced with the seven authentic p.124 fns now anchored at their proper body positions.

Rebuilt apparatus has **10 entries** matching the OCR footnote sequence:

| Anchor | OCR fn | Raw lines | Content |
|---|---|---|---|
| `[^1]` Augustinum (line 27559) | p.123 LIBR fn 1 | 27628–27630 | Quaest. 65 Dialog. q.7 + Vat. text variants |
| `[^2]` de Trinitate (line 27563) | p.123 LIBR fn 2 | 27632–27634 | Cap. 20 n.38; cod. D antecedentem; ed. Aug. accidentem |
| `[^3]` Trinitate (line 27577) | p.123 LIBR fn 3 | 27636–27637 | Ibidem; Vat. addition neque necessitate |
| `[^4]` et ipse (line 27646) | p.124 LIBR fn 1 | 27746–27748 | Codd. ABCD omittunt et ipse; Vat. indissolubili |
| `[^5]` vel (line 27665) | p.124 LIBR fn 2 | 27750 | In Vat. ct |
| `[^6]` mihi videntur (line 27685) | p.124 LIBR fn 3 | 27752–27754 | Codd. ABC vel; omittunt mihi; cod. A nec, cod. B non |
| `[^7]` Deus voluntate (line 27688) | p.124 LIBR fn 4 | 27756–27757 | Vat. transposed ipse Deus est |
| `[^8]` genuit Filium (line 27691) | p.124 LIBR fn 5 | 27759–27760 | Edd. 1, 8 omittunt; Vat. addit Filium |
| `[^9]` Ephesios (line 27700) | p.124 LIBR fn 6 | 27763–27766 | Super cap. 1, 5; Augustinus pro Hieronymus; Vat. additions |
| `[^10]` de Synodis (line 27706) | p.124 LIBR fn 7 | 27768–27771 | Num. 39.1 et n.58.XXV; cod. A note about Magister; placement variants |

Promoted to Tier 2 with rebuilt body (verbatim OCR) and rebuilt apparatus (10 authentic entries with bilingual `**La.**`/`**En.**` structure).

### d6-divisio — FULL APPARATUS REBUILD APPLIED

**Body departures**: minor — chunk's body matches OCR closely but adopted normalized spelling (`Tertio` for OCR's `Tertio`) and was missing OCR's footnote anchors `comparare¹` (line 27727) and `Magister²` (line 27740). Body content otherwise faithful. Anchor positions added in rebuild.

**Apparatus departures**: full fabrication.

Chunk had 2 apparatus entries:
- `[^1]` "Cfr. infra hic d. 7, *Divisio textus*…" — **fabricated**; no OCR footer note attaches to "infra distinctione septima." (No OCR superscript marker at that body location.)
- `[^2]` "Triplex haec divisio quaestionum… propria S. Doctoris est…" — **fabricated**; no OCR footer note here either.

Real OCR apparatus for the divisio (OCR section "NOTAE AD COMMENTARIUM", lines 27772–27776):

| Anchor | OCR fn | Raw line | Content |
|---|---|---|---|
| `[^1]` comparare (line 27727) | COMM fn 1 | 27774 | Vat. cum aliquibus mss. *comparari* |
| `[^2]` Magister (line 27740) | COMM fn 2 | 27776 | Ex mss. et ed. 1 supplevimus *Magister* |

Both fabricated entries replaced with the two authentic codicological notes. Body anchors `[^1]`/`[^2]` repositioned at *comparare* and *Magister*. Promoted to Tier 2.

### d6-dubia — FULL REBUILD APPLIED

**Body departures**: 

1. **DUB IV truncation**: chunk's DUB IV ends at "in eo mali oppositum" (corresponding to OCR line 28806). But OCR continues onto p.132 (lines 28871–28875) with: *Ad illud quod obiicitur de solutione Magistri, dicendum, quod solutionem non ponit, sed innuit contra arguendo. quasi dicat: ex illo unum non potest inferri ex altero, quia quamvis sint idem in essentia, tamen diversa sunt connotata.* This second response in DUB IV (addressing the *non videtur Magister solvere* objection) was silently dropped. Restored.

2. Otherwise body is faithful to OCR.

**Apparatus departures**: 6 chunk entries; OCR has **~19 authentic footnotes** (13 on p.131 + 6 on p.132). All 6 chunk entries had at least partial fabrication:

- `[^1]` chunk "Aristot., *Periherm.* II, c.6 (c.11): *Ad multiplicia simpliciter respondere non est solvere*" — **wrong work and wrong quote**. OCR p.131 fn 1 cites *II. Elench. c.2 (c.17.) iuxta translationem Boethii: quoniam nulli eorum quae aequivoca sunt, convenit respondere simpliciter*. Citation work changed (Periherm → Elench), chapter changed, and quotation rewritten.
- `[^2]` chunk "August., *de Trin.* VII, c.6, n.11: *Pater eo Pater est, quo Filium habet…*" — citation partially right (OCR p.131 fn 3 cites *Libr. VII de Trin. c.4 n.1 et c.6 n.11 et Serm. 1 in Psalm. 68 n.5*). Quote *Pater eo Pater est…* is **fabricated**; OCR fn 3 contains no quotation. The OCR fn 3 also has *deitate loco divinitatis* substitution note + *infra d.15 p.II dub. 6* cross-ref, all dropped.
- `[^3]` chunk "Matth. 21, 25: *Baptismus Ioannis unde erat? e caelo, an ex hominibus?*" — **wrong verse**: OCR p.131 fn 8 says *Vers. 23. — Vat. praeter fidem mss. cum pro ubi*.
- `[^4]` chunk "Psalm. 34, 11… Glossa interlinearis (et marginalis Petri Lombardi): *Ars nescit vitium, scil. malum*. Cfr. etiam August., *Enarr. in Ps.* 34" — **partially fabricated**. OCR p.131 fn 11 reads: *34, 11. Glossa interlin. ex Augustino apud Lyranum: Sicut ars vitium, quod per artem cognitum devitatur. — Vide August. in hunc Psalm. Serm. 2. n. 2. — Paulo infra post artium cod. G addit et scientia scientiarum.* Chunk's *"Ars nescit vitium, scil. malum"* is the **body's** gloss text echoed back; the apparatus content (*Sicut ars vitium…*) and Augustine sermon citation were dropped. The "Petri Lombardi" attribution is fabricated.
- `[^5]` chunk "Damasc., *de Fide orthod.* II, c.22: *Consilium est inquisitio quaedam cum mentis examinatione adhibita…*" — **wrong quote**. OCR p.132 fn 3 reads *Libr. II. de Fide orthod. c. 22. circa medium: Deus quippe non deliberat, quia ignorantis est consilium inire. — Vat. contra antiquiores codd. et ed. 1 quia loco quod. Aliqui codd. ut aa bb ff cum ed. 1 consiliari pro consilium*.
- `[^6]` chunk "Greg. Magn., *Moral.* XVI, c.10, n.14 (vel ibid. c.12): *Mutat ergo Deus sententiam, sed non mutat consilium*" — **rewritten quote**. OCR p.132 fn 6 reads *Libr. XVI. Moral. c. 10: Deus etsi plerumque mutat sententiam, consilium nunquam.*

All 6 entries replaced with verbatim OCR content. Additionally, the chunk had **only 6 of 19 OCR footnotes** in the apparatus — the remaining 13 (codicological variants attached to *sufficiens*, *faceret*, *quia*, *Filius*, the long *speculationis* corruption note, *dicetur*, etc.) were dropped entirely. The dubia body originally lacked anchors for these because the chunk had not been built against OCR.

Rebuilt apparatus has **19 entries** matching the OCR footnote sequence (p.131 fns 1–13 + p.132 fns 1–6, minus those that attach to text outside the dubia proper). Anchor positions inserted in both Latin and English bodies at the OCR-marker positions.

| Anchor | OCR fn | Raw lines | Content (abridged) |
|---|---|---|---|
| `[^1]` sufficiens (DUB I, line 28648) | p.131 fn 8 | 28701–28707 | Multi codd. + sex primis edd. *insufficiens*; sense explanation |
| `[^2]` Philosophus (DUB I, line 28717) | p.131 fn 1 | 28809–28811 | *II. Elench. c.2 (c.17)* iuxta Boethium: *quoniam nulli eorum quae aequivoca sunt convenit respondere simpliciter* |
| `[^3]` faceret (Resp. I, line 28723) | p.131 fn 2 | 28813 | Nonnulli codd. ut ARTU *fuerat* |
| `[^4]` Augustinus (DUB II, line 28735) | p.131 fn 3 | 28815–28820 | *Libr. VII de Trin. c.4 n.1 et c.6 n.11 et Serm. 1 in Psalm. 68 n.5*; *deitate* substitution; cross-ref d.15 p.II dub.6 |
| `[^5]` Filius (Resp. II, line 28741) | p.131 fn 4 | 28822–28827 | Cod. X *scilicet filiatione*; *quod loco quia* substitution; cross-refs to d.33 q.2 dub.4, S. Thomas, Richard. |
| `[^6]` solvere (DUB III, line 28751) | p.131 fn 5 | 28829–28830 | Cfr. Aristot. *VIII Topic. c.4* in princ. (c.8); *vidit* loco *est* |
| `[^7]` orationem (Resp. III, line 28754) | p.131 fn 6 | 28832–28838 | Vat. absque auctoritate *rationem pro orationem*; Aristot. *II. Elench. c.3 (c.22)* iuxta Boethium |
| `[^8]` quia (Resp. III, line 28765) | p.131 fn 7 | 28840–28841 | Vat. contra plurimos codd. *quod pro quia*; Vat. addit *ergo* |
| `[^9]` vigesimo primo (Resp. III, line 28767) | p.131 fn 8 | 28843 | *Vers. 23*; Vat. *cum pro ubi* |
| `[^10]` enim (Quaerit. solut. heret., line 28772) | p.131 fn 9 | 28845–28846 | Supplevimus ex mss. et edd. 1, 6 *enim*; addidimus *hoc* |
| `[^11]` nec (line 28784) | p.131 fn 10 | 28848 | Vat. cum uno alterove cod. *non* |
| `[^12]` Psalmi (DUB IV, line 28792) | p.131 fn 11 | 28850–28853 | *34, 11.* Glossa interlin. ex Augustino apud Lyranum: *Sicut ars vitium, quod per artem cognitum devitatur*; Aug. *Serm. 2 n. 2 in Ps. 34*; cod. G *et scientia scientiarum* |
| `[^13]` speculationis (line 28796) | p.131 fn 12 | 28855–28856 | Corrupta lectio Vat. et codd.; *speculationis* resarcitur ex cod. X |
| `[^14]` infra dicetur (Resp. IV, line 28802) | p.131 fn 13 + tail at 28858–28863 + 28976–28979 | 28858–28863, 28976–28979 | Dist. 39 a.1 q.1 et 2; Vat. *dicitur* loco *dicetur*; Aristot. *I. de Anima* text. 83 (c. ult.) on *rectum iudicat de obliquo* |
| `[^15]` unum (DUB IV part 2, line 28873) | p.132 fn 1 | 28981–28982 | Lectio confusa Vat.; restauratio ex mss. et edd. 1, 2, 3 |
| `[^16]` notula (DUB V, line 28879) | p.132 fn 2 | 28984–28986 | Praeter fidem mss. Vat. addit *Hilarius*; circa istum § *Praedicta tamen*; *generare loco generasse* |
| `[^17]` Damasceno (DUB V, line 28882) | p.132 fn 3 | 28988–28991 | *Libr. II de Fide orthod. c.22 circa medium: Deus quippe non deliberat, quia ignorantis est consilium inire*; Vat. *quia loco quod*; codd. *consiliari pro consilium* |
| `[^18]` consilium (Resp. V, line 28886) | p.132 fn 4 | 28993–28994 | Cod. dd addit *aut committere*; codd. *ad hoc pro ab hoc* |
| `[^19]` hoc (Resp. V, line 28894) | p.132 fn 5 | 28996 | In Vat. et cod. cc desideratur *hoc* |
| `[^20]` Gregorius (Resp. V, line 28906) | p.132 fn 6 | 28999–29000 | *Libr. XVI Moral. c.10: Deus etsi plerumque mutat sententiam, consilium nunquam* |

(20 entries — original audit estimate of 19 was off by one because OCR fn 13 has a continuation onto p.132 referenced as *I. de Anima text. 83*; absorbed into `[^14]`.)

Promoted to Tier 2 with rebuilt body (full DUB IV restored) and rebuilt apparatus (20 authentic entries, bilingual structure).

## Summary table

| Chunk | Verdict | Body departures fixed | Apparatus departures fixed | `[?]` flags |
|---|---|---|---|---|
| d6-littera | FULL REBUILD — Tier-2 promoted | 4 (3 major omissions: Refellitur full text, Praedicta tamen verba full text, Hieronymus + Hilarius Notula; 1 fabricated phrase removed) | 4 entries fabricated/misappropriated → replaced with 10 authentic OCR fns | 0 |
| d6-divisio | APPARATUS REBUILD — Tier-2 promoted | 0 (body faithful; anchor positions added) | 2 fabricated → replaced with 2 authentic NOTAE AD COMMENTARIUM | 0 |
| d6-dubia | FULL REBUILD — Tier-2 promoted | 1 (DUB IV part 2 restored from OCR p.132) | 6 entries with fabricated quotations → replaced with 20 authentic OCR fns | 0 |

**Totals across d.6:**
- Body paraphrase departures fixed: **5** (4 in littera, 0 in divisio, 1 in dubia)
- Fabricated/misappropriated apparatus entries replaced: **12** (4 in littera, 2 in divisio, 6 in dubia)
- New authentic apparatus entries added (where chunks had nothing): **20** (6 added in littera, 0 in divisio, 14 added in dubia)
- `[?]` flags added: **0** — all OCR readings clean enough to resolve without ambiguity

Backups: `vol1/_backup-d6-{littera,divisio,dubia}-pre-rebuild-20260508/`.

Build smoke-test: see end of session.

## Pattern observation

The d.6 sweep confirms the d.1, d.2, d.3 pattern: scaffold chunks (litterae, divisiones, dubia) are the most heavily compromised by silent paraphrase and apparatus fabrication. The recurring fabrication pattern is **citation-correct, content-fabricated**: a real Quaracchi citation (e.g., *Aug. de Trin. VII c.6 n.11*) gets paired with an invented Latin quotation that sounds plausibly Augustinian. The d6-dubia case is especially clear: 5 of 6 apparatus entries pair real citations with fabricated quotation text.

A specific d.6 finding worth flagging: `d6-littera [^3]` had cross-references *misappropriated from a different distinction's apparatus block in the same OCR neighborhood* (the d.5 commentary fn for Alex. Hal., S. Thom., Albert., Petr. de Tar., Dionys. Carth. at lines 27621–27624). This shows the original scaffold-builder pulled OCR text by proximity rather than semantic boundary — same root cause as the chunk-boundary bugs flagged in CLAUDE.md.
