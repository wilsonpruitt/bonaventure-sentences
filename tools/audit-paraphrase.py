#!/usr/bin/env python3.11
"""Silent-paraphrase audit across Tier-2 chunks d.1-d.40.

For each chunk:
  1. Extract its ## Latin body
  2. Slice raw OCR text by frontmatter line_start/line_end
  3. Tokenize both (lowercase, alpha-only, length>=3)
  4. Compute Jaccard overlap of word sets and length ratio
  5. Flag status-string smells (PDF supplement / first-pass / Tier-1 gap-fill / etc.)

Low Jaccard or extreme length ratio = paraphrase suspect.

Output: markdown report ranked by suspicion score, written to
manual-review/d1-d40-paraphrase-audit.md by default.

Usage:
  python3.11 tools/audit-paraphrase.py                      # full report
  python3.11 tools/audit-paraphrase.py --max-d 25           # subset
  python3.11 tools/audit-paraphrase.py --chunk d3-littera   # single chunk diff dump
"""
from __future__ import annotations
import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VOL1 = REPO / "vol1"
RAW_PT1 = REPO / "raw" / "bonaventure_vol1_raw.txt"
RAW_PT2 = REPO / "raw" / "bonaventure_vol1_pt2_raw.txt"

# Status strings that smell like paraphrase / unfinished work
SMELL_PATTERNS = [
    (re.compile(r"OCR[- ]dropped", re.I),       "OCR-dropped column"),
    (re.compile(r"PDF\s+supplement", re.I),     "PDF supplement"),
    (re.compile(r"supplement(?:ed)?\s+(?:by|from)", re.I), "supplemented from PDF"),
    (re.compile(r"reconstruct", re.I),          "reconstructed"),
    (re.compile(r"first[- ]pass", re.I),        "first-pass (not promoted)"),
    (re.compile(r"Tier[- ]?1\b", re.I),         "Tier-1 status"),
    (re.compile(r"gap[- ]fill", re.I),          "gap-fill"),
    (re.compile(r"auto[- ]?chunked", re.I),     "auto-chunked skeleton"),
    (re.compile(r"pending\s+final\s+verification", re.I), "pending verification"),
    (re.compile(r"OCR\s+(?:gap|jump|drop)", re.I), "OCR gap/jump"),
    (re.compile(r"vision\s+(?:re-)?OCR", re.I), "vision-OCR origin"),
    (re.compile(r"placeholder", re.I),          "placeholder"),
]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LATIN_BLOCK_RE = re.compile(
    r"^## Latin\s*\n(.*?)(?=^## (?:English|Apparatus|Notes|Scholion)|\Z)",
    re.DOTALL | re.MULTILINE,
)
WORD_RE = re.compile(r"[A-Za-zÀ-ÿ]{3,}")
# pt2 OCR mangles word interiors heavily ("praedestinalio" for "praedestinatio").
# Token by 5-char prefix of words length >= 5 — same word stems survive most
# OCR-garble patterns and we drop short function words that add no signal.
PREFIX_LEN = 5
MIN_WORD_LEN = 5


@dataclass
class ChunkAudit:
    path: Path
    chunk_id: str
    distinctio: int
    chunk_type: str
    line_start: int | None
    line_end: int | None
    status: str
    smells: list[str]
    chunk_words: int
    raw_words: int
    jaccard: float | None
    length_ratio: float | None
    score: float
    notes: list[str]


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    out: dict = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        v = v.strip().strip('"').strip("'")
        out[k.strip()] = v
    return out


def extract_latin(text: str) -> str:
    m = LATIN_BLOCK_RE.search(text)
    if not m:
        return ""
    body = m.group(1)
    # Strip <!-- page N --> comments, [^N] markers, italic *...*, bold **...**, ###/####
    body = re.sub(r"<!--.*?-->", " ", body, flags=re.DOTALL)
    body = re.sub(r"\[\^[^\]]+\]", " ", body)
    body = re.sub(r"^#{1,6}\s+.*$", " ", body, flags=re.MULTILINE)
    return body


def tokenize(s: str) -> set[str]:
    """Token-set of 5-char prefixes of words length >= 5, lowercased.

    This is OCR-garble-tolerant: 'praedestinatio' and 'praedestinalio' both
    yield 'praed', so word-stem overlap survives the typical pt2 OCR mangle.
    Short function words are dropped — they add no paraphrase signal.
    """
    return {
        w.lower()[:PREFIX_LEN]
        for w in WORD_RE.findall(s)
        if len(w) >= MIN_WORD_LEN
    }


