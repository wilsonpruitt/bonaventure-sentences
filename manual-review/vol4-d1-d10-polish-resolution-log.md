# Vol IV (Book IV) — d.1–d.10 Decade Polish Gate — Resolution Log

Gate run 2026-06-20 after d.10 closed (Book IV's first decade boundary). Three passes per CLAUDE.md "Polish-blocker cadence."

## Status: PARTIAL — mechanical passes complete & clean; Pass-1 high-priority item resolved; lower-priority OCR-glyph flags catalogued for a focused 600 dpi sweep (see "Remaining").

---

## Pass 2 — Style / formatting audit (FULL corpus d.1–d.10) — ✅ CLEAN
Programmatic scan over all Vol IV d.1–d.10 chunks:
- Required Tier-2 frontmatter present in every chunk (`id, volume, book, distinctio, type, title_la, title_en, printed_pages, pdf_pages, source, transcription_status`); every `transcription_status` begins `Phase C Tier 2 complete —`.
- `## Latin` / `## English` present in all; `## Apparatus` present in all `has_apparatus: true` quaestiones.
- **Marker pairing** (`[^N]` in Latin body == English body == `[^N]:` defs) verified — spot-checked manually (the ad-hoc scanner's block-regex under-counted → false mismatches; `build-content.mjs` parses + renders all chunks cleanly, the authoritative pairing check). Build: 4 books, 1906 questions, **1426 translated**, no parse errors.

## Pass 3 — Cross-chunk boundary integrity (d.1–d.10) — ✅ CLEAN (mechanical)
- `audit-headers.py --volume 4 --min-d 1 --max-d 10`: every distinction shows **positive** ART/QUAEST/DUB diffs (chunk ≥ raw), **zero LOSS flags** → no gross body/footnote dropouts (the class this audit catches).
- `audit-paraphrase.py`: 0 critical, 1 high (known artifact: a chunk lacking `line_start` frontmatter, not a real paraphrase).
- d.6–d.10 built with explicit per-chunk footer/scholion **ownership rules** + coordinator-side **apparatus-count self-check** (every quaestio ≥ ~7 footnotes); seams reconciled live.
- **d.10 p.232 a1-q3/a1-q4 "double-claim"** investigated — FALSE ALARM: the two chunks render different citation clusters (q3 = Gratian/Ambrose/Aristotle; q4 = Augustine *de Moribus*/Avicenna); the page partitioned correctly.

## Pass 1 — [?] flag resolution (d.1–d.10)
### RESOLVED at 600 dpi
- **d6-p1-dubia — offset error + DUB. I "splice."** Originally built off the WRONG PDF pages (printed=pdf confusion → read pdf 147–148). Re-verified vs correct **pdf 167–168 / printed 147–148 at 600 dpi** (running head "DIST. VI. P. I. DUBIA." confirmed). The "[Continuatio Dub. I: *tem*…]" artifact was an IA-djvu diagonal-column mis-stitch: the orphaned clause is the **tail of DUB. II's Respondeo** (column-wrap "…ignorantia iuris. — Cum au-" → "[au]tem rebaptizatur Catholicus… gravissime peccat"), now restored to DUB. II; DUB. I ends cleanly at "…non est simile." Footnote [^6] re-attached to the DUB. II tail. Apparatus 13, La/En/def parity confirmed. `[?] OFFSET ERROR` note replaced with a resolved-note.

### CATALOGUED — accepted-as-rendered (conservative) pending a focused 600 dpi pass
Remaining inline `[?]` flags are overwhelmingly **single-glyph / clipped-variant OCR notes** (printed reading rendered; residual ambiguity flagged) and **scholion-disposition notes**. Scholion dispositions were cross-checked across siblings during building; glyph flags are low-risk (rendered text matches the printed page; the flag concerns a marginal variant siglum or a digit in a cross-reference). Not gross errors; do not affect rendered text.

**Scholion-disposition items worth a targeted 600 dpi check** (possible drop of a keyed sub-section across a parallel batch):
- d.7 — ART I scholion (early block in a1-q1 + unified p.168 block reassigned to ART II) + ART II scholion split across a2-q1/a2-q3 → verify the "Quoad seq. (2.) quaestionem" line (raw L19354) not dropped.
- d.8 — ART II Pars II scholion: a2-q1 rendered §"1."; a2-q2 rendered none though a2-q1 said the "De hac 2. quaestione" section was a2-q2's → verify not dropped. Also d8-p2-a2-q2 p.198 footer n.9 ownership.
- d.9 — ART I scholion (a1-q1 §I; q2–q4 none) + ART II joint scholion (a2-q1) → verify q2/q3/q4 keyed sections not dropped.
- d.6 — p2-divisio body marker order (2,3,5,4,6, content-anchored) re-verify keying.

### Pre-existing flags (from d.1–d.5 original builds, in next-session-resume.md)
d.1 (p1-littera p.10 markers — resolved by divisio; p2-a2-q3 [^6c]); d.3 (p.63 L-col footer attribution; d3-p2-dubia [^11] question-number clip); d.4 (littera page-offset note; p1-a1-q2 dropped p.98 note 7; p1-divisio stray superscript; p2-dubia p.116 illegible variant). These remain catalogued.

## Remaining gate work (deferred, NOT a correctness blocker)
A dedicated 600 dpi pass over the catalogued glyph/variant `[?]` flags + the scholion-disposition checks above. Mechanical integrity (formatting, marker pairing, header/footnote dropout) is confirmed clean.
