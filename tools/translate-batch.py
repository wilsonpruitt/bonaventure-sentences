#!/usr/bin/env python3.11
"""Batch-translate Bonaventure chunks via the Anthropic API.

Reads chunk .md files that have Latin bodies but no English translation
(marked [Translation pending]), sends each to Claude for Tier-2 translation,
and writes the English back into the chunk file.

Prerequisites:
    pip3.11 install anthropic
    export ANTHROPIC_API_KEY=sk-ant-...

Usage:
    # Translate all pending chunks in vol2/
    python3.11 tools/translate-batch.py vol2/

    # Translate specific files
    python3.11 tools/translate-batch.py vol1/bon-sent-I-d9-a1-q1.md vol1/bon-sent-I-d9-a1-q2.md

    # Dry run — show what would be translated
    python3.11 tools/translate-batch.py vol2/ --dry-run

    # Control concurrency (default 4, max 6 per acta usage strategy)
    python3.11 tools/translate-batch.py vol2/ --concurrency 2

    # Use a specific model
    python3.11 tools/translate-batch.py vol2/ --model claude-sonnet-4-6

    # Resume after interruption (skips chunks already translated)
    python3.11 tools/translate-batch.py vol2/  # automatic — checks for [Translation pending]

    # Translate only a specific distinction range
    python3.11 tools/translate-batch.py vol2/ --dist 1-10

    # Estimate cost without translating
    python3.11 tools/translate-batch.py vol2/ --estimate
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("ERROR: pip3.11 install anthropic", file=sys.stderr)
    sys.exit(1)

REPO = Path(__file__).resolve().parent.parent

SYSTEM_PROMPT = """You are translating St. Bonaventure's Commentary on the Sentences of Peter Lombard (Quaracchi critical edition, 1882) from Latin to English.

## Critical instructions

- Translate ALL Latin text provided, even if it begins mid-sentence. Do not skip, summarize, or reorganize any content.
- Produce paragraph-for-paragraph parallel translation.
- Do NOT add editorial markup (bold headers, section labels) not present in the Latin.
- Translate scholion sections FULLY and LITERALLY — preserve the Quaracchi editors' voice, every citation, every cross-reference in full form (e.g. "II Sent. d. 3, p. II, a. 2, q. 2", not abbreviated).
- Translate apparatus footnotes literally. Each [^N] marker in the Latin must appear at the matching position in the English.
- Silently correct obvious OCR errors (letter substitutions, broken words). Flag genuinely ambiguous readings.

## Translation style

Formal academic English for theological scholarship. Consistent formulae:
- *Videtur quod...* → "It seems that..."
- *Sed contra* / *Contra* → "On the contrary"
- *Respondeo. Dicendum quod...* → "I respond: It must be said that..."
- *Ad primum / secundum / tertium...* → "To the first / second / third [objection]..."
- *Praeterea* / *Item* → "Likewise"
- *Ergo* / *igitur* → "Therefore"
- *Unde* → "Hence"

## Key terminology (lock these)

- *esse* → being (or "to-be" when context requires)
- *essentia* → essence
- *substantia* → substance
- *suppositum* → supposit
- *forma / materia* → form / matter
- *potentia* → potency or power (context)
- *actus* → act, actuality
- *ratio* → account, ground, formal character (context)
- *intellectus* → intellect
- *voluntas* → will
- *caritas* → charity
- *gratia* → grace
- *exemplar* → exemplar
- *illuminatio* → illumination
- *vestigium* → vestige, trace
- *imago / similitudo* → image / likeness
- *processio* → procession
- *quod est / quo est* → "that which is" / "that by which it is" (preserve Latin in italics on first occurrence)
- *per essentiam* → by essence
- *per participationem* → by participation
- *secundum se* → in itself

## Structural markers to preserve

- `### Articulus N` / `### Article N`
- `### Quaestio N` / `### Question N` (italicize the title)
- `**Contra:**` / `**Sed contra:**`
- `**Respondeo:**`
- `**Ad argumenta...**` / `*Ad N.*`
- `> **Conclusio.**` for conclusions (blockquote)
- `### Scholion` for Quaracchi editorial commentary

## Output format

Return ONLY two sections, no preamble:

### English

[Full paragraph-for-paragraph translation with all structural markers, scholion sections, and [^N] footnote markers preserved at matching positions]

### Notes

