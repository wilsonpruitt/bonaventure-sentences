# Opera Omnia Tracker

What it would take to cover all ten Quaracchi volumes of Bonaventure's *Opera
Omnia* end-to-end. Companion to `PLAN.md` (phases) and `progress.md`
(checkbox log). This file is the quantified rollup.

Last updated: 2026-04-14.

> ⛔ **STALE — DO NOT TRUST THE SCOPE TABLE BELOW (noted 2026-08-19).** It reports Vols II, III and
> IV as raw text "❌ empty file" with 0 chunks done. All three are chunked (464 / 412 / 646 files)
> and **Vol III is live**. Every session estimate downstream of that table is therefore wrong.
> Vol V's Hexaemeron front is also far past what this records — the repo's `next-session-resume.md`
> is authoritative for state, always.
>
> ⚠ **The table also never counted the four Sentences Proemia**, which are missing from the corpus
> entirely — see `manual-review/proemia-gap-scoping.md`. Add ~11–14 chunks across Vols I–IV when
> these numbers are next rebuilt.

---

## Velocity assumptions

Calibrated from Phase C (Vol I, d. 1–8). All estimates use *sessions*, not
wall-clock days.

| Step | Current | Post-pipeline (Phase B) |
|---|---|---|
| Raw text scrape (IA `pdftotext`) | 1 session / volume | same |
| Chunking (semantic re-chunk) | 0.5 session / distinction | 0.2 (scripted) |
| Latin body translation (Tier 2) | 3–5 chunks / session | same (bottleneck) |
| Apparatus translation | 0.3 chunks / session (manual) | bundled (tool at 80%) |
| Scholion translation | bundled | bundled |

**Working rule:** 1 distinction ≈ 1–1.5 sessions post-pipeline; 1 volume of
Sentences commentary ≈ 48 distinctions ≈ 60 sessions.

---

## Scope table — all 10 volumes

Chunk counts for Vol I are actual; II–X are estimates from page count ÷ 5
(Vol I ratio). Flag any row as "estimate" until the raw text exists.

| Vol | Works | Printed pp. | Raw text | Chunks (est.) | Done | Sessions needed | Phase |
|----:|---|---:|---|---:|---:|---:|:---:|
| I   | *Comm. in I Sent.* (d. 1–48, pt. 1 + pt. 2) | ~1000 | ⚠️ pt. 1 only (3.1 MB); pt. 2 missing | ~270 | 70 (d. 1–8) | ~80 | **C (active)** |
| II  | *Comm. in II Sent.* (d. 1–44) | ~1100 | ❌ empty file | ~240 | 0 | ~150 | D |
| III | *Comm. in III Sent.* (d. 1–40) | ~900 | ❌ empty file | ~200 | 0 | ~125 | D |
| IV  | *Comm. in IV Sent.* (d. 1–50) | ~1100 | ❌ empty file | ~240 | 0 | ~150 | D |
| V   | *Opuscula Theologica Selecta* — 3 QD (scientia Christi, myst. Trinitatis, perfectione evang.), Breviloquium, Itinerarium, De reductione artium, **Collationes in Hexaemeron** + de septem donis + de decem praeceptis, Sermones selecti | ~580 | ✅ downloaded 2026-07-28 (offset +76; see CLAUDE.md VOL V section) | ~250 | 1 | — | **E (ACTIVE — Breviloquium pilot done 2026-07-28)** |
| VI  | *Comm. in Sacram Scripturam* I — Eccl., Sap., Luke 1–8 | ~700 | ❌ | ~150 | 0 | ~90 | F |
| VII | *Comm. in Sacram Scripturam* II — Luke 9–24, John | ~700 | ❌ | ~150 | 0 | ~90 | F — ⚠ correction 2026-07-28: the *Hexaemeron* is in **Vol V**, not here; the "Hexaemeron priority" flag moves to Vol V |
| VIII| *Opuscula Varia Theologica* — Apologia pauperum, De perfectione vitae ad sorores, De regimine animae, et al. | ~900 | ❌ | ~120 | 0 | ~80 | E/F |
| IX  | *Sermones* (de tempore, de sanctis, de B. V. Maria) | ~800 | ❌ | ~180 | 0 | ~110 | F |
| X   | Prolegomena, indexes, apparatus criticus, fragments | ~350 | ❌ | ~30 | 0 | ~20 | F — Quaracchi's index volume is SUPERSEDED by generated indexes (scripture + cross-ref, see `INDEX-PLAN.md`, approved 2026-07-31); prolegomena/fragments still likely skip |
| **Total** | | **~8150** | | **~1660** | **70** | **~955** | |

