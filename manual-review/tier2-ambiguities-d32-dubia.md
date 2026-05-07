# d.32 Dubia — Tier-2 ambiguities

Logged 2026-05-06 during Tier-2 promotion of `vol1/bon-sent-I-d32-dubia.md` (raw lines 14826–15017, printed pp. 565–566).

## Ambiguities flagged inline as `[?]`

1. **DUB. II answer, p.566 col-A opening: `Ad illud[^8] — quare non dicitur potentia de potentia?`** — In the raw OCR (lines 14933) the leading words are `Ad iUud - quare non dicitur potentia de po-/tentia?` with a hyphen/dash, no clear apparatus marker before the dash. I have placed apparatus footnote `[^8]` (which corresponds to *In codd. K P Q W Y hic additur quod quaeritur*) here because its content is clearly about the opening of this sub-paragraph; but the exact spelling and any added words (`quod quaeritur` per K P Q W Y) is contained in the apparatus rather than promoted into the body. Position confirmed by sense; verify against PDF p.566 if a future polish pass disagrees.

2. ~~**DUB. V conclusion, last sentence: `Et ideo Magister bo[ne dicit][?].`**~~ — **RESOLVED 2026-05-06 via column-bleed discovery on p. 867 (raw lines 15020–15030).** The truncation was not "bo[ne dicit]" but `Magister bonum exemplum ponit in hoc termino Deus, quod significat essentiam et supponit personam. — Quando ergo quaeritur, utrum dicatur essentialiter, an personaliter; dicendum, quod quantum ad significatum dicitur essentialiter, sed quantum ad suppositum dicitur personaliter; et ideo nulla est controversia.` The same column-bleed surfaced two further sub-dubia (DUB. VI–VII) that the auto-chunker had clipped; these are now appended and the chunk's `line_end` extended to 15061. See `## DUB. VI–VII append (2026-05-06)` below.

## Notes (resolved without `[?]` flag)

- **Sub-dubia order in OCR**: The two-column reflow puts `DuB. V.` (col B, line 14949) spatially before `DUB. III.` (col A, line 14950) and `DuB. IV.` (col A, line 14982). Reflowed to canonical I–V order without a flag — clearly a typesetting artifact.
- **OCR garbles silently corrected** (per CLAUDE.md rule): `Ubro` → `libro`, `f/ePatre` → `de Patre`, `dei`/`del`/`hic`-style minor letter substitutions, `liifferunt` → `differunt`, `aho` → `alio`, `iUud` → `illud`.
- **Apparatus footnote count**: 6 entries on p.565 + 9 entries on p.566 = 15 total. Body markers `[^1]`–`[^15]` placed to match.

## DUB. VI–VII append (2026-05-06)

Auto-chunker had clipped the dubia block at raw line 15017 (visible end of p. 866 col-B). PDF p. 867 has a page-top running head `DISTINCTIO XXXIII.` at raw 15018, but the actual d.33 littera doesn't start until the **second** `DISTINCTIO XXXIII.` heading at raw 15062. Raw lines 15020–15061 are column-bleed continuation of the d.32 dubia: end of DUB. V's response (15020–15030), DUB. VI (15031–end of col-A and col-B start), DUB. VII (col-B). Reflowed to canonical order.

7 new apparatus entries appended (`[^16]`–`[^22]`) from the p. 867 footer (raw lines 15080–15089):
- `[^16]` Hoc dubium … B. Alberto, hic a. ult. (DUB. VI ref)
- `[^17]` Ioan. 14:10 textual variant (autem / in / enim; ipse adiectum)
- `[^18]` Ioan. 8:29 textual variant + Vat./cod. cc gloss
- `[^19]` cross-ref to d.30 q.2 in corp. + Thom./Richard. parallel
- `[^20]` Plures codd. *dicitur*
- `[^21]` codd. N P Q aa add *dicere*
- `[^22]` cross-ref a.2 q.1 ad 1 + sed/et Filii variant + Thom./Richard. parallel

No new `[?]` flags. Body in DUB. VI–VII reads cleanly in OCR; minor garbles silently corrected (`Quanclo` → `Quando`, `loanne` → `Ioanne`, `Ioannis decimo quarto` for the gospel ref, `surt` / spacing). The OCR `non vult%` glyph at line 15044 is a footnote marker (= `[^20]`), placed before the response body's `dicitur` variant; verified against the apparatus key `Plures codd. ut P Q X aa bb cum ed. 1 dicitur`.
