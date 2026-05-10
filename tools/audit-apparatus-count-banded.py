#!/usr/bin/env python3.11
"""Apparatus-count audit, page-banded version (Wave 9b Tier C, 2026-05-10).

Improvement over `audit-apparatus-count.py`: instead of counting footer-opener
patterns across the whole chunk slice (which sweeps in body objections, in-entry
numerals, and neighbor-chunk footers on shared pages), this version:

  1. Splits the chunk's raw slice into per-printed-page sections using
     page-number markers (bare 1-3 digit lines) and Quaracchi running heads
     (`SENTENTIARUM LIB.`, `DIST. N.`, `DISTINCTIO N`, `NOTAE AD ...`).
  2. Within each page section, detects the footer band as the densest cluster
     of footer-opener lines (≥2 openers within a 12-line window) at or near
     the section tail.
  3. Counts only footer-opener lines within that band, then sums per page.

This eliminates the dominant Bucket-B/C noise sources surfaced by the
2026-05-10 sample-validate:
  - body-objection numerals (`1. Pater totum`, `2. Item`) outside the band
  - in-entry citation patterns (`c. 14. n. 17`, `edd. 4, 5, 6`) inside long
    multi-clause entries — only the entry-opening line matches now
  - shared-page neighbor footers, when the chunk's line range only touches
    the body of an adjacent page (the band of that page falls outside the
    chunk's owned section)

Limitations:
  - Quaracchi sometimes splits a page's footer between two columns (left and
    right column footer); the OCR linearizes both, but a long body in
    column 2 can split the footer cluster. The tool treats them as one
    band when the gap is <= 12 lines, but very long page bodies may split
    spuriously.
  - Pages that are FULLY shared (e.g. d29-divisio occupying just the
    bottom of p.507 and top of p.508) still over-count, because the
    chunk's line range includes the full footer of those pages. That
    requires chunk-portion attribution, not done here.

Usage:
  python3.11 tools/audit-apparatus-count-banded.py                      # all
  python3.11 tools/audit-apparatus-count-banded.py --min-d 1 --max-d 40
  python3.11 tools/audit-apparatus-count-banded.py --chunk d35-divisio  # single
  python3.11 tools/audit-apparatus-count-banded.py --verbose --chunk d8-littera
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

# Same hardened opener regex as the original tool (Wave 5, 2026-05-09).
FOOTER_NOTE_RE = re.compile(
    r"^\s*(?:\d{1,2}(?![.0-9])|[\W_]{1,3}|[ivx]{1,3}\.?)\s+[A-Z][a-zà-ÿ]"
)

# Bare page-number line (1-3 digits, surrounded only by whitespace).
PAGE_NUM_RE = re.compile(r"^\s*\d{1,3}\s*$")

# Quaracchi running heads / section headers that mark a printed-page top.
RUNNING_HEAD_RE = re.compile(
    r"^\s*(?:SENTENTIARUM\s+LIB|LIBR\.\s+I+\.\s+SENT|DIST\.\s+[IVXL]+|"
    r"DUB[IO]A?\s+CIRCA|DISTINCTIO\s+[IVXL]+|NOTAE\s+AD\b|"
    r"COMMENTARIUS\s+IN\s+DISTINCTIONEM|TRACTATIO\s+QUAESTIONUM|"
    r"DIVISIO\s+TEXTUS|ARTICULUS\s+(?:UNICUS|[IVXL]+)|QU.{0,3}STIO\s+[IVXL]+)",
    re.IGNORECASE,
)

# Cluster gap: footer-opener lines within this many lines of each other are
# treated as one band. Tuned so that 2-column footers join, but body
# objections separated by paragraph prose stay split.
BAND_GAP = 12


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


def raw_slice(distinctio: int, ls: int, le: int) -> list[str]:
    if distinctio >= 24:
        raw = RAW_PT2.read_text(encoding="utf-8", errors="replace")
    else:
        raw = RAW_PT1.read_text(encoding="utf-8", errors="replace")
    lines = raw.splitlines()
    if ls < 1 or le > len(lines) + 5:
        return []
    return lines[ls - 1 : min(le, len(lines))]


def find_page_starts(lines: list[str]) -> list[int]:
    """Return ascending line indices where a new printed page begins.

    A page break is signalled by a bare page-number line OR a recognised
    Quaracchi running-head / section opener. Adjacent markers within 5
    lines collapse to one (a running head + page number on consecutive
    lines is one boundary).
    """
    starts = [0]
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        is_marker = PAGE_NUM_RE.match(s) or RUNNING_HEAD_RE.match(s)
        if is_marker and i > starts[-1] + 5:
            starts.append(i)
    return starts


def detect_band(section: list[str]) -> tuple[int, int]:
    """Within a page section, return (band_start, band_end) line indices
    relative to the section. Returns (len, len) if no band is found.

    Band = densest cluster of footer-opener matches with gaps <= BAND_GAP.
    Prefer clusters in the BOTTOM HALF of the section (typical Quaracchi
    layout) and with at least 2 entries (a one-entry "cluster" is more
    likely a body false-positive).
    """
    n = len(section)
    matches = [i for i, ln in enumerate(section) if FOOTER_NOTE_RE.match(ln)]
    if not matches:
        return n, n

    clusters = [[matches[0]]]
    for idx in matches[1:]:
        if idx - clusters[-1][-1] <= BAND_GAP:
            clusters[-1].append(idx)
        else:
            clusters.append([idx])

    eligible = [c for c in clusters if len(c) >= 2]
    if not eligible:
        # Only solo openers — probably body. Return last solo if it's in the
        # bottom 30% (could be a 1-entry footer band).
        last_solo = clusters[-1][0]
        if last_solo > 0.7 * n:
            return last_solo, n
        return n, n

    # Pick the cluster nearest the bottom of the section that has size >= 2.
    eligible.sort(key=lambda c: c[-1])
    chosen = eligible[-1]
    return chosen[0], n


def count_footers_in_band(section: list[str], band_start: int, band_end: int) -> int:
    """Count footer-opener lines within the detected band."""
    return sum(1 for ln in section[band_start:band_end] if FOOTER_NOTE_RE.match(ln))


def banded_count(slice_lines: list[str], verbose: bool = False) -> tuple[int, list[dict]]:
    """Return (total_count, per_page_details)."""
    starts = find_page_starts(slice_lines)
    starts.append(len(slice_lines))
    per_page = []
    total = 0
    for i in range(len(starts) - 1):
        a, b = starts[i], starts[i + 1]
        if b - a < 8:
            continue
        section = slice_lines[a:b]
        band_a, band_b = detect_band(section)
        n = count_footers_in_band(section, band_a, band_b)
        if verbose:
            head = next((s.strip() for s in section[:5] if s.strip()), "")
            per_page.append({
                "section_start": a,
                "section_end": b,
                "section_len": b - a,
                "band_start_in_section": band_a,
                "band_count": n,
                "section_head_preview": head[:80],
            })
        total += n
    return total, per_page


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-d", type=int, default=1)
    ap.add_argument("--max-d", type=int, default=48)
    ap.add_argument("--chunk", default=None,
                    help="Single chunk filter, e.g. d35-divisio or d8-littera")
    ap.add_argument("--min-diff", type=int, default=3,
                    help="flag chunks where (banded_count - apparatus_defs) >= this")
    ap.add_argument("--verbose", action="store_true",
                    help="print per-page detection details")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    rows = []
    for p in sorted(VOL1.glob("bon-sent-I-d*.md")):
        m = re.match(r"bon-sent-I-d(\d+)-(.+)\.md", p.name)
        if not m:
            continue
        d = int(m.group(1))
        if not (args.min_d <= d <= args.max_d):
            continue
        if args.chunk and args.chunk not in p.name:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        try:
            ls = int(fm.get("line_start", ""))
            le = int(fm.get("line_end", ""))
        except (ValueError, TypeError):
            continue
        slice_lines = raw_slice(d, ls, le)
        if not slice_lines:
            continue

        chunk_count = count_apparatus_defs(text)
        # Original heuristic count for comparison
        orig_count = sum(1 for ln in slice_lines if FOOTER_NOTE_RE.match(ln))
        banded, details = banded_count(slice_lines, verbose=args.verbose)

        diff_orig = orig_count - chunk_count
        diff_banded = banded - chunk_count
        improvement = diff_orig - diff_banded

        rows.append({
            "chunk": p.stem,
            "d": d,
            "pages": fm.get("printed_pages", ""),
            "chunk_app": chunk_count,
            "orig_raw": orig_count,
            "banded_raw": banded,
            "diff_orig": diff_orig,
            "diff_banded": diff_banded,
            "improvement": improvement,
            "details": details,
            "status_tier2": fm.get("transcription_status", "").lower().startswith(
                "phase c tier 2 complete"),
        })

    rows.sort(key=lambda r: -r["diff_banded"])

    lines = ["# Apparatus-Count Audit — page-banded (Wave 9b Tier C)", ""]
    lines.append(
        "Re-counts footer-opener lines using per-page band detection. "
        f"Range d.{args.min_d}–d.{args.max_d}. "
        "Columns: `chunk_app` = chunk `[^N]:` defs; `orig` = original "
        "audit raw count (whole-slice); `banded` = new banded count; "
        "`diff_b` = banded − chunk_app; `improvement` = diff_orig − diff_banded "
        "(positive = banded reduced overcount)."
    )
    lines.append("")
    lines.append(
        f"**Audited: {len(rows)} chunks. "
        f"Mean diff orig→banded: "
        f"{sum(r['diff_orig'] for r in rows) / max(len(rows),1):.1f} → "
        f"{sum(r['diff_banded'] for r in rows) / max(len(rows),1):.1f}. "
        f"Mean improvement: "
        f"{sum(r['improvement'] for r in rows) / max(len(rows),1):.1f} entries.**"
    )
    lines.append("")
    lines.append("| Chunk | d | Pages | Chunk app | Orig raw | Banded | Diff orig | Diff banded | Improvement |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    show = rows
    for r in show:
        lines.append(
            f"| `{r['chunk']}` | {r['d']} | {r['pages']} | "
            f"{r['chunk_app']} | {r['orig_raw']} | {r['banded_raw']} | "
            f"{r['diff_orig']:+d} | {r['diff_banded']:+d} | "
            f"{r['improvement']:+d} |"
        )

    if args.verbose:
        lines.append("")
        lines.append("## Per-page detail")
        lines.append("")
        for r in show:
            if not r["details"]:
                continue
            lines.append(f"### {r['chunk']} (pages {r['pages']})")
            lines.append("")
            lines.append("| Section [start:end] | Len | Band start | Band count | Section head |")
            lines.append("|---|---|---|---|---|")
            for d in r["details"]:
                lines.append(
                    f"| [{d['section_start']}:{d['section_end']}] | "
                    f"{d['section_len']} | {d['band_start_in_section']} | "
                    f"{d['band_count']} | `{d['section_head_preview']}` |"
                )
            lines.append("")

    report = "\n".join(lines)
    if args.out:
        out_path = REPO / args.out
        out_path.write_text(report, encoding="utf-8")
        print(f"wrote {out_path}")
    else:
        print(report)


if __name__ == "__main__":
    main()
