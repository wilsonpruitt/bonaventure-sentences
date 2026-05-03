# Tier-2 ambiguities — bon-sent-I-d22-a1-q2

Promoted to Tier 2 on 2026-05-03. No `[?]` flags inline in the chunk. Notes on editorial decisions:

- **Marginal labels stripped from body.** The OCR shows several Quaracchi marginal/sidehead labels bleeding into the column (e.g. *"Tria sunt in nomine"*, *"conclusio j."*, *"conclusio 2. bimembris"*, *"Conclusio 3."*, *"Conclusio 4."*, *"Deus innotescit nobis tripliciter via"*, *"Solutio oppositorum"*, *"Ad 4. opposit."*, *"Ad 1. opposit."*, *"Ad 3, primum"*, *"Ad 2"*, *"Ad 3, secundum"*). Per `feedback_corpus-editorial-cleanup.md` these are stripped from the body, since they are editorial apparatus, not Bonaventure's text. The Scholion II preserves the editorial mapping for any reader who wants to chase the marginalia.

- **Solution numbering.** Bonaventure's solutions in the source body are ordered: *Ad 4* (singulariter), *Ad 1* (unitas a parte rei → continues onto p.394), *Ad 2* (synonyma), *Ad 3* (a parte intelligendi). I preserved this exact order and numbering — see Scholion II, which explicitly notes that "in solutione oppositorum ordo argumentorum mutatus est."

- **Footnote [^15] anchor.** The OCR garbles `quod''` (with a stray quote) at "et sic dicendum, quod^ quodam modo nomen unum"; placed `[^15]` immediately after *quod* to match Quaracchi's variant note (Vat. omits *quod*).

- **Footnote [^24] (multi-target).** The p.394 footer block in the OCR holds five short notes (`1 Supple: est…`, `* Ex plurimis mss. … nomina`, `5 Nempe p.I.q.1`, `* Cod. T una veritas`, `5 Ed. 1 adiungit sed veritas et unitas`). These cover five inline markers in Bonaventure's text on p.394 (`tamen`, `nomina synonyma`, `problemate`, `vera unitas`, `vanitas`). To keep the apparatus block compact and to match the Quaracchi convention of consolidating short successive notes, I merged them into a single trailing footnote `[^24]` anchored at *tamen*. Each sub-clause is set off by an em-dash inside that note. If a future pass prefers five separate footnotes, splitting is mechanical.

- **Page 392 footnote 5 (Ambrosius).** OCR `Id est, II. de Fide ad Gratianum, in Prologo` is the standard Quaracchi pointer to Ambrose's *De Fide ad Gratianum* II, Prologue (cited by Bonaventure as *de Trinitate* — the title both works circulated under in the 13th century). Rendered as such; not flagged.

- **Page 393 footnote 19 (Dionysius).** OCR garble `Noni.` silently fixed to *Nom.*; `pag. 77 nota 10` retained as Quaracchi cross-reference.

- **No `[?]` flags remain.** All silent OCR fixes are routine letter-substitution corrections (`utruni→utrum`, `nonwn→nomen`, `Aitctoritate→Auctoritate`, `appeliat→appellat`, `magnura→magnum`, `Hbro→libro`, `nuUum→nullum`, `nuilum→nullum`, `oranis→omnis`, `mlellectuum→intellectuum`, `intellectmm→intellectuum`, `huius-modi→huiusmodi`, `iustitiam→iustitiam`, `confiteri→confiteri`, etc.). None are semantically ambiguous.
