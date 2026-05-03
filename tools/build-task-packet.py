#!/usr/bin/env python3.11
"""Build a self-contained agent task packet for one chunk.

Input: a chunk file in vol1/ that has a `### Latin` body but no English.
Output: agent-tasks/<chunk-id>.md containing:
  - the Tier-2 prompt
  - glossary excerpt
  - Latin body
  - apparatus draft (if apparatus footnotes detected and apparatus-translate is run)
  - exact target output path

Usage: python3.11 tools/build-task-packet.py vol1/bon-sent-I-d9-a1-q1.md
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TASKS = REPO / "agent-tasks"
TASKS.mkdir(exist_ok=True)

PROMPT = (REPO / "translation-prompt.md").read_text()


def build_packet(chunk_path: Path) -> Path:
    text = chunk_path.read_text()
    chunk_id = chunk_path.stem

    fm_match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    front_matter = fm_match.group(1) if fm_match else ""

    latin_match = re.search(
        r"## Latin\n+(.*?)(?=\n## |\Z)", text, re.DOTALL
    )
    latin_body = latin_match.group(1).strip() if latin_match else ""

    target_rel = f"vol1/{chunk_id}.md"

    packet = f"""# Agent Task: {chunk_id}

## Target output

Write the completed Tier-2 chunk to `{target_rel}`, replacing the existing file.
Preserve the YAML front matter exactly. Replace `[Translation pending]` and
`[Notes pending]` placeholders with translated content. Add `### Apparatus`
section if the Latin body contains footnote markers.

## Front matter (preserve verbatim)

```yaml
{front_matter}
```

## Tier-2 standard

Per `feedback_bonaventure-translation-depth.md`: literal translation, not
paraphrase. Translate ALL scholion and apparatus content fully (do NOT mark
as `[Scholion omitted]` — the legacy prompt's instruction to skip them is
superseded). Preserve every Quaracchi citation in full form.

Output structure (h2 sentinel headings, parser-required):

```
## Latin
<full Latin body, paragraph-for-paragraph>

## English
<full English translation, paragraph-for-paragraph parallel>

## Apparatus
[^1]: **La.** <Latin apparatus text>
    **En.** <English translation>
[^2]: **La.** ...
    **En.** ...

## Notes
<editorial notes, cross-references, doctrinal flags>
```

Inline footnote markers `[^N]` must appear in BOTH the Latin and English
bodies at matching positions. Scholion content lives inside the body blocks
as `### Scholion` subsections.

## Translation prompt (apply this)

{PROMPT}

## Latin body to translate

```
{latin_body}
```
"""

    out = TASKS / f"{chunk_id}.md"
    out.write_text(packet)
    return out


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: build-task-packet.py <chunk.md> [<chunk.md> ...]")
        sys.exit(1)
    for arg in sys.argv[1:]:
        out = build_packet(Path(arg))
        print(f"Wrote: {out.relative_to(REPO)} ({out.stat().st_size} bytes)")
