#!/usr/bin/env python3.11
"""Header-inventory audit — per distinction, count semantic markers in raw OCR
vs corresponding chunk headers. Catches silent body dropouts (the d.27 DUB V
class of failure where an entire dubium is missing from a chunk but no [?]
flag is placed).

For each distinction d.N:
  - Slice raw OCR by [DISTINCTIO N start, DISTINCTIO N+1 start)
  - Count semantic markers in the slice: ARTICULUS, QUAESTIO, DUB
    (with OCR-garble tolerant regex)
  - Sum the same headers across all chunks for that distinction
  - Report mismatches

Usage:
  python3.11 tools/audit-headers.py                  # full corpus (Vol I)
  python3.11 tools/audit-headers.py --min-d 27 --max-d 27
  python3.11 tools/audit-headers.py --out manual-review/headers-audit.md
  python3.11 tools/audit-headers.py --volume 2       # Vol II (ranges from frontmatter)

Vol I derives per-distinction raw ranges by parsing `DISTINCTIO N.` headers
in the raw OCR. Vol II's distinction headers are OCR-garbled past reliable
parsing (`DISTINCTIO II.` → `DISTmCTIO 11.`), so for `--volume 2` the raw
slice for distinction d is taken from the chunk frontmatter instead: it is
[min(line_start), max(line_end)] over all `bon-sent-II-d{d}-*` chunks. Those
bounds are author-verified during the re-chunk pass, so this is in fact a
tighter ground truth than header-parsing.
"""
from __future__ import annotations
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def vol_cfg(volume: int) -> dict:
    if volume == 3:
        return dict(
            cdir=REPO / "vol3",
            cglob_all="bon-sent-III-d*.md",
            cglob_d="bon-sent-III-d{}-*.md",
            fn_re=re.compile(r"bon-sent-III-d(\d+)-"),
            raws=[REPO / "raw" / "bonaventure_vol3_raw.txt"],
            ranges_from="frontmatter",
            vlabel="III",
        )
    if volume == 2:
        return dict(
            cdir=REPO / "vol2",
            cglob_all="bon-sent-II-d*.md",
            cglob_d="bon-sent-II-d{}-*.md",
            fn_re=re.compile(r"bon-sent-II-d(\d+)-"),
            raws=[REPO / "raw" / "bonaventure_vol2_raw.txt"],
            ranges_from="frontmatter",
            vlabel="II",
        )
    return dict(
        cdir=REPO / "vol1",
        cglob_all="bon-sent-I-d*.md",
        cglob_d="bon-sent-I-d{}-*.md",
        fn_re=re.compile(r"bon-sent-I-d(\d+)-"),
        raws=[REPO / "raw" / "bonaventure_vol1_raw.txt",
              REPO / "raw" / "bonaventure_vol1_pt2_raw.txt"],
        ranges_from="raw-headers",
        vlabel="I",
    )


FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_fm(text: str) -> dict:
    m = FM_RE.match(text)
    if not m:
        return {}
    out: dict = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def vol2_distinction_line_ranges(cfg: dict) -> dict[int, tuple[int, int]]:
    """Build {d: (min_line_start, max_line_end)} from vol2 chunk frontmatter."""
    spans: dict[int, list[int]] = {}
    for p in sorted(cfg["cdir"].glob(cfg["cglob_all"])):
        m = cfg["fn_re"].match(p.name)
        if not m:
            continue
        d = int(m.group(1))
        fm = parse_fm(p.read_text(encoding="utf-8", errors="replace"))
        try:
            ls, le = int(fm["line_start"]), int(fm["line_end"])
        except (KeyError, ValueError, TypeError):
            continue
        lo, hi = spans.get(d, (ls, le))
        spans[d] = (min(lo, ls), max(hi, le))
    return spans

