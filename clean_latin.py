#!/usr/bin/env python3
"""
Clean Latin OCR text from Quaracchi edition of Bonaventure's Sentences.

Strategy (per user request):
1. Strip critical apparatus (footnotes) — scattered throughout, not just at end
2. Strip Scholion sections (Quaracchi editors' notes)
3. Strip marginalia (short editorial labels in the Quaracchi margin)
4. Fix common OCR character substitutions
5. Normalize spacing and rejoin hyphenated words
6. Remove page headers and stray page numbers
"""

import re
import sys
import os
import glob
import argparse
from pathlib import Path


# --- OCR character fixes ---

NAME_FIXES = {
    'Tliom.': 'Thom.',
    'Ricliard.': 'Richard.',
    'Ililarius': 'Hilarius',
    'Ililario': 'Hilario',
    '/Egid.': 'Aegid.',
    'Pctr.': 'Petr.',
}

WORD_FIXES = [
    # li -> h confusions
    (r'\bliic\b', 'hic'),
    (r'\blioc\b', 'hoc'),
    (r'\bliabet\b', 'habet'),
    (r'\bliabent\b', 'habent'),
    (r'\bliabere\b', 'habere'),
    (r'\bliabens\b', 'habens'),
    (r'\bliomo\b', 'homo'),
    (r'\bliominem\b', 'hominem'),
    (r'\bliominis\b', 'hominis'),
    (r'\bliuius\b', 'huius'),
    (r'\bliunc\b', 'hunc'),
    (r'\blianc\b', 'hanc'),
    (r'\bliae\b', 'hae'),
    (r'\bliaec\b', 'haec'),
    (r'\bliis\b', 'his'),
    (r'\blii\b', 'hii'),

    # U -> li confusions
    (r'universaU', 'universali'),
    (r'nuUo', 'nullo'),
    (r'nuUa', 'nulla'),
    (r'iUa\b', 'illa'),
    (r'iUud\b', 'illud'),
    (r'iUi\b', 'illi'),
    (r'iUis\b', 'illis'),

    # Common single-char confusions
    (r'\bheatitud', 'beatitud'),
    (r'\bhonitas\b', 'bonitas'),
    (r'\bhonitatis\b', 'bonitatis'),
    (r'\bhonum\b', 'bonum'),
    (r'\bhoni\b', 'boni'),
    (r'\butruiB\b', 'utrum'),
    (r'\bItetn\b', 'Item'),
    (r'\bperfeclio\b', 'perfectio'),
    (r'\bsimihter\b', 'similiter'),
    (r'\bsimihs\b', 'similis'),
    (r'\bahqua\b', 'aliqua'),
    (r'\bahquo\b', 'aliquo'),
    (r'\bahquod\b', 'aliquod'),
    (r'\bahquid\b', 'aliquid'),
    (r'\bahquis\b', 'aliquis'),
    (r'\bsubslantialis\b', 'substantialis'),
    (r'\bsubslantia\b', 'substantia'),
    (r'\bdeitalem\b', 'deitatem'),
    (r'\bterrainus\b', 'terminus'),
    (r'\bsimphciter\b', 'simpliciter'),
    (r'\bcontiiigen', 'contingen'),
    (r'\bneeessit', 'necessit'),
    (r'\bFihum\b', 'Filium'),
    (r'\bFihi\b', 'Filii'),
    (r'\bFiho\b', 'Filio'),
    (r'\bsuperllua\b', 'superflua'),
    (r'\bMetiiph\b', 'Metaph'),
    (r'\bPeriiierm\b', 'Periherm'),
    (r'\bsir\b', 'sit'),
    (r'\bdicaLur\b', 'dicatur'),
    (r'\bafTirma', 'affirma'),
    (r'\bquotl\b', 'quod'),
    (r'\bralione\b', 'ratione'),
    (r'\bcontradi-\n\s*clione\b', 'contradictione'),
    (r'\bilh\b', 'illi'),
]

# --- Page headers / footers ---
PAGE_HEADER_PATTERNS = [
    r'^SENTENTL?[AVJI]?RUM\s+LIB\.\s+[IVX]+\.?\s*$',
    r'^S\.\s+BONAV',
]

# --- Apparatus / footnote detection ---
# Apparatus lines are footnotes from the Quaracchi critical edition.
# They appear after body text on each page, then body text resumes.

