# Citation pilot — hand-verification sample

> **Frozen snapshot, 2026-07-31** — regenerate identically with
> `python3.11 tools/build-citations.py --volumes 1,5 --vol1-max-d 10 --sample 50 --seed 7`.
>
> What the verdicts mean. Every row's *mechanical* claim was verified programmatically
> against the chunk files as part of a whole-ledger sweep — **815 claims, 0 failures**:
> each `chunk` target exists on disk, each `page` target really carries that printed page
> in its own `printed_pages`, each `page-multi`/`ambiguous`/`articulus` member exists, and
> each verse record is well-formed. Every row whose correctness turns on *judgment*
> (author exclusion, book inheritance, `ibid.`/chain governance, a tier-B ordinal join)
> was additionally read in its own context in the chunk file; those carry a note.
>
> ⚠️ A verdict here means **the parser did the right thing with what the chunk says.**
> It is not a claim about the plate. The two corpus findings the pilot surfaced are in
> `index-pilot-log.md` and are unfixed by design.

| # | Chunk | Section | Anchor | Class | Raw | Target | Conf | Resolution | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `bon-brev-p1-c2` | apparatus:p211-1 | p211-1 | logical | `I. Sent. d. 2.` | `I:d2` |  | distinctio | ✔ |
| 2 | `bon-brev-p1-c3` | apparatus:p211-6 | p211-6 | chain-continuation | `d. 9. q. 1.` | `bon-sent-I-d9-a1-q1` |  | chunk | ✔ chain continues Book I (`cfr. I. Sent. d. 2. q. 4; d. 9. q. 1.`) |
| 3 | `bon-brev-p1-c4` | apparatus:p212-5 | p212-5 | logical | `I. Sent. d. 22. q. 4` | `bon-sent-I-d22-a1-q4` |  | chunk | ✔ |
| 4 | `bon-brev-p2-c10` | apparatus:p228-7 | p228-7 | page | `supra pag. 225, nota 1` | `bon-brev-p2-c7+bon-brev-p2-c8` |  | page-multi | ✔ |
| 5 | `bon-brev-p2-c12` | apparatus:p230-7 | p230-7 | relative-bare | `loc. cit.` | `` |  | unresolvable | ✔ correctly unresolvable — nothing to inherit |
| 6 | `bon-brev-p2-c3` | apparatus:p221-1 | p221-1 | logical | `II. Sent. d. 14. p. I. a. 1. q. 2.` | `bon-sent-II-d14-p1-a1-q2` |  | chunk | ✔ |
| 7 | `bon-brev-p2-c4` | apparatus:p222-1 | p222-1 | logical | `II. Sent. d. 15. a. 2. q. 1.` | `bon-sent-II-d15-a2-q1` |  | chunk | ✔ |
| 8 | `bon-brev-p2-c6` | apparatus:p224-6 | p224-6 | page | `supra pag. 215, nota 4` | `bon-brev-p1-c6+bon-brev-p1-c7` |  | page-multi | ✔ |
| 9 | `bon-brev-p3-c5` | apparatus:p235-1 | p235-1 | logical | `II. Sent. d. 33. a. 3. q. 1.` | `bon-sent-II-d33-a3-q1` |  | chunk | ✔ |
| 10 | `bon-brev-p3-c8` | latin_body | p236-7 | body-ordinal | `Iacobi primo` | `Iac 1:14` | B | verse | ✔ |
| 11 | `bon-brev-p4-c1` | apparatus:p241-3 | p241-3 | logical | `III. Sent. d. 1. a. 2. q. 1.` | `bon-sent-III-d1-a2-q1` |  | chunk | ✔ |
| 12 | `bon-brev-p4-c4` | apparatus:p244-3 | p244-3 | logical | `III. Sent. d. 1. a. 2. q. 4.` | `bon-sent-III-d1-a2-q4` |  | chunk | ✔ |
| 13 | `bon-brev-p4-c4` | apparatus:p245-2 | p245-2 | logical | `I. Sent. d. 2. q. 4.` | `bon-sent-I-d2-a1-q4` |  | chunk | ✔ |
| 14 | `bon-brev-p4-c9` | apparatus:p249-7 | p249-7 | apparatus-explicit | `Luc. 22, 37` | `Luc 22:37` | A | verse | ✔ |
| 15 | `bon-brev-p4-c9` | apparatus:p249-7 | p249-7 | relative | `ibid. d. 21.` | `III:d21` |  | distinctio | ✔ `ibid.` inherits III (`III. Sent. d. 16. per totam; … ibid. d. 21.`) |
| 16 | `bon-brev-p5-c1` | apparatus:p252-2 | p252-2 | apparatus-explicit | `Iac. 1, 17` | `Iac 1:17` | A | verse | ✔ |
| 17 | `bon-brev-p5-c1` | apparatus:p253-2 | p253-2 | logical | `I. Sent. d. 14. a. 2. q. 1.` | `bon-sent-I-d14-a2-q1` |  | chunk | ✔ |
| 18 | `bon-brev-p5-c2` | apparatus:p253-8 | p253-8 | logical | `I. Sent. d. 37. p. I. a. 1. q. 1.` | `bon-sent-I-d37-p1-a1-q1` |  | chunk | ✔ |
| 19 | `bon-brev-p5-c5` | apparatus:p258-1 | p258-1 | page | `supra pag. 234, nota 4` | `bon-brev-p3-c4+bon-brev-p3-c5` |  | page-multi | ✔ |
| 20 | `bon-brev-p5-c6` | apparatus:p260-1 | p260-1 | page | `tom. III. pag. 503, nota 4` | `bon-sent-III-d23-dubia` |  | chunk | ✔ explicit `tom. III.` |
| 21 | `bon-brev-prol-s2` | apparatus:p204-3 | p204-3 | logical | `II. Sent. d. 2. p. I. a. 2. q. 3` | `bon-sent-II-d2-p1-a2-q3` |  | chunk | ✔ |
| 22 | `bon-brev-prol-s4` | apparatus:p206-6 | p206-6 | logical | `II. Sent. d. 15. a. 2. q. 1.` | `bon-sent-II-d15-a2-q1` |  | chunk | ✔ |
| 23 | `bon-sent-I-d10-a1-q2` | apparatus:12 | 12 | relative | `supra d. 1. a. 2. q. 1.` | `bon-sent-I-d1-a2-q1` |  | chunk | ✔ |
| 24 | `bon-sent-I-d10-littera` | apparatus:13 | 13 | apparatus-explicit | `Ioan. 4, 7` | `Ioan 4:7` | A | verse | ✔ |
| 25 | `bon-sent-I-d10-littera` | apparatus:2 | 2 | apparatus-explicit | `Ioan. 4, 16` | `Ioan 4:16` | A | verse | ✔ |
| 26 | `bon-sent-I-d10-littera` | apparatus:23 | 23 | apparatus-explicit | `Col. 1, 13` | `Col 1:13` | A | verse | ✔ |
| 27 | `bon-sent-I-d2-a1-q4` | apparatus:18 | 18 | authority:Albert. | `I. Sent. d. 26. a. 10.` | `` |  | excluded | ✔ |
| 28 | `bon-sent-I-d2-a1-q4` | scholion |  | logical | `II. Sent. d. 16.` | `II:d16` |  | distinctio | ✔ |
| 29 | `bon-sent-I-d2-a1-q4` | scholion |  | authority:Aegid. | `I. Sent. d. 10.` | `` |  | excluded | ✔ |
| 30 | `bon-sent-I-d2-a1-q4` | scholion |  | relative | `infra d. 3. p. I. a. 1. q. 2.` | `bon-sent-I-d3-p1-a1-q2` |  | chunk | ✔ |
| 31 | `bon-sent-I-d2-divisio` | apparatus:4 | 4 | work | `de mysterio Trinitatis` | `work:mysterio-trinitatis` |  | work | ✔ |
| 32 | `bon-sent-I-d2-dubia` | apparatus:24 | 24 | apparatus-explicit | `Gen. 1, 1` | `Gen 1:1` | A | verse | ✔ |
| 33 | `bon-sent-I-d2-dubia` | apparatus:30 | 30 | logical | `II. Sent. d. 10. a. 3. q. 2.` | `bon-sent-II-d10-a3-q2` |  | chunk | ✔ |
| 34 | `bon-sent-I-d2-littera` | apparatus:55 | 55 | apparatus-explicit | `Isai. 6, 6` | `Isai 6:6` | A | verse | ✔ |
| 35 | `bon-sent-I-d3-littera` | apparatus:45 | 45 | relative-bare | `ibid.` | `` |  | unresolvable | ✔ |
| 36 | `bon-sent-I-d3-p1-a1-q1` | scholion |  | authority:Richard. a Med. | `II. Sent. d. 24. a. 2. q. 4` | `` |  | excluded | ✔ |
| 37 | `bon-sent-I-d3-p1-a1-q1` | scholion |  | authority:Albert. | `I. Sent. d. 1. a. 15` | `` |  | excluded | ✔ |
| 38 | `bon-sent-I-d3-p1-a1-q2` | latin_body | 1 | body-ordinal | `Sapientiae decimo quarto` | `Sap 14:11` | B | verse | ✔ |
| 39 | `bon-sent-I-d3-p2-a1-q1` | scholion |  | logical | `II. Sent. d. 26. a. 1. q. 5.` | `bon-sent-II-d26-a1-q5` |  | chunk | ✔ |
| 40 | `bon-sent-I-d3-p2-a1-q2` | scholion |  | relative-bare | `ibid` | `` |  | unresolvable | ✔ |
| 41 | `bon-sent-I-d3-p2-a2-q1` | apparatus:21 | 21 | relative-bare | `ibid.` | `` |  | unresolvable | ✔ |
| 42 | `bon-sent-I-d4-dubia` | apparatus:30 | 30 | relative | `supra d. 2. q. 3.` | `bon-sent-I-d2-a1-q3` |  | chunk | ✔ |
| 43 | `bon-sent-I-d5-a2-q1` | apparatus:8 | 8 | chain-continuation | `d. 37` | `I:d37` |  | distinctio | ✔ |
| 44 | `bon-sent-I-d7-dubia` | apparatus:12 | 12 | relative | `infra d. 26.` | `I:d26` |  | distinctio | ✔ |
| 45 | `bon-sent-I-d8-littera` | apparatus:9 | 9 | apparatus-explicit | `Ioan. 16, 13` | `Ioan 16:13` | A | verse | ✔ |
| 46 | `bon-sent-I-d8-p1-a1-q1` | apparatus:6 | 6 | apparatus-explicit | `Rom. 8, 20` | `Rom 8:20` | A | verse | ✔ |
| 47 | `bon-sent-I-d8-p2-a1-q2` | scholion |  | chain-continuation | `d. 35. q. 2.` | `bon-sent-I-d35-a1-q2` |  | chunk | ✔ |
| 48 | `bon-sent-I-d8-p2-a1-q3` | apparatus:16 | 16 | relative | `supra d. 8. a. 2.` | `bon-sent-I-d8-p1-a2-q1+bon-sent-I-d8-p1-a2-q2` |  | articulus | ✔ |
| 49 | `bon-sent-I-d9-a1-q1` | scholion |  | chain-continuation | `d. 5. q. 2` | `bon-sent-I-d5-a1-q2+bon-sent-I-d5-a2-q2` |  | ambiguous | ✔ |
| 50 | `bon-sent-I-d9-a1-q2` | scholion |  | authority:Albert. | `I. Sent. d. 26. a. 7` | `` |  | excluded | ✔ |
