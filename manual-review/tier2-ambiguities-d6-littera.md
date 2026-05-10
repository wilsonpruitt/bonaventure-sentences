# d.6 littera — Tier-2 Ambiguities Log

Sweep audit 2026-05-08. **No `[?]` flags.** All OCR readings (raw lines 27551–27714) resolved cleanly during full body + apparatus rebuild from `raw/bonaventure_vol1_raw.txt`. See `manual-review/d6-scaffolds-sweep-audit-log.md` for fix log.

---

## 2026-05-10 from-scratch rebuild — new flags

`vol1/bon-sent-I-d6-littera.md` rebuilt from scratch as part of d.1-d.10 rechunk pipeline. Two `[?]` flags introduced:

- **Apparatus [^11] (Hilary, *de Synodis*)**: OCR raw line 27768 reads `Num. 39. 1. et n. 58. XXV.` — `n. 39. 1.` is anomalous (Quaracchi typically cites *de Synodis* by anathema/section number). Currently rendered `n. 39 [?]`. → Resolve via 600dpi PDF eyes-on at p.124 source-citation footer band; possibly `n. 38, 1.` or a section-number conflation.
- **Apparatus [^9] (p.124 textual variant after `genuit Filium,`)**: body marker `[^9]` placed at OCR raw line 27691 (`Filium,"`). Printed p.124 footer carries 5 textual-variant entries; entry 5 (OCR 27759-27761) covers the *Filium* addition after *bonus genuit*. The marker appears to share that footer note. Currently rendered as a cross-reference to note 8. → Resolve via 600dpi PDF p.124 footer band check.

Both flags pending PDF eyes-on as part of the d.1-d.10 polish-resolution sweep.