# Sigla that indicate apparatus content
APPARATUS_SIGLA = re.compile(
    r'(?:Vat|Cod|Codd|codd|mss|edd?\.|ed\.\s*[1-9]|'
    r'Aristot|Seneca|Dionys|Cfr|cfr|Praeter|Restituimus|'
    r'Maior\s+pars|Multi\s+codd|Aliqu[ai]\s+codd|'
    r'Paulo\s+(?:post|ante|infra)|Mox\s+(?:Vat|post|cod)|'
    r'In\s+(?:fine|principio)\s+argum|'
    r'Hanc\s+[lJ]ectionem|'
    r'S\.\s+Bonav\.|'
    r'Scot\.|Alex\.\s+Hal|'
    r'Richard\.\s+a\s+Med|'
    r'B\.\s+Albert|'
    r'Petr\.\s+a\s+Tar|'
    r'Henr\.\s+Gand|'
    r'Durand\.|Biel\b|'
    r'Ilenr\.\s+Gand|'
    r'Hexaem\.\s+Serm)'
)


def is_apparatus_line(line):
    """Detect a line that belongs to the critical apparatus."""
    stripped = line.strip()
    if not stripped:
        return False

    # Lines starting with footnote markers: digit(s), ^, ', ", >, «, *
    # followed by apparatus sigla
    if re.match(r"""^[\d\^'"\*>«■]+\s""", stripped):
        # Check if it contains apparatus-like content
        if APPARATUS_SIGLA.search(stripped):
            return True
        # Also catch short footnote number references like "3  Aristot."
        if re.match(r'^\d\s{2,}', stripped):
            return True

    # Continuation lines of apparatus (contain manuscript sigla heavily)
    # These are lines that are clearly part of a footnote block
    sigla_count = len(re.findall(
        r'\b(?:Vat|Cod|codd|mss|edd?\.\s*[1-9]|loco|pro\b|omittit|addit|ponit|'
        r'substituimus|habent|habentur|exhibet|desiderantur|deest)\b',
        stripped
    ))
    if sigla_count >= 2:
        return True

    return False


def is_scholion_line(line):
    """Detect SCHOLION section headers."""
    stripped = line.strip()
    return stripped == 'SCHOLION.' or stripped == 'SCHOLION'


def classify_lines(lines):
    """Classify each line as body, apparatus, scholion, marginalia, page_header, or page_number.

    Returns list of (classification, line) tuples.
    """
    result = []
    in_apparatus = False
    in_scholion = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Empty lines: context-dependent
        if not stripped:
            result.append(('blank', line))
            continue

        # Page numbers (standalone digits)
        if re.match(r'^\d{1,4}\s*$', stripped):
            result.append(('page_number', line))
            continue

        # Page headers
        is_header = False
        for pat in PAGE_HEADER_PATTERNS:
            if re.match(pat, stripped, re.IGNORECASE):
                is_header = True
                break
        if is_header:
            result.append(('page_header', line))
            continue

        # Scholion start
        if is_scholion_line(line):
            in_scholion = True
            in_apparatus = False
            result.append(('scholion', line))
            continue

        # If in scholion, check if we've returned to body text
        # Body text resumes at a QUAESTIO/QUESTIO header or DIST. header
        if in_scholion:
            # Scholion ends at a QUAESTIO, DIST, or other body header
            if (re.match(r'^QU[.^iflÆAE]*STIO\b', stripped, re.IGNORECASE) or
                re.match(r'^DIST\.\s', stripped) or
                re.match(r'^ARTICULUS\b', stripped) or
                re.match(r'^TRACTATIO\b', stripped) or
                re.match(r'^(?:Utrum|Utrvm)\b', stripped) or
                re.match(r'^CoNTRA\b', stripped)):
                in_scholion = False
                # Fall through to body classification
            else:
                result.append(('scholion', line))
                continue

        # Apparatus detection
        if is_apparatus_line(line):
            in_apparatus = True
            result.append(('apparatus', line))
            continue

        # If we were in apparatus, check if this is a continuation
        if in_apparatus:
            is_body_resumption = (
                re.match(r'^\d+\.\s+(?:Item|Ad\s|Similiter|Praeterea)', stripped) or
                re.match(r'^(?:Respondeo|Contra|Sed\s+contra|CONCLUSIO|QU|DIST|ARTICULUS|TRACTATIO|DOUBT|DUBIA|CoNTRA)', stripped, re.IGNORECASE) or
                re.match(r'^(?:Utrum|Circa\s+primum|Consequenter|Secundo|Tertio|Quarto)', stripped)
            )
            if is_body_resumption:
                in_apparatus = False
                # Fall through to body classification
            else:
                # Apparatus continues — these are continuation lines of footnotes
                result.append(('apparatus', line))
                continue

        # Everything else is body text (may contain marginalia)
        result.append(('body', line))

    return result