# OCR-garble-tolerant regex for each marker class.
# pt2 OCR has heavy column-bleed: markers can sit mid-line, indented arbitrarily,
# even paired across columns. We use whitespace-or-line-start anchors so we
# pick up mid-line occurrences but still skip in-word matches.
DIST_RE = re.compile(r"(?:^|\s)DISTINCTIO\s+([IVXL]+)\.", re.MULTILINE)
# ARTICULUS full word — running-head "ART." truncated forms won't match.
ART_RE = re.compile(r"(?:^|\s)ART[IiUuLl]+CULUS\b", re.IGNORECASE)
# QUAESTIO variants: QUAESTIO, QU.ESTIO, QU^STIO, QDAESTIO, QIIAESTIO, etc.
# Require full ESTIO ending so running-head "QUAEST." doesn't match.
QUAEST_RE = re.compile(
    r"(?:^|\s)Q[uUDIi][\.\\\^aAyV]*[A-Za-z]{0,3}ESTIO\b",
)
# DUB variants: DUB., DuB., DiiB., Dlib., DoB., etc. with I/II/III/etc. or 1/2
DUB_RE = re.compile(
    r"(?:^|\s)D[uUiIlLoO][bBrR]\.?\s+[IVXLivxl\d]+\.",
)
# Body header anchors in chunks (markdown ### or #### with DUB/ARTICULUS/QUAESTIO).
# Tolerate "DUB. I" / "Dub. I" / "Dubium I" forms; "QUAESTIO I" or "Question I"
# (we only count Latin-side; English form rare); "ARTICULUS I" or "ART. I".
CHUNK_DUB_RE = re.compile(
    r"^#{2,4}\s+(?:DUB\.|Dub\.|Dubium)\s+([IVXLivxl]+|\d+)",
    re.MULTILINE,
)
CHUNK_ART_RE = re.compile(
    r"^#{2,4}\s+(?:ARTICULUS|Articulus|ART\.)\s+([IVXLivxl]+|UNICUS|Unicus|\d+)",
    re.MULTILINE,
)
CHUNK_QUAEST_RE = re.compile(
    r"^#{2,4}\s+(?:QUAESTIO|Quaestio|QUAEST\.|Quaest\.)\s+([IVXLivxl]+|\d+)",
    re.MULTILINE,
)


def roman_to_int(s: str) -> int:
    table = {"I": 1, "V": 5, "X": 10, "L": 50}
    out, prev = 0, 0
    for ch in reversed(s.upper()):
        v = table.get(ch, 0)
        if v < prev:
            out -= v
        else:
            out += v
        prev = v
    return out


def find_distinction_ranges(raw: str) -> dict[int, tuple[int, int]]:
    """Return {distinctio_number: (start_offset, end_offset)} from raw text."""
    matches = list(DIST_RE.finditer(raw))
    out: dict[int, tuple[int, int]] = {}
    for i, m in enumerate(matches):
        try:
            n = roman_to_int(m.group(1))
        except Exception:
            continue
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
        # Use the FIRST occurrence per number (later ones are commentarius repeats)
        if n not in out:
            out[n] = (start, end)
    return out


def extract_unique_numerals(slice_text: str, marker_re: re.Pattern, numeral_re: re.Pattern) -> set[str]:
    """For each marker hit, extract the roman/digit numeral that follows
    and deduplicate. Page-top header repeats then collapse to a single entry."""
    out: set[str] = set()
    for m in marker_re.finditer(slice_text):
        # Search forward up to 30 chars for a numeral
        tail = slice_text[m.end():m.end() + 30]
        nm = numeral_re.search(tail)
        if nm:
            out.add(nm.group(0).upper())
    return out


NUMERAL_RE = re.compile(r"[IVXLivxl]+|\d+")


def count_markers_in_slice(slice_text: str) -> dict[str, int]:
    return {
        "ART": len(extract_unique_numerals(slice_text, ART_RE, NUMERAL_RE)),
        "QUAEST": len(extract_unique_numerals(slice_text, QUAEST_RE, NUMERAL_RE)),
        "DUB": len(extract_unique_numerals(slice_text, DUB_RE, NUMERAL_RE)),
    }