[5-10 bullet points: ambiguous passages, key translation decisions, doctrinal flags]"""

# Rough token estimates (Latin words → input tokens, English words → output tokens)
TOKENS_PER_LATIN_WORD = 2.5  # Latin with diacritics/ligatures
TOKENS_PER_ENGLISH_WORD = 1.3
SYSTEM_PROMPT_TOKENS = len(SYSTEM_PROMPT.split()) * 1.3  # ~1500 tokens, cached


def extract_latin(text: str) -> str | None:
    m = re.search(
        r"## Latin\n+(.*?)(?=\n## (?:English|Apparatus|Notes|Scholion|---))",
        text, re.DOTALL,
    )
    if m:
        body = m.group(1).strip()
        if body and body != "[Translation pending]":
            return body
    # Fallback: everything after ## Latin until end
    m = re.search(r"## Latin\n+(.*)", text, re.DOTALL)
    if m:
        body = m.group(1).strip()
        if body and body != "[Translation pending]":
            return body
    return None


def is_pending(text: str) -> bool:
    return "[Translation pending]" in text


def extract_dist(text: str) -> int | None:
    m = re.search(r"distinctio:\s*(\d+)", text)
    return int(m.group(1)) if m else None


def estimate_cost(latin_words: int, model: str) -> dict:
    input_tokens = int(SYSTEM_PROMPT_TOKENS + latin_words * TOKENS_PER_LATIN_WORD)
    output_tokens = int(latin_words * 1.2 * TOKENS_PER_ENGLISH_WORD)  # ~1.2x expansion

    # Pricing per 1M tokens (as of 2026-04)
    prices = {
        "claude-sonnet-4-6": {"input": 3.0, "output": 15.0, "cache_read": 0.30},
        "claude-opus-4-6": {"input": 15.0, "output": 75.0, "cache_read": 1.50},
        "claude-haiku-4-5": {"input": 0.80, "output": 4.0, "cache_read": 0.08},
    }
    p = prices.get(model, prices["claude-sonnet-4-6"])

    # System prompt is cached after first call
    cached_input = SYSTEM_PROMPT_TOKENS
    uncached_input = input_tokens - cached_input

    cost = (
        (cached_input / 1_000_000) * p["cache_read"]
        + (uncached_input / 1_000_000) * p["input"]
        + (output_tokens / 1_000_000) * p["output"]
    )
    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "cost_usd": cost,
    }


def find_chunks(paths: list[str], dist_range: tuple[int, int] | None) -> list[Path]:
    chunks = []
    for p in paths:
        path = REPO / p
        if path.is_dir():
            for f in sorted(path.glob("bon-sent-*.md")):
                chunks.append(f)
        elif path.is_file():
            chunks.append(path)
        else:
            print(f"WARNING: {p} not found", file=sys.stderr)

    # Filter to pending only
    pending = []
    for f in chunks:
        text = f.read_text()
        if not is_pending(text):
            continue
        if extract_latin(text) is None:
            continue
        if dist_range:
            d = extract_dist(text)
            if d is None or not (dist_range[0] <= d <= dist_range[1]):
                continue
        pending.append(f)

    return pending


async def translate_chunk(
    client: anthropic.AsyncAnthropic,
    chunk_path: Path,
    model: str,
    progress: dict,
) -> dict:
    text = chunk_path.read_text()
    latin = extract_latin(text)
    if not latin:
        return {"file": str(chunk_path), "status": "skip", "reason": "no latin"}

    chunk_id = chunk_path.stem
    latin_words = len(latin.split())

    user_msg = f"""Translate this chunk ({chunk_id}).

## Latin body

