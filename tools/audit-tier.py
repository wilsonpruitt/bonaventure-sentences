#!/usr/bin/env python3.11
"""Tiered audit helper for completed Tier-2 chunks.

Scores each chunk on doctrinal/structural risk signals and assigns a tier:
  - Tier 1 (SKIM):   ~30 sec — read English summary, spot-check 1–2 paragraphs
  - Tier 2 (NORMAL): ~3 min  — read English in full, eyeball Latin parallel
  - Tier 3 (DEEP):   ~10 min — full bilingual read, verify citations, check apparatus

Signals (each capped at 3pt to prevent any one factor dominating):
  - Size:               1pt per 1k Latin words (cap 3)
  - Footnote density:   1pt per 5 [^N] markers (cap 3)
  - Has scholion:       2pt
  - Conclusio present:  1pt
  - Apparatus variants: 2pt if codd./lectio/Vat./contra appear
  - Doctrinal density:  1pt per 1.5% hot-term density (cap 2) —
                        normalized so a chunk *about* esse doesn't auto-tier-3
  - Type:               +1 quaestio, +2 dubia, 0 littera/divisio
                        (dubia are dense, terse, citation-heavy)

Tier thresholds: <4 = SKIM, 4–7 = NORMAL, >7 = DEEP.

Usage:
  python3.11 tools/audit-tier.py vol1/bon-sent-I-d8-*.md       # rank
  python3.11 tools/audit-tier.py --queue vol1/                  # write audit-queue.md
  python3.11 tools/audit-tier.py --explain vol1/bon-sent-I-d8-p2-a1-q1.md
"""
import re
import sys
from pathlib import Path
from dataclasses import dataclass

REPO = Path(__file__).resolve().parent.parent

DOCTRINAL_TERMS = re.compile(
    r"\b(trinitas|trinitatis|personae?|personarum|processi[oa]|relati[oa]"
    r"|essenti[ae]|substanti[ae]|suppositum|natur[ae]|hypostas[ie]s"
    r"|gratia|gratiam|liberum\s+arbitrium|caritas|merit"
    r"|transsubstantiati|sacrament|eucharist"
    r"|incarnati[oa]|hypostatic"
    r"|exemplar|illuminati[oa]|vestigi|imag[oin]"
    r"|esse(?:ntia)?|aequivalent|participation)\b",
    re.IGNORECASE,
)

VARIANT_TERMS = re.compile(
    r"\b(codd?\.|cod\.|Vat\.|lectio|propter|contra\s+(?:cod|mss)|mss\.)\b"
)

CONCLUSIO = re.compile(r"^>\s*\*\*Conclusio\*\*|^### Conclusio|Respondeo", re.MULTILINE)

SCHOLION = re.compile(r"^### Scholion\b", re.MULTILINE)


@dataclass
class Score:
    chunk_id: str
    tier: int
    total: float
    signals: dict
    minutes: float


def score_chunk(path: Path) -> Score | None:
    text = path.read_text()
    if "[Translation pending]" in text or "## English" not in text:
        return None

    fm_match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    fm = fm_match.group(1) if fm_match else ""
    chunk_type_match = re.search(r"^type:\s*(\w+)", fm, re.MULTILINE)
    chunk_type = chunk_type_match.group(1) if chunk_type_match else "unknown"

    latin_match = re.search(r"## Latin\n+(.*?)(?=\n## (?:English|Apparatus|Notes)|\Z)", text, re.DOTALL)
    english_match = re.search(r"## English\n+(.*?)(?=\n## (?:Latin|Apparatus|Notes)|\Z)", text, re.DOTALL)
    apparatus_match = re.search(r"## Apparatus\n+(.*?)(?=\n## (?:Latin|English|Notes)|\Z)", text, re.DOTALL)

    latin = latin_match.group(1) if latin_match else ""
    english = english_match.group(1) if english_match else ""
    apparatus = apparatus_match.group(1) if apparatus_match else ""

    la_words = len(latin.split())
    footnotes = len(set(re.findall(r"\[\^(\d+)\]", latin)))
    has_scholion = 1 if SCHOLION.search(text) else 0
    has_conclusio = 1 if CONCLUSIO.search(text) else 0
    has_variants = 1 if VARIANT_TERMS.search(apparatus) else 0
    doctrinal_hits = len(DOCTRINAL_TERMS.findall(latin))

    type_pts = {"dubia": 2, "quaestio": 1}.get(chunk_type, 0)
    doctrinal_density = (doctrinal_hits / la_words * 100) if la_words else 0

    signals = {
        "size_pts":       min(3.0, round(la_words / 1000, 1)),
        "footnote_pts":   min(3.0, round(footnotes / 5, 1)),
        "scholion_pts":   has_scholion * 2,
        "conclusio_pts":  has_conclusio,
        "variant_pts":    has_variants * 2,
        "doctrinal_pts":  min(2.0, round(doctrinal_density / 1.5, 1)),
        "type_pts":       type_pts,
        "_meta": {
            "type": chunk_type,
            "la_words": la_words,
            "en_words": len(english.split()),
            "footnotes": footnotes,
            "doctrinal_hits": doctrinal_hits,
        },
    }

    total = sum(v for k, v in signals.items() if k != "_meta")
    if total < 4:
        tier, minutes = 1, 0.5
    elif total <= 7:
        tier, minutes = 2, 3.0
    else:
        tier, minutes = 3, 10.0

    return Score(path.stem, tier, total, signals, minutes)


