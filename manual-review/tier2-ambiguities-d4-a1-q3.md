# Tier-2 ambiguities — d.4 a.un. q.3

## 2026-05-12 rebuild — p.102 Q.III footer added; mis-anchored [^7]/[^8] removed

### Investigation of prior [^7] (Vat. hic *subiectum* loco *substantivum*) and [^8] (Cod. R addit *genuit*)

Both prior entries were traced to the raw p.101 footer block in `raw/bonaventure_vol1_raw.txt`:
- **`Cod. R addit genuit.`** at raw line 24283 — this is the FIRST entry of the p.101 footer block (OCR marker `•` = printed numeral 1).
- **`Vat. hic subiecium loco substantimm...`** at raw line 24291 — this is the THIRD entry of the p.101 footer block (OCR marker `3`).

Neither anchors into the Q.III body. The 9 entries of the p.101 footer block split as:
- entries 1–3 (`Cod. R addit genuit`, `Exemplum...Aristot II. Periherm c.2 citharoedus`, `Vat. hic subiectum`) → anchor into the Q.II body that occupies the upper portion of p.101 (Q.II ended on p.101 before Q.III began); these belong to chunk `bon-sent-I-d4-a1-q2`, not q3.
- entries 4–9 (Periherm c.1, Periherm c.2 Catonis/Boethius, Cod S omnium, S. Doctor phoenix, Cfr. Priscian II.5, Postulantibus proprie) → anchor into Q.III body anchors 1–6 (Philosophum¹, Philosophus², principium³, suppositum⁴, Ioannes⁵, proprie⁶). These are the current `[^1]`–`[^6]` (unchanged).

**Disposition**: Prior `[^7]` and `[^8]` REMOVED from this chunk. They should be added to `bon-sent-I-d4-a1-q2` if not already present. The `octavo[^7]` anchor and `Posset[^8]` anchor in the Q.III response were mis-placed by the 2026-05-10 rechunk pipeline.

### New p.102 Q.III footer entries — apparatus rebuilt to 10 entries

Raw p.102 footer block (after Q.III ends and Q.IV begins, at raw lines ~24443-24465) has 6 entries; entries 1-2 (`Vers. 8`, `Vat. praeter fidem mss... nomen Dei`) anchor into Q.IV body (Ps 66:8 reference; nomen Dei in Q.IV body) and belong to `bon-sent-I-d4-a1-q4`. Entries 3-6 anchor into Q.III response on p.102 and were added here as new `[^7]`-`[^10]`:

- `[^7]` (sequuntur) — anchored at `sequuntur` in reply ad 1, raw line 24352.
- `[^8]` (Priscian XVII. Grammat / accidentium) — anchored at `discohaerentia accidentium` in reply ad 2 (the body word the Priscian variant `adiacentium/accidentium` applies to), raw line 24360.
- `[^9]` (Vat. potest + ex intellectu / intellectum) — anchored at `Posset` in reply ad 2 (the variant reading is *potest* for *Posset*), raw line ~24385. Previously was `[^8]`.
- `[^10]` (Supplevimus cum) — anchored at `cum` in reply ad 3-4 (`ut cum dicitur: principium creaturarum`), where editors supplied *cum* from manuscripts.

### Remaining [?] flags

1. **Line 55 / 93** — `sic nec hoc[?] nomen Deus` / `so neither does this[?] name God`. OCR shows `hoc''` (two apostrophe-like glyphs); these may be a printer's footnote marker or simply OCR artifact / stray quotation. No corresponding raw p.102 footer entry tracks this position (the 4 Q.III p.102 footer entries are all accounted for by other anchors). Treated as no-anchor; flag kept for 600dpi PDF eyes-on confirmation.

2. **Line 123 / 125** — `Cfr. Priscian., II. Grammat. c. 5.[?]` / `Cf. Priscian, Grammar II, c. 5.[?]`. OCR rendered c. number garble as `S` (= 5); reading confirmed but flag kept pending PDF verify.

3. Pre-existing `[^7]/[^8]` content (now removed) — see above.
