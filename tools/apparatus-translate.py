#!/usr/bin/env python3.11
"""
apparatus-translate.py — mechanical Latin → English translator for the
Quaracchi critical apparatus.

The Quaracchi apparatus is highly formulaic. This script handles the ~95% of
entries that are pure abbreviations + formulaic sentence patterns + sigla,
leaving only genuinely novel prose for human/LLM review.

Pipeline:
1. Parse the input into footnote entries (numbered 1, 2, 3, ...).
2. For each entry:
   a. Normalize whitespace and common OCR artifacts.
   b. Run an ordered sequence of sentence-pattern regexes that produce
      English fragments directly.
   c. Fall back to per-token lexicon substitution for any Latin that
      didn't match a pattern.
   d. Compute a confidence score based on how much ended up translated
      vs. how much is still Latin.
3. Emit a JSON document with Latin+English pairs, per-entry confidence,
   and a list of "unhandled" tokens for any entry below the threshold.

Usage:
    apparatus-translate.py < input.txt > output.json
    apparatus-translate.py input.txt output.json
    apparatus-translate.py --single "Cap. 10. n. 13. Vat. cum cod. A omittit X."
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

# Import the lexicon module (sibling file).
sys.path.insert(0, str(Path(__file__).parent))
import apparatus_lexicon as lex  # noqa: E402


# ----------------------------------------------------------------------------
# Data model
# ----------------------------------------------------------------------------

@dataclass
class Entry:
    """One footnote entry in the apparatus."""
    id: int
    la: str
    en: str = ""
    confidence: float = 0.0
    unhandled: list[str] = field(default_factory=list)


# ----------------------------------------------------------------------------
# Parsing: split a raw apparatus block into numbered entries
# ----------------------------------------------------------------------------

# Quaracchi numbers its footnotes per page with Arabic numerals or occasionally
# small letters. The OCR preserves them as bare numbers at line starts.
ENTRY_RE = re.compile(r"^\s*(\d+|[a-z])\.?\s+(.+?)(?=^\s*(?:\d+|[a-z])\.?\s|\Z)",
                      re.MULTILINE | re.DOTALL)


def parse_apparatus_block(text: str) -> list[Entry]:
    """
    Split a raw apparatus block into numbered entries.
    Falls back to treating each line as its own entry if no numbering is found.
    """
    entries: list[Entry] = []
    matches = list(ENTRY_RE.finditer(text))
    if matches:
        for m in matches:
            raw_id = m.group(1)
            body = m.group(2).strip()
            body = re.sub(r"\s+", " ", body)
            try:
                num = int(raw_id)
            except ValueError:
                num = len(entries) + 1
            entries.append(Entry(id=num, la=body))
    else:
        # No numbering detected — treat each non-empty line as an entry
        for i, line in enumerate(
            [line.strip() for line in text.splitlines() if line.strip()], start=1
        ):
            entries.append(Entry(id=i, la=line))
    return entries


# ----------------------------------------------------------------------------
# Sigla protection: freeze manuscript letters so lexicon substitution can't
# touch them. The apparatus uses `cod. A`, `codd. BCD`, `mss. AB`, `ms. X`,
# `ed. 1`, `edd. 1, 3, 5`. Protected spans are replaced with an unambiguous
# placeholder during translation and swapped back at the end.
# ----------------------------------------------------------------------------

# Match siglum phrases of the form:
#   (cod.|codd.|ms.|mss.|cf.|cfr.) followed by one-or-more capital letters
#   (Vat.) optionally followed by capital letters
#   (ed.|edd.) followed by digits and commas
# The letters/digits after the head word are the protected payload.
SIGLA_PROTECT = [
    # "cod. ABC" / "codd. ABCD"
    re.compile(r"\b(codd?\.)\s*([A-Z]+)\b"),
    # "ms. ABC" / "mss. ABCD"
    re.compile(r"\b(mss?\.)\s*([A-Z]+)\b"),
    # "ed. 1" / "edd. 1, 3, 5" (keep the head word unprotected; protect only
    # the digit list so patterns can still match on "ed.")
    re.compile(r"\b(edd?\.)\s*(\d+(?:\s*,\s*\d+)*)"),
    # Bare uppercase manuscript letter groups preceded by "Vat.", "cum", "et"
    # in sigla-list context — trickier, skip for now to avoid false positives.
]


def protect_sigla(text: str) -> tuple[str, dict[str, str]]:
    """
    Replace protected sigla spans with placeholders of the form §§Nn§§ where
    Nn is a sequential index. Returns (text, placeholder_map).
    """
    placeholders: dict[str, str] = {}
    counter = [0]

    def store(original: str) -> str:
        counter[0] += 1
        key = f"§§{counter[0]}§§"
        placeholders[key] = original
        return key

    out = text
    for pattern in SIGLA_PROTECT:
        def repl(m: re.Match) -> str:
            return m.group(1) + " " + store(m.group(2))
        out = pattern.sub(repl, out)
    return out, placeholders


def restore_sigla(text: str, placeholders: dict[str, str]) -> str:
    for key, original in placeholders.items():
        text = text.replace(key, original)
    return text


# ----------------------------------------------------------------------------
# Italic-span protection (v2): freeze everything wrapped in *...* so that
# lexicon substitution and pattern matching can't touch it.
#
# In the Quaracchi apparatus, italics mark three distinct things:
#   1. Latin work titles: *De praedicamentis*, *Summa theologiae*, *Metaph.*
#   2. Quoted variant readings: "cod. B legit *assumendo* pro *assumere*"
#   3. Lemmata from the main text being glossed
#
# None of these should be translated — they need to survive the pipeline
# verbatim. Protection uses the same placeholder mechanism as sigla protection,
# but with a distinct marker (§§i§§) so sigla and italics don't collide.
# ----------------------------------------------------------------------------

ITALIC_RE = re.compile(r"\*([^*\n]+)\*")


def protect_italics(text: str, start_index: int = 0) -> tuple[str, dict[str, str]]:
    """
    Replace *italic spans* with placeholders of the form §§iN§§. Returns
    (text, placeholder_map). The stars are preserved in the stored value so
    restoration yields a perfect round-trip.

    The optional `start_index` lets a second pass (run after pattern handlers
    emit new italic spans) avoid key collisions with the first pass's
    placeholders.
    """
    placeholders: dict[str, str] = {}
    counter = [start_index]

    def repl(m: re.Match) -> str:
        counter[0] += 1
        key = f"§§i{counter[0]}§§"
        placeholders[key] = m.group(0)
        return key

    out = ITALIC_RE.sub(repl, text)
    return out, placeholders


def restore_italics(text: str, placeholders: dict[str, str]) -> str:
    for key, original in placeholders.items():
        text = text.replace(key, original)
    return text


# ----------------------------------------------------------------------------
# Cleanup of common OCR artifacts that leak into the apparatus
# ----------------------------------------------------------------------------

OCR_FIXES = [
    (r"[‘’`]", "'"),
    (r"[“”]", '"'),
    (r"«", "«"),
    (r"»", "»"),
    (r"\s+—\s+", " — "),
    (r"\s+,", ","),
    (r"\s+\.", "."),
    (r"\s+;", ";"),
    (r"\s{2,}", " "),
    (r"\.\s*—\s*", ". — "),
]


def normalize(text: str) -> str:
    out = text
    for pattern, repl in OCR_FIXES:
        out = re.sub(pattern, repl, out)
    return out.strip()


# ----------------------------------------------------------------------------
# Sentence-pattern regexes — the heart of the translator
# ----------------------------------------------------------------------------
#
# Each pattern is:   (regex, handler_function)
# The handler receives the match object and returns an English fragment.
# Patterns are applied in order; once a span of text matches, it is marked
# "handled" and later patterns skip it.
#
# The goal is not to be comprehensive from day one — the goal is to handle
# the ~20 most common sentence shapes in Quaracchi apparatus, which together
# cover the majority of entries. Grow the list as we hit new patterns.

SIGLA_SOURCE = (
    r"(?:(?:Vat\.?|Vatican\.?)|(?:cod\.?|codex)\s*[A-Z]+"
    r"|(?:codd\.?|codices)\s*[A-Z][A-Z,\s]*"
    r"|(?:mss?\.?|manuscripti)\s*[A-Z]*"
    r"|(?:edd?\.?|editio(?:nes)?)\s*\d*(?:\s*,\s*\d+)*"
    r"|orig\.?|textus|originale)"
)


def _expand_sigla(s: str) -> str:
    """Render a sigla phrase in readable form without changing meaning."""
    s = re.sub(r"\s+", " ", s.strip())
    return s


def _handle_chapter_n(m: re.Match) -> str:
    return f"Ch. {m.group(1)}, n. {m.group(2)}"


def _handle_lib_cap_n(m: re.Match) -> str:
    lib, cap, n = m.group(1), m.group(2), m.group(3)
    return f"Bk. {lib}, ch. {cap}, n. {n}"


def _handle_q_a(m: re.Match) -> str:
    return f"q. {m.group(1)}, a. {m.group(2)}"


def _handle_d_p_a_q(m: re.Match) -> str:
    return f"d. {m.group(1)}, p. {m.group(2)}, a. {m.group(3)}, q. {m.group(4)}"


def _handle_omittunt(m: re.Match) -> str:
    sources = _expand_sigla(m.group("sources"))
    word = m.group("word")
    return f"{sources} omit *{word}*"


def _handle_addunt(m: re.Match) -> str:
    sources = _expand_sigla(m.group("sources"))
    word = m.group("word")
    return f"{sources} add *{word}*"


def _handle_habent(m: re.Match) -> str:
    sources = _expand_sigla(m.group("sources"))
    word = m.group("word")
    return f"{sources} have *{word}*"


def _handle_legunt_pro(m: re.Match) -> str:
    sources = _expand_sigla(m.group("sources"))
    read = m.group("read")
    orig = m.group("orig")
    return f"{sources} read *{read}* instead of *{orig}*"


def _handle_x_pro_y(m: re.Match) -> str:
    sources = _expand_sigla(m.group("sources"))
    new = m.group("new")
    old = m.group("old")
    return f"{sources} [read] *{new}* instead of *{old}*"


def _handle_restituimus_ex(m: re.Match) -> str:
    source = _expand_sigla(m.group("source"))
    return f"Restored from {source}"


def _handle_supplevimus_ex(m: re.Match) -> str:
    source = _expand_sigla(m.group("source"))
    return f"Supplied from {source}"


def _handle_cfr(m: re.Match) -> str:
    return "Cf."


def _handle_vide_supra(m: re.Match) -> str:
    return "See above"


def _handle_vide_infra(m: re.Match) -> str:
    return "See below"


def _handle_loc_cit(m: re.Match) -> str:
    return "loc. cit."


def _handle_ibid(m: re.Match) -> str:
    return "ibid."


def _handle_paulo_ante(m: re.Match) -> str:
    return "A little before"


def _handle_paulo_post(m: re.Match) -> str:
    return "A little after"


def _handle_in_fine(m: re.Match) -> str:
    return "at the end"


def _handle_in_principio(m: re.Match) -> str:
    return "at the beginning"


def _handle_in_fine_textus(m: re.Match) -> str:
    return "At the end of the text"


def _handle_in_principio_textus(m: re.Match) -> str:
    return "At the beginning of the text"


def _handle_in_medio_textus(m: re.Match) -> str:
    return "In the middle of the text"


def _handle_ad_n(m: re.Match) -> str:
    return f"reply to obj. {m.group(1)}"


# --- v2 handlers -----------------------------------------------------------

def _handle_de_title(m: re.Match) -> str:
    """
    "De <title>" where <title> is an italic-protected placeholder or a
    recognized abbreviation. Render as "On <title>" without translating the
    title itself. This exists so that Aristotelian and Augustinian work
    titles like *De praedicamentis* survive the pipeline.
    """
    title = m.group("title")
    return f"On {title}"


def _handle_videri_non_debet(m: re.Match) -> str:
    return "ought not to be understood"


def _handle_videri_debet(m: re.Match) -> str:
    return "ought to be understood"


def _handle_patet_ex(m: re.Match) -> str:
    src = m.group("src").strip()
    return f"is clear from {src}"


def _handle_sensu_eodem(m: re.Match) -> str:
    return "in the same sense"


def _handle_eodem_modo(m: re.Match) -> str:
    return "in the same way"


def _handle_aliter_aliter(m: re.Match) -> str:
    return "one way... another way"


def _handle_ad_verbum(m: re.Match) -> str:
    return "word-for-word"


def _italicize_if_bare(word: str) -> str:
    """
    Wrap a captured word in *italics* unless it's already an italic
    placeholder (§§iN§§). Used by ablative-absolute handlers so that the
    preserved Latin token can't be lexicon-substituted in a later pass.
    """
    word = word.strip()
    if word.startswith("§§") and word.endswith("§§"):
        return word
    return f"*{word}*"


def _handle_ablative_absolute_omisso(m: re.Match) -> str:
    """
    "omisso <word>" → "with <word> omitted". Ablative absolute with omitto.
    """
    word = _italicize_if_bare(m.group("word"))
    return f"with {word} omitted"


def _handle_ablative_absolute_addito(m: re.Match) -> str:
    """
    "addito <word>" → "with <word> added".
    """
    word = _italicize_if_bare(m.group("word"))
    return f"with {word} added"


def _handle_ablative_absolute_mutato(m: re.Match) -> str:
    """
    "mutato <word>" → "with <word> changed".
    """
    word = _italicize_if_bare(m.group("word"))
    return f"with {word} changed"


def _handle_ablative_absolute_posito(m: re.Match) -> str:
    """
    "posito <word>" → "with <word> set [in its place]".
    """
    word = _italicize_if_bare(m.group("word"))
    return f"with {word} set [in place]"


def _handle_scilicet_lemma(m: re.Match) -> str:
    return "namely"


def _handle_videsis(m: re.Match) -> str:
    return "see"


def _handle_et_passim(m: re.Match) -> str:
    return "and throughout"


def _handle_apud(m: re.Match) -> str:
    return "in"


PATTERNS = [
    # Citation structures (more specific first)
    (re.compile(
        r"\blib(?:r)?\.?\s*([IVXLCDM\d]+)[,.]?\s*cap?\.?\s*(\d+)[,.]?\s*n\.?\s*(\d+)",
        re.IGNORECASE,
    ), _handle_lib_cap_n),
    (re.compile(
        r"\b[Cc]ap(?:it)?\.?\s*(\d+)[,.]?\s*n\.?\s*(\d+)",
    ), _handle_chapter_n),
    (re.compile(
        r"\bd\.?\s*(\d+)[,.]?\s*p\.?\s*([IVX\d]+)[,.]?\s*a\.?\s*(\d+)[,.]?\s*q\.?\s*(\d+)",
        re.IGNORECASE,
    ), _handle_d_p_a_q),
    (re.compile(
        r"\bq\.?\s*(\d+)[,.]?\s*a\.?\s*(\d+)", re.IGNORECASE,
    ), _handle_q_a),
    (re.compile(r"\bad\s+(\d+)\b"), _handle_ad_n),

    # Source + verb patterns
    (re.compile(
        rf"(?P<sources>{SIGLA_SOURCE}(?:\s+(?:et|cum|contra)\s+{SIGLA_SOURCE})*)"
        r"\s+omittunt?\s+(?P<word>\S+)",
    ), _handle_omittunt),
    (re.compile(
        rf"(?P<sources>{SIGLA_SOURCE}(?:\s+(?:et|cum|contra)\s+{SIGLA_SOURCE})*)"
        r"\s+addunt?\s+(?P<word>\S+)",
    ), _handle_addunt),
    (re.compile(
        rf"(?P<sources>{SIGLA_SOURCE}(?:\s+(?:et|cum|contra)\s+{SIGLA_SOURCE})*)"
        r"\s+habent\s+(?P<word>\S+)",
    ), _handle_habent),
    (re.compile(
        rf"(?P<sources>{SIGLA_SOURCE}(?:\s+(?:et|cum|contra)\s+{SIGLA_SOURCE})*)"
        r"\s+legunt?\s+(?P<read>\S+)\s+pro\s+(?P<orig>\S+)",
    ), _handle_legunt_pro),

    # "X cum Y et Z: ‹word› pro ‹word›" (source list followed by word pro word)
    (re.compile(
        rf"(?P<sources>{SIGLA_SOURCE}(?:\s+(?:et|cum)\s+{SIGLA_SOURCE})+)"
        r":?\s+(?P<new>\S+)\s+pro\s+(?P<old>\S+)",
    ), _handle_x_pro_y),

    # Editorial actions
    (re.compile(r"[Rr]estituimus\s+ex\s+(?P<source>" + SIGLA_SOURCE + ")"),
     _handle_restituimus_ex),
    (re.compile(r"[Ss]upplevimus\s+ex\s+(?P<source>" + SIGLA_SOURCE + ")"),
     _handle_supplevimus_ex),

    # Cross-references
    (re.compile(r"\bcfr?\.", re.IGNORECASE), _handle_cfr),
    (re.compile(r"\bvid(?:e)?\s+supra\b", re.IGNORECASE), _handle_vide_supra),
    (re.compile(r"\bvid(?:e)?\s+infra\b", re.IGNORECASE), _handle_vide_infra),
    (re.compile(r"\bv\.\s+supra\b", re.IGNORECASE), _handle_vide_supra),
    (re.compile(r"\bv\.\s+infra\b", re.IGNORECASE), _handle_vide_infra),
    (re.compile(r"\bloc\.\s*cit\b", re.IGNORECASE), _handle_loc_cit),
    # "Ibid." / "Ibidem" — consume trailing period to avoid double punctuation
    (re.compile(r"\bibid(?:em)?\.?", re.IGNORECASE), _handle_ibid),

    # Positional phrases (textus variants match before plain ones)
    (re.compile(r"\bin\s+fine\s+textus\b", re.IGNORECASE), _handle_in_fine_textus),
    (re.compile(r"\bin\s+principio\s+textus\b", re.IGNORECASE), _handle_in_principio_textus),
    (re.compile(r"\bin\s+medio\s+textus\b", re.IGNORECASE), _handle_in_medio_textus),
    (re.compile(r"\bpaulo\s+ante\b", re.IGNORECASE), _handle_paulo_ante),
    (re.compile(r"\bpaulo\s+post\b", re.IGNORECASE), _handle_paulo_post),
    (re.compile(r"\bin\s+fine\b", re.IGNORECASE), _handle_in_fine),
    (re.compile(r"\bin\s+principio\b", re.IGNORECASE), _handle_in_principio),

    # --- v2: work titles, idioms, ablative absolutes ------------------------

    # "De <italic-placeholder-or-abbreviation>" — render as "On <title>"
    # without translating the title. Runs AFTER italic protection, so italic
    # titles appear as §§iN§§ placeholders at this stage.
    (re.compile(
        r"\bDe\s+(?P<title>§§i\d+§§|[A-Z][a-zA-Z]*\.?(?:\s+[a-z]+\.?)?)",
    ), _handle_de_title),

    # Common Latin idioms that lexicon-substitution would otherwise fragment.
    (re.compile(r"\bvideri\s+non\s+debet\b", re.IGNORECASE), _handle_videri_non_debet),
    (re.compile(r"\bvideri\s+debet\b", re.IGNORECASE), _handle_videri_debet),
    (re.compile(r"\bpatet\s+ex\s+(?P<src>§§\w+§§|[a-zA-Z., ]+?)(?=[;.,]|$)",
                re.IGNORECASE), _handle_patet_ex),
    (re.compile(r"\bsensu\s+eodem\b", re.IGNORECASE), _handle_sensu_eodem),
    (re.compile(r"\beodem\s+sensu\b", re.IGNORECASE), _handle_sensu_eodem),
    (re.compile(r"\beodem\s+modo\b", re.IGNORECASE), _handle_eodem_modo),
    (re.compile(r"\baliter\s+et\s+aliter\b", re.IGNORECASE), _handle_aliter_aliter),
    (re.compile(r"\bad\s+verbum\b", re.IGNORECASE), _handle_ad_verbum),
    (re.compile(r"\bet\s+passim\b", re.IGNORECASE), _handle_et_passim),
    (re.compile(r"\bvidesis\b", re.IGNORECASE), _handle_videsis),

    # Ablative absolutes: "<participle> <noun>" → "with <noun> <done>".
    # Scoped to a small set of participles that actually occur in the
    # apparatus (omisso, addito, mutato, posito). Noun is captured greedily
    # until punctuation.
    (re.compile(
        r"\bomisso\s+(?P<word>§§\w+§§|[a-zA-Z]+(?:\s+[a-z]+)?)",
    ), _handle_ablative_absolute_omisso),
    (re.compile(
        r"\baddito\s+(?P<word>§§\w+§§|[a-zA-Z]+(?:\s+[a-z]+)?)",
    ), _handle_ablative_absolute_addito),
    (re.compile(
        r"\bmutato\s+(?P<word>§§\w+§§|[a-zA-Z]+(?:\s+[a-z]+)?)",
    ), _handle_ablative_absolute_mutato),
    (re.compile(
        r"\bposito\s+(?P<word>§§\w+§§|[a-zA-Z]+(?:\s+[a-z]+)?)",
    ), _handle_ablative_absolute_posito),
]


# ----------------------------------------------------------------------------
# Lexicon fallback: token-by-token substitution for Latin that patterns missed
# ----------------------------------------------------------------------------

LEXICON = lex.merged_lexicon()

# Keys that contain a period or multi-word phrases need literal matching,
# not \b word boundaries. Split them into two lists.
MULTI_WORD_KEYS = sorted(
    [k for k in LEXICON if " " in k or "." in k],
    key=len, reverse=True,
)
SINGLE_WORD_KEYS = [k for k in LEXICON if k not in MULTI_WORD_KEYS]


def _case_preserving_replace(key: str, value: str) -> callable:
    """
    Build a regex substitution callback that replaces `key` (case-insensitive)
    with `value`, preserving the capitalization of the first letter of the
    matched token when the match started with a capital.
    """
    def callback(m: re.Match) -> str:
        matched = m.group(0)
        if matched and matched[0].isupper() and value:
            return value[0].upper() + value[1:]
        return value
    return callback


def lexicon_substitute(text: str) -> tuple[str, list[str]]:
    """
    Apply lexicon substitutions to remaining Latin tokens.
    Returns (english, untranslated_tokens).
    """
    out = text

    # Multi-word / punctuation-bearing keys first (longest first so longer
    # abbreviations win over shorter overlapping ones). Case-insensitive
    # matching with case preservation for the first letter.
    for key in MULTI_WORD_KEYS:
        pattern = re.escape(key)
        out = re.sub(
            rf"(?<!\w){pattern}(?!\w)",
            _case_preserving_replace(key, LEXICON[key]),
            out,
            flags=re.IGNORECASE,
        )

    # Then whole-word keys.
    for key in SINGLE_WORD_KEYS:
        out = re.sub(
            rf"\b{re.escape(key)}\b",
            _case_preserving_replace(key, LEXICON[key]),
            out,
            flags=re.IGNORECASE,
        )

    unhandled = _find_latin_leftovers(out)
    return out, unhandled


# English words that superficially end with Latin-looking suffixes but should
# NOT be flagged as Latin leftovers.
_ENGLISH_FALSE_POSITIVES = frozenset({
    "this", "his", "was", "has", "its", "also",
    "status", "focus", "campus", "genus", "bonus", "thus",
    "basis", "crisis", "thesis", "analysis",
})

# Regex for Latin-looking words not caught by the lexicon. This is
# deliberately broad — false positives are cheap (they just flag entries for
# review), but false negatives let bad output through with high confidence.

_LATIN_ENDINGS = re.compile(
    r"\b[A-Za-z]{4,}(?:"
    r"orum|arum|ibus|entur|antur|untur|itur|atur|etur|bantur|bundus|"
    r"issimus|issima|issimum|issimis|issimos|issimas|"
    r"entium|antium|antibus|entibus|"
    r"endum|endam|endos|endas|endae|endis|endorum|endarum|"
    r"atus|ata|atum|atos|atas|atae|atorum|atarum|"
    r"itus|itum|itos|itae|itorum|itarum|"
    r"osus|osa|osum|osae|osis|osos|osas|osorum|osarum|"
    r"alis|ales|alia|alem|alibus|alium|"
    r"aris|ares|arium|aribus|"
    r"ivus|iva|ivum|ivae|ivis|ivos|ivas|"
    r"abant|abam|abas|abat|abamus|abatis|"
    r"ebant|ebam|ebas|ebat|ebamus|ebatis|"
    r"avit|averunt|avisti|averam|averat|averamus|"
    r"amus|antur|"
    r"tatem|tates|tatis|tatum|tatibus|"
    r"tionis|tionem|tionibus|tiones|tionum"
    r")\b"
)

# Common Latin function words and pronouns that should be caught if they
# survived the lexicon pass (indicates a lexicon gap).
_COMMON_LATIN = re.compile(
    r"\b(?:quod|quae|qui|quem|quam|quos|quas|quibus|cuius|cui|"
    r"sed|autem|enim|quidem|ergo|igitur|tamen|vero|ipse|ipsa|ipsum|"
    r"tantum|modo|semper|numquam|iam|adhuc|"
    r"multis|multi|multae|multa|multos|multas|multorum|multarum|multum|"
    r"nonnullis|nonnulli|nonnullae|nonnulla|"
    r"huiusmodi|eiusmodi|"
    r"huic|huius|hunc|hanc|hoc|hac|his|horum|harum|hisce)\b"
)


def _find_latin_leftovers(text: str) -> list[str]:
    """Collect Latin-looking words that the translator didn't handle."""
    out = set()
    for m in _LATIN_ENDINGS.finditer(text):
        word = m.group(0)
        if word.lower() not in _ENGLISH_FALSE_POSITIVES:
            out.add(word)
    for m in _COMMON_LATIN.finditer(text):
        out.add(m.group(0))
    return sorted(out)


