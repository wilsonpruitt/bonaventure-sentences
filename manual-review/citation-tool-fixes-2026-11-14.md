# Citation tool fixes, 2026-11-14 (Vol VII ruling 37 / docket item 11)

Scope: `manual-review/vol7-lucam-p88-gate-evidence-sheet.md` § 11. Only `tools/build-citations.py` and
`tools/scripture-books.json` (one body form) changed. No chunk text, no `tools/authorities.json`. Measured
with `python3.11 tools/build-citations.py` on the same tree before and after. The generated ledger and QA
report are not committed here: the coordinator regenerates them on master.

## Totals, before to after

| | before | after |
|---|---|---|
| ledger records | 37,675 | 37,792 (+117) |
| QA flags | 213 | 211 (-2: T1, T8) |
| crossref `chunk` | 9,362 | 9,799 |
| `page-multi` | 1,453 | 1,031 (-422) |
| `forward` | 24 | 23 |
| `dangling` | 227 | 226 |
| `unresolvable` | 349 | 362 |
| `distinctio` | 780 | 783 |
| `ambiguous` / `articulus` / `work` | 172 / 285 / 217 | unchanged |
| anaphora unresolved | 338 | 348 |
| coordinate `ibid.` honoured | 363 | 365 |
| printed slips table | 20 | 23 |

Regression check (record-by-record diff on chunk, section, class, subclass, raw text): 20 keys disappear and
137 appear, and every one of the 20 is a deliberate re-filing, none an unrelated loss: 2 paragraph-break false
positives (T1), 12 cross-note `ibid.`/`loc. cit.` false resolutions now `unresolvable` (T10), 2 own-author
`Sent.` loci re-filed from `authority` to `crossref` (T7), 1 page record whose raw text now carries `in nota 8`
(T9), 2 previously unresolvable coordinate `ibid.` now bound to a body ordinal (T11), 1 T10 residual. All
other volumes' `forward`/`dangling`/`ambiguous` counts are unchanged.

## Per defect

