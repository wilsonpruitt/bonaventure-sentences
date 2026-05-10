# Wave 9b Tier C — Apparatus-Count Triage

Triage of 154 chunks at audit diff +5 to +19 (d.1–d.40, Tier-2-complete chunks only).

Adjusted diff = raw audit diff − (chapter rubrics + Scholion headers + italicized work-citations + lettered series). Noise sources are the Lesson-10 false-positive contributors documented in `d1-d4-tier2-promotion-log.md`.

**Buckets:**
- **A — metadata-only candidate** (adjusted ≤ 2): 2 chunks. Batch-update status string after eyes-on confirmation. No full agent dispatch.
- **B — small undercoverage** (adjusted 3–8): 78 chunks. Short-prompt agent per chunk.
- **C — large undercoverage** (adjusted > 8): 74 chunks. Full disposition agent like Tier B.

Reminder: the audit is a triage signal, never ground truth (Lesson 10). Bucket A in particular still warrants eyes-on the printed footer band before promoting the status string. The adjusted-diff calculation is itself a heuristic — it may over- or under-subtract.

| Chunk | d | Type | Pages | Raw | Chunk | Diff | Rubrics | Schol | Cites | Lett | Noise | Adj | Bucket |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `bon-sent-I-d32-divisio` | 32 | divisio | [554, 555, 556] | 11 | 6 | +5 | 3 | 0 | 0 | 0 | 3 | 2 | **A** |
| `bon-sent-I-d23-littera` | 23 | littera | [402, 403, 404] | 32 | 27 | +5 | 6 | 0 | 0 | 0 | 6 | 0 | **A** |
| `bon-sent-I-d35-divisio` | 35 | divisio | [600] | 15 | 4 | +11 | 3 | 0 | 0 | 0 | 3 | 8 | **B** |
| `bon-sent-I-d31-p2-a2-q1` | 31 | quaestio | [545, 546] | 14 | 5 | +9 | 0 | 1 | 0 | 0 | 1 | 8 | **B** |
| `bon-sent-I-d32-a2-q2` | 32 | quaestio | [563, 564] | 19 | 10 | +9 | 0 | 1 | 0 | 0 | 1 | 8 | **B** |
| `bon-sent-I-d37-p1-a3-q1` | 37 | quaestio | [646, 647] | 20 | 11 | +9 | 0 | 1 | 0 | 0 | 1 | 8 | **B** |
| `bon-sent-I-d4-a1-q4` | 4 | quaestio | [103, 104] | 16 | 7 | +9 | 0 | 1 | 0 | 0 | 1 | 8 | **B** |
| `bon-sent-I-d16-a1-q2` | 16 | quaestio | [281, 282] | 30 | 22 | +8 | 0 | 0 | 0 | 0 | 0 | 8 | **B** |
| `bon-sent-I-d20-a2-q1` | 20 | quaestio | [371, 372, 373] | 25 | 17 | +8 | 0 | 0 | 0 | 0 | 0 | 8 | **B** |
| `bon-sent-I-d23-a2-q3` | 23 | quaestio | [414, 415, 416] | 21 | 13 | +8 | 0 | 0 | 0 | 0 | 0 | 8 | **B** |
| `bon-sent-I-d39-littera` | 39 | littera | [682, 683] | 16 | 8 | +8 | 0 | 0 | 0 | 0 | 0 | 8 | **B** |
| `bon-sent-I-d40-a3-q1` | 40 | quaestio | [714, 715] | 23 | 15 | +8 | 0 | 0 | 0 | 0 | 0 | 8 | **B** |
| `bon-sent-I-d34-dubia` | 34 | dubia | [595, 596, 597] | 28 | 18 | +10 | 1 | 2 | 0 | 0 | 3 | 7 | **B** |
| `bon-sent-I-d8-littera` | 8 | littera | [147, 148, 149] | 42 | 32 | +10 | 3 | 0 | 0 | 0 | 3 | 7 | **B** |
| `bon-sent-I-d26-divisio` | 26 | divisio | [450, 451] | 13 | 4 | +9 | 2 | 0 | 0 | 0 | 2 | 7 | **B** |
| `bon-sent-I-d27-p1-a1-q4` | 27 | quaestio | [478, 479] | 22 | 14 | +8 | 0 | 1 | 0 | 0 | 1 | 7 | **B** |
| `bon-sent-I-d27-p1-divisio` | 27 | divisio | [466, 467] | 11 | 3 | +8 | 1 | 0 | 0 | 0 | 1 | 7 | **B** |
| `bon-sent-I-d27-p2-a1-q4` | 27 | quaestio | [489, 490, 491] | 32 | 24 | +8 | 1 | 0 | 0 | 0 | 1 | 7 | **B** |
| `bon-sent-I-d3-p2-a1-q2` | 3 | quaestio | [82, 83, 84] | 23 | 15 | +8 | 0 | 1 | 0 | 0 | 1 | 7 | **B** |
| `bon-sent-I-d31-p2-divisio` | 31 | divisio | [540, 541] | 9 | 1 | +8 | 0 | 1 | 0 | 0 | 1 | 7 | **B** |
| `bon-sent-I-d36-a1-q1` | 36 | quaestio | [620, 621] | 22 | 14 | +8 | 1 | 0 | 0 | 0 | 1 | 7 | **B** |
| `bon-sent-I-d8-p2-a1-q4` | 8 | quaestio | [173, 174] | 14 | 6 | +8 | 1 | 0 | 0 | 0 | 1 | 7 | **B** |
| `bon-sent-I-d1-a3-q2` | 1 | quaestio | [39, 40, 41, 42] | 31 | 24 | +7 | 0 | 0 | 0 | 0 | 0 | 7 | **B** |
| `bon-sent-I-d16-a1-q1` | 16 | quaestio | [279, 280] | 22 | 15 | +7 | 0 | 0 | 0 | 0 | 0 | 7 | **B** |
| `bon-sent-I-d19-p1-a1-q4` | 19 | quaestio | [347, 348, 349, 350] | 37 | 30 | +7 | 0 | 0 | 0 | 0 | 0 | 7 | **B** |
| `bon-sent-I-d2-divisio` | 2 | divisio | [49, 50] | 13 | 6 | +7 | 0 | 0 | 0 | 0 | 0 | 7 | **B** |
| `bon-sent-I-d21-a1-q2` | 21 | quaestio | [381, 382, 383] | 21 | 14 | +7 | 0 | 0 | 0 | 0 | 0 | 7 | **B** |
| `bon-sent-I-d25-a1-q1` | 25 | quaestio | [435, 436, 437, 438] | 34 | 27 | +7 | 0 | 0 | 0 | 0 | 0 | 7 | **B** |
| `bon-sent-I-d27-p2-a1-q1` | 27 | quaestio | [481, 482, 483, 484] | 31 | 24 | +7 | 0 | 0 | 0 | 0 | 0 | 7 | **B** |
| `bon-sent-I-d31-p2-a2-q2` | 31 | quaestio | [546, 547, 548] | 18 | 11 | +7 | 0 | 0 | 0 | 0 | 0 | 7 | **B** |
| `bon-sent-I-d32-a1-q2` | 32 | quaestio | [559, 560, 561] | 15 | 8 | +7 | 0 | 0 | 0 | 0 | 0 | 7 | **B** |
| `bon-sent-I-d4-a1-q1` | 4 | quaestio | [97, 98, 99] | 22 | 15 | +7 | 0 | 0 | 0 | 0 | 0 | 7 | **B** |
| `bon-sent-I-d6-a1-q3` | 6 | quaestio | [129, 130] | 12 | 5 | +7 | 0 | 0 | 0 | 0 | 0 | 7 | **B** |
| `bon-sent-I-d9-divisio` | 9 | divisio | [179, 180] | 12 | 5 | +7 | 0 | 0 | 0 | 0 | 0 | 7 | **B** |
| `bon-sent-I-d39-a2-q1` | 39 | quaestio | [692, 693] | 14 | 6 | +8 | 1 | 1 | 0 | 0 | 2 | 6 | **B** |
| `bon-sent-I-d40-a2-q1` | 40 | quaestio | [706, 707, 708, 709, 710] | 36 | 28 | +8 | 0 | 2 | 0 | 0 | 2 | 6 | **B** |
| `bon-sent-I-d2-a1-q3` | 2 | quaestio | [54, 55, 56] | 19 | 12 | +7 | 0 | 1 | 0 | 0 | 1 | 6 | **B** |
| `bon-sent-I-d23-a1-q2` | 23 | quaestio | [405, 406, 407] | 20 | 13 | +7 | 0 | 1 | 0 | 0 | 1 | 6 | **B** |
| `bon-sent-I-d29-a1-q2` | 29 | quaestio | [510, 511, 512] | 17 | 10 | +7 | 0 | 1 | 0 | 0 | 1 | 6 | **B** |
| `bon-sent-I-d3-p2-a2-q1` | 3 | quaestio | [88, 89, 90] | 33 | 26 | +7 | 0 | 1 | 0 | 0 | 1 | 6 | **B** |
| `bon-sent-I-d31-p1-a1-q1` | 31 | quaestio | [532, 533, 534, 535] | 14 | 7 | +7 | 1 | 0 | 0 | 0 | 1 | 6 | **B** |
| `bon-sent-I-d32-a2-q1` | 32 | quaestio | [561, 562, 563] | 21 | 14 | +7 | 0 | 1 | 0 | 0 | 1 | 6 | **B** |
| `bon-sent-I-d32-dubia` | 32 | dubia | [565, 566, 567] | 29 | 22 | +7 | 0 | 1 | 0 | 0 | 1 | 6 | **B** |
| `bon-sent-I-d35-a1-q4` | 35 | quaestio | [609, 610] | 20 | 13 | +7 | 0 | 1 | 0 | 0 | 1 | 6 | **B** |
| `bon-sent-I-d5-dubia` | 5 | dubia | [119, 120, 121, 122] | 42 | 35 | +7 | 0 | 1 | 0 | 0 | 1 | 6 | **B** |
| `bon-sent-I-d1-a1-q1` | 1 | quaestio | [30, 31, 32] | 28 | 22 | +6 | 0 | 0 | 0 | 0 | 0 | 6 | **B** |
| `bon-sent-I-d11-a1-q1` | 11 | quaestio | [209, 210, 211, 212, 213] | 57 | 51 | +6 | 0 | 0 | 0 | 0 | 0 | 6 | **B** |
| `bon-sent-I-d12-littera` | 12 | littera | [218, 219] | 24 | 18 | +6 | 0 | 0 | 0 | 0 | 0 | 6 | **B** |
| `bon-sent-I-d13-divisio` | 13 | divisio | [230] | 11 | 5 | +6 | 0 | 0 | 0 | 0 | 0 | 6 | **B** |
| `bon-sent-I-d15-p1-a1-q3` | 15 | quaestio | [262, 263, 264] | 27 | 21 | +6 | 0 | 0 | 0 | 0 | 0 | 6 | **B** |
| `bon-sent-I-d21-divisio` | 21 | divisio | [378, 379] | 11 | 5 | +6 | 0 | 0 | 0 | 0 | 0 | 6 | **B** |
| `bon-sent-I-d28-a1-q2` | 28 | quaestio | [499, 500] | 15 | 9 | +6 | 0 | 0 | 0 | 0 | 0 | 6 | **B** |
| `bon-sent-I-d29-dubia` | 29 | dubia | [516, 517, 518, 519] | 29 | 23 | +6 | 0 | 0 | 0 | 0 | 0 | 6 | **B** |
| `bon-sent-I-d40-a4-q1` | 40 | quaestio | [716, 717] | 14 | 8 | +6 | 0 | 0 | 0 | 0 | 0 | 6 | **B** |
| `bon-sent-I-d27-p1-a1-q2` | 27 | quaestio | [468, 469, 470, 471, 472, 473, 474] | 57 | 48 | +9 | 0 | 4 | 0 | 0 | 4 | 5 | **B** |
| `bon-sent-I-d26-a1-q3` | 26 | quaestio | [456, 457, 458, 459] | 31 | 23 | +8 | 1 | 2 | 0 | 0 | 3 | 5 | **B** |
| `bon-sent-I-d34-divisio` | 34 | divisio | [585] | 12 | 4 | +8 | 3 | 0 | 0 | 0 | 3 | 5 | **B** |
| `bon-sent-I-d29-a2-q2` | 29 | quaestio | [515, 516] | 16 | 9 | +7 | 0 | 2 | 0 | 0 | 2 | 5 | **B** |
| `bon-sent-I-d7-a1-q1` | 7 | quaestio | [135, 136, 137] | 43 | 36 | +7 | 1 | 1 | 0 | 0 | 2 | 5 | **B** |
| `bon-sent-I-d11-littera` | 11 | littera | [207, 208] | 24 | 18 | +6 | 1 | 0 | 0 | 0 | 1 | 5 | **B** |
| `bon-sent-I-d13-a1-q1` | 13 | quaestio | [230, 231, 232] | 20 | 14 | +6 | 0 | 1 | 0 | 0 | 1 | 5 | **B** |
| `bon-sent-I-d20-a1-q1` | 20 | quaestio | [368, 369, 370] | 21 | 15 | +6 | 0 | 1 | 0 | 0 | 1 | 5 | **B** |
| `bon-sent-I-d24-a1-q1` | 24 | quaestio | [420, 421, 422] | 31 | 25 | +6 | 0 | 1 | 0 | 0 | 1 | 5 | **B** |
| `bon-sent-I-d28-divisio` | 28 | divisio | [495, 496] | 10 | 4 | +6 | 1 | 0 | 0 | 0 | 1 | 5 | **B** |
| `bon-sent-I-d35-a1-q5` | 35 | quaestio | [611, 612] | 16 | 10 | +6 | 0 | 1 | 0 | 0 | 1 | 5 | **B** |
| `bon-sent-I-d12-a1-q2` | 12 | quaestio | [221, 222, 223] | 18 | 13 | +5 | 0 | 0 | 0 | 0 | 0 | 5 | **B** |
| `bon-sent-I-d15-p1-a1-q1` | 15 | quaestio | [259, 260, 261] | 22 | 17 | +5 | 0 | 0 | 0 | 0 | 0 | 5 | **B** |
| `bon-sent-I-d17-p1-divisio` | 17 | divisio | [291] | 10 | 5 | +5 | 0 | 0 | 0 | 0 | 0 | 5 | **B** |
| `bon-sent-I-d21-a2-q1` | 21 | quaestio | [383, 384, 385] | 19 | 14 | +5 | 0 | 0 | 0 | 0 | 0 | 5 | **B** |
| `bon-sent-I-d24-a2-q2` | 24 | quaestio | [426, 427, 428] | 21 | 16 | +5 | 0 | 0 | 0 | 0 | 0 | 5 | **B** |
| `bon-sent-I-d26-dubia` | 26 | dubia | [462, 463, 464] | 28 | 23 | +5 | 0 | 0 | 0 | 0 | 0 | 5 | **B** |
| `bon-sent-I-d27-p2-a1-q2` | 27 | quaestio | [482, 483, 484, 485, 486] | 28 | 23 | +5 | 0 | 0 | 0 | 0 | 0 | 5 | **B** |
| `bon-sent-I-d28-dubia` | 28 | dubia | [504, 505] | 22 | 17 | +5 | 0 | 0 | 0 | 0 | 0 | 5 | **B** |
| `bon-sent-I-d37-p2-a1-q3` | 37 | quaestio | [655, 656, 657] | 14 | 9 | +5 | 0 | 0 | 0 | 0 | 0 | 5 | **B** |
| `bon-sent-I-d5-a2-q2` | 5 | quaestio | [117, 118] | 10 | 5 | +5 | 0 | 0 | 0 | 0 | 0 | 5 | **B** |
| `bon-sent-I-d7-divisio` | 7 | divisio | [134, 135] | 13 | 8 | +5 | 0 | 0 | 0 | 0 | 0 | 5 | **B** |
| `bon-sent-I-d10-a1-q3` | 10 | quaestio | [193, 194] | 13 | 8 | +5 | 0 | 1 | 0 | 0 | 1 | 4 | **B** |
| `bon-sent-I-d33-a1-q2` | 33 | quaestio | [574, 575, 576] | 18 | 13 | +5 | 0 | 1 | 0 | 0 | 1 | 4 | **B** |
| `bon-sent-I-d37-p1-a1-q2` | 37 | quaestio | [640, 641] | 15 | 10 | +5 | 0 | 1 | 0 | 0 | 1 | 4 | **B** |
| `bon-sent-I-d40-a3-q2` | 40 | quaestio | [715, 716] | 14 | 9 | +5 | 0 | 1 | 0 | 0 | 1 | 4 | **B** |
| `bon-sent-I-d4-dubia` | 4 | dubia | [105, 106, 107] | 34 | 15 | +19 | 0 | 0 | 0 | 0 | 0 | 19 | **C** |
| `bon-sent-I-d37-p1-a1-q1` | 37 | quaestio | [638, 639] | 29 | 10 | +19 | 2 | 0 | 0 | 0 | 2 | 17 | **C** |
| `bon-sent-I-d2-a1-q4` | 2 | quaestio | [56, 57, 58] | 28 | 11 | +17 | 0 | 0 | 0 | 0 | 0 | 17 | **C** |
| `bon-sent-I-d3-littera` | 3 | littera | [62, 63, 64, 65, 66] | 61 | 43 | +18 | 2 | 0 | 0 | 0 | 2 | 16 | **C** |
| `bon-sent-I-d37-p2-a2-q1` | 37 | quaestio | [658, 659] | 29 | 11 | +18 | 0 | 2 | 0 | 0 | 2 | 16 | **C** |
| `bon-sent-I-d26-a1-q1` | 26 | quaestio | [451, 452, 453, 454] | 36 | 19 | +17 | 0 | 1 | 0 | 0 | 1 | 16 | **C** |
| `bon-sent-I-d27-p2-dubia` | 27 | dubia | [491, 492] | 24 | 7 | +17 | 1 | 0 | 0 | 0 | 1 | 16 | **C** |
| `bon-sent-I-d5-a2-q1` | 5 | quaestio | [115, 116, 117] | 24 | 7 | +17 | 0 | 1 | 0 | 0 | 1 | 16 | **C** |
| `bon-sent-I-d10-a1-q1` | 10 | quaestio | [194, 195, 196] | 28 | 12 | +16 | 0 | 0 | 0 | 0 | 0 | 16 | **C** |
| `bon-sent-I-d33-a1-q1` | 33 | quaestio | [570, 571, 572, 573] | 40 | 24 | +16 | 0 | 0 | 0 | 0 | 0 | 16 | **C** |
| `bon-sent-I-d38-a2-q1` | 38 | quaestio | [673, 674, 675, 676] | 30 | 14 | +16 | 0 | 0 | 0 | 0 | 0 | 16 | **C** |
| `bon-sent-I-d8-p2-a1-q1` | 8 | quaestio | [166, 167, 168] | 23 | 7 | +16 | 0 | 0 | 0 | 0 | 0 | 16 | **C** |
| `bon-sent-I-d25-littera` | 25 | littera | [432, 433, 434] | 43 | 24 | +19 | 4 | 0 | 0 | 0 | 4 | 15 | **C** |
| `bon-sent-I-d7-a1-q4` | 7 | quaestio | [143, 144] | 20 | 3 | +17 | 0 | 2 | 0 | 0 | 2 | 15 | **C** |
| `bon-sent-I-d37-p1-divisio` | 37 | divisio | [637] | 17 | 1 | +16 | 1 | 0 | 0 | 0 | 1 | 15 | **C** |
| `bon-sent-I-d28-a1-q1` | 28 | quaestio | [497, 498, 499] | 36 | 21 | +15 | 0 | 0 | 0 | 0 | 0 | 15 | **C** |
| `bon-sent-I-d29-divisio` | 29 | divisio | [507, 508] | 18 | 3 | +15 | 0 | 0 | 0 | 0 | 0 | 15 | **C** |
| `bon-sent-I-d40-a1-q2` | 40 | quaestio | [704, 705] | 22 | 7 | +15 | 0 | 0 | 0 | 0 | 0 | 15 | **C** |
| `bon-sent-I-d31-p1-a1-q2` | 31 | quaestio | [535, 536, 537, 538] | 34 | 18 | +16 | 1 | 1 | 0 | 0 | 2 | 14 | **C** |
| `bon-sent-I-d20-littera` | 20 | littera | [366, 367] | 28 | 13 | +15 | 1 | 0 | 0 | 0 | 1 | 14 | **C** |
| `bon-sent-I-d34-a1-q1` | 34 | quaestio | [585, 586, 587, 588] | 31 | 16 | +15 | 1 | 0 | 0 | 0 | 1 | 14 | **C** |
| `bon-sent-I-d37-p1-a2-q1` | 37 | quaestio | [642, 643] | 29 | 14 | +15 | 0 | 1 | 0 | 0 | 1 | 14 | **C** |
| `bon-sent-I-d8-p1-a2-q2` | 8 | quaestio | [158, 159, 160, 161] | 53 | 38 | +15 | 0 | 1 | 0 | 0 | 1 | 14 | **C** |
| `bon-sent-I-d25-a2-q1` | 25 | quaestio | [441, 442, 443, 444] | 35 | 21 | +14 | 0 | 0 | 0 | 0 | 0 | 14 | **C** |
| `bon-sent-I-d29-a2-q1` | 29 | quaestio | [512, 513, 514] | 33 | 19 | +14 | 0 | 0 | 0 | 0 | 0 | 14 | **C** |
| `bon-sent-I-d32-a1-q1` | 32 | quaestio | [555, 556, 557] | 27 | 13 | +14 | 0 | 0 | 0 | 0 | 0 | 14 | **C** |
| `bon-sent-I-d37-p1-a2-q2` | 37 | quaestio | [644, 645] | 22 | 8 | +14 | 0 | 0 | 0 | 0 | 0 | 14 | **C** |
| `bon-sent-I-d37-p1-dubia` | 37 | dubia | [649, 650, 651] | 30 | 16 | +14 | 0 | 0 | 0 | 0 | 0 | 14 | **C** |
| `bon-sent-I-d38-a2-q2` | 38 | quaestio | [676, 677, 678, 679] | 24 | 10 | +14 | 0 | 0 | 0 | 0 | 0 | 14 | **C** |
| `bon-sent-I-d5-littera` | 5 | littera | [108, 109, 110] | 44 | 28 | +16 | 3 | 0 | 0 | 0 | 3 | 13 | **C** |
| `bon-sent-I-d31-p2-a1-q1` | 31 | quaestio | [541, 542] | 29 | 15 | +14 | 1 | 0 | 0 | 0 | 1 | 13 | **C** |
| `bon-sent-I-d34-littera` | 34 | littera | [582, 583, 584] | 35 | 21 | +14 | 1 | 0 | 0 | 0 | 1 | 13 | **C** |
| `bon-sent-I-d25-a1-q2` | 25 | quaestio | [439, 440, 441] | 30 | 17 | +13 | 0 | 0 | 0 | 0 | 0 | 13 | **C** |
| `bon-sent-I-d27-p1-a1-q1` | 27 | quaestio | [467, 468] | 19 | 6 | +13 | 0 | 0 | 0 | 0 | 0 | 13 | **C** |
| `bon-sent-I-d27-p2-a1-q3` | 27 | quaestio | [487, 488] | 20 | 7 | +13 | 0 | 0 | 0 | 0 | 0 | 13 | **C** |
| `bon-sent-I-d29-a1-q1` | 29 | quaestio | [508, 509, 510] | 28 | 15 | +13 | 0 | 0 | 0 | 0 | 0 | 13 | **C** |
| `bon-sent-I-d3-p1-a1-q1` | 3 | quaestio | [67, 68, 69, 70] | 41 | 28 | +13 | 0 | 0 | 0 | 0 | 0 | 13 | **C** |
| `bon-sent-I-d31-p2-dubia` | 31 | dubia | [549, 550, 551, 552] | 38 | 25 | +13 | 0 | 0 | 0 | 0 | 0 | 13 | **C** |
| `bon-sent-I-d8-p2-dubia` | 8 | dubia | [175, 176] | 19 | 6 | +13 | 0 | 0 | 0 | 0 | 0 | 13 | **C** |
| `bon-sent-I-d12-divisio` | 12 | divisio | [219, 220] | 14 | 2 | +12 | 0 | 0 | 0 | 0 | 0 | 12 | **C** |
| `bon-sent-I-d2-a1-q1` | 2 | quaestio | [50, 51, 52] | 30 | 18 | +12 | 0 | 0 | 0 | 0 | 0 | 12 | **C** |
| `bon-sent-I-d25-divisio` | 25 | divisio | [434, 435] | 15 | 3 | +12 | 0 | 0 | 0 | 0 | 0 | 12 | **C** |
| `bon-sent-I-d26-littera` | 26 | littera | [447, 448, 449, 450] | 38 | 22 | +16 | 5 | 0 | 0 | 0 | 5 | 11 | **C** |
| `bon-sent-I-d35-littera` | 35 | littera | [597, 598] | 28 | 15 | +13 | 1 | 1 | 0 | 0 | 2 | 11 | **C** |
| `bon-sent-I-d31-p2-a1-q2` | 31 | quaestio | [542, 543] | 25 | 13 | +12 | 0 | 1 | 0 | 0 | 1 | 11 | **C** |
| `bon-sent-I-d39-a2-q3` | 39 | quaestio | [695, 696, 697] | 22 | 10 | +12 | 0 | 1 | 0 | 0 | 1 | 11 | **C** |
| `bon-sent-I-d7-a1-q3` | 7 | quaestio | [141, 142] | 17 | 5 | +12 | 0 | 1 | 0 | 0 | 1 | 11 | **C** |
| `bon-sent-I-d24-a2-q1` | 24 | quaestio | [425, 426] | 21 | 10 | +11 | 0 | 0 | 0 | 0 | 0 | 11 | **C** |
| `bon-sent-I-d37-p1-a3-q2` | 37 | quaestio | [648, 649] | 21 | 10 | +11 | 0 | 0 | 0 | 0 | 0 | 11 | **C** |
| `bon-sent-I-d37-p2-dubia` | 37 | dubia | [665, 666] | 22 | 11 | +11 | 0 | 0 | 0 | 0 | 0 | 11 | **C** |
| `bon-sent-I-d38-littera` | 38 | littera | [667, 668] | 19 | 8 | +11 | 0 | 0 | 0 | 0 | 0 | 11 | **C** |
| `bon-sent-I-d6-divisio` | 6 | divisio | [124, 125] | 13 | 2 | +11 | 0 | 0 | 0 | 0 | 0 | 11 | **C** |
| `bon-sent-I-d15-p2-a1-q2` | 15 | quaestio | [271, 272] | 21 | 10 | +11 | 0 | 1 | 0 | 0 | 1 | 10 | **C** |
| `bon-sent-I-d6-a1-q2` | 6 | quaestio | [127, 128] | 18 | 7 | +11 | 0 | 1 | 0 | 0 | 1 | 10 | **C** |
| `bon-sent-I-d15-p1-divisio` | 15 | divisio | [288, 289] | 11 | 1 | +10 | 0 | 0 | 0 | 0 | 0 | 10 | **C** |
| `bon-sent-I-d30-a1-q1` | 30 | quaestio | [521, 522, 523, 524] | 22 | 12 | +10 | 0 | 0 | 0 | 0 | 0 | 10 | **C** |
| `bon-sent-I-d33-divisio` | 33 | divisio | [569, 570] | 16 | 6 | +10 | 0 | 0 | 0 | 0 | 0 | 10 | **C** |
| `bon-sent-I-d37-p2-a2-q2` | 37 | quaestio | [660, 661] | 18 | 8 | +10 | 0 | 0 | 0 | 0 | 0 | 10 | **C** |
| `bon-sent-I-d5-a1-q2` | 5 | quaestio | [114, 115] | 18 | 8 | +10 | 0 | 0 | 0 | 0 | 0 | 10 | **C** |
| `bon-sent-I-d6-a1-q1` | 6 | quaestio | [125, 126] | 16 | 6 | +10 | 0 | 0 | 0 | 0 | 0 | 10 | **C** |
| `bon-sent-I-d8-p1-divisio` | 8 | divisio | [149, 150] | 14 | 4 | +10 | 0 | 0 | 0 | 0 | 0 | 10 | **C** |
| `bon-sent-I-d8-p2-divisio` | 8 | divisio | [165, 166] | 12 | 2 | +10 | 0 | 0 | 0 | 0 | 0 | 10 | **C** |
| `bon-sent-I-d9-dubia` | 9 | dubia | [187, 188, 189, 190, 191, 192] | 71 | 61 | +10 | 0 | 0 | 0 | 0 | 0 | 10 | **C** |
| `bon-sent-I-d19-p1-dubia` | 19 | dubia | [350, 351, 352, 353] | 47 | 37 | +10 | 0 | 1 | 0 | 0 | 1 | 9 | **C** |
| `bon-sent-I-d8-p1-a2-q1` | 8 | quaestio | [156, 157, 158] | 19 | 9 | +10 | 0 | 1 | 0 | 0 | 1 | 9 | **C** |
| `bon-sent-I-d19-p2-a1-q4` | 19 | quaestio | [362, 363, 364] | 37 | 28 | +9 | 0 | 0 | 0 | 0 | 0 | 9 | **C** |
| `bon-sent-I-d24-a3-q2` | 24 | quaestio | [430, 431] | 20 | 11 | +9 | 0 | 0 | 0 | 0 | 0 | 9 | **C** |
| `bon-sent-I-d24-divisio` | 24 | divisio | [419] | 13 | 4 | +9 | 0 | 0 | 0 | 0 | 0 | 9 | **C** |
| `bon-sent-I-d24-littera` | 24 | littera | [418, 419] | 25 | 16 | +9 | 0 | 0 | 0 | 0 | 0 | 9 | **C** |
| `bon-sent-I-d33-a1-q3` | 33 | quaestio | [576, 577, 578] | 21 | 12 | +9 | 0 | 0 | 0 | 0 | 0 | 9 | **C** |
| `bon-sent-I-d36-a3-q1` | 36 | quaestio | [625, 626, 627] | 22 | 13 | +9 | 0 | 0 | 0 | 0 | 0 | 9 | **C** |
| `bon-sent-I-d37-p2-a2-q3` | 37 | quaestio | [662, 663, 664, 665] | 22 | 13 | +9 | 0 | 0 | 0 | 0 | 0 | 9 | **C** |
| `bon-sent-I-d8-p1-a1-q1` | 8 | quaestio | [150, 151, 152] | 31 | 22 | +9 | 0 | 0 | 0 | 0 | 0 | 9 | **C** |
| `bon-sent-I-d8-p1-dubia` | 8 | dubia | [161, 162, 163, 164, 165] | 19 | 10 | +9 | 0 | 0 | 0 | 0 | 0 | 9 | **C** |