def raw_slice(distinctio: int, ls: int, le: int) -> str:
    # Pt2 starts at d.24 per memory; some d.24/d.25 content also lives in pt1.
    # Heuristic: if distinctio >= 24 prefer pt2; let pt1 fallback if line range
    # doesn't fit pt2.
    pt2 = RAW_PT2.read_text(encoding="utf-8", errors="replace").splitlines()
    pt1 = RAW_PT1.read_text(encoding="utf-8", errors="replace").splitlines()

    def take(lines: list[str]) -> str:
        if ls is None or le is None or ls < 1 or le > len(lines) + 5:
            return ""
        end = min(le, len(lines))
        return "\n".join(lines[ls - 1 : end])

    if distinctio >= 24:
        s = take(pt2)
        if s:
            return s
        return take(pt1)
    s = take(pt1)
    if s:
        return s
    return take(pt2)


def audit_chunk(path: Path, raw_pt1_lines: int, raw_pt2_lines: int) -> ChunkAudit | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)
    if not fm:
        return None
    chunk_id = fm.get("id", path.stem)
    try:
        distinctio = int(fm.get("distinctio", "0"))
    except ValueError:
        distinctio = 0
    chunk_type = fm.get("type", "")
    status = fm.get("transcription_status", "")

    def to_int(k: str) -> int | None:
        v = fm.get(k, "")
        try:
            return int(v)
        except (ValueError, TypeError):
            return None

    ls = to_int("line_start")
    le = to_int("line_end")

    smells = [label for pat, label in SMELL_PATTERNS if pat.search(status)]

    notes: list[str] = []
    chunk_latin = extract_latin(text)
    chunk_tokens = tokenize(chunk_latin)
    chunk_words = len(chunk_tokens)

    raw_words = 0
    jaccard: float | None = None
    length_ratio: float | None = None

    if ls is None or le is None:
        notes.append("no line_start/line_end frontmatter — content audit skipped")
    elif not chunk_latin.strip():
        notes.append("no ## Latin block found — chunk malformed")
    else:
        raw_text = raw_slice(distinctio, ls, le)
        if not raw_text:
            notes.append(f"raw slice empty (range {ls}-{le} out-of-bounds)")
        else:
            raw_tokens = tokenize(raw_text)
            raw_words = len(raw_tokens)
            if raw_words and chunk_words:
                inter = len(chunk_tokens & raw_tokens)
                union = len(chunk_tokens | raw_tokens)
                jaccard = inter / union if union else 0.0
                length_ratio = chunk_words / raw_words

    # Suspicion score:
    #   smells:    +2 per smell
    #   jaccard:   +6 if <0.30, +3 if <0.50, +1 if <0.65
    #   length:    +3 if ratio <0.40 or >2.5
    #   no bounds: +1 (can't audit, mild risk)
    score = 2.0 * len(smells)
    if jaccard is not None:
        if jaccard < 0.30:
            score += 6
        elif jaccard < 0.50:
            score += 3
        elif jaccard < 0.65:
            score += 1
    if length_ratio is not None and (length_ratio < 0.40 or length_ratio > 2.5):
        score += 3
    if ls is None or le is None:
        score += 1

    return ChunkAudit(
        path=path,
        chunk_id=chunk_id,
        distinctio=distinctio,
        chunk_type=chunk_type,
        line_start=ls,
        line_end=le,
        status=status[:120],
        smells=smells,
        chunk_words=chunk_words,
        raw_words=raw_words,
        jaccard=jaccard,
        length_ratio=length_ratio,
        score=score,
        notes=notes,
    )


