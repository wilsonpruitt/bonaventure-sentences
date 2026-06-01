# Bonaventure Sentences — Next Session Resume

**Last updated:** 2026-05-31 (d42-a3-q2 promoted -> Tier 2, commit 1713aee)

**Branch:** master

## NEXT ACTION -> `bon-sent-II-d42-dubia` (d.42 a3-q2 now Tier 2; a3-q2 was the LAST article chunk of d.42)

**`bon-sent-II-d42-a3-q2` shipped 2026-05-31 (commit 1713aee):** QUAESTIO II *Utrum peccatum habeat dividi per aversionem et conversionem tanquam per diversas peccatorum differentias*, printed **pp.973-974** (PDF 995-996), 15-entry apparatus (per-page restart: p.973 1-9, p.974 1-6), `has_scholion: false` (a3-q1 Scholion II covers it). Marker pairing 15/15 clean. Alignment PASS (`Secundo quaeritur… per diversas peccatorum differentias` = q2). Build 875 q / 856 translated. Audits: a3-q2 paraphrase HIGH flag is benign (no line_start/line_end on Tier-2 frontmatter -> content audit skipped, not a paraphrase issue); header audit clean; apparatus-count flags only the remaining d42-dubia skeleton (+52).

> **HAND-OFF TO d42-dubia (forwarded):** The DUBIA block (`DUBIA CIRCA LITTERAM MAGISTRI` / `DUB. I.`) begins at raw **67682**, opening on the bottom of printed **p.974** (PDF 996) and continuing onto p.975+. **p.974 footers 7 and 8 belong to the dubia, NOT to a3-q2** — a3-q2 consumed p.974 footers 1-6 (rendered `[^10]`-`[^15]`); do NOT re-claim them. The dubia's first two body-footers (the SHARED p.974 footer split) are: footer 7 = `Vide scholion ad praecedentem quaest.` (anchored on the DUB. I opener `…postquam transit actu`); footer 8 = `Quod insinuatur hic in lit. Magistri, c. 2. — Omnes edd. et Magistri et Comment. cum codd. habent postquam transit pro postquam transiit. Unde nihil immutavimus.` The dubia then continues with its own fresh p.975 footer sequence. DUB. I = *utrum peccatum interdum est in aliquo reatu postquam transit actu* (super quid fundetur reatus sive obligatio ad poenam; opinio 1 reatus super actum, etc.). d.42 dubia apparatus audit diff +52 (whole-distinction dubia block — expect multiple DUB. with per-page footer sequences across pp.974-97x).

## NEXT ACTION (superseded) -> `bon-sent-II-d42-a3-q2` (d.42 a3-q1 now Tier 2)

