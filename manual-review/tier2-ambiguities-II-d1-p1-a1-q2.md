# Tier-2 ambiguities — II.d.1 p.I a.1 q.2 (Utrum mundus productus sit ab aeterno, an ex tempore)

Drafted 2026-05-13 during Tier-2 promotion of `vol2/bon-sent-II-d1-p1-a1-q2.md` (raw lines 2019–2410; printed pp.19–24; pdf pp.41–46, offset +22).

Two genuinely ambiguous OCR spots survive in this chunk. Both are parked for the d.10 polish-blocker pass — at that point a 600dpi extract of pdf pp.41–46 will resolve them eyes-on against the printed page.

## [?] flags inline in the chunk

### 1. Codex-letter list at apparatus entry 3 (p.19 footer 3)

**Location**: `## Apparatus` → `[^3]` **La.**
**Text as rendered**:
> Paulo inferius plures codd. ni B E F H K V *mundus incepit* pro *mutatus incipit*.

**OCR raw** (chunk file line 47, raw line 2065):
```
Paulo inferius plures codd. ni B E F H Iv V mundns incepit pvo muralus incipit.
```

**Ambiguity**:
- `ni` is plausibly OCR for either `in` (preposition) or a stray ligature glitch — Quaracchi typically reads "Paulo inferius plures codd. cum ed. N…" or "plures codd. M N O P…" but never "ni"; I have provisionally let `ni` stand and flagged.
- The sequence of codex letters as printed includes `Iv` which I have read as `K` (Quaracchi's K and Iv ligatures are visually adjacent at 200dpi).

**Resolution path**: 600dpi extract of p.19 col 1 footer 3; verify the codex-letter run reads `B E F H K V` (most likely), and resolve `ni` → `in` or some other connective.

### 2. *potum / lutum* variant at apparatus entry 49 (p.24 footer 7)

**Location**: `## Apparatus` → `[^49]` **La.**

The Quaracchi note records a textual variant where the Vatican ms. reads *lutum* ("clay") at the position where the body has *potum* — and glosses *potum* as "vasculum vel poculum" per Du Cange. The body itself reads `Angelus possit facere potum figuli`, which I have translated as "an Angel can make a *potum* of a potter" (leaving the Latin in italics rather than guessing English between "vessel," "cup," and "drinking-pot").

**Ambiguity**:
- Whether *potum* should render in English as "vessel," "cup," "drinking-pot," or some neutral hand-leaving as Latin. The Du Cange entry cited by Quaracchi is the right source.
- Whether the body should be amended to *lutum* (the Vat. reading would make obvious sense: "an Angel can shape the *clay* of a potter, since he has no hands") or kept as *potum*.

**Resolution path**: 600dpi extract of p.24 body line; verify the body reads *potum* (vs *lutum*), then settle on the English rendering. If *potum* is correct, "drinking-pot" / "cup" is the Du Cange gloss; if *lutum*, "clay" is direct.

## Resolved at draft time (recorded for completeness)

- **OCR garbles silently corrected** where context made the reading unambiguous: `Uirum` → `Utrum`; `molu` / `motnm` → `motum`; `oslensiva` → `ostensiva`; `Adopposi-` and `Fuudameuia.` / `Notandura.` / etc. marginal glosses trimmed (not rendered as headings); `Pliilosoplii` → `Philosophi`; `infmitum` / `inflnitas` → `infinitum` / `infinitas`; `inceperunt` / `incipit` cluster resolved against context; Roman-numeral garbles in apparatus normalized (`,\l.` → `XI.`, `1 2` for `12`, etc.); page-number bleeds (`20`, `22`, `23`, `24`) treated as Quaracchi running-head/page-number markers and used to anchor `<!-- page N -->` breaks at chunk-line 33, 103, 168, 251, 317.
- **Apparatus numbering**: Quaracchi restarts numbering per page; chunk uses a single sequence 1–51 across pp.19–24, with the crosswalk table in `## Notes`.
- **Marginal-gloss trims** (per CLAUDE.md "trim marginal glosses aggressively"): `Ad oppositum`, `Fundamenta`, `Conclusio`, `Solutio I/II...`, `Distinctio`, `Notandum`, `Aliae rationes a parte causae producentis`, `Primum exemplum` / `Secundum exemplum`, `Iudicium auctoris`, `Alii aliter intelligunt Aristotelem`, `Alia solutio`, `Quaestio incidentalis`, `Solvendum`. These were not rendered as headings; the structural rhythm of the chunk (6 rationes Philosophi → 6 fundamenta per se nota → conclusio → respondeo with replies 1–6 → Scholion I–IV) is surfaced via bold numbering instead.

## Larger Quaracchi cross-references left flat (not flagged)

A handful of bibliographic / textual-variant entries (e.g. `Cfr. tom. I. pag. 137, nota 6 et 8.`; `tom. I. pag. 798, nota 6.`; `tom. I. pag. 638, nota 1.`) reference Quaracchi Vol I locations that this Vol II project hasn't yet cross-indexed; they are preserved verbatim in both La and En blocks without follow-up. If the corpus eventually grows hyperlinking, these become anchor candidates.
