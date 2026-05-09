# Tier-2 ambiguities — d.35, a.1, q.1 (*Utrum ponendae sint ideae in Deo*)

Logged 2026-05-07. OCR raw lines 18309–18857 of `raw/bonaventure_vol1_pt2_raw.txt`. Two-column page layout caused heavy OCR fragmentation, especially in the long scholion (sections I–VI).

## Body of q.1

- **bon-sent-I-d35-a1-q1, body fund. 1**: OCR `Quanlum ergo ad primnni quaeritur, ulruni sit / in Deo ponere ideas`. Standard reading restored from context: *Quantum ergo ad primum quaeritur, utrum sit in Deo ponere ideas.* No flag — silently corrected.
- **fund. 2 minor**: OCR `omne agens ratiombililiter, non a casu, vel ex necessitate, praecognoscit rem, antequam sit`. The Quaracchi apparatus n. 2 cites the more probable reading *ratiomibilissime* in some codices; we keep *rationabiliter* per Vat. text. Flagged in apparatus, not body.
- **fund. 3**: OCR garble `dncit / liajjet / simihtndinem / Angustinns` resolved silently to *ducit / habet / similitudinem / Augustinus*.
- **Contra 1**: OCR `singuhs se immittens` standard reading *singulis se immittens*; cf. Quaracchi n. 5 noting Vat. variant *innitens*.
- **Conclusio 1 marginal heading "Conclusio .2" / "Conclusio .1"**: in OCR these are marginal labels printed *in the margin* (`conciusio -2`, `coiiciusio .1`). They are editorial cross-reference labels for the two conclusiones (concl. 1 and concl. 2 of the Quaracchi reconstruction) — preserved as marginal italic notes in the body.
- **Resp., paragraph 4**: OCR `simulitudo expressiva ° et idea` — the `°` is footnote anchor 6 in the Quaracchi block (`Cod. Z expressissima`).
- **Resp., paragraph 5 "soiutio op posilorum"**: this is the marginal heading *Solutio oppositorum* introducing the replies; preserved.
- **ad 4**: OCR `et* Deus est ipsa regula` — `et*` flags a textual variant; per apparatus n. 2 (this page block), supply `quia` from cod. bb. Rendered `[*quia*] Deus est ipsa regula` with `[?]` retained inline.

## Scholion

The scholion (printed pages 602–605, sections I–VI) is dense and heavily column-broken. The following spots are flagged:

- **Schol. I, citation of Augustine 83 Quaest.**: OCR `Idcas igitur Latine possu-mus vel formas vel species dicere, ut \erbuni e verbo traiis-ferre videamui-` rendered *Ideas igitur Latine possumus vel formas vel species dicere, ut verbum e verbo transferre videamur*.
- **Schol. I, Uldaricus citation**: OCR `Uldaricus (apud Dionys. Carth., hic I. Sent. d. 36. q. i.)` — kept as in the Quaracchi text.
- **Schol. I, Greek**: OCR shows `[jiapi-BEiYiJ-a a napa3Eixvu[ii]` and `XoYoi appelliiiitor`. These are Greek transliterations: *παράδειγμα ἀπὸ παραδείκνυμι* and *λόγοι appellantur*. Restored as Greek where unambiguous; flagged with `[?]` where the OCR garble is total.
- **Schol. II, S. Bonaventura *Breviloquium* citation**: OCR `Sapienlia divina ct in quantum est ralio cognoscendi omnia cognita, dicitur liw` — *liw* clearly = *lux*; restored as *lux* with `[?]`. Quaracchi parallels confirm.
- **Schol. III.1 (Scotus opinion)**: OCR `cum qua fere conveniunt Durandus (I. Sent. d. 36. q. 3.) multique Nominales` resolved confidently.
- **Schol. III.3 (S. Bonaventura excerpts a–l)**: a long lettered series of textual citations from B.'s other works, mostly OCR-clean enough to restore. The stretches of lines 18705–18802 around Greek footnote markers and Italian/Latin block quotations are the most error-prone; multiple `[?]` flags placed where word-form is uncertain.
- **Schol. IV (concord with S. Thomas)**: OCR clean.
- **Schol. V (improbation of first opinion)**: OCR `inferendo effectum cx cuusa` → *causa*; clean.
- **Schol. VI (cross-references)**: a citation list of Alex. Hal., Scotus, B. Albert., Petr. a Tarantasia, Richard. a Med., Aegid. R., Henr. Gand., Durand., Dionys. Carth., Biel. Standard scholastic-bibliographical formula; restored from OCR.

## Apparatus (page-foot blocks)