def rank(paths: list[Path]) -> list[Score]:
    scored = []
    for p in paths:
        s = score_chunk(p)
        if s:
            scored.append(s)
    scored.sort(key=lambda s: (-s.tier, -s.total))
    return scored


def fmt_table(scores: list[Score]) -> str:
    lines = ["| Tier | Chunk | Score | La words | Notes | Est. audit |",
             "|:----:|---|---:|---:|---|---:|"]
    label = {1: "SKIM", 2: "NORM", 3: "DEEP"}
    for s in scores:
        m = s.signals["_meta"]
        notes = []
        if s.signals["scholion_pts"]: notes.append("scholion")
        if s.signals["variant_pts"]: notes.append("variants")
        if s.signals["doctrinal_pts"] >= 1: notes.append(f"{m['doctrinal_hits']} doctr.")
        if m["type"] in ("dubia", "littera"): notes.append(m["type"])
        notes_str = ", ".join(notes) or "—"
        lines.append(
            f"| {label[s.tier]} | `{s.chunk_id}` | {s.total:.1f} | {m['la_words']} | {notes_str} | {s.minutes:.0f}m |"
        )
    return "\n".join(lines)


def explain(path: Path):
    s = score_chunk(path)
    if not s:
        print(f"{path.name}: skipped (no English yet)")
        return
    label = {1: "SKIM", 2: "NORMAL", 3: "DEEP"}[s.tier]
    print(f"{path.name}")
    print(f"  Tier: {label} (score {s.total:.1f}, ~{s.minutes:.0f} min)")
    for k, v in s.signals.items():
        if k == "_meta":
            print(f"  meta: {v}")
        elif v:
            print(f"  +{v} {k}")


def write_queue(scored: list[Score], out: Path):
    by_tier = {1: [], 2: [], 3: []}
    for s in scored:
        by_tier[s.tier].append(s)

    label = {1: "SKIM (~30 sec)", 2: "NORMAL (~3 min)", 3: "DEEP (~10 min)"}
    total_min = sum(s.minutes for s in scored)

    out_text = [
        "# Audit Queue",
        f"\n_{len(scored)} chunks · est. {total_min:.0f} min ({total_min/60:.1f} hrs) total audit time_\n",
        "Attack DEEP first while fresh; SKIM at end.\n",
    ]
    for tier in (3, 2, 1):
        out_text.append(f"\n## Tier {tier} — {label[tier]} ({len(by_tier[tier])} chunks)\n")
        out_text.append(fmt_table(by_tier[tier]) if by_tier[tier] else "_(none)_")
    out.write_text("\n".join(out_text))
    print(f"\nWrote {out.relative_to(REPO)}")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)

    if args[0] == "--explain":
        for a in args[1:]:
            explain(Path(a))
        return

    write_queue_flag = False
    if args[0] == "--queue":
        write_queue_flag = True
        args = args[1:]

    paths = []
    for a in args:
        p = Path(a)
        if p.is_dir():
            paths.extend(sorted(p.glob("bon-sent-*.md")))
        else:
            paths.append(p)

    scored = rank(paths)
    if not scored:
        print("No translated chunks found.")
        return

    print(fmt_table(scored))
    total_min = sum(s.minutes for s in scored)
    print(f"\n{len(scored)} chunks · est. {total_min:.0f} min audit ({total_min/60:.1f} hrs)")

    if write_queue_flag:
        write_queue(scored, REPO / "AUDIT-QUEUE.md")


if __name__ == "__main__":
    main()