def render_report(audits: list[ChunkAudit], max_d: int) -> str:
    audits.sort(key=lambda a: (-a.score, a.distinctio, a.chunk_id))

    lines = []
    lines.append(f"# Silent-Paraphrase Audit — d.1–d.{max_d}")
    lines.append("")
    lines.append(f"Generated by `tools/audit-paraphrase.py`. Total chunks audited: **{len(audits)}**.")
    lines.append("")
    lines.append("**Score**: 2/smell + 6 (J<0.30) | 3 (J<0.50) | 1 (J<0.65) + 3 if length-ratio extreme + 1 if no bounds.")
    lines.append("**Jaccard**: word-set overlap between chunk `## Latin` body and raw-OCR slice. Low = paraphrase suspect.")
    lines.append("**LenR**: chunk-words / raw-words. Far from 1.0 = chunk diverges in size.")
    lines.append("")

    # Buckets
    buckets = {
        "CRITICAL (score >= 8)": [a for a in audits if a.score >= 8],
        "HIGH (4 <= score < 8)": [a for a in audits if 4 <= a.score < 8],
        "MEDIUM (2 <= score < 4)": [a for a in audits if 2 <= a.score < 4],
        "OK (score < 2)": [a for a in audits if a.score < 2],
    }
    for name, items in buckets.items():
        lines.append(f"## {name} — {len(items)} chunks")
        lines.append("")
        if not items:
            lines.append("(none)")
            lines.append("")
            continue
        lines.append("| Score | Chunk | Type | J | LenR | Smells | Notes |")
        lines.append("|---|---|---|---|---|---|---|")
        for a in items:
            j = f"{a.jaccard:.2f}" if a.jaccard is not None else "—"
            r = f"{a.length_ratio:.2f}" if a.length_ratio is not None else "—"
            smells = ", ".join(a.smells) or "—"
            notes = "; ".join(a.notes) or "—"
            lines.append(
                f"| {a.score:.0f} | `{a.chunk_id}` | {a.chunk_type} | {j} | {r} | {smells} | {notes} |"
            )
        lines.append("")

    # Per-distinction summary
    lines.append("## Per-distinction summary")
    lines.append("")
    lines.append("| d. | chunks | critical | high | medium | ok | mean J |")
    lines.append("|---|---|---|---|---|---|---|")
    by_d: dict[int, list[ChunkAudit]] = {}
    for a in audits:
        by_d.setdefault(a.distinctio, []).append(a)
    for d in sorted(by_d):
        chunks = by_d[d]
        crit = sum(1 for a in chunks if a.score >= 8)
        hi = sum(1 for a in chunks if 4 <= a.score < 8)
        md = sum(1 for a in chunks if 2 <= a.score < 4)
        ok = sum(1 for a in chunks if a.score < 2)
        js = [a.jaccard for a in chunks if a.jaccard is not None]
        mj = sum(js) / len(js) if js else None
        mj_s = f"{mj:.2f}" if mj is not None else "—"
        lines.append(f"| {d} | {len(chunks)} | {crit} | {hi} | {md} | {ok} | {mj_s} |")
    lines.append("")

    return "\n".join(lines)


def diff_dump(path: Path):
    """Single-chunk debug dump: print chunk Latin alongside raw slice."""
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)
    distinctio = int(fm.get("distinctio", "0"))
    ls = int(fm.get("line_start", "0"))
    le = int(fm.get("line_end", "0"))
    print(f"# {path.name}")
    print(f"distinctio={distinctio} line_start={ls} line_end={le}")
    print(f"status: {fm.get('transcription_status', '')[:200]}")
    print()
    print("## Chunk Latin (cleaned)")
    print(extract_latin(text)[:2000])
    print()
    print("## Raw OCR slice")
    print(raw_slice(distinctio, ls, le)[:2000])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-d", type=int, default=40)
    ap.add_argument("--min-d", type=int, default=1)
    ap.add_argument("--chunk", help="single-chunk diff dump (e.g. d3-littera)")
    ap.add_argument("--out", default="manual-review/d1-d40-paraphrase-audit.md")
    args = ap.parse_args()

    if args.chunk:
        matches = list(VOL1.glob(f"bon-sent-I-{args.chunk}.md"))
        if not matches:
            matches = list(VOL1.glob(f"bon-sent-I-*{args.chunk}*.md"))
        if not matches:
            sys.exit(f"no chunk match for {args.chunk}")
        for p in matches:
            diff_dump(p)
        return

    audits: list[ChunkAudit] = []
    raw_pt1_n = sum(1 for _ in RAW_PT1.open())
    raw_pt2_n = sum(1 for _ in RAW_PT2.open())
    for p in sorted(VOL1.glob("bon-sent-I-d*.md")):
        # filter by distinctio
        m = re.match(r"bon-sent-I-d(\d+)-", p.name)
        if not m:
            continue
        d = int(m.group(1))
        if not (args.min_d <= d <= args.max_d):
            continue
        a = audit_chunk(p, raw_pt1_n, raw_pt2_n)
        if a is not None:
            audits.append(a)

    report = render_report(audits, args.max_d)
    out_path = REPO / args.out
    out_path.write_text(report, encoding="utf-8")
    print(f"wrote {out_path} — {len(audits)} chunks audited")
    crit = sum(1 for a in audits if a.score >= 8)
    hi = sum(1 for a in audits if 4 <= a.score < 8)
    print(f"  critical: {crit}  high: {hi}")


if __name__ == "__main__":
    main()
