#!/usr/bin/env python3
"""
Chunk Bonaventure Vol I (In I Sententiarum, distributio 1) into individual files.

Strategy:
- Lines 1 to first DIST. header: Prolegomena → bon-sent-I-proleg.md
- Lines after: Parse DIST/QUAEST headers to create per-quaestio chunks
- Each DUBIA section gets its own file: bon-sent-I-d{N}-dubia.md

OCR normalization applied to header lines before parsing.
"""

import re
from pathlib import Path

RAW_FILE = Path(__file__).parent / "raw" / "bonaventure_vol1_raw.txt"
OUT_DIR = Path(__file__).parent / "vol1"
OUT_DIR.mkdir(exist_ok=True)

with open(RAW_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

TOTAL_LINES = len(lines)


def normalize_header(line: str) -> str:
    """Aggressively normalize OCR artifacts in header lines."""
    s = line.strip()
    # Collapse multiple spaces
    s = re.sub(r"\s+", " ", s)
    # Fix ART variants: \RT., .VRT., AKT., .\RT., etc.
    s = re.sub(r"[\\.]?[AV\\]?RT\.", "ART.", s)
    s = re.sub(r"AKT\.", "ART.", s)
    # Fix QUAEST variants: QU.\EST., QU\EST., QLAEST., OUAEST., QIIAESr., QH.VESr., QL\EST., etc.
    s = re.sub(r"Q[UHLI]*[\\.]?[AVLE]*E?S[Tr]*\.", "QUAEST.", s, flags=re.IGNORECASE)
    s = re.sub(r"QU?[\\.]EST\.", "QUAEST.", s)
    s = re.sub(r"QL?\\EST\.", "QUAEST.", s)
    s = re.sub(r"QU\\\.EST\.", "QUAEST.", s)  # QU.\EST.
    s = re.sub(r"QUAIiST\.", "QUAEST.", s)
    # Catch any remaining QU + noise + EST pattern
    s = re.sub(r"QU?\S?\\?\.?EST\.", "QUAEST.", s)
    # Normalize OUAEST
    s = s.replace("OUAEST.", "QUAEST.")
    # Fix DUBIA variants: DUBI.\., DUB1.\., DUBL\., DUBI\., DUBIA.., etc.
    s = re.sub(r"DUB[I1][\\.]?[A\\.]?\.*", "DUBIA.", s)
    s = re.sub(r"DUBL\\?\.", "DUBIA.", s)
    # Fix UNICUS variants: UNICDS, UMCUS, INICUS, IJNICUS, UiMCUS, UiMCLIS, miCUS, UNICllS
    s = re.sub(r"U?[IiMm]?[NnMm]?[IiCc][CcKk]?[UuLl][SsIi]", "UNICUS", s)
    s = s.replace("UNICllS", "UNICUS")
    s = s.replace("UNICLIS", "UNICUS")
    s = s.replace("UNICUSS", "UNICUS")
    # Fix missing period after garbled dist numbers: "XVIII ART" → "XVIII. ART"
    s = re.sub(r"(DIST\. [IVXL]+) (ART|P\.)", r"\1. \2", s)
    # "XVII P." missing period: "DIST. XVII P." → "DIST. XVII. P."
    s = re.sub(r"(DIST\. [IVXL]+) (P\.)", r"\1. \2", s)
    # Fix DIVISIO TEXTUS variants: TEXTIIS, TEXTLIS
    s = re.sub(r"TEXT[LIUW]+S", "TEXTUS", s)
    # Fix P. variants: 1'. for P., }'. for P., R for P.
    s = re.sub(r" [1}\']['\.]\.?\s+", " P. ", s)
    s = re.sub(r" R ([IVX]+)\.", r" P. \1.", s)
    # Fix "XVd/" → "XVII" etc. - garbled dist numbers
    s = s.replace("XVd/", "XVII")
    s = s.replace("XV[l", "XVII")
    s = s.replace("XV[[", "XVII")
    s = s.replace("XVllL", "XVIII")
    s = s.replace("XVlli", "XVIII")
    s = s.replace("XV[I", "XVII")
    # Normalize Roman numerals - fix common OCR l/I/1 confusion
    # Do this token by token after the period
    return s


def roman_to_int(s: str) -> int:
    """Convert Roman numeral string to integer."""
    s = s.strip().rstrip(".")
    if s == "UNICA" or s == "UNICUS":
        return 1
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
    total = 0
    for i, c in enumerate(s):
        if c not in vals:
            return 0
        if i + 1 < len(s) and vals.get(c, 0) < vals.get(s[i + 1], 0):
            total -= vals[c]
        else:
            total += vals[c]
    return total


# Map of known OCR-garbled Roman numerals
ROMAN_FIXES = {}
# Populate with common OCR confusions
for clean, garbled_list in {
    "I": ["l", "1"],
    "II": ["H", "fl", "U", "n", "ll", "tl", "Jl", "It", "11"],
    "III": ["lU", "m", "lll", "Hl", "Hf", "tll", "IH", "Hi", "I!I", "lH", "III"],
    "IV": ["lV", "1V"],
    "V": [],
    "VI": ["VJ", "Vl"],
    "VII": ["Vll", "VII", "V(["],
    "VIII": ["Vlll", "VIU", "Vm", "Vin", "VIH", "Vill", "VIll", "VIU"],
    "IX": ["lX"],
    "X": [],
    "XI": ["Xl", "X1"],
    "XII": ["Xll", "X11"],
    "XIII": ["Xlll", "Xni", "XIll", "X1ll", "XI]"],
    "XIV": ["XlV"],
    "XV": ["xv"],
    "XVI": ["XVl"],
    "XVII": ["XVll", "XVn", "XVlI", "XV[I", "XV[l", "XVd/", "XVli"],
    "XVIII": ["XVllL", "XVlIi", "XVIU", "XVlli", "XVlll"],
    "XIX": ["XlX"],
    "XX": [],
    "XXI": ["XXl"],
    "XXII": ["XXll", "XXII"],
    "XXIII": ["XXIIL", "XXin", "XXlIf", "XXIll"],
}.items():
    ROMAN_FIXES[clean] = clean
    for g in garbled_list:
        ROMAN_FIXES[g] = clean


def clean_roman(raw: str) -> str:
    """Normalize an OCR'd Roman numeral."""
    raw = raw.strip().rstrip(".")
    if raw in ROMAN_FIXES:
        return ROMAN_FIXES[raw]
    if re.match(r"^[IVXLC]+$", raw):
        return raw
    # Try replacing common l->I, 1->I substitutions
    attempt = raw.replace("l", "I").replace("1", "I")
    if re.match(r"^[IVXLC]+$", attempt):
        return attempt
    return raw


# Pattern for normalized DIST. headers
DIST_PAT = re.compile(
    r"^DIST\.\s+"
    r"(\S+)\.\s+"                    # dist number
    r"(?:P\.\s+(\S+)\.\s+)?"        # optional pars
    r"("
        r"ART\.\s+\S+\s+QUAEST\.\s+\S+"    # art + quaest
        r"|QUAEST\.\s+\S+"                   # quaest without art
        r"|ART\.\s+\S+\s+QUAEST\.\s*$"     # truncated quaest (running header, no number)
        r"|DUBIA\."                           # dubia
        r"|DIVISIO\s+TEXTUS"                  # divisio
    r")"
)


def parse_header(normalized: str):
    """Parse a normalized DIST. header line."""
    m = DIST_PAT.match(normalized)
    if not m:
        return None

    dist_raw = m.group(1)
    pars_raw = m.group(2)
    body = m.group(3)

    dist = clean_roman(dist_raw)
    dist_n = roman_to_int(dist)
    if dist_n == 0:
        return None  # couldn't parse distinctio number

    pars = clean_roman(pars_raw) if pars_raw else None

    if "DUBIA" in body:
        return {"type": "dubia", "dist": dist, "dist_n": dist_n, "pars": pars}
    elif "DIVISIO" in body:
        return {"type": "divisio", "dist": dist, "dist_n": dist_n, "pars": pars}
    else:
        # Extract quaestio number (last token)
        tokens = body.split()
        q_raw = tokens[-1]
        # If the line ends with "QUAEST." and no number, it's a truncated running header — skip
        if q_raw == "QUAEST.":
            return None
        q = clean_roman(q_raw)
        # Extract article info
        art_raw = None
        if "ART." in body:
            art_idx = tokens.index("ART.")
            if art_idx + 1 < len(tokens):
                art_raw = tokens[art_idx + 1]
        art = clean_roman(art_raw) if art_raw else None
        return {
            "type": "quaestio", "dist": dist, "dist_n": dist_n,
            "pars": pars, "art": art, "quaest": q,
        }


def make_chunk_id(meta: dict) -> str:
    dist_n = meta["dist_n"]
    pars_suffix = f"-p{roman_to_int(meta['pars'])}" if meta.get("pars") else ""
    if meta["type"] == "dubia":
        return f"bon-sent-I-d{dist_n}{pars_suffix}-dubia"
    elif meta["type"] == "divisio":
        pars_suffix2 = f"-p{roman_to_int(meta['pars'])}" if meta.get("pars") else ""
        return f"bon-sent-I-d{dist_n}{pars_suffix2}-divisio"
    else:
        q_int = roman_to_int(meta["quaest"]) if meta.get("quaest") else 0
        art_int = roman_to_int(meta["art"]) if meta.get("art") else None
        art_suffix = f"-a{art_int}" if art_int and art_int > 0 else ""
        return f"bon-sent-I-d{dist_n}{pars_suffix}{art_suffix}-q{q_int}"


def make_title(meta: dict) -> str:
    dist_n = meta["dist_n"]
    pars = f", p. {roman_to_int(meta['pars'])}" if meta.get("pars") else ""
    if meta["type"] == "dubia":
        return f"I Sent., d. {dist_n}{pars}, dubia"
    elif meta["type"] == "divisio":
        return f"I Sent., d. {dist_n}{pars}, divisio textus"
    else:
        q_int = roman_to_int(meta["quaest"]) if meta.get("quaest") else 0
        art_int = roman_to_int(meta["art"]) if meta.get("art") else None
        art_str = f", a. {art_int}" if art_int and art_int > 0 else ""
        return f"I Sent., d. {dist_n}{pars}{art_str}, q. {q_int}"


# --- Scan for headers ---
headers = []
for i, line in enumerate(lines):
    stripped = line.strip()
    if not stripped.startswith("DIST."):
        continue
    normalized = normalize_header(stripped)
    parsed = parse_header(normalized)
    if parsed:
        headers.append((i, parsed, normalized))

print(f"Total lines: {TOTAL_LINES}")
print(f"Raw headers found: {len(headers)}")

# Show lines starting with DIST. that DIDN'T parse, for debugging
unparsed = []
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith("DIST.") and len(stripped) > 10:
        normalized = normalize_header(stripped)
        parsed = parse_header(normalized)
        if not parsed:
            unparsed.append((i + 1, stripped[:80], normalized[:80]))

if unparsed:
    print(f"\nUnparsed DIST. lines ({len(unparsed)}):")
    for ln, raw, norm in unparsed[:20]:
        print(f"  L{ln}: {raw}")
        print(f"    → {norm}")

# --- Dedup running headers ---
# The Quaracchi edition has running headers at the top of each page that repeat
# the current section. We want the SECOND occurrence (the actual content start).
deduped = []
for idx, (line_no, meta, norm) in enumerate(headers):
    chunk_id = make_chunk_id(meta)
    if idx + 1 < len(headers):
        next_id = make_chunk_id(headers[idx + 1][1])
        next_line = headers[idx + 1][0]
        if next_id == chunk_id and (next_line - line_no) < 350:
            continue
    deduped.append((line_no, meta))

headers_final = deduped
print(f"Headers after dedup: {len(headers_final)}")

# --- Write prolegomena ---
# Find the first DISTINCTIO header as the true start of commentary
first_dist_line = None
for i, line in enumerate(lines):
    if line.strip().startswith("DISTINCTIO"):
        first_dist_line = i
        break

proleg_end = first_dist_line if first_dist_line else (headers_final[0][0] if headers_final else TOTAL_LINES)
proleg_text = "".join(lines[:proleg_end])
proleg_path = OUT_DIR / "bon-sent-I-proleg.md"
with open(proleg_path, "w", encoding="utf-8") as f:
    f.write("---\n")
    f.write('id: "bon-sent-I-proleg"\n')
    f.write("volume: 1\n")
    f.write("book: 1\n")
    f.write('title: "Prolegomena to Book I of the Sentences"\n')
    f.write(f"line_start: 1\n")
    f.write(f"line_end: {proleg_end}\n")
    f.write(f"word_count_latin: {len(proleg_text.split())}\n")
    f.write("---\n\n")
    f.write("# I Sent., Prolegomena\n\n")
    f.write("### Latin\n\n")
    f.write(proleg_text)

print(f"\nWrote prolegomena: lines 1–{proleg_end}")

# --- Write chunks ---
chunks_written = 0
seen_ids = {}

for idx, (line_no, meta) in enumerate(headers_final):
    if idx + 1 < len(headers_final):
        end_line = headers_final[idx + 1][0]
    else:
        # Find where the actual content ends (before library card)
        end_line = TOTAL_LINES
        for j in range(TOTAL_LINES - 1, max(line_no, TOTAL_LINES - 200), -1):
            if lines[j].strip().startswith("Boston  College"):
                end_line = j - 5
                break

    chunk_id = make_chunk_id(meta)
    if chunk_id in seen_ids:
        seen_ids[chunk_id] += 1
        chunk_id = f"{chunk_id}-v{seen_ids[chunk_id]}"
    else:
        seen_ids[chunk_id] = 1

    title = make_title(meta)
    chunk_text = "".join(lines[line_no:end_line])
    word_count = len(chunk_text.split())

    filepath = OUT_DIR / f"{chunk_id}.md"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f'id: "{chunk_id}"\n')
        f.write(f"volume: 1\n")
        f.write(f"book: 1\n")
        f.write(f"distinctio: {meta['dist_n']}\n")
        if meta.get("pars"):
            f.write(f"pars: {roman_to_int(meta['pars'])}\n")
        if meta["type"] == "quaestio":
            if meta.get("art"):
                f.write(f"articulus: {roman_to_int(meta['art'])}\n")
            f.write(f"quaestio: {roman_to_int(meta['quaest'])}\n")
        f.write(f"type: {meta['type']}\n")
        f.write(f'title: "{title}"\n')
        f.write(f"line_start: {line_no + 1}\n")
        f.write(f"line_end: {end_line}\n")
        f.write(f"word_count_latin: {word_count}\n")
        f.write("---\n\n")
        f.write(f"# {title}\n\n")
        f.write("### Latin\n\n")
        f.write(chunk_text)
        f.write("\n\n### English\n\n[Translation pending]\n")
        f.write("\n### Notes\n\n[Notes pending]\n")

    chunks_written += 1

print(f"Chunks written: {chunks_written}")

# Summary
dist_counts = {}
for _, meta in headers_final:
    d = meta["dist_n"]
    t = meta["type"]
    key = f"d{d}"
    if key not in dist_counts:
        dist_counts[key] = {"q": 0, "dubia": 0, "divisio": 0, "n": d}
    dist_counts[key][t[0]] = dist_counts[key].get(t[0], 0) + 1

print(f"\nDistinctiones covered: {len(set(m['dist_n'] for _, m in headers_final))}")
print("\nPer-distinctio breakdown:")
for key in sorted(dist_counts.keys(), key=lambda k: dist_counts[k]["n"]):
    info = dist_counts[key]
    parts = []
    if info.get("q", 0): parts.append(f"{info['q']}q")
    if info.get("d", 0): parts.append(f"{info['d']} dubia")
    if info.get("divisio", 0): parts.append("divisio")
    print(f"  Dist. {info['n']:>3}: {', '.join(parts)}")
