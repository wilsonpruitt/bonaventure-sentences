#!/usr/bin/env python3.11
"""Regenerate Vol II d.3 chunks from raw OCR using semantic boundaries.

Session 31 (2026-05-16). Adapted from tools/rechunk_d2.py. The auto-chunker
mislabeled d.3 (dup2 skeletons, wrong splits). Boundaries below verified by
grep/awk on raw markers in raw/bonaventure_vol2_raw.txt
(d.3 = lines 6628-9660; d.4 starts 9661 — semantic `DISTINCTIO IV.` at 9661
immediately followed by `Cap. I.` + Lombard text "An perfecti et beati creati
sint…"; the earlier `DISTINCTIO IV.  129` at line 9631 is a page-top
running-head bleed, NOT the semantic boundary).

OCR-garbled headers resolved (running-head text + +22 offset, never OCR digits):
  6628 'DISTINCTIO III. / Pars I.'   = DISTINCTIO III, littera (Cap. I-VI)
  6817 'COMMENTAPJUS IN DIST. III.'  = COMMENTARIUS … Pars I
  6855 'ARTICULUS 1.'                = ARTICULUS I (folds into p1-a1-q1)
  7814 'ARTICULUS  II.'              = ARTICULUS II (folds into p1-a2-q1)
  8477 'C0MMENTARIU8 IN DIST. III.'  = COMMENTARIUS … Pars II
  8507 'ARTIGULUS  I.'               = ARTICULUS I (folds into p2-a1-q1)
  8858 'ARTIGULUS II.'               = ARTICULUS II (folds into p2-a2-q1)
  9323 'ARTICULUS  111.'             = ARTICULUS III (folds into p2-a3-q1)
  9602 'DUBIA GIRCA LITTERAM MAGISTRL' = DUBIA CIRCA LITTERAM MAGISTRI (Pars II)

Lombard's d.3 littera (6628-6816) covers BOTH pars in one block:
  Pars I (6629) Cap. I-III ; Pars II Cap. IV-VI.
There is NO separate pars-II littera (the d.1/d.2 precedent). So d.3 has a
SINGLE `d3-littera` chunk.

Short ARTICULUS openers are folded into that article's q1 (CLAUDE.md
Vol II override step 5 — no standalone aN-divisio chunks). The pars-level
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
# numbers below were all derived with). Same fix as rechunk_d2.py.
lines = RAW.read_text().split("\n")


def extract(start, end):
    return "\n".join(lines[start - 1:end]).strip()


# (id, type, pars, articulus, quaestio, line_start, line_end, title_la, note)
CHUNKS = [
    ("bon-sent-II-d3-littera", "littera", None, None, None, 6628, 6816,
     "Distinctio III. Magistri Sententiarum (Pars I et II).",
     "Lombard d.3 text, Pars I (Cap. I-III) + Pars II (Cap. IV-VI). Single littera (d.1/d.2 precedent). Ends before COMMENTARIUS Pars I (6817)."),
    ("bon-sent-II-d3-p1-divisio", "divisio", 1, None, None, 6817, 6858,
     "Commentarius in Distinctionem III, Pars I — Divisio textus.",
     "COMMENTARIUS IN DIST. III Pars I (6817) + DIVISIO TEXTUS (6824) + TRACTATIO QUAESTIONUM (6836). ARTICULUS I opener (6855) folds into a1-q1."),
    ("bon-sent-II-d3-p1-a1-q1", "quaestio", 1, 1, 1, 6859, 7220,
     "Utrum Angeli sint compositi ex materia et forma.",
     "ARTICULUS I opener folded in + QUAESTIO I (6859). Ends before QUAESTIO II (7221)."),
    ("bon-sent-II-d3-p1-a1-q2", "quaestio", 1, 1, 2, 7221, 7579,
     "Utrum materia, ex qua compositi sunt Angeli, sit eadem cum materia corporalium.",
     "QUAESTIO II (7221). Ends before QUAESTIO III (7580)."),
    ("bon-sent-II-d3-p1-a1-q3", "quaestio", 1, 1, 3, 7580, 7813,
     "Utrum materia corporalium et incorporalium sit una numero.",
     "QUAESTIO III (7580). Ends before ARTICULUS II (7814)."),
    ("bon-sent-II-d3-p1-a2-q1", "quaestio", 1, 2, 1, 7814, 7972,
     "Utrum in Angelis sit mera discretio personalis.",
     "ARTICULUS II opener (7814) folded in + QUAESTIO I (7824). Ends before QUAESTIO II (7973)."),
    ("bon-sent-II-d3-p1-a2-q2", "quaestio", 1, 2, 2, 7973, 8197,
     "Utrum personalis proprietas in Angelis sit substantialis, vel accidentalis.",
     "QUAESTIO II (7973). Ends before QUAESTIO III (8198)."),
    ("bon-sent-II-d3-p1-a2-q3", "quaestio", 1, 2, 3, 8198, 8358,
     "Utrum discretio personalis sit a parte principii formalis, vel materialis.",
     "QUAESTIO III (8198). Ends before DUBIA CIRCA LITTERAM (8359)."),
    ("bon-sent-II-d3-p1-dubia", "dubia", 1, None, None, 8359, 8476,
     "Dubia circa litteram Magistri (Pars I).",
     "DUBIA CIRCA LITTERAM (8359): DUB I (8360), DUB II (8416), DUB IV (8442 — DUB III folio-bled). Ends before COMMENTARIUS Pars II (8477)."),
    ("bon-sent-II-d3-p2-divisio", "divisio", 2, None, None, 8477, 8510,
     "Commentarius in Distinctionem III, Pars II — Divisio textus.",
     "COMMENTARIUS IN DIST. III Pars II (8477) + DIVISIO TEXTUS (8486) + TRACTATIO QUAESTIONUM (8498). ARTICULUS I opener (8507) folds into a1-q1."),
    ("bon-sent-II-d3-p2-a1-q1", "quaestio", 2, 1, 1, 8511, 8674,
     "Utrum Deus malum condiderit Angelum.",
     "ARTICULUS I opener folded in + QUAESTIO I (8511). Ends before QUAESTIO II (8675)."),
    ("bon-sent-II-d3-p2-a1-q2", "quaestio", 2, 1, 2, 8675, 8857,
     "Utrum Angelus in primo instanti suae creationis fuerit malus propria voluntate.",
     "QUAESTIO II (8675). Ends before ARTICULUS II (8858)."),
    ("bon-sent-II-d3-p2-a2-q1", "quaestio", 2, 2, 1, 8858, 9162,
     "Utrum Angelus omnia creata, quae cognoscit, cognoscat per species innatas.",
     "ARTICULUS II opener (8858) folded in + QUAESTIO I (8864). Ends before QUAESTIO II (9163)."),
    ("bon-sent-II-d3-p2-a2-q2", "quaestio", 2, 2, 2, 9163, 9322,
     "Utrum Angelus per cognitionem naturalem divinam essentiam cognoverit in se ipsa sine medio.",
     "QUAESTIO II (9163). Ends before ARTICULUS III (9323)."),
    ("bon-sent-II-d3-p2-a3-q1", "quaestio", 2, 3, 1, 9323, 9504,
     "Utrum Angeli naturali dilectione dilexerint Deum propter ipsum et super omnia.",
     "ARTICULUS III opener (9323) folded in + QUAESTIO I (9331). Ends before QUAESTIO II (9505)."),
    ("bon-sent-II-d3-p2-a3-q2", "quaestio", 2, 3, 2, 9505, 9601,
     "Utrum Angelus naturali dilectione magis diligat superiorem, an parem, an inferiorem.",
     "QUAESTIO II (9505). Ends before DUBIA CIRCA LITTERAM MAGISTRI Pars II (9602)."),
    ("bon-sent-II-d3-p2-dubia", "dubia", 2, None, None, 9602, 9660,
     "Dubia circa litteram Magistri (Pars II).",
     "DUBIA CIRCA LITTERAM MAGISTRI (9602): DUB I (9604), DUB II (9641), DUB III (9643). Ends before DISTINCTIO IV (9661)."),
]

NEW_IDS = {c[0] for c in CHUNKS}


def frontmatter(cid, ctype, pars, art, q, s, e, title_la, note, wc):
    fm = [
        "---",
        f'id: "{cid}"',
        "volume: 2",
        "book: 2",
        "distinctio: 3",
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
        f'transcription_status: "auto-chunked 2026-05-13; rechunked 2026-05-16 session 31 (correct semantic boundaries, raw {s}-{e}) — {note}"',
        "format_version: 1",
        "---",
    ]
    return "\n".join(fm)


# Report orphans (old d3 files not in the new id set) — deleted below.
existing = sorted(OUT.glob("bon-sent-II-d3-*.md"))
print("Existing d3 files:")
for p in existing:
    tag = "OVERWRITE" if p.stem in NEW_IDS else "DELETE (orphan)"
    print(f"  {p.name}: {tag}")
print()

# Delete every old d3 file (clean slate; backup already taken).
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
