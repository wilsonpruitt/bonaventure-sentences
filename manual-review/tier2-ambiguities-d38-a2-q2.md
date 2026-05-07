# d.38 a.2 q.2 — Tier-2 ambiguities

Date: 2026-05-07. OCR raw lines 25984–26273 of `bonaventure_vol1_pt2_raw.txt`. Printed pp. 676–679. Two-column OCR is heavily fragmented at column-boundaries; the scholion at the page-foot of p. 678 / page-head of p. 679 in particular is shredded across multiple lines.

## Inline `[?]` flags

- **Respondeo (opening)**: `sicut necessario probatum est [?]` — OCR reads "sicut necessario probatum est"; footnote anchor at the OCR position is the `Hic in fundam.` apparatus note (which we render as note [^9]). Sense ambiguous between "as has been necessarily proven" and reading `necessarium` as adjective. Currently rendered "as has been necessarily proven."
- **Respondeo (Et praeterea, sicut dictum est [?])**: OCR fragments here; the parallel reference seems to be back to the body of fundamentum 4. Render preserved as "as has been said."
- **Respondeo (sed quoniam divina cognitio [?] non habet)**: footnote in OCR — note flags `Codd. L praecognitio.` — text reads either *cognitio* or *praecognitio* per witness. Kept *cognitio* per Quaracchi text.
- **Scholion §I (`EandiMii qiiacstiom` / `Uli'iini sil possibili', Dinini noii`)**: OCR reads `EandiMii qiiacstiom Ulrum sit possibili Dinini non`. Reconstructed as "Eandem quaestionem... utrum sit possibile, Deum non...". The full scholion sentence is broken across the column-foot at the page-break and the visible OCR characters do not reconstruct cleanly. **Status: ACCEPT-FRAGMENT** for now; needs 600dpi PDF eyes-on at next decade-polish (d.40) cycle. Substantive content of §I (sensus compositus/divisus + connotatum vs principale significatum) is reconstructed from the body-text (the scholion paraphrases the *Respondeo*).
- **Scholion §II (Biel, here[?])**: OCR breaks off mid-citation ("Biel, hio"). Could be "hic q. unica" or another locus; left as `here[?]`.

## Frontmatter corrections (vs. auto-chunked starting state)

- `printed_pages: [638, 639, 640]` → **`[676, 677, 678, 679]`**. Pages 638–640 belonged to d.37; d.38 a.2 q.2 sits at the end of d.38 a.2, opening on p. 676.
- `pdf_pages: [228, 229, 230]` → **`[266, 267, 268, 269]`** (pt2 offset = printed − 410).
- `source: ... pp. 638–640` → `pp. 676–679`.
- `transcription_status` rewritten per CLAUDE.md Tier-2 recipe.

## Apparatus reconstruction notes

OCR puts the apparatus block at the page-foot of pp. 676–679. We extracted **10 footnotes**, mapped to body anchors `[^1]`–`[^10]`. Some Quaracchi footnotes that appear in OCR (e.g. the marginalia on `Mastrius`) have been merged into the corresponding apparatus entry rather than split as separate footnotes, because Quaracchi numbering on pp. 678–679 runs across two columns and several entries are continuation glosses rather than independent notes.

## Resolution disposition

To be reviewed at the d.31–d.40 polish-blocker cycle (after d.40 ships): bring 600dpi PDF eyes-on for the scholion fragments, and verify Mastrius citation in [^8].
