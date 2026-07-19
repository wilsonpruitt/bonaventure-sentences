#!/usr/bin/env python3.11
"""Pass 2 style/formatting audit — full corpus, Vols I–IV.

Per CLAUDE.md "Polish-blocker cadence" §2. Streams file-by-file (8 GB RAM Mac).
Identifies Tier-2 chunks by transcription_status prefix and flags:

  1. Missing Tier-2 frontmatter (title_la, title_en, printed_pages,
     pdf_pages, source, has_apparatus, transcription_status).
  2. Missing `## Latin`, `## English`, `## Apparatus` sections.
  3. Apparatus marker pairing: every `[^N]:` def has matching `[^N]` body
     anchors in BOTH Latin and English; no orphan body anchors w/o def.
  4. Missing page-break `<!-- page N -->` comments.
  5. transcription_status not starting with `Phase C Tier 2 complete —`.
  6. Legacy auto-chunked duplicates (e.g. d{N}-divisio.md superseded by
     d{N}-p1-divisio.md + d{N}-p2-divisio.md).
  7. `**En.**` indent inconsistency WITHIN a single chunk (mixing 4 and 5).

Apparatus labels may be bare-numeric (`[^12]`, Vols I–III) or page-qualified
(`[^p1005-1]`, `[^p997n-2]`, Vol IV) — see LABEL_RE and label_sort_key. Matching
only digits here silently blinded every Vol IV apparatus check.

Writes a triage report to manual-review/corpus-style-audit.md.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).resolve().parent.parent
# Renamed 2026-07-19: the old name ("vol3-d21-d30-pass2-style-audit.md") dated
# from the gate that first ran this and was misleading — the scan is full-corpus
# and now covers Vols I–IV, not one volume's decade.
REPORT_PATH = REPO / "manual-review" / "corpus-style-audit.md"

TIER2_REQUIRED = [
    "title_la", "title_en", "printed_pages", "pdf_pages",
    "source", "has_apparatus", "transcription_status",
]

TIER2_STATUS_PREFIX = "Phase C Tier 2 complete —"
SKELETON_MARKERS = ("auto-chunked", "skeleton")


def parse_frontmatter(text: str) -> dict | None:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    out: dict = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        v = v.strip()
        # Strip surrounding double quotes (frontmatter strings)
        if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
            v = v[1:-1]
        out[k.strip()] = v
    return out


def split_sections(body: str) -> dict[str, str]:
    parts = re.split(r"\n##\s+(Latin|English|Apparatus|Notes|Scholion)\s*\n",
                     body)
    sections: dict[str, str] = {}
    if len(parts) < 3:
        return sections
    for i in range(1, len(parts) - 1, 2):
        sections[parts[i]] = parts[i + 1]
    return sections


def label_sort_key(label: str) -> tuple:
    """Order apparatus labels that may be bare-numeric OR page-qualified.

    Vols I–III use bare `[^12]`. Vol IV uses page-qualified `[^p1005-1]`, plus
    register suffixes for pages carrying two footer registers (`[^p997n-2]`,
    `[^p983c-1]` — see CLAUDE.md). A plain `key=int` raises ValueError on those,
    which is why every sort here goes through this instead.
    """
    m = re.fullmatch(r"p(\d+)([a-z]*)-(\d+)", label)
    if m:
        return (1, int(m.group(1)), m.group(2), int(m.group(3)))
    if label.isdigit():
        return (0, int(label), "", 0)
    return (2, 0, label, 0)


# Matches bare-numeric and page-qualified labels alike. Digits-only here was a
# silent Vol IV blind spot: page-qualified labels matched nothing, so defs and
# anchors both came back empty and every Vol IV chunk's apparatus pairing
# reported clean without ever being checked.
LABEL_RE = r"[A-Za-z0-9-]+"


def body_anchors(text: str) -> set[str]:
    """Return set of [^N] body anchors (not definitions)."""
    out: set[str] = set()
    for m in re.finditer(rf"\[\^({LABEL_RE})\]", text):
        # Skip if it's a definition (line-start `[^N]:`)
        start = m.start()
        line_start = text.rfind("\n", 0, start) + 1
        rest = text[m.end():m.end() + 1]
        if start == line_start and rest == ":":
            continue
        out.add(m.group(1))
    return out


def app_definitions(text: str) -> list[str]:
    return re.findall(rf"^\[\^({LABEL_RE})\]:", text, re.MULTILINE)


def en_indent_widths(app_text: str) -> set[int]:
    """Return set of leading-space counts on **En.** continuation lines."""
    widths: set[int] = set()
    for m in re.finditer(r"^( +)\*\*En\.\*\*", app_text, re.MULTILINE):
        widths.add(len(m.group(1)))
    return widths


def is_tier2(fm: dict) -> bool:
    status = fm.get("transcription_status", "")
    if any(s in status for s in SKELETON_MARKERS):
        return False
    return TIER2_STATUS_PREFIX in status or "Tier 2" in status


def expected_pages(fm: dict) -> list[int]:
    raw = fm.get("printed_pages", "")
    m = re.match(r"\[(.*)\]", raw)
    if not m:
        return []
    out: list[int] = []
    for tok in m.group(1).split(","):
        tok = tok.strip()
        if tok.isdigit():
            out.append(int(tok))
    return out


def audit_chunk(path: Path) -> dict:
    """Stream a single chunk; return findings dict."""
    text = path.read_text()
    fm = parse_frontmatter(text)
    findings: dict[str, list[str]] = defaultdict(list)
    if fm is None:
        findings["no_frontmatter"].append("no frontmatter block")
        return {"path": path, "fm": {}, "tier2": False, "findings": findings}

    if not is_tier2(fm):
        return {"path": path, "fm": fm, "tier2": False, "findings": findings}

    # 1. Required Tier-2 frontmatter
    for k in TIER2_REQUIRED:
        if k not in fm or not fm[k]:
            findings["missing_frontmatter"].append(k)

    # 5. status prefix
    status = fm.get("transcription_status", "")
    if not status.startswith(TIER2_STATUS_PREFIX):
        findings["status_prefix"].append(status[:80])

    # 2. Sections
    body_start = text.find("\n---\n")
    body = text[body_start + 5:] if body_start >= 0 else text
    sections = split_sections(body)
    for s in ("Latin", "English"):
        if s not in sections:
            findings["missing_section"].append(s)
    has_app = fm.get("has_apparatus", "").lower().startswith("true")
    if has_app and "Apparatus" not in sections:
        findings["missing_section"].append("Apparatus")

    # 3. Apparatus marker pairing
    if "Apparatus" in sections:
        defs = set(app_definitions(sections["Apparatus"]))
        la_anchors = body_anchors(sections.get("Latin", ""))
        en_anchors = body_anchors(sections.get("English", ""))
        # orphan defs (def with no body anchor in either body)
        orphan_defs = sorted(defs - (la_anchors | en_anchors), key=label_sort_key)
        if orphan_defs:
            findings["orphan_app_defs"].extend(orphan_defs)
        # body anchors with no def
        missing_def_la = sorted(la_anchors - defs, key=label_sort_key)
        missing_def_en = sorted(en_anchors - defs, key=label_sort_key)
        if missing_def_la:
            findings["body_anchor_no_def_la"].extend(missing_def_la)
        if missing_def_en:
            findings["body_anchor_no_def_en"].extend(missing_def_en)
        # La<->En anchor mismatch
        only_la = sorted(la_anchors - en_anchors, key=label_sort_key)
        only_en = sorted(en_anchors - la_anchors, key=label_sort_key)
        if only_la:
            findings["anchor_only_la"].extend(only_la)
        if only_en:
            findings["anchor_only_en"].extend(only_en)

        # 7. **En.** indent mix within chunk
        widths = en_indent_widths(sections["Apparatus"])
        if len(widths) > 1:
            findings["en_indent_mix"].append(
                ",".join(str(w) for w in sorted(widths)))

    # 8. Scholion ordering: ### Scholion must be the LAST subsection of its
    #    ## Latin / ## English block (parser reads everything after it as the
    #    scholion → body content after ### Scholion is silently emptied).
    for sec_name in ("Latin", "English"):
        sec = sections.get(sec_name, "")
        sm = re.search(r"\n###\s+Scholion\b", sec)
        if not sm:
            continue
        after = sec[sm.end():]
        # Any further ### subsection (e.g. a quaestio/article header) or a
        # non-scholion ## heading after Scholion means body content follows it.
        if re.search(r"\n###\s+(?!Scholion)\S", after):
            findings["scholion_not_last"].append(sec_name)

    # 4. Page-break presence
    pages = expected_pages(fm)
    if pages:
        page_comments = re.findall(r"<!--\s*page\s+(\d+)\s*-->",
                                   sections.get("Latin", ""))
        if not page_comments:
            findings["no_page_breaks"].append(
                f"printed_pages={pages} but 0 <!-- page N --> comments")

    return {"path": path, "fm": fm, "tier2": True, "findings": findings}


def find_legacy_duplicates(chunks: list[Path]) -> list[tuple[str, list[str]]]:
    """Detect d{N}-divisio.md superseded by d{N}-p1-divisio.md + d{N}-p2-divisio.md
    (and similar for other no-pars types when pars-split siblings exist)."""
    by_dir: dict[Path, dict[str, list[Path]]] = defaultdict(
        lambda: defaultdict(list))
    for p in chunks:
        # Extract distinctio number + type from filename
        # Covers all four volumes. Alternation is ordered LONGEST-FIRST
        # (IV|III|II|I) so "IV" cannot be partially consumed as "I"; the old
        # (?:I|II) form only worked by backtracking and silently skipped
        # Vols III and IV entirely. The optional -s\d+ group is the editorial
        # "sectio" level (Vol IV d.49 P.II only, see CLAUDE.md §5a).
        m = re.match(
            r"bon-sent-(?:IV|III|II|I)-d(\d+)(?:-(p\d+))?(?:-s\d+)?"
            r"-(\w+(?:-q\d+)?)\.md",
            p.name)
        if not m:
            continue
        d_num, pars, rest = m.groups()
        key = (d_num, rest)
        by_dir[p.parent][key].append(p)

    dups: list[tuple[str, list[str]]] = []
    # -dup2 vestigial auto-chunker skeletons: <chunk>-dup2.md superseded by
    # the canonical <chunk>.md when the canonical is Tier-2.
    for p in chunks:
        if not p.name.endswith("-dup2.md"):
            continue
        canonical = p.parent / p.name.replace("-dup2.md", ".md")
        if canonical.exists():
            dups.append((str(p.relative_to(REPO)),
                         [str(canonical.relative_to(REPO))]))
    for parent, key_map in by_dir.items():
        # For each (d_num, rest), find both a non-pars file AND pars-split siblings
        for (d_num, rest), paths in key_map.items():
            has_nonpars = False
            has_pars = False
            for p in paths:
                # Check if this exact filename has p1/p2 in it
                if re.search(rf"-d{d_num}-p\d+(?:-s\d+)?-{re.escape(rest)}\.md$", p.name):
                    has_pars = True
                elif re.search(rf"-d{d_num}-{re.escape(rest)}\.md$", p.name):
                    has_nonpars = True
            # Also need to look at OTHER paths in parent matching pars-variants
            # of this rest+d_num
            if has_nonpars:
                pars_variants = [
                    pp for pp in parent.glob(
                        f"bon-sent-*-d{d_num}-p*-{rest}.md")
                ]
                if pars_variants:
                    nonpars_file = [
                        p for p in paths
                        if re.search(rf"-d{d_num}-{re.escape(rest)}\.md$",
                                     p.name)
                    ][0]
                    dups.append((str(nonpars_file.relative_to(REPO)), [
                        str(pv.relative_to(REPO)) for pv in pars_variants
                    ]))
    return dups


def main() -> int:
    chunks: list[Path] = []
    for vol_dir, prefix in [(REPO / "vol1", "bon-sent-I-d"),
                            (REPO / "vol2", "bon-sent-II-d"),
                            (REPO / "vol3", "bon-sent-III-d"),
                            (REPO / "vol4", "bon-sent-IV-d")]:
        if vol_dir.exists():
            chunks.extend(sorted(vol_dir.glob(f"{prefix}*.md")))

    results = []
    tier2_count = {"vol1": 0, "vol2": 0, "vol3": 0, "vol4": 0}
    skeleton_count = 0
    for p in chunks:
        r = audit_chunk(p)
        results.append(r)
        if r["tier2"]:
            # Derive the key from the path rather than an else-fallback: the
            # old form defaulted anything non-vol1/vol2 to "vol3", so adding a
            # volume without touching this would have silently mis-tallied it.
            key = next((v for v in ("vol1", "vol2", "vol3", "vol4")
                        if f"/{v}/" in str(p)), None)
            if key is None:
                raise RuntimeError(f"chunk in unrecognised volume dir: {p}")
            tier2_count[key] += 1
        else:
            skeleton_count += 1

    # Legacy duplicate scan (across all chunks, not just Tier-2)
    dups = find_legacy_duplicates(chunks)

    # Tally failures
    mode_tally: dict[str, int] = defaultdict(int)
    chunk_failures: list[dict] = []
    for r in results:
        if not r["tier2"]:
            continue
        if not r["findings"]:
            continue
        for mode in r["findings"]:
            mode_tally[mode] += 1
        chunk_failures.append(r)

    # Build report
    lines: list[str] = []
    lines.append("# Pass 2 — Style/Formatting Audit (full corpus, Vols I–IV)")
    lines.append("")
    lines.append(
        f"Generated by `tools/audit-style-formatting.py`. "
        f"Walked Vol I={tier2_count['vol1']} + Vol II={tier2_count['vol2']} "
        f"+ Vol III={tier2_count['vol3']} + Vol IV={tier2_count['vol4']} "
        f"Tier-2 chunks ({skeleton_count} skeletons skipped).")
    lines.append("")
    lines.append("## Failure-mode tallies")
    lines.append("")
    if mode_tally:
        for mode, n in sorted(mode_tally.items(), key=lambda x: -x[1]):
            lines.append(f"- `{mode}`: {n} chunk(s)")
    else:
        lines.append("- (none)")
    lines.append("")
    lines.append(f"Legacy auto-chunked duplicates: {len(dups)}")
    lines.append("")

    # Per-mode sections
    by_mode: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for r in chunk_failures:
        chunk_id = r["path"].name
        for mode, vals in r["findings"].items():
            detail = ", ".join(str(v) for v in vals) if vals else ""
            by_mode[mode].append((chunk_id, detail))

    for mode in sorted(by_mode.keys()):
        lines.append(f"## FLAG `{mode}` ({len(by_mode[mode])})")
        lines.append("")
        for chunk_id, detail in sorted(by_mode[mode]):
            lines.append(f"- `{chunk_id}` — {detail}")
        lines.append("")

    if dups:
        lines.append(f"## FLAG `legacy_duplicate` ({len(dups)})")
        lines.append("")
        for nonpars, parsvars in sorted(dups):
            lines.append(f"- `{nonpars}` superseded by {parsvars}")
        lines.append("")

    REPORT_PATH.parent.mkdir(exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines))

    # Console summary
    total_flags = sum(mode_tally.values()) + len(dups)
    print(" | ".join(
        f"Vol {roman} Tier-2: {tier2_count[key]}"
        for roman, key in (("I", "vol1"), ("II", "vol2"),
                           ("III", "vol3"), ("IV", "vol4")))
        + f" | skeletons skipped: {skeleton_count}")
    print(f"Failure tallies: {dict(mode_tally)}")
    print(f"Legacy duplicates: {len(dups)}")
    print(f"Total FLAGs: {total_flags}")
    print(f"Report: {REPORT_PATH.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
