#!/usr/bin/env python3.11
"""Polish-blocker Pass 2: full-corpus style/formatting scan.

Scans every Tier-2 chunk (vol1/ .. vol4/) for the mechanical invariants the
polish-blocker requires. Triage signal — reports, does not fix.

"Full corpus every time" per CLAUDE.md's polish-blocker cadence — vol3/vol4 were
added 2026-07-13 at the Vol IV d.31–d.40 gate (the script had silently been
scanning only vol1+vol2 since Vol III opened).
"""
import re, sys, glob, os

DIRS = ["vol1", "vol2", "vol3", "vol4"]
REQUIRED_FM = ["title_la", "title_en", "printed_pages", "pdf_pages",
               "source", "has_apparatus", "transcription_status"]

def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text[len(m.group(0)):] if m else text
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^(\w+):\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip()
    return fm, text[m.end():]

def is_tier2(fm):
    ts = fm.get("transcription_status", "") if fm else ""
    return "Tier 2 complete" in ts or "Tier 2 apparatus-incomplete" in ts

def body_markers(body):
    # exclude apparatus definition lines (start of line [^N]:)
    out = []
    for line in body.splitlines():
        if re.match(r"^\s*\[\^[^\]]+\]:", line):
            continue
        out.extend(re.findall(r"\[\^([^\]]+)\]", line))
    return out

def main():
    issues = []  # (chunk, severity, msg)
    files = []
    for d in DIRS:
        files.extend(sorted(glob.glob(f"{d}/bon-sent-*.md")))

    seen_ids = {}
    divisio_pars = {}  # distinction-key -> set of pars seen, to detect superseded plain divisio

    for f in files:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        fm, body = parse_frontmatter(text)
        name = os.path.basename(f)
        if fm is None:
            issues.append((name, "ERR", "no frontmatter block"))
            continue
        if not is_tier2(fm):
            continue  # skeleton — skip style checks

        # 1. required frontmatter
        for k in REQUIRED_FM:
            if k not in fm or fm[k] == "" or fm[k] == '""':
                issues.append((name, "FM", f"missing/empty frontmatter: {k}"))

        # 5. transcription_status prefix
        ts = fm.get("transcription_status", "").strip().strip('"')
        if not ts.startswith("Phase C Tier 2 complete —"):
            if "apparatus-incomplete" in ts:
                issues.append((name, "STATUS", "status = apparatus-incomplete (pending rebuild)"))
            else:
                issues.append((name, "STATUS", f"status prefix: {ts[:48]!r}"))

        # 2. structure headers
        has_app = fm.get("has_apparatus", "").lower() == "true"
        if "## Latin" not in body:
            issues.append((name, "STRUCT", "missing ## Latin"))
        if "## English" not in body:
            issues.append((name, "STRUCT", "missing ## English"))
        if has_app and "## Apparatus" not in body:
            issues.append((name, "STRUCT", "has_apparatus:true but no ## Apparatus"))

        # 4. page breaks
        if "<!-- page" not in body:
            issues.append((name, "PAGE", "no <!-- page N --> markers"))

        # 3. apparatus marker pairing
        # split body into Latin / English / Apparatus regions
        defs = re.findall(r"^\s*\[\^([^\]]+)\]:", body, re.M)
        def_set = set(defs)
        # duplicate defs
        dup = set(x for x in defs if defs.count(x) > 1)
        if dup:
            issues.append((name, "APP", f"duplicate apparatus defs: {sorted(dup)}"))

        # regions
        lat = re.search(r"## Latin(.*?)(?:## English|\Z)", body, re.S)
        eng = re.search(r"## English(.*?)(?:## Apparatus|## Notes|\Z)", body, re.S)
        lat_markers = set(body_markers(lat.group(1))) if lat else set()
        eng_markers = set(body_markers(eng.group(1))) if eng else set()

        if has_app:
            # every def should be anchored in both bodies
            missing_lat = def_set - lat_markers
            missing_eng = def_set - eng_markers
            if missing_lat:
                issues.append((name, "PAIR", f"defs not anchored in Latin: {sorted(missing_lat, key=lambda s:(len(s),s))}"))
            if missing_eng:
                issues.append((name, "PAIR", f"defs not anchored in English: {sorted(missing_eng, key=lambda s:(len(s),s))}"))
            # body markers with no def
            orphan_lat = lat_markers - def_set
            orphan_eng = eng_markers - def_set
            orphans = orphan_lat | orphan_eng
            if orphans:
                issues.append((name, "PAIR", f"body markers with no apparatus def: {sorted(orphans, key=lambda s:(len(s),s))}"))

        # 6. legacy duplicate tracking: plain divisio vs pars-split
        m = re.match(r"bon-sent-(I{1,2})-d(\d+)-(p(\d)-)?divisio\.md", name)
        if m:
            key = (m.group(1), m.group(2))
            divisio_pars.setdefault(key, set()).add(m.group(4))  # None for plain

    # report superseded plain divisio
    for key, parsset in divisio_pars.items():
        if None in parsset and any(p for p in parsset if p):
            vol, dn = key
            issues.append((f"bon-sent-{vol}-d{dn}-divisio.md", "DUP",
                           "plain divisio coexists with pars-split divisio (legacy duplicate?)"))

    # output
    if not issues:
        print("CLEAN — no style/formatting issues across Tier-2 corpus.")
        return
    by_chunk = {}
    for c, sev, msg in issues:
        by_chunk.setdefault(c, []).append((sev, msg))
    print(f"# Pass-2 style scan — {len(issues)} issue(s) across {len(by_chunk)} chunk(s)\n")
    for c in sorted(by_chunk):
        print(f"## {c}")
        for sev, msg in by_chunk[c]:
            print(f"  [{sev}] {msg}")
    print(f"\nTotal: {len(issues)} issues / {len(by_chunk)} chunks")

if __name__ == "__main__":
    main()