| # | status | change | effect on its named sites |
|---|---|---|---|
| T1 | **fixed** | `scan_scripture_apparatus` skips a match whose book name and number are separated by a blank line (paragraph break) | `c1-v46-56` ¶ 97/98 "Esther. 98" gone, QA -1. Same class also removed `bon-eccl-c8-v9-13` "Iacob. 1" (a false chapter-level record, Vol VI) |
| T3 | **fixed** | new `CROSSREF_SLIPS` table (the `PRINTED_SLIPS` class for cross-references): record kept, raw text as printed, listed in the QA slips table, verdict set to `unresolvable`, target blanked | p. 38 n. 7 `supra pag. 1, nota 5`: `forward` to `unresolvable` (the permanent forward closed) |
| T8 | **fixed** | same table | p. 54 n. 10 `d. 8. p. II. dub. 2.`: `dangling` to `unresolvable`, QA -1 |
| T4 | **fixed** | same table (reason recorded) | p. 44 n. 7 `tom. VI. pag. 91, nota 3`: wrong `bon-eccl-c11-v1-10` edge removed. The same note's `ibid. v. 45` stays unresolved |
| T6 | **fixed, corpus-wide** | `resolve_page(…, by_id)`: on a shared page, keep only the chunks that carry apparatus note `p<page>-<nota>` (or note `<nota>` for a one-page chunk); one survivor is the target (`page-multi` to `chunk`, anchor `fn-pP-N` follows) | all 11 named Vol VII sites resolve (p. 50 nn. 2, 3; p. 52 n. 10; p. 58 n. 1; p. 64 n. 5; p. 69 n. 4; p. 71 n. 6; p. 79 n. 3; p. 82 n. 12; p. 83 n. 3; p. 84 n. 6), including the Vol III and Vol VI targets and the p. 83 n. 3 to p. 283 n. 2 reciprocal. **Scale: 422 records, not ~11**: 136 Vol V, 99 Vol VI, 86 Vol IV, 79 Vol III, 17 Vol VII, 5 Vol II, all `page-multi` to `chunk` and nothing else changes. The sheet said "every `pag. N, nota M`"; the count is reported here because it is larger than the sheet's estimate |
| T7 | **fixed, Vol VII citing chunks only** (plus the Eccle class corpus-wide) | (a) `Bonav.` no longer counts as a foreign author for `Sent.` loci and `Comment. in Ioan.` when the citing chunk is Vol VII (`OWN_AUTHOR_VOLUMES`); (b) `IOAN_PARA_RE` accepts `Comment. in Ioan. 1, 44. n. 91` (no `c.`, verse between); (c) new `Comment. in Eccle. C, V` class (`scan_eccle`, resolves by chapter and verse range into Vol VI) | p. 68 n. 6 (c. 2 n. 4), p. 72 n. 4 (c. 1 n. 52), p. 82 n. 5 (c. 1 n. 64 and `IV. Sent. d. 2. a. 2. q. 2`), p. 83 n. 9 (`IV. Sent. d. 4. p. II. a. 1. q. 3`), p. 64 n. 10 (1, 44. n. 91), p. 50 n. 2 (`Comment. in Eccle. 1, 8` to `bon-eccl-c1-v8-11`) all `chunk`. Extra, same shapes: `Comment. in Ioan. 19, 14. n. 15` (p. 20 n. 10), `19, 34. n. 52` (Vol VI `bon-cioan-c2`), and 8 own `Comment. in Eccle.` sites in Vols II and VI, all `chunk` |
| T9 | **fixed** | bare `pag. N` in a parenthesis after `Breviloq.`/`Itiner.`/`Hexaëm.` is Vol V; `in nota N` accepted by the page scanner and the anchor | p. 55 n. 8: `forward tom7:p203` to `bon-brev-prol-s2`, anchor `fn-p203-8`; `forward` -1 |
| T10 | **fixed, Vol VII only** | for apparatus anaphors in Vol VII the within-chunk walk stops at the note boundary. The cross-chunk pass is restricted to the chunk's first note, and only if that note opens with the anaphor | the 7 named false resolutions (p. 64 n. 6; p. 69 nn. 4, 9; p. 73 n. 9; p. 74 n. 1; p. 77 n. 10) are `unresolvable`. 6 more of the same shape (p. 19 n. 5; p. 22 n. 1; p. 26 n. 8; p. 73 n. 4; p. 7 n. 2; p. 8 n. 7 x2: `ibid.` after Baron./Gregor./Origen/Migne bound to an unrelated scripture verse) also correct. p. 79 n. 3 now correct through T6 (its `loc. cit.` follows `tom. III. pag. 466, nota 1` in the same note) |
| T11 | **fixed, corpus-wide** | `Ecclesiastae` added as an `Eccle` body form (`scripture-books.json`); the body-ordinal scanner accepts the comma form (`Deuteronomii, duodecimo`); `VERS_RE` accepts `Ver.` | c2-v40-52 ¶¶ 107, 109; c3-v1-9 ¶ 11; c3-v10-14 ¶ 29; ¶ 93 `Deuteronomii, duodecimo` (Deut 12:5); p. 65 n. 12 `Ver. 14.` (Exod 12:14). **Scale: +100 records**, not +5-6: ~70 Vol VI `Ecclesiastae N` sites in the Ecclesiastes commentary itself, 5 chapter-level records upgraded to verse by `Ver.`, 14 comma-form records, 2 `ibid.` made resolvable. All additive and read as printed |
| T13 | **fixed, Vol VII only** | roman `d.` accepted in `scan_sentences`, plus the `lit. Magistri,` interposition | p. 69 n. 4 `III. Sent. d. XIII` (`III:d13`, its `loc. cit.` now follows it) and p. 85 n. 9 `II. Sent. lit. Magistri, d. XXIV` (`II:d24`). In Vols I-VI the roman form would add ~73 records, re-bind some `ibid.` chains and add 1 QA flag |
| T12 + IV-d21 | **fixed** | explicit two-row `LUCAM_SITES` table; `LUC_RE` not widened | `bon-ioan-c3-v13-16` p. 283 n. 2 to `bon-luc-c3-v21-22` (`chunk`, lands on the Vat. addition in the apparatus, not the body; the p. 83 n. 3 reverse link resolves under T6); `bon-sent-IV-d21-p1-a1-q2` n. 8 to `lucam:18:13` (`forward`) |

## Deferred

- **T5** (in-work `c. N. n. M` / `supra n. N` / `infra` + ordinal): not in the job, waits with the *Ioannem* class (ruling 24 /
  82(a)). Count only: a regex over the Vol VII apparatus finds **~46 hits in 16 chunks** (an upper bound; some belong to
  other authors).
- **T2**: closed (never recurred), no tool work.
- **T7 outside Vol VII**: letting `S. Bonav.` through the author guard in Vols I-VI would re-file **~100** `authority:Bonav.`
  Sentences loci (scholia and apparatus of Vols I-V) from `authority` to `crossref` and change some `ibid.` chains. That is a
  corpus-wide ruling the sheet does not make; `OWN_AUTHOR_VOLUMES = {7}` is the one-line switch.
- **T10 outside Vol VII**: the across-note walk is the rule Vols I-VI were built on (docstring of `resolve_anaphora`); the
  boundary is `ANAPHOR_NOTE_BOUNDARY_VOLUMES = {7}`.
- **T13 outside Vol VII**: `ROMAN_DIST_VOLUMES = {7}` (about +73 records and 1 new QA flag, `bon-itin-scholion`, if opened).
- **T6**: not deferred anywhere; it is corpus-wide because the fix is a pure `page-multi` to `chunk` disambiguation.

## Left as is, for the coordinator

- The generated ledger, `citation-qa-report.md` and `build-index-json.py` output were not regenerated into the commit.
- Within Vol VII the `ibid.` records now `unresolvable` (13) are real unresolved anaphora, visible in the QA "Unresolved
  anaphora" table; they read as no record rather than a wrong one.
