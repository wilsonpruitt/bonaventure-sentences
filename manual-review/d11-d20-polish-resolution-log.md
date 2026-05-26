# Vol II d.11–d.20 decade polish-blocker — resolution log

Started 2026-05-25 (session continuation), after Vol II d.20 reached 9/9 Tier-2
(d.1–d.20 = 228 chunks promoted; build 639 translated / 879 quaestio routes).
Three passes per `CLAUDE.md` "Polish-blocker cadence". Hard gate before d.21
dispatch. PDF source: `raw/doctorisseraphic02bona.pdf`; offset `pdf = printed + 22`.

(Distinct from `vol2-d1-d10-polish-resolution-log.md`, which closed the prior
Vol II decade on 2026-05-22.)

## Inventory — Pass 1 inline `[?]` flags (d.11–d.20)

Gathered 2026-05-25 by grep filtering out backticks-meta + "no `[?]` flags"
declarations from each chunk's `transcription_status` / `## Notes`.

| Chunk | Page(s) | Flag | Resolution |
|---|---|---|---|
| `d14-p1-a1-q1` | p.338 | Scholion II — `Alex. Hal., S. p. II. q. 50. m. 1.[?]` (Latin+English) | ✓ RESOLVED 2026-05-25 — no stray glyph; column-edge artifact at 450 dpi |
| `d14-p1-a2-q1` | p.341 | (a) in-line position of marker `[^2]` in arg. 2 (no printed ² glyph at 450 dpi) | ✓ ACCEPT-ILLEGIBLE 2026-05-25 — confirmed at 600 dpi no printed `²` in body; Quaracchi attached cross-ref implicitly to *motus circularis* sub-arg; editorial placement at clause-end retained |
| `d14-p1-a2-q1` | p.342 R-2 | (b) Mediavilla codex sigil `F1 (T a secunda manu)` — parenthesis faint | ✓ RESOLVED 2026-05-25 — parenthesis unambiguous at 600 dpi `p-342-r600.png` full-width footer crop |
| `d14-p1-a2-q2` | p.343 | in-line position of marker `[^9]` within *Ad opp. 6* (faint ⁹ at clause-end) | ✓ RESOLVED 2026-05-25 — printed `⁹` unambiguous at 600 dpi `p-343-r600.png` (R-top crop): *quod nullo modo concedi potest⁹.* |
| `d14-p1-a3-q1` | p.346 | Scholion I phrase *Hucusque proxime accedunt* | ✓ RESOLVED-VACUOUS 2026-05-25 — phrase not present in printed Scholion I (600 dpi) nor in raw OCR for chunk's line range; flag was a stray transcription_status probe, dropped |
| `d14-p1-a3-q2` | p.350 | `[^25]` *et per hoc etiam… litteram* anchor placement (Ad 6) | ✓ RESOLVED 2026-05-25 — at 600 dpi `p-350-r600.png` (L-foot crop) footer reads *et per hoc etiam... littera.* (not *litteram*); apparatus corrected La+En; body anchor at *in littera[^25]* confirmed |
| `d14-p1-littera` | pp.333–334 | three marginal labels *Dubium 3.* / *Dubium 1.* (×3, body inline) | ✓ RESOLVED 2026-05-25 — 600 dpi confirms Pars II Dubium numbering is continuous (Cap. VII=1/2, Cap. IX=3, Cap. X=4); Cap. IX *Dubium 3.* real (Lat+Eng); Cap. X corrected from *Dubium 1.* → *Dubium 4.* (Lat+Eng) |
| `d18-a2-q2` | p.450 | Conclusio `Damasceni[^23] [?]` — second-anchor question | ✓ RESOLVED 2026-05-25 — `[^23]` covers Greg.Naz.+Damasceni+Augustini *de Spiritu*; stray `[?]` was OCR spacing artifact, removed |
| `d18-a2-q2` | p.451 | `²` on *absque dolore* — stray vs real anchor | ✓ RESOLVED 2026-05-25 — `²` is real at 600 dpi; p.451 L-2 footer ² (*Cfr. infra d. 19*) reclaimed as new `[^25]` (was dropped during chunking, not held by d18-a2-q3) |
| `d20-a1-q4` | p.482 | `[^1]` anchor on *intelligibile* / *intendetur* variant | ✓ RESOLVED 2026-05-25 — 600 dpi `p-482-r600.png` footer ¹ reads *Non pauci codd. cum edd. 3, 4, 5 intendetur*; variant substitutes for *intelligibile* at *Respondeo* opener; existing anchor placement at *intelligibile[^1]* correct; apparatus edd. corrected 2,3,4 → 3,4,5; `[?]` removed |

