# d27-p1-a1-q2 Tier-2 ambiguities (Wave 9b Tier A close, 2026-05-09)

## Context

Apparatus rebuild on `vol1/bon-sent-I-d27-p1-a1-q2.md`. Pre-rebuild: 25 entries (`[^1]`–`[^25]`), all body-anchored. Post-rebuild: 48 entries — the 25 body-anchored entries preserved verbatim, plus 23 new page-foot lemma-variant entries `[^26]`–`[^48]` supplementing the per-page footer sequences.

## Per-page footer count (ground truth, eyes-on raw OCR pp. 468–474)

| Printed page | Footer entries (numbered) | Covered by pre-rebuild [^1]–[^25] | Added in [^26]–[^48] |
|---|---|---|---|
| 468 | 7 (entries 1–7) | only entry 4 (= [^1] *Libr. Sent.*) — entries 1, 2, 3, 5, 6, 7 were merged inline into [^1] | [^26]–[^31] (entries 1, 2, 3, 5, 6, 7) |
| 469 | 10 (entries 1–10) | entries 2–10 = [^2]–[^10]. Entry 1 (Vat. *generari*) was missing. | [^32] (entry 1) |
| 470 | 14 (entries 1–14) | entries 1, 5, 7, 9, 10, 11 = [^11], [^13], [^14], [^15], [^12], [^16]. Entries 2, 3, 4, 6, 8, 12, 13, 14 were missing. | [^33]–[^40] (entries 2, 3, 4, 6, 8, 12, 13, 14) |
| 471 | 11 (entries 1–11) | entries 1 (Hilary num. 21), 3, 5, 8 = [^17], [^18], [^19], [^20]. Entry 2 (Hilary num. 6) was merged into [^17]. Entries 4, 6, 7, 9, 10, 11 missing. | [^41]–[^47] (entries 2, 4, 6, 7, 9, 10, 11) |
| 472 | 5 (entries 1–5) | entries 1–4 = [^21], [^22], [^23], [^24]. Entry 5 was merged into [^24]. | [^48] (entry 5, retained inline in [^24] for continuity, also broken out for per-page count fidelity) |
| 473 | 1 (entry 1) | entry 1 = [^25]. Complete. | — |
| 474 | 0 (no numbered footers; only inline italic editorial paragraph). | — | — |
| **Total** | **48** | 25 (with merging) | 23 |

## Hardened-audit overcount judgment

`audit-apparatus-count.py` (post-2026-05-09 hardening) reported raw=57 footer markers in the OCR range, against pre-rebuild chunk count 25 (diff +32). Eyes-on per-page footer enumeration confirms ground-truth = 48. The audit overcount is ~+9 (≈19% noise on the high side), consistent with the Wave-2 Wave-9b finding that the heuristic over-counts when chunks contain Scholion content with italicized work-citations (`*Sent.* d. 36. q. 3.`), lettered series, and numbered-argument openers — d27-p1-a1-q2 contains a long Scholion (sections I, II, III with numbered cross-references to S. Thom., Alex. Hal., Albert, etc.) and the Anecdota II disquisition with numbered argument blocks `1.`–`8.` plus a lettered `5.` `6.` `7.` `8.` series, which the heuristic regex catches as footer openers.

**Disposition:** ACCEPT WITH REASON. Chunk now has 48 `[^N]:` defs, audit-heuristic raw=57. Diff +9 is heuristic-overcount on Scholion + Anecdota lettered/numbered series, not missing apparatus. Ground-truth count (per-page footer enumeration) is 48 and is fully covered.

## Open `[?]` flags (3)

1. **`[^47]` (page 471 footer 11): OCR truncated at column boundary.** The IA djvu OCR cuts the right column off at `Vat. cum cod.` (line ~5414 of `raw/bonaventure_vol1_pt2_raw.txt`); the printed page-bottom in the Quaracchi 1882 edition continues with a small variant note that did not survive deinterleaving. Tag preserved as `**La.** Vat. cum cod. [?] [OCR truncated at column boundary…]`. **Resolution path:** consult the Quaracchi PDF p. 471 footer block at 600dpi via `tools/extract-pages.py --volume vol1pt2 --pages 471 --dpi 600` to recover the truncated text. Deferred — not blocking polish-cadence (per CLAUDE.md `feedback_bonaventure-pdf-supplement-audit.md` discipline).

2. **`*valuabiliter[?]*`** (Anecdota II body, p. 474 line 286 of chunk Latin / line ~5613 of raw): `valuabiliter` is not a normal Latin word; OCR likely corrupting `variabiliter` ("variably"). Pre-existing flag from prior Tier-2 pass; preserved.

3. **`*inventurus[?]*`** (Anecdota II body close, p. 474 final clause): the cod. G ending phrase `nescio si unquam sit cum alicubi inventurus esse` is grammatically rough; OCR may have garbled. Pre-existing flag from prior Tier-2 pass; preserved.

## Body-paraphrase guard

Walked the chunk's Latin against raw OCR pp. 468–474 deinterleaved sequence. The chunk's Latin body is **verbatim** transcription with light OCR-cleanup (capital-letter restoration, italic-emphasis preservation, deinterleaved column reassembly). No paraphrase clusters detected. The Anecdota I + II passages are integrally preserved. Status string `complete` (not `apparatus-rebuilt-body-paraphrased`) is justified.

## Sanity check on convention

Per-page restart numbering not strictly enforced by the corpus parser; consecutive `[^N]` numbering retained. Page-of-origin labeled inline in each new entry (`[Page NNN, footer M.]`) so that future per-page-restart auditors can map entries to the printed source.

## Audit results at rebuild close

| Audit | Result | Disposition |
|---|---|---|
| `audit-paraphrase.py` (full corpus) | 0 critical / 1 high (pre-existing d11-divisio, unrelated) | clean |
| `audit-formatting.py` | WARN: `apparatus def with no marker: ['26'…'48']` | ACCEPT WITH REASON — entries [^26]–[^48] are page-foot lemma-variant supplements; absence of body marker is by design and documented in the apparatus section header (`> **Page-foot lemma-variant entries.** …that bear on lemma text or editorial notes rather than on body markers`). Pattern matches Wave-1 disposition for `d3-p2-dubia` orphan apparatus defs. |
| `audit-apparatus-count.py --min-d 27 --max-d 27` | raw=57, chunk=48, diff +9 | ACCEPT WITH REASON — heuristic over-counts on Scholion italicized work-citations + Anecdota II numbered argument series. Ground-truth per-page footer enumeration = 48; fully covered. |
