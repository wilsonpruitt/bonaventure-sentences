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

(pending Pass 1 close)

## Pass 3 — cross-chunk boundary integrity sweep (d.11–d.20)

(pending Pass 1 close)
