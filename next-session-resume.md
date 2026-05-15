# Next session — Vol II d.1 Tier-2 continuation (session 12 — FINAL chunk of d.1)

Updated 2026-05-15 at close of session 11 (d.1 p2-a3-q2 done — ARTICLE III COMPLETE; only the closing dubia remains).

Head commit: `a8bbd42` — Vol II d.1 Tier-2 session 11 (p2-a3-q2, 20-entry apparatus, full-chunk PDF re-set, p.50→51 footer runover + p.51 cross-chunk split, no scholion). Resume commit follows.

## Status

- Vol I COMPLETE (411/411 Tier-2).
- Vol II auto-chunked: 464 skeletons across d.1–d.44.
- Vol II d.1 pars 1 **COMPLETE** (9/9 chunks Tier-2):
  - `d1-littera` (session 1)
  - `d1-p1-divisio` (session 1)
  - `d1-p1-a1-q1` *causal principle* (session 2)
  - `d1-p1-a1-q2` *world-eternity* (session 3)
  - `d1-p1-a2-q1` *Manichaean dualism* (session 4)
  - `d1-p1-a2-q2` *immediate vs. mediated creation* (session 4)
  - `d1-p1-a3-q1` *creation as mutation* (session 4)
  - `d1-p1-a3-q2` *creation as medium* (session 4) — incl. Erigena/Council-of-Sens history
  - `d1-p1-dubia` *DUB I–V* (session 4; **page-38 apparatus backfilled session 5**, entries 16–21)