**`bon-sent-II-d42-a3-q1` shipped 2026-05-31 (commit 63ccdff):** ARTICULUS III opener (`De modis dividendi peccata.`) folded in + QUAESTIO I *Utrum peccatum habeat dividi per differentias materiales tantum, an etiam per formales*, printed **pp.970-973** (PDF 992-995), 20-entry apparatus (per-page restart rendered as running slugs `[^1]`-`[^20]`: p.970 footers **6-10 picked up** [1-5 were a2-q2's], p.971 1-9, p.972 1-6; p.973 has no q1 body-footer — body there is Scholion + q2 opener). `has_scholion: true` — **Article-III Scholion I-II held here; Scholion II ("De seq. (2.) quaestione…") covers a3-q2.** Marker pairing 20/20 clean. Alignment PASS (`Primo quaeritur… an per differentias formales et specificas` = q1). Build 875 q / 855 translated. Audits: a3-q1 does NOT flag; the 2 flagged d.42 chunks are the remaining skeletons (a3-q2 +19, dubia +52).

> **HAND-OFF TO a3-q2 (forwarded):** QUAESTIO II (`Utrum peccatum habeat dividi per aversionem et conversionem tanquam per diversas peccatorum differentias`, `Secundo quaeritur`, raw **67587**) opens in the **R-column of printed p.973** (PDF 995), continues onto p.974+. **a3-q2 has NO scholion of its own** — Scholion II (held in a3-q1) covers it; set `has_scholion: false`. **a3-q2's first body-footer is the fresh p.973 footer sequence** (the `Ieremiae secundo¹: Duo mala fecit populus meus…` + `Ecclesiastici decimo…` references) — no q1 footer migrates forward. q2 fund. 1 (Jeremiah 2: *Duo mala fecit populus meus*), fund. 2 (aversio = *contemptus*, conversio); Sed contra opens on the Glossa to Ecclesiasticus 10 (*Initium omnis peccati superbia*: « Caveamus superbiam et cupiditatem, non tanquam duo mala, sed unum »). Offset `pdf = printed + 22`; OCR running-head digits mangled — trust running-head TEXT + offset, confirm printed_pages via low-dpi render. After a3-q2 comes d42-dubia (still a skeleton, apparatus diff +52).

**`bon-sent-II-d42-a2-q2` shipped 2026-05-31 (commit 86c8201):** QUAESTIO II *Utrum veniale conveniat cum mortali in reatu poenae aeternae*, printed **pp.967-970** (PDF 989-992), 27-entry apparatus (per-page restart: p.967 1-7, p.968 1-8, p.969 1-7, p.970 1-5), `has_scholion: false` (a2-q1 Scholion II covers it). Marker pairing 27/27 clean. Alignment PASS (`Secundo quaeritur… reatu poenae aeternae` = q2). Build 875 q / 854 translated. Audits: a2-q2 does NOT flag; the 3 flagged d.42 chunks are the remaining skeletons (a3-q1 +34, a3-q2 +19, dubia +52).

> **HAND-OFF TO a3-q1 (forwarded):** ARTICULUS III (`De modis dividendi peccata.`, short opener `Consequenter quaeritur tertio loco de modis dividendi peccata… in generali quaeruntur hic duo`, raw **67404**) folds into a3-q1 per the Vol II chunking convention. **a3-q1** (`Utrum peccatum habeat dividi per differentias materiales tantum, an etiam per formales`, `Circa primum sic proceditur`, raw **~67416**) opens on the bottom half of printed **p.970** (PDF 992). Article-III opener lists q1 = `utrum peccatum habeat dividi per differentias materiales tantum, an per differentias formales et specificas`; q2 = `utrum peccatum dividi habeat per conversionem et aversionem tanquam per diversas peccatorum differentias`. **p.970 footers 6-10 belong to a3-q1** (6 = Vat. addit *et specificas*; 7 = Porphyry *de Praedicab. de Specie et de Differentia*; 8 = Aristotle *de Praedicam. de Oppositis*; 9 = Vide supra d.XXXIII lit. Magistri c.2; 10 = Aristot. pag.89 n.7). **a3-q1's fresh footer sequence begins at p.970 footer 6** — q2 consumed p.970 footers 1-5; do NOT re-claim them. a3-q1 continues onto pp.971-972. a3-q1 likely carries the Article-III scholion (check for `pro quaest. seq.` covering a3-q2).

**`bon-sent-II-d42-a2-q1` shipped 2026-05-31 (commit f604e20):** QUAESTIO I *Utrum peccatum veniale et mortale conveniant in aversione* (+ ARTICULUS II opener folded in), printed **pp.964-966** (PDF 986-988), 25-entry apparatus (per-page restart: p.964 footers 2-8 picked up [footer 1 was consumed by a1-q2, NOT re-claimed], p.965 1-10, p.966 1-8) = 18 unique slug-defs, 18/18 marker pairing clean. Alignment PASS (`Primo quaeritur` = q1). `has_scholion: true` — **SCHOLION I-II held here; Scholion II covers q2.** Build 875 q / 853 translated.

> **HAND-OFF TO a2-q2 (forwarded):** QUAESTIO II (`Utrum veniale conveniat cum mortali in reatu poenae aeternae`, `Secundo quaeritur…`, raw **67196**) opens on printed **p.967** (PDF 989). **a2-q2 has NO scholion of its own** — Scholion II ("Quoad sequentem (2.) quaest.", held in a2-q1) covers it; set `has_scholion: false`. The SCHOLION block runs across p.966-967; the `QUAEST. I.`->`QUAEST. II.` running-head transition falls *inside* the scholion. **a2-q2's first body footer is the fresh p.967 footer sequence — no q1 footer migrates forward.** Alignment = q2 (`Secundo quaeritur… reatu poenae aeternae`); fund. 1 (Poena assumta pro mortali… proportionabilis), fund. 2 (puniri aeternaliter ratione sui), fund. 3 (veniale stat cum gratia et cum mortali). After a2-q2 come a3-q1/q2 and d42-dubia (still auto-chunked skeletons, apparatus diffs +52/+34/+19).

**`bon-sent-II-d42-a1-q2` shipped 2026-05-31 (commit b302dc0):** QUAESTIO II *Utrum peccatum operis addat aliquid supra peccatum voluntatis*, printed **pp.962-964** (PDF 984-986), 13-entry apparatus (running slugs `[^1]`–`[^13]`; picked up the 3 migrated p.962 footers from q1 — Psalm 68:28 gloss `[^2]`, Augustine *de Trin.* `[^3]`, *de Lib. Arb.* I c.6 n.15 `[^4]` — plus p.962R 5-7, p.963 8-13, p.964 footer 1 `[^1]` *Vide scholion ad praecedentem quaest.*), `has_scholion: false` (q1 Scholion II covers q2). Marker pairing 13/13 clean. Alignment PASS (`Secundo quaeritur` = q2). Build 875 q / 852 translated. Audits: apparatus-count does NOT flag q2; the 5 flagged d.42 chunks are the remaining skeletons (a2-q1/q2, a3-q1/q2, dubia).

> **HAND-OFF TO a2-q1 (forwarded):** ARTICULUS II (`De comparatione peccati venialis ad mortale`, short opener `Consequenter quaeritur circa secundum… quaeruntur duo`, raw **66981**) folds into a2-q1 per the Vol II chunking convention. **a2-q1** (`Utrum peccatum veniale et mortale conveniant in aversione`, `Circa primum sic proceditur… Primo quaeritur`, raw **66990**) opens in printed **p.964** (PDF 986) — fund. 1 (Augustinus, *peccatum non est appetitus rerum malarum*), fund. 2 (Ad Romanos 7, *Non concupisces* gloss), fund. 3 (sexto Musicae, *Amor inferioris pulcritudinis*). Alignment = q1 (`Primo quaeritur` / `conveniant in aversione`); q2 = `Secundo quaeritur, utrum conveniant in reatu sive obligatione ad aeternitatem poenae`. **p.964 footers 2, 3, 4 belong to a2-q1** (footer 2 = *De Natura boni* c. 34, 36 / *appetitus rerum* / Cfr. p. 838 n. 8; footer 3 = Plurima codd. + edd. 1, 2 *communicat*; footer 4 = Apoc.-numbering note, Ipsa verba Glossae vide supra p. 528 n. 4 et p. 721 n. 2). **p.964 footer 1 (`Vide scholion ad praecedentem quaest.`) was already consumed as q2's `[^1]`** — a2-q1's first fresh footer is the *De Natura boni* note; do NOT re-claim footer 1.

**`bon-sent-II-d42-divisio` shipped 2026-05-31 (commit 4a689ee):** COMMENTARIUS IN DISTINCTIONEM XLII opener + subtitle *De differentiis peccatorum in communi* + lemma *Cum autem voluntas mala et operatio etc.* + DIVISIO TEXTUS + TRACTATIO QUAESTIONUM, printed **p.959** (PDF 981), 3-entry apparatus (single p.959 footer sequence), `has_scholion: false`, marker pairing 1-3 clean, build 875 q / 850 translated. Seam with d42-littera verified clean (littera closes `…radix omnis mali.` immediately before the COMMENTARIUS opener; no leakage). TRACTATIO listing matches actual structure (3 articles actus/reatus/modus; a1 q1+q2, a2 q1+q2, a3 q1+q2). **Hand-off forwarded:** printed p.960 (PDF 982) is entirely a1-q1 (`ARTICULUS I. De comparatione peccati operis ad peccatum voluntatis. / QUAESTIO I. Utrum peccatum voluntatis et operis sint duo peccata, vel unum.`, raw 66682/66687) with its own fresh per-page footer sequence; no divisio footer belongs to a1-q1.

**`bon-sent-II-d42-littera` shipped 2026-05-31 (commit 40e550d):** Lombard littera Caps. I-VIII (De differentiis peccatorum in communi), printed **pp.957-959** (PDF 979-981), 16-entry apparatus (per-page restart 957:1-6 / 958:1-10), `has_scholion: false`, marker pairing 1-16 clean. Seam with d.41-a2-q3 verified: p.957 L-col top (`et tunc tollit... obiecta`) is the d.41 tail and its two footers stay with the d.41 dubium; littera footers begin at the `NOTAE AD LIBR. SENTENTIARUM.` divider.

> **PAGE-NUMBER LESSON (q2, 2026-05-31):** the OCR running-head digits near d.41 a.2 are garbled -- `981 / 9S2 / 953` were really **951 / 952 / 953**. **Printed pp. 980-983 are DIST. XLIII (de peccato in Spiritum sanctum), NOT d.41.** The auto-chunker's stale `line_start: 66064` did not point at the true quaestio title either (the raw file has a corrupted/duplicated d.40<->d.41 concordance region ~66900-66930). **Always confirm printed_pages via a low-dpi PDF render of the running head before committing.**

### d.41 unit inventory (all Tier 2 as of 2026-05-31)

| Unit | Status |
|---|---|
| `d41-littera` | Tier 2 complete |
| `d41-a1-q1` / `q2` / `q3` | Tier 2 complete |
| `d41-a2-q1` | Tier 2 complete |
| `d41-a2-q2` | Tier 2 complete (commit 76408f3, pp.951-953) |
| `d41-a2-q3` | Tier 2 complete |
| `d41-dubia` | Tier 2 complete (commit c81c137) |

### d.42 progress

| Unit | Status |
|---|---|
| `d42-littera` | Tier 2 complete (commit 40e550d, pp.957-959) |
| `d42-divisio` | Tier 2 complete (commit 4a689ee, p.959) |
| `d42-a1-q1` | Tier 2 complete (commit 93e7ad2, pp.960-962) |
| `d42-a1-q2` | Tier 2 complete (commit b302dc0, pp.962-964) |
| `d42-a2-q1` | Tier 2 complete (commit f604e20, pp.964-966, scholion I-II) |
| `d42-a2-q2` | Tier 2 complete (commit 86c8201, pp.967-970, 27-entry apparatus) |
| `d42-a3-q1` | Tier 2 complete (commit 63ccdff, pp.970-973, 20-entry apparatus, Scholion I-II) |
| `d42-a3-q2` | Tier 2 complete (commit 1713aee, pp.973-974, 15-entry apparatus) |
| `d42-dubia` | auto-chunked skeleton (NEXT) |

### Next: d.42 dubia

`bon-sent-II-d42-dubia` (*DUBIA CIRCA LITTERAM MAGISTRI*) — the LAST unit of d.42:
- `DUBIA CIRCA LITTERAM MAGISTRI` / `DUB. I.` at raw **67682**, opening at the bottom of printed **p.974** (PDF 996); continues onto p.975+.
- DUB. I = *utrum peccatum interdum est in aliquo reatu postquam transit actu* (Quaeritur: super quid fundetur reatus sive obligatio ad poenam; opinio 1 = reatus super actum; non probat possibilitas absolutionis; opinio auctoris = duplex obligatio respectu poenae aeternae / temporalis).
- **SHARED p.974 footer split:** p.974 footers 7 (`Vide scholion ad praecedentem quaest.`) and 8 (`Quod insinuatur hic in lit. Magistri c.2 — …postquam transit pro postquam transiit…`) belong to the dubia and are its first two body-footers. a3-q2 consumed p.974 footers 1-6; do NOT re-claim. Then fresh p.975+ footer sequences.
- **Offset:** `pdf = printed + 22`; OCR running-head digits in this band are mangled -- trust running-head *text* + offset and confirm with a low-dpi PDF render before committing.
- After d42-dubia, d.42 is COMPLETE -> advance to d.43-littera. (d.50 is the next decade polish gate.)

**Polish gate:** d.41 is NOT a decade boundary. The d.31-d.40 polish gate already closed; next gate fires at d.50. No polish blocker now.

---

## Standard per-chunk recipe (Vol II)

See project `CLAUDE.md` → "VOL II OVERRIDE" + "Efficient single-chunk subagent dispatch". In brief: PDF-priority inversion (450 dpi column bands authoritative for Respondeo/Solutio/footers; OCR base for clean prose + marker spacing); `extract-pages.py --volume vol2 --dpi 450` then `colcrop.py vol2 <page>`; backup → re-set Latin column-by-column → literal English → full per-page-restart apparatus → frontmatter Tier-2 + `## Notes` → three `--volume 2` audits + smoke build → two commits (chunk+content.json; then resume).
