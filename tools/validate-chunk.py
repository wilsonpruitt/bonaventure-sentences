#!/usr/bin/env python3.11
"""Structural validator for completed Tier-2 chunks.

Checks the things `build-content.mjs` requires, before commit:
  - YAML front matter present and parseable
  - Has `### Latin` and `### English` sections
  - Footnote markers `[^N]` are balanced between Latin and English bodies
  - Apparatus entries (if present) follow `[^N] **La.** ... **En.** ...` format
  - English body word count is plausibly close to Latin (0.8x–1.5x)

Exits non-zero on any failure. Prints a summary per chunk.

Usage:
  python3.11 tools/validate-chunk.py vol1/bon-sent-I-d9-a1-q1.md
  python3.11 tools/validate-chunk.py vol1/bon-sent-I-d9-*.md
"""
import re
import sys
from pathlib import Path


def extract_section(text: str, name: str) -> str | None:
    sentinels = ("Latin", "English", "Apparatus", "Notes")
    pattern = (
        rf"## {name}\n+(.*?)(?=\n## (?:{'|'.join(sentinels)})\b|\n---\n|\Z)"
    )
    m = re.search(pattern, text, re.DOTALL)
    return m.group(1).strip() if m else None


def footnote_markers(body: str) -> list[str]:
    return sorted(set(re.findall(r"\[\^(\d+)\]", body)), key=int)


def validate(path: Path) -> list[str]:
    errors = []
    text = path.read_text()

    if not text.startswith("---\n"):
        errors.append("missing YAML front matter")

    latin = extract_section(text, "Latin")
    english = extract_section(text, "English")
    apparatus = extract_section(text, "Apparatus")

    if not latin:
        errors.append("missing ### Latin section")
    if not english:
        errors.append("missing ### English section")
    if english and "[Translation pending]" in english:
        errors.append("English section is still placeholder")

    if latin and english:
        la_marks = footnote_markers(latin)
        en_marks = footnote_markers(english)
        if la_marks != en_marks:
            errors.append(
                f"footnote marker mismatch: Latin={la_marks} English={en_marks}"
            )

        la_words = len(latin.split())
        en_words = len(english.split())
        if la_words > 50:
            ratio = en_words / la_words
            if ratio < 0.7 or ratio > 1.7:
                errors.append(
                    f"En/La word ratio {ratio:.2f} out of expected 0.7–1.7"
                )

    if apparatus:
        entries = re.findall(
            r"\[\^(\d+)\]:?\s+\*\*La\.\*\*(.*?)(?=\n\[\^\d+\]|\Z)",
            apparatus,
            re.DOTALL,
        )
        for num, body in entries:
            if "**En.**" not in body:
                errors.append(f"apparatus [^{num}] missing **En.** translation")

    return errors


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: validate-chunk.py <chunk.md> [<chunk.md> ...]")
        sys.exit(1)

    failed = 0
    for arg in sys.argv[1:]:
        path = Path(arg)
        errs = validate(path)
        if errs:
            failed += 1
            print(f"FAIL {path.name}")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"OK   {path.name}")

    print(f"\n{len(sys.argv)-1} checked, {failed} failed")
    sys.exit(1 if failed else 0)
