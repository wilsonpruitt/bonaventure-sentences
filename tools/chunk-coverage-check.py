#!/usr/bin/env python3.11
"""Diagnostic: compare raw-OCR semantic structure vs existing chunk files for Vol II.

Read-only. Flags the d.32-class failures:
  - folded questions (raw has more QUAESTIO headers under an article than chunk files)
  - mislabeled / duplicate chunks (-dup2/-dup3 files)
  - missing littera / divisio / dubia
  - article/question count mismatch vs the TRACTATIO plan

Usage: python3.11 tools/chunk-coverage-check.py 33 40
"""
import re, sys, glob, os

RAW = "raw/bonaventure_vol2_raw.txt"

# distinction body ranges (start line of each DISTINCTIO header, OCR-tolerant)
def dist_starts():
    pat = re.compile(r"^\s+(?:COMMENTARIUS\s+IN\s+)?DISTINCTIO\s+", re.I)
    rom = re.compile(r"DISTINCTIO\s+((?:X{1,3})(?:IX|IV|V?I{0,3})|XL(?:I{0,3}|IV|V?I{0,3}))\b", re.I)
    starts = {}
    with open(RAW) as f:
        lines = f.readlines()
    # only the body region (before the end-of-volume index ~line 71000)
    for i, ln in enumerate(lines, 1):
        if i > 70000:
            break
        if pat.match(ln):
            m = rom.search(ln.upper().replace("XXXLIL", "XXXIII").replace("XLLL", "XLIII"))
            if m:
                n = roman_to_int(m.group(1).upper())
                if n and n not in starts:
                    starts[n] = i
    return starts, lines

def roman_to_int(s):
    vals = {"I":1,"V":5,"X":10,"L":50}
    if not s or any(c not in vals for c in s):
        return None
    total, prev = 0, 0
    for c in reversed(s):
        v = vals[c]
        total += -v if v < prev else v
        prev = max(prev, v)
    return total

# OCR-tolerant standalone-header regexes (anchored: lots of leading whitespace, header alone-ish)
ART = re.compile(r"^\s{20,}[\^'`.]?ARTI[CG]ULUS\s+([IVXL]+|in|il|ill|iv|v|vi)\b", re.I)
QUA = re.compile(r"^\s{25,}[\^'`.]{0,2}QU[.\^A-Z\\]{0,3}ESTIO\s+([IVXLU]+|il|in|ill)\b", re.I)
DUB = re.compile(r"^\s{15,}DUB\.?\s+([IVXL]+)\b", re.I)
TRACT = re.compile(r"TRACTATIO\s+QU", re.I)

def scan(lines, lo, hi):
    arts, quas, dubs = [], [], []
    for i in range(lo, min(hi, len(lines))):
        ln = lines[i]
        # skip running heads: lines that ALSO contain a page number / DIST. running head
        if re.search(r"DIST\.\s", ln):
            continue
        m = ART.match(ln)
        if m: arts.append((i+1, ln.strip()[:50]))
        m = QUA.match(ln)
        if m: quas.append((i+1, ln.strip()[:50]))
        m = DUB.match(ln)
        if m: dubs.append((i+1, ln.strip()[:40]))
    return arts, quas, dubs

def main():
    d_lo, d_hi = int(sys.argv[1]), int(sys.argv[2])
    starts, lines = dist_starts()
    print(f"# Chunk-coverage diagnostic — Vol II d.{d_lo}–d.{d_hi}\n")
    ordered = sorted(starts)
    for d in range(d_lo, d_hi+1):
        if d not in starts:
            print(f"## d.{d}: NO DISTINCTIO header found in raw — INVESTIGATE\n")
            continue
        lo = starts[d]
        nxt = [n for n in ordered if n > d]
        hi = starts[nxt[0]] if nxt else len(lines)
        arts, quas, dubs = scan(lines, lo, hi)
        files = sorted(glob.glob(f"vol2/bon-sent-II-d{d}-*.md"))
        fnames = [os.path.basename(f).replace("bon-sent-II-","").replace(".md","") for f in files]
        dups = [f for f in fnames if "dup" in f]
        has_litt = any("littera" in f for f in fnames)
        has_div  = any("divisio" in f for f in fnames)
        has_dub  = any("dubia" in f for f in fnames)
        q_files  = [f for f in fnames if re.search(r"-q\d", f) and "dup" not in f]
        flags = []
        if not has_litt: flags.append("NO littera file")
        if not has_div:  flags.append("NO divisio file")
        if dubs and not has_dub: flags.append("raw has DUB but NO dubia file")
        if dups: flags.append("DUP files: " + ",".join(dups))
        # fold check: raw quaestio count vs quaestio file count
        if len(quas) != len(q_files):
            flags.append(f"QUAESTIO count mismatch: raw={len(quas)} files={len(q_files)}")
        print(f"## d.{d}  (raw lines {lo}–{hi})")
        print(f"  raw markers: ARTICULUS={len(arts)}  QUAESTIO={len(quas)}  DUB={len(dubs)}")
        print(f"  q-files={len(q_files)}: {', '.join(q_files)}")
        print(f"  litt={has_litt} div={has_div} dub={has_dub}  dups={dups}")
        if quas:
            print("  QUAESTIO headers found in raw:")
            for ln_no, txt in quas:
                print(f"      L{ln_no}: {txt}")
        if dubs:
            print(f"  DUB headers: {[t for _,t in dubs]}")
        if flags:
            print("  *** FLAGS: " + " | ".join(flags))
        print()

if __name__ == "__main__":
    main()
