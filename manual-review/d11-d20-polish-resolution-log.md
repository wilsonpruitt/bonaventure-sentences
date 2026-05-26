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

## Pass 2 final dispatch — 6 Bucket-C `orphan_app_defs` (2026-05-26)

Final 6 Pass-2 FLAGs closed. Backups in `_backup-pass2-final-20260526/`. Per-flag disposition:

1. **`vol1/bon-sent-I-d1-a2-q1.md` [^3]/[^4]/[^5]/[^6]** — Case-4 padding-DELETE. All four defs are EXACT DUPLICATES of `vol1/bon-sent-I-d1-a1-q3.md`'s [^13]/[^14]/[^15]/[^16] (Vat. additions *amorem*/*cognitionem* after *istum*/*illam*; *hoc* + omitted proposition after *ordinatione*; *scilicet usus Dei...* after *ultimum*; *in* for *ad*). Lemmas (`istum`, `ordinatione`, `ultimum`) live in the prior chunk's body, not in d1-a2-q1's "Articulus II" body. Defs removed; prefatory `>` note updated to clarify the [^3]-[^6] Quaracchi-numbered footers are carried by d1-a1-q3 ([^13]-[^16]).

2. **`vol1/bon-sent-I-d9-dubia.md` [^54]** — Case-4 padding-DELETE. Per the chunk's own `transcription_status` (2026-05-12 polish-pass): the original phantom [^54] was deleted and body anchors re-mapped, but the orphan def [^54] (Vat. *hoc* variant) was never cleared. Sequential numbering [^53] then [^55] is intact in body; def [^54] removed as residual.

3. **`vol2/bon-sent-II-d11-a2-q3.md` [^2]/[^3]/[^4]** — Case-3 anchor placement. Per chunk's own `## Notes`, these correspond to p.286 footers nn.5–7. p.286 holds only title + opener + obj.1 ("Tertii Regum vigesimo[^1]: *Custodi virum istum; qui si lapsus fuerit, erit anima tua pro anima illius;* …et hoc videtur dicere"). Placed [^4] (Vers.39) after the scripture quote close (`anima illius;[^4]`); [^2] (Cod. V *accidentale* / Vat. *creatum* additions) at `salutis suae[^2] periculum`; [^3] (In quaest. seq.) at `et hoc[^3] videtur dicere`. Mirrored in English at parallel clauses.

4. **`vol2/bon-sent-II-d14-p1-a2-q1.md` [^4]/[^5]/[^6]** — Case-3 anchor placement. Defs: [^4] *Vide scholion ad praecedentem quaest.*; [^5] Chalcidius *in Timaeum* n.59 seqq.; [^6] *De hoc et seqq. fundam.* vide Aristot. II *de Caelo* text 22 seqq. Placed [^4] at ARTICULUS II opener clause-end ("Consequenter quaeritur de caelis quantum ad figuram[^4]"); [^6] at the question opener's "videtur[^6]:" (since it is a section-header footer covering "this and following fundamentals"); [^5] at end of arg 1 ("ergo etc.[^5]") covering the Chalcidius cosmological-observational citation that parallels arg 1's *experientia sensus*. Mirrored in English.

5. **`vol2/bon-sent-II-d18-littera.md` [^15]** — Case-3 anchor placement. Def is "Gennadius, c. 14. Paulo inferius pro *cum corporibus* Vat. et edd. 2,3,4,5,6,7,9 *in corporibus*." Cap. VII body contains the *Ecclesiasticis Dogmatibus* quote with the exact lemma "cum corporibus per coitum seminari". Placed [^15] at `cum corporibus[^15]` in La and "with bodies[^15]" in En.

