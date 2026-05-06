# Tier-2 Ambiguities: bon-sent-I-d30-dubia

Date: 2026-05-06  
Raw OCR source: `bonaventure_vol1_pt2_raw.txt`, lines 10976–11185

---

## [?] Flags

### 1. Apparatus fn.13 codex identity (p. 527)
**Location:** [^13], apparatus on p. 527, right column  
**OCR reads:** `Pro verbis temporis existentiam cod. [exhibet] temporis continentiam...`  
The codex siglum is not legible in the OCR (the line break garbles it). The apparatus says "cod. [?] exhibet" — the codex letter is missing.  
**Currently rendered:** `cod. [?] exhibet` — flagged inline.  
**Resolution:** Requires PDF eyes-on to recover the codex siglum.

### 2. Printed page numbers for this chunk
**Location:** frontmatter `printed_pages` and `pdf_pages`  
**OCR situation:** The only legible page header in the dubia OCR range is "328" at line 11076, which does not fit the sequence (neighboring pages 524 at line 10670 and 530 at ~line 11274). "328" is almost certainly an OCR garble of "528" (the leading "5" dropped).  
**Currently rendered:** `printed_pages: [527, 528, 529]`, `pdf_pages: [117, 118, 119]` (= 527–529 minus 410).  
**Resolution:** Confirm against PDF or check d.30 quaestio page numbers to bracket the dubia precisely. Low priority: page numbers do not affect text content.

### 3. DUB. II OCR garbles in right-column marginal notes
**Location:** DUB. II response, OCR lines with marginal labels  
**OCR reads:** Various marginal gloss fragments appear interleaved with the text: `Notanda di-`, `Adqnaesiio-`, `i""'""'-` — these are section-annotation labels in the printed margin, not body text.  
**Currently rendered:** Trimmed out per CLAUDE.md rules (marginal glosses bleeding inline are editorial marginalia, not Bonaventure's text).  
**Resolution:** None required — correct to trim.

### 4. DUB. II "instantiam in imperitis" — reading uncertain
**Location:** DUB. II objection, `Si tu das instantiam in im'pe-tuis` in OCR  
**OCR reads:** `instantiam m im'pe-tuis` — garbled. Context: "Si tu das instantiam in imperitis" (if you give an instance in things at their very beginning / in those at their beginning). The word "imperitis" or "impetuosis" is possible; the OCR line-break fragment `im'pe-` makes it unclear.  
**Currently rendered:** `instantiam in imperitis` (conjectured from context: the objector raises the case of things at the outset/beginning).  
**Resolution:** Requires PDF eyes-on. Flag: `[?]` not placed inline because the phrase is syntactically clear and the sense follows naturally; flagged here for PDF verification.

### 5. DUB. III "nvu^" for "nummus"
**Location:** DUB. III opening, OCR reads `nvu^`  
**OCR reads:** `nvu^ mutatus non est`  
**Currently rendered:** `nummus mutatus non est` — silent OCR correction; context is unambiguous (the whole dubium is about whether the coin is changed).  
**Resolution:** None required — unambiguous.

---

## Non-[?] OCR notes (silently corrected)

- `Dicendnni` → `Dicendum` (DUB. I response opener)
- `acclii` → `actu` (DUB. I, "quia actu legit")
- `creanduni` → `creandum` (DUB. I)
- `ad sv` (DUB. V, OCR garble of "ad se") → `ad se` — unambiguous from context
- `huiusmodi ,` → `huiusmodi` (extra comma from OCR column break)
- `i'i potentia` → `in potentia` (DUB. III)
- `Iteni` → `Item` (DUB. V opening)
- `qnaeritur` → `quaeritur` (DUB. V)
- `hene esse` → `bene esse` (DUB. IV response)
- `flliatio` → `filiatio` (DUB. IV response)
- `adoptio-neni` → `adoptionem` (hyphenated line break)
- `siraplicitatera` → `simplicitatem` (DUB. IV response)
- `Qu^edam` → `Quaedam` (DUB. III response)
- `•""""•` and `"dif udil!'?` and `^^soiu` — marginal gloss fragments, trimmed
- `iilud` → `illud` (DUB. III final sentence)
- `iniporlat` → `importat` (DUB. V)
- `relationeni` → `relationem` (DUB. V)
- `csse` → `esse` (DUB. V)
- `quantura` → `quantum` (DUB. V)
- `tantura` → `tantum` (DUB. V)
- `largitatera` → `largitatem` (DUB. V)
- `conimunicante` → `communicante` (DUB. V)
- `inteiligendi` → `intelligendi` (DUB. V)
- `appellalio` → `appellatio` (DUB. V)
- `clans` → `dans` (DUB. V, "in quantum dans")
- `Spiritura` → `Spiritum` (DUB. V)