---

## Rollup — what it would take

- **Sessions to finish Vol I (current phase):** ~80.
- **Sessions to finish the full Sentences (Vols I–IV):** ~505. At 3 sessions/week = ~3 years.
- **Sessions for everything (I–X):** ~955. At 3 sessions/week = ~6 years.
- **Minimum viable Opera Omnia** (I–IV + *Itinerarium* + *Breviloquium* + *Hexaemeron* + *Reductio*): ~540 sessions. ~3.5 years.

**Headline:** linear solo work is not viable past Vol I. The path to full
coverage requires:

1. **Phase B pipeline shipped** (batch vision OCR, apparatus v2, chunk
   scaffolding). Current per-chunk cost must drop 3–5×.
2. **Raw text acquired** for Vols II–X from Internet Archive — one
   focused session per volume. Blocking for everything downstream.
3. **Parallel translation agents** (deferred; see
   `feedback_agent-token-accounting`) once scaffolding makes each chunk a
   self-contained task.
4. **Tier-3 draft tier accepted** for Vols V–X. Tier 2 quality across
   ~1590 un-started chunks is ~900 sessions; Tier 3 with a "draft" badge
   and on-demand upgrade is ~400 sessions.

---

## Per-volume readiness checklist

Track one volume per row. A volume is "ready for translation" only when all
five boxes are checked.

| Vol | PDF | Raw `.txt` | Chunks written | Sigla registry | Translation-pending skeletons |
|----:|:---:|:---:|:---:|:---:|:---:|
| I   | ✅  | ✅ (pt. 1) | partial (135 legacy + 70 Tier 2) | ✅ | ❌ (manual chunk-by-chunk) |
| II  | ❌  | ❌ | ❌ | ❌ | ❌ |
| III | ❌  | ❌ | ❌ | ❌ | ❌ |
| IV  | ❌  | ❌ | ❌ | ❌ | ❌ |
| V   | ❌  | ❌ | ❌ | ❌ | ❌ |
| VI  | ❌  | ❌ | ❌ | ❌ | ❌ |
| VII | ❌  | ❌ | ❌ | ❌ | ❌ |
| VIII| ❌  | ❌ | ❌ | ❌ | ❌ |
| IX  | ❌  | ❌ | ❌ | ❌ | ❌ |
| X   | ❌  | ❌ | ❌ | ❌ | ❌ |

---

## Decisions this tracker should drive

1. **Commit to Tier 2 for I–IV, Tier 3 for V–X?** If yes, total shrinks
   from ~955 to ~540 sessions.
2. **Download Vol I pt. 2 PDF** — without it, Vol I caps at d. 23. Vol I
   pt. 2 on IA: `doctorisseraphic12bona`.
3. **Prioritize *Itinerarium* as a showcase Opusculum** before finishing
   Vol I? It's short (2–3 sessions), famous, and would broaden the site's
   audience while Vol I grinds.
4. **Partner recruitment.** At 3 sessions/week solo, this is a 3–6 year
   project. Two additional translators at the same cadence compress the
   Sentences to ~1 year.

---

## Agent-driven cost estimate (added 2026-04-14)

Once the agent pipeline ships (`tools/build-task-packet.py` + `tools/validate-chunk.py`,
plus per-distinction rechunk scripts modeled on `tools/rechunk_d9.py`), the
bottleneck shifts from solo translation to **human audit**.

