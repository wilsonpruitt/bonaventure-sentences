#!/usr/bin/env python3.11
"""Pass-3 seam-continuity screen for a Vol II distinction range.

For each adjacent chunk pair in canonical order, determine whether they share a
printed page (mid-page boundary). For mid-page boundaries, surface the prior
chunk's Latin-body tail and the next chunk's Latin-body head so a human (or a
targeted PDF re-read) can confirm grammatical continuity — the cascade-merge
signature is a grammatically broken splice in the prior chunk's tail.
"""
import re, sys, glob, os, ast

def fm_field(text, key):
    m = re.search(rf"^{key}:\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else None

def printed_pages(text):
    raw = fm_field(text, "printed_pages")
    if not raw:
        return []
    try:
        return ast.literal_eval(raw)
    except Exception:
        return [int(x) for x in re.findall(r"\d+", raw)]

def latin_body(text):
    m = re.search(r"## Latin(.*?)(?:## English)", text, re.S)
    if not m:
        return ""
    body = m.group(1)
    # strip page comments, headings, blockquote markers for tail/head sampling
    lines = [l.rstrip() for l in body.splitlines()
             if l.strip() and not l.strip().startswith("<!--")
             and not l.strip().startswith("#") and not l.strip().startswith("---")]
    return lines

# canonical sort key for chunk filenames
def sortkey(name):
    m = re.search(r"d(\d+)(?:-p(\d))?(?:-a(\d))?(?:-q(\d))?", name)
    d = int(m.group(1))
    pars = int(m.group(2)) if m.group(2) else 0
    art = int(m.group(3)) if m.group(3) else 0
    q = int(m.group(4)) if m.group(4) else 0
    # type ordering within a distinction/pars: littera, divisio, articles, dubia
    if "littera" in name: typ = 0
    elif "divisio" in name: typ = 1
    elif "dubia" in name: typ = 9
    else: typ = 2
    return (d, pars, typ, art, q)

TERMINAL = ('.', '»', ':', '?', '!', '"')

VOL = {1: ("vol1", "I"), 2: ("vol2", "II"), 3: ("vol3", "III")}

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    vol = 2
    for a in sys.argv[1:]:
        if a.startswith("--volume"):
            vol = int(a.split("=")[-1]) if "=" in a else int(sys.argv[sys.argv.index(a)+1])
    min_d, max_d = int(args[0]), int(args[1])
    vdir, vrom = VOL[vol]
    files = []
    for f in glob.glob(f"{vdir}/bon-sent-{vrom}-d*.md"):
        m = re.search(r"-d(\d+)", f)
        if m and min_d <= int(m.group(1)) <= max_d:
            files.append(f)
    files.sort(key=lambda f: sortkey(os.path.basename(f)))

    chunks = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            t = fh.read()
        if "Tier 2 complete" not in (fm_field(t, "transcription_status") or ""):
            continue
        chunks.append((os.path.basename(f), printed_pages(t), latin_body(t)))

    print(f"# Pass-3 seam screen d{min_d}-d{max_d} — {len(chunks)} Tier-2 chunks\n")
    midpage = 0
    suspects = []
    for i in range(len(chunks) - 1):
        name, pp, body = chunks[i]
        nname, npp, nbody = chunks[i+1]
        if not pp or not npp or not body or not nbody:
            continue
        shares = pp[-1] == npp[0]
        if not shares:
            continue
        midpage += 1
        tail = body[-1]
        head = nbody[0]
        broken = not tail.rstrip().endswith(TERMINAL)
        flag = "  <-- TAIL NOT TERMINAL" if broken else ""
        if broken:
            suspects.append((name, nname, pp[-1]))
        print(f"[p.{pp[-1]}] {name} -> {nname}{flag}")
        print(f"    tail: ...{tail[-120:]}")
        print(f"    head: {head[:100]}...")
        print()
    print(f"\n{midpage} mid-page boundaries; {len(suspects)} tail-not-terminal suspect(s).")
    for s in suspects:
        print(f"  SUSPECT p.{s[2]}: {s[0]} -> {s[1]}")

if __name__ == "__main__":
    main()