6. **`vol2/bon-sent-II-d19-a2-q2.md` [^9]** — Case-3 anchor placement. Def is "Psalm. 48,13. — Paulo inferius pro *mortis* plures codd. *mortalitatis*." *Sed contra* arg 3 cites Psalm 48:13 verbatim ("homo per peccatum similis factus est iumentis insipientibus"). Placed [^9] at `iumentis insipientibus[^9]` in La and "the senseless beasts[^9]" in En; the *mortis*/*mortalitatis* variant ("paulo inferius") sits in the following clause "quantum ad conditionem mortis iumentis similis effectus est".

**Audits post-fix:** `audit-style-formatting.py` orphan_app_defs 6 → **0**, total FLAGs 6 → **0**; `audit-paraphrase.py` clean across all touched distinctions (d.1 Vol I 0/0; d.9 Vol I 0/0; d.11 Vol II 0/0; d.14 Vol II 0/1 HIGH from unrelated sibling-skeleton; d.18–19 Vol II 0/0). Build green: 879 routes / 639 translated / 2 books (no delta).

**Pass 2 status: CLOSED.** All originally-flagged Pass-2 items resolved across the Bucket-A/B (2026-05-25 PM), Bucket-C grouped dispatch (2026-05-26 AM/midday), and this final 6-flag dispatch (2026-05-26 PM).

## Pass 3 — cross-chunk boundary integrity sweep (d.11–d.20)

**Status (2026-05-26 PM): CLOSED.** Enumerated all chunk-pair boundaries inside d.11–d.20 in semantic order via inline helper (yaml-frontmatter `printed_pages` walk). **97 boundaries total, 83 mid-page** (i.e. `prior.printed_pages[-1] == receiving.printed_pages[0]`). Audited each: receiving chunk's `## Notes` block (and/or the prior chunk's forward-handoff note) explicitly documents the page-split / footer-migration / continuity status.

**Per-distinction breakdown (mid-page boundaries / FLAGs):**

- d.11: 7 mid-page boundaries — all CLEAN. (d11-divisio→a1-q1 p.276, a1-q1→a1-q2 p.279, a1-q2→a1-q3 p.280, a1-q3→a2-q1 p.282, a2-q1→a2-q2 p.285, a2-q2→a2-q3 p.286, a2-q3→dubia p.289.)
- d.11→d.12 inter-distinction: dubia→d12-littera p.290 — CLEAN.
- d.12: 6 mid-page — all CLEAN.
- d.12→d.13: dubia→d13-littera p.308 — CLEAN.
- d.13: 6 mid-page — all CLEAN.
- d.13→d.14: dubia→d14-p1-littera p.333 — CLEAN.
- d.14: 13 mid-page (p1 + p2 + intra-pars) — all CLEAN. (Includes d14-p1-dubia→d14-p2-divisio p.350 cross-pars boundary; p2-divisio holds the explicit page-split note.)
- d.14→d.15: d14-p2-dubia→d15-littera p.370 — CLEAN.
- d.15: 7 mid-page — all CLEAN.
- d.15→d.16: d15-dubia→d16-littera p.391 — CLEAN.
- d.16: 7 mid-page — all CLEAN.
- d.16→d.17: d16-dubia→d17-littera p.408 — CLEAN.
- d.17: 7 mid-page — all CLEAN.
- d.17→d.18: d17-dubia→d18-littera p.429 — CLEAN.
- d.18: 7 mid-page — 6 CLEAN + 1 follow-up resolved (see d18-a2-q2/q3 note below).
- d.18→d.19: d18-dubia→d19-littera p.455 — CLEAN.
- d.19: 7 mid-page — all CLEAN.
- d.19→d.20: implicit through divisio inheritance — CLEAN.
- d.20: 7 mid-page — all CLEAN (the d.20 series was built in semantic order this same wave with explicit hand-off Notes in every chunk; verified by helper).

**Pass-1 follow-up resolution — `d18-a2-q2` p.450 R-2 footers ⁶/⁷/⁸.**

Generated `/tmp/colcrop/vol2-p450-{L,R}-{0..2}.png` via `tools/colcrop.py vol2 450`. Eyes-on R-2 column band confirms three numbered footers exactly as projected in the resume note:
- ⁶ *Haec ex Gregorio sumta solutio iam supra d. 12. a. 1. q. 2. ad 3. habetur.*
- ⁷ *Codd. Y aa* propter*.* (Quaracchi prints *aa*, not *oa* — minor resume-note OCR transcription error; printed reading is *aa*.)
- ⁸ *Cfr. supra pag. 20, nota 7.*

**Disposition: CONSOLIDATED into existing [^23] composite scholion-footer; NO body text missing; no splice.** All three footer entries anchor within the SCHOLION I body that runs from p.450 R-mid into p.451 L-1 (the *Gregorius Nazianzeni/Nysseni* codd.-variant scholion + *de Spiritu et anima* c. 13 textual reception). The d18-a2-q2 apparatus [^23] already absorbs this content verbatim (the printed scholion paragraph terminating *Has potentias habet, antequam corpori misceatur*) and the parenthetical note at line 271 explicitly enumerates the three marginal source-pointer/codd.-variant/cross-reference items. Cross-checked the p.450 R-2 PDF crop body band against d18-a2-q2 [^23]'s full English+Latin pair: every Latin clause from *Libr. II. de Fide orthod. c. 12…* through *…antequam corpori misceatur* appears verbatim in [^23]. **No grammatical splice; no missing body words; no orphan apparatus.** The three footers are a marginal-typography convention (Quaracchi often prints source-pointers + variant-glosses as separately-numbered footers even when the scholion already incorporates the citation inline); their atomic split-out as [^26]/[^27]/[^28] would be a cosmetic refinement, deferred (no impact on body or translation integrity).

Note updated in d18-a2-q2's `## Notes` block: Pass-3 follow-up CLOSED.

**No splices, no rebuilds, no body recovery needed across all 83 mid-page boundaries.** This is consistent with the Vol II cadence — every d.11–d.20 chunk was promoted with the cross-chunk hand-off discipline locked from 2026-05-25; the cascade-merge failure-mode (d9-divisio precedent) requires building a chunk *without* having read its neighbor's PDF page, which the one-chunk-per-subagent dispatch with hand-off briefings explicitly prevents.

**Pass 3 status: CLOSED. d.11–d.20 decade-polish-blocker FULLY CLOSED (Pass 1 + Pass 2 + Pass 3).** Next action: dispatch d.21-littera (Vol II).
