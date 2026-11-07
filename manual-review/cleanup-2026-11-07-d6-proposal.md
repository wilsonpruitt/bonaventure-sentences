# D6 / W51 proposal (NOT APPLIED): bare `Vers. N; ibid. v. M` with no book in the note

**Status:** implemented behind `CITATIONS_W51=1` in `tools/build-citations.py` (default OFF). With the flag off the ledger is byte-identical to the committed `index/citations.tsv`. Wilson rules; the change relaxes ruling 57 C1's "right not to guess".

**Rule prototyped.** A coordinate `ibid.` whose note is only `Vers. N ...` (no scripture locus, no author, no other digits) takes its book, and for `ibid. v. M` its chapter, from (1) the body's scripture record anchored at that note, (2) the chunk's own lemma (`bon-ioan-cN` / `bon-cioan-cN` = John N; `bon-eccl-cN` = Eccle N; `bon-sap-cN` = Sap N), (3) the nearest scripture record before the anchor in the body, looking back past non-scripture records. Confidence is always C.

**Measured.** 43 sites of this exact shape corpus-wide (the gate's "28" counted a narrower set; *Ioannem* 21, Sentences 13, Eccl. 4, Sap. 3, Praecepta 1, *Collationes* 1). Flag on: **31 resolve, 12 stay unresolved**; ledger records 35,603 unchanged (31 `relative-bare` rows become anaphor rows); unresolved anaphora 322 -> 291; coordinate ibids honoured 360 -> 391; QA 211 unchanged.

**My confidence on the 31:** HIGH 17 (11 are `ibid. C, V` where only the book is inferred, 5 are confirmed by the quoted Latin, 1 by a parallel list) · MED-HIGH 7 · MED 4 (a chapter assumed from the lemma) · **WRONG 3** (the flag as written resolves them to a place that cannot be right).

**Recommendation.** Do not adopt the rule as written: its fallbacks are not equally safe, and 3 of 31 would be wrong silently. If Wilson wants it, adopt only (i) `ibid. C, V` inside a commentary chunk whose lemma names the book (book-only inference; all 12 such sites checked right), and (ii) `ibid. v. M` from the lemma only when the verse cannot exceed the chapter (needs a verse-count table the tool lacks). Drop the look-back fallback (it chose Matth 11:27 over I Cor 11:27 via the new D5 record `Matthaei ultimo`).

| chunk | note | raw | before (committed) | after (flag on) | my confidence | check / reason |
|---|---|---|---|---|---|---|
| bon-sent-II-d40-dubia | 4 | `ibid. 3, 22` | unresolvable | Exod 3:22 | HIGH | look-back to `Exodi duodecimo` (the [^4] anchor); Exod 12:35 is the despoiling and 3:22 / 11:2 its parallels. Right although by look-back |
| bon-sent-II-d44-a3-q1 | 4 | `ibid. v. 7` | unresolvable | unresolvable | n/a | no body join, no lemma (Sentences / Praecepta chunk) and no scripture record before the anchor: still not guessed |
| bon-sent-II-d44-a3-q1 | 9 | `ibid. v. 25` | unresolvable | unresolvable | n/a | no body join, no lemma (Sentences / Praecepta chunk) and no scripture record before the anchor: still not guessed |
| bon-sent-III-d17-a2-q1 | p371-11 | `ibid. 7, 26` | unresolvable | unresolvable | n/a | no body join, no lemma (Sentences / Praecepta chunk) and no scripture record before the anchor: still not guessed |
| bon-sent-III-d22-a1-q3 | p456-3 | `ibid. v. 21` | unresolvable | unresolvable | n/a | no body join, no lemma (Sentences / Praecepta chunk) and no scripture record before the anchor: still not guessed |
| bon-sent-III-d34-p1-dubia | 2 | `ibid. 57, 15` | unresolvable | unresolvable | n/a | no body join, no lemma (Sentences / Praecepta chunk) and no scripture record before the anchor: still not guessed |
| bon-sent-III-d36-a1-q5 | 6 | `ibid. 12, 31` | unresolvable | unresolvable | n/a | no body join, no lemma (Sentences / Praecepta chunk) and no scripture record before the anchor: still not guessed |
| bon-sent-IV-d1-p2-a2-q2 | 6 | `ibid. v. 12` | unresolvable | unresolvable | n/a | no body join, no lemma (Sentences / Praecepta chunk) and no scripture record before the anchor: still not guessed |
| bon-sent-IV-d10-p1-a1-q1 | 5 | `ibid. 11, 27` | unresolvable | Matth 11:27 | WRONG | look-back landed on the D5 record `Matthaei ultimo`; the text (`Panis, quem frangimus`, `Itaque quicumque manducaverit`) is I Cor 10:16 / 11:27. Keep unresolved |
| bon-sent-IV-d35-a1-q1 | p780-2 | `ibid. 5, 32` | unresolvable | unresolvable | n/a | no body join, no lemma (Sentences / Praecepta chunk) and no scripture record before the anchor: still not guessed |
| bon-sent-IV-d35-a1-q1 | p781-2 | `ibid. 5, 29` | unresolvable | unresolvable | n/a | no body join, no lemma (Sentences / Praecepta chunk) and no scripture record before the anchor: still not guessed |
| bon-sent-IV-d48-dubia | p997-2 | `ibid. v. 16` | unresolvable | unresolvable | n/a | no body join, no lemma (Sentences / Praecepta chunk) and no scripture record before the anchor: still not guessed |
| bon-sent-IV-d9-a2-q2 | 1 | `ibid. v. 27` | unresolvable | unresolvable | n/a | no body join, no lemma (Sentences / Praecepta chunk) and no scripture record before the anchor: still not guessed |
| bon-praec-c2 | p514-3 | `ibid. v. 21` | unresolvable | unresolvable | n/a | no body join, no lemma (Sentences / Praecepta chunk) and no scripture record before the anchor: still not guessed |
| bon-cioan-c20 | p622-7 | `ibid. v. 19` | unresolvable | Ioan 20:19 | MED-HIGH | lemma John 20; Vers. 20 and Luc. 24, 39 are the appearance of 20:19-20 |
| bon-eccl-c3-v16-22 | p36-1 | `ibid. 9, 5` | unresolvable | Eccle 9:5 | HIGH | `ibid. C, V`: only the book (Eccle) is inferred; Vers. 7 = Eccle 12:7, and 9:5 fits |
| bon-eccl-c5-v12-19 | p49-2 | `ibid. v. 5` | unresolvable | Eccle 5:5 | MED | lemma chapter 5 assumed for `v. 5` (Vers. 3) |
| bon-eccl-c5-v12-19 | p49-5 | `ibid. v. 9` | unresolvable | Eccle 5:9 | MED | lemma chapter 5 assumed for `v. 9` (Vers. 1) |
| bon-eccl-c6-v8-11 | p53-4 | `ibid. 3, 11` | unresolvable | Eccle 3:11 | HIGH | `ibid. C, V`: book only (Eccle 3:11, *cuncta fecit bona*) |
| bon-ioan-c1-v1-2 | p246-5 | `ibid. 10, 30` | unresolvable | Ioan 10:30 | HIGH | `ibid. C, V`: book only (John 10:30) |
| bon-ioan-c1-v15-18 | p255-6 | `ibid. v. 11` | unresolvable | Ioan 1:11 | MED-HIGH | lemma chapter 1 for `v. 11` (*in propria venit*) |
| bon-ioan-c1-v19-23 | p256-5 | `ibid. v. 35` | unresolvable | Ioan 1:35 | MED-HIGH | lemma chapter 1 for `v. 35`; Vers. 29 and v. 35 are the Baptist pericope |
| bon-ioan-c1-v3-5 | p248-8 | `ibid. 15, 5` | unresolvable | Ioan 15:5 | HIGH | `ibid. C, V`: book only (John 15:5) |
| bon-ioan-c1-v6-8 | p250-10 | `ibid. v. 9` | unresolvable | Ioan 1:9 | HIGH | quoted *Erat lux vera* is John 1:9 |
| bon-ioan-c10-v1-10 | p385-1 | `ibid. v. 22` | unresolvable | Ioan 10:22 | HIGH | quoted *Facta sunt autem encaenia* is John 10:22 |
| bon-ioan-c21-v18-23 | p527-7 | `ibid. v. 26` | unresolvable | Ioan 21:26 | WRONG | lemma gives `Ioan 21:26`, but John 21 has 25 verses; the place is John 13:26 (the body's *supra decimo tertio*). Keep unresolved |
| bon-ioan-c5-v1-9 | p306-6 | `ibid. 11, 4` | unresolvable | Ioan 11:4 | HIGH | `ibid. C, V`: book only (John 11:4) |
| bon-ioan-c5-v19-23 | p309-1 | `ibid. v. 38` | unresolvable | Ioan 5:38 | MED-HIGH | lemma chapter 5 for `v. 38` |
| bon-ioan-c5-v19-23 | p309-6 | `ibid. v. 25` | unresolvable | Ioan 5:25 | MED-HIGH | lemma chapter 5 for `v. 25` (the dead hearing the voice; the note then cites Luke 7:15) |
| bon-ioan-c5-v31-39 | p314-9 | `ibid. 14, 10` | unresolvable | Ioan 14:10 | HIGH | `ibid. C, V`: book only (John 14:10, 10:38) |
| bon-ioan-c5-v40-47 | p317-5 | `ibid. 1, 11` | unresolvable | Ioan 1:11 | HIGH | `ibid. C, V`: book only (John 1:11) |
| bon-ioan-c6-v1-9 | p318-12 | `ibid. v. 14` | unresolvable | Ioan 6:14 | HIGH | quoted *Illi ergo homines* is John 6:14 |
| bon-ioan-c6-v22-33 | p325-14 | `ibid. 3, 34` | unresolvable | Ioan 3:34 | HIGH | `ibid. C, V`: book only (John 3:34; 1:29) |
| bon-ioan-c6-v34-40 | p328-2 | `ibid. 5, 44` | unresolvable | Ioan 5:44 | HIGH | `ibid. C, V`: book only (John 5:44; 6:26) |
| bon-ioan-c7-v1-13 | p340-8 | `ibid. 1, 11` | unresolvable | Ioan 1:11 | HIGH | `ibid. C, V`: book only (John 1:11) |
| bon-ioan-c8-v21-30 | p360-12 | `ibid. v. 36` | unresolvable | Ioan 8:36 | MED-HIGH | lemma chapter 8 for `v. 36` (Vers. 33, *Si ergo vos Filius liberaverit*) |
| bon-ioan-c8-v21-30 | p361-1 | `ibid. v. 13` | unresolvable | Ioan 8:13 | MED | lemma chapter 8 for `v. 13`; Vers. 31 sits outside the chunk but in c. 8 |
| bon-ioan-c8-v21-30 | p361-9 | `ibid. v. 3` | unresolvable | Ioan 8:3 | MED | lemma chapter 8 for `v. 3`; Vers. 1 and v. 3 are the adulteress pericope, which fits |
| bon-ioan-c8-v31-36 | p363-3 | `ibid. v. 48` | unresolvable | Ioan 8:48 | HIGH | quoted *Responderunt ergo Iudaei* is John 8:48 |
| bon-ioan-c9-v1-11 | p372-6 | `ibid. v. 35` | unresolvable | Ioan 9:35 | HIGH | quoted *Audivit Iesus* is John 9:35 |
| bon-sap-c10 | p174-11 | `ibid. 3, 15` | unresolvable | Sap 3:15 | MED-HIGH | `ibid. C, V`: book only (Sap 3:15) |
| bon-sap-c19 | p232-8 | `ibid. v. 21` | unresolvable | Sap 19:21 | WRONG | lemma Sap 19, but Vers. 27 cannot be Sap 19 (22 verses): the note's book/chapter is a body citation the ledger lacks. Keep unresolved |
| bon-sap-c9 | p170-8 | `ibid. 8, 16` | unresolvable | Sap 8:16 | HIGH | `ibid. C, V`: book only (Sap 8:16, 17) |
