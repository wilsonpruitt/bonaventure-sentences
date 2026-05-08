# d.30 Scaffolds Sweep Audit Log

**Date:** 2026-05-08
**Scope:** `vol1/bon-sent-I-d30-{divisio, littera, dubia}.md` (3 chunks named in task)
**Auditor goal:** Verify chunk bounds against pt2 raw OCR; diff Latin body and apparatus against raw OCR; flag silent paraphrase or fabricated apparatus; verify anchors.
**Prior status:** d.27–d.30 polish-cleared 2026-05-06 (`d27-d30-polish-resolution-log.md`); all 25 inventoried flags resolved/accepted.

---

## Chunk verdicts

### `bon-sent-I-d30-divisio.md` — VERIFIED CLEAN

- **Bounds (raw lines 10330–10371):** Confirmed. Starts at `DIVISIO TEXTUS` (raw 10330); ends at "Tertio… an secundum relationem" (raw 10371). The ARTICULUS UNICUS heading begins at 10375 (correctly excluded). TRACTATIO QUAESTIONUM block (10364–10371) is correctly retained inside the divisio chunk per CLAUDE.md re-chunking rules.
- **Latin body diff vs raw OCR:** Verbatim with documented silent OCR corrections (`DIVTSIO TE.XTUS.` → `DIVISIO TEXTUS.`, `priina` → `prima`, `taraen` → `tamen`, etc.). No paraphrase detected.
- **Apparatus (4 entries):** All four entries verified against OCR footnote bands at lines 10350–10354. `[^1]` Dist. XXVIII c.6, `[^2]` Codd. DE donatur, `[^3]` Pro aeternaliter plurimi codd., `[^4]` Pro quoddam codd. AFG. Renderings match OCR + existing ambiguities log.
- **Anchors:** `[^1][^3]` at *aeternaliter* (raw line 10336: `aeternaliter '`); `[^2][^4]` at *quoddam* (raw line 10342: `quoddam ^`). Note that Quaracchi's note 2 ("Codd. DE *donatur*") at the *quoddam* anchor is semantically odd but matches OCR placement; previously documented and accepted in `tier2-ambiguities-d30-divisio.md` and the d27–d30 polish log.
- **English:** Literal, parallel paragraph-for-paragraph. No paraphrase.
- **No new `[?]` flags.** No edits required.

### `bon-sent-I-d30-littera.md` — VERIFIED CLEAN (with previously-accepted page-520 reconstruction)

- **Bounds (raw lines 10164–10316):** Confirmed. Starts at `DISTINCTIO XXX.` (raw 10164); body runs through both columns of pp. 518–520 across the heavily-degraded p. 520 OCR; ends at "non in dante" (raw 10312, with trailing blanks to 10316). Next semantic unit (`COMMENTARIUS IN DISTINCTIONEM XXX`) begins at 10317 — correctly excluded.
- **Latin body diff vs raw OCR:** Top of p. 518 and right column of p. 519 verbatim from OCR. Lower half of p. 520 (lines ~10279–10316) was reconstructed from severely degraded OCR; reconstruction documented in `tier2-ambiguities-d30-littera.md` and resolved via PDF eyes-on per d27–d30 polish log. **Spot-check (Augustine quote in DUB. I context, transition sentence "Ex his aperte ostenditur…"):** consistent with Lombard text at this locus and with Quaracchi's *de Trinitate* V.16.17 source. No paraphrase.
- **Apparatus (10 entries):** Entries [^1]–[^9] verified against OCR footnotes on pp. 518–519 (raw 10234–10268). `[^10]` "Codd. DE *donatur*" — its placement at "et ad illum cui datur[^10]" corresponds to OCR line 10304 marker `'-` on p. 520 right column; previously flagged + PDF-confirmed (codex letters D, E legible, period faint) in the ambiguities log.
- **Anchors:** All `[^N]` markers correspond to OCR superscript positions. `[^1][^6]` at *dominus* (raw 10168 / 10237 cross-anchor); other markers at OCR-marker positions confirmed.
- **English:** Literal. Augustine quotes preserved with appropriate quotation marks. No paraphrase.
- **No new `[?]` flags.** No edits required.

