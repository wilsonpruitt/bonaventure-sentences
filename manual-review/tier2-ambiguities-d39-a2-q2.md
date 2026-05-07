# Tier-2 Ambiguities — d.39 a.2 q.2

## Resolved-with-flag

**bon-sent-I-d39-a2-q2, apparatus [^1] (Dionysius citation)**: OCR for the Greek word in the Dionysius quote (`ἑνικῶς` / *henikōs*) is partially legible at 600 dpi; the OCR `(ἑνικῶς)` is plausible but reading 'Senel' (OCR garble for 'Semel') is corrected silently to 'Semel'. The Greek transliteration `henikōs` (= "in a unitive manner") is the standard reading of De Div. Nom. c. 7 § 2; flagged `[?]` for verification against a Patristic edition.

## Notes on chunk boundary

- Frontmatter `printed_pages` was [676, 677, 678] — INCORRECT. Q.II runs pp. 693–695 (PDF pp. 283–285, since pt2 PDF offset = printed − 410). Verified from PDF running heads "DIST. XXXIX. ART. II. QUAEST. II" on p. 693 and "DIST. XXXIX. ART. II. QUAEST. III" on p. 695 (which contains end of Q.II + start of Q.III).
- OCR for QUAESTIO II header itself is missing/eaten in raw lines (page break between p.693-bot and p.694-top); reconstructed from PDF eyes-on at 600 dpi.
- Arg 1 ("Primo auctoritate Dionysii…") is on bottom-right of p. 693; arg 2 onwards begins at top of p. 694.
- Marginal gloss "Fundamenta." appears in the PDF margin next to arg 1 and is editorial decoration — not transcribed in the body per CLAUDE.md OCR-cleanup rules.
- `line_end` corrected from 27680 → 27613 (true Q.II/Q.III boundary; QUAESTIO III header at line 27615).
