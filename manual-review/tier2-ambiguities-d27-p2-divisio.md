# Tier-2 ambiguities — `bon-sent-I-d27-p2-divisio`

## Apparatus-count audit disposition (2026-05-12)

**Audit flag**: `audit-apparatus-count.py` reports raw=13 chunk=0 +13 SKELETON-SUSPECT for chunk line range 6286–6356 (pp. 480–481).

**Disposition: ACCEPT-AS-NULL — false positive, no apparatus belongs to this chunk.**

### Evidence

The 7 numbered footer entries the audit detected within lines 6308–6324 are the **page-480 column footer**, which attaches to the body content immediately above (the *end* of the preceding chunk `bon-sent-I-d27-p1-dubia`, whose body text on p. 480 occupies raw lines 6240–6285 before the page-bottom rule). Variant words referenced by those 7 footnotes — `proprietatem informantem`, `significetur`, `tunc`, `de se`, `illis quae ita`, `quando`, `producente` — all appear in the d27-p1-dubia body text on p. 480, **not** in the divisio body.

Confirmed:

- `bon-sent-I-d27-p1-dubia.md` (printed_pages [479, 480]) already carries 16 apparatus entries covering both the p. 479 and p. 480 footers; the 7 p. 480 entries are accounted for there.
- The divisio body itself (lines 6286–6306 on p. 480, lines 6336–6356 on p. 481) contains zero footnote-marker glyphs in the OCR; no body anchors exist that an apparatus entry would target.
- The p. 481 footer (raw lines ~6428+) attaches to `bon-sent-I-d27-p2-a1-q1` (whose article-q1 body begins on p. 481), and that chunk's 24 apparatus entries already include them.

The remaining +6 from the heuristic count (13 vs the 7 visibly numbered) is regex noise: the audit script matches generic line-leading number-tokens and picks up false hits inside footnote-1's long editorial discussion of grammatical forms.

### Action

- `has_apparatus: false` is correct.
- No apparatus block added.
- Frontmatter `transcription_status` updated to note false-positive disposition.
- No body edits.