## Bucket A

- `bon-sent-I-d32-divisio` — divisio, pp. [554, 555, 556], raw=11 chunk=6 diff=+5 adj=2
- `bon-sent-I-d23-littera` — littera, pp. [402, 403, 404], raw=32 chunk=27 diff=+5 adj=0

## Bucket B

- `bon-sent-I-d35-divisio` — divisio, pp. [600], raw=15 chunk=4 diff=+11 adj=8
- `bon-sent-I-d31-p2-a2-q1` — quaestio, pp. [545, 546], raw=14 chunk=5 diff=+9 adj=8
- `bon-sent-I-d32-a2-q2` — quaestio, pp. [563, 564], raw=19 chunk=10 diff=+9 adj=8
- `bon-sent-I-d37-p1-a3-q1` — quaestio, pp. [646, 647], raw=20 chunk=11 diff=+9 adj=8
- `bon-sent-I-d4-a1-q4` — quaestio, pp. [103, 104], raw=16 chunk=7 diff=+9 adj=8
- `bon-sent-I-d16-a1-q2` — quaestio, pp. [281, 282], raw=30 chunk=22 diff=+8 adj=8
- `bon-sent-I-d20-a2-q1` — quaestio, pp. [371, 372, 373], raw=25 chunk=17 diff=+8 adj=8
- `bon-sent-I-d23-a2-q3` — quaestio, pp. [414, 415, 416], raw=21 chunk=13 diff=+8 adj=8
- `bon-sent-I-d39-littera` — littera, pp. [682, 683], raw=16 chunk=8 diff=+8 adj=8
- `bon-sent-I-d40-a3-q1` — quaestio, pp. [714, 715], raw=23 chunk=15 diff=+8 adj=8
- `bon-sent-I-d34-dubia` — dubia, pp. [595, 596, 597], raw=28 chunk=18 diff=+10 adj=7
- `bon-sent-I-d8-littera` — littera, pp. [147, 148, 149], raw=42 chunk=32 diff=+10 adj=7
- `bon-sent-I-d26-divisio` — divisio, pp. [450, 451], raw=13 chunk=4 diff=+9 adj=7
- `bon-sent-I-d27-p1-a1-q4` — quaestio, pp. [478, 479], raw=22 chunk=14 diff=+8 adj=7
- `bon-sent-I-d27-p1-divisio` — divisio, pp. [466, 467], raw=11 chunk=3 diff=+8 adj=7
- `bon-sent-I-d27-p2-a1-q4` — quaestio, pp. [489, 490, 491], raw=32 chunk=24 diff=+8 adj=7
- `bon-sent-I-d3-p2-a1-q2` — quaestio, pp. [82, 83, 84], raw=23 chunk=15 diff=+8 adj=7
- `bon-sent-I-d31-p2-divisio` — divisio, pp. [540, 541], raw=9 chunk=1 diff=+8 adj=7
- `bon-sent-I-d36-a1-q1` — quaestio, pp. [620, 621], raw=22 chunk=14 diff=+8 adj=7
- `bon-sent-I-d8-p2-a1-q4` — quaestio, pp. [173, 174], raw=14 chunk=6 diff=+8 adj=7
- `bon-sent-I-d1-a3-q2` — quaestio, pp. [39, 40, 41, 42], raw=31 chunk=24 diff=+7 adj=7
- `bon-sent-I-d16-a1-q1` — quaestio, pp. [279, 280], raw=22 chunk=15 diff=+7 adj=7
- `bon-sent-I-d19-p1-a1-q4` — quaestio, pp. [347, 348, 349, 350], raw=37 chunk=30 diff=+7 adj=7
- `bon-sent-I-d2-divisio` — divisio, pp. [49, 50], raw=13 chunk=6 diff=+7 adj=7
- `bon-sent-I-d21-a1-q2` — quaestio, pp. [381, 382, 383], raw=21 chunk=14 diff=+7 adj=7
- `bon-sent-I-d25-a1-q1` — quaestio, pp. [435, 436, 437, 438], raw=34 chunk=27 diff=+7 adj=7
- `bon-sent-I-d27-p2-a1-q1` — quaestio, pp. [481, 482, 483, 484], raw=31 chunk=24 diff=+7 adj=7
- `bon-sent-I-d31-p2-a2-q2` — quaestio, pp. [546, 547, 548], raw=18 chunk=11 diff=+7 adj=7
- `bon-sent-I-d32-a1-q2` — quaestio, pp. [559, 560, 561], raw=15 chunk=8 diff=+7 adj=7
- `bon-sent-I-d4-a1-q1` — quaestio, pp. [97, 98, 99], raw=22 chunk=15 diff=+7 adj=7
- `bon-sent-I-d6-a1-q3` — quaestio, pp. [129, 130], raw=12 chunk=5 diff=+7 adj=7
- `bon-sent-I-d9-divisio` — divisio, pp. [179, 180], raw=12 chunk=5 diff=+7 adj=7
- `bon-sent-I-d39-a2-q1` — quaestio, pp. [692, 693], raw=14 chunk=6 diff=+8 adj=6
- `bon-sent-I-d40-a2-q1` — quaestio, pp. [706, 707, 708, 709, 710], raw=36 chunk=28 diff=+8 adj=6
- `bon-sent-I-d2-a1-q3` — quaestio, pp. [54, 55, 56], raw=19 chunk=12 diff=+7 adj=6
- `bon-sent-I-d23-a1-q2` — quaestio, pp. [405, 406, 407], raw=20 chunk=13 diff=+7 adj=6
- `bon-sent-I-d29-a1-q2` — quaestio, pp. [510, 511, 512], raw=17 chunk=10 diff=+7 adj=6
- `bon-sent-I-d3-p2-a2-q1` — quaestio, pp. [88, 89, 90], raw=33 chunk=26 diff=+7 adj=6
- `bon-sent-I-d31-p1-a1-q1` — quaestio, pp. [532, 533, 534, 535], raw=14 chunk=7 diff=+7 adj=6
- `bon-sent-I-d32-a2-q1` — quaestio, pp. [561, 562, 563], raw=21 chunk=14 diff=+7 adj=6
- `bon-sent-I-d32-dubia` — dubia, pp. [565, 566, 567], raw=29 chunk=22 diff=+7 adj=6
- `bon-sent-I-d35-a1-q4` — quaestio, pp. [609, 610], raw=20 chunk=13 diff=+7 adj=6
- `bon-sent-I-d5-dubia` — dubia, pp. [119, 120, 121, 122], raw=42 chunk=35 diff=+7 adj=6
- `bon-sent-I-d1-a1-q1` — quaestio, pp. [30, 31, 32], raw=28 chunk=22 diff=+6 adj=6
- `bon-sent-I-d11-a1-q1` — quaestio, pp. [209, 210, 211, 212, 213], raw=57 chunk=51 diff=+6 adj=6
- `bon-sent-I-d12-littera` — littera, pp. [218, 219], raw=24 chunk=18 diff=+6 adj=6
- `bon-sent-I-d13-divisio` — divisio, pp. [230], raw=11 chunk=5 diff=+6 adj=6
- `bon-sent-I-d15-p1-a1-q3` — quaestio, pp. [262, 263, 264], raw=27 chunk=21 diff=+6 adj=6
- `bon-sent-I-d21-divisio` — divisio, pp. [378, 379], raw=11 chunk=5 diff=+6 adj=6
- `bon-sent-I-d28-a1-q2` — quaestio, pp. [499, 500], raw=15 chunk=9 diff=+6 adj=6
- `bon-sent-I-d29-dubia` — dubia, pp. [516, 517, 518, 519], raw=29 chunk=23 diff=+6 adj=6
- `bon-sent-I-d40-a4-q1` — quaestio, pp. [716, 717], raw=14 chunk=8 diff=+6 adj=6
- `bon-sent-I-d27-p1-a1-q2` — quaestio, pp. [468, 469, 470, 471, 472, 473, 474], raw=57 chunk=48 diff=+9 adj=5
- `bon-sent-I-d26-a1-q3` — quaestio, pp. [456, 457, 458, 459], raw=31 chunk=23 diff=+8 adj=5
- `bon-sent-I-d34-divisio` — divisio, pp. [585], raw=12 chunk=4 diff=+8 adj=5
- `bon-sent-I-d29-a2-q2` — quaestio, pp. [515, 516], raw=16 chunk=9 diff=+7 adj=5
- `bon-sent-I-d7-a1-q1` — quaestio, pp. [135, 136, 137], raw=43 chunk=36 diff=+7 adj=5
- `bon-sent-I-d11-littera` — littera, pp. [207, 208], raw=24 chunk=18 diff=+6 adj=5
- `bon-sent-I-d13-a1-q1` — quaestio, pp. [230, 231, 232], raw=20 chunk=14 diff=+6 adj=5
- `bon-sent-I-d20-a1-q1` — quaestio, pp. [368, 369, 370], raw=21 chunk=15 diff=+6 adj=5
- `bon-sent-I-d24-a1-q1` — quaestio, pp. [420, 421, 422], raw=31 chunk=25 diff=+6 adj=5
- `bon-sent-I-d28-divisio` — divisio, pp. [495, 496], raw=10 chunk=4 diff=+6 adj=5
- `bon-sent-I-d35-a1-q5` — quaestio, pp. [611, 612], raw=16 chunk=10 diff=+6 adj=5
- `bon-sent-I-d12-a1-q2` — quaestio, pp. [221, 222, 223], raw=18 chunk=13 diff=+5 adj=5
- `bon-sent-I-d15-p1-a1-q1` — quaestio, pp. [259, 260, 261], raw=22 chunk=17 diff=+5 adj=5
- `bon-sent-I-d17-p1-divisio` — divisio, pp. [291], raw=10 chunk=5 diff=+5 adj=5
- `bon-sent-I-d21-a2-q1` — quaestio, pp. [383, 384, 385], raw=19 chunk=14 diff=+5 adj=5
- `bon-sent-I-d24-a2-q2` — quaestio, pp. [426, 427, 428], raw=21 chunk=16 diff=+5 adj=5
- `bon-sent-I-d26-dubia` — dubia, pp. [462, 463, 464], raw=28 chunk=23 diff=+5 adj=5
- `bon-sent-I-d27-p2-a1-q2` — quaestio, pp. [482, 483, 484, 485, 486], raw=28 chunk=23 diff=+5 adj=5
- `bon-sent-I-d28-dubia` — dubia, pp. [504, 505], raw=22 chunk=17 diff=+5 adj=5
- `bon-sent-I-d37-p2-a1-q3` — quaestio, pp. [655, 656, 657], raw=14 chunk=9 diff=+5 adj=5
- `bon-sent-I-d5-a2-q2` — quaestio, pp. [117, 118], raw=10 chunk=5 diff=+5 adj=5
- `bon-sent-I-d7-divisio` — divisio, pp. [134, 135], raw=13 chunk=8 diff=+5 adj=5
- `bon-sent-I-d10-a1-q3` — quaestio, pp. [193, 194], raw=13 chunk=8 diff=+5 adj=4
- `bon-sent-I-d33-a1-q2` — quaestio, pp. [574, 575, 576], raw=18 chunk=13 diff=+5 adj=4
- `bon-sent-I-d37-p1-a1-q2` — quaestio, pp. [640, 641], raw=15 chunk=10 diff=+5 adj=4
- `bon-sent-I-d40-a3-q2` — quaestio, pp. [715, 716], raw=14 chunk=9 diff=+5 adj=4