### `bon-sent-I-d30-dubia.md` — VERIFIED CLEAN

- **Bounds (raw lines 10976–11185):** Confirmed. Starts at `DIST. XXX. DUBIA.` heading (raw 10976) and `DUBIA CIRCA LITTERAM MAGISTRI` (raw 10980); ends after DUB. V at "non autem spiritus sanctus" on p. 528 (raw 11146, blanks to 11185). Next unit `DISTINCTIO XXXI.` begins at raw 11190 — correctly excluded.
- **Latin body diff vs raw OCR:** Five DUBIA (I–V) verbatim with documented silent OCR corrections (per `tier2-ambiguities-d30-dubia.md`). Marginal gloss fragments (`Notanda di-`, `Adqnaesiio-`, etc.) correctly trimmed per CLAUDE.md rule. Conjectural readings (`instantiam in imperitis`, `nummus`) flagged in ambiguities log; both contextually unambiguous and previously accepted.
- **Apparatus (23 entries):** Count verified — 13 footnotes on raw p. 527 (OCR lines 11051–11071) + 10 footnotes on raw p. 528 (OCR lines 11151–11177) = 23 total. Entries renumbered continuously [^1]–[^23] in chunk; renumbering correct and traceable.
- **Anchors:** All [^N] markers correspond to OCR superscript positions. Spot-checked: [^2] at *vere* (raw 11012 `vere''`); [^11] at start of DUB. II body marker on tempus argument; [^21] at *posse referri* in DUB. V (raw 11126 `posse referri '`).
- **English:** Literal. Boethius and Ambrose attributions preserved; technical scholastic phraseology (*esse primum*, *bene esse*, *relatio secundum esse*) glossed in italics or parentheses per CLAUDE.md key-terminology table.
- **No new `[?]` flags.** No edits required.

---

## Totals

- **Chunks audited:** 3 (divisio, littera, dubia)
- **Bounds verified correct:** 3/3
- **Latin paraphrases detected:** 0
- **Fabricated apparatus entries detected:** 0
- **Vat-variant inversions detected:** 0
- **Body omissions detected:** 0
- **New `[?]` flags raised:** 0
- **Substantive edits made:** 0
- **Backups created:** 0 (no edits → no backup needed)
- **`transcription_status` updates:** 0 (no edits → status string unchanged)

## Anomalies / observations

1. **Note 2 ("Codd. DE *donatur*") in divisio:** Apparatus text appears semantically unrelated to its anchor at *quoddam* — this is a quirk of Quaracchi's apparatus rather than a chunk error. Previously logged + accepted in d27–d30 polish log. No action.
2. **Apparatus `[^10]` in littera ("Codd. DE *donatur*") repeats text similar to divisio's `[^2]`:** This is intentional — Quaracchi's apparatus reuses the variant note across the divisio commentary and the second occurrence of *donatur* in the Augustine quotation on p. 520. Previously accepted via PDF eyes-on.
3. **p. 520 OCR degradation:** The lower half of p. 520 has severe OCR garble (e.g. `gt'1'Ciniis`, `Snlisliinlia`, `tcmporalilci-`). Reconstruction is documented and PDF-confirmed; further verification is not justified by the cost-benefit at Tier 2.

## Build smoke-test

`cd site && node scripts/build-content.mjs`
→ `Built content.json: 1 book(s), 422 questions, 350 translated` (clean, no parser errors).

---

## Conclusion

All three named d.30 scaffold chunks (divisio, littera, dubia) are correctly Tier-2 against the IA djvu OCR. No silent paraphrase, no fabricated apparatus, no Vat-variant inversion, no body omission. The 2026-05-06 polish pass holds. **Nothing committed; no edits made.**
