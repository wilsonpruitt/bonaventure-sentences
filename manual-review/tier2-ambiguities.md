# Tier-2 Ambiguities Log

Running log of spots where the Tier-2 verification pass could not produce a fully confident reading. Each entry: chunk id, line/section, the question, current best guess, what would resolve it.

**Workflow note (locked 2026-05-01):** the IA djvu.txt (= `raw/bonaventure_vol1_raw.txt`) is the **canonical Latin source of truth** for this project. It's ABBYY-quality OCR and is much more reliable than eyes-on-PDF reads of the small-set scholarly text. The PDF is consulted only for:
1. Verifying OCR garbles flagged by `?` glyphs or impossible Latin
2. Confirming footnote-anchor positions (the OCR strips footnote superscripts)
3. Resolving ambiguities listed below

---

## d.1, a.1, q.1 (pp. 30–32)

- **Scholion opening word**: OCR garbles as `niiliiiui` (raw line 13653). Likely candidates: *Plurimi* / *Plures* / *Multi*. Currently rendered `Plurimi[?]`. → Resolve with PDF p. 32 inspection.
- **Scholion: Henr. Gand. *Summa* article number**: OCR truncates as `S. a. ` (raw line 13665). The `a.` number is missing. Likely article ~8 (since old chunk had `S. a. 8, q. 1`). Currently `S. a. [?]`. → Resolve with PDF p. 32.
- **Scholion: Scotus reference**: OCR garble `'l !i. in tiiic.` (raw line 13654) likely = `L. n. in fine` (lectio/lectura n. [last]). Currently `[a. unic., q. unic., in fine]` placeholder. → Resolve with PDF p. 32.

---

## Open ambiguities (cumulative)

3 open: all in d.1, a.1, q.1 scholion (above).

### d.10, a.1, q.2 (2026-05-02)

**d10-a1-q2, apparatus [^4]**: OCR reads "Vers. 3." for the Romans citation, but the body quotes *Caritas Dei diffusa est in cordibus nostris* = Romans 5:5. Currently rendered "Vers. 5[?]". → Resolve by checking PDF p. 192 footnote 4; expected reading is "Vers. 5".

**d10-a1-q2, scholion II opening**: OCR reads "Quaeslio iii soiut. ad i. tacta" — almost certainly "Quaestio in solut. ad 4. tacta" (the irascibilis question is treated in *Ad 4* of the respondeo). Currently rendered "ad 4[?]". → Resolve by checking PDF p. 193 scholion II.

**d10-a1-q3, scholion I opening**: OCR reads "In solut. ad i. verba locum Richardi" — the quoted phrase that follows ("Non dicunt modum amandi circa amorem etc.") is verbatim from the body's *Ad 4* reply, so this is "ad 4". Currently rendered "ad 4[?]". → Resolve by checking PDF p. 194 scholion I.

---

## d.11 + d.12 (2026-05-02 — re-pass audit after batch Tier-2 promotion)

**Audit context:** d.11 (a1-q1, a1-q2, dubia) and d.12 (littera, divisio, a1-q1, a1-q2, a1-q3, a1-q4, dubia) were promoted to Tier 2 in a single session. Initial pass did not flag ambiguities inline. This re-pass logs the silent calls and OCR-gap reconstructions identified after the fact.

### High priority — fabricated apparatus

**d12-a1-q1, apparatus [^10]–[^13]**: The page-221 apparatus block is **missing from the IA djvu OCR** (after page-220 fn 9 "Cod. X immutabilitati" the OCR jumps straight to page-221 body, then to scholion, with no fn block in between). The chunk body has four footnote markers in this stretch (`alter accipit ab altero ' / intelligatur prius '' / Ad illud ergo '' / quod per ''`). On first pass I wrote plausible-looking apparatus entries for [^10]–[^13]; **none of these phrases ("altero accipiat" Vat variant, "HVW prius om", "autem loco ergo", "Cod. R quia per") appear anywhere in `raw/bonaventure_vol1_raw.txt`**. They are reconstructions, not transcriptions. → Resolve by checking PDF p. 221 footnotes; if the apparatus is genuinely missing in the printed edition (unlikely), revert to body-only anchors. Chunk now flagged inline with `[?]` markers on those four entries.

### Silent OCR corrections worth confirming

**d11-a1-q1, apparatus [^7]** (Damascene reference): OCR garble at chunk-file line 208 reads `Libr. I. de Fide orthod. c. f*.`. Currently rendered `c. 8`. The "f*" glyph is most likely `8` (font shape) but could be `2` (separately, raw line 252 has a Damascene-related fn reading `orthod. c. 2.`). Both 2 and 8 appear in standard Damascene chapter divisions for this passage. → Resolve by checking PDF p. 209 fn 7.

**d12-littera, apparatus [^14]**: OCR reads `loan. 13, 26` for the "De Patre procedit" citation, which is unambiguously **John 15:26** (verse content matches). Silently corrected to `Ioan. 15, 26` / `John 15:26`. → No PDF check needed (content-confirmed); flagged for transparency.

**d12-littera, apparatus [^15]**: OCR garble `Cap. 27. n. i8.` for Augustine *De Trin.* XV. Currently rendered `Cap. 27, n. 48`. The `i8` glyph is more likely `48` (the well-known section "Quapropter qui potest intelligere..." is XV.27.48), but `18` is grammatically possible. → Resolve by checking PDF p. 219 fn 9.

### Editorial clarifications (no ambiguity, but worth tracking)

**d11-a1-q1, apparatus [^50]**: Bracketed-in `[Lombard, Sent. I, dist. 11,]` before `cap. 2` to disambiguate which `cap. 2` the OCR-only "Cap. 2." refers to. Content-confirmed: Lombard's text is the only `cap. 2` in scope.

**d12-a1-q3, apparatus [^18]**: Aristotle *Physics* II.5 quote truncated with `...` after `sic et causam contingit esse` — the full quote continues several lines in OCR but is not central to the apparatus point.

**d12-a1-q2, scholion I**: Inserted `[scil. Spiritum sanctum]` after Quaracchi's `Pater principalius producat Filium` because the bare "Filium" in that sentence is a slip for "Spiritum sanctum" (verified by the immediate context discussing the Spirit's procession, not the Son's generation).

**d11-dubia, dub IV apparatus**: The OCR places dub-IV's 5 footnotes ~60 lines below the body (lines 41923–41932), separated from the body by an unrelated d.12 page-running header. The 5 anchors in the body were matched to the 5 footnotes by content (variant readings about *aliquem/illum*, *tunc*, *et loqui*, *Ioan. 16:13*, *vel/sive*). Match is high-confidence but should be verified against PDF p. 218 fn 1–5 if any spot-check is done.

---

## Open ambiguities (cumulative — updated 2026-05-02)

7 open: 3 in d.1 a1-q1 scholion + 3 in d.10 a1-q2/q3 + 1 cluster of 4 in d.12 a1-q1 fabricated apparatus (highest priority).

### d.13 a1-q1 (2026-05-02)
**bon-sent-I-d13-a1-q1, pro-argument 2 closing word**: OCR breaks at column/page transition (raw line ~43898, between "ergo a primo³ in divinis vere et proprie est" and "3. Item, amor noster…"). Closing predicate noun lost. Currently rendered: *"…vere et proprie est [processio] in divinis"* with editorial brackets. → Confirm against PDF p. 231 column-2 to bracket-resolution.

### d.13 a1-q2 (2026-05-02)

**d13-a1-q2, apparatus [^1] ("ita")**: OCR garble at end of Aug. *De Trin.* citation reads "*posuimus ita h*" with trailing word obscured. Tentatively rendered *ita*; Quaracchi probably gives the precise reading the editors adopted (e.g. *ita habet* or a quoted phrase). → Resolve by checking PDF p. 232 fn 5.

