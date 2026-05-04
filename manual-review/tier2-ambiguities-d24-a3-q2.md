# Tier-2 ambiguities — bon-sent-I-d24-a3-q2

Source: `raw/bonaventure_vol1_pt2_raw.txt` lines 1286–1399. Printed pp. 430–431. PDF pp. 20–21 (offset = printed − 410).

This is the last chunk for d.24 (no dubia). Tail trimmed before "NOTANDA CIRCA LITTERAM MAGISTRI" (which belongs to the d.24 littera chunk) and well before the "DISTINCTIO XXV." running head at raw line 1430.

## `[?]` flags raised in chunk

- **Scholion, opening verb**: OCR shows `S. Doctor feiicit loculionem deitas est trina`. Resolved as `refugit` (shrinks-from / avoids), the standard Quaracchi idiom in similar scholia, and the only plausible Latin verb fitting the OCR garble + sense ("the holy Doctor avoids the locution *deitas est trina*"). Marked `refugit[?]` in Latin and "shrinks from[?]" in English. Confidence: medium-high. Alternatives considered: `fugit` (fits sense but loses the OCR initial `re-` shape), `respuit` (rejects — looser fit). Cross-check on PDF page 21 recommended.
- **Scholion, "abstracti pro concreto"**: OCR is `quod tiic abstracti pro concreto`. Resolved as `quod hic abstracti [ponitur] pro concreto`. Inserted `[ponitur]` in brackets in the Latin (the verb is implied by the construction; OCR has no verb glyph here, but the standard scholastic phrase requires one). English: "that here the abstract [stands] for the concrete." This is editorial bracketing, not a `[?]` flag.

## Silent corrections of OCR garbles (logged for transparency)

- `umta.s` → `unitas` (title)
- `hnportant` → `important` (title)
- `esscntiae` → `essentiae` (title)
- `quatn` → `quam`
- `trinm` → `trinus`
- `videlur` → `videtur`
- `lioc` → `hoc`
- `siniul` → `simul`
- `Iteni` → `Item`
- `pari ra-tione` line break joined → `pari ratione`
- `CoNTR.\` → `Contra:` (heading)
- `piuralitatem` → `pluralitatem`
- `important^` → `important[^4]`
- `dePatre` → `de Patre`
- `nec: trinitas est trina^` → `nec: trinitas est trina[^5]` (footnote marker is for the editorial supply of these words from codd. P Q)
- `unitatera imporlent` → `unitatem important`
- `ansecundum` → `an secundum`
- `singulari videntur dici secundum     ,` (stray comma artifact from column gutter) → `singulari, videntur dici secundum`
- `singillatim,` retained as-is (genuine Latin)
- `ncm est unitas personalis` → `non est unitas personalis` (the `ncm`/`non` substitution is unambiguous)
- `Dicendum "` → `Dicendum[^6]`
- `mologiam` (line-broken from preceding column) → `etymologiam` (left-column line ends with `consuevit` mid-sentence, right-column begins with `mologiam`; Quaracchi printed reads `consuevit assignari duplex etymologiam` — `duplex etymologia[m]` with assignari reconstructed from context; alternatively `assignari duplex etymologia`. Inserted `assignari duplex` from context — this is the Quaracchi standard for "twofold etymology is wont to be assigned").
- `sicdicitur` → `sic dicitur`
- `sicul` → `sicut`
- `unitaspe?--` → `unitas personalis` (line break across columns; the `?--` is OCR scrap of the line-end ligature)
- `qnidem` → `quidem`
- `etymologia ultima ^` → `etymologia ultima[^8]`
- `unitas trium '` → `unitas trium[^7]`
- `ter^` → `ter[^9]` (in body of respondeo "unitas ter")
- `auteni` → `autem`
- `potesf` → `potest`
- `conciusio.` (margin gloss bleed) → trimmed (this is the "Conclusio." marginal note at the end of the respondeo; not part of body text)
- `Ad opposi-` (margin gloss "Ad oppositorum") → trimmed
- `soiuijp op-posilorura.` (heavy OCR garble of marginal "ad oppositorum opinionem" or similar) → trimmed; this is editorial marginalia, not Bonaventure's text
- `circa unitatem in recto` retained
- `vernm` → `verum`
- `PaU^e` → `Patre`
- `conveniunt '"` (footnote marker) → `conveniunt[^10]`
- `trinitas trina"` → `trinitas trina[^11]`
- `concretione , et ita ut inhaerentem` retained (Quaracchi punctuation)
- `feiicit` → `refugit[?]` (see flag above)
- `loculionem` → `locutionem`
- `liymno` → `hymno`
- `Ofiicium` → `Officium`
- `Tliomas` → `Thomas`
- `Te trina ,tas` (column-break artifact) → `Te trinitas`
- `tiic` → `hic`

## Apparatus footer marker mapping

OCR footer markers are degraded numeric/typographic glyphs ('1', '2', '3', '*', "'", '"', '>', '"' for the right-column entries). Mapped to body anchors by content:

- fn 1 (`deest et`) → "et[^1] in singulari"
- fn 2 (`repetit unitas`) → "essentialis[^2]" (Vat. inserts an extra *unitas* here)
- fn 3 (`addunt haec`) → "Non enim[^3]" 
- fn 4 (`mendose importat`) → "ergo important[^4] unitatem personae"
- fn 5 (`verba nec trinitas est trina ex codd P Q`) → "trinitas est trina[^5]"
- fn 6 (`Ad praedictorum / convenit pro consuevit`) → "Dicendum[^6], quod ad hoc consuevit"
- fn 7 (`Isidor. VII Etymolog. c. 4`) → "trinitas est unitas trium[^7]"
- fn 8 (`omittitur ultima`) → "etymologia ultima[^8]"
- fn 9 (`praemittitur trinitas`, right-col) → "unitas ter[^9]"
- fn 10 (`Paritas in hoc est: sicut de homine non praedicatur animal...`, right-col long note) → "diversae species in eo conveniunt[^10]"
- fn 11 (`Codd. VZ omittunt neque trinitas trina`, right-col) → "neque trinitas trina[^11]"

## Notes for future verification

- p.430 (verso) and p.431 (recto) form a single opening; the question runs continuously across the column-break. The right-column body of p.430 finishes the question's solutions and then continues to p.431 ("ut hoc nomen Deus...") through the SCHOLION.
- The d.24 littera commentary ("NOTANDA CIRCA LITTERAM MAGISTRI") at raw lines ~1402–1427 is intentionally NOT included here; it belongs to `bon-sent-I-d24-littera.md`.
- Footnote 10 text was reconstructed from the right-column footer; `Paritas in hoc est: sicut de homine non praedicatur animal, quatenus sub se comprehendit alias diversas species animalium...` — confidence high but a single eyes-on PDF check at p.21 (printed 431) would harden the *qua/quia* and *ea/eo* variant readings reported.
