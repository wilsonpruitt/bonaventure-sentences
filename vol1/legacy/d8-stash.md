---
stash: true
purpose: "Dist. VIII opening material extracted during Phase C d. 7 rebuild (2026-04-12). Previously conflated into legacy bon-sent-I-d7-dubia.md lines 105–336. Includes Lombard's Dist. VIII text (which is itself divided into Pars I and Pars II) + Bonaventure's Commentarius."
source_lines: "legacy pre-rebuild bon-sent-I-d7-dubia.md lines 105–336; raw/bonaventure_vol1_raw.txt line 30860+ (DISTINCTIO VIII)"
printed_pages: [147, 148, 149, 150]
---

# Dist. VIII opening — stashed content

Dist. VIII structure: Lombard's text is split into **Pars I** (*De veritate ac proprietate divinae essentiae*) and **Pars II**. Running heads confirm:
- p. 147: DIST. VIII. P. II.
- p. 149: DIST. VIII. P. I. DIVISIO TEXTUS.

This is unusual — Pars II's running head appears on p. 147 before Pars I's divisio on p. 149. Likely because Lombard's Cap. I of Pars I spans pp. 147–148 (the Augustine *De Trin.* V quote about *essentia*), then Bonaventure's commentary starts on p. 149 with Pars I divisio, and then Pars II content comes later. The legacy conflation mixed these together.

Raw text search: `grep -n "DISTINCTIO VIII\|COMMENTARIUS IN DISTINCTIONEM VIII\|DIVISIO TEXTUS" raw/bonaventure_vol1_raw.txt` around line 30860+.

Contains (from legacy lines 105+):
1. Lombard's Dist. VIII Pars I text (Cap. I: *De veritate ac proprietate divinae essentiae*)
2. More Pars I content + Pars II content
3. Bonaventure's Commentarius + Divisio Textus + Tractatio Quaestionum

Use when rebuilding Dist. VIII.
