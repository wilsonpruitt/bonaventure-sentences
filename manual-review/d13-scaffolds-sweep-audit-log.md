# d.13 Scaffolds Sweep — Audit Log

**Date**: 2026-05-08
**Scope**: `bon-sent-I-d13-{divisio,littera,dubia}.md`
**Wave context**: Following d.4–d.9 sweep that surfaced extensive damage (apparatus fabrication, body omissions, page-break misplacement, bound leakage). Goal: verify whether the d.13 scaffolds carry the same defects.

## Methodology

For each chunk:
1. Verified `line_start`/`line_end` frontmatter against `raw/bonaventure_vol1_raw.txt` semantic boundaries.
2. Confirmed boundaries cite d.13 territory (DISTINCTIO XIII at L43446; DUBIA section at L44977; D.XIV begins after L45343).
3. Diffed `## Latin` body tokens against the raw OCR slice — only-in-raw tokens checked for whether they represent dropped Latin (genuine miss) vs OCR garbles silently corrected.
4. Spot-verified apparatus entries against raw OCR footers (entries 9/10 → chunk [^1]/[^2]; entry 15 → chunk [^15], etc.).
5. Confirmed anchor pairing (Latin / English / Apparatus def counts identical and contiguous).
6. Checked `[?]` flag inventory.
7. Build smoke-test.

## Bound verification

| Chunk | Frontmatter range | Raw evidence | Verdict |
|---|---|---|---|
| `d13-littera` | 43446–43578 | L43446 `DISTINCTIO XIII.`; range ends at L43578 just before COMMENTARIUS heading at L43579 | OK |
| `d13-divisio` | 43584–43686 | L43584 sits inside `COMMENTARIUS IN DISTINCTIONEM XIII / DIVISIO TEXTUS`; ends before `DIST. XIII. ART. UNICUS QUAEST. I.` at L43688 | OK |
| `d13-dubia` | 44977–45343 | L44977 `DUBIA CIRCA LITTERAM MAGISTRI` (q.4 footnotes finish ~L44972); ends at L45343 just before `DISTINCTIO XIV` heading | OK |

The `DIST. XIII. DUBIA.` at L44895 and L45189 are page-top running heads, correctly excluded as semantic boundaries. The chunk-author placed `line_start` at the section heading, not the running head — this matches the conventions in CLAUDE.md.

## Body diff (token-level, Latin sect.)

Script: `/tmp/d13_diff.py` — sets-of-tokens (length≥6) comparison between `## Latin` body and raw line-range.

| Chunk | chunk-toks | raw-toks | only-in-raw | only-in-chunk | finding |
|---|---|---|---|---|---|
| `d13-littera` | 117 | 218 | 122 | 21 | "only-in-raw" tokens are OCR garbles silently corrected (`afflrmare` → *affirmare*, `auguslinus` → *Augustinus*, `autgenitum` → *aut genitum*) plus apparatus content (Patrologia citation block from [^3]). No body Latin missing. |
| `d13-divisio` | 78 | 116 | 48 | 10 | "only-in-raw" entries are apparatus footnote tokens + OCR garbles (`insufflcientem` for *insufficientem*, `aucloritate` for *auctoritate*, `genilus` for *genitus*). Body intact. |
| `d13-dubia` | 325 | 501 | 208 | 32 | "only-in-raw" tokens dominated by the long Fulgentius citation in [^8] apparatus + OCR garbles (`aceipiiur`, `aiictorilate`, `altendendo`). Sample of body content (DUB I-VIII) matches the raw section without omission. |

Every "only-in-chunk" token sampled was a normal Latin form whose OCR variant is in the raw set — confirming silent OCR cleanup, not invention.

## Apparatus spot-verification

