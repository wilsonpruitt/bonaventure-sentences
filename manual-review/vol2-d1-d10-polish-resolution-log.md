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
- **NORMALIZED 2026-05-22.** All four chunks now carry `printed_pages`,
  `pdf_pages`, `source`, `has_scholion`, `has_apparatus` and `<!-- page N -->`
  comments in both the Latin and English bodies. Page breaks placed at the
  paragraph boundary before the first paragraph beginning on each page
  (verified against 600 dpi p.122–125 tops and 450 dpi p.126–129 tops);
  where a page begins mid-paragraph the comment sits before the next
  paragraph start, the standard corpus approximation. Build re-verified
  (541 translated). `has_scholion`: a2-q2/a3-q1/a3-q2 true, dubia false.

## Pass 1 — `[?]` flag resolution (d.1–d.10) — IN PROGRESS

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

### Resolutions

**d.3 (2026-05-22)** — 600 dpi extract of printed pp.122–125 (`p-{122..125}.png`,
4486×6850). All four d.3 low-confidence items RESOLVED, no content change:
- `d3-p2-a2-q2` `[^1]` — RESOLVED. p.122 footer note 1 reads
  `Cap. 7. § 2. et c. 4. § 2. 22; c. 5. § 8.` — the `2. 22` is a list of two
  sections (§§ 2, 22) of Dionysius *de Div. Nom.* c. 4 with the `§` distributed,
  standard Quaracchi style. Rendering faithful.
- `d3-p2-a2-q2` `[^14]` — RESOLVED. p.123 footer note 6 reads in full
  `August., in Ioan. tract. 1. n. 19: Quomodo homo positus in sole caecus,
  praesens est illi sol, sed ipse soli absens est; sic omnis stultus, omnis
  iniquus, omnis impius caecus est corde etc. — Cod. aa ut lux caeco.` —
  matches the chunk verbatim.
- `d3-p2-a3-q1` `[^1]` — RESOLVED. p.124 footer note 3 reads
  `Cfr. etiam Epist. 11, ubi n. 5.` — `Epist. 11` (arabic 11) confirmed.
- `d3-p2-a3-q1` `[^5]` — RESOLVED. p.125 footer note 2 reads
  `Alluditur ad Thren. 3, 25:` — `25` confirmed (IA OCR `3, 23` was the
  digit-mangle); matches Vulgate Lam 3:25 and the rendered text.
- `d3-p1-a1-q1` `[^15]` (Damascene chapter, from the original inventory) —
  still PENDING; not yet swept.

**d.9 (2026-05-22)** — 600 dpi extract of printed pp.238, 243, 256, 257. All
four d.9 items resolved:
- `d9-a1-q8` `[^12]` — RESOLVED. p.256 footer 3 reads `Cod. aa subiungit in
  Deum` at 600 dpi; siglum `aa` confirmed. `[?]` dropped, no content change.
- `d9-a1-q9` `[^8]` — RESOLVED **with correction**. p.257 footer 6 reads
  `B. Albert., hic a. 5. ad ult.` — the OCR `S.` mangled `5`, not `8`. The
  chunk's provisional `a. 8` was wrong; corrected to `a. 5` in the Latin and
  English apparatus. `[?]` dropped.
- `d9-a1-q1` SCHOLION II — RESOLVED **with correction**. p.243 R-col scholion
  reads `subiungimus Petr. a Tar., hic a. 3. 4.` — trailing numeral is `4`,
  not the provisional `1`. Corrected in the Latin and English scholion.
  `[?]` dropped.
- `d9-divisio` `[^5]` (genuine dropped anchor, from pass 2) — RESOLVED. The
  body anchor was missing in both languages though the apparatus def
  (`Cap. 30. n. 56.`) existed. 600 dpi p.238 shows superscript ¹ after
  `de Vera Religione` in *Definitio I*; `Cap. 30. n. 56.` is the Augustine
  *de Vera Religione* locus. `[^5]` anchor placed in Latin and English.
  d.9 guard-rail audits re-run clean; build 541 translated.

**d.1 (2026-05-22) — IN PROGRESS.** 600 dpi extract of printed pp.11, 12, 13.
- `d1-littera` `[^22]` `Matth. 22,[?]` — the verse number is **37**, confirmed
  on the 600 dpi p.13 footer note 3 (`Infra respicitur Matth. 22, 37; et
  I. Cor. 13, 12.`). NOT 30 as the editorial best-guess supposed.
- **DEFECT FOUND — `d1-littera` p.13 apparatus is mis-numbered; needs a
  careful re-walk before `[^22]` can be cleanly closed.** The 600 dpi p.13
  footer has **8 numbered notes**, not the 7 the chunk Notes claim. Printed
  footer (verified at 600 dpi):
  1. `Cfr. August., Enchirid. c. 29; XXII. de Civ. Dei, c. 1.`
  2. `Vat. cum nonnullis edd. videatur.`
  3. `Cfr. I. Sent. d. XL. c. 4. Infra respicitur Matth. 22, 37; et I. Cor. 13, 12.`
  4. `II. Cor. 5, 4.`
  5. `Cod. C perstiterunt, codd. A D cum edd. 1, 8 perstiter[u/a]nt; subinde Vat. perperam sublimetur, omnibus codd. et edd. refragantibus.`
  6. `Vat. cum nonnullis edd. componens.`
  7. `Libr. de Spiritu et anima, c. 14. (inter opera August.), et iterum Hugo a S. Vict., l. de Sacram. p. VI. c. 1.`
  8. `Sola Vat. omittit verba et de rationali et non rationali, primo.`
  The chunk currently has only 7 p.13 entries `[^20]`–`[^26]`, because
  `[^22]` **merged printed notes 3 + 4** into one entry (and rendered the
  II Cor verse as `5, 1` — should be `5, 4`). Printed note 4 (`II. Cor.
  5, 4.`) needs its **own entry**; `[^23]`–`[^26]` then shift +1 to
  `[^24]`–`[^27]`, and their body anchors must move with them. Additional
  text-fidelity fixes the re-walk should make: `[^23]` (current) reads
  `edd. 1, H` (printed `edd. 1, 8`) and `sublimatur` (printed `sublimetur`);
  `[^25]` (current) reads *de Spiritu et anima* `c. 11` (printed `c. 14`).
  This is a numbering/anchor repair, deliberately deferred from this pass
  rather than half-fixed — the `[?]` on `[^22]` stays until it is done.
- `d1-littera` `[^4]` anchor + `[^15]` Hugh ref — still PENDING.
- `d1-p1-a1-q1`, `d1-p1-a1-q2`, `d2-*` — still PENDING.

## Pass 3 — cross-chunk boundary integrity sweep (d.1–d.10) — PENDING

For every mid-page chunk boundary in d.1–d.10, verify against 450 dpi PDF
column bands that no body text or footnote was lost at the seam (the OCR
cascade-merge failure mode — see `d9-divisio` s66 incident). d.10's nine
boundaries were each documented CLEAN at promotion time (see each d.10
chunk's `## Notes`); d.1–d.9 boundaries still need the sweep.
