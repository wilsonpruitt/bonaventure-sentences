#!/usr/bin/env python3.11
"""Regenerate d9 chunks from raw text using semantic boundaries.

Boundaries identified by grep on raw markers (DISTINCTIO, COMMENTARIUS,
ARTICULUS, QUAESTIO, DUBIA). OCR variants noted: QIIAESTIO (line 36760)
should have been QUAESTIO III. Running-head 'DIST. IX. DIVISIO TEXTUS' at
35976 is mid-littera, NOT a chapter boundary.

Writes Latin body as raw OCR; English / apparatus are Tier-1 placeholders.
After running, hand-translate or feed to a translation agent.
"""
from pathlib import Path

RAW = Path("/Users/wilsonpruitt/bonaventure-sentences/raw/bonaventure_vol1_raw.txt")
OUT = Path("/Users/wilsonpruitt/bonaventure-sentences/vol1")

lines = RAW.read_text().splitlines()


def extract(start, end):
    return "\n".join(lines[start - 1:end]).strip()


chunks = {
    "bon-sent-I-d9-littera": {
        "range": (35561, 36016),
        "type": "littera",
        "meta": {},
        "title": "I Sent., d. 9 — Littera Magistri",
        "note": "2026-04-14: Lombard d.9 Caps I–V. Includes running-head 'DIST. IX. DIVISIO TEXTUS' at 35976 which is mid-Cap-V text, not a Bonaventure boundary.",
    },
    "bon-sent-I-d9-divisio": {
        "range": (36017, 36134),
        "type": "divisio",
        "meta": {},
        "title": "I Sent., d. 9 — Divisio textus",
        "note": "2026-04-14: COMMENTARIUS heading + DIVISIO TEXTUS + TRACTATIO QUAESTIONUM listing.",
    },
    "bon-sent-I-d9-a1-q1": {
        "range": (36135, 36546),
        "type": "quaestio",
        "meta": dict(articulus=1, quaestio=1),
        "title": "I Sent., d. 9, a. unicus, q. 1",
        "note": "2026-04-14: ARTICULUS UNICUS intro + QUAESTIO I. (a1 = articulus unicus per project naming.)",
    },
    "bon-sent-I-d9-a1-q2": {
        "range": (36547, 36759),
        "type": "quaestio",
        "meta": dict(articulus=1, quaestio=2),
        "title": "I Sent., d. 9, a. unicus, q. 2",
        "note": "2026-04-14: Regenerated from raw 36547–36759.",
    },
    "bon-sent-I-d9-a1-q3": {
        "range": (36760, 36858),
        "type": "quaestio",
        "meta": dict(articulus=1, quaestio=3),
        "title": "I Sent., d. 9, a. unicus, q. 3",
        "note": "2026-04-14: OCR header reads 'QIIAESTIO III' (line 36760). Quaestio: Utrum in divinis generatio sit aeterna. Was missing from prior auto-chunking.",
    },
    "bon-sent-I-d9-a1-q4": {
        "range": (36859, 37164),
        "type": "quaestio",
        "meta": dict(articulus=1, quaestio=4),
        "title": "I Sent., d. 9, a. unicus, q. 4",
        "note": "2026-04-14: Regenerated from raw 36859–37164.",
    },
    "bon-sent-I-d9-dubia": {
        "range": (37165, 37970),
        "type": "dubia",
        "meta": {},
        "title": "I Sent., d. 9 — Dubia circa litteram Magistri",
        "note": "2026-04-14: Dub I–XIII. Ends before DISTINCTIO X at 37971.",
    },
}


def build_md(chunk_id, info):
    start, end = info["range"]
    latin_body = extract(start, end)
    word_count = len(latin_body.split())
    meta = info["meta"]
    meta_lines = []
    for k in ("articulus", "quaestio"):
        if k in meta:
            meta_lines.append(f'{k}: {meta[k]}')
    meta_block = "\n".join(meta_lines)
    meta_section = (meta_block + "\n") if meta_block else ""

    return f"""---
id: "{chunk_id}"
volume: 1
book: 1
distinctio: 9
{meta_section}type: {info['type']}
title: "{info['title']}"
line_start: {start}
line_end: {end}
word_count_latin: {word_count}
boundary_note: "{info['note']}"
---

# {info['title']}

## Latin

{latin_body}

## English

[Translation pending]

## Notes

[Notes pending]
"""


# Stale d9 files from prior auto-chunking — list before deleting
stale_glob = sorted(OUT.glob("bon-sent-I-d9-*.md"))
if stale_glob:
    print("Existing d9 files (will be overwritten or kept if not in new set):")
    new_ids = set(chunks.keys())
    for p in stale_glob:
        marker = "OVERWRITE" if p.stem in new_ids else "ORPHAN — review/delete manually"
        print(f"  {p.name}: {marker}")
    print()

for chunk_id, info in chunks.items():
    path = OUT / f"{chunk_id}.md"
    path.write_text(build_md(chunk_id, info))
    s, e = info["range"]
    print(f"Wrote: {path.name} ({s}-{e}, {e-s+1} lines)")

print("\nDone. Audit Latin bodies before translating; OCR may have garbled headers internally.")
