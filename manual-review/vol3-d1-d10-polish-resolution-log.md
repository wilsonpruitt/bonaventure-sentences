# Vol III d.1–d.10 — Decade Polish-Blocker Resolution Log

Polish-blocker gate fired when `bon-sent-III-d10-*` closed. Three locked-in passes
over Vol III d.1–d.10 per CLAUDE.md "Polish-blocker cadence (every 10 distinctions)".
Active volume: Vol III (`raw/doctorisseraphic03bona.pdf`, `raw/bonaventure_vol3_raw.txt`,
offset pdf = printed + 22).

- Pass 1 — `[?]` flag resolution: completed (see below).
- Pass 2 — full-corpus style/formatting audit: completed (see below).
- Pass 3 — cross-chunk boundary integrity sweep: completed (see below).

## Pass 1 — `[?]` flag resolution

Scan of all 114 Vol III d.1–d.10 chunks (inline `[?]` + `## Notes` blocks; no per-chunk
`tier2-ambiguities` logs exist for Vol III). Nearly every occurrence was a "**[?] flags:
NONE**" declaration. The Quaracchi editor's own bracketed variant-queries reproduced
verbatim (`[substantificatio?]` in d10-a1-q2 `[^p229-3]`; `[reading?]`/`[qui?]` glosses in
d3-p1-a1-q2 / d3-p2-a1-q2) are source text, not our flags — left as-is. **Exactly one
genuine parked flag:** `d9-a2-q3` p.219 footers `[^1c]`/`[^2c]`/`[^3c]`, "lightly
reconstructed" from running citations.

- **RESOLVED `bon-sent-III-d9-a2-q3` p.219 footers** (eyes-on 600 dpi, PDF 241). The
  reconstruction was wrong on all three notes; corrected verbatim from the printed
  left-column footer, and a missing fourth note was recovered:
  - `[^1c]` (¹ on *summa veritas*): *Cfr. infra d. 24. a. 1. q. 2; d. 26. a. 1. q. 3;
    d. 27. a. 1. q. 1. — Subinde pro Hoc autem cod. T Hoc modo, cod. A Hoc tantum.*
  - `[^2c]` (² on *Enchiridio*): *Cap. 2. n. 1. seq. Vide q. praeced. arg. 1. ad oppos.
    — Paulo ante codd. F K U sperando in Deum…*
  - `[^3c]` (³ on *quidam ponunt*): *Edd. ponant. Cod. bb unde [cod. Z inde] quidam ponunt.*
  - `[^4c]` **NEW** (⁴ on terminal *accipiendi*): *Vide scholion ad praecedentem quaest.*
    — anchor added to both bodies.
  The "lightly reconstructed / flag for d.10 polish" caveat in `## Notes` was replaced with
  a RESOLVED disposition. q3/q4 boundary confirmed clean (q3 ends *…modum accipiendi⁴*;
  QUAESTIO IV opens immediately on the same page).

No other open `[?]` flags remain in Vol III d.1–d.10.

## Pass 2 — full-corpus style/formatting audit

`tools/audit-style-formatting.py` was extended to walk Vol III (114 Tier-2 chunks) in
addition to Vol I (406) + Vol II (448) — the pass is full-corpus per the cadence. Six
flags surfaced, all in Vol III; dispositioned:

- **`anchor_only_la` (2) — FIXED.** Footnote marker present in the Latin body but dropped
  from the English: `d9-a1-q2` `[^20]` (added after "The Damascene", mirroring
  *Narrat tamen Damascenus[^20]*); `d9-a2-q2` `[^10]` (added at the start of reply *To 2*,
  mirroring *Ad[^10] illud*). Footnote defs were intact; only the English in-text superscript
  was missing.
- **`en_indent_mix` (2) — FIXED.** `d1-a2-q3` and `d3-p2-a3-q2` mixed 5- and 6-space
  `**En.**` apparatus indents; normalized the 6-space lines to the corpus-standard 5.
- **`orphan_app_defs` (2):**
  - `d5-littera` `[^2]`/`[^3]`/`[^4]` — **FIXED** (eyes-on p.118/119, PDF 140/141). All four
    NOTAE superscripts ¹²³⁴ are on p.118. Body anchors for 2/3/4 were missing from both
    languages and `[^1]` was mis-placed onto the *de Fide ad Petrum* lemma (that lemma is
    note ²). Re-anchored: ¹ on *vel* (*persona personam, vel natura naturam*); ² on
    *de Fide ad Petrum*; ³ on *…in sacra Pagina exstiterunt*; ⁴ on *Concilio Toletano sexto*
    — mirrored in English. The `<!-- page 119 -->` break was wrongly placed before the
    Toledo VI quote (which is on p.118); moved it after *…non quod commune* / before
    *est Trinitati*. Fixed a roman→arabic glitch in the `[^3]` def (*edd. I, 8* → *1, 8*).
  - `d5-a2-q4` `[^11]` — **ACCEPTED (by design).** The def is explicitly a scholion
    source-reference with no body marker (*"(Scholion source-reference — no body marker.)"*),
    a Quaracchi pattern; not an error. This is the single remaining audit flag and is expected.

