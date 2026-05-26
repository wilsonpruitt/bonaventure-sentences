#!/usr/bin/env python3.11
"""Normalize `**En.**` continuation-line indent to exactly 5 spaces.

Per CLAUDE.md "Apparatus conventions": the d.10+ corpus convention is 5
spaces. Pass-2 audit `en_indent_mix` FLAG fires when a single chunk mixes
4/5/6 spaces. This helper rewrites every leading-whitespace span on a
`**En.**` continuation line under an apparatus `[^N]:` def to exactly 5
spaces. Idempotent.

Usage:
    python3.11 tools/normalize-en-indent.py vol1/bon-sent-I-d3-p1-a1-q1.md [more...]
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

EN_LINE_RE = re.compile(r"^( +)(\*\*En\.\*\*)", re.MULTILINE)


def normalize(text: str) -> tuple[str, int]:
    """Rewrite leading whitespace on `**En.**` lines to 5 spaces.

    Returns (new_text, n_replacements_changed)."""
    changes = 0

    def repl(m: re.Match) -> str:
        nonlocal changes
        leading = m.group(1)
        if len(leading) != 5:
            changes += 1
        return "     " + m.group(2)

    new = EN_LINE_RE.sub(repl, text)
    return new, changes


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    total_changed_lines = 0
    total_changed_files = 0
    for arg in argv[1:]:
        path = Path(arg)
        if not path.is_absolute():
            path = REPO / arg
        if not path.exists():
            print(f"MISSING: {path}", file=sys.stderr)
            continue
        orig = path.read_text()
        new, n = normalize(orig)
        if n:
            path.write_text(new)
            total_changed_lines += n
            total_changed_files += 1
            print(f"{path.relative_to(REPO)}: rewrote {n} **En.** line(s)")
        else:
            print(f"{path.relative_to(REPO)}: already normalized")
    print(f"\nFiles changed: {total_changed_files} | lines: {total_changed_lines}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