# ----------------------------------------------------------------------------
# Confidence scoring
# ----------------------------------------------------------------------------

def score(original_la: str, english: str, unhandled: list[str]) -> float:
    """
    Confidence score: fraction of the output that looks like English rather
    than Latin. Quoted Latin words in italics (matching *word*) are excluded
    from the Latin count — they're intentional quotations of variant readings.
    """
    # Strip italicized Latin quotations — those are intentional.
    stripped = re.sub(r"\*[^*]+\*", "", english)
    # Count tokens in the stripped English.
    tokens = [t for t in re.findall(r"[A-Za-z]+", stripped) if len(t) >= 2]
    if not tokens:
        return 1.0
    latin_tokens = set(unhandled)
    # Tokens in the unhandled set are counted as Latin; the rest are English.
    latin_in_output = sum(1 for t in tokens if t in latin_tokens)
    english_fraction = 1.0 - (latin_in_output / len(tokens))
    return round(english_fraction, 3)


# ----------------------------------------------------------------------------
# Main translation function
# ----------------------------------------------------------------------------

def translate_entry(entry: Entry) -> Entry:
    """Translate a single apparatus entry in place."""
    entry.la = normalize(entry.la)

    # v2: Protect italic spans FIRST — work titles, quoted variant readings,
    # and lemmata must survive the pipeline verbatim. Italics are protected
    # before sigla because sigla phrases sometimes appear inside italics
    # (e.g. "*cod. B*" in a footnote about a codex), but we want the outer
    # italics to dominate.
    current, italic_placeholders = protect_italics(entry.la)

    # Protect sigla (ms. letters, edition numbers) from lexicon substitution.
    current, sigla_placeholders = protect_sigla(current)

    # Apply sentence patterns — each replaces its matching span with English.
    for pattern, handler in PATTERNS:
        current = pattern.sub(lambda m, h=handler: h(m), current)

    # v2: Second italic-protection pass. Some handlers (notably the ablative
    # absolute family: omisso, addito, mutato, posito) emit new *word* spans
    # around preserved Latin tokens. These need protection before the lexicon
    # fallback, or the lexicon will happily substitute "etiam" → "also"
    # inside "*etiam*" and produce "*also*". Start the second pass's counter
    # past the first pass's highest index to avoid key collisions.
    first_pass_max = len(italic_placeholders)
    current, new_italic_placeholders = protect_italics(current, start_index=first_pass_max)
    italic_placeholders.update(new_italic_placeholders)

    # Fallback lexicon substitution for remaining tokens.
    current, unhandled = lexicon_substitute(current)

    # Restore protected sigla and italics (in reverse order — italics last
    # since they were protected first).
    current = restore_sigla(current, sigla_placeholders)
    current = restore_italics(current, italic_placeholders)

    # Light English cleanup
    current = re.sub(r"\s{2,}", " ", current).strip()
    current = re.sub(r"\s+,", ",", current)
    current = re.sub(r"\s+\.", ".", current)
    current = re.sub(r"\s+;", ";", current)
    current = current[0].upper() + current[1:] if current else current

    entry.en = current
    entry.unhandled = unhandled
    entry.confidence = score(entry.la, entry.en, unhandled)
    return entry