600 dpi crops generated 2026-05-25 in `raw/vision/vol2/r600/p-{N}-r600.png` for
pp. 333, 334, 335, 337, 338, 341, 342, 343, 346, 350, 451, 482.

## Pass 1 — `[?]` flag resolution at 600 dpi

In progress — see table above.

### Session 2026-05-25 (PM)

**3 flags closed across 2 chunks (d14-p1-a1-q1, d18-a2-q2). 6 flags pending across 6 chunks.**

- **d14-p1-a1-q1, Scholion II.** 600 dpi (`/tmp/p338-scholion-seam.png`) shows `Alex. Hal., S. p. II. q. 50. m. 1.` ending the line cleanly with no stray glyph; the em-dash to `Scot., Report. hic q. 1. n. 16.` begins the next visual line. The OCR-flagged "extra glyph" was a column-edge artifact at 450 dpi. `[?]` removed from Latin (line 103) and English (line 184). Chunk `## Notes` updated.

- **d18-a2-q2 (×2).** 600 dpi confirmed `²` is real on *absque dolore* (`/tmp/p451-R-top.png`); reading (a) of the Notes block is correct. The p.451 L-2 footer ² (*Cfr. infra d. 19. a. 2. q. 1, et a. 3. q. 1, ubi hoc explicatur*) belongs in **this** chunk as the body anchor for *absque dolore². Recovered as new [^25] (Latin + English). Verified d18-a2-q3 apparatus does NOT hold this footer (begins at [^1] = *Vers. 26 seq.* = p.451 L-2 footer ³), so this is a chunking-time drop, not a hand-off transfer. Separately, the `Damasceni[^23] [?]` in the Conclusio: the existing [^23] explicitly covers Damascenus + Greg. Naz. + Augustini *de Spiritu et anima* c. 13 (continuation onto p.450 R-bot includes *Verba auctoris libri de Spiritu et anima, c. 13. sunt:…*); no second anchor needed. The stray `[?]` was OCR spacing noise. Removed. transcription_status updated 22 → 25 entries.

**Pass 3 follow-up identified in this session:** d18-a2-q2 is missing the p.450 R-2 footer block ⁶/⁷/⁸ (*Haec ex Gregorio sumta solutio iam supra d. 12*; *Codd. Y oa propter*; *Cfr. supra pag. 20, nota 7*) — body anchors never placed during chunking. Triage in Pass 3 cross-chunk boundary sweep.

Build verified: 2 books / 879 questions / 639 translated.

600 dpi crops added this session: p.450 (originally not pre-cached) at `raw/vision/vol2/r600/p-450-r600.png`.

### Remaining pending
None. Pass 1 CLOSED 2026-05-25.

### Session 2026-05-25 (later PM) — 5 d.14 flags closed across 5 chunks
- d14-p1-a2-q1 (×2): [^2] inline ACCEPT-ILLEGIBLE + Mediavilla sigil parenthesis RESOLVED
- d14-p1-a2-q2: [^9] inline ⁹ RESOLVED (printed superscript present at 600 dpi)
- d14-p1-a3-q1: *Hucusque proxime accedunt* RESOLVED-VACUOUS (not in body/raw)
- d14-p1-a3-q2: [^25] RESOLVED (litteram → littera correction; anchor confirmed)
- d14-p1-littera: 3 Dubium labels RESOLVED (Pars II continuous numbering; Cap. X corrected 1→4)

Pass 1 essentially closed; only d20-a1-q4 remains (deferred to its own dispatch).

### Session 2026-05-25 (final) — d20-a1-q4 closed; Pass 1 CLOSED

- **d20-a1-q4, p.482 [^1].** 600 dpi `raw/vision/vol2/r600/p-482-r600.png` shows footer ¹ as *Non pauci codd. cum edd. 3, 4, 5 intendetur*. The manuscript variant *intendetur* (future passive of *intendere*) substitutes for the printed *intelligibile* at the *Respondeo* opener (*quod quidem non videtur esse intelligibile*); the prior anchor placement at *intelligibile[^1]* is therefore correct. Apparatus corrected (edd. 2,3,4 → 3,4,5; gloss + `[?]` markers removed in both La and En). Chunk `## Notes` updated; transcription_status amended.

