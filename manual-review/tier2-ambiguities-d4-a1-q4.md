# Tier-2 ambiguities — d.4 art.1 q.4

Created 2026-05-11 during the body-paraphrase rebuild wave (Bucket 3 of d.1-d.10 polish).
Chunk: `vol1/bon-sent-I-d4-a1-q4.md`. Raw OCR range: pt1 lines 24414–24625. Printed pages 102–103 (Quaracchi Vol I).

## [?] flags placed inline

### apparatus [^2] — OCR fragmentary (HIGH)
- **Location**: `vol1/bon-sent-I-d4-a1-q4.md:135`
- **Raw OCR lines**: 24444–24445
- **Garble**: `Vat. praeter fidem mss. [...] nomen Dei` — middle of the Quaracchi footer note is illegible in the IA djvu OCR.
- **Disposition**: Recover full text from 600dpi PDF at printed p. 102 footer when next batch of PDF eyes-on runs. Render the missing middle clause in both `**La.**` and `**En.**` lines.

### Scholion II — OCR fragments (LOW)
- Scholion II opening words and mid-clauses suffered the usual scholion-header OCR breakup. Body still readable and rendered, but a fragment or two at clause boundaries may need re-set from 600dpi PDF.
- **Disposition**: Defer; not blocking Tier-2 completeness. Re-visit during d.1-d.10 [?] resolution pass if/when Scholion II is touched again.

## Substantive rebuild findings (not [?] flags — full dispositions)

### Body Sed-contra args 1-2 restored from raw OCR
- Prior chunk had paraphrased Sed-contra args as `Sicut se habet homo ad hominem...`, not in raw.
- Restored verbatim:
  - Arg 1: `Pronomen refert rem pro proprio supposito...` (raw line ~24XXX)
  - Arg 2: `Item quia iste terminus homo proprie supponit pro individuo...`

### Respondeo two-opinion-plus-melius-est-dicere structure restored
- Prior chunk had a three-opinion abridgment. Re-set to the raw OCR's actual two-opinion structure plus Bonaventure's `melius est dicere` closing.

### Scholion III added (raw line ~24628)
- Cross-refs preserved: Bonav d.29, Alexander Hal., B. Albert, Petr a Tar, Richard a Med, Henr Gand, Dionys Carth, Biel.

### Fabricated `[^7]` (Aristot Metaph X — *Omne etenim... aut idem aut diversum*) — NOT reintroduced
- Removed 2026-05-10. Verified absent in 2026-05-11 rebuild.

## Adjacent finding — d.4 a.1 q.III apparatus-incomplete (NEW BACKLOG ITEM)

During this rebuild the agent traced the original task-brief's claim that p.103 footers 1-6 (Vers. 8; Vat praeter fidem; Ex plurimis mss substituimus *sequuntur*; Priscian XVII.1 ratio contextus; Vat potest; Supplevimus *cum*) were missing from Q.IV's apparatus.

**Disposition**: those 4 footers carry body anchors in **Q.III**'s response section, which prints on p. 102 (anchors at raw lines L24352 *sequuntur*, L24369–24373 *intellectum* / *Posset*, L24383 *cum*), not Q.IV. They are correctly absent from Q.IV's apparatus.

**Action**: open a separate backlog item to verify `vol1/bon-sent-I-d4-a1-q3.md` carries these 4 footer entries. If it doesn't, `d4-a1-q3` is apparatus-incomplete and needs its own pass.

## Convention note (low priority)

Apparatus diff per `audit-apparatus-count.py`: raw heuristic 16 vs chunk 9 = +7. Within tolerance (no flag). Diff explained by:
- Q.III footer anchors (per above) — 4 entries.
- Per-page footer-block opener regex noise (~2-3 false positives on this stretch).
- No genuine Q.IV footer is missing from the chunk.