# --- Marginalia detection ---
# Standalone marginalia: lines that are ENTIRELY marginalia (no body text)
STANDALONE_MARGINALIA = [
    r'^(?:Fundamcnia|FQndamenia|pnndamenia|Fimdamenta|Fundamenta)\.?\s*$',
    r'^(?:soiuiio|soluiio|Solutio)\s+op[a-z\-]*\.?\s*$',
    r'^(?:Dupiei|Duplex)\s+di[a-z\-]*\.?\s*$',
    r'^(?:Tersitas|versitas)\s+ra[a-z\-]*\.?\s*$',
    r'^(?:Aa|Ad)\s+(?:wosi|opposi)[a-z\-]*\.?\s*$',
    r'^(?:Qiialuoi|Quatuor)\s+(?:regulae|regu)[a-z\-]*\.?\s*$',
    r'^positorum\.\s*$',
    r'^tionis\.\s*$',
    r'^gicae\.\s*$',
    r'^(?:DnpiMmo|Duplex\s+mo)[a-z\-]*\.?\s*$',
    r'^(?:conciusio|conclusio|Conclusio)\.\s*$',  # standalone only
    # Garbled Conclusio headers (marginalia, not body)
    r'^Personarum\s+■',  # garbled conclusio header
]

# Patterns for marginalia prefixes jammed onto body text
MARGINALIA_PREFIX_PATTERNS = [
    r'(?:Fundamcnia|FQndamenia|pnndamenia|Fimdamenta|Fundamenta)',
    r'(?:conciusio|conclusio|Conclusio)',
    r'(?:soiuiio|soluiio|Solutio)',
    r'(?:Ad\s+opposi|Aa\s+wosi)',
]


def is_likely_marginalia(line):
    """Detect lines that are ENTIRELY marginalia (standalone fragments)."""
    stripped = line.strip()
    if not stripped:
        return False

    # Check standalone patterns
    for pat in STANDALONE_MARGINALIA:
        if re.match(pat, stripped, re.IGNORECASE):
            return True

    # Very short garbled lines (< 30 chars) with no Latin sentence structure
    if len(stripped) < 30 and not re.match(r'^\d+\.', stripped):
        words = stripped.split()
        if len(words) <= 3 and not any(w in stripped.lower() for w in ['ergo', 'item', 'sed', 'quia', 'quod', 'sic', 'etc']):
            garble_chars = len(re.findall(r'[■\^\*\'"<>{}|]', stripped))
            if garble_chars >= 2:
                return True

    return False


def strip_marginalia_prefix(line):
    """Remove marginalia prefix jammed onto body text.

    e.g., "pnndamenia.supponendo de Deo" -> "supponendo de Deo"
    e.g., "conciusio.  nere personarum" -> "nere personarum"
    e.g., "Fundamcnia.producendum" -> "producendum"
    e.g., "FQndamenia.  DfiMm  de  Dco" -> "DfiMm  de  Dco"
    """
    # Build pattern from known prefixes
    prefix_words = '|'.join(MARGINALIA_PREFIX_PATTERNS)
    m = re.match(
        r'^(?:' + prefix_words + r')[a-z\-]*\.\s*',
        line, re.IGNORECASE
    )
    if m:
        remainder = line[m.end():]
        if remainder.strip():  # only strip if there's body text after
            return remainder
        return ''  # otherwise the whole line was marginalia

    # Garbled marginalia clusters: '"dri^iSr' '''^"^' before body text
    m = re.match(r'^["\'■\^\*]+[a-zA-Z\^\'".\s]*?["\'■\^\*]+\s+', line)
    if m and len(m.group()) < 35:
        remainder = line[m.end():]
        if remainder and remainder[0].islower():
            return remainder

    # "sup-Aa wosi" pattern: marginalia jammed into a hyphenated word
    # e.g., "ex eisdem sup-Aa wosipositionibus" -> "ex eisdem suppositionibus"
    line = re.sub(r'-(?:Aa\s+wosi|Ad\s+opposi)[a-z]*', '', line)

    return line


