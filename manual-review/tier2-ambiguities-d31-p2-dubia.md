# Tier-2 ambiguities — `bon-sent-I-d31-p2-dubia`

Originally logged 2026-05-06 during Tier-2 promotion (8-entry apparatus). Superseded 2026-05-09 during Wave 9b Tier A apparatus rebuild (8 → 25 entries).

## Body-anchor positions ([?] flags)

The four `[?]` flags now embedded in the chunk are all on body-anchor uncertainty for new apparatus entries; none flag content of the apparatus Latin/English itself.

1. **DUB IV, body marker [^6] (Vide supra d. 11 a. 2. q. 1, et d. 18[?] p. II. q. 1)**: OCR raw line 13402 reads `Vide supra d. \L  a. 2. q. 1, et d. IS. p. II. q. I.` — `\L` and `IS` are OCR garbles for Roman numerals. Best reading is `XI` (= 11) for the first and `XVIII` (= 18) for the second, but PDF spot-check not done. Currently rendered as 11 and 18 with `[?]`. → Resolve by 600-dpi PDF check of p. 550 footer fn 4.

2. **DUB IV, body marker [^8] (Cod. T cum nonnullis aliis adiicit *est*)**: anchor position uncertain. Footer says Cod. T adds `est` somewhere in the second-account passage. Body has multiple candidates: `talis est`, `imago est`, `frequenter imago non aequatur ei cuius est`. Currently anchored on `talis est` / `as such` — best fit because Quaracchi listed this fn between fn 7 (`qui est`) and fn 9 (`indistincta`/`indiscreta`), which brackets the start of the second account. → Resolve by 600-dpi PDF check of p. 550 body marker between fns 6 and 7 (per-page numbering).

3. **DUB IV, body marker [^14] ("Cod. T (in marg.) addit *in*"; placed at "ideo prima")**: OCR raw line 13454 shows `ideo^ prima dicitur similitudo` — the `^` is the marker. The footer says Cod. T adds *in* near here. The English mirrors at "therefore the first[^14] is called". Position is plausible but not pdf-verified. → Resolve by 600-dpi PDF check of p. 551.

4. **DUB VIII, body marker [^25] ("Complures codd. ... *quin*"; placed at "non quia")**: page-552 footer 5 records a *quin* variant. The body has `non quia utrumque non sit verum` (in `**Respondeo**` of DUB VIII reply); `non quin` is a Latin idiom and the most plausible site for the variant. Alternative candidate: `quia videtur haec confessio fidei` (DUB VIII opening). Currently anchored on `non quia` / `not because`. → Resolve by 600-dpi PDF check of p. 552 footer fn 5 (or post-substantiam-footer entry).

## Apparatus content (no [?] embedded in Latin/English text proper)

The 25 footer entries themselves are OCR-clean enough (after silently correcting common garbles: `iddit` → `addit`, `defmitur` → `definitur`, `incongnie` → `incongrue`, `cmcordibus` → `concordibus`) that no `[?]` appears within the rendered Latin or English of any apparatus entry.

The four prior-log [?] flags (perfectam, attribuit, quod, elidere) were body-text uncertainties about marker positions; they are now resolved by the 25-entry apparatus rebuild — `attribuit` now carries the rendered cross-ref [^15]; `elidere`/`elidebat` is covered by [^23]; `expressam` MS variant is now its own entry [^12]; the unmarked `quod` after `Dicendum,` was a residual OCR mark-up artifact and carries no Quaracchi footer in the per-page footer block, so the [?] is dropped (the body now carries no marker at that position).

## Page-counting note

The hardened audit-apparatus-count heuristic returned 38 for raw lines 13273–13569, but eyes-on walk yields 25 dubia-relevant footers:

- **p. 549**: 2 entries (fns 8, 9 of the page-549 footer block; the earlier 7 footers belong to the prior d.30 a3-q3 chunk which spans the page-548–549 break)
- **p. 550**: 10 entries (full per-page sequence 1–10)
- **p. 551**: 8 entries (full per-page sequence 1–8)
- **p. 552**: 5 entries (fns 1–5 of the dubia portion; fns labelled 1–2 in the right-hand column of p. 552 belong to the d.32 chunk that begins on this page)

The heuristic overcount (~13) is consistent with Lesson 9's stated ~10% noise margin extended by the cross-distinction page sharing on pp. 549 and 552.