## Bucket C

- `bon-sent-I-d4-dubia` — dubia, pp. [105, 106, 107], raw=34 chunk=15 diff=+19 adj=19
- `bon-sent-I-d37-p1-a1-q1` — quaestio, pp. [638, 639], raw=29 chunk=10 diff=+19 adj=17
- `bon-sent-I-d2-a1-q4` — quaestio, pp. [56, 57, 58], raw=28 chunk=11 diff=+17 adj=17
- `bon-sent-I-d3-littera` — littera, pp. [62, 63, 64, 65, 66], raw=61 chunk=43 diff=+18 adj=16
- `bon-sent-I-d37-p2-a2-q1` — quaestio, pp. [658, 659], raw=29 chunk=11 diff=+18 adj=16
- `bon-sent-I-d26-a1-q1` — quaestio, pp. [451, 452, 453, 454], raw=36 chunk=19 diff=+17 adj=16
- `bon-sent-I-d27-p2-dubia` — dubia, pp. [491, 492], raw=24 chunk=7 diff=+17 adj=16
- `bon-sent-I-d5-a2-q1` — quaestio, pp. [115, 116, 117], raw=24 chunk=7 diff=+17 adj=16
- `bon-sent-I-d10-a1-q1` — quaestio, pp. [194, 195, 196], raw=28 chunk=12 diff=+16 adj=16
- `bon-sent-I-d33-a1-q1` — quaestio, pp. [570, 571, 572, 573], raw=40 chunk=24 diff=+16 adj=16
- `bon-sent-I-d38-a2-q1` — quaestio, pp. [673, 674, 675, 676], raw=30 chunk=14 diff=+16 adj=16
- `bon-sent-I-d8-p2-a1-q1` — quaestio, pp. [166, 167, 168], raw=23 chunk=7 diff=+16 adj=16
- `bon-sent-I-d25-littera` — littera, pp. [432, 433, 434], raw=43 chunk=24 diff=+19 adj=15
- `bon-sent-I-d7-a1-q4` — quaestio, pp. [143, 144], raw=20 chunk=3 diff=+17 adj=15
- `bon-sent-I-d37-p1-divisio` — divisio, pp. [637], raw=17 chunk=1 diff=+16 adj=15
- `bon-sent-I-d28-a1-q1` — quaestio, pp. [497, 498, 499], raw=36 chunk=21 diff=+15 adj=15
- `bon-sent-I-d29-divisio` — divisio, pp. [507, 508], raw=18 chunk=3 diff=+15 adj=15
- `bon-sent-I-d40-a1-q2` — quaestio, pp. [704, 705], raw=22 chunk=7 diff=+15 adj=15
- `bon-sent-I-d31-p1-a1-q2` — quaestio, pp. [535, 536, 537, 538], raw=34 chunk=18 diff=+16 adj=14
- `bon-sent-I-d20-littera` — littera, pp. [366, 367], raw=28 chunk=13 diff=+15 adj=14
- `bon-sent-I-d34-a1-q1` — quaestio, pp. [585, 586, 587, 588], raw=31 chunk=16 diff=+15 adj=14
- `bon-sent-I-d37-p1-a2-q1` — quaestio, pp. [642, 643], raw=29 chunk=14 diff=+15 adj=14
- `bon-sent-I-d8-p1-a2-q2` — quaestio, pp. [158, 159, 160, 161], raw=53 chunk=38 diff=+15 adj=14
- `bon-sent-I-d25-a2-q1` — quaestio, pp. [441, 442, 443, 444], raw=35 chunk=21 diff=+14 adj=14
- `bon-sent-I-d29-a2-q1` — quaestio, pp. [512, 513, 514], raw=33 chunk=19 diff=+14 adj=14
- `bon-sent-I-d32-a1-q1` — quaestio, pp. [555, 556, 557], raw=27 chunk=13 diff=+14 adj=14
- `bon-sent-I-d37-p1-a2-q2` — quaestio, pp. [644, 645], raw=22 chunk=8 diff=+14 adj=14
- `bon-sent-I-d37-p1-dubia` — dubia, pp. [649, 650, 651], raw=30 chunk=16 diff=+14 adj=14
- `bon-sent-I-d38-a2-q2` — quaestio, pp. [676, 677, 678, 679], raw=24 chunk=10 diff=+14 adj=14
- `bon-sent-I-d5-littera` — littera, pp. [108, 109, 110], raw=44 chunk=28 diff=+16 adj=13
- `bon-sent-I-d31-p2-a1-q1` — quaestio, pp. [541, 542], raw=29 chunk=15 diff=+14 adj=13
- `bon-sent-I-d34-littera` — littera, pp. [582, 583, 584], raw=35 chunk=21 diff=+14 adj=13
- `bon-sent-I-d25-a1-q2` — quaestio, pp. [439, 440, 441], raw=30 chunk=17 diff=+13 adj=13
- `bon-sent-I-d27-p1-a1-q1` — quaestio, pp. [467, 468], raw=19 chunk=6 diff=+13 adj=13
- `bon-sent-I-d27-p2-a1-q3` — quaestio, pp. [487, 488], raw=20 chunk=7 diff=+13 adj=13
- `bon-sent-I-d29-a1-q1` — quaestio, pp. [508, 509, 510], raw=28 chunk=15 diff=+13 adj=13
- `bon-sent-I-d3-p1-a1-q1` — quaestio, pp. [67, 68, 69, 70], raw=41 chunk=28 diff=+13 adj=13
- `bon-sent-I-d31-p2-dubia` — dubia, pp. [549, 550, 551, 552], raw=38 chunk=25 diff=+13 adj=13
- `bon-sent-I-d8-p2-dubia` — dubia, pp. [175, 176], raw=19 chunk=6 diff=+13 adj=13
- `bon-sent-I-d12-divisio` — divisio, pp. [219, 220], raw=14 chunk=2 diff=+12 adj=12
- `bon-sent-I-d2-a1-q1` — quaestio, pp. [50, 51, 52], raw=30 chunk=18 diff=+12 adj=12
- `bon-sent-I-d25-divisio` — divisio, pp. [434, 435], raw=15 chunk=3 diff=+12 adj=12
- `bon-sent-I-d26-littera` — littera, pp. [447, 448, 449, 450], raw=38 chunk=22 diff=+16 adj=11
- `bon-sent-I-d35-littera` — littera, pp. [597, 598], raw=28 chunk=15 diff=+13 adj=11
- `bon-sent-I-d31-p2-a1-q2` — quaestio, pp. [542, 543], raw=25 chunk=13 diff=+12 adj=11
- `bon-sent-I-d39-a2-q3` — quaestio, pp. [695, 696, 697], raw=22 chunk=10 diff=+12 adj=11
- `bon-sent-I-d7-a1-q3` — quaestio, pp. [141, 142], raw=17 chunk=5 diff=+12 adj=11
- `bon-sent-I-d24-a2-q1` — quaestio, pp. [425, 426], raw=21 chunk=10 diff=+11 adj=11
- `bon-sent-I-d37-p1-a3-q2` — quaestio, pp. [648, 649], raw=21 chunk=10 diff=+11 adj=11
- `bon-sent-I-d37-p2-dubia` — dubia, pp. [665, 666], raw=22 chunk=11 diff=+11 adj=11
- `bon-sent-I-d38-littera` — littera, pp. [667, 668], raw=19 chunk=8 diff=+11 adj=11
- `bon-sent-I-d6-divisio` — divisio, pp. [124, 125], raw=13 chunk=2 diff=+11 adj=11
- `bon-sent-I-d15-p2-a1-q2` — quaestio, pp. [271, 272], raw=21 chunk=10 diff=+11 adj=10
- `bon-sent-I-d6-a1-q2` — quaestio, pp. [127, 128], raw=18 chunk=7 diff=+11 adj=10
- `bon-sent-I-d15-p1-divisio` — divisio, pp. [288, 289], raw=11 chunk=1 diff=+10 adj=10
- `bon-sent-I-d30-a1-q1` — quaestio, pp. [521, 522, 523, 524], raw=22 chunk=12 diff=+10 adj=10
- `bon-sent-I-d33-divisio` — divisio, pp. [569, 570], raw=16 chunk=6 diff=+10 adj=10
- `bon-sent-I-d37-p2-a2-q2` — quaestio, pp. [660, 661], raw=18 chunk=8 diff=+10 adj=10
- `bon-sent-I-d5-a1-q2` — quaestio, pp. [114, 115], raw=18 chunk=8 diff=+10 adj=10
- `bon-sent-I-d6-a1-q1` — quaestio, pp. [125, 126], raw=16 chunk=6 diff=+10 adj=10
- `bon-sent-I-d8-p1-divisio` — divisio, pp. [149, 150], raw=14 chunk=4 diff=+10 adj=10
- `bon-sent-I-d8-p2-divisio` — divisio, pp. [165, 166], raw=12 chunk=2 diff=+10 adj=10
- `bon-sent-I-d9-dubia` — dubia, pp. [187, 188, 189, 190, 191, 192], raw=71 chunk=61 diff=+10 adj=10
- `bon-sent-I-d19-p1-dubia` — dubia, pp. [350, 351, 352, 353], raw=47 chunk=37 diff=+10 adj=9
- `bon-sent-I-d8-p1-a2-q1` — quaestio, pp. [156, 157, 158], raw=19 chunk=9 diff=+10 adj=9
- `bon-sent-I-d19-p2-a1-q4` — quaestio, pp. [362, 363, 364], raw=37 chunk=28 diff=+9 adj=9
- `bon-sent-I-d24-a3-q2` — quaestio, pp. [430, 431], raw=20 chunk=11 diff=+9 adj=9
- `bon-sent-I-d24-divisio` — divisio, pp. [419], raw=13 chunk=4 diff=+9 adj=9
- `bon-sent-I-d24-littera` — littera, pp. [418, 419], raw=25 chunk=16 diff=+9 adj=9
- `bon-sent-I-d33-a1-q3` — quaestio, pp. [576, 577, 578], raw=21 chunk=12 diff=+9 adj=9
- `bon-sent-I-d36-a3-q1` — quaestio, pp. [625, 626, 627], raw=22 chunk=13 diff=+9 adj=9
- `bon-sent-I-d37-p2-a2-q3` — quaestio, pp. [662, 663, 664, 665], raw=22 chunk=13 diff=+9 adj=9
- `bon-sent-I-d8-p1-a1-q1` — quaestio, pp. [150, 151, 152], raw=31 chunk=22 diff=+9 adj=9
- `bon-sent-I-d8-p1-dubia` — dubia, pp. [161, 162, 163, 164, 165], raw=19 chunk=10 diff=+9 adj=9