Final audit after fixes: 1 flag (the accepted `d5-a2-q4 [^11]`). Smoke build clean.

## Pass 3 — Boundary integrity sweep

**Summary: 80 same-distinction shared-printed-page boundaries checked, 0 anomalies, 0 fixes applied.**

Scope: every chunk boundary within Vol III d.1–d.10 where the prior chunk's last
`printed_pages` value equals the next chunk's first (i.e. the two chunks share a
printed page; a quaestio / divisio / scholion / dubia split mid-page). Reading order
within each distinction: littera → divisio → articles (aN-qM) → dubia, with pars
distinctions (d.3) ordered p1 then p2. 80 such boundaries enumerated.

Per-boundary checks (CLAUDE.md Pass 3 (a)/(b)/(c)):
- **(a) continuity** — receiving chunk's opening `## Latin` sentence is grammatically
  continuous with the prior chunk's closing `## Latin` sentence.
- **(b) footer hand-off ledger** — the shared page's footer notes are fully accounted
  for across the two chunks; prior chunk's "forwarded" note ranges reconcile with the
  next chunk's "received/picked-up" ranges (and silence on one side is flagged).
- **(c) no cascade-merge splice** — prior chunk's tail parses as grammatical Latin
  (no mid-sentence splice / silent drop of near-identical clauses — the IA djvu OCR
  failure signature).

Method: worked from each chunk's `## Latin` tail/head and `## Notes` hand-off ledgers
(every one of the 114 d.1–d.10 chunks carries a `## Notes` block; all 80 boundaries
have reciprocated incoming/forward footer ledgers). No anomaly required a PDF
column-band re-render: every prior-tail terminates in a complete sentence (full stop,
closed quotation `»`, or a terminal scholion doctor-citation list), and every
next-head opens a self-standing new unit (`Secundo/Tertio/Quarto … quaeritur …`,
`Consequenter quaeritur …`, `Circa primum sic proceditur …`, `In parte ista sunt
dubitationes/quaestiones circa litteram …`, or a fresh `COMMENTARIUS … DIVISIO TEXTUS`).
No dangling clause, no mid-word truncation, no near-identical-clause splice was found
at any of the 80 seams.

**Cascade-merge (check c) result: NONE detected** across all 80 boundaries. The d9-divisio
(s66)-class failure that motivated this pass (silent ~170-word drop at a mid-page seam)
does not recur anywhere in Vol III d.1–d.10.

Three boundaries carried a forecast-vs-eyes-on footer-ownership correction that was
already resolved at build time (documented in the chunk `## Notes`, apparatus rendered
to the corrected ledger) — recorded here as reconciled, not live anomalies:
- p.121 d5-divisio → d5-a1-q1: d5-divisio's `## Notes` corrects a confused d5-littera
  note about p.118 left-column footers; ownership resolved (divisio owns p.121 nn.1–4,
  q1 leads at p.121 n.5). Reconciled.
- p.209 d9-a1-q4 → d9-a1-q5: d9-a1-q5 records that q4's "p.209 nn.6–10 forwarded"
  forecast was a slight mis-statement — q4's footers were fully on pp.207–208; q5 owns
  its own p.209+ sequence. Reconciled eyes-on.
- p.225 d10-divisio → d10-a1-q1: forecast forwarded "p.225 nn.1–3"; eyes-on q1 carries
  all of p.225 nn.1–5. Reconciled eyes-on; apparatus matches.

### Per-boundary disposition (80)