**d13-a1-q2, apparatus [^8] (combined Damascene + "addunt sc.")**: Raw OCR fn 2 on p. 232 ("Aliqui codd. ut B T Y cum ed. 1 addunt *sc.*") gives no clear body anchor. Combined with the Damascene citation footnote here. → Resolve by checking PDF p. 232 to see where *sc.* is actually inserted.

**d13-a1-q2, apparatus fn 3 from p. 232 ("Restituimus ex mss. et ed. 1 *de*")**: Tiny variant, no clear body anchor; OMITTED from chunk apparatus to avoid fabricating a position. → Resolve by checking PDF p. 232 fn 3 for the body location of restored *de*.

**d13-a1-q2, apparatus [^20] (Petr. Hisp. cite)**: OCR reads "*tract. de Praedicab. de Proprio oil*" — trailing "oil" is unintelligible OCR for a section/chapter reference. Rendered "[?]". → Resolve by checking PDF p. 233 fn 12.

**d13-a1-q2, apparatus [^28] (cod. X addition)**: OCR ends mid-phrase at "*grammaticus est*" — chunk's raw line range cuts the example off. Likely the standard Aristotelian "*grammaticus est musicus*" *per accidens* predication parallel for "generans est spirans". → Resolve by checking PDF p. 234 last footnote for the full example.

**d13-a1-q2, apparatus [^11] body-anchor placement**: The "Tres modi" footnote (Vat. corruption of the threefold distinction) — placed at end of the *similem per modum naturae* clause, which is the natural completion of the corrupted member-list. Confirm anchor sits where Quaracchi's superscript number sits on PDF p. 233.

### d.13 a1-q3 (2026-05-02)

**d13-a1-q3, apparatus [^18] anchor (cod. bb adds *scilicet*)**: Anchor placed at *vim spirativam et generativam* (rejected first opinion); could equally belong at *Filius procedit per modum esse, Spiritus per modum bene esse*. → Resolve by checking PDF p. 236 fn 8.

**d13-a1-q3, apparatus [^19] join across page**: The OCR splits this *imperfectum*/*imperfectionem* + *non* note — variant block on p. 236 fn 9, editor's exegesis ("subiectum huius propositionis non sunt termini, sed emanationes…") on p. 237. Reassembled by content. High confidence, but spot-check the join vs PDF p. 236–237.

### d.14 p1-a1-q1 (2026-05-02)

**d14-p1-a1-q1, apparatus [^4] anchor ("ita" / *et* added)**: OCR shows a marker near *ita Filius* in contra-2; apparatus 4 is "In nonnullis mss. ut R bb ff et ed. 1 adiungitur *et*" — placed [^4] at *ita* (so the variant adds "et" after). Plausible but not airtight; the variant could attach to one of several *et* positions in the chunk. → Resolve by checking PDF p. 245 fn 4 superscript position.

**d14-p1-a1-q1, apparatus [^11] anchor ("in processione aeterna")**: ed.1 adds *aeterna emanatione* by way of explanation, then "paulo infra" gives *recipiatur*/*producatur* variants for the Greeks-clause. Anchor [^11] placed at *in processione aeterna* in the respondeo. Spot-check that Quaracchi's superscript actually sits here (not earlier at *primus quidem modus*).

**d14-p1-a1-q1, apparatus [^7] anchor ("aut" before *gratiae*)**: Cod. M repeats *ratione* — anchor placed at *aut* in contra-5 ("ratione Spiritus sancti aut[^7] gratiae") on the assumption the repetition was "aut ratione gratiae". OCR doesn't clearly mark the position.

**d14-p1-a1-q1, Ad-5 alternative reading**: After the threefold distinction of *temporale*, the chunk shows "Potest tamen dici, quod gratia habet esse temporale ratione eius in quo est, scilicet liberi arbitrii…" rendered as a continuation. This is the *Alia solutio* (alternative solution) — Quaracchi typesets it as a marginal label. Rendered as a paragraph break only; no separate heading.

### d.14 p1-a1-q2 (2026-05-02)

