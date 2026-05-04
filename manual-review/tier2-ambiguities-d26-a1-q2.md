# Tier-2 ambiguities: bon-sent-I-d26-a1-q2

Logged during 2026-05-04 promotion of d.26 a.1 q.2 (covering OCR Quaestio II + Quaestio III, pp. 454–459).

No `[?]` flags written in body. Two-column OCR reflow was clear throughout; obvious garbles (`Riehardus`→`Richardus`, `simihter`→`similiter`, `omniiio`→`omnino`, `entitale`→`entitate`, `Sidicas`→`Si dicas`, `qiiod`→`quod`, `Itera`→`Item`, `liypostasi`→`hypostasi`, `quodsi`→`quod si`, `consubstantialis`/`connaturalis`, `chstinguit`→`distinguit`, `Riehardus`→`Richardus`, `septimo libro de Trinitate`, `solura`→`solum`, `videram`/`verura`→`verum`, `prius`/`prins`→`prius`, `Itera`→`Item`, `enira`/`enim`, `eonstituantur`→`constituantur`, `relationera`→`relationem`, `clistinguere`→`distinguere`, `Itera`→`Item`, `essentialiter`, `quararodo`→`quomodo`, `videturn`/`videtur`, `Quaero`/`Quaeritur`, `liabitudinem`→`habitudinem`, `proprie`/`proprie`, `enira`→`enim`, `noraine`→`nomine`, `dependeant`/`dependeat`, `inteliexisse`→`intellexisse`) silently corrected per CLAUDE.md OCR-cleanup rules.

Per the user's audit note, OCR's "QDAESTIO III." (raw line 3831) is treated here as an internal subdivision of the file's q2; both internal questions are rendered with their own `### QUAESTIO II.` / `### QUAESTIO III.` headings, fundamenta, conclusio, respondeo, and replies, but the file's frontmatter `quaestio: 2` and `title_la` reflect Quaestio II's title only.

P.456's scholion is rendered as its own short Scholion block following the Q.II reply set. P.459's full Scholion (I–IV) follows the Q.III reply set.

No `[?]` ambiguities flagged.

## Post-split apparatus alignment note (2026-05-04)

After the split out of QDAESTIO III content into a separate `bon-sent-I-d26-a1-q3.md` chunk, this q2 chunk retains 15 body markers and 15 apparatus entries. There is a known minor mis-alignment between body markers [^14]/[^15] and apparatus entries [^14]/[^15]:

- Body [^14] at *prima tria obiecta* — apparatus [^14] (sense-note "Sensus est: sicut alia praedicamenta...") aligns correctly.
- Body [^15] at *etiam cum* — but apparatus [^15] content discusses `deest *prima*. M: *contra* pro *circa*. Y: *secundum* pro *aliud*` — i.e., variants on "prima/circa/aliud" which are in the *same paragraph* as [^14], not at [^15]'s "etiam cum" anchor.

Most likely Quaracchi placed TWO separate footnote markers in the "prima tria obiecta circa solutionem oppositorum...aliud..." sentence: one at "prima" (sense-note), one at "aliud" or "circa" (variants). The original auto-chunk inserted only one body marker, so [^15]'s content effectively orphans onto the next anchor. Resolution requires eyes-on-PDF read of p. 456 footer.