- p.  7  d1-littera → d1-divisio  — CLEAN
- p.  8  d1-divisio → d1-a1-q1  — CLEAN
- p. 16  d1-a1-q3 → d1-a1-q4  — CLEAN
- p. 18  d1-a1-q4 → d1-a2-q1  — CLEAN
- p. 21  d1-a2-q1 → d1-a2-q2  — CLEAN
- p. 28  d1-a2-q2 → d1-a2-q3  — CLEAN
- p. 31  d1-a2-q3 → d1-a2-q4  — CLEAN
- p. 33  d1-a2-q4 → d1-dubia  — CLEAN
- p. 36  d2-littera → d2-divisio  — CLEAN
- p. 39  d2-a1-q1 → d2-a1-q2  — CLEAN
- p. 43  d2-a1-q3 → d2-a2-q1  — CLEAN
- p. 46  d2-a2-q1 → d2-a2-q2  — CLEAN
- p. 49  d2-a2-q3 → d2-a3-q1  — CLEAN
- p. 54  d2-a3-q2 → d2-a3-q3  — CLEAN
- p. 56  d2-a3-q3 → d2-dubia  — CLEAN
- p. 60  d3-p1-littera → d3-p1-divisio  — CLEAN
- p. 65  d3-p1-a1-q1 → d3-p1-a1-q2  — CLEAN
- p. 70  d3-p1-a1-q2 → d3-p1-a1-q3  — CLEAN
- p. 72  d3-p1-a1-q3 → d3-p1-a2-q1  — CLEAN
- p. 74  d3-p1-a2-q1 → d3-p1-a2-q2  — CLEAN
- p. 76  d3-p1-a2-q2 → d3-p1-a2-q3  — CLEAN
- p. 78  d3-p1-a2-q3 → d3-p1-dubia  — CLEAN
- p. 80  d3-p1-dubia → d3-p2-divisio  — CLEAN
- p. 81  d3-p2-divisio → d3-p2-a1-q1  — CLEAN
- p. 87  d3-p2-a2-q1 → d3-p2-a2-q2  — CLEAN
- p. 90  d3-p2-a2-q2 → d3-p2-a3-q1  — CLEAN
- p. 92  d3-p2-a3-q1 → d3-p2-a3-q2  — CLEAN
- p. 94  d3-p2-a3-q2 → d3-p2-dubia  — CLEAN
- p. 97  d4-littera → d4-divisio  — CLEAN
- p.100  d4-a1-q1 → d4-a1-q2  — CLEAN
- p.104  d4-a1-q3 → d4-a2-q1  — CLEAN
- p.106  d4-a2-q1 → d4-a2-q2  — CLEAN
- p.108  d4-a2-q2 → d4-a2-q3  — CLEAN
- p.113  d4-a3-q1 → d4-a3-q2  — CLEAN
- p.115  d4-a3-q2 → d4-a3-q3  — CLEAN
- p.116  d4-a3-q3 → d4-dubia  — CLEAN
- p.121  d5-divisio → d5-a1-q1  — CLEAN (footer ledger self-correction reconciled; see note above)
- p.124  d5-a1-q1 → d5-a1-q2  — CLEAN
- p.125  d5-a1-q2 → d5-a1-q3  — CLEAN
- p.126  d5-a1-q3 → d5-a1-q4  — CLEAN
- p.128  d5-a1-q4 → d5-a1-q5  — CLEAN
- p.132  d5-a2-q1 → d5-a2-q2  — CLEAN
- p.135  d5-a2-q2 → d5-a2-q3  — CLEAN
- p.140  d5-a2-q4 → d5-a2-q5  — CLEAN
- p.142  d5-a2-q5 → d5-dubia  — CLEAN
- p.146  d6-littera → d6-divisio  — CLEAN
- p.148  d6-divisio → d6-a1-q1  — CLEAN
- p.152  d6-a1-q1 → d6-a1-q2  — CLEAN
- p.154  d6-a1-q2 → d6-a1-q3  — CLEAN
- p.159  d6-a2-q1 → d6-a2-q2  — CLEAN
- p.162  d6-a2-q2 → d6-a2-q3  — CLEAN
- p.168  d7-littera → d7-divisio  — CLEAN
- p.169  d7-divisio → d7-a1-q1  — CLEAN
- p.173  d7-a1-q1 → d7-a1-q2  — CLEAN
- p.175  d7-a1-q2 → d7-a1-q3  — CLEAN
- p.179  d7-a2-q1 → d7-a2-q2  — CLEAN
- p.182  d7-a2-q3 → d7-dubia  — CLEAN
- p.185  d8-littera → d8-divisio  — CLEAN
- p.185  d8-divisio → d8-a1-q1  — CLEAN
- p.189  d8-a1-q2 → d8-a1-q3  — CLEAN
- p.193  d8-a2-q1 → d8-a2-q2  — CLEAN
- p.195  d8-a2-q2 → d8-a2-q3  — CLEAN
- p.197  d8-a2-q3 → d8-dubia  — CLEAN
- p.199  d9-divisio → d9-a1-q1  — CLEAN
- p.202  d9-a1-q1 → d9-a1-q2  — CLEAN
- p.205  d9-a1-q2 → d9-a1-q3  — CLEAN
- p.209  d9-a1-q4 → d9-a1-q5  — CLEAN (footer ledger self-correction reconciled; see note above)
- p.211  d9-a1-q5 → d9-a1-q6  — CLEAN
- p.213  d9-a1-q6 → d9-a2-q1  — CLEAN
- p.216  d9-a2-q2 → d9-a2-q3  — CLEAN
- p.219  d9-a2-q3 → d9-a2-q4  — CLEAN
- p.221  d9-a2-q4 → d9-dubia  — CLEAN
- p.224  d10-littera → d10-divisio  — CLEAN
- p.225  d10-divisio → d10-a1-q1  — CLEAN (footer ledger self-correction reconciled; see note above)
- p.227  d10-a1-q1 → d10-a1-q2  — CLEAN
- p.229  d10-a1-q2 → d10-a1-q3  — CLEAN
- p.232  d10-a1-q3 → d10-a2-q1  — CLEAN
- p.235  d10-a2-q1 → d10-a2-q2  — CLEAN
- p.237  d10-a2-q2 → d10-a2-q3  — CLEAN
- p.238  d10-a2-q3 → d10-dubia  — CLEAN

**Disposition: Pass 3 closed CLEAN. No content fixes applied; no chunk files modified.**
Note (b) for d.8 p.185: this printed page is shared by THREE chunks in reading order
(d8-littera → d8-divisio → d8-a1-q1); both consecutive seams on p.185 were checked and
the p.185 footer split (littera nn.1–4 / divisio nn.1–2 / a1-q1 from n.3) reconciles
across all three.