### Per-chunk measurements

Measured on `bon-sent-I-d9-a1-q1` (412-line raw chunk, 1 articulus-unicus quaestio):

| Component | Words | Tokens (≈ 1.35× words) |
|---|---:|---:|
| Task packet input (prompt + glossary + Latin body) | 3,276 | ~4,400 |
| Expected agent output (En body 1.2× La + apparatus En + scholion En + notes) | ~2,800 | ~3,800 |

Bigger chunks (e.g. dubia or littera, 800+ raw lines) will run 2–3× larger.
Average across d.9's 7 chunks: input ~6.5k, output ~5k tokens per chunk.

### Cost per chunk (average)

| Model | Input $ | Output $ | **Per chunk** |
|---|---:|---:|---:|
| Sonnet 4.6 ($3/M in, $15/M out) | $0.020 | $0.075 | **$0.10** |
| Opus 4.6 ($15/M in, $75/M out) | $0.098 | $0.375 | **$0.47** |

### Project rollup

Chunk counts from the scope table above (1660 total; 70 done; 1590 remaining):

| Scope | Chunks | Sonnet API $ | Opus API $ |
|---|---:|---:|---:|
| Vol I finish (~190 remaining; d.9 = 7 done) | 190 | $19 | $89 |
| Sentences I–IV (II–IV blocked on raw scrape) | 950 | $95 | $447 |
| Full Opera Omnia I–X | 1,590 | $159 | $747 |

### Realistic API budget (with re-runs)

Raw per-chunk math undercounts because (a) littera + dubia chunks run 2–3×
the average size, and (b) ~30% of chunks need re-translation after audit
or validator failure. Applying both:

| Scope | Chunks | Effective $/chunk (Opus, with re-runs) | **Total** |
|---|---:|---:|---:|
| Vol I finish | 190 | ~$0.75 | **~$140** |
| Sentences I–IV | 950 | ~$0.75 | **~$700** |
| Full Opera I–X | 1,590 | ~$0.75 | **~$1,200** |

Max plan removes window throttling, so wall time = (parallel agent
throughput) + (human audit). The first is hours; the second is the binding
constraint.

### Human audit — the actual bottleneck

Audit is not optional (per `feedback_bonaventure-translation-depth.md`).
At 5 min/chunk human review:

- Vol I finish: ~16 hrs audit
- Sentences I–IV: ~80 hrs audit
- Full Opera: ~130 hrs audit

Audit can't be parallelized. At 10 hrs/week of evening review, full Opera
= ~3 months. **Getting audit time down is the lever** — agents have already
collapsed translation; if a 1-min/chunk skim suffices for most chunks
(deep-read only the doctrinally complex ones), full Opera audit drops to
~30 hrs / ~3 weeks.

### Prerequisites still needed before agent rollout

1. **Re-chunk d.10–23** (~14 distinctions × 30 min scripting + inspection per d.8 lessons on OCR-garbled headers like `QIIAESTIO`).
2. **Download Vol I pt. 2 PDF** (`doctorisseraphic12bona`) and Vol II–IV via Internet Archive.
3. **Generalize `rechunk_d9.py` → `rechunk.py`** with per-distinction config so the same script handles all distinctions in I–IV.
4. **Seed `apparatus-sigla.json` for Vols II–IV** before agents run on those volumes (low-confidence apparatus otherwise).
5. **Wire `apparatus-translate.py` into `build-task-packet.py`** so the agent gets a draft apparatus rather than translating from scratch (saves ~500 tokens/chunk and improves citation accuracy).

---

## How to update this file

- When a chunk is completed, bump the "Done" column for its volume.
- When a volume's raw text is scraped, flip its ✅ in the readiness table
  and re-estimate chunks from `wc -l raw/bonaventure_vol{N}_raw.txt / 500`.
- When Phase B ships, re-baseline "Sessions needed" for all rows using the
  post-pipeline rate.
- Don't duplicate progress.md's checkbox log here — this file is for the
  scope rollup; progress.md is the per-step journal.
