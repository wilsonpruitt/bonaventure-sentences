# `lucam` inbound citation class (Vol VII ruling 24), built 2026-11-14

Tool job in `tools/build-citations.py`: `LUC_RE` / `scan_lucam` / `build_luc_index` / `resolve_lucam`, plus a double-count
guard in `extract` (a scripture record starting inside a span `LUC_RE` matches is dropped). `Chunk` now parses `verses:`.
Resolution: (division, verse) in a Luke chunk's `verses:` -> `chunk`; the `n` form by `paragraphs:`; not built -> `forward`
with target `lucam:<ch>:<v>` (`lucam:<ch>:n<n>` for the paragraph form). `governed_by_author` guard runs WITHOUT the
`Bonav.` siglum (it is the work's own author), and a `Bonav.` within 20 chars before the title overrides an earlier clause's author.

## Deltas (before -> after)
Records 36077 -> 36096 (+19: +20 `lucam` crossref [19 sites + 1 `ibid.` that follows one], -1 scripture). Scripture 22128 -> 22127.
Crossref 12783 -> 12803. `forward` 3 -> 23. QA flags 211 -> 211.
The sheet said these sites were filed as Gospel verses at confidence A. Measured: NOT so for all but one. The scripture
scanner's `in ` guard already skipped `in Luc. C, V`, so almost all were simply unindexed. The one removed scripture record was
a wrong `ibid.` (bon-cioan-c21 p623-6, `ibid.` -> `Ioan 11:1`); it now inherits the Luke citation (`lucam:24:13`), which the note's text confirms
(`In Comment. in Luc. 24, 13. ... a Card. Hugone ibid.`). `bon-serm-s2` p550-8 `Luc. 13, 21` is a real Gospel ref and stays; the commentary cite is p550-9.

## Sites (19), all `forward` (no built chunk holds these verses; only Cap. I vv. 1-38 exist)
| chunk | label | raw | target |
|---|---|---|---|
| bon-sent-I-d16-a1-q3 | scholion | Comment. in Lucam c. 9. v. 34. | lucam:9:34 |
| bon-sent-I-d2-dubia | fn 1 | Comment. in Luc. IX, 28. | lucam:9:28 |
| bon-sent-III-d30-a1-q4 | scholion | Comment. in Lucam, 17, 4. | lucam:17:4 |
| bon-sent-III-d36-a1-q1 | scholion | Comment. in Lucam (c. 6. n. 20.) | lucam:6:n20 |
| bon-serm-s2 | p545-12 | Comment. in Lucam, ad 18, 25 | lucam:18:25 |
| bon-serm-s2 | p550-9 | Comment. in Luc. 13, 21. | lucam:13:21 |
| bon-serm-s3 | p555-3 | Comment. in Lucam, c. 22, 19. | lucam:22:19 |
| bon-serm-s3 | p558-3 | Comment. in Lucam, c. 9. ad v. 28. | lucam:9:28 |
| bon-serm-tract | p574-9 | Comment. in Lucam, c. 23, 43 | lucam:23:43 |
| bon-cioan-c21 | p623-6 | Comment. in Luc. 24, 13. (+ `ibid.`) | lucam:24:13 |
| bon-ioan-c1-v24-28 | p258-10 | Comment. in Luc. 3, 16. | lucam:3:16 |
| bon-ioan-c10-v11-21 | p388-16 | Comment. in Luc. 9, 50. | lucam:9:50 |
| bon-ioan-c11-v7-32 | p402-14 | Comment. in Luc. 17, 19. | lucam:17:19 |
| bon-ioan-c13-v21-30 | p432-3 | Comment. in Luc. 22, 23 | lucam:22:23 |
| bon-ioan-c16-v5-15 | p460-10 | Comment. in Luc. 17, 1 | lucam:17:1 |
| bon-ioan-c17-v6-11 | p471-8 | Comment. in Luc. 11, 1. | lucam:11:1 |
| bon-ioan-c18-v24-27 | p485-9 | Comment in Luc. 22, 60 | lucam:22:60 |
| bon-ioan-c19-v16-27 | p495-10 | Comment. in Luc. 23, 33 | lucam:23:33 |
| bon-ioan-c21-v9-14 | p523-9 | Comment. in Luc. 24, 35. | lucam:24:35 |

## Versus the sheet's ~22
The sheet counted a grep of rendered text: 3 hits inside `## Notes` only (our English, colon form `24:35`; never scanned), and the sheet's
`-dubia` twin of the I-d16 `c. 9. v. 34` is the same site as the scholion record. Not caught on purpose: `S. Bonav. Exposit. in Luc. 18, 13`
(bon-sent-IV-d21-p1-a1-q2 fn 8): a Bonaventure Luke cite, but under `Exposit.`, not the attested `Comment.` shape (and unindexed today); add `Exposit` to
`LUC_RE` if wanted. False positives: none seen (all 19 are `Comment. in Luc(am)`; Ambrose's `Exposit. in Luc.` never matches).
Not done: the page+note tie-break (`pag. 7, nota 5` -> `bon-luc-prol`) named in ruling 24: separate tool line, not in this job.
