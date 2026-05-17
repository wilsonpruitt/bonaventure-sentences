#!/usr/bin/env python3.11
"""Regenerate Vol II d.4 chunks from raw OCR using semantic boundaries.

Session 33 (2026-05-17). Adapted from tools/rechunk_d3.py. The auto-chunker
gave d.4 OLD line-count bounds (divisio started 6 lines late, missing the
COMMENTARIUS header; a1/a2/a3-q1 did not fold their ARTICULUS openers).
Boundaries below verified by grep/awk on raw markers in
raw/bonaventure_vol2_raw.txt:

  d.4 = lines 9661-10585.
  d.4 begins at semantic `DISTINCTIO IV.` (9661) + `Cap. I.` Lombard text
  ("An perfecti et beati creati sint, an miseri et imperfecti").
  d.5 starts at semantic `DISTINCTIO V.` (10586); the `DISTINCTIO V.  143`
  at line 10570 is a page-top running-head bleed, NOT the boundary
  (DUB. III's Respondeo runs 10572-10585 below that bleed).

d.4 is SINGLE-PARS — running heads are `DIST. IV. ART. I/II/III` with NO
`P. I/II`, so there is no pars division (contrast d.1/d.2/d.3). Chunk ids
carry no `-p{N}-` segment; pars=None throughout.

OCR-garbled headers resolved (running-head text + +22 offset, never OCR digits):
   9661 'DISTINCTIO IV.'                = d.4 littera, Lombard Cap. I
   9722 'COMMENTARIUS IN DI8TINCTI0NEM lY.' = COMMENTARIUS IN DISTINCTIONEM IV
   9745 'TRACTATIO QUAESTIONUM.'        = tractatio (stays in divisio chunk)
   9763 'ARTICULUS I.'                  = ART. I (folds into a1-q1)
  10057 'ARTICULUS II.'                 = ART. II (folds into a2-q1)
  10261 'ARTICULUS III.'                = ART. III (folds into a3-q1)
  10529 'DUBIA CIRCA LITTERAM MAGISTRI.'= dubia (DUB I-III)

Lombard's d.4 littera (9661-9721) is one short chapter; the p.129
`NOTAE AD LIBR. SENTENTIARUM` block is d4-littera's apparatus (cross-
distinction footer split already documented in committed d3-p2-dubia
Notes — resolved at the d4-littera Tier-2 build, no backfill into d.3).

Short ARTICULUS openers are folded into that article's q1 (CLAUDE.md
Vol II override step 5 — no standalone aN-divisio chunks). The
`divisio` chunk holds COMMENTARIUS + DIVISIO TEXTUS + TRACTATIO QUAESTIONUM.

Writes Latin body = raw OCR; English/apparatus are skeleton placeholders.
Tier-2 promotion re-sets each chunk against the 450 dpi column-band PDF.
"""
from pathlib import Path

ROOT = Path("/Users/wilsonpruitt/bonaventure-sentences")
RAW = ROOT / "raw/bonaventure_vol2_raw.txt"
OUT = ROOT / "vol2"

# NOTE: split on "\n" only — NOT splitlines(). The Vol II raw has 1056 form
# feeds (\f, page-start sentinels); str.splitlines() also splits on \f and
# would shift every line number ~1055 off from grep/awk (which the boundary
# numbers below were all derived with). Same fix as rechunk_d2.py / d3.py.
lines = RAW.read_text().split("\n")


def extract(start, end):
    return "\n".join(lines[start - 1:end]).strip()


