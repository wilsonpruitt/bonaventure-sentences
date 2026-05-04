#!/usr/bin/env python3.11
"""Audit Tier-2 formatting consistency across vol1/bon-sent-I-d{N}-*.md chunks.

Severity levels: ERROR (parser/build risk), WARN (convention drift), INFO (notable).
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).resolve().parent.parent
VOL1 = REPO / "vol1"

REQUIRED_FRONTMATTER = {
    "id", "volume", "book", "distinctio", "type",
    "line_start", "line_end", "format_version",
}
TIER2_REQUIRED = {
    "title_la", "title_en", "printed_pages", "pdf_pages", "source",
    "has_apparatus", "transcription_status",
}

PT1_OFFSET = 102   # printed = pdf - 102, i.e., pdf = printed + 102
PT2_OFFSET = -410  # printed = pdf + 410, i.e., pdf = printed - 410
# pt1 covers d.1 through end of d.23 dubia (raw lines up to ~71373 in pt1 file).
# pt2 starts at d.24 (which begins at pt2 raw line 166 onward).
# d.23 dubia is stitched (pt1 + pt2); we expect line_start_pt2/line_end_pt2 there.

def parse_frontmatter(text: str) -> dict | None:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    out: dict = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        # Strip trailing comments
        if val.startswith("[") and val.endswith("]"):
            try:
                out[key] = [int(x.strip()) for x in val[1:-1].split(",") if x.strip()]
                continue
            except ValueError:
                pass
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        out[key] = val
    return out

def section_split(body: str) -> dict[str, str]:
    """Split body by `## Latin / ## English / ## Apparatus` headings."""
    parts = re.split(r"\n##\s+(Latin|English|Apparatus|Notes|Scholion)\s*\n", body)
    sections: dict[str, str] = {}
    if len(parts) < 3:
        return sections
    # parts = [pre, name1, content1, name2, content2, ...]
    for i in range(1, len(parts) - 1, 2):
        sections[parts[i]] = parts[i + 1]
    return sections

def collect_markers(text: str) -> list[str]:
    """All [^N] markers (excluding the [^N]: definition itself).

    Definitions only appear at line start (`^[^N]:`). Inline markers
    immediately followed by a real colon (e.g. `Boethius[^5]: ergo`) must
    still be counted, so we test for line-start, not for trailing `:`.
    """
    out: list[str] = []
    for m in re.finditer(r"\[\^(\d+)\]:?", text):
        is_def = m.group(0).endswith(":") and (m.start() == 0 or text[m.start() - 1] == "\n")
        if not is_def:
            out.append(m.group(1))
    return out

def collect_definitions(text: str) -> list[str]:
    return re.findall(r"^\[\^(\d+)\]:", text, re.MULTILINE)

def audit_chunk(path: Path) -> list[tuple[str, str]]:
    """Return list of (severity, message) findings for this chunk."""
    findings: list[tuple[str, str]] = []
    text = path.read_text()
    fm = parse_frontmatter(text)
    if fm is None:
        return [("ERROR", "no frontmatter block")]

    chunk_id = fm.get("id", path.stem)

    # 1. Required keys
    missing = REQUIRED_FRONTMATTER - set(fm.keys())
    if missing:
        findings.append(("ERROR", f"missing required keys: {sorted(missing)}"))

    # 2. id == filename
    if chunk_id != path.stem:
        findings.append(("ERROR", f"id '{chunk_id}' != filename stem '{path.stem}'"))

    # 3. Tier-2 status check
    status = fm.get("transcription_status", "")
    is_tier2 = "Phase C Tier 2 complete" in status or "Tier 2" in status
    is_skeleton = "auto-chunked" in status

    if is_skeleton:
        return [("INFO", "skeleton (not Tier-2)")]

    if not is_tier2:
        findings.append(("WARN", f"unrecognized transcription_status prefix: {status[:60]}..."))

    # 4. Tier-2 required keys
    missing_t2 = TIER2_REQUIRED - set(fm.keys())
    if missing_t2:
        findings.append(("ERROR", f"missing Tier-2 keys: {sorted(missing_t2)}"))

    # 5. title_en breadcrumb prefix check
    title_en = fm.get("title_en", "")
    if re.search(r"\b[Ii]\s*Sent\.?,?\s*d\.?\s*\d+", title_en):
        findings.append(("WARN", f"title_en has breadcrumb prefix: '{title_en[:60]}...'"))

    # 6. PDF offset check
    printed = fm.get("printed_pages")
    pdf_pp = fm.get("pdf_pages")
    if isinstance(printed, list) and isinstance(pdf_pp, list) and printed and pdf_pp:
        if len(printed) != len(pdf_pp):
            findings.append(("WARN", f"printed/pdf page count mismatch: {len(printed)} vs {len(pdf_pp)}"))
        else:
            offsets = {pdf - prn for prn, pdf in zip(printed, pdf_pp)}
            if len(offsets) > 1:
                findings.append(("ERROR", f"inconsistent offsets within chunk: {offsets}"))
            else:
                offset = offsets.pop()
                # Heuristic: pt2 chunks are d.24+ OR d.23 dubia (stitched).
                d_num = fm.get("distinctio", 0)
                is_pt2 = (isinstance(d_num, str) and d_num.isdigit() and int(d_num) >= 24) or \
                         (isinstance(d_num, int) and d_num >= 24)
                # d.23 dubia is special — it spans both
                if chunk_id == "bon-sent-I-d23-dubia":
                    if offset != PT1_OFFSET:
                        findings.append(("WARN", f"d.23 dubia primary pdf offset {offset} (expected pt1 +102 since printed_pages list pt1 first)"))
                elif is_pt2:
                    if offset != PT2_OFFSET:
                        findings.append(("ERROR", f"pt2 chunk pdf offset {offset:+d} (expected {PT2_OFFSET:+d})"))
                else:
                    if offset != PT1_OFFSET:
                        findings.append(("ERROR", f"pt1 chunk pdf offset {offset:+d} (expected {PT1_OFFSET:+d})"))

    # 7. Body sections
    body = text[text.find("\n---\n") + 5:] if "\n---\n" in text else ""
    sections = section_split(body)
    if "Latin" not in sections:
        findings.append(("ERROR", "no `## Latin` section"))
    if "English" not in sections:
        findings.append(("ERROR", "no `## English` section"))
    if fm.get("has_apparatus") in ("true", "True", True) and "Apparatus" not in sections:
        findings.append(("ERROR", "has_apparatus=true but no `## Apparatus` section"))

    # 8. Marker pairing (Latin vs English)
    if "Latin" in sections and "English" in sections:
        la_markers = sorted(set(collect_markers(sections["Latin"])), key=int)
        en_markers = sorted(set(collect_markers(sections["English"])), key=int)
        if la_markers != en_markers:
            extra_la = set(la_markers) - set(en_markers)
            extra_en = set(en_markers) - set(la_markers)
            msg_parts = []
            if extra_la:
                msg_parts.append(f"in Latin only: {sorted(extra_la, key=int)}")
            if extra_en:
                msg_parts.append(f"in English only: {sorted(extra_en, key=int)}")
            findings.append(("ERROR", "marker mismatch Latin vs English: " + "; ".join(msg_parts)))

    # 9. Apparatus parsing
    if "Apparatus" in sections:
        app_text = sections["Apparatus"]
        defs = collect_definitions(app_text)
        # Each entry should have **La.** and **En.** with 4-space-indented En.
        entries = re.findall(r"^\[\^(\d+)\]:\s*(.*?)(?=^\[\^|\Z)", app_text, re.DOTALL | re.MULTILINE)
        for num, body_text in entries:
            if "**La.**" not in body_text:
                findings.append(("ERROR", f"apparatus [^{num}] missing **La.**"))
            if "**En.**" not in body_text:
                findings.append(("ERROR", f"apparatus [^{num}] missing **En.**"))
            else:
                # En line should be 4-space-indented (markdown list-continuation)
                en_lines = [ln for ln in body_text.splitlines() if "**En.**" in ln]
                for ln in en_lines:
                    if not ln.startswith("    "):
                        findings.append(("WARN", f"apparatus [^{num}] **En.** not 4-space-indented"))

        # Marker count vs definition count
        if "Latin" in sections:
            la_markers_set = set(collect_markers(sections["Latin"]))
            def_set = set(defs)
            missing_def = la_markers_set - def_set
            extra_def = def_set - la_markers_set
            if missing_def:
                findings.append(("ERROR", f"markers without apparatus def: {sorted(missing_def, key=int)}"))
            if extra_def:
                findings.append(("WARN", f"apparatus def with no marker: {sorted(extra_def, key=int)}"))

    # 10. line_start_pt2 only on d.23 dubia
    has_pt2_field = "line_start_pt2" in fm or "line_end_pt2" in fm
    if has_pt2_field and chunk_id != "bon-sent-I-d23-dubia":
        findings.append(("INFO", f"unexpected line_start_pt2/line_end_pt2 fields"))

    return findings


def main() -> int:
    chunk_paths = sorted(VOL1.glob("bon-sent-I-d*.md"))
    # Filter to d.1 through d.25 (numeric extraction)
    target = []
    for p in chunk_paths:
        m = re.match(r"bon-sent-I-d(\d+)-", p.name)
        if m and 1 <= int(m.group(1)) <= 25:
            target.append(p)

    by_sev: dict[str, list[tuple[str, str]]] = defaultdict(list)
    summary: dict[str, int] = defaultdict(int)
    skeleton_count = 0
    tier2_count = 0
    for p in sorted(target):
        findings = audit_chunk(p)
        for sev, msg in findings:
            if sev == "INFO" and "skeleton" in msg:
                skeleton_count += 1
                continue
            by_sev[sev].append((p.name, msg))
            summary[sev] += 1
        if not any(sev == "INFO" and "skeleton" in m for sev, m in findings):
            tier2_count += 1

    print(f"Audited {len(target)} chunks (d.1-d.25): {tier2_count} Tier-2, {skeleton_count} skeleton")
    print(f"Summary: " + ", ".join(f"{k}={v}" for k, v in sorted(summary.items())))
    print()

    for sev in ("ERROR", "WARN", "INFO"):
        rows = by_sev.get(sev, [])
        if not rows:
            continue
        print(f"=== {sev} ({len(rows)}) ===")
        for name, msg in rows:
            print(f"  {name}: {msg}")
        print()

    return 1 if summary.get("ERROR", 0) else 0


if __name__ == "__main__":
    sys.exit(main())