def count_chunk_headers(distinctio: int, cfg: dict) -> dict[str, int]:
    """Sum unique semantic headers across all chunk files for this distinction.
    Counts only Latin-form headers in `## Latin` body sections.
    Roman-numeral keys are scoped per chunk-file (so two chunks each having
    their own `DUB. I` count as two distinct dubia)."""
    dubs: set[str] = set()
    arts: set[str] = set()
    quaests: set[str] = set()
    for p in sorted(cfg["cdir"].glob(cfg["cglob_d"].format(distinctio))):
        text = p.read_text(encoding="utf-8", errors="replace")
        m = re.match(r"^---\n.*?\n---\n", text, re.DOTALL)
        body = text[m.end():] if m else text
        latin_m = re.search(
            r"^## Latin\s*\n(.*?)(?=^## (?:English|Apparatus)|\Z)",
            body, re.DOTALL | re.MULTILINE,
        )
        section = latin_m.group(1) if latin_m else body
        # Scope per chunk: prefix with stem so identical roman numerals
        # in different chunks (e.g. d8-p1-dubia DUB.I + d8-p2-dubia DUB.I)
        # both count.
        stem = p.stem
        for hit in CHUNK_DUB_RE.findall(section):
            dubs.add(f"{stem}|{hit.upper()}")
        for hit in CHUNK_ART_RE.findall(section):
            arts.add(f"{stem}|{hit.upper()}")
        for hit in CHUNK_QUAEST_RE.findall(section):
            quaests.add(f"{stem}|{hit.upper()}")
    return {"ART": len(arts), "QUAEST": len(quaests), "DUB": len(dubs)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-d", type=int, default=1)
    ap.add_argument("--max-d", type=int, default=48)
    ap.add_argument("--volume", type=int, default=1, choices=(1, 2, 3),
                    help="1 = Vol I (default, ranges from raw DISTINCTIO headers); "
                         "2 = Vol II (ranges from chunk frontmatter)")
    ap.add_argument("--out", default=None, help="optional markdown report path")
    args = ap.parse_args()
    cfg = vol_cfg(args.volume)

    if cfg["ranges_from"] == "frontmatter":
        # Vol II: per-distinction raw slice = [min line_start, max line_end]
        # over that distinction's chunks (line-based into the single raw file).
        raw_lines = cfg["raws"][0].read_text(encoding="utf-8", errors="replace").splitlines()
        spans = vol2_distinction_line_ranges(cfg)

        def slice_for(d: int):
            if d not in spans:
                return None
            lo, hi = spans[d]
            return "\n".join(raw_lines[lo - 1:min(hi, len(raw_lines))])
    else:
        pt1 = cfg["raws"][0].read_text(encoding="utf-8", errors="replace")
        pt2 = cfg["raws"][1].read_text(encoding="utf-8", errors="replace")
        # pt1 covers d.1-d.23 territory; pt2 covers d.24-d.48 territory
        pt1_ranges = find_distinction_ranges(pt1)
        pt2_ranges = find_distinction_ranges(pt2)

        def slice_for(d: int):
            if d <= 23 and d in pt1_ranges:
                s, e = pt1_ranges[d]
                return pt1[s:e]
            if d in pt2_ranges:
                s, e = pt2_ranges[d]
                return pt2[s:e]
            return None

    rows = []
    for d in range(args.min_d, args.max_d + 1):
        slice_text = slice_for(d)
        if slice_text is None:
            continue
        raw_counts = count_markers_in_slice(slice_text)
        chunk_counts = count_chunk_headers(d, cfg)
        diff = {k: chunk_counts[k] - raw_counts[k] for k in raw_counts}
        # raw counts include running-head false positives; keep tolerance
        # Negative diff = chunk has FEWER headers than raw (silent dropout suspect)
        # Large positive diff = chunk has spurious extra headers
        flag = ""
        if diff["DUB"] < -1:
            flag += "DUB-LOSS "
        if diff["QUAEST"] < -1:
            flag += "Q-LOSS "
        if diff["ART"] < -1:
            flag += "A-LOSS "
        rows.append({
            "d": d,
            "raw": raw_counts,
            "chunk": chunk_counts,
            "diff": diff,
            "flag": flag.strip(),
        })

    # Render
    lines = [f"# Header-Inventory Audit — Vol {cfg['vlabel']}", ""]
    lines.append("Per-distinction count of semantic headers in raw OCR vs chunk body bodies. Negative diff = chunk has fewer headers than raw (silent dropout suspect). Tolerance ±1 because OCR has running-head false positives."
                 + (" Vol II ranges are taken from chunk frontmatter line_start/line_end (author-verified), not from parsing OCR-garbled DISTINCTIO headers." if args.volume == 2 else ""))
    lines.append("")
    lines.append("| d | ART raw / chunk / diff | QUAEST raw / chunk / diff | DUB raw / chunk / diff | Flag |")
    lines.append("|---|---|---|---|---|")
    for r in rows:
        ar, qr, dr = r["raw"]["ART"], r["raw"]["QUAEST"], r["raw"]["DUB"]
        ac, qc, dc = r["chunk"]["ART"], r["chunk"]["QUAEST"], r["chunk"]["DUB"]
        ad, qd, dd = r["diff"]["ART"], r["diff"]["QUAEST"], r["diff"]["DUB"]
        lines.append(f"| {r['d']} | {ar} / {ac} / {ad:+d} | {qr} / {qc} / {qd:+d} | {dr} / {dc} / {dd:+d} | {r['flag'] or '—'} |")
    report = "\n".join(lines)

    if args.out:
        out_path = REPO / args.out
        out_path.write_text(report, encoding="utf-8")
        print(f"wrote {out_path}")
    else:
        print(report)

    flagged = [r for r in rows if r["flag"]]
    if flagged:
        print(f"\n{len(flagged)} distinction(s) flagged for review:")
        for r in flagged:
            print(f"  d.{r['d']}: {r['flag']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