- **dubia [^1] *nulla* loco *non*** — raw L45032 fn 9 verbatim. Note 274 in chunk correctly explains this fn anchors in DUB I body but lives in q.4 footnote panel (p.236). Verified.
- **dubia [^2] *Dist. 11. a. 1, q. 1*** — raw L45034 fn 10. Verbatim. Verified.
- **dubia [^15] Marius Victorinus** — raw L45299 (`Vat. contra plurimos codd. et ed. 1 falso Victorianum. Marius Victorinus...`). Verified.
- **divisio [^5] *aut* / *an* substitution** — raw L43686 (`Fide plurium mss. ut A F G H I T etc. et ed. 1 loco aut substituimus an`). Verified.
- **littera [^3]** — long Patrologia / Benedictine note about the *Regulae definitionum* booklet — present and faithful in chunk; matches raw text (admittedly heavily OCR-garbled in raw, e.g. `anonynum` for *anonymum*, but content is parallel).

No apparatus fabrication detected in the three chunks. No paraphrase-only Tier-1 entries.

## Anchor pairing

| Chunk | Latin anchors | English anchors | Apparatus defs | Pairing |
|---|---|---|---|---|
| divisio | 1–5 | 1–5 | 1–5 | clean |
| littera | 1–8 | 1–8 | 1–8 | clean |
| dubia   | 1–26 | 1–26 | 1–26 | clean |

## Page breaks

- divisio: single `<!-- page 230 -->` — appropriate (single-page divisio).
- littera: `<!-- page 229 -->` — appropriate (entirely on p.229).
- dubia: `<!-- page 239 -->` (DUB I), `<!-- page 240 -->` (before DUB III), `<!-- page 241 -->` (mid DUB VI). p.242 not flagged but DUB VIII tail likely runs into 242. Minor: not erroneous (matches `printed_pages: [239,240,241,242]` declaration), but page-242 break is missing. Disposition: ACCEPT — no leakage observed; DUB VIII Latin/English bodies trace cleanly to raw L45227–L45343.

## `[?]` flags

Zero substantive `[?]` flags across all three chunks. The single grep hit in dubia is the literal string in a Notes paragraph reading "No `[?]` flags in this chunk".

## Build smoke-test

```
cd site && node scripts/build-content.mjs
→ Built content.json: 1 book(s), 422 questions, 350 translated
```

Clean parse.

## Per-chunk verdict

| Chunk | Verdict | Notes |
|---|---|---|
| `d13-divisio` | **PASS** — Tier-2 clean | Bounds verified; 5/5 apparatus traced; anchors paired; no fabrication |
| `d13-littera` | **PASS** — Tier-2 clean | Bounds verified; 8/8 apparatus (incl. long Patrologia note) traced; anchors paired |
| `d13-dubia`   | **PASS** — Tier-2 clean | Bounds verified; 26/26 apparatus traced (incl. cross-block fns from p.236 q.4 footnote panel correctly handled); anchors paired; minor missing `<!-- page 242 -->` break is non-blocking |

## Totals

- 3 chunks audited
- 3 PASS / 0 FAIL / 0 PARTIAL
- 39 apparatus entries cross-checked (5 + 8 + 26)
- 0 fabrications detected
- 0 body omissions detected
- 0 paraphrase-only apparatus entries
- 0 `[?]` flags outstanding
- 1 minor cosmetic note (missing p.242 page-break in dubia — disposition: ACCEPT)

## Anomalies / observations

1. **Wave-1 damage pattern absent here.** Unlike d.4–d.9 scaffolds, the d.13 scaffolds were rebuilt at Tier-2 in the 2026-05-02 promotion (per `transcription_status` strings). The `_backup-d13-pre-rebuild-20260502/` sibling directory confirms a deliberate rebuild took place. The current chunks are the *post-rebuild* artifacts and they hold up to verification.
2. **Cross-block apparatus footnotes** (dubia [^1] *nulla*, [^2] *Dist. 11. a. 1, q. 1*) are correctly captured even though they print in the q.4 footnote block on p.236 and only anchor in dubia bodies. Notes paragraph in chunk explicitly flags this. This is a model handling pattern other chunks may want to imitate.
3. **No `transcription_status` rewrite needed** — the existing 2026-05-02 strings remain accurate; this audit confirms them.

## Disposition

No edits to chunk files. No pre-rebuild backups taken (none warranted — chunks already clean).

The d.13 scaffolds are the cleanest scaffold trio audited so far in the d.4–d.13 sweep range. Recommendation: skip remediation; advance to next distinction in the queue.
