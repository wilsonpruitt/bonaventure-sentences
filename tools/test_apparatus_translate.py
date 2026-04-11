#!/usr/bin/env python3.11
"""
Regression tests for apparatus-translate.py.

Runs a fixed set of Latin apparatus snippets through the translator and
checks that the English output contains (or does not contain) expected
substrings. This is deliberately string-based rather than exact-match,
since the exact English wording is allowed to shift as the lexicon grows.

Run: python3.11 tools/test_apparatus_translate.py
Exit 0 if all pass, 1 otherwise. Prints a per-test summary.
"""

from __future__ import annotations

import importlib.util
import sys
from dataclasses import dataclass
from pathlib import Path

# Dynamic import of apparatus-translate.py (dash in filename prevents direct
# `import apparatus_translate`). The module must be registered in sys.modules
# before exec_module runs, or @dataclass decorators inside it fail.
_HERE = Path(__file__).parent
_SPEC = importlib.util.spec_from_file_location(
    "apparatus_translate", _HERE / "apparatus-translate.py"
)
assert _SPEC and _SPEC.loader
apparatus_translate = importlib.util.module_from_spec(_SPEC)
sys.modules["apparatus_translate"] = apparatus_translate
_SPEC.loader.exec_module(apparatus_translate)

translate_entry = apparatus_translate.translate_entry
Entry = apparatus_translate.Entry


@dataclass
class Case:
    name: str
    la: str
    must_contain: list[str]
    must_not_contain: list[str] = None

    def __post_init__(self):
        if self.must_not_contain is None:
            self.must_not_contain = []


CASES: list[Case] = [
    # --------- v2 targets ---------------------------------------------------
    Case(
        name="v2: italic work title preserved (De praedicamentis)",
        la="Arist., *De praedicamentis*, c. De oppositis.",
        must_contain=["*De praedicamentis*"],
        must_not_contain=["Concerning praedicamentis"],
    ),
    Case(
        name="v2: italic variant readings preserved (X pro Y)",
        la="Cod. B legit *assumendo* pro *assumere*.",
        must_contain=["*assumendo*", "*assumere*", "reads", "instead of"],
    ),
    Case(
        name="v2: idiom — videri non debet",
        la="Videri non debet, quod Augustinus hic approbet.",
        must_contain=["Ought not to be understood"],
        must_not_contain=["Videri non debet"],
    ),
    Case(
        name="v2: idiom — ad verbum",
        la="Cod. A ad verbum ut apud Arist.",
        must_contain=["word-for-word"],
    ),
    Case(
        name="v2: idiom — eodem modo",
        la="Eodem modo legitur in cod. B.",
        must_contain=["In the same way"],
    ),
    Case(
        name="v2: ablative absolute — omisso",
        la="Vat. legit, omisso verbo, pro cod. A.",
        must_contain=["with *verbo* omitted"],
    ),
    Case(
        name="v2: ablative absolute — addito (protected from lexicon)",
        la="Cod. B, addito etiam, sequitur originale.",
        # The preserved Latin word must survive lexicon substitution: the
        # test guards against the previous bug where "etiam" → "also" leaked
        # into the italicized span.
        must_contain=["with *etiam* added"],
        must_not_contain=["*also*"],
    ),

    # --------- pre-existing behavior (regression) ---------------------------
    Case(
        name="existing: chapter/n citation",
        la="Cap. 11, n. 17.",
        must_contain=["Ch. 11", "n. 17"],
    ),
    Case(
        name="existing: lib/cap/n citation",
        la="Lib. I, cap. 4, n. 4.",
        must_contain=["Bk. I", "ch. 4", "n. 4"],
    ),
    Case(
        name="existing: codd. add <word>",
        la="Codd. ABC addunt etiam.",
        must_contain=["add"],
    ),
    Case(
        name="existing: cf. abbreviation",
        la="Cf. Arist., Eth. Nic. II, c. 1.",
        must_contain=["Cf."],
    ),
    Case(
        name="existing: see above / see below",
        la="Vide supra ad arg. 2.",
        must_contain=["See above"],
    ),
    Case(
        name="existing: ibid (no double period)",
        la="Ibid. Cf. et supra.",
        must_contain=["Ibid."],
        must_not_contain=["Ibid..", "ibid.."],
    ),
    Case(
        name="existing: 'paulo post' positional phrase",
        la="Paulo post quidam codices addunt etiam secundum se.",
        must_contain=["A little after"],
    ),
]


def run() -> int:
    passed = 0
    failed = 0
    for case in CASES:
        entry = Entry(id=0, la=case.la)
        translate_entry(entry)
        en = entry.en

        missing = [s for s in case.must_contain if s not in en]
        leaked = [s for s in case.must_not_contain if s in en]

        if not missing and not leaked:
            passed += 1
            print(f"  PASS  {case.name}")
        else:
            failed += 1
            print(f"  FAIL  {case.name}")
            print(f"        LA: {case.la}")
            print(f"        EN: {en}")
            if missing:
                print(f"        missing: {missing}")
            if leaked:
                print(f"        leaked:  {leaked}")

    total = passed + failed
    print()
    print(f"  {passed}/{total} passed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(run())
