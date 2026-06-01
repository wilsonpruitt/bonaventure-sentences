# Bonaventure Sentences — Next Session Resume

**Last updated:** 2026-05-31 (d42-a2-q1 promoted -> Tier 2, commit f604e20)

**Branch:** master

## NEXT ACTION -> `bon-sent-II-d42-a2-q2` (d.42 a2-q1 now Tier 2)

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
| `a2-q2`, `a3-q1` / `q2`, `d42-dubia` | auto-chunked skeleton (NEXT: a2-q2) |

### Next: d.42 a2-q2

`bon-sent-II-d42-a2-q2` (*Utrum veniale conveniat cum mortali in reatu poenae aeternae*):
- `QUAESTIO II.` opener `Secundo quaeritur, utrum veniale conveniat cum mortali in reatu poenae aeternae` at raw **67196**, opening on printed **p.967** (PDF 989). Alignment = q2 (`Secundo quaeritur… reatu poenae aeternae`).
- **`has_scholion: false`** — Scholion II ("Quoad sequentem (2.) quaest.") is held in a2-q1 and covers this question. No q1 footer migrates forward; a2-q2's apparatus begins with the fresh p.967 footer sequence.
- After a2-q2 come a3-q1/q2 and d42-dubia -- all still auto-chunked skeletons (apparatus audit diffs +19 to +52).
- **Offset:** `pdf = printed + 22`; OCR running-head digits in this band are mangled -- trust running-head *text* + offset and confirm with a low-dpi PDF render before committing.

**Polish gate:** d.41 is NOT a decade boundary. The d.31-d.40 polish gate already closed; next gate fires at d.50. No polish blocker now.

---

## Standard per-chunk recipe (Vol II)

See project `CLAUDE.md` → "VOL II OVERRIDE" + "Efficient single-chunk subagent dispatch". In brief: PDF-priority inversion (450 dpi column bands authoritative for Respondeo/Solutio/footers; OCR base for clean prose + marker spacing); `extract-pages.py --volume vol2 --dpi 450` then `colcrop.py vol2 <page>`; backup → re-set Latin column-by-column → literal English → full per-page-restart apparatus → frontmatter Tier-2 + `## Notes` → three `--volume 2` audits + smoke build → two commits (chunk+content.json; then resume).