- Vol II d.1 pars 2 **IN PROGRESS** (7/8 chunks Tier-2; ARTICLES I, II & III complete — only the closing dubia left):
  - `d1-p2-divisio` *Divisio textus + Tractatio quaestionum* (session 5)
  - `d1-p2-a1-q1` *Utrum a primo efficiente debuerit, vel potuerit esse rerum multitudo* (session 6) — 16-entry apparatus, PDF-verified
  - `d1-p2-a1-q2` *Utrum rerum universitas triplici differentia distinguatur* (session 7) — 23-entry apparatus, full-chunk PDF re-set (largest chunk in d.1)
  - `d1-p2-a2-q1` *Quis sit finis principalior rerum conditarum, divina gloria an utilitas nostra* (session 8) — ART. II opener absorbed (no separate a2-divisio chunk); 13-entry apparatus, full PDF re-set, cross-chunk footer splits on pp. 43 & 45
  - `d1-p2-a2-q2` *Utrum natura spiritualis dignitate naturae praecellat compositam* (session 9) — 13-entry apparatus, full PDF re-set, cross-chunk footer splits on pp. 45 & 47
  - `d1-p2-a3-q1` *Utrum Angelus et anima differant specie* (session 10) — ART. III opener absorbed; 12-entry apparatus, full PDF re-set (triplex-opinio Respondeo), p.47 cross-chunk split resolved a2-q2's [^12]
  - `d1-p2-a3-q2` *Quae sit differentia, per quam Angelus et anima differunt* (session 11) — 20-entry apparatus, full PDF re-set (triplex-modus Respondeo), p.50→51 footer runover + p.51 cross-chunk split, no scholion (a3-q1's covers it)
- Site build: 2 books, 873 chunks, **427 translated**.
- No deploy. Wilson's policy: hold until Vol II has meaningful Tier-2 work to show.

## Open [?] flags parked for d.10 polish-blocker

- `d1-p1-a3-q1` [^21] (*vel inceptio* anchor on p. 33) — footer entry was not separately resolvable in OCR before the SCHOLION block; mapped by content match. Resolution: 600 dpi PDF extract of p. 33 and eyes-on. See `manual-review/tier2-ambiguities-II-d1-p1-a3-q1.md`.
- `d1-p1-a3-q2` — page-mapping in the apparatus crosswalk is approximate where two-column OCR linearization is ambiguous; per-footer content match is faithful, but per-page sequence numbers may be off by one in places.
- `d1-p2-divisio` [^1] — the page-38 footer note-7 anchor: OCR shows an isolated `*` at *In prima*, possibly a divisio-diagram brace rather than a footnote marker. Also the page-38 note-6/7/8 boundary (where the footer splits between p1-dubia and the divisio) rests on two-column content match. See `manual-review/tier2-ambiguities-II-d1-p2-divisio.md`.
- `d1-p1-dubia` *in octavo* — stray `\` OCR glyph after *motorem primum, in octavo* (raw 3308); no distinct page-38 note, treated as covered by note 3's *Subaudi: libro Physicorum* ([^19]). Confirm at 600 dpi (printed p. 38 = PDF p. 60).
- `d1-p2-a1-q1` [^1] — *de Gen. et Corr.* locus reads *text. 56* in the 450 dpi PDF (OCR had *text. 36*); re-confirm at 600 dpi. [^7] cross-ref *tom. I pag. 171* taken from OCR (left edge cropped in the 450 dpi extract). Both low-confidence, non-blocking. See `manual-review/tier2-ambiguities-II-d1-p2-a1-q1.md`.
- `d1-p2-a1-q2` [^8] / [^20] — [^8] (*Supple: supremi*) body anchor sits ambiguously in the two-column Sed-contra-1 (*primae differentiae generis*); [^20] (*Codd. U Y supplent ordinatur*) `°` marker fell in the cascade-damaged *ordo in formis corporalibus* sentence, content-matched to *forma elementi*. Non-blocking; re-confirm at 600 dpi. (No separate per-chunk ambiguities file yet — fold into the d.10 log.)
- `d1-p2-a2-q1` [^1] / [^13] / [^7] — [^1] single anchor after *Magister* carries Lombard + Scripture + Augustine *de Doctr. christ.* (Quaracchi note 4); re-confirm marker not repeated after *Doctrina christiana*. [^13] (*Subaudi cum cod. N Deum* → reply 4 *in laudando*) rests on the two-column p.45-footer linearization at the a2-q1/a2-q2 boundary — re-confirm p.45 footer note 1 is not q2's opener. [^7] (*quodsi non frustra facit*) marker surfaced as a stray `S` glyph (raw 3756), content-matched to Aristot. *de Caelo* p.44 note 5. All non-blocking; fold into the d.10 log.
- `d1-p2-a2-q2` [^12] **RESOLVED (session 10)** / [^4] — [^12]: ~~reply 4's *infra* vs. a3-q1 Fundamentum 1~~ resolved by session-10's 450 dpi p.47 footer read: p.47 footer notes 1–2 (`Dist. II. a. 1. q. 1.`; `Garciones... Du Cange`) are the first two footer entries and both anchor a2-q2 reply 4 (*infra*, *garcioni*); a3-q1's notes begin at footer note 3. a2-q2 [^12] assignment stands; no backfill. [^4] (still open): the Augustine Contra-1 note runs p.45 footer → runover at head of p.46 footer left column; the `...XIV. de Trin. c. 14. n. 20. — Textus seq.... «Sed illa sola [creatura est imago Dei]...»` seam rests on two-column linearization. Non-blocking; fold into the d.10 log.
- `d1-p2-a3-q1` [^12] — the *rationale Angeli est intellectuale* marker (raw 4001, right col) sits in the heavily cascade-bled reply-2/3 region; content-matched to p.48 footer note 7 (`Secundum Dionys., de Div. Nom. c. 7. § 2.`). Secure on content; eyes-on with the other p.48 markers at 600 dpi. Non-blocking; fold into the d.10 log.
- `d1-p2-a3-q2` [^16] / [^20] — [^16]: the page-50-footer note 11 opener (`Nonnulli codd. ut V aa cum Vat. hic subiungunt perfi-`) continues at the head of the page-51 footer left column (`et autem (Vat. nam perficit) non mediante potentia...`); seam rests on two-column linearization at the chunk-internal p.50↔51 boundary. [^20]: chunk's terminal clause OCR-split *Et sic patent quae-* (p.51 L) | *sita* (p.51 R), marker on *sita*; reconstructed *quaesita*, anchored to p.51 footer note 4 (`Vide Scholion ad q. 1.`) — secure (terminal clause, terminal note before the dubia's `Hic c. 4.`). Both non-blocking; fold into the d.10 log.

## Next chunk: d1-p2-dubia — THE FINAL CHUNK OF DISTINCTION 1

**ARTICLES I, II & III are all complete.** The only remaining chunk in d.1 is the closing **`d1-p2-dubia`** (*Dubia circa litteram Magistri*). Finishing it closes distinction 1 (and all of pars 2) end-to-end.

- Boundaries (verified session 11 from raw): `DUBIA CIRCA LITTERAM MAGISTRI` text at **raw 4187**; `DUB. 1` head at **raw 4189**; running head `DIST. I. P. II. DUBIA.` at raw 4170 (so the dubia opens on printed **p. 51**, bottom). **End = raw 4263** (next semantic header `DISTINCTIO II.` — OCR-garbled `DISTmCTIO 11.` — at raw **4264**, which begins distinction 2; running head `DIST. II. P. II.` at raw 4309 = printed p. 53). Re-verify against raw and **grep for all `DUB.` headers** (raw 4189 = DUB. 1; count DUB. 2/3/… up to raw 4263) before chunking — the dubia is a multi-dubium block like `d1-p1-dubia`.
- Pages: dubia spans printed **pp. 51–52** (PDF 73–74, offset +22). Page-51's body top is already the dubia opening (seen in session 11's p.51 crops: *...tati quam aliis? Respondeo: Dicendum, quod causa in actu est...* and *...ritas, bonitate abstracta. Respondeo: Dicendum, quod bonitas est duplex in creatura...*). Budget a focused session + full 450 dpi PDF pass (pp. 51–52 = PDF 73–74; p.51 already extracted/cropped from session 11 under `/tmp/colcrop/vol2-p051-*` — re-extract if /tmp cleared).
- **Cross-chunk footer inheritance (already mapped in a3-q2's Notes):** the printed **p. 51 footer note 5 onward** anchor in *this* dubia — left-col note 5 `Hic c. 4.`; right-col notes 6–11 `Sequimur cod. bb addendo et...`; `Dist. 43.`; `Dist. 43. a. 2. q. 1. et 2.`; `De hoc dubio vide I. Sent. d. 1. dub. 13. seq...`; `Sive: «Quomodo substantiae in eo quod sint, bona sint, cum non sint substantialia bona».`; `Vat. cum uno alteroque cod. novum esse.` p.51 footer notes 1–4 belong to a3-q2 (reply 4) and are its [^17]–[^20] — do **not** re-capture. Start the dubia's apparatus crosswalk from the p.51 footer's **note 5**.
- After this chunk, **distinction 1 is fully Tier-2 (pars 1 + pars 2 complete)**. Next would be **DISTINCTIO II** (raw 4264+, `DISTmCTIO 11.` OCR garble — chunker already tolerates per CLAUDE.md) — start a fresh d.2 re-chunk pass; the auto-chunker line ranges for d.2 are stale and must be re-derived from raw semantic headers as always.

`tools/colcrop.py` (committed session 8) is the PIL column-band cropper: `python3.11 tools/colcrop.py vol2 <printed-page> [split_x=1660] [n_bands=3] [scale=1.8]` → `/tmp/colcrop/vol2-pNNN-{L,R}-{0..n}.png`. Read L column top→bottom then R column; footer bands are the bottom band of each column.

### Apparatus / PDF discipline (carry forward — proven sessions 6–7)

Session 7 (q2, ~2160 words, pp. 41–43) confirmed: for any large quaestio the IA OCR cascade-fragments the Respondeo and *all* page-footers. The reliable workflow: `python3.11 tools/extract-pages.py --volume vol2 --pages <printed> --dpi 450`, then a PIL helper that crops each page into left/right column bands (top+bottom) plus footer bands, `resize` ~1.7–2.2×, and Read each crop. Reflow column-by-column (whole left column of a page, then whole right). Footnote numbering **restarts every printed page** — keep a per-page→chunk crosswalk and document it in `## Notes`. Page-footer split convention (notes follow body anchors, not the chunk that physically holds the footer text) still applies — always check the last page's footer vs. the next chunk.

### Workflow per CLAUDE.md (locked-in)

1. Find OCR line range; verify boundaries against raw.
2. Latin verbatim from raw OCR, NOT from PDF.
3. `[^N]` anchors at OCR positions, not end-of-clause.
4. English literal, paragraph-for-paragraph.
5. Apparatus walked page-by-page from raw OCR footers.
6. Log `[?]` flags inline; resolve at decade polish-blocker (d.10).
7. `node scripts/build-content.mjs` smoke-test before commit.

### Lessons confirmed by sessions 2–4 (carry forward)

- **Trim marginal glosses aggressively** (`Ad oppositum`, `Fundamenta`, `Conclusio`, `Solutio`, `Distinctio`, `Notandum`, `Triplex productio`, `Determinatio trium productionum`, `Epilogus`, `Dupliciter relatio`, `Aliter`, `Eliditur error 1/2/3`, etc.). Don't render them as headings or text.
- **Apparatus marker renumbering is fine** — chunk-internal sequence 1–N is more readable than Quaracchi's per-page restart. Document the page-by-page crosswalk in `## Notes`.
- **Page-break markers** go in the chunk at the printed-page running-head or page-number boundary; if OCR ate a running head, mark `<!-- page N -->` position as `[?]` rather than guessing.
- **Don't try to resolve subtle OCR ambiguities eyes-on-OCR alone** — the d.10 polish pass + 600dpi PDF clears them in seconds.
- **Watch for column-linearization page-spillover** — session 4 caught a "missing" page-30 footer at the top of the next chunk's OCR window. Always glance at the next chunk's first ~20 lines if a footer reference seems short.
- **Cross-chunk footer split is now a confirmed recurring pattern (session 5, page 38).** When a printed page's footer block sits at a chunk boundary, its notes split by *body anchor*, not by which chunk physically contains the footer text. Session 5: page-38 footer notes 1–6 anchored in `d1-p1-dubia`'s page-38 body (DUB III tail/IV/V) but that chunk had only captured pp. 36–37 footer; notes 7–8 anchored in `d1-p2-divisio`. **Before promoting any chunk, verify the prior chunk's last printed page footer was fully captured for the body it holds on that page.** Same convention as `d1-p1-divisio` (notes 1–4 in next chunk's footer). Backfilling a committed Tier-2 chunk is acceptable and expected when this is found — renumber its sequence continuously and document in its Notes + `transcription_status`.
- **Vol II audit scripts not yet implemented**: `audit-paraphrase.py`, `audit-headers.py`, `audit-apparatus-count.py` still vol1-only. Manual confidence required for vol2 chunk quality until those scripts are extended. Smoke build (`build-content.mjs`) is the only mechanical check.

