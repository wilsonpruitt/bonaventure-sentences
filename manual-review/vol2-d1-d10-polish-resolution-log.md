# Vol II d.1–d.10 decade polish-blocker — resolution log

Started 2026-05-22 (session 74), after Vol II d.10 reached 9/9 Tier-2. Three
passes per `CLAUDE.md` "Polish-blocker cadence". Hard gate before d.11.
PDF source: `raw/doctorisseraphic02bona.pdf`; offset `pdf = printed + 22`.

(Distinct from `d1-d10-polish-resolution-log.md`, which is the **Volume I** log.)

## Pass 2 — style/formatting audit (full corpus) — DONE 2026-05-22

Programmatic scan of all vol2 d.1–d.10 chunks: required Tier-2 frontmatter
fields, `## Latin/English/Apparatus` structure, apparatus marker pairing
(defs vs body anchors in both languages), page-break presence,
`transcription_status` prefix.

**Fixed (mechanical, committed):**
- `d10-littera` — English body was missing apparatus markers `[^6]`–`[^9]`
  (present in Latin body). Restored.
- `d1-p2-a1-q1` — English body was missing `[^2]` (`nunquam` / "never").
  Restored.

**Flagged for pass 1 (genuine dropped anchors — need 600 dpi eyes-on):**
- `d1-littera` `[^4]` — apparatus def `Codd. C T cum ed. 1 quousque` exists;
  body anchor never placed (documented in the chunk's own Notes: anchor lies
  inside heavily column-interleaved Cap. III text).
- `d9-divisio` `[^5]` — apparatus def `Cap. 30. n. 56.` (p.238 footer ¹) exists;
  body anchor missing from both Latin and English. Belongs at the *Hierarchia
  increata* definition on p.238.

**Formatting-drift finding (NOT skeletons — Tier-2 with older frontmatter):**
- `d3-p2-a2-q2`, `d3-p2-a3-q1`, `d3-p2-a3-q2`, `d3-p2-dubia` (all promoted
  2026-05-16) lack the `printed_pages` / `pdf_pages` / `source` / `has_apparatus`
  frontmatter fields and use no `<!-- page N -->` body comments. Content is
  complete and Tier-2. Page ranges are recoverable from each chunk's
  `transcription_status` ("printed pp. 122–124", "124–127", "127–128",
  "128–129"). To normalize: add the four fields + page-break comments.

## Pass 1 — `[?]` flag resolution (d.1–d.10) — PENDING

Resolve every inline `[?]` and every "low-confidence, confirm at 600 dpi"
note in d.1–d.10 via 600 dpi PDF eyes-on. For each: RESOLVE (with PDF
citation) or ACCEPT-ILLEGIBLE (with reason).

Inventory gathered 2026-05-22:
- `d1-littera` — `[^4]` anchor position; `[^22]` *Matth.* 22:[?] verse
  (OCR glyph `Ti\`, provisionally 30); the line-137 footer-4 anchor caveat.
- `d1-p1-a1-q1` — p.15 and p.17 `<!-- page -->` break positions approximate;
  `[^12]` Aristotle `text. 28`; `[^13]` Plato *Gorgias* `ed. Serrani tom. I.
  pag. 465`; three Scholion IV entries (S. Thom. *de Potent.*, Durand.,
  Dionys. Carth.) flagged for degraded right-column footer.
- `d1-p1-a1-q2` — `[^3]` (`mundus incepit` / `mutatus incipit`); `[^49]`
  (`potum` / `lutum` variant).
- `d2-p1-a1-q2` `[^9]`; `d2-p1-a1-q3` `[^7]` (`pag. 446` vs 440);
  `d2-p1-a1-q1` `[^18]` Greek accent; `d2-p1-a2-q2` p.66 Contra-1 clause;
  `d2-p1-a2-q3` `[^5]` (`Num. 37`); `d2-p1-dubia` `[^3]`/`[^4]` Psalm digits;
  `d3-p1-a1-q1` `[^15]` Damascene chapter. (All marked "non-blocking, sense
  secure" in their chunk Notes — confirm and clear.)
- `d9-a1-q1` SCHOLION II — `Petr. a Tar., hic a. 3. 1[?]` trailing numeral.
- `d9-a1-q8` `[^12]` — codex siglum (IA OCR `asi`/`aa`/`asn`, rendered `aa`).
- `d9-a1-q9` `[^8]` — Albert article `a. 8[?]` (OCR digit-mangle).
- `d10` — no `[?]` flags (all 9 chunks clean; one literal-citation note on
  `d10-littera` `[^1]` `tr. 3. 2. 5.`, reproduced verbatim, no flag).

## Pass 3 — cross-chunk boundary integrity sweep (d.1–d.10) — PENDING

For every mid-page chunk boundary in d.1–d.10, verify against 450 dpi PDF
column bands that no body text or footnote was lost at the seam (the OCR
cascade-merge failure mode — see `d9-divisio` s66 incident). d.10's nine
boundaries were each documented CLEAN at promotion time (see each d.10
chunk's `## Notes`); d.1–d.9 boundaries still need the sweep.
