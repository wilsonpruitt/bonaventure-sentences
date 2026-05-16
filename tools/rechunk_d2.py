#!/usr/bin/env python3.11
"""Regenerate Vol II d.2 chunks from raw OCR using semantic boundaries.

Session 13 (2026-05-15). The auto-chunker mislabeled d.2: non-dup skeletons
held pars-I ranges under p2 ids; -dup2/-dup3 held the real pars-II ranges,
split wrong. Boundaries below verified by grep on raw markers in
raw/bonaventure_vol2_raw.txt (d.2 = lines 4264-6627; d.3 starts 6628).

OCR-garbled headers resolved:
  4264 'DISTmCTIO 11.'      = DISTINCTIO II
  4697 'QU.\\ESTIO 11.'      = QUAESTIO II (p1 a1 q2)
  5108 'QU.\\EST[0 I.'       = QUAESTIO I  (p1 a2 q1)

Lombard's d.2 littera (4264-4417) covers BOTH pars in one block:
  Pars 1 (4265) Cap. I-III ; Pars II (4365) Cap. IV-V.
There is NO separate pars-II littera — pars II commentary (5530) follows
pars I dubia directly. So d.2 has a SINGLE `d2-littera` chunk (the d.1
precedent: bon-sent-II-d1-littera covers "Pars I et II").

Short ARTICULUS openers are folded into that article's q1 (CLAUDE.md
Vol II override step 5 — no standalone aN-divisio chunks).

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
# numbers below were all derived with).
lines = RAW.read_text().split("\n")


def extract(start, end):
    return "\n".join(lines[start - 1:end]).strip()


# (id, type, pars, articulus, quaestio, line_start, line_end, title_la, note)
CHUNKS = [
    ("bon-sent-II-d2-littera", "littera", None, None, None, 4264, 4417,
     "Distinctio II. Magistri Sententiarum (Pars I et II).",
     "Lombard d.2 text, Pars I (Cap. I-III) + Pars II (Cap. IV-V). Single littera (d.1 precedent). printed pp.53-54."),
    ("bon-sent-II-d2-p1-divisio", "divisio", 1, None, None, 4418, 4462,
     "Commentarius in Distinctionem II, Pars I — Divisio textus.",
     "COMMENTARIUS IN DIST. II (4418) + DIVISIO TEXTUS (4425) + TRACTATIO QUAESTIONUM (4444). ARTICULUS I opener folds into a1-q1."),
    ("bon-sent-II-d2-p1-a1-q1", "quaestio", 1, 1, 1, 4463, 4696,
     "(p1 a1 q1)",
     "ARTICULUS I opener (4463-4466) folded in + QUAESTIO I (4467)."),
    ("bon-sent-II-d2-p1-a1-q2", "quaestio", 1, 1, 2, 4697, 4912,
     "(p1 a1 q2)",
     "QUAESTIO II (raw OCR 'QU.\\ESTIO 11.' at 4697)."),
    ("bon-sent-II-d2-p1-a1-q3", "quaestio", 1, 1, 3, 4913, 5097,
     "(p1 a1 q3)",
     "QUAESTIO III (4913). Ends before ARTICULUS II (5098)."),
    ("bon-sent-II-d2-p1-a2-q1", "quaestio", 1, 2, 1, 5098, 5212,
     "Utrum aevum praecedat aliquo modo tempus.",
     "ARTICULUS II opener + 3-q listing (5098-5107) folded in + QUAESTIO I (raw 'QU.\\EST[0 I.' 5108)."),
    ("bon-sent-II-d2-p1-a2-q2", "quaestio", 1, 2, 2, 5213, 5333,
     "(p1 a2 q2)",
     "QUAESTIO II (5213)."),
    ("bon-sent-II-d2-p1-a2-q3", "quaestio", 1, 2, 3, 5334, 5449,
     "(p1 a2 q3)",
     "QUAESTIO III (5334). Ends before DUBIA (5450)."),
    ("bon-sent-II-d2-p1-dubia", "dubia", 1, None, None, 5450, 5529,
     "Dubia circa litteram Magistri (Pars I).",
     "DUBIA CIRCA LITTERAM MAGISTRI (5450): DUB I (5452), DUB II (5479). Ends before COMMENTARIUS Pars II (5530)."),
    ("bon-sent-II-d2-p2-divisio", "divisio", 2, None, None, 5530, 5554,
     "Commentarius in Distinctionem II, Pars II — Divisio textus.",
     "COMMENTARIUS Pars II (5530) + Pars II (5531) + DIVISIO TEXTUS (5539) + TRACTATIO QUAESTIONUM (5548). ARTICULUS I opener folds into a1-q1."),
    ("bon-sent-II-d2-p2-a1-q1", "quaestio", 2, 1, 1, 5555, 5743,
     "(p2 a1 q1)",
     "ARTICULUS I opener (5555-5559) folded in + QUAESTIO I (5560)."),
    ("bon-sent-II-d2-p2-a1-q2", "quaestio", 2, 1, 2, 5744, 5886,
     "(p2 a1 q2)",
     "QUAESTIO II (5744). Ends before ARTICULUS II (5887)."),
    ("bon-sent-II-d2-p2-a2-q1", "quaestio", 2, 2, 1, 5887, 6125,
     "(p2 a2 q1)",
     "ARTICULUS II opener (5887-5896) folded in + QUAESTIO I (5897)."),
    ("bon-sent-II-d2-p2-a2-q2", "quaestio", 2, 2, 2, 6126, 6244,
     "(p2 a2 q2)",
     "QUAESTIO II (6126)."),
    ("bon-sent-II-d2-p2-a2-q3", "quaestio", 2, 2, 3, 6245, 6381,
     "(p2 a2 q3)",
     "QUAESTIO III (6245)."),
    ("bon-sent-II-d2-p2-a2-q4", "quaestio", 2, 2, 4, 6382, 6500,
     "Utrum plures Angeli sint simul in eodem loco.",
     "QUAESTIO IV (6382). Ends before DUBIA (6501)."),
    ("bon-sent-II-d2-p2-dubia", "dubia", 2, None, None, 6501, 6627,
     "Dubia circa litteram Magistri (Pars II).",
     "DUBIA CIRCA LITTERAM MAGISTRI (6501): DUB I, DUB II (6564). Ends before DISTINCTIO III (6628)."),
]

NEW_IDS = {c[0] for c in CHUNKS}


def frontmatter(cid, ctype, pars, art, q, s, e, title_la, note, wc):
    fm = [
        "---",
        f'id: "{cid}"',
        "volume: 2",
        "book: 2",
        "distinctio: 2",
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
        f'transcription_status: "auto-chunked 2026-05-13; rechunked 2026-05-15 session 13 (correct semantic boundaries, raw {s}-{e}) — {note}"',
        "format_version: 1",
        "---",
    ]
    return "\n".join(fm)


# Report orphans (old d2 files not in the new id set) — deleted below.
existing = sorted(OUT.glob("bon-sent-II-d2-*.md"))
print("Existing d2 files:")
for p in existing:
    tag = "OVERWRITE" if p.stem in NEW_IDS else "DELETE (orphan)"
    print(f"  {p.name}: {tag}")
print()

# Delete every old d2 file (clean slate; backup already taken).
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
