# Tier-2 ambiguities — bon-sent-I-d22-a1-q1

Resolved 2026-05-03 during Tier-2 promotion. One `[?]` flag in the Scholion text.

- **Scholion II opening (`Solut. ad 6. 7.[?]`):** OCR shows `Solut. ad 6. 7.` but the Bonaventure body of this question contains only objections 1–6 (no separate "objection 7" — the contra has 5 args; the article has only this one quaestio). The reference may be either to obj. 6 alone (where `7` is OCR garble for stray punctuation) or to a cross-tract reference. Provisionally retained as `6. 7.` with `[?]` flag pending PDF check at 400 dpi.
- **Body OCR fixes silently applied** (no `[?]` needed):
  - L67369 `Dionysius de Divinis Nominibus'` — `'` is anchor 1 → `[^1]`.
  - L67381 `»tomen` → `nomen` (initial OCR glyph garble).
  - L67391 `subterftigit` → `subterfugit` (ft/fu OCR confusion).
  - L67394 `onine` → `omne`.
  - L67399 `quod nec '` — apostrophe is anchor 7.
  - L67407 `Contra: i.` → `Contra: 1.`
  - L67411-12 `divinis noniinibus` → `divinis nominibus`.
  - L67485 `» 67, 5.` — `»` is the OCR rendering of footnote marker 9; entry text is `67, 5.` (Psalm 67:5).
  - L67520 `e (licitur dupliciter` → `dicitur dupliciter` (mid-line break artifact).
  - L67537 `effabihs` → `effabilis`.
  - L67541 `fldei` → `fidei`.
  - L67566 `quam ^'` — `^'` together = anchor 11 (`[^23]`).
  - L67583 `quafitatis` → `qualitatis`.
  - L67663 `UislincUo` → `Distinctio`; `pcr se` → `per se`.
  - L67667 `novwii pmlum` → `nomen positum` (Scholion I citing Richard. a Med. on proportion).
  - L67670-71 `oreata` → `creata`; `creala` → `creata`.
  - L67673 `loan. Damasccnum` → `Ioan. Damascenum`.
  - L67682 `codem` → `eodem`.
  - L67684 `Alex. llal.` → `Alex. Hal.`
  - L67688 `e,\planat` → `explanat`; `signiflcent` → `significent`.
  - L67689 `notiflcabilis` → `notificabilis`.
  - L67690 `temporo` → `tempore`.
  - L67692 `signiflcamus` → `significamus`; `signiflcat` → `significat`.
  - L67694 `riicit` → `dicit`.
  - L67695 `Vcrbum substanlivum` → `Verbum substantivum`; `signiflcatio-` → `significatio-`.
  - L67697 `substantlam` → `substantiam`; `seoundum` → `secundum`.

All resolved by context-unambiguous OCR cleanup per project CLAUDE.md silent-fix rule.
