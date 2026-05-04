# Tier-2 ambiguities — bon-sent-I-d26-dubia

Source: `raw/bonaventure_vol1_pt2_raw.txt` lines 4355–4587 (printed pp. 462–464; pdf pp. 52–54).

## Apparatus

- **[^22] in DUB X body, anchor on *simul natura*** (raw line 4579, single-quote marker `'`): the corresponding footer note is not present in the IA djvu OCR sweep of p. 464 (between line 4587 and the start of DISTINCTIO XXVII at line 4588 there is no apparatus block). The phrase *relativa simul natura sunt* is the standard tag from Aristotle, *Categoriae* c. *de Relatione* (7b15) — almost certainly the reference Quaracchi gives. → Resolve with eyes-on-PDF read of p. 464 footer (pdf p. 54). Currently rendered as a stub `[?]`-flagged entry.

- **[^23] in DUB X response, anchor on *sic et*** (raw line 4583): same situation. The marker is on the conjunction `et` after `sic`, suggesting a textual variant (perhaps Vat. omits or substitutes). → Resolve with eyes-on-PDF read of p. 464 footer.

## Body OCR

- **DUB. VII, *primo nuncupabatur*** (note [^18]): Quaracchi footer reads "Mox **niendum** in Vat., pro *nativitate*..." — `niendum` is OCR garble for *tenendum*. Rendered with `[?]` in the apparatus entry.

- **DUB. V, Boethius citation** (note [^11]): OCR has "posse locum accidentia per[?]mutare" — line break in the original; the intended word is *permutare* but the OCR fragments break the word. Currently rendered with `[?]` flag.

- **OCR garbles silently corrected** (no `[?]` needed):
  - Line 4358: `DuB. L` → `DUB. I.`
  - Line 4396: `DuB. 11.` → `DUB. II.`
  - Line 4395 (col B): `DuB. V.` (good)
  - Line 4374, 4430, 4495, 4504, 4572 (×2): `DuB.` casing normalized to `DUB.`
  - Line 4355: `DUBIA CIRC\ LITTERAM MAGISTRL` → `DUBIA CIRCA LITTERAM MAGISTRI.`
  - `alvud` → `aliud` (4358 col B, 4400)
  - `videtur^` → `videtur` (anchor handled separately)
  - `Responbeo` → `Respondeo`
  - `iinmuta-bilis` → `immutabilis`
  - `nuUo` → `nullo`
  - `fdius` → `filius` (multiple)
  - `fdia` → `filia`
  - `verura` → `verum`
  - `lioc` → `hoc`
  - `dieere` → `dicere`
  - `inlelhgentem` → `intelligentem`
  - `alietali` → `alietati`
  - `proprietalis` → `proprietatis`
  - `coieceditur` / `consitit` → `consistit`
  - `Boetbium` → `Boethium`
  - `creaiione` → `creatione`
  - `aftopftojie` (Greek mangled) → `adoptione`
  - `dicebat,quod` (joined): split
  - `Telativorum` → `relativorum`
  - `nyncupatur` (line 4538) → `nuncupatur`
  - `nuncupahatur` → `nuncupabatur`
  - `Aelhiopibus` → `Aethiopibus`
  - `flngere` → `fingere`
  - `usitatuni` → `usitatum`
  - `Sabel-liuni` → `Sabellium`
  - `loannis` → `Ioannis`
  - `Augustini ` `'"` → anchor [^10]; `"` → anchor [^11]
  - `'» Libr. V. de Trin.` → note 10 marker `'»` (= `10`)
  - Margin glosses (e.g. `Dupiex no- "'"^'`, `Aiiier.`, `sabiiistin-`, `•ripies imi-`, `solutio j`, `soiuiio`) stripped from running text — they are editorial marginalia.
  - Trailing/leading column spurs and broken hyphenation across columns rejoined.

## Citations preserved verbatim

- `*primae ad Timotheum ultimo*` → 1 Tim 6, 20 (apparatus note [^1])
- `infra distinctione vigesima octava` → preserved as transcribed; not normalized
- `Ioannis octavo` (= John 8) — Quaracchi footer note [^17] gives `Vers. 44` (John 8:44)
- All `n.`, `c.`, book numerals (Roman = chapter) preserved verbatim per project discipline

## Boundary

- Chunk boundary fixed: `line_start: 4477 → 4355` to capture the full DUBIA CIRCA LITTERAM MAGISTRI block including DUB. I, II, III, IV, V (which were entirely missing in the prior auto-chunked skeleton).
- Chunk ends at line 4587 — one line before `DISTINCTIO XXVII.` heading at 4588.
