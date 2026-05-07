# d.35 littera — Tier-2 ambiguities

Generated 2026-05-07 during the Tier-2 promotion of `vol1/bon-sent-I-d35-littera.md` (Lombard's *Sententiarum* Lib. I, Dist. XXXV, Capp. I–IX, printed pp. 597–598).

## Frontmatter scope correction

- **Initial scaffolding listed `printed_pages: [598, 599, 600]`** — verified at 400 dpi against `raw/doctorisseraphic12bona.pdf` pp. 187–189 that the Lombard littera occupies **only printed pp. 597–598** (PDF pp. 187–188). Printed p. 599 (PDF p. 189) opens *COMMENTARIUS IN DISTINCTIONEM XXXV* (Bonaventure), and p. 600 opens *ARTICULUS UNICUS / De ideis* (q. 1). Frontmatter corrected to `[597, 598]` / `[187, 188]`. Source string and `transcription_status` updated accordingly. The OCR line span `18018–18226` is retained as-is — those raw lines do contain the full Lombard text plus mixed-column footer apparatus.

## OCR column-mixing

- **`raw/bonaventure_vol1_pt2_raw.txt` lines 18018–18226 are heavily column-fragmented.** ABBYY emitted the two-column body and the multi-column footnote band as interleaved short lines, so the Lombard text could not simply be reflowed from contiguous OCR rows. Cross-checked against 400-dpi PDF renders of pp. 597–598; the canonical Latin in this chunk is the OCR text *as disambiguated by the PDF column order*, with no silent re-wording.

## Apparatus

- **15 footnote entries total**: 5 from p. 597 footer (numbered ¹–⁵ in Quaracchi) + 10 from p. 598 footer (numbered ¹–¹⁰ in Quaracchi); renumbered consecutively `[^1]–[^15]` in the chunk.

- **`[^3]` is anchored twice**: once in Cap. I body listing (after *et* before *providentia*) and once in the Cap. II chapter title (after *praevidentia*). Both anchors are explicitly addressed by the same Quaracchi note ("In ipso capitulo plurimae edd. falso habent *sive providentia non de futuris*"), so a shared `[^3]` is the correct rendering.

## `[?]` flags inline in chunk

- **`[^15]` Psalm citation**: OCR reads "Psalm. i9, 11" — the lower-case `i` substituted for `1` is OCR-consistent with the Quaracchi smudge handling, so the reading is `Psalm. 19, 11` (Vulgate / Psalm 18 LXX). However, the quoted text *Et pulchritudo agri mecum est* corresponds in Augustine's *Enarrationes* to a different Psalm (frequently cited at Ps. 49 / Ps. 50 by Lombard elsewhere). Left as `[?]` pending Augustine concordance check at the polish-pass (decade-end) stage. **Rendered with the Quaracchi reference verbatim**; the `[?]` warns translators not to "harmonize" the citation away.

- **`[^10]` final note `[?]` in d.34 template**: NOT carried over here; this chunk's `[^10]` (`Codd. A C E *Praeterea*`) is unambiguous.

## Items NOT flagged (resolved in pass)

- *praescientia* vs *praevidentia* in Cap. I listing — settled by the Quaracchi `[^2]` note (omission variant in Vat. + edd. 4, 6); kept as transmitted.
- *Deo* / *Deum* at p. 598 line 4 — settled by `[^6]` (kept dative *Deo* per codices and ed. I).
- *terrenae* / *aeternae* in the Ambrose-Colossians citation (p. 598 last line) — `[^9]` Quaracchi explicitly restores *terrenae*; followed.
- *Propterea* / *Praeterea* opening of Cap. IX — `[^10]` flags the codex variant; kept *Propterea* per the body of editions.
