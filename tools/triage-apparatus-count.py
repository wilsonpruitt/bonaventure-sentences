#!/usr/bin/env python3.11
"""Apparatus-count triage — bucket Tier C chunks (audit-apparatus-count diff
+5 to +19) into three workload classes by subtracting known noise contributors
from the raw heuristic and comparing the residual to the chunk's apparatus
count.

Lessons 9/10 (see `manual-review/d1-d4-tier2-promotion-log.md`) identified
predictable false-positive sources in `audit-apparatus-count.py`:

  - Chapter rubrics on littera chunks: `Cap. I.`, `Cap. II.`, ... — each
    rubric matches the footer-opener regex.
  - Numbered argument openers in commentary chunks: `1. Auctoritate`,
    `2. Item` — these get past the negative-lookahead because of OCR garbles.
  - Scholion section openers: `I.`, `II.`, `III.`
  - Italicized work-citations inside Scholion: `*Sent.* d. 36. q. 3.`,
    `*S.* I. q. 14. a. 4.` — match because the regex is permissive on
    leading-glyph patterns.
  - Lettered series inside Scholion: `a)`, `b)`, `c)`.

This script counts those signals in the raw slice, subtracts them from the
audit's diff, and buckets the chunks. Buckets:

  A — adjusted_diff <= 2: metadata-only candidate, batch-update status
                           string, no full agent dispatch.
  B — adjusted_diff 3..8: small-undercoverage candidate, short-prompt agent.
  C — adjusted_diff > 8 : likely real undercoverage, full disposition agent.

The output is a markdown triage table written to
`manual-review/wave9b-tier-c-triage.md`. The script is advisory — every
disposition still requires eyes-on per Lesson 10 ("the audit is ALWAYS a
triage signal, never ground truth — both directions").
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VOL1 = REPO / "vol1"
RAW_PT1 = REPO / "raw" / "bonaventure_vol1_raw.txt"
RAW_PT2 = REPO / "raw" / "bonaventure_vol1_pt2_raw.txt"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
APPARATUS_DEF_RE = re.compile(r"^\[\^[^\]]+\]:", re.MULTILINE)
APPARATUS_BLOCK_RE = re.compile(r"^## Apparatus\s*\n(.*)\Z", re.DOTALL | re.MULTILINE)
SCHOLION_BLOCK_RE = re.compile(r"^### Scholion\b.*?(?=^---|\Z)", re.DOTALL | re.MULTILINE)

# Same heuristic as audit-apparatus-count.py (verbatim copy so the diff
# numbers reconcile exactly).
FOOTER_NOTE_RE = re.compile(
    r"^\s*(?:\d{1,2}(?![.0-9])|[\W_]{1,3}|[ivx]{1,3}\.?)\s+[A-Z][a-zà-ÿ]",
    re.MULTILINE,
)

# Noise contributors — counted in raw slice and subtracted from diff.
CHAPTER_RUBRIC_RE = re.compile(r"\bCap(?:itulum)?\.?\s+[IVXLM]{1,4}\b", re.IGNORECASE)
SCHOLION_HEADER_RE = re.compile(r"\bSCHOLION\b", re.IGNORECASE)
# Italicized work-citations inside Scholion: `*Sent.*`, `*S.*`, `*de Trin.*`,
# etc. Match the surrounding `*...*` italic and the d./q./a./n. pattern.
WORK_CITE_RE = re.compile(r"\*[^*]{1,40}\*\s*(?:[ldqan]\.\s*\d|\d{1,3})", re.IGNORECASE)
# Lettered series openers in Scholion: `a)`, `b)`, `c)`, `d)`.
LETTER_SERIES_RE = re.compile(r"^\s*[a-h]\)\s+[A-Z]", re.MULTILINE)


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    out: dict = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def count_apparatus_defs(text: str) -> int:
    m = APPARATUS_BLOCK_RE.search(text)
    block = m.group(1) if m else text
    return len(APPARATUS_DEF_RE.findall(block))


def raw_slice(distinctio: int, ls: int, le: int) -> str:
    if distinctio >= 24:
        raw = RAW_PT2.read_text(encoding="utf-8", errors="replace")
    else:
        raw = RAW_PT1.read_text(encoding="utf-8", errors="replace")
    lines = raw.splitlines()
    if ls < 1 or le > len(lines) + 5:
        return ""
    return "\n".join(lines[ls - 1 : min(le, len(lines))])


def chunk_type(fm: dict, text: str) -> str:
    t = fm.get("type", "").lower()
    if t:
        return t
    if "## Scholion" in text or "### Scholion" in text:
        return "quaestio-scholion"
    return "unknown"


def has_scholion(text: str) -> bool:
    return bool(SCHOLION_BLOCK_RE.search(text))


def estimate_noise(slc: str, chunk_text: str) -> dict:
    rubrics = len(CHAPTER_RUBRIC_RE.findall(slc))
    scholion_hdr = len(SCHOLION_HEADER_RE.findall(slc))
    work_cites = len(WORK_CITE_RE.findall(slc))
    letter_series = len(LETTER_SERIES_RE.findall(slc))
    # Scholion-heavy chunks: italicized citations cluster heavily. Cap at a
    # ceiling to avoid wild over-subtraction.
    work_cites = min(work_cites, 12)
    return {
        "chapter_rubrics": rubrics,
        "scholion_headers": scholion_hdr,
        "work_citations": work_cites,
        "letter_series": letter_series,
        "total": rubrics + scholion_hdr + work_cites + letter_series,
    }


def bucket(adjusted_diff: int) -> str:
    if adjusted_diff <= 2:
        return "A"  # metadata-only candidate
    if adjusted_diff <= 8:
        return "B"  # small undercoverage
    return "C"  # large undercoverage


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-d", type=int, default=1)
    ap.add_argument("--max-d", type=int, default=40)
    ap.add_argument("--min-diff", type=int, default=5,
                    help="lower bound on raw audit diff (default 5)")
    ap.add_argument("--max-diff", type=int, default=19,
                    help="upper bound on raw audit diff (default 19)")
    ap.add_argument("--out", default="manual-review/wave9b-tier-c-triage.md")
    args = ap.parse_args()

    rows = []
    for p in sorted(VOL1.glob("bon-sent-I-d*.md")):
        m = re.match(r"bon-sent-I-d(\d+)-", p.name)
        if not m:
            continue
        d = int(m.group(1))
        if not (args.min_d <= d <= args.max_d):
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        try:
            ls = int(fm.get("line_start", ""))
            le = int(fm.get("line_end", ""))
        except (ValueError, TypeError):
            continue
        slc = raw_slice(d, ls, le)
        if not slc:
            continue
        chunk_count = count_apparatus_defs(text)
        if chunk_count == 0:
            # SKELETON-SUSPECT — out of Tier C scope; handled separately.
            continue
        raw_count = len(FOOTER_NOTE_RE.findall(slc))
        diff = raw_count - chunk_count
        if not (args.min_diff <= diff <= args.max_diff):
            continue
        status = fm.get("transcription_status", "")
        if not status.lower().startswith("phase c tier 2 complete"):
            # Out of scope — not a Tier-2-complete chunk.
            continue
        noise = estimate_noise(slc, text)
        adjusted = max(0, diff - noise["total"])
        ctype = chunk_type(fm, text)
        printed_pages = fm.get("printed_pages", "")
        rows.append({
            "chunk": p.stem,
            "d": d,
            "type": ctype,
            "pages": printed_pages,
            "raw": raw_count,
            "chunk_app": chunk_count,
            "diff": diff,
            "rubrics": noise["chapter_rubrics"],
            "scholion": noise["scholion_headers"],
            "cites": noise["work_citations"],
            "letter": noise["letter_series"],
            "noise": noise["total"],
            "adjusted": adjusted,
            "bucket": bucket(adjusted),
        })

    rows.sort(key=lambda r: (r["bucket"], -r["adjusted"], -r["diff"]))

    counts = {"A": 0, "B": 0, "C": 0}
    for r in rows:
        counts[r["bucket"]] += 1

    lines = ["# Wave 9b Tier C — Apparatus-Count Triage", ""]
    lines.append(f"Triage of {len(rows)} chunks at audit diff +{args.min_diff} to +{args.max_diff} "
                 f"(d.{args.min_d}–d.{args.max_d}, Tier-2-complete chunks only).")
    lines.append("")
    lines.append("Adjusted diff = raw audit diff − (chapter rubrics + Scholion headers + "
                 "italicized work-citations + lettered series). Noise sources are the "
                 "Lesson-10 false-positive contributors documented in "
                 "`d1-d4-tier2-promotion-log.md`.")
    lines.append("")
    lines.append("**Buckets:**")
    lines.append(f"- **A — metadata-only candidate** (adjusted ≤ 2): {counts['A']} chunks. "
                 "Batch-update status string after eyes-on confirmation. No full agent dispatch.")
    lines.append(f"- **B — small undercoverage** (adjusted 3–8): {counts['B']} chunks. "
                 "Short-prompt agent per chunk.")
    lines.append(f"- **C — large undercoverage** (adjusted > 8): {counts['C']} chunks. "
                 "Full disposition agent like Tier B.")
    lines.append("")
    lines.append("Reminder: the audit is a triage signal, never ground truth (Lesson 10). "
                 "Bucket A in particular still warrants eyes-on the printed footer band before "
                 "promoting the status string. The adjusted-diff calculation is itself a "
                 "heuristic — it may over- or under-subtract.")
    lines.append("")
    lines.append("| Chunk | d | Type | Pages | Raw | Chunk | Diff | Rubrics | Schol | Cites | Lett | Noise | Adj | Bucket |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        lines.append(
            f"| `{r['chunk']}` | {r['d']} | {r['type']} | {r['pages']} | "
            f"{r['raw']} | {r['chunk_app']} | +{r['diff']} | "
            f"{r['rubrics']} | {r['scholion']} | {r['cites']} | {r['letter']} | "
            f"{r['noise']} | {r['adjusted']} | **{r['bucket']}** |"
        )
    lines.append("")

    # Per-bucket sub-sections for at-a-glance scanning.
    for b in ("A", "B", "C"):
        lines.append(f"## Bucket {b}")
        lines.append("")
        bucket_rows = [r for r in rows if r["bucket"] == b]
        if not bucket_rows:
            lines.append("(none)")
            lines.append("")
            continue
        for r in bucket_rows:
            lines.append(f"- `{r['chunk']}` — {r['type']}, pp. {r['pages']}, "
                         f"raw={r['raw']} chunk={r['chunk_app']} diff=+{r['diff']} "
                         f"adj={r['adjusted']}")
        lines.append("")

    report = "\n".join(lines)

    out_path = REPO / args.out
    out_path.write_text(report, encoding="utf-8")
    print(f"wrote {out_path}")
    print(f"  Bucket A (metadata-only): {counts['A']}")
    print(f"  Bucket B (small under):   {counts['B']}")
    print(f"  Bucket C (large under):   {counts['C']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
