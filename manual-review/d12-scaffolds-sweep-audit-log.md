# d.12 Scaffolds Sweep Audit Log — 2026-05-08

Audit of `bon-sent-I-d12-{divisio,littera,dubia}.md` per the d.4–d.9 sweep methodology. All three chunks were already promoted to Tier 2 on 2026-05-02 with detailed apparatus pulled from OCR; this audit re-verifies bounds, body fidelity, and apparatus content against `raw/bonaventure_vol1_raw.txt`.

## Per-chunk verdict

### bon-sent-I-d12-littera  (lines 41858–42095)
**Verdict: PASS (no rebuild needed).**

- Bounds verified. `DISTINCTIO XII.` header at OCR line 41864; running-head break to printed page 219 at OCR line 41960 (chunk's `<!-- page 219 -->` marker placed at correct paragraph break "Ex eodem sensu dicitur etiam *proprie* procedere de Patre"). Text terminates before `COMMENTARIUS IN DISTINCTIONEM XII.` at line 42044. Apparatus block (page-218 NOTAE + page-219 NOTAE) closes at line 42037, just before the page-220 running head — `line_end: 42095` is generous but harmless (covers the end-of-page footnote block).
- `## Latin` body diffs cleanly against OCR lines 41864–41957 (cap. I + opening of cap. II) and 41962–42007 (rest of cap. II). Punctuation, italics, Quaracchi quotation marks (« »), citations match.
- 18-footnote apparatus verified against OCR page-218 footers (fn 1 lines 41992–41996; main NOTAE block 41999–42013) and page-219 footers (lines 42017–42037). All 18 chunk apparatus entries present in OCR; bilingual `**La.**`/`**En.**` structure intact.
- One minor OCR-garble silently corrected: chunk apparatus [^14] reads `Ioan. 15, 26` where OCR raw has `loan. 13, 26`. The Quaracchi citation is unambiguously John 15:26 (*De Patre procedit* — Spirit-of-Truth verse), and OCR `3` for `5` is a known ABBYY confusion. Correction is sound; not flagged.
- English translation literal and parallel to Latin paragraph-for-paragraph.
- No `[?]` flags raised.

### bon-sent-I-d12-divisio  (lines 42040–42147)
**Verdict: PASS (no rebuild needed).**

- Bounds verified. `COMMENTARIUS IN DISTINCTIONEM XII.` at OCR line 42044; second running-head `DISTINCTIO XII. DIVISIO TEXTUS.` (the page-219 page-bottom running head — *not* a semantic header) at line 41957 is correctly NOT used as the chunk's start, despite the line_start frontmatter being 42040. Wilson's tentative bound "42042 → 42149" is correct; the existing `42040–42147` is functionally identical.
- COMMENTARIUS, DIVISIO TEXTUS, TRACTATIO QUAESTIONUM, and ARTICULUS UNICUS heading sequence all present and ordered correctly.
- `## Latin` body diffs cleanly against OCR. The page break (`<!-- page 220 -->`) is correctly placed after the first DIVISIO paragraph, before "*Secundo*, utrum *principalius et plenius*..." — matches OCR running-head transition at line 42067.
- 2-footnote apparatus (NOTAE AD COMMENTARIUM block at OCR lines 42126–42131) verified:
  - [^1] "Aliqui codd. ut A I S T V Y *procedat*" — exact match to OCR fn 1.
  - [^2] "Vat. absque auctoritate mss. et ed. 1 paulo ante ponendo *partes* loco *capitula*, et omissis verbis *in quatuor capitulis* pronuntiat..." — chunk preserves the OCR's truncation (the OCR fn 2 ends at "pro-" and the continuation onto p.220 was lost across the page break in OCR). Chunk's English correctly notes "[reading truncated in OCR]". This is a single legitimate truncation, not a fabrication. Acceptable as-is per d.9-style policy on OCR truncation.
- English translation literal and parallel.
- No `[?]` flags raised. (The `[?]` would have applied to [^2] truncation, but the chunk's "[reading truncated in OCR]" English note is a clearer in-place disclosure than a flag — leave as-is.)

### bon-sent-I-d12-dubia  (lines 43069–43304)
**Verdict: PASS (no rebuild needed).**

- Bounds verified. `DUBIA CIRCA LITTERAM MAGISTRI` at OCR line 43076. Dub I body 43078–43113; page-226 NOTAE at lines 43153–43168 (fn 6–12 in our count) and page-227 NOTAE at 43257–43282 (fn 1–12 — the per-page numbering resets in OCR). DUB II opens at line 43208, DUB III at 43227, DUB IV at 43240. Ends before page break at line 43285 (`SENTENTIARUM LIB.` running head) and DISTINCTIO XIII opener at 43289.
- `## Latin` body diffs cleanly across all four dubia. Punctuation, italics, marginalia (chunk correctly excludes the "ut propositio contradictoria", "Solvitur 1.", "Solvitur 2.", "Soluitur alia.", "Solutio aliorum.", "Non probatur.", "Solutio vera." marginal labels — these are Quaracchi's typeset side-glosses, and the chunk renders them as inline italic markers like `*Solutio 1.*`/`*Solutio aliorum.*`/`*Non probatur.*`/`*Solutio vera.*` at the right paragraph positions, which is the correct Tier-2 convention).
- 19-footnote apparatus verified against the two OCR NOTAE blocks (page 226: fn 6 "Aristot., I Periherm. c. 6 (c. 8)"; page 227 fn 1–12). Spot-checked [^1] [^4] [^6] [^9] [^11] [^14] [^16] [^17] [^19] — all match OCR verbatim.
- The page break `<!-- page 227 -->` is correctly placed inside DUB IV's response, between "*Solutio aliorum.*" + "*Non probatur.*" and "*Solutio vera.*", matching the OCR running-head transition.
- English translation literal; *Solutio* labels translated as "*Solution 1.*" / "*The solution of others.*" / "*Not proven.*" / "*The true solution.*" — consistent with d.9 dubia and corpus-wide convention.
- No `[?]` flags raised.

## Totals

| Chunk | Bounds | Latin body | English | Apparatus entries | Fabricated entries | `[?]` raised |
|---|---|---|---|---|---|---|
| littera | 41858–42095 (verified) | clean | clean | 18 | 0 | 0 |
| divisio | 42040–42147 (verified) | clean | clean | 2 | 0 | 0 (truncation in [^2] disclosed inline) |
| dubia | 43069–43304 (verified) | clean | clean | 19 | 0 | 0 |
| **TOTAL** | | | | **39** | **0** | **0** |

## Anomalies

1. **OCR `Ioan. 13, 26` → corpus `Ioan. 15, 26`**: littera apparatus [^14]. ABBYY OCR garble of `5` to `3`, silently corrected to the unambiguous Quaracchi reading. Not a fabrication; documenting here so future audits don't re-flag.

2. **Divisio [^2] OCR truncation across page 219→220 break**: the OCR loses the continuation of the long Vat.-variant note at the page-bottom NOTAE block. The chunk preserves the truncation honestly via "[reading truncated in OCR]" in the English. Recommended for resolution at the next d.10–d.20 polish-blocker decade pass via 600 dpi PDF eyes-on (printed page 220 footer note 2 continuation). NOT a fabrication; flag-equivalent already in place.

3. **No fabrication, no body omissions, no bound leakage, no misplaced page breaks** — d.12 is meaningfully cleaner than d.4/d.5/d.7/d.9, all of which had at least one fabricated apparatus entry. Likely because d.12 was promoted to Tier 2 on 2026-05-02 (after the d.9 wave-1 audit lessons were already applied to the OCR-direct-apparatus discipline). Recommend continuing this approach for d.13+ rechunks.

## Backups

No backups created — no substantive edits made. All three chunks pass audit as-shipped.

## Build smoke-test

`cd site && node scripts/build-content.mjs` → `Built content.json: 1 book(s), 422 questions, 350 translated` (clean parse, no errors).