def translate_apparatus(text: str) -> list[Entry]:
    """Parse a raw apparatus block and translate each entry."""
    entries = parse_apparatus_block(text)
    return [translate_entry(e) for e in entries]


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Mechanically translate the Quaracchi Latin critical apparatus into "
            "English drafts, flagging low-confidence entries for review."
        )
    )
    parser.add_argument(
        "input", nargs="?", type=Path,
        help="Input file with apparatus block (stdin if omitted)",
    )
    parser.add_argument(
        "output", nargs="?", type=Path,
        help="Output JSON file (stdout if omitted)",
    )
    parser.add_argument(
        "--single", type=str, default=None,
        help="Translate a single apparatus string (no parsing into entries)",
    )
    parser.add_argument(
        "--threshold", type=float, default=0.75,
        help="Confidence threshold below which entries go into the review queue",
    )
    parser.add_argument(
        "--pretty", action="store_true", default=True,
        help="Pretty-print JSON output",
    )
    args = parser.parse_args()

    if args.single:
        entry = Entry(id=1, la=args.single)
        translate_entry(entry)
        result = asdict(entry)
    else:
        if args.input:
            text = args.input.read_text(encoding="utf-8")
        else:
            text = sys.stdin.read()
        entries = translate_apparatus(text)
        low_conf = [e for e in entries if e.confidence < args.threshold]
        result = {
            "entries": [asdict(e) for e in entries],
            "review_queue": [e.id for e in low_conf],
            "stats": {
                "total": len(entries),
                "high_confidence": len(entries) - len(low_conf),
                "low_confidence": len(low_conf),
                "threshold": args.threshold,
            },
        }

    indent = 2 if args.pretty else None
    payload = json.dumps(result, indent=indent, ensure_ascii=False)

    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)

    return 0


if __name__ == "__main__":
    sys.exit(main())