**Pass 1 (d.11–d.20) CLOSED 2026-05-25.** Next blocker: Pass 2 (style/formatting audit, full corpus per CLAUDE.md "Polish-blocker cadence" §2).

## Pass 2 — style/formatting audit (d.1–d.20)

Bucket A+B closed 2026-05-25 at commit `3276b94` (15 `en_indent_mix` normalized to 5-space; 5 `missing_frontmatter` chunks backfilled). ~21 Bucket-C eyes-on FLAGs remained.

### Bucket-C session 2026-05-26 — `d27-p1-a1-q2` `orphan_app_defs` (23 entries) RESOLVED-PADDING

- **Flag:** `vol1/bon-sent-I-d27-p1-a1-q2.md` apparatus defs `[^26]–[^48]` had no matching body anchors in either Latin or English (23 consecutive orphans).
- **Diagnosis:** *not* Case 1 (body truncation), *not* Case 2 (cascade-merge splice), *not* Case 3 (anchor-stripping). The chunk body is complete on pp. 468–474 (closes mid-Anecdota II at the `cod. G` terminator, matching the printed text); pp. 472–474 are the Anecdota material with no Quaracchi footers needing body anchors. `[^26]–[^48]` were a **duplicate-padding apparatus block** added by the 2026-05-09 Wave 9b rebuild to satisfy a per-page footer count target. Every padded entry restated lemma-variant content already present inline within `[^1]–[^25]` — e.g. `[^26]` (Vat. *eaedem proprietates*) is in `[^1]`; `[^27]`/`[^28]`/`[^29]`/`[^30]`/`[^31]` are all in `[^1]`; `[^36]` is in `[^13]`; `[^37]` is in `[^14]`; `[^41]` is in `[^17]`; `[^42]`/`[^43]`/`[^46]` are in `[^19]`; `[^45]` is in `[^20]`; `[^48]` was self-annotated "duplicated here to bring the per-page footer count for p. 472 to its full five-entry total". The `[^47]` `[?]`-flagged "OCR truncated" stub was likewise spurious (no missing body anchor on p. 471 — the page-foot ¹¹ variant content is already covered by `[^19]`/`[^20]`).
- **Action:** removed `[^26]–[^48]` and the prefatory `>` "Page-foot lemma-variant entries" note; chunk apparatus returns to its faithful 25 body-anchored entries `[^1]–[^25]`. Backup at `_backup-d27-p1-a1-q2-pre-rebuild-20260526/`. Frontmatter `transcription_status` rewritten; `## Notes` paragraph added documenting the disposition. No `[?]` flags placed (the chunk's two remaining `[?]` markers — `valuabiliter[?]` and `inventurus[?]` — are pre-existing OCR-garble flags in the Anecdota II text, untouched by this pass).
- **Audits:** paraphrase + headers + apparatus-count clean for d.27; style-formatting re-run drops `d27-p1-a1-q2` from the `orphan_app_defs` bucket. Build smoke-tested green: 879 routes / 639 translated / 2 books.

### Bucket-C grouped dispatch 2026-05-26 — 14 of 20 remaining FLAGs RESOLVED, 6 STOP-FLAG-DEFERRED

**Group 1 (orphan_app_defs) — 7 of 12 closed via Case-4 padding-delete; 5 STOP-FLAG-DEFERRED:**

- `vol1/bon-sent-I-d43-a1-q2.md` [^2] — Case-4 DELETED. Editorial gloss "Intellige: in Bon. Cfr. August., VI. et VII. *de Trin.* c. I." duplicates the cross-reference subsumed by [^6] (Aug. *de Trin.* on body's "octavo de Trinitate[^6]"). Lemma overlap on the same body referent. Backup at `_backup-d43-a1-q2-pre-fix-20260526/`.
- `vol1/bon-sent-I-d8-p1-a1-q2.md` [^35] — Case-4 DELETED. Trailing orphan beyond body's [^34] max anchor (def-max=35, body-max=34). Wave-9b padding extending count past body. Aristotelian *Libr. I. c. 8.* citation referent already covered by adjacent [^34] body lemma. Backup in `_backup-pass2-bucket-c-20260526/`.
- `vol2/bon-sent-II-d13-a2-q2.md` [^24] — Case-4 DELETED. Trailing orphan (def-max=24, body-max=23). Aristot. *VIII Metaph.* cross-ref padding. Backup as above.
- `vol2/bon-sent-II-d13-a3-q1.md` [^25] — Case-4 DELETED. Trailing orphan (def-max=25, body-max=24). Aristot. text 74 Democritus *vacuo facto* padding. Backup as above.
- `vol2/bon-sent-II-d13-a3-q2.md` [^23] — Case-4 DELETED. Trailing orphan (def-max=23, body-max=22). *De Div. Nom.* c. 2 § 4 *lampadum* padding. Backup as above.
- `vol2/bon-sent-II-d17-a1-q2.md` [^24] — Case-4 DELETED. Trailing orphan (def-max=24, body-max=23). *cod. cc et ed. 1 bene additur autem* variant padding. Backup as above.
- `vol1/bon-sent-I-d1-a2-q1.md` [^7] + [^8] — Case-4 DELETED. Near-identical duplicates ("Vide lit. Magistri, c. 2." / "Cfr. lit. Magistri, c. 2.") subsumed by [^19] ("De tribus sequentibus definitionibus fruitionis... vide hic lit. Magistri, c. 2. 3."). Wave-9b padding. Backup as above.
- `vol1/bon-sent-I-d1-a2-q1.md` [^3], [^4], [^5], [^6] — **STOP-FLAG-DEFERRED**. Mid-range orphans (within body anchor span [^1]–[^31]); each contains substantive Vat./codd. textual variants that may belong at specific body lemmas not currently anchored. Distinguishing padding from missing-anchor needs 600 dpi PDF eyes-on of pp. 41–43 footer blocks. Beyond this dispatch's per-chunk time cap.
- `vol1/bon-sent-I-d9-dubia.md` [^54] — **STOP-FLAG-DEFERRED**. Mid-range orphan; "Vat. contra plurimos codd. et ed. 1 minus bene *hoc*" generic variant. Needs PDF walk to find the specific *hoc* body lemma. Beyond cap.
- `vol2/bon-sent-II-d11-a2-q3.md` [^2], [^3], [^4] — **STOP-FLAG-DEFERRED**. Per the chunk's own `## Notes`: p.286 footers nn. 4–7 are carried as [^1]–[^4]. Body has [^1] (3 Kings 20) and jumps to [^5] (Num 25 Vers. 3) — three middle anchors never placed. Defs are substantive (cod V *accidentale*/Vat *creatum*; "In quaest. seq."; "Vers. 39"). Genuine Case-3 anchor-stripping requiring p. 286 column-band PDF walk to place [^2]/[^3]/[^4] at the correct lemmas. Beyond cap.
- `vol2/bon-sent-II-d14-p1-a2-q1.md` [^4], [^5], [^6] — **STOP-FLAG-DEFERRED**. Mid-range orphans; defs are substantive Chalcidius/Aristot. citations plus "Vide scholion ad praecedentem quaest." Case-3 anchor-placement requiring PDF walk.
- `vol2/bon-sent-II-d18-littera.md` [^15] — **STOP-FLAG-DEFERRED**. Mid-range orphan; "Gennadius, c. 14" + *cum corporibus*/*in corporibus* variant. Needs PDF walk to find the *cum corporibus* body lemma.
- `vol2/bon-sent-II-d19-a2-q2.md` [^9] — **STOP-FLAG-DEFERRED**. Mid-range orphan; "Psalm 48, 13" + *mortis*/*mortalitatis* variant. Needs PDF walk for the *mortis* body lemma.

**Group 2 (anchor_only_la) — all 5 RESOLVED via English-side anchor mirror:**

- `vol1/bon-sent-I-d42-a1-q3.md` [^24] — RESOLVED. Latin body has *unquam[^24]* in the *Praeterea*-block ("…quod illud quod nunquam est praesens, unquam[^24] sit praesens"). Mirrored into English at "what is never present should ever[^24] be present".
- `vol1/bon-sent-I-d45-dubia.md` [^25] + `body_anchor_no_def_la` [^25] — RESOLVED-FALSE-POSITIVE. Both flags were caused by the prefatory `>` apparatus note saying "this chunk renumbers them sequentially [^1]–[^25] across the four printed pages". The footnote-syntax bracket in the prose was parsed as a body anchor by the audit. Rewrote the prose to "1 through 21" (true def count). No actual body anchor [^25] exists in the chunk.
- `vol2/bon-sent-II-d13-a2-q2.md` [^20] — RESOLVED. Latin body has *forma ultimo[^20] completiva*; mirrored into English at "the *ultimately completive*[^20] form is more noble".
- `vol2/bon-sent-II-d15-a2-q2.md` [^9] — RESOLVED. Latin body has *completum[^9]* at *Secundus ordo* / "a minus completo perveniatur ad magis completum[^9]"; English had [^9] missing and the *next* [^10] mis-placed at "more complete" instead of "more composite". Re-anchored: "to the more complete[^9]" (was [^10]); the other [^10] at "more composite a thing is[^10]" remains correct.

**Group 3 (specials) — all 3 RESOLVED:**

- `vol2/bon-sent-II-d12-a2-q2.md` missing_frontmatter — RESOLVED. Chunk diagnosed as fully real Tier-2 (Latin body + English body + Apparatus 13 entries + Scholion I + Notes block all present and parallel). Backfilled 6 missing keys: `title_la`, `title_en`, `printed_pages: [304, 305]`, `pdf_pages: [326, 327]` (Vol II offset +22), `source: "S. Bonaventurae, Opera Omnia, Tomus II (Quaracchi, 1885), pp. 304–305"`, `has_scholion: true`, `has_apparatus: true`. Status string appended with "frontmatter Tier-2 keys backfilled 2026-05-26 (Pass 2 Bucket-C)".
- `vol1/bon-sent-I-d8-p2-divisio.md` missing_section: Apparatus — RESOLVED. The 3 apparatus entries `[^1]/[^2]/[^3]` were defined inline inside the Latin section with no `## Apparatus` heading. Moved them under a proper `## Apparatus` section after the English body. Also placed the missing `[^3]` anchor in the English body at "in God there is purely[^3] a multiplicity of names" mirroring Latin *in Deo est pure[^3]*.
- `vol1/bon-sent-I-d3-divisio.md` legacy_duplicate — RESOLVED via RENAME. `git mv vol1/bon-sent-I-d3-divisio.md vol1/bon-sent-I-d3-p1-divisio.md`; updated `id` + added `pars: 1` in frontmatter; updated `tools/backfill-line-bounds.py` reference from `bon-sent-I-d3-divisio.md` → `bon-sent-I-d3-p1-divisio.md`. Content (pp. 66–67 of d.3 pars I) is real and was never duplicated by `d3-p2-divisio.md` (which covers p. 80 only); the rename brings the filename in line with the p2 sibling.

**Audits (touched distinctions):** paraphrase clean for d.1, d.3, d.8, d.42, d.43, d.45 (Vol I) and d.11, d.12, d.13, d.15, d.17, d.18, d.19 (Vol II) — no new CRITICAL flags introduced. HIGH flags pre-exist (d.43 / d.45 legacy paraphrase noise; Vol II skeleton siblings). Build smoke-tested green: 879 routes / 639 translated / 2 books (route delta = 0 from the d.3 rename — same chunk, new filename; build script reads `book:` from frontmatter, not filename).

**Pass 2 FLAG count: 20 → 6 (residual).** All 6 residual are mid-range `orphan_app_defs` requiring 450–600 dpi PDF walks to place missing body anchors (Case 3). They are NOT padding-duplicates: each contains substantive textual content (Vat./codd. variants, biblical/patristic citations) that probably anchors at a specific lemma in the body but the anchor was never placed during the Wave-9b rebuild. **Pass 2 NOT yet closed.** Per-chunk follow-up needed:
- `bon-sent-I-d1-a2-q1` [^3]/[^4]/[^5]/[^6] (4 orphans; p. 42–43 footer block)
- `bon-sent-I-d9-dubia` [^54] (1 orphan; *hoc* variant)
- `bon-sent-II-d11-a2-q3` [^2]/[^3]/[^4] (3 orphans; p. 286 footers nn. 5/6/7)
- `bon-sent-II-d14-p1-a2-q1` [^4]/[^5]/[^6] (3 orphans; Chalcidius/Aristot. citations)
- `bon-sent-II-d18-littera` [^15] (1 orphan; Gennadius c. 14)
- `bon-sent-II-d19-a2-q2` [^9] (1 orphan; Psalm 48, 13)

## Pass 3 — cross-chunk boundary integrity sweep (d.11–d.20)

(pending Pass 2 close — 6 Bucket-C orphan_app_defs FLAGs remaining)
