# Tier-2 ambiguities — bon-sent-I-d1-a1-q2

Rebuild date: 2026-05-07. Raw OCR lines 13675–13961 in `raw/bonaventure_vol1_raw.txt`.

No `[?]` flags inline in the chunk: all OCR garbles in this chunk are silently recoverable from context per the standard OCR-cleanup rules. Items below are logged for transparency.

## Silent OCR corrections

| OCR | Restored | Basis |
|---|---|---|
| `QLI.ESTIO IL` | `Quaestio II.` | Standard heading garble (cf. d.1 a.1 q.1) |
| `Ulrum` | `Utrum` | Standard `U/Ul` glyph confusion |
| `nti` | `uti` | Standard `n/u` confusion in lower-case |
| `utrbiii` | `utibili` | Cluster garble of *utibili*; context confirms (printed title is *de utibili*) |
| `Universa` (heading wrap) + `Faninmmu.propter semetipsu77i` | `«Universa propter semetipsum operatus est Deus»` | `Faninmmu.` is marginal-gloss bleed (*Fundamenta* margin); `semetipsu77i` is OCR digit-substitution for `m`. Vulgate Pr 16:4 confirms wording. |
| `Denm` | `Deum` | Standard `n/u` confusion |
| `diiigendum`, `propler`, `oninis`, `defmitione`, `crsato`, `mentiri`, `lioc` (apparatus), `flde` | `diligendum`, `propter`, `omnis`, `definitione`, `creato`, [unchanged], `hoc`, `fide` | Routine OCR letter substitutions |
| `Vulgala`, `coniingit`, `iit`, `aiitiqua`, `Tliomae`, `aliqnis uii- tur`, `uii-` (footnote 8), `od. 1`, `suppeditjmt`, `conftTOY`, `con(m jS`, `valitudinem`, `mendum`, `castigavimus` | `Vulgata`, `contingit`, `ut`, `antiqua`, `Thomae`, `aliquis utitur`, `utitur`, `ed. 1`, `suppeditant`, `convenit`, `contingit`, `valitudinem` (kept — Quaracchi spelling), `mendum`, `castigavimus` | Routine apparatus OCR fixes |
| `Qualenus` (apparatus 9) | `Quatenus` | `t/l` glyph swap |
| `Elhio.` (apparatus 9) | `Ethic.` | OCR `c→o`, then `Eth` style |
| `depotcntiis, quaenon` | `de potentiis, quae non` | OCR word-merging + `e→c` |
| `recto per modum` (apparatus 17) | *recto per modum* | Preserved verbatim — apparatus is reporting an emended Vatican reading; phrase is referential, not authorial. |

## Marginal-gloss bleed-throughs stripped

The OCR mid-paragraph contains the following marginal-gloss fragments that are editorial side-notes, not Bonaventure's text. All stripped:

- `Faninmmu.` (= *Fundamenta*) — opens fund. 1
- `Ad opposi-/"""■ cumque` (= *Ad opposita*) — opens contra section
- `Q"'?'»»"-./^modi utenc/^""i^J;,^™` (= *Quaestionis solutio* and *Quatuor modi utendi*) — opens *respondeo*
- `Aliadistin-modum u-` (= *Alia distinctio modum utendi*)
- `Diversiino-/deutimurtjo-/nisetmaiis.` (= *Diverso modo utimur bonis et malis*)
- `Soiutioop-/positorum.` (= *Solutio oppositorum*) — opens *ad 1*

## Apparatus numbering decision

Quaracchi prints footnote numbering per-page (p. 32: 1–10; p. 33: 1–7 = 17 entries). Renumbered sequentially 1–17 across the chunk for chunk-internal consistency, matching the convention used in `bon-sent-I-d1-a1-q1.md` and other Tier-2 chunks. Page boundary noted in the apparatus blockquote header.

## Structural anomalies discovered (relative to pre-rebuild chunk)

1. **Conclusio reading.** Pre-rebuild Latin had `Non omni ex creato possumus uti ut instrumento, neque ut habitu, neque ut actu medio; omnibus tamen ex iis possumus uti ut obiecto, quod approbandum vel respuendum est, vel approbando, vel acceptando, vel tolerando, vel respuendo.` OCR shows `Non omni re creata possumus uti ut instrumento neque ut habitu neque ut actu, omni tamen re uti possumus ut obiecto, sed quadrupliciter, vel operando, vel acceptando, vel tolerando, vel respuendo.` — *re creata* (not *ex creato*), no *medio* on *actu*, *operando* (not *approbando*), and the final *quadrupliciter* clause is OCR-form. Restored to OCR reading.

2. **Pre-rebuild apparatus had only 8 entries, several wrong.** Entry [^3] in pre-rebuild was *Categories De oppositis* (matches OCR fn 4 of p.32, not 3); entry [^5] (`Ibid., c. 3, n. 3, ubi habetur: Res quaedam sunt quibus fruendum est…`) does not match any OCR apparatus entry — it appears fabricated or imported from a different question. Entry [^8] (`Codd. B et edd. antiquiores addunt vel utentis, quod a Vat. omittitur`) likewise does not appear in the OCR apparatus for Q.II. Both rebuilt from raw OCR.

3. **Fundamentum 1 phrasing.** Pre-rebuild had `omnia ordinabilia sunt in Deum…recte utimur eo: ergo omni creato contingit uti; ergo omnibus est utendum`. OCR shows `omnia sunt ordinabilia in Deum… recte utimur: ergo si omnia contingit ordinare, omnibus est utendum`. Restored.

4. **Fundamentum 2 phrasing.** Pre-rebuild compressed the arg ("ens et bonum convertuntur; sed omne bonum creatum est diligendum; sed ex diligendo est uti…"). OCR has the full Dionysius citation and a fuller chain (`omnia sunt entia: ergo omnia sunt bona. Sed omne bonum diligendum…sed non est diligendum propter se: ergo propter aliud; sed hoc est uti`). Restored.

5. **Fundamentum 3 phrasing.** Pre-rebuild paraphrased; OCR shows the standard `omni virtute contingit recte uti: ergo opus omnis virtutis est rectus usus…` form. Restored.

6. **Contra 1 phrasing.** OCR includes `quia omnia ordinantur in finem per caritatem quaecumque recte ordinantur` and the closing `cum non sit uti recte nisi per caritatem` — both dropped from pre-rebuild. Restored.

7. **Contra 4 phrasing.** Pre-rebuild had a substantively different argument (about always misusing evil). OCR shows: `virtute non contingit male uti, sicut patet ex eius definitione: ergo ab oppositis malo culpae sive vitiis non contingit recte uti: ergo non omnibus aliis a Deo est utendum.` Restored.

8. **Heading style.** Pre-rebuild used `**QUAESTIO II.**` bold caps on its own line. Switched to standard chunk h3 form `### Quaestio II. *Utrum…*` per the format used in `bon-sent-I-d1-a1-q1.md`.

9. **Conclusio rendering.** Promoted to `>` blockquote with `**Conclusio.**` bolded, per Tier-2 standard.

10. **`Ad 3-4` heading.** Pre-rebuild had `**Ad 3–4.**`; OCR has `3. 4.` separate numerals introducing the joint reply. Rendered as `**Ad 3, 4.**`.
