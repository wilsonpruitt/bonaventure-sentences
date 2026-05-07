# d.39 divisio — Tier-2 ambiguities

Tier-2 rebuild 2026-05-07 from raw OCR lines 26536–26584 (`raw/bonaventure_vol1_pt2_raw.txt`).

No `[?]` flags raised. The OCR garbles in this block were all unambiguous and silently corrected:

- `DI8TINCTI0NEM` → `DISTINCTIONEM` (heading)
- `pei-fectioin'` → `perfectione` (chapter sub-heading)
- `Siipia egil` → `Supra egit`
- `iiic` → `hic`
- `qnoniam vere` → `quoniam vere`
- `perfectimi` → `perfectum`
- `liabet liaec` → `habet haec`
- `deterniinat` → `determinat`
- `diminutio- / nem` → `diminutionem`
- `orania` → `omnia`
- `terlia` → `tertia`
- `TEXTLIS` → `TEXTUS`
- `QU.^ESTIONUM` → `QUAESTIONUM`
- `.\d intelligentiam` → `Ad intelligentiam`
- `ulrum` → `utrum`
- Footnote-marker garble `ultimo capitulo -.` resolved as `ultimo capitulo[^2].`

Apparatus entries (2): note 1 = `Cfr. supra pag. 312, nota 8.` (OCR `.312, nota S.` — the `S` is a clear `8` garble; the cross-reference page 312 is unambiguous in context). Note 2 = `Supple cum Vat. ibi: Simul itaque.`

Frontmatter correction: `printed_pages` was `[662]`, corrected to `[684]` (the COMMENTARIUS heading sits on the page preceding the running-head "DIST. XXXIX. ART. I. QUAEST. I. 685" at OCR line 26613). PDF page = 684 − 410 = 274.