**d14-p1-a1-q2, apparatus [^5] truncated continuation**: After "Ex mss. et ed. 1 restituimus male omissum *semper*", OCR shows "Paulo ante ed. Veneta cum Lugdunensi post *modus* adiungit" with the added word lost at column break. Likely *dicendi* (matches fn 10's note about *modus dicendi* / *modus*), but unconfirmed. Currently rendered with `[?]` flag and editorial bracket. → Resolve by checking PDF p. 247 fn 5 column break.

**d14-p1-a1-q2, apparatus [^7] missing referent**: OCR shows "Plurimi cum ed. 1 *creaturam*, quod refertur ad" with the referent dropped at column break. Currently bracket-supplied as "[*respectum vel effectum*]" based on body context. → Resolve by checking PDF p. 247 fn 7.

### d.14 p2-a1-q1 (2026-05-02 — actually Art. II q.1)

**d14-p2-a1-q1 = d14-a2-q1**: auto-chunker named this "p2" but Quaracchi labels it Articulus II. Frontmatter retained as `pars: 2, articulus: 1` for sibling consistency; rename to `articulus: 2` (no pars) needed across all 7 d.14 chunks. See d.13's rename precedent.

**d14-p2-a1-q1, p.280 apparatus block absent**: The OCR shows the p.279 footnote block (fns 1–11) but no separate apparatus on p.280. Body markers visible in OCR p.280 segment ("donum perfectum '", "Concedendum ergo est \", "ars bene vivendi':", "aliquid '", "datione *", "quia'", "transfertur *") were treated as scanner noise (typographic artifacts), NOT as footnote anchors. → Spot-check PDF p. 280 to confirm there really is no footnote block (low priority — page is mostly Ad-replies).

### d.14 p2-a1-q2 (2026-05-02 — actually Art. II q.2, *Utrum SS detur ab aliquo viro sancto*)

**d14-p2-a1-q2, Ad 8 sentence-gap**: OCR breaks mid-sentence after "dicendum, quod ordo" and resumes with "quia aliquae creaturae sunt ita nobiles". Filled with `[est in nobilitate creaturarum,][?]` based on natural reading of the surrounding argument. → Spot-check PDF p. 233 (printed) to recover the actual phrase between "ordo" and "quia aliquae".

**d14-p2-a1-q2, fn 27 (anchor *congruenter*)**: OCR for footnote keyed to "patiens congruenter" on p. 233 is missing/garbled in the raw block I have. Inserted placeholder `[^27]` entry; → reread PDF p. 233 footnote band for the actual Vat./codd. variant note.

**d14-p2-a1-q2, scholion I cross-references**: "Cfr. supra d. 3. p. 1. q. 2.[?] ad ult.; et II. Sent. d. 16. q. 1. a. 1.[?]" — OCR garbled the precise refs ("d. ?, q. 72. m. 4. — S. Tliom." etc.). Numbers shown are best-guesses from PDF p. 233 read; → reverify in 600 dpi extract.

**d14-p2-a1-q2, scholion II citation list**: "B. Albert., hic a. 16.[?]" and "Aegid. R., ... II. Sent. d. 26. a. 1. q. 4.[?]" — small superscripts unclear in 400 dpi extract. The rest of the list (Alex. Hal., S. Thom., Petr. a Tar., Richard. a Med., Durand., Dionys. Carth.) is clean.

**d14-p2-a1-q2, fn-renumbering**: Quaracchi numbers footnotes per page (p.230 1–9, p.231 1–15, p.232 1–6); Tier-2 chunk renumbers continuously 1–29. Verified anchors against OCR marker positions; ambiguous ones above flagged. No silent guesses on body text itself.

### d.14 p1-dubia (2026-05-02)

**d14-p1-dubia, Dub VI footnotes 24/25/27/28**: Dub VI body spans pp. 234–235 (page break mid-word "impro-/prie"). The first half's footnote anchors are on p. 234 (numbered through 18); the second half's anchors (intra, deficiente, fluvius — body markers ', *, ^) live on p. 235's footnote band, which my IA OCR fragmented and the 400 dpi extract is hard to read clearly. Apparatus entries [^24], [^27], [^28] are placeholders. Fn [^25] (Gregory's *Operatur enim magna...*) is real but the exact locus (*Hom. in Evang.* 30 vs *Moralia*) needs verification — Bonaventure attributes it to Gregory but it's elsewhere ascribed to Bernard. → reread PDF p. 235 footnote band (zoom region: lower 25% of page) to recover the four/five Quaracchi entries.

**d14-p1-dubia, Dub II Magister cross-ref**: OCR has "accipit Magister "." — fn anchor with stray quote-marks. Treated as anchor for [^4] (the cod. dd alt-solution block). Confirmed against PDF p. 233.

**d14 dubia chunk-name**: chunk file is `bon-sent-I-d14-p1-dubia.md` but Dist. XIV has no genuine pars division at the dubia level — `pars: 1` in frontmatter is auto-chunker carryover. Same renaming sweep d.13 received is still pending for all 7 d.14 chunks (see prior memory entry).

**d15-p1-divisio, body line "quantum ad modum"**: OCR ends column at "ubi incipit agere quantum ad modum" with no following word, but apparatus fn 1 references "post *processionis* addit ..." indicating *processionis* should follow. Body left as OCR (period after *modum*) and Vat. variant noted in fn; verify against PDF p. 288 column break.

**d15-p2-divisio, NOTAE block straddling littera/divisio**: NOTAE AD COMMENTARIUM at raw lines 49480–49499 contains 4 entries; only entries (3) "Fide mss. ... removimus verba praemissa quaestione" and (4) "*unam* / *Aliam*" anchor in this divisio body. Entries (1) "Errorem ... eliminando particulam *non*" and (2) "Nempe propositionem, quae est: Filius est factus" reference the LITTERA tail at raw lines 49404–49412 (last paragraph of Lombard's text on p2 about *factus secundum humanam naturam*). Plan: include (1) and (2) in the d15-littera chunk when built.

**d15-p2-divisio, printed_pages [313, 314]**: Best-guess based on line position (49426) following ~5 questions of p1 from p. 289. No running-head page number visible in the OCR for this column. Verify against PDF.

**d15-p1-dubia VI / p2-divisio NOTAE re-attribution**: The 4-entry NOTAE block at raw 49480–49500 (between p1-dubia VI's response and p2-divisio's body) was earlier flagged as having entries (1) *non/factus* and (2) *Nempe Filius est factus* belonging to "littera tail." Correction (2026-05-02): both belong to **dubia VI's response** at body line "Ad illud quod obiicitur, quod est factus" — Lombard's text was emended by Quaracchi editors to remove a spurious *non* before *factus*. Now correctly anchored as [^27] in dubia. Entries (3) and (4) remain in p2-divisio. The "littera will fold them in" plan is cancelled.

**d15 p2-dubia chunk missing**: auto-chunker (vol1/_backup-d15-pre-rebuild-20260502/bon-sent-I-d15-p2-a1-q3.md original) folded p2-dubia DUB I body into q3's chunk (line_end was 50157). Trimmed q3 to 50132 in this Tier-2 pass. p2-dubia chunk file does NOT yet exist; raw text spans approximately lines 50140 (DUBIA CIRCA LITTERAM MAGISTRI / DUB. I) through ~50500+ (DUB I–VI). DUB I body is on p. 273, DUB II at line 50158, DUB III at 50175, DUB IV at 50258, DUB V at 50279, DUB VI at 50314. Apparatus blocks at 50209–50220 (1st col, fns for DUB I + tail of q3 response 4) and 50329+ (more fns for DUB IV/V/VI). Needs new skeleton file `vol1/bon-sent-I-d15-p2-dubia.md` next session.

## d.16 littera (2026-05-02 — Tier 2 build)

**d16-littera fn 18, p. 277 NOTAE 8**: Quaracchi prints `Phil. 2, 7` as the "et mox" cross-reference, but the Hilarius passage Lombard cites couples Ioan. 14:28 (*Pater maior me est*) with **Phil. 2:9** (*donavit ei nomen quod est super omne nomen*), not Phil. 2:7 (*formam servi accipiens*). Either (a) Quaracchi editors are silently cross-referring back to fn 13's Phil. 2:7 above, or (b) OCR garble of `2, 9` → `2, 7`. Image at 400 dpi reads `2, 7.` — preserved as-printed; flagged for verification against another Quaracchi printing.

**d16-littera fn 4 anchor disambiguation**: Body text reads `non ut appareret eis ipsa substantia`; NOTAE 4 records that codd. DE + originale read *eius* and codd. A read *eis eius*. Bonaventure prints `eis` per the body, so the marker is anchored at *eis*. The OCR shows the asterisk after `eis` (`eis*`), matching.

**d16-littera marginal subtitles stripped**: The IA OCR captured several Quaracchi marginal reading-aid notes inline (`oe visibiii visibili specie.` line 50437, `soiuuij Au-` near the *primo libro de Trinitate* citation at 50567, `Aiiter^./rius!"^` near the Hilary section at 50600–50601). These are sidebar headings ("De visibili specie", "Solutio Augustini", "Aliter Hilarius"), not Lombard's body; omitted per the d.14/d.15 littera convention.

**d16-littera body OCR garble at 50456**: `sed ad aliiui.` resolved as *sed ad aliud* (preserving Augustine's accusative). Confirms the printed Quaracchi reads `aliud`; not flagged inline since context is unambiguous.

## d16-a1-q1 (2026-05-02)

**Page-header OCR vs. memory.** Raw OCR shows "270" / "280" for the two physical page numbers framing q.I. Memory has d.16 littera at pp. 276–277 and divisio at pp. 277–278, which puts q.I at 279–280. Treated OCR "270/280" as misreads of "279/280" and set `printed_pages: [279, 280]`. Verify against PDF when next at the laptop with vol1 PDF open.

**p.279 textual-apparatus footnotes 1–7 dropped.** OCR lines 50741–50751 carry seven textual-variant notes (`In Vat. contra mss. deest missione`; `Ex mss. et ed. I supplevimus iterum`; `Vat. omissis verbis Magistri ...`; etc.) that annotate Bonaventure's *Commentarius* preamble + divisio of d.15 p. I–II — content already covered in `bon-sent-I-d16-divisio.md`. Did not duplicate them here. If those notes anchor to content actually in q.I (unlikely from positioning), recover from PDF p. 381.

**fn 1 anchor.** Anchor placed at first "Augustinus" of pro-arg 1 (the Lombard-citation footnote `Libr. IV. de Trin. c. 20. n. 28`). OCR-mark glyph is `'` (apostrophe = small superscript), spacing supports this position; verify in PDF.

**fn 3 (textual variant).** Anchored to sed-contra opener "videtur, quia". OCR line break at 50825 ends `...presented before "270"` — anchor placement is at the `quia` Quaracchi inserted; correct per the apparatus content.

## d16-a1-q2 (2026-05-02)

**fn 16 ("Ex multis codd. ... supplevimus *autem*").** First clause anchored at "Ex hoc patet primum" (start of replies to opposing arguments — the *autem* gets supplied between "hoc" and "patet"). Second clause "Post *accipit* supple: *Augustinus*" is unanchorable: *accipit* does not appear in the printed text. Flagged with `[?]` in apparatus entry; verify against PDF p. 384.

**fn 19 anchor.** "post revelationem excitat^N ad dilectionem" — the apparatus consolidates four variants (T+ed.1 *exercitat*, WXVZ *delectationem*, cc *ad devotionem et dilectionem*, *enim* vs *autem* substitution). Anchor placed at "excitat" before *ad dilectionem* per OCR position.

**fn 13 (sensibles/quaerentes).** Anchored at "iam provecti" — covers the Vat. *sensuales* / *quaerentes* substitutions occurring in the immediately preceding sentence ("Quidam enim volunt signa, ut puta sensibles; quidam intelligentiam quaerunt..."). Placement choice: at end of the sentence rather than at *sensibles* itself.

**Page split p.281→p.282.** Body crosses mid-paragraph at end of pro-arg 3 / start of pro-arg 4. `<!-- page 282 -->` placed before "4. Item, si missio est..." per running-head position in OCR (chunk line 86).

## d16-a1-q3 (2026-05-02)

**fn 20 anchor.** Quaracchi's apparatus note "Ad obiectionem quartam specialis a S. Doctore non est data responsio" is meta-textual — there is no body anchor in Bonaventure's reply chain because the reply is missing. Placed `[^20]` at a stub heading `*[Ad 4.][^20]*` between the *Ad 3* and *Ad 5* replies. Renders as a footnote with no body context other than the heading; reader will see why.

**fn 24 anchor.** Apparatus says "Supple: *columba*, vel pone cum codd. Y Z *quae* loco *quia*" — the editors note that *columba* is to be supplied as subject of *erat pretium redemptionis*. Anchored at "in columba, quia" (the *quia* before *erat pretium*); did not actually insert *columba* into the text body. PDF check would confirm.

**Page split p.283→p.284.** Body crosses just before "ideo Spiritus sanctus apparuit in creatura irrationali" per OCR running-head/page-number positions (raw line ~51593). Placed `<!-- page 284 -->` there.

## d17-littera (2026-05-02)

**fn 41 anchor — IV. Reg. 2:9 long marginal note.** Quaracchi prints a long codd-ABCDE marginal note glossing the Elias/Eliseus passage with a quotation from "In libro Regum legitur sic..." up through "non esse discipulus super Magistrum postulavit." This is a SCHOLIASTIC marginal note added by the codd., not part of the body. Rolled into apparatus entry [^41] as block-quoted note. PDF spot-check would confirm transcription of the note's tail ("postulavit").

**fn 47 textual point — *liberatorem* vs *propitiationem*.** Lombard's text has "misit Filium suum *liberatorem* pro peccatis nostris" (1 John 4:10). Quaracchi flags Vulgate has *propitiationem* and edd. 1, 8 with Augustine read *salvatorem* (= Greek ἱλασμόν, "propitiation"). We retain Lombard's *liberatorem* in body and document the variants in the apparatus entry.

**fn 56 — Wisdom 7:22 word order.** Quaracchi flags that the Vulgate inverts the order: *mobilis, incoinquinatus, certus*, but Lombard has *mobilis, certus, incoinquinatus*. We retain Lombard's order in body.

**fn 61 — distinction boundary editor's note.** This is not an ordinary apparatus entry but a Quaracchi editor's meta-note about where d.17 ends and d.18 begins (Vat. and most editions push d.18's opening into d.17; codd. ABCD + edd. 1, 2 + the early Commentators draw the boundary correctly). The fn marker is anchored at "dona eius" (the very last quoted word of Lombard's cap. VI tail). The note's apparatus entry on p. 291 properly belongs to the divisio chunk's territory, but content-wise it bridges the two — left here so readers see the editorial decision in context.

**Page boundaries used.** p.287 ends after "interiorem, quia certiorem"; p.288 spans "Amplectere dilectione Deum..." through "*Deus ergo caritas est*"; p.289 spans "Tunc enim mitti vel dari..." through "alioquin et irrationales creaturae haberent Spiritum sanctum, quod fidei pietas non admittit"; p.290 spans "Ut autem certius fiat..." through "...non videtur esse Spiritus sanctus"; p.291 (tail of littera only) spans "Ad quod dicimus..." through "...sed dona eius". Quaracchi's odd-page running heads not all preserved by OCR; boundaries inferred from even-page running heads ("SENTENTIARUM LIB. I.") and column-break visual cues — recommend a 300-dpi PDF spot-check before any heavy quotation from these page-break boundaries.

**OCR fix — line 49 "*influere*" with closing-quote stub.** OCR rendered the fn anchor as `''` (two apostrophes) which I read as a single fn marker. Verified the corresponding apparatus entry "Sola Vat. *astruere*" matches a single anchor at "influere" — the mark is fn 5 of p. 287.

**OCR fix — fn anchors `'`, `^`, `*`, `''`, `°` etc.** Quaracchi uses superscript Roman lowercase letters (a, b, c, ...) for textual variants and superscript Arabic numerals (1, 2, 3, ...) for source-citations on the same page; OCR collapses both to glyphs like `'`, `^`, `*`, `°`. We've renumbered them as a continuous 1..61 chunk-wide for compatibility with the unified chunk format.


## merged from tier2-ambiguities-d17-divisio.md
# d17-p1-divisio Tier-2 ambiguities (2026-05-02)

Per-chunk staging file — written in parallel with two sibling agents to avoid write conflicts on the main `tier2-ambiguities.md`.

## d17-p1-divisio (raw 52652–52771, p. 291 + bridging into p. 292)

- **Apparatus span across page break**: NOTAE AD COMMENTARIUM appear in two blocks — two notes on p. 291 (first appearance of the block, immediately under the COMMENTARIUS preamble) and three notes on p. 292 (interspersed with q.1's NOTAE in the OCR). p. 292 NOTAE 1–3 belong to the divisio (matching body markers `Deus, et'`, `concludit"`, `a^ non habente`); NOTAE 4+ on p. 292 belong to q.1. Renumbered 1–5 continuously within the divisio chunk.
- **OCR garble `cariiate`** (p. 292 NOTA 4) — non-issue here since that note is q.1, not divisio.
- **OCR garble `aliqwo`** (p. 292 NOTA 3) → silently corrected to `aliquo`.
- **Body marker placement**: OCR has `Hie quaeritur` for `Hic quaeritur` (intra-Latin reference); silently corrected.
- **`yVe autem`** (line ~52685) is OCR garble for `Ne autem` (capital N misread as `yV`); silently corrected.
- **`liabet` / `noti/icat` / `confirmal`** silently corrected to `habet` / `notificat` / `confirmat`.
- No `[?]` flags raised — all OCR garbles in this chunk resolve unambiguously by Quaracchi context.

## merged from tier2-ambiguities-d17-a1-q1.md
# Tier-2 ambiguities — bon-sent-I-d17-p1-a1-q1

Per-chunk staging file. Merge into `tier2-ambiguities.md` after parallel agents settle.

## Resolved silently from OCR (no [?] flags raised)

- OCR `r.irca` → `Circa` (capital C lost to dropcap)
- OCR `nuUa` → `nulla`, `eflQciatur` → `efficiatur` (l/I + Q-tail OCR garbles)
- OCR `infmitae`/`inflnitum`/`inflammat` → `infinitae`/`infinitum`/`inflammat` (long-s and ligature confusion)
- OCR `babitus`/`habilum` → `habitus`/`habitum`
- OCR `temoni` retained (genuine: rudder/tiller)
- OCR `Voluntas eniin` → `Voluntas enim`
- OCR `aniraam`, `niotoris`, `etfectus`, `oliiicitur` etc. — silent fixes throughout
- Marginal subtitles (`Fundamenta.`, `Rationes idem.`, `Opinio Mag.`, `Expositio huius positionis`, `Ratio huius positionis`, `Reprobatur`, `Alia expositio per triplici distinctionem`, `Iudicium de Magistro`, `Rationes`, `A parte essentiae`, `Solvuntur rationes primae`, `Aliter`, `Solvuntur secundae rationes`, `Alia solutio`) — stripped from body; they bleed in OCR but are editorial running glosses.

## Genuine [?] candidates (none flagged inline this pass)

OCR baseline was clean for the body and apparatus of this quaestio; no `[?]` markers were inserted in the chunk. The most awkward verifications were:

1. **fn 22 marker placement** — Master cites Joh. 17, but printed apparatus reads `Vers. 21` (i.e. *Ut sint unum* is John 17:21, while the body's reference text says "decimo septimo"). Apparatus simply gives verse number; correctly preserved.
2. **fn 31 (1 Cor. 3:9) replacement of *similiter* → *sibi*** — Quaracchi's own conjecture, well-documented in note. Translated as written.
3. **Apparatus 12 (codd. variant on `caritas dicit quid creatum`)** — long textual note. Translated literally; preserved Quaracchi's hesitating stance (*non est spernenda, immo magis placeret quam ceterae*).
4. **fn 35** — Quaracchi flags M aa bb's *reformatio* for *recreatio* as "formaliter loquendo melius"; preserved.

No PDF re-read needed; OCR was sufficient at every point.

## Doctrinal anchor preserved

The critical move — Bonaventure rejects the Master *materially* but excuses him *as having only "fallen short" (defecit)* — is rendered:

> "And in all these things he spoke truly and did not err, but fell short."

And the closing softening:

> "And in this there was not error, but only a defect."

Both rendered consistently, *defectus* = "defect" / "fell short" in this chunk.

## merged from tier2-ambiguities-d17-a1-q2.md
# d17-p1-a1-q2 Tier-2 ambiguities (2026-05-02)

- **OCR fundamentum 3 (`propter quod unumquodque et illud magis`)**: OCR has `n[n]umquodque` (likely typo for `unumquodque`) and `illud` (apparatus note 1 confirms Vatican reading `illud` vs mss `aliud`). Set as `illud` per Vat with `[^2]` flagging the variant. The Aristotle citation note immediately follows as `[^3]`. PDF spot-check could confirm whether the exponent in OCR really sits between `unumquodque` and `magis` (currently emitted at end of clause).
- **OCR `homm` in respondeo (raw `optat alicui homm`)**: clearly OCR garble of `bonum`. Silently corrected to *bonum*. (Confirms the *amor amicitiae* definition: wishing the good for another.)
- **OCR `comwpiscentiae`** (twice in respondeo passage): silently corrected to *concupiscentiae*.
- **OCR `dihgam` / `dihgat` / `diUgere` / `dihgenda` / `dilectionem` / `aniicitiae` / `aniicitiae`**: standard `li`/`m`/`n` ligature OCR errors, silently corrected.
- **OCR `cliligenda` (running-head Latin title)**: corrected to *diligenda*.
- **Apparatus [^7] `diligei` variant**: OCR shows `diligel` (likely `diligei` or `diliget`). Kept as printed *diligei* — this is the OCR rendering of the variant reading itself, not editorial Latin, so a [?] would be appropriate here for spot-check. Flagged.
- **Apparatus [^14] `delectatio` vs `dilectio`**: OCR has `defectatio` for the variant; silently corrected to *delectatio* (Quaracchi's standard contrast term). Spot-check with PDF if any doubt.
- **Apparatus [^17] `formax speciaks`**: OCR garble for *formae speciales*.
- **Apparatus [^21] `Libr. II Sent. d. 2.3.`**: OCR `2.3.` clearly = `23`; likewise `1-3` for `q. 1-3`; rendered as such.
- **Apparatus [^22] codex list `ABDFGHiVqTZ ee (f`**: OCR's `iV` and `(f` likely = `N` and `ff`. Rendered as A, B, D, F, G, H, N, q, T, Z, ee, ff.
- **Page-break placement**: signature `38` between p. 297 and p. 298 fixed at `Et si quaeratur`. Mid-respondeo `297` marker placed at the body break before *tiae, quia Augustinus loquitur*; that landed mid-sentence in OCR, so the `<!-- page 297 -->` is set at the start of the *Ad 1* paragraph for readability. Not a substantive shift.

## merged from tier2-ambiguities-d17-a1-q3.md
# Tier-2 ambiguities log — d17-p1-a1-q3

Per-chunk staging file. Concatenate into main `tier2-ambiguities.md` after parallel agents land.

## Resolved silently from OCR garbles

- Heading `gl!.\ESTIO [11.` → `QUAESTIO III.` (well-attested OCR ligature: `gl!.\E` → `QUAES`; bracket `[` → `1`).
- Subheading `Ulrum (jim cerlitudinalUer scire po.isit, se csse in carilnte.` → `Utrum quis certitudinaliter scire possit, se esse in caritate.` (`(jim` → `quis`; `U` mid-word → `i`; `csse` → `esse`).
- Numbered fundamentum 5 printed in OCR as `0.` (zero) — restored to `5.` from context (it follows fund. 4 and continues the *videtur quod sic* series).
- Conclusion block printed `ffotno in slatu viae, seclma revelatimie` → `Homo in statu viae, sed sine revelatione`. The OCR `seclma` is hard to read; restored as `sed sine` per the substantive corollary that revelation is the only path to certainty (matches respondeo's "nisi per revelationem").
- Contra arg 4 OCR: `haheris caritatem est Deo acceptus, e) hoc*` — restored to `habentis caritatem est Deo acceptus, et hoc` (genitive `habentis` is the natural construction "[it belongs to] the one having charity to be acceptable to God"; `e)` → `et`).
- Respondeo §3 OCR `Una el praecipua` → `Una et praecipua` (one well-attested glyph slip).
- Footnote 8 OCR `Vat. cnm cnd. cc aii itiis, el niox infrii loco ita` is murky — preserved as `Vat. cum cod. cc *ab itiis*, et mox infra loco *ita*`. The variant `ab itiis` is implausible; could be `ab istis` or another reading. Flagged below.

## `[?]` flags (none kept inline this round)

I resolved silently above rather than leaving inline `[?]`. Concerns to surface to a second reviewer:

1. **fn 8 `ab itiis`** — almost certainly an OCR garble of *ab istis* or similar; the Vatican-codex-cc reading should be cross-checked against PDF p. 298 if a clean print is at hand.
2. **Conclusion `seclma revelatimie`** — restored `sed sine revelatione` on doctrinal grounds; the second word might also read *secundum* (yielding "according to revelation"), but that flips the sense and contradicts the respondeo, so `sed sine` is the safer reading.
3. **Sub-conclusion marginal labels** `conchjsio 1.`, `conchisio 2.`, `Raiio I.`–`Raiio IV.`, `concin` (margin labels in Quaracchi) were dropped from the body since the printed margin glosses are not part of Bonaventure's text. The structure they label is preserved by paragraph breaks and explicit numbering.
4. **Apostolus footnote (page 299)** — fund. 5 contra (`Apostolus '`) cites *I. Cor. 4, 4* per OCR fn 1; this is the same passage as contra arg. 2's footnote 7. Both anchors retained.

## merged from tier2-ambiguities-d17-a1-q4.md
# Tier-2 Ambiguities — d.17 p.1 a.1 q.4 (2026-05-02)

Per-chunk staging file. Concatenate into the main `tier2-ambiguities.md` after this chunk + sibling q.3 + dubia all complete.

## Resolved silently from OCR + context

- **Title (running head, OCR garbled)**: OCR reads `Ulrum  carilas  in  universali  sit  cognoscibilis  etiam  a  non  habente  eah` — clearly the printed running head with `eam` mangled to `eah` and `Utrum` to `Ulrum`. Resolved to *Utrum caritas in universali sit cognoscibilis etiam a non habente eam*. (Cross-checked against the divisio's *tractatio quaestionum*, which gives the shorter form *si possit cognosci a non habente*; the running head adds *in universali*, *etiam*, and *eam*, all consistent with Quaracchi practice. Title kept as printed.)
- **arg. 1, OCR `Sed ^ non per essentiam`**: footnote-anchor `^` displaced after `Sed`. Apparatus entry [^3] in the Quaracchi (re-numbered [^1] here) explicitly says *Ex mss. et edd. 1, 2, 3 supplevimus scilicet*, so the footnote anchor belongs to the supplied *scilicet* (which the editors place after *Sed*). Marker placed at end of `Sed`.
- **arg. 1, OCR `secundae ad Corinthios duodecimo` + `quae non sunt ipsae»`**: the Glossa quotation has `intellectiva` for `intellecta` per apparatus [^2]; preserved Bonaventure's reading.
- **arg. 2, OCR `aut per primam lucem ^`**: the `^` is the apparatus marker for [^3] (Vat. omits *aut per primam lucem*); placed at end of clause.
- **resp., OCR `Cognoscit igitur anima, quid sit reclitudo`**: `reclitudo` → *rectitudo* (cl/ct OCR confusion). Silent fix.
- **resp., OCR `et quaedani directio uaturalis`**: `quaedani` → *quaedam*; `uaturalis` → *naturalis*. Silent fix.
- **Scholion II, OCR `Necessario enim oportet ponere, quod anima novit Deiim et se ipsam`**: `Deiim` → *Deum*; silent.
- **Scholion III, no. 5, citation closing**: OCR ends `nec a nobis na-` mid-word with line break and no closing quote/bracket. The Augustinian phrase from *de Trin.* IX. c. 7. n. 12 is *nec a nobis nascendo discedit*. Restored as `nec a nobis na[scendo discedit]».` with editorial brackets indicating the printed text's truncation.
- **Scholion III, no. 4, OCR `(VIII.  c.  3.  n.  i.)`**: the lowercase `i` is a Roman numeral typo for `4`; the cited passage is *de Trin.* VIII c. 3 n. 4. Resolved to `n. 4`.
- **Scholion III, no. 4, OCR `n.  7.).` after `(ibid.  c.  i.  5.  n.  7.)`**: `c. i. 5.` is OCR confusion of `c. 4. 5.` (Augustine *de Trin.* VIII c. 4–5 n. 7). Resolved.

## Flagged `[?]` (none in body)

No inline `[?]` flags in body. All ambiguities resolved against context + sibling chunks (q.1, q.2 doctrinal anchors) + apparatus content.

## Note on apparatus numbering

The printed Quaracchi has 13 footnotes on p. 301 (numbered 1–13) and 12 footnotes spanning pp. 302–303 (re-started 1–12 in two batches: pp. 302 has 1–12, p. 303 has 1–2). Per Tier-2 convention, anchors renumbered continuously 1–21 in this chunk. Page 303 footnotes 1–2 (which gloss the closing *Unde quod Augustinus dicit* paragraph) became [^20] and [^21] here.

## Cross-references confirmed

- **Doctrinal anchor** *cognitio experientiae* / *cognitio speculationis* (intuitive / abstractive distinction) introduced here; foreshadowed in q.3 (per divisio frame).
- **Anselm reflexive-will citation** in Scholion I subordinate point matches q.2's [^19] (*Anselmus, libr. de Concord. praesc. et lib. arb. q. 3. c. 11*) — same locus, same point, different framing.
- **Scholion III, no. 5** cites *de Trin.* VIII c. 6 n. 9 — same Augustinian text Bonaventure leans on in q.1 for the *quo diligimus Deum* analysis. The "iniustus knowing iustus" question is the structural parallel for the present q.4 (*non habens caritatem* knowing *caritas*).

## merged from tier2-ambiguities-d17-dubia.md
# Tier-2 ambiguities — d17-p1-dubia (2026-05-02)

Per-chunk staging log. To be merged into `tier2-ambiguities.md` after parallel agents finish.

## Resolved silently (OCR garble → obvious correction)

- `niB. I.` → `DUB. I.` (and `DuB. IV.`/`DuB. V.`/etc. similarly normalized)
- `Respondeo: Dnpiextia bona...` — `Dnpiex` is a marginal gloss `Duplex` bleeding into the line; trimmed (per CLAUDE.md "marginal glosses bleeding inline").
- Marginal `Aib sointio.`, `Dapiex lu-`, `dapiicM le-`, `Aii.i i|iiae-`, `Ad-2.`, `Q..aesi`, `Deus d`, `Non si`, `Dnpiei mo-/senti?™"`, `Hios.'` — all stripped as marginal apparatus tags.
- `pai-to` → `parte`; `(lubitationes` → `dubitationes`; `dvai` → `circa`; `priuKt` → `primo`; `(luliitatur` → `dubitatur`.
- `pro.rimum` → `proximum`; `coii.tniiifiii.s-` → `consequens`; `Videtiu-` → `Videtur`.
- `(jilectionem` → `dilectionem`; `Uem` → `Item`; `comequem` → `consequens`.
- `crcala` → `creata`; `secjuitur` → `sequitur`; `secnnda'` → `secunda`.
- `acceplatio` → `acceptatio`; `anior` → `amor`; `liabere` → `habere`; `lucem habitat inaccessibilem` (so OCR; Vulg. `inhabitat`, see fn).
- `ralionem` → `rationem`; `aliqua` (passim).
- `manilestare` / `mani-iestare` → `manifestare`.
- Body/apparatus footnote markers re-numbered 1..40 continuously.
- Page break inserted after line 54667 (printed p.303 → p.304); a second page break is around the boundary of Dub V (between line 54817 apparatus block and 54827 body — pp. 305 → 306). p.305 had no surviving page-number marker in OCR (column footer), so I marked just two `<!-- page -->` comments that I could pin reliably (304 and 306).

## Open `[?]` — none flagged inline

The chunk OCR was unusually clean once marginals were stripped; no genuine `[?]` ambiguities remain. Two near-calls accepted as written:

- `Et ita ex hoc, quod caritati coniuncta;` (Dub VI end) — OCR `coniuntUa` clearly = `coniuncta`; sentence is elliptical in Latin (verb `est` understood), preserved in English with a dash-style supplement.
- Dub V apparatus fn 21 (Vat. *sic* / *si*) ends with the fragmentary `et quidem` which the apparatus continues on the next column in the print; rendered "and indeed." as the final clause.

## Notes for cross-merge

- Skeleton frontmatter `line_end: 54577` was a chunker bug (cut after fn 8 of Dub I). Real range 54529–54959. New `word_count_latin: 2284` (recomputed).
- 7 dubia, 40 footnotes total, no scholion in this chunk.

**bon-sent-I-d28-a1-q4, apparatus [^11]**: page-503 footer ³ OCR reads `Codd. et edd. impncessibilitas , sed  m  nominis.` — text is clearly garbled mid-line and the marginal pickup of "sui nominis" from the right column has bled in. Body ms. anchor sits on the word `inspirabilis` in the *Respondeo* (corresponding to OCR `inspirahilis`). Currently rendered as: codd./edd. read `improcessibilis`, but it should be read `inspirabilis`. → Resolve via printed page 503 PDF eyes-on if footer can be recovered.

**bon-sent-I-d5-a1-q2, apparatus [^8]**: OCR footer note 7 (page 115) reads `Vat. praeter fidem mss. et ed. 1 addit est. Textum Magistri vide in lit. c. 1. et 2. circa finem.` — single footnote bundles two distinct items: (a) Vat. variant adding *est* in `substantia [est] de substantia` (anchor on `substantia⁷` line 26368), and (b) cross-reference to the Master's text `c. 1 et 2 circa finem` (which logically attaches to `littera *` at body line 26266 — already given footer note `Hic c. 1 post medium` = my [^1]). Currently rendered: both items kept under [^8] anchored on `substantia`, English notes the cross-ref. → Resolve via 600dpi PDF eyes-on of p.115 footer to confirm whether Quaracchi's footer 7 truly bundles both, or OCR has merged adjacent notes.

## bon-sent-I-d5-littera (2026-05-10 d.1-d.10 rechunk pipeline from-scratch)

No `[?]` flags placed inline. The Lombard text on Distinction V is well preserved in the Quaracchi OCR; all marker-position attachments resolved cleanly against the per-page footer numbering (p.108 = 14, p.109 = 11, p.110 = 14; total 39 entries). OCR garbles in the apparatus block (e.g. *supernue* for *supervacue*, *anle* for *ante*, *Trinilate* for *Trinitate*, *insiimatione* for *insinuatione*, *piaesentlie- seos* for *parentheseos*) were silently corrected where the printed-Latin intent was unambiguous. No flagged residues.

**d6-a1-q1, arg. 2 / apparatus [^2]**: OCR `emanat alj alio ^` and footer `Nonnulli codd. ut KWXY ee aliqm pro alio`. The variant reading `ee aliqm` looks corrupt (likely `ex aliquo` or `ab aliquo`). → Rendered as printed `ee aliquo` with [?]; needs PDF eyes-on at p.125 footer fn 2.
**d6-a1-q1, apparatus [^12]**: OCR `quae in praecedentibus taclai'` — last word truncated/garbled at line break. Likely `tactae sunt` or `tactae`. → Rendered `tactae [sunt]` with [?]; PDF check at p.126 footer fn 4 needed.
**d6-a1-q1, scholion II**: OCR ends `B. Albert., hic` mid-sentence (line 28041) and the next line begins page 126 footer block, suggesting scholion II continues but is cut at the chunk boundary at line 28085. → Rendered with trailing [?]; the full citation list may extend onto p.127 in raw OCR — pending verification once d.6 a.1 q.2 chunk is built.

## d.7 divisio (2026-05-10 from-scratch rebuild)

**bon-sent-I-d7-divisio, body line ~"utrum [potentia] generandi sit in Filio"**: OCR raw line 29126 reads `utrum / generandi sit in Filio` with the noun apparently missing across the column break (lines 29125-29126: `Filius possit generare ; in secunda , utrum / generandi sit in Filio`). Context demands *potentia*. → Rendered `[potentia]` editorially supplied with [?]; PDF p.134 col. 2 eyes-on at 600dpi to confirm.
**bon-sent-I-d7-divisio, apparatus [^5]**: OCR raw line 29289 `qui et pro genmdium ponunt germdimm` — both terms OCR-garbled. Quaracchi typically distinguishes *gerundium* vs *gerundivum*. → Rendered as `*gerundium* / *gerundivum*` with [?]; PDF p.135 footer note 5 eyes-on at 600dpi to confirm direction of variant.
**bon-sent-I-d7-divisio, p.134 footer block (raw lines 29133-29170)**: An additional ~10-11 textual-variant footer entries (markers 1-11 with `aliquam`, `accipiatur`, `Mendum Vat. omittentis`, `repetunt ex`, `Dist. XXVI`, etc.) belong to the page 134 footer apparatus, but their body anchors were lost in the OCR for the divisio's opening lines (29109-29132). → Currently rendering only the 8 anchored entries from p.135 footer. p.134 footer entries pending PDF eyes-on to identify body anchors and integrate.

## d.7 littera (2026-05-10 from-scratch rebuild)

**bon-sent-I-d7-littera, apparatus [^11]**: OCR raw lines 29137-29139 read `Mendum Vat. omittentis ; / 1,2,3,5,6,8,9,10. Paulo / •loco Potest ergo.` — the word being omitted (semicolon glyph followed by what should be a Latin word or particle) is OCR-garbled across a column break. → Rendered `Mendum Vat. omittentis [?]` with editorial flag; PDF p.133 footer note 3 eyes-on at 600dpi to identify the omitted lemma.

## bon-sent-I-d7-dubia (2026-05-10 from-scratch rebuild)

**d.7-dubia, Dub. VII tail (raw lines 31005-31015)**: OCR of the closing sentence is fragmented across stub-columns: `potentia potest in- / telligi ovi / formaliter, et / tem modo non / et sic est in solo Patre; vel / sic ponitur esse in Filio; alio au- / tem modo non`. Word "ovi" between "intelligi" and "formaliter" is unrecoverable from OCR; likely a corrupted adverb (possibly *uno modo* / *aliter*). Currently rendered with [?] flags at three points. → Resolve via 600dpi PDF p.146 (PDF p.248) eyes-on read.

**d.7-dubia, Dub. IV apparatus note 12 (p.146 footer line 30971)**: footer ends mid-sentence `ponit loco` with no further text in OCR before next note. The completing word (e.g. *hypostasim*, repeated) is cut. → Resolve via 600dpi PDF; flagged [?] in note body.

**bon-sent-I-d2-a1-q1, p.50 fundamenta intro**: OCR has *triplici habita suppositione* + *ratione status, qui non est nisi in summo et primo* — translated *status* as "rational ground of the *terminus*" (per app. note 12, *status* = principle beyond which one cannot pass in causal regress). [?] retained on phrase "rationale of the *status*" understanding. → Resolve: keep current literal "rational ground of the *terminus*" with [^12] in respondeo carrying the sense.

**bon-sent-I-d2-a1-q1, p.51 sed-contra arg.4**: OCR shows quoted maxim *« in aeternis sit idem esse et posse »* matches app. note 8's Aristot. III Phys. 32. No flag needed; cross-anchored at [^8].

**bon-sent-I-d2-a1-q2, apparatus [^17] (p.54 footer 6)**: PDF reads "Paulo post cod. X *unitas* pro *nullo*", but in the body the relevant passage is "quia illa a *nullo*" — and *unitas* would be a strange substitution. Possibly "*unitas*" is a misread of another variant, or the referent is not the body word I assumed. Currently rendered verbatim. → Resolve via fresh 600dpi recheck of p.54 footer 6 in next polish pass.

**bon-sent-I-d4-divisio, apparatus [^1] (p.96 NOTAB note 1)**: OCR reads "Vat. contra mss. et ed. 1 omittit *iid*." The token *iid* is unclear — likely OCR garble for *id* or *idem* (cf. p.96 footer note 1 above which mentions "item pro idem"). Body anchor placed on "Et" at start of second sentence of divisio (raw line 23493 "Et iucidit"); could equally anchor at "ponitur secunda pars" (line 23492) if *iid* refers to a different word. Currently rendered with [?] flag pending 600dpi PDF eyes-on. → Resolve at next d.1-d.10 polish pass.

**bon-sent-I-d4-dubia, DUB VII Respondeo (p.107 body)**: OCR "in sermone Tniiuntur sine oppositione" — Tniiuntur is a garble. Currently rendered "iungunt[?]" (joined). Likely *iuniuntur* / *coniunguntur*. Resolve via 600dpi PDF p.107 eyes-on.

## d.2 littera rebuild (2026-05-10)

- **bon-sent-I-d2-littera, p.46 footer note 8**: OCR garble «««*'« hoc» suggests Vatican-edition lemma is *audit hoc* (vs. text *audit haec*). Currently rendered *audit hoc*[?]. → Resolve via 600dpi PDF p.46 footer.
- **bon-sent-I-d2-littera, p.47 footer notes 36–37 (body markers [^36], [^37])**: Quaracchi printing has marginal rubric «*Aliae auctoritates*» appearing inline in OCR at this position; OCR also doubles the Gen. 1, 1 reference across the page-break. Currently flagged with [?]. → Resolve via 600dpi PDF p.47–48 to confirm whether these are two distinct apparatus entries or a single rubric+citation pair.
- **bon-sent-I-d2-littera, p.48 footer note 43**: apparatus footer uses *passus est* as a lemma but the body word at the marker position is *natus est* (Filius) / *processit* (Spiritus) — apparently a printer's slip in the apparatus. Currently rendered *passus est* (verbatim) with translator's bracket. → Resolve via 600dpi PDF p.48 footer.

## d.4 a.1 q.3 from-scratch rebuild (2026-05-10)

- **bon-sent-I-d4-a1-q3, Respondeo "sic nec hoc[?] nomen Deus"**: OCR has `hoc''` (double-apostrophe glyph). Likely a footnote marker in OCR that did not survive transcription cleanly; no corresponding footer note on p.102 maps unambiguously. Currently rendered `hoc[?]`. → Resolve at decade-end with 600dpi PDF eyes-on (printed p. 102).
- **bon-sent-I-d4-a1-q3, app. [^5] (Priscian)**: OCR has `II.  Grammat.  c.  S.` — the `S` is almost certainly OCR for `5` but flagged because Priscianus *Inst. Gramm.* II.5 vs II.S unclear without PDF check. Currently rendered `c. 5.[?]`. → Resolve with 600dpi PDF.
- **bon-sent-I-d4-a1-q3, app. [^8] (Cod. R addit genuit)**: OCR-anchored text `Cod. R addit genuit.` is grammatically odd in this q.3 context (no obvious Respondeo word for *genuit* to attach to); placement at the start of the page-101 footer block is unambiguous, but the lemma it glosses is not. Currently rendered with [?]. → Resolve with 600dpi PDF.

## d.4 a.1 q.1 (2026-05-10 from-scratch rebuild)

**bon-sent-I-d4-a1-q1, scholion §I opener**: OCR garbles "explicationem aliquor[??] / quae in liac quaestione" — likely *aliquorum terminorum*. Currently rendered "aliquorum [terminorum?]". → Resolve with 600dpi PDF p.98 footer/scholion margin.
**bon-sent-I-d4-a1-q1, app. [^10] (p.98 fn 2)**: OCR ends "tract. de Re-" cut at line break, never resumes — clearly *Restrictione*. Currently rendered "Re[strictione?]". → Resolve with PDF p.98 footer.
**bon-sent-I-d4-a1-q1, app. [^14] (p.98 fn 6)**: OCR `non multiplicabilem in i` truncated mid-line — Quaracchi's emendation almost certainly *immultiplicabilem* (matches body text). Currently rendered "*immultiplicabilem*[?]". → Resolve with PDF p.98 footer.
**bon-sent-I-d4-a1-q1, app. [^15] (p.98 fn 7)**: OCR `Vat. contra antiquiores codd. et ed. I addit i` — added word truncated. Currently rendered "[verbum?]". → Resolve with PDF p.98 footer.
**bon-sent-I-d4-a1-q1, app. [^16] (p.98 fn 8)**: OCR `non liabeat suppositionem aliam a / sito antecedente` — `[suppo]sito` lost across line break. Currently rendered "[supposito?]". → Resolve with PDF p.98 footer.
**bon-sent-I-d4-a1-q1, app. [^17] (p.98 fn 9)**: OCR `Cod. K. addit dcut hic` — *dcut* almost certainly *scilicet* abbreviation. Currently rendered "[scilicet?]". → Resolve with PDF p.98 footer.

**bon-sent-I-d9-littera, multiple**: d.9 littera rebuild from scratch 2026-05-10. (a) Cap. III. header marked [?] — OCR shows "Cap. III." indirectly through running placement; chapter rubric placement between Ambrose Cap.I/II blocks and Cap.V is ambiguous in OCR column glitch (lines 35687-35690); the printed page likely shows Cap. III. with running-head context but PDF eyes-on needed. (b) [^13] Isaiah 53,8 — OCR note 6 on p.178 reads "Cap. 33, 8." which is implausible as a Hieronymus Eccl. cap (only 12 chap); rendered as Isai. 53, 8 (the Isaiah ineffability prooftext at body "Generationem eius quis enarrabit?"). Resolve with 600dpi PDF p.178 footer band check.

## 2026-05-10 batch — d.1-littera from-scratch rebuild

**bon-sent-I-d1-littera, p.27 "In homine autem spes ponenda..."**: OCR line 12981-12982 reads `In homine autem spes ponenda / quia Maledictus est qui hoc facit` — predicate of "spes ponenda" missing (compare Augustine's original *De doctr. christ.* I.22, which has "spes ponenda non est"). Apparatus note 18 (raw line 13051: "mss. omnes et edd. 1, 8 male... omittunt nos ante consolatur") flags an adjacent omission but not this one. Currently rendered as "*spes ponenda non est*[?]" in the English on conjectural restoration; the Latin body preserves the OCR as-is. → Resolve at next 600dpi PDF eyes-on pass.


## bon-sent-I-d3-littera (2026-05-10 from-scratch rebuild)

- **d3-littera, p.62 apparatus [^2]**: OCR truncates the second text-critical footnote at line 18357–18358 ("Codd. CDE et" — entry breaks). Currently rendered as `[?]` flag inline. → Resolve via 600dpi PDF extraction of p.62 footer (PDF page 164).
- **d3-littera, p.63 apparatus [^8]**: OCR shows `BCDE et ed. I , omisso` then breaks mid-clause before `Iranspositis verbis`. Word governed by `omisso` (likely `vel` or `vestigium`) not legible. Marked `[?]`. → Resolve via 600dpi PDF p.63 footer (PDF 165).
- **d3-littera, p.65 "in anima"**: Body OCR at line 18732 reads `in  anima'` with an apostrophe-shaped marker; the footer at 18818 gives `Codd. et edd. 1, 3, S, 6, 7, 9  animo.` That variant note is merged into [^39] (which covers note 10 of the printed footer) rather than given its own anchor; the anchor in body is left as `[?]` inline (English side only) to preserve the OCR signal. → Verify via 600dpi PDF p.65 footer.
- **d3-littera, p.66 entire footer block absent from OCR**: Anchors [^43]–[^45] (Augustine *de Trin.* IX; Fulgentius/Pseudo-Aug. *de Fide ad Petrum*; closing citation) all rendered as `[?]` placeholders. Raw text terminates at body line 18874; COMMENTARIUS begins 18876. → Extract p.66 footer (PDF 168) at 600 dpi and backfill the three notes' specific chapter/n. citations.
- **d3-littera, p.64 [^17]**: The OCR-listed footer entries for p.64 conflate the running reference to *de Trin.* libr. xiv with the preceding "Cap. 8, n. 11" of note 16; rendered as a stitched-together pair with [^17] flagged for verification.

## bon-sent-I-d3-p2-a1-q2 (2026-05-10 from-scratch rebuild)

- **d3-p2-a1-q2, app. [^3] (p.82 fn 3)**: OCR variant note refers to Cod. R `quia enim in Filio proprie est imago` and codd. P Q `cognita` loco `cognoscendi` — but neither phrase appears in the printed body of this question. The variant likely applies to a passage modified by Vat. that was suppressed in the Quaracchi text. Currently anchored at body "et particeps" (placeholder); `[?]` flag on apparatus content. → Resolve with 600dpi PDF p.82 footer band check to confirm note 3's actual body anchor.
- **d3-p2-a1-q2, app. [^9] (p.82 fn 5, "Cfr. supra d. 1. a. 1. q. 1.")**: Cross-reference note has no obvious body anchor in the OCR text. Currently anchored at body "his potentiis" (end of arg 3, before page break). `[?]` flag on apparatus content. → 600dpi PDF p.82 eyes-on to confirm.
- **d3-p2-a1-q2, p.84 apparatus block absent from OCR**: Raw OCR jumps from body line 21636 directly to SCHOLION (21639), with no footer block between. The p.84 footer was recovered via 700dpi PDF extraction; entries [^22] (De prima assignatione vide IX. de Trin.), [^23] (Vat. respondeo), [^24] (Cod. O addit suum) are present in the PDF footer column. Confidence: high for [^22]; medium for [^23] and [^24] since they were read at 700dpi. → 1200dpi verification optional.

## bon-sent-I-d8-p1-dubia (2026-05-10 rebuild)
- **[^7]**: OCR `Cod. T vermi, cod. W ibi pro hem.` — `hem` almost certainly garble for `bene` (last word of body before footnote anchor). Currently rendered `bene`. → Resolve via 600dpi PDF at p.163.
- **[^11]**: OCR `de loco in. Paulo infra i ...` — final `in` is truncated, probably `de loco in locum`. Currently rendered `de loco in [locum][?]`. → Resolve via 600dpi PDF at p.163.
