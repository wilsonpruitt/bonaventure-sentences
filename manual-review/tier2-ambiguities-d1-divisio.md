# d.1 divisio — Tier-2 ambiguities log

Promoted 2026-05-08 from auto-chunked skeleton to Tier-2 verbatim from raw OCR
(`raw/bonaventure_vol1_raw.txt` lines 13224–13377; printed pp. 29–30; PDF pp. 131–132).

## OCR garbles silently corrected (unambiguous from PDF + context)

All resolved against `raw/vision/vol1/p-029.png` and `p-030.png` extracted at 400 dpi.

| OCR (raw) | Corrected | Notes |
|---|---|---|
| `sigjia` | `signa` | obvious; matches the *res / signa* division thesis |
| `prnponit` | `proponit` | letter substitution |
| `p^'ima` / `p7-i-ma` / `pi'ima` | `prima` | broken hyphenation + glyph noise |
| `Fi-ui` | `Frui` | broken hyphen across word |
| `el utuntnr` | `et utuntur` | OCR `el` → `et`, `utuntnr` → `utuntur` |
| `«ecitnrfa` | *secunda* | italic OCR garble; PDF reads *secunda* |
| `deflnitiones` | `definitiones` | `fl` ligature mis-parse |
| `definitionuin` | `definitionum` | `m` → `in` |
| `parle` | `parte` | `t` → `l` |
| `quoruni` | `quorum` | `m` → `ni` |
| `wft` | `uti` | OCR of italic *uti* |
| `Secwndo` | `Secundo` | `u` → `w` |
| `continsat` | `contingat` | `g` → `s` |
| `frid` | `frui` | `u` → `d` (italic *frui*) |
| `oraittit` | `omittit` | `m` → `ra` |
| `consUtuctionem` (constru-cUonem) | `constructionem` | broken across line |
| `subslituimus` | `substituimus` | `t` → `sl` |
| `addidlmus` | `addidimus` | `i` → `l` |
| `Itenim` | `Iterum` | mid-word glyph noise |
| `revcra` | `revera` | `e` → `c` |
| `anliquiores` | `antiquiores` | `t` → `l` |
| `fr^uatur` | `fruatur` | footnote-marker spacing |
| `istarumtrium` | `istarum trium` | missing space |
| `conflrmat` / `confirmat` | `confirmat` | `fi`-ligature |

## Footnote-anchor placements

OCR preserves the Quaracchi marker spacing `secunda ' :`, `duas '`, `Secundo  ^`,
`considerandum  *`, `sit ^`, `explanat ipsam "`, `etc. '.`, `secun-da  *`,
`fruendum  est  ^`, `videntur  '°`, `quarum  "`, `tertia  quaestio  ^'^`. These were
mapped to `[^1]`–`[^12]` in body order. Apparatus on p.29 holds notes 1–5; p.30
holds notes 6–12 (Quaracchi restarts numbering each page; chunk numbering is
continuous).

## Genuine `[?]` flags

None. Every OCR garble in this chunk was resolvable either by morphological
context (Latin grammar) or by direct comparison with the 400 dpi PDF pages.