The chunk has six page-foot apparatus blocks (one per printed page). Total restored entries: **12** numbered footnotes for the body+scholion. Where the OCR yields a partial reading and the citation is fixed (e.g. *Quaest. 46. n. 2*, *Libr. XI. de Civ. Dei. c. 29*), the entry is restored verbatim. Footnote markers (`²`, `³`, `'`, `''`, `^`) on individual words are mapped to the closest semantic anchor, per the workflow recipe.

No content suppressed. All `[?]` flags above carry into the chunk file.

## Wave 9b Tier A apparatus rebuild (2026-05-09)

**Trigger**: hardened-heuristic `audit-apparatus-count.py` flagged the chunk as `INCOMPLETE-SUSPECT` with raw=49, chunk=12, diff=+37. Status downgraded to `Phase C Tier 2 apparatus-incomplete` pending eyes-on rebuild.

**Method**: extracted printed pp. 600–605 from `raw/doctorisseraphic12bona.pdf` (PDF pages 190–195) at 600 dpi via `pdftoppm`. Inspected each page footer block by eye, page-by-page, per Lesson 9 ("Ground-truth is the printed page footer, not the audit script").

**Per-page footer count (PDF eyes-on, 600 dpi)**:

| printed page | footer entries | chunk markers |
|---|---|---|
| p. 600 | 6 | [^1]–[^6] (already present) |
| p. 601 | 6 | [^7]–[^12] (already present) |
| p. 602 | 3 | [^13]–[^15] (NEW this rebuild) |
| p. 603 | 0 | pure Scholion body — no footer block |
| p. 604 | 0 | pure Scholion body — no footer block |
| p. 605 | 0 | begins Q.II; that page's footers belong to the q.2 chunk |
| **total** | **15** | **15** |

**Heuristic noise**: audit reports raw=49, ground-truth=15, so ~34 false-positive openers. The Scholion (pp. 602–605) is unusually dense with italicized work-citations (`*Sent.* d. 36. q. 3.`, `*S.* p. I. q. 23. m. 4. a. 1.`, `*Hexaem.* Serm. 3.`, `*de Verit.* q. 3. a. 2.`, lettered series `a)`–`m)` in Bonaventure-excerpts block, numbered list items `1.`/`2.`/`3.` in §III, etc.); each can pattern-match against the footer-opener regex. Same false-positive class noted in CLAUDE.md Lesson 9 (heuristic "still not perfectly faithful (~10% noise either direction)" — d.35 a.1 q.1 is a 70%-noise outlier because of unusually heavy Scholion).

**Disposition: ACCEPT WITH REASON** — the +34 audit residual after rebuild is purely Scholion-citation false positives, not missing apparatus.

### New entries

- **[^13]** (p. 602 footer 1): textual variants on body §3-resp. — `Aliquot codd. ut A T V cum ed. 1 *praesenter*, alii ut X Z aa *praesens*. Voci *animam*, quae proxime sequitur, cod. R praefigit *ipsam*. Dein post *alia similitudo* cod. addit *causata a veritate*, et paulo inferius post *et eo* cod. X inserit *est*.` Anchor placed after *animam* in body Latin and English.
- **[^14]** (p. 602 footer 2): `Supple cum cod. *bb* *quia*.` Anchor placed after *et* in `et[^14] Deus est ipsa regula et idea` (body §4-resp.). This anchor was previously a wrong reuse of `[^8]` from p. 601's footer block — fixed in this rebuild.
- **[^15]** (p. 602 footer 3): `Vat. praeter fidem codd. et ed. I hic interponit *defectus et*.` Anchor placed after *non ponit* in `idea in Deo non ponit[^15] imperfectionem`.

### Body-paraphrase guard

Spot-check of body Latin (raw lines 18322–18534) against rebuilt chunk: clean. No paraphrase clusters. OCR-cleanup (`siniilitudo`→`similitudo`, `praesenlialiter`→`praesentialiter`, `simulitudo`→`similitudo`, `cnnvertentis`→`convertentis`, etc.) is mechanical letter-substitution, not rewriting. Status string accordingly uses `Phase C Tier 2 complete`, not the `apparatus-rebuilt-body-paraphrased` variant.

### `[?]` flag count post-rebuild

Body + Scholion: **0** `[?]` flags currently in chunk. Prior pass (2026-05-07) noted "scholion from OCR with [?] flags on ambiguous spots" — those were resolved in that pass; this rebuild touched only the apparatus block and the two body anchor positions on p. 602, so no new `[?]` flags were introduced. The three new apparatus entries [^13]–[^15] read cleanly off the 600 dpi PDF crop.

### Anchor counts (post-rebuild)

- Latin body markers: 15 (one each for [^1]–[^15])
- English body markers: 15 (mirrored)
- Apparatus definitions: 15 (one each)
- Once-per-file blockquote note: present (line 38 of chunk file)