# (id, type, pars, articulus, quaestio, line_start, line_end, title_la, note)
CHUNKS = [
    ("bon-sent-II-d4-littera", "littera", None, None, None, 9661, 9721,
     "Distinctio IV. Magistri Sententiarum.",
     "Lombard d.4 text (single Cap.: an perfecti et beati creati sint, an miseri et imperfecti). p.129 NOTAE AD LIBR. SENTENTIARUM is this chunk's apparatus (cross-dist. split documented in committed d3-p2-dubia). Ends before COMMENTARIUS (9722)."),
    ("bon-sent-II-d4-divisio", "divisio", None, None, None, 9722, 9762,
     "Commentarius in Distinctionem IV — Divisio textus.",
     "COMMENTARIUS IN DISTINCTIONEM IV (9722) + DIVISIO TEXTUS + TRACTATIO QUAESTIONUM (9745). ARTICULUS I opener (9763) folds into a1-q1. Ends before ARTICULUS I (9763)."),
    ("bon-sent-II-d4-a1-q1", "quaestio", None, 1, 1, 9763, 9872,
     "Quales creati sunt Angeli quoad gloriam et gratiam — utrum in gratia creati fuerint.",
     "ARTICULUS I opener (9763) + title (9765) folded in + QUAESTIO I (9767). Ends before QUAESTIO II (9873)."),
    ("bon-sent-II-d4-a1-q2", "quaestio", None, 1, 2, 9873, 10056,
     "Utrum Angeli in primo instanti suae creationis gloriam habere potuerint.",
     "QUAESTIO II (9873). Ends before ARTICULUS II (10057)."),
    ("bon-sent-II-d4-a2-q1", "quaestio", None, 2, 1, 10057, 10162,
     "De Angelis quoad futuri eventus praescientiam — utrum bonis revelari debuerit futura permansio.",
     "ARTICULUS II opener (10057) + title (10059) + sub-divisio (10061-10063) folded in + QUAESTIO I (10065). Ends before QUAESTIO II (10163)."),
    ("bon-sent-II-d4-a2-q2", "quaestio", None, 2, 2, 10163, 10260,
     "Utrum malis Angelis revelari potuerit sua damnatio.",
     "QUAESTIO II (10163). Ends before ARTICULUS III (10261)."),
    ("bon-sent-II-d4-a3-q1", "quaestio", None, 3, 1, 10261, 10437,
     "De cognitione matutina et vespertina Angelorum — utrum cognitionem matutinam habuerint in ipsa creatione.",
     "ARTICULUS III opener (10261) + title (10263) + sub-divisio (10265-10268) folded in + QUAESTIO I (10270). Ends before QUAESTIO II (10438)."),
    ("bon-sent-II-d4-a3-q2", "quaestio", None, 3, 2, 10438, 10528,
     "Utrum Angeli cognitionem vespertinam habuerint post glorificationem.",
     "QUAESTIO II (10438). Ends before DUBIA CIRCA LITTERAM MAGISTRI (10529)."),
    ("bon-sent-II-d4-dubia", "dubia", None, None, None, 10529, 10585,
     "Dubia circa litteram Magistri.",
     "DUBIA CIRCA LITTERAM MAGISTRI (10529): DUB I (10531), DUB II (10537), DUB III (10572 — below the p.143 DISTINCTIO V running-head bleed at 10570). Ends before semantic DISTINCTIO V (10586)."),
]

NEW_IDS = {c[0] for c in CHUNKS}


def frontmatter(cid, ctype, pars, art, q, s, e, title_la, note, wc):
    fm = [
        "---",
        f'id: "{cid}"',
        "volume: 2",
        "book: 2",
        "distinctio: 4",
    ]
    if pars is not None:
        fm.append(f"pars: {pars}")
    if art is not None:
        fm.append(f"articulus: {art}")
    if q is not None:
        fm.append(f"quaestio: {q}")
    fm += [
        f"type: {ctype}",
        f'title_la: "{title_la}"',
        f'title_en: ""',
        f"line_start: {s}",
        f"line_end: {e}",
        f"word_count_latin: {wc}",
        f'transcription_status: "auto-chunked 2026-05-13; rechunked 2026-05-17 session 33 (correct semantic boundaries, raw {s}-{e}) — {note}"',
        "format_version: 1",
        "---",
    ]
    return "\n".join(fm)


# Report orphans (old d4 files not in the new id set) — deleted below.
existing = sorted(OUT.glob("bon-sent-II-d4-*.md"))
print("Existing d4 files:")
for p in existing:
    tag = "OVERWRITE" if p.stem in NEW_IDS else "DELETE (orphan)"
    print(f"  {p.name}: {tag}")
print()

# Delete every old d4 file (clean slate; backup already taken).
for p in existing:
    p.unlink()

for cid, ctype, pars, art, q, s, e, title_la, note in CHUNKS:
    body = extract(s, e)
    wc = len(body.split())
    fm = frontmatter(cid, ctype, pars, art, q, s, e, title_la, note, wc)
    md = f"{fm}\n\n# {cid}\n\n## Latin\n\n{body}\n\n## English\n\n[Translation pending]\n\n## Apparatus\n\n[Apparatus pending]\n"
    (OUT / f"{cid}.md").write_text(md)
    print(f"Wrote {cid}.md ({s}-{e}, {e - s + 1} lines, {wc} words)")

print(f"\nDone. {len(CHUNKS)} chunks. Tier-2 promote littera + divisio next.")