### Pace

- Session 4: 5 short-to-medium chunks in one extended session when apparatus is OCR-clean.
- Session 5: 1 divisio chunk + a cross-chunk apparatus backfill (page-38 footer found mis-split). Cross-chunk corrections cost ~1 chunk-equivalent of effort — budget for them when a chunk boundary falls inside a printed page.
- Session 6: `d1-p2-a1-q1` solo focused session — dense ~1190-word quaestio (pp. 39–40), full 450 dpi PDF pass.
- Session 7: `d1-p2-a1-q2` solo focused session — **largest chunk in d.1** (~2160 words, pp. 41–43, 23 apparatus entries), entire chunk re-set against PDF. A ~2000-word quaestio with heavy cascade damage is a full session on its own; do not bundle.
- Session 8: `d1-p2-a2-q1` solo focused session — ~1300-word quaestio (pp. 43–45, 13 apparatus entries) + re-chunk decision (absorb ART. II opener) + two cross-chunk footer splits (pp. 43, 45) verified against a1-q2's committed crosswalk. Re-chunk + dual cross-chunk split adds ~½ chunk-equivalent over a clean mid-size quaestio. Added `tools/colcrop.py`.
- Session 9: `d1-p2-a2-q2` solo focused session — ~870-word quaestio (pp. 45–47, 13 apparatus entries), full PDF re-set, two cross-chunk footer splits (p.45 note 1 → a2-q1; p.47 notes 3–7 → a3-q1) + a page-45→46 footnote runover folded into [^4]. Mid-size quaestio with two clean cross-chunk splits ≈ one focused session. Two q2-style chunks (a2-q1 + a2-q2) fit in a single working stretch when each is ~900–1300 words and cascade damage is footer-localized — but the dual cross-chunk bookkeeping is the real cost, not word count.
- Session 10: `d1-p2-a3-q1` solo focused session — ~1060-word quaestio (pp. 47–49, 12 apparatus entries) with a *triplex-opinio* Respondeo + three-part scholion, fully two-column-shattered; full 450 dpi PDF re-set. The p.47 cross-chunk footer split (notes 1–2 → a2-q2, 3–7 → a3-q1) was the prior session's open [?] — reading the footer in source order both populated a3-q1 and **retired a2-q2's [^12] flag** in the same pass. Resolving a downstream chunk's flag while building the next chunk is efficient — read shared footers in printed order once and assign both directions.
- Session 11: `d1-p2-a3-q2` solo focused session — ~1330-word quaestio (pp. 49–51, **20 apparatus entries** — the largest apparatus count in d.1 pars 2) with a *triplex-modus* Respondeo, fully two-column-shattered; full 450 dpi PDF re-set. No scholion (a3-q1's covers it — saved a translation pass; always check the prior chunk's scholion for *«pro quaest. seq.»* before assuming a missing scholion is an error). Three sequential cascade sessions (a2-q1→a2-q2→a3-q1→a3-q2) confirm the steady-state cadence: one heavily-damaged ~1000–1300-word quaestio per focused session, ~12–20 apparatus entries, the cross-chunk footer bookkeeping (not word count) being the dominant cost.

