# Next session resume

**Last updated:** 2026-05-31 (d41-a2-q3 promoted to Tier 2)

## NEXT ACTION

`bon-sent-II-d41-dubia` — DUBIA CIRCA LITTERAM MAGISTRI for d.41 (DUB. I, II, III).

- d.41 is NOT yet complete: after a2-q3 comes the dubia block, then DISTINCTIO XLII.
- **Raw range:** `DUBIA CIRCA LITTERAM MAGISTRI` header at raw **66357**; runs to `DISTINCTIO XLII` at raw **66472** (`raw/bonaventure_vol2_raw.txt`).
- **Printed span:** pp. 935–936 (pdf 957–958, offset +22). DUB. I begins mid-page on printed p. 935.
- **Skeleton file exists:** `vol2/bon-sent-II-d41-dubia.md`.
- **DUB. openers:**
  - DUB. I (raw 66359/66361): *In parte ista sunt quaestiones circa litteram, et primo quaeritur de hoc quod dicit, quod fides intentionem dirigit.*
  - DUB. II (raw 66370/66373): *Item quaeritur de hoc quod dicit: Omnis vita infidelium peccatum est.*
  - DUB. III (raw 66434/66436): *Item quaeritur de hoc quod dicit, quod peccata, quae a nescientibus vel coactis perpetrantur, non omnino possunt sine voluntate committi.* (continues onto p. 937 / raw 66474+ past the DISTINCTIO XLII running head — verify the DUB. III tail at raw 66474–66478 which sits after the p.937 head but is still DUB. III content: *...et tunc tollit simpliciter rationem voluntarii... et sic loquitur Magister in littera. — Et per hoc patent illa duo obiecta.*)

## HAND-OFF IN (from d41-a2-q3, commit 4ad9483 — CONFIRMED)

q3 ended with its reply 3.4 + scholion (raw 66355) on printed p. 935. The DUBIA opens mid-page on the same printed p. 935. **p.935 footer notes that belong to the DUBIA (NOT captured by q3):** `Gal. 5, 6` (Vulg. per caritatem pro per dilectionem), `Cfr. supra d. 38. a. 2. q. 2. in fine corp.`, `Vide eius verba supra pag. 891, nota 4` (Bernardus), `Supple: homo. Matth. 13, 32` (re DUB. I *ne deficiant in via*) — these are p.935 footers 2–5 (raw 66400–66407). p.935 footer 1 (`Vide supra d. 36. a. 2. q. 2. ...rationem ultionis`) was correctly taken by q3 ([^9]). Pick up footers 2–5 for DUB. I.

## DONE so far (Vol II d.41)

- d41-littera — Tier 2
- d41-a1-q1, a1-q2, a1-q3 — Tier 2 (Articulus I complete)
- d41-a2-q1, a2-q2 — Tier 2
- **d41-a2-q3 — Tier 2 (2026-05-31, commit 4ad9483)** — pp.933–935, 9 apparatus, scholion present, opener aligned (third of Art.II). Articulus II complete.
- **REMAINING in d.41:** d41-dubia (DUB. I–III, raw 66357–66471).

## After d.41

Once d41-dubia ships, d.41 is COMPLETE. d.41 is NOT a decade boundary — no polish gate. Next distinction = `bon-sent-II-d42-littera` (DISTINCTIO XLII begins raw 66472).

## Reminders

- Vol II PDF-priority inversion: column-band PDF authoritative for Respondeo/Solutio/footers.
- Run the three `--volume 2 --min-d 41 --max-d 41` audits + smoke build before commit.
- Two commits per chunk (chunk+content.json; then this resume file). No deploy.