def clean_body_text(text):
    """Apply OCR character fixes and normalize spacing."""
    for old, new in NAME_FIXES.items():
        text = text.replace(old, new)
    for pattern, replacement in WORD_FIXES:
        text = re.sub(pattern, replacement, text)

    lines = text.split('\n')
    cleaned = []
    for line in lines:
        line = re.sub(r'  +', ' ', line)
        line = line.rstrip()
        cleaned.append(line)
    return '\n'.join(cleaned)


def rejoin_hyphens(text):
    """Rejoin words broken across lines with hyphens."""
    lines = text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if (i + 1 < len(lines) and
            line.rstrip().endswith('-') and
            lines[i + 1].strip() and
            lines[i + 1].strip()[0].islower()):
            rejoined = line.rstrip()[:-1] + lines[i + 1].strip()
            result.append(rejoined)
            i += 2
        else:
            result.append(line)
            i += 1
    return '\n'.join(result)


def clean_chunk(filepath, dry_run=False, verbose=False):
    """Clean a single Latin chunk file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('### Latin\n', 1)
    if len(parts) != 2:
        print(f"  SKIP (no ### Latin section): {filepath}")
        return False

    header = parts[0] + '### Latin\n'
    latin = parts[1]

    # Check for ### English section
    english_split = latin.split('\n### English\n', 1)
    if len(english_split) == 2:
        latin = english_split[0]
        english_section = '\n### English\n' + english_split[1]
    else:
        english_section = ''

    lines = latin.split('\n')
    orig_count = len(lines)

    # Classify all lines
    classified = classify_lines(lines)

    # Keep only body + blank lines, with marginalia handling
    body_lines = []
    removed_counts = {'apparatus': 0, 'scholion': 0, 'page_header': 0, 'page_number': 0, 'marginalia': 0}

    prev_was_blank = False
    for cls, line in classified:
        if cls in ('apparatus', 'scholion', 'page_header', 'page_number'):
            removed_counts[cls] += 1
            prev_was_blank = False
            continue

        if cls == 'blank':
            if not prev_was_blank:
                body_lines.append(line)
            prev_was_blank = True
            continue

        prev_was_blank = False

        # Body line: check for marginalia
        if is_likely_marginalia(line):
            removed_counts['marginalia'] += 1
            continue

        # Strip marginalia prefixes
        line = strip_marginalia_prefix(line)

        body_lines.append(line)

    # Rejoin and fix OCR
    body_text = '\n'.join(body_lines)
    body_text = rejoin_hyphens(body_text)
    body_text = clean_body_text(body_text)
    body_text = re.sub(r'\n{4,}', '\n\n\n', body_text)

    new_count = len(body_text.strip().split('\n'))

    if verbose or dry_run:
        basename = os.path.basename(filepath)
        total_removed = sum(removed_counts.values())
        details = ', '.join(f"{k}:{v}" for k, v in removed_counts.items() if v > 0)
        print(f"  {basename}: {orig_count} -> {new_count} lines (removed: {details})")

    if not dry_run:
        cleaned = header + '\n' + body_text.strip() + '\n' + english_section
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cleaned)

    return True


def main():
    parser = argparse.ArgumentParser(description='Clean Latin OCR in Bonaventure Sentences chunks')
    parser.add_argument('--dry-run', action='store_true', help='Show what would change without writing')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show details for each file')
    parser.add_argument('--file', type=str, help='Clean a single file')
    parser.add_argument('--vol', type=int, default=1, help='Volume number (default: 1)')
    args = parser.parse_args()

    base_dir = Path(__file__).parent

    if args.file:
        files = [args.file]
    else:
        vol_dir = base_dir / f'vol{args.vol}'
        files = sorted(glob.glob(str(vol_dir / '*.md')))

    if not files:
        print(f"No files found in vol{args.vol}/")
        return

    print(f"{'DRY RUN — ' if args.dry_run else ''}Cleaning {len(files)} files...")

    cleaned = 0
    skipped = 0
    for f in files:
        result = clean_chunk(f, dry_run=args.dry_run, verbose=args.verbose or args.dry_run)
        if result:
            cleaned += 1
        else:
            skipped += 1

    print(f"\nDone: {cleaned} cleaned, {skipped} skipped")


if __name__ == '__main__':
    main()