### Remaining d.1 pars 2 chunks (in order)

Pars II structure (from the p2 divisio's *Tractatio quaestionum*): three articles — ART. I *de rerum distinctione* (2 q), ART. II *de rerum ordine ad finem et ad invicem* (2 q), ART. III *de differentia Angeli et animae* — plus a closing dubia.

| Chunk | Lines | Notes |
|---|---|---|
| ~~d1-p2-divisio~~ | 3321–3378 | ✅ session 5 |
| ~~d1-p2-a1-q1~~ | 3382–3502 | ✅ session 6 (16-entry apparatus, PDF) |
| ~~d1-p2-a1-q2~~ | 3503–3670 | ✅ session 7 (23-entry apparatus, full PDF re-set) |
| ~~d1-p2-a2-q1~~ | 3672–3817 | ✅ session 8 (13-entry apparatus, full PDF re-set; ART. II opener absorbed, pp. 43/45 cross-chunk footer splits) |
| ~~d1-p2-a2-q2~~ | 3818–3924 | ✅ session 9 (13-entry apparatus, full PDF re-set; pp. 45/47 cross-chunk footer splits + p.45→46 note runover) |
| ~~d1-p2-a3-q1~~ | 3925–4048 | ✅ session 10 (12-entry apparatus, full PDF re-set; ART. III opener absorbed, p.47 split resolved a2-q2 [^12]) |
| ~~d1-p2-a3-q2~~ | 4049–4186 | ✅ session 11 (20-entry apparatus, full PDF re-set; p.50→51 footer runover, p.51 cross-chunk split, no scholion) |
| d1-p2-dubia | 4187–4263 | **next — FINAL chunk of d.1** — `DUBIA CIRCA LITTERAM MAGISTRI` raw 4187, `DUB. 1` 4189; ends raw 4263 (`DISTINCTIO II.` = `DISTmCTIO 11.` raw 4264). Pages 51–52. Inherits p.51 footer notes 5+ |

ARTS. I, II & III all done. Remaining: **the closing dubia only** (raw 4187–4263) — one chunk to finish distinction 1 and all of pars 2 end-to-end. Boundaries derived (dubia = 4187–4263; d.2 begins `DISTmCTIO 11.` raw 4264); still re-verify against raw and count the `DUB.` headers before chunking. 1 more focused session closes d.1; then the work moves to **distinction 2** (fresh re-chunk pass — auto-chunker ranges stale as always).

## Polish-blocker (after d.10 ships)

1. `[?]` flag resolution — Vol II d.1–d.10 only.
2. Style/formatting audit — full corpus (Vol I + Vol II).
3. Resolution log at `manual-review/II-d1-d10-polish-resolution-log.md`.

## Tools cheat sheet

```bash
# Inspect raw chunk range
awk 'NR>={start} && NR<={end}' raw/bonaventure_vol2_raw.txt

# Vol II offset: pdf_page = printed + 22
python3.11 tools/extract-pages.py --volume vol2 --pages {printed_pages}

# Chunker warnings
python3.11 tools/auto-chunk-volume.py 2 --dry-run 2>&1 | awk '/WARNINGS/,/Chunk list/'

# Smoke build
cd site && node scripts/build-content.mjs
```

Vol II offsets: see CLAUDE.md table (`pdf = printed + 22`). No deploy until meaningful Vol II Tier-2 work to show.