{latin}"""

    t0 = time.time()
    try:
        response = await client.messages.create(
            model=model,
            max_tokens=16384,
            system=[{
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }],
            messages=[{"role": "user", "content": user_msg}],
        )
    except anthropic.APIError as e:
        return {"file": str(chunk_path), "status": "error", "error": str(e)}

    elapsed = time.time() - t0
    english_output = response.content[0].text

    # Parse the response: extract ### English and ### Notes sections
    eng_match = re.search(
        r"###?\s*English\s*\n+(.*?)(?=\n###?\s*Notes|\Z)",
        english_output, re.DOTALL,
    )
    notes_match = re.search(
        r"###?\s*Notes\s*\n+(.*)",
        english_output, re.DOTALL,
    )

    english_body = eng_match.group(1).strip() if eng_match else english_output.strip()
    notes_body = notes_match.group(1).strip() if notes_match else ""

    # Write back into the chunk file
    new_text = text.replace("[Translation pending]", english_body)
    if notes_body:
        new_text = new_text.replace("[Notes pending]", notes_body)

    # Update transcription_status
    today = datetime.now().strftime("%Y-%m-%d")
    new_text = re.sub(
        r'transcription_status:.*',
        f'transcription_status: "API-translated {model} {today}"',
        new_text,
    )

    chunk_path.write_text(new_text)

    result = {
        "file": str(chunk_path.relative_to(REPO)),
        "status": "ok",
        "latin_words": latin_words,
        "english_words": len(english_body.split()),
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "cache_read": getattr(response.usage, "cache_read_input_tokens", 0),
        "cache_creation": getattr(response.usage, "cache_creation_input_tokens", 0),
        "elapsed_s": round(elapsed, 1),
    }

    progress["completed"].append(result)
    done = len(progress["completed"])
    total = progress["total"]
    print(f"  [{done}/{total}] {chunk_path.name} — {latin_words}w Latin → {len(english_body.split())}w English ({elapsed:.1f}s)")

    return result


async def run_batch(
    chunks: list[Path],
    model: str,
    concurrency: int,
    progress_path: Path,
):
    client = anthropic.AsyncAnthropic()

    progress = {"total": len(chunks), "completed": [], "model": model}

    sem = asyncio.Semaphore(concurrency)

    async def bounded(chunk):
        async with sem:
            return await translate_chunk(client, chunk, model, progress)

    print(f"\nTranslating {len(chunks)} chunks with {model} (concurrency={concurrency})")
    print(f"Progress log: {progress_path}\n")

    tasks = [bounded(c) for c in chunks]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Handle exceptions
    for i, r in enumerate(results):
        if isinstance(r, Exception):
            progress["completed"].append({
                "file": str(chunks[i].relative_to(REPO)),
                "status": "error",
                "error": str(r),
            })

    # Write progress
    progress_path.write_text(json.dumps(progress, indent=2))

    # Summary
    ok = [r for r in progress["completed"] if isinstance(r, dict) and r.get("status") == "ok"]
    errors = [r for r in progress["completed"] if isinstance(r, dict) and r.get("status") == "error"]
    total_input = sum(r.get("input_tokens", 0) for r in ok)
    total_output = sum(r.get("output_tokens", 0) for r in ok)
    total_cache = sum(r.get("cache_read", 0) for r in ok)

    print(f"\n--- Summary ---")
    print(f"Translated: {len(ok)}/{len(chunks)}")
    if errors:
        print(f"Errors: {len(errors)}")
        for e in errors:
            print(f"  {e['file']}: {e.get('error', 'unknown')}")
    print(f"Total input tokens: {total_input:,} (cache hits: {total_cache:,})")
    print(f"Total output tokens: {total_output:,}")


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("paths", nargs="+", help="Chunk files or directories (e.g. vol2/)")
    ap.add_argument("--model", default="claude-sonnet-4-6", help="Model to use (default: claude-sonnet-4-6)")
    ap.add_argument("--concurrency", type=int, default=4, help="Max parallel requests (default: 4, max recommended: 6)")
    ap.add_argument("--dry-run", action="store_true", help="Show what would be translated")
    ap.add_argument("--estimate", action="store_true", help="Estimate cost without translating")
    ap.add_argument("--dist", help="Distinction range, e.g. 1-10 or 5")
    ap.add_argument("--progress", help="Progress log path (default: <dir>/translate-progress.json)")
    args = ap.parse_args()

    dist_range = None
    if args.dist:
        parts = args.dist.split("-")
        if len(parts) == 1:
            dist_range = (int(parts[0]), int(parts[0]))
        else:
            dist_range = (int(parts[0]), int(parts[1]))

    chunks = find_chunks(args.paths, dist_range)

    if not chunks:
        print("No pending chunks found.")
        return

    print(f"Found {len(chunks)} pending chunks")

    if args.dry_run:
        for c in chunks:
            text = c.read_text()
            latin = extract_latin(text)
            words = len(latin.split()) if latin else 0
            d = extract_dist(text)
            print(f"  d.{d or '?':>2} {c.name} ({words} Latin words)")
        total_words = sum(len(extract_latin(c.read_text()).split()) for c in chunks if extract_latin(c.read_text()))
        print(f"\nTotal: {total_words:,} Latin words")
        return

    if args.estimate:
        total_words = 0
        for c in chunks:
            latin = extract_latin(c.read_text())
            if latin:
                total_words += len(latin.split())
        est = estimate_cost(total_words, args.model)
        print(f"\nEstimate for {len(chunks)} chunks ({total_words:,} Latin words):")
        print(f"  Input tokens:  ~{est['input_tokens']:,}")
        print(f"  Output tokens: ~{est['output_tokens']:,}")
        print(f"  Est. cost:     ~${est['cost_usd']:.2f} ({args.model})")
        print(f"\n  With prompt caching (system prompt cached after 1st call):")
        cached_savings = (SYSTEM_PROMPT_TOKENS * (len(chunks) - 1) / 1_000_000) * 2.7  # ~savings
        print(f"  Cache savings: ~${cached_savings:.2f}")
        print(f"  Net est. cost: ~${max(0, est['cost_usd'] - cached_savings):.2f}")
        return

    if args.concurrency > 6:
        print("WARNING: concurrency > 6 not recommended (rate limits). Capping at 6.")
        args.concurrency = 6

    progress_path = Path(args.progress) if args.progress else (chunks[0].parent / "translate-progress.json")

    asyncio.run(run_batch(chunks, args.model, args.concurrency, progress_path))


if __name__ == "__main__":
    main()
