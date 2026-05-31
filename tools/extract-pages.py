#!/usr/bin/env python3.11
"""
extract-pages.py — batch PDF page extraction for the Bonaventure project.

Wraps the `pdftoppm` command-line tool (from Poppler) to extract one PNG per
printed page of a volume's PDF into `raw/vision/<volume>/p-NNN.png`. The
output directory is keyed off the *printed* page number, not the PDF page
index, so that callers can pass natural citations like "pp. 32–34" without
having to compute the PDF offset each time.

Design:

- Each volume has its own printed-page → PDF-page offset. Vol I pt 1:
  PDF page = printed page + 102. Offsets are configured below.
- The script is idempotent: it skips any page whose output file already
  exists. This lets you extract Dist. 1 on one run, Dist. 2 on another,
  and never re-OCR the overlapping pages.
- `pdftoppm` is invoked once per invocation, with a `-f N -l M` range and
  `-r <resolution>` dpi. Default is 200 dpi, which is a good balance
  between image clarity and file size (typical Vol I PDF page at 200 dpi
  is ~600 kB PNG).
- Prints a summary at the end: extracted vs. skipped vs. errored.

This script deliberately does NOT do any OCR. It just produces page images.
Vision OCR of the images is a separate step (currently done by me reading
the images directly via the Read tool; could be upgraded later to a vision
API backend without changing this script).

Usage:
    # Extract pp. 32–45 (printed page range) of Vol I:
    python3.11 tools/extract-pages.py --volume vol1 --pages 32-45

    # Force re-extraction even if files exist:
    python3.11 tools/extract-pages.py --volume vol1 --pages 32-45 --force

    # Extract a single page:
    python3.11 tools/extract-pages.py --volume vol1 --pages 32

    # Override the resolution (default 200 dpi):
    python3.11 tools/extract-pages.py --volume vol1 --pages 32-45 --dpi 300

Exit codes:
    0 — success (all requested pages were extracted or skipped as already-done)
    1 — one or more errors (pdftoppm failed, missing PDF, invalid range, etc.)
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


# ----------------------------------------------------------------------------
# Volume configuration
# ----------------------------------------------------------------------------

@dataclass
class VolumeConfig:
    """
    Per-volume PDF location and the offset between printed-page numbers and
    PDF page indices. `printed_to_pdf(n)` returns the PDF page that contains
    printed page N.
    """
    name: str
    pdf_path: Path
    # offset = pdf_page - printed_page
    pdf_offset: int
    # Valid printed-page range for the PDF (inclusive).
    printed_min: int
    printed_max: int
    description: str = ""

    def printed_to_pdf(self, printed: int) -> int:
        return printed + self.pdf_offset


# The repo root is the parent of the tools/ directory containing this file.
REPO_ROOT = Path(__file__).resolve().parent.parent

VOLUMES: dict[str, VolumeConfig] = {
    "vol1": VolumeConfig(
        name="vol1",
        pdf_path=REPO_ROOT / "raw" / "doctorisseraphic11bona.pdf",
        pdf_offset=102,          # PDF page = printed page + 102
        printed_min=1,
        printed_max=632,
        description="Opera Omnia, Tomus I pt 1 — Commentarius in I Librum Sententiarum (pp.1–~410)",
    ),
    "vol1-pt2": VolumeConfig(
        name="vol1-pt2",
        pdf_path=REPO_ROOT / "raw" / "doctorisseraphic12bona.pdf",
        pdf_offset=-410,         # PDF page = printed page − 410
        printed_min=411,
        printed_max=872,
        description="Opera Omnia, Tomus I pt 2 — Commentarius in I Librum Sententiarum (pp.~411–872)",
    ),
    "vol2": VolumeConfig(
        name="vol2",
        pdf_path=REPO_ROOT / "raw" / "doctorisseraphic02bona.pdf",
        pdf_offset=22,           # PDF page = printed page + 22 (verified 2026-05-13)
        printed_min=11,
        printed_max=1030,
        description="Opera Omnia, Tomus II — Commentarius in II Librum Sententiarum",
    ),
    # Pending: vol3, vol4 (PDFs local; offsets TBD on first use)
}


# ----------------------------------------------------------------------------
# Page-range parsing
# ----------------------------------------------------------------------------

def parse_range(spec: str) -> list[int]:
    """
    Parse a page-range spec. Supports single pages and hyphen-separated
    ranges; multiple comma-separated segments are allowed.

    Examples:
        "32"          → [32]
        "32-34"       → [32, 33, 34]
        "32,35-37"    → [32, 35, 36, 37]
    """
    pages: list[int] = []
    for segment in spec.split(","):
        segment = segment.strip()
        if not segment:
            continue
        if "-" in segment:
            lo, hi = segment.split("-", 1)
            try:
                lo_i, hi_i = int(lo), int(hi)
            except ValueError as e:
                raise ValueError(f"invalid range '{segment}'") from e
            if hi_i < lo_i:
                raise ValueError(f"range endpoints reversed: '{segment}'")
            pages.extend(range(lo_i, hi_i + 1))
        else:
            try:
                pages.append(int(segment))
            except ValueError as e:
                raise ValueError(f"invalid page '{segment}'") from e
    # Dedupe while preserving order.
    seen: set[int] = set()
    ordered: list[int] = []
    for p in pages:
        if p not in seen:
            seen.add(p)
            ordered.append(p)
    return ordered


# ----------------------------------------------------------------------------
# Extraction
# ----------------------------------------------------------------------------

# The Anthropic API rejects any single image whose base64 payload exceeds
# 5 MB (the messages.N.content.M: 400 error). base64 inflates the on-disk
# size ~1.37x, so a PNG larger than this threshold cannot be Read directly —
# it must be cropped first (tools/colcrop.py) before sending to the model.
MAX_SAFE_BYTES = 3_600_000  # ~4.9 MB once base64-encoded


@dataclass
class Result:
    extracted: list[int]
    skipped: list[int]
    errored: list[tuple[int, str]]
    # (printed_page, size_bytes) for files too large to Read without cropping.
    oversized: list[tuple[int, int]]


def output_path(volume: str, printed: int) -> Path:
    return REPO_ROOT / "raw" / "vision" / volume / f"p-{printed:03d}.png"


def extract_one(
    config: VolumeConfig,
    printed: int,
    dpi: int,
    force: bool,
) -> tuple[str, str | None]:
    """
    Extract a single printed page. Returns (status, error_message).
    status ∈ {"extracted", "skipped", "error"}.
    """
    if printed < config.printed_min or printed > config.printed_max:
        return (
            "error",
            f"page {printed} out of range [{config.printed_min}, {config.printed_max}]",
        )

    out_path = output_path(config.name, printed)
    if out_path.exists() and not force:
        return ("skipped", None)

    out_path.parent.mkdir(parents=True, exist_ok=True)

    pdf_page = config.printed_to_pdf(printed)
    # pdftoppm's -f / -l are 1-indexed; it writes to <prefix>-<page>.png.
    # We use a temporary prefix, then rename the single output file so the
    # final name uses the *printed* page number, not the PDF page number.
    tmp_prefix = out_path.parent / f".tmp-{printed:03d}"
    cmd = [
        "pdftoppm",
        "-png",
        "-r", str(dpi),
        "-f", str(pdf_page),
        "-l", str(pdf_page),
        str(config.pdf_path),
        str(tmp_prefix),
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        return ("error", f"pdftoppm exited {e.returncode}: {e.stderr.decode(errors='replace').strip()}")
    except FileNotFoundError:
        return ("error", "pdftoppm not found on PATH (brew install poppler)")

    # pdftoppm names files as <prefix>-<NNNNNN>.png where NNNNNN is zero-
    # padded to the width of the page count. Find the one file we just made.
    candidates = sorted(tmp_prefix.parent.glob(f"{tmp_prefix.name}-*.png"))
    if not candidates:
        return ("error", f"pdftoppm produced no output for pdf page {pdf_page}")
    if len(candidates) > 1:
        return ("error", f"pdftoppm produced multiple outputs: {[c.name for c in candidates]}")
    candidates[0].replace(out_path)
    return ("extracted", None)


def extract_pages(
    volume: str,
    pages: list[int],
    dpi: int = 200,
    force: bool = False,
) -> Result:
    if volume not in VOLUMES:
        raise ValueError(
            f"unknown volume '{volume}'; known: {sorted(VOLUMES.keys())}"
        )
    config = VOLUMES[volume]
    if not config.pdf_path.exists():
        raise FileNotFoundError(f"PDF not found at {config.pdf_path}")

    result = Result(extracted=[], skipped=[], errored=[], oversized=[])
    for printed in pages:
        status, err = extract_one(config, printed, dpi, force)
        if status == "extracted":
            result.extracted.append(printed)
            size = output_path(volume, printed).stat().st_size
            if size > MAX_SAFE_BYTES:
                result.oversized.append((printed, size))
        elif status == "skipped":
            result.skipped.append(printed)
        else:
            result.errored.append((printed, err or "unknown error"))
    return result


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Extract one PNG per printed page of a Bonaventure volume "
            "into raw/vision/<volume>/p-NNN.png. Idempotent: skips pages "
            "whose output files already exist."
        )
    )
    parser.add_argument(
        "--volume", "-V", required=True, choices=sorted(VOLUMES.keys()),
        help="Which volume to extract from",
    )
    parser.add_argument(
        "--pages", "-p", required=True,
        help="Page range to extract, e.g. '32-45' or '32,35-37' (printed page numbers)",
    )
    parser.add_argument(
        "--dpi", type=int, default=200,
        help="Resolution in dpi (default: 200)",
    )
    parser.add_argument(
        "--force", "-f", action="store_true",
        help="Re-extract pages even if their output files already exist",
    )
    args = parser.parse_args()

    if not shutil.which("pdftoppm"):
        print("error: pdftoppm not found on PATH. Install poppler:", file=sys.stderr)
        print("  brew install poppler", file=sys.stderr)
        return 1

    try:
        pages = parse_range(args.pages)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    try:
        result = extract_pages(args.volume, pages, dpi=args.dpi, force=args.force)
    except (ValueError, FileNotFoundError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    print(f"Volume: {args.volume} ({VOLUMES[args.volume].description})")
    print(f"Requested: {len(pages)} pages ({args.pages})")
    print(f"Extracted: {len(result.extracted)}")
    print(f"Skipped:   {len(result.skipped)} (already existed)")
    if result.oversized:
        print(
            f"⚠ Oversized: {len(result.oversized)} page(s) exceed ~{MAX_SAFE_BYTES // 1_000_000} MB — "
            "too large to Read directly (Anthropic API caps images at 5 MB base64)."
        )
        for printed, size in result.oversized:
            print(f"  p. {printed}: {size / 1_048_576:.1f} MB — crop before reading, e.g.")
            print(f"      python3.11 tools/colcrop.py {args.volume} {printed}")
    if result.errored:
        print(f"Errored:   {len(result.errored)}")
        for printed, err in result.errored:
            print(f"  p. {printed}: {err}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
