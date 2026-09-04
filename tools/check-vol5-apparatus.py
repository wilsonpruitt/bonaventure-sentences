#!/usr/bin/env python3.11
"""Vol V apparatus integrity check.

`audit-apparatus-count.py` is BLIND to Vol V: that script counts footer-note
openers in the raw OCR, and Vol V's OCR renders every superscript numeral as a
punctuation glyph (^ ' ") — so there is nothing for it to match. This script
replaces it with checks that do not depend on the raw at all.

It verifies three things across `vol5/*.md`:

  1. LABEL PAIRING — every `[^id]:` definition in ## Apparatus has exactly one
     matching anchor in the ## Latin body and one in the ## English body.
     (A mismatch means an entry will render detached or silently vanish.)

  2. DUPLICATE DEFS — no `[^id]:` is defined twice in one file. Quaracchi
     restarts footnote numbering on every printed page, so bare numbers would
     collide; labels are page-qualified (`[^p214-5]`) to prevent exactly this.
     A duplicate silently drops an entry at render time.

  3. FOOTER OWNERSHIP — across all chunks, each printed page's notes must run
     1..N with no gaps and no page claimed twice for the same number. A GAP
     means a note is owned by nobody (the failure mode that cost Vol IV three
     whole registers); a DOUBLE means two chunks claim the same note.

Gaps at the TOP of a page's range are expected while work is in progress — the
last note(s) of a page are often forwarded to the next, not-yet-written chunk.
Those show as a trailing shortfall, not an interior gap, and are reported
separately as PENDING rather than as an error.

Usage:  python3.11 tools/check-vol5-apparatus.py [--expect-max PAGE=N ...]
Exit code is 1 if any interior gap, duplicate, double-claim, or pairing
mismatch is found; 0 otherwise.
"""
import glob
import os
import re
import sys
from collections import defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOL5 = os.path.join(REPO_ROOT, "vol5")

# Printed-page → true total number of footer notes, where known from an
# eyes-on band read. Lets the script distinguish "still pending" from "lost".
KNOWN_TOTALS = {
    # QD de scientia Christi (pp. 3-43) — the work opens the volume.
    3: 9,
    4: 9,
    5: 7,
    6: 9,   # nn.1-6 Quaest. I, nn.7-9 Quaest. II; page fully consumed
    7: 11,
    8: 7,
    9: 6,
    10: 8,  # nn.1-7 Quaest. II, n.8 Quaest. III — both now spent (q3 landed)
    11: 10,
    12: 10,
    13: 8,   # n.5 runs over the gutter, left register into right
    14: 6,   # n.3 runs over the gutter
    15: 5,   # n.3 runs over the gutter
    16: 8,   # Quaest. III closes here under an ornamental rule; nothing forwarded
    17: 10,
    18: 9,
    19: 8,
    20: 10,
    21: 12,
    22: 8,
    23: 10,
    24: 9,   # n.9 BREAKS OFF at the foot and completes at the HEAD of p.25's
             # left register — the work's first PAGE-CROSSING runover. Counted
             # here, on the leaf where it opens.
    25: 9,   # opens with p.24 n.9's runover above n.1; n.9 in turn BREAKS OFF
             # and completes in the whole of p.26's left register.
    26: 7,   # its OWN numerals all stand in the RIGHT register — the left
             # register is entirely p.25 n.9's runover. Seven is not a miscount.
    27: 8,   # n.1 (the whole LEFT register, a full-column editorial note) is
             # Quaest. IV's; nn.2-8 are Quaest. V's -- picked up by bon-qsc-q5,
             # so the leaf is now complete.
    28: 8,   # n.5 runs over the gutter, left register into right
    29: 8,   # n.6 runs over the gutter, left register into right
    30: 9,
    31: 6,
    32: 9,   # n.1 is Quaest. V's (reply 18 closes across the top band of both
             # columns); nn.2-9 are Quaest. VI's -- picked up by bon-qsc-q6,
             # so the leaf is now complete. Same SHAPE as p.27, ratio 1/8.
    33: 12,  # n.8 runs over the gutter, left register into right
    34: 6,   # n.5 runs over the gutter, left register into right
    35: 7,   # n.4 runs over the gutter, left register into right
    36: 3,   # a short register: the leaf is almost all reply prose
    37: 7,   # BOUNDARY LEAF, and the work's LAST: nn.1-3 are Quaest. VI's
             # (reply 19.20 closes across the top band of both columns);
             # nn.4-7 are Quaest. VII's and are a legitimate forwarded
             # PENDING until bon-qsc-q7 lands. Ratio 3/4 -- a sixth boundary
             # and a sixth distinct ratio.
    205: 8,
    206: 11,
    207: 8,
    208: 7,   # prologue ends here; nothing forwarded
    201: 5,
    202: 10,
    203: 8,
    204: 9,   # nn.8-9 are § 3's — pending until prol-s3 lands
    210: 8,
    211: 7,
    212: 7,
    213: 7,
    214: 9,
    215: 6,
    216: 6,
    217: 7,
    218: 7,   # Pars I ends here; nothing forwarded
    219: 5,   # Pars II opens; nn.1-3 Cap. I, nn.4-5 Cap. II
    220: 6,   # nn.1-5 Cap. II, n.6 Cap. III
    221: 7,   # nn.1-3 Cap. III, nn.4-7 Cap. IV; page fully consumed
    222: 5,   # nn.1-2 Cap. IV (tail), nn.3-5 Cap. V
    223: 9,   # all nine Cap. V
    224: 8,   # nn.1-7 Cap. VI, n.8 Cap. VII
    225: 7,   # nn.1-4 Cap. VII, nn.5-7 Cap. VIII; page fully consumed
    226: 9,   # nn.1-5 Cap. VIII, nn.6-9 Cap. IX; page fully consumed
    227: 9,   # all nine Cap. IX; Cap. X opens on this page but claims no note
    228: 9,   # all nine Cap. X; page fully consumed
    229: 8,   # all eight Cap. XI; page fully consumed
    230: 7,   # n.1 Cap. XI, nn.2-7 Cap. XII; PARS II ends here, nothing forwarded
    231: 7,   # PARS III opens: nn.1-6 Cap. I, n.7 Cap. II (forwarded to p3-c2)
    232: 9,   # nn.1-7 Cap. II, nn.8-9 Cap. III (forwarded to p3-c3)
    233: 5,   # nn.1-3 Cap. III, nn.4-5 Cap. IV (forwarded to p3-c4)
    234: 9,   # nn.1-2 Cap. IV, nn.3-9 Cap. V; page fully consumed
    235: 7,   # n.1 Cap. V, nn.2-7 Cap. VI; page fully consumed
    236: 7,   # nn.1-6 Cap. VII, n.7 Cap. VIII (forwarded to p3-c8)
    237: 9,   # band-read while closing the p.236->p.237 runover test, then
              # re-read in full by p3-c8: nn.1-3 left block, nn.4-9 right,
              # but SIX of the nine (nn.1-6) anchor in the LEFT column -- a
              # three-note UNDERRUN of the column division. Capp. VIII AND IX
              # both sit on this page, yet ALL NINE notes are Cap. VIII's;
              # Cap. IX claims none. Page fully consumed by p3-c8.
    238: 8,   # band-read in full by p3-c9: nn.1-4 left block (n.4 broken
              # MID-WORD at "Amor ergo... fu-"), right block opens with n.4's
              # unnumbered continuation then nn.5-8. Anchors track the blocks
              # exactly here (nn.1-4 left, nn.5-8 right) -- a COINCIDENCE page
              # whose split falls INSIDE a note, the p.236 shape repeated.
              # nn.1-7 Cap. IX, n.8 Cap. X (forwarded to p3-c10).
    239: 9,   # band-read in full by p3-c10: nn.1-4 left block (n.4 broken at a
              # WORD boundary at "...II. Sent. d. 35. per totam, ubi etiam"),
              # right block opens with n.4's unnumbered continuation then
              # nn.5-9. But nn.1-6 ALL anchor in the LEFT column, so nn.5-6
              # anchor left and print right -- a one-note OVERRUN on top of a
              # split falling INSIDE a note. All nine are Cap. X's; the page is
              # fully consumed by p3-c10 and nothing is forwarded.
    240: 9,   # band-read in full by p3-c11: nn.1-4 left block (n.4 broken at a
              # PUNCTUATION boundary, after the colon of "Ibid. III. c. 3. n. 7:"),
              # right block opens with n.4's unnumbered continuation then nn.5-9.
              # Anchors and blocks COINCIDE exactly here (nn.1-4 left, nn.5-9
              # right) -- the p.238 shape, not p.239's overrun. All nine are
              # Cap. XI's; page fully consumed by p3-c11.
    241: 10,  # band-read in full by p3-c11, but split by PARS, not by block:
              # left block nn.1-5 (+ the printer's signature), right block
              # nn.6-10, both closing complete. nn.1-2 anchor in Pars III
              # Cap. XI's closing paragraph (owned by p3-c11); nn.3-10 anchor
              # in PARS QUARTA Cap. I and are a legitimate forwarded PENDING
              # until bon-brev-p4-c1 lands (which it now has).
    242: 6,   # band-read in full by p4-c1, split by CAPITULUM, not by block:
              # left block nn.1-4 with n.4 broken off MID-WORD at "-- Pro his ta-",
              # right block opening UNNUMBERED with "men 1, 2, 3 cum pluribus
              # codd. ..." then nn.5-6. nn.1-2 anchor in Pars IV Cap. I (owned by
              # p4-c1); nn.3-6 anchor in Cap. II and are a legitimate forwarded
              # PENDING until bon-brev-p4-c2 lands (which it now has). The p.242
              # GUTTER RUNOVER is POSITIVE and is logged on p4-c2's ledger line.
    243: 9,   # band-read in full by p4-c2, split by CAPITULUM, and the division
              # falls INSIDE the left block: left block nn.1-5 with n.5 broken
              # off at a WORD boundary ("...decet eius nec operari, quod"),
              # right block opening UNNUMBERED with "etiam paulo post omittitur
              # a pluribus codd. ..." then nn.6-9. nn.1-3 anchor in Cap. II
              # (owned by p4-c2); nn.4-9 anchor in Cap. III and are a legitimate
              # forwarded PENDING until bon-brev-p4-c3 lands. The p.243 GUTTER
              # RUNOVER is POSITIVE and is p4-c3's to render and to log.
              # CLOSED by bon-brev-p4-c3, which owns nn.4-9 and logs the gutter.
    244: 7,   # band-read in full by p4-c3, split by CAPITULUM one note ABOVE a
              # block break that is itself inside a note: left block nn.1-3 with
              # n.3 broken off at a WORD boundary INSIDE A SQUARE-BRACKETED
              # LEMMA ("-- Superius pro a principio [2 cum aliquot"), right block
              # opening UNNUMBERED with "codd. a primo principio] Vat., 1 et 3
              # in principio, ..." then nn.4-7. nn.1-2 anchor in Cap. III (owned
              # by p4-c3); nn.3-7 anchor in Cap. IV and are a legitimate
              # forwarded PENDING until bon-brev-p4-c4 lands. The p.244 GUTTER
              # RUNOVER is POSITIVE and is p4-c4's to render and to log.
              # CLOSED by bon-brev-p4-c4, which owns nn.3-7 and logs the gutter.
    245: 9,   # band-read in full by p4-c4, split by CAPITULUM and by BLOCK at
              # the SAME point -- the first COINCIDENCE page in Pars IV: left
              # block nn.1-4 closing complete ("... et 2 inter."), right block
              # opening NUMBERED at n.5 and carrying nn.5-9. nn.1-4 anchor in
              # Cap. IV (owned by p4-c4); nn.5-9 anchor in Cap. V and are a
              # legitimate forwarded PENDING until bon-brev-p4-c5 lands. The
              # p.245 GUTTER RUNOVER is NEGATIVE, closed from both sides by
              # p4-c4; the p.245 -> p.246 test is negative from the p.245 side
              # only and stays open.
              # CLOSED by bon-brev-p4-c5, which owns nn.5-9. NOTE the ANCHOR
              # split is 6/3 (nn.1-6 left, nn.7-9 right) against the 4/5 BLOCK
              # split -- the block break falls TWO NOTES ABOVE the anchor break,
              # the mirror of p.244. The p.245 -> p.246 test is CLOSED NEGATIVE
              # from the p.246 side by p4-c5.
    246: 9,   # band-read in full by p4-c5. A TRUE COINCIDENCE PAGE: anchors 5/4
              # (nn.1-5 left column, all Cap. V; nn.6-9 right column, all
              # Cap. VI), blocks 5/4 at the same point, and the Cap. V / Cap. VI
              # boundary between nn.5 and 6. Left block opens NUMBERED at n.1
              # ("Rom. 9, 5. ..."), closing the p.245 -> p.246 test NEGATIVE;
              # right block opens NUMBERED at n.6, so the p.246 GUTTER RUNOVER
              # is NEGATIVE (both logged by p4-c5). nn.1-5 anchor in Cap. V
              # (owned by p4-c5); nn.6-9 anchor in Cap. VI and are a legitimate
              # forwarded PENDING until bon-brev-p4-c6 lands. ** n.9 BREAKS OFF
              # at "-- Post pauca pro potest": the p.246 -> p.247 PAGE-CROSSING
              # RUNOVER IS POSITIVE and is p4-c6's to render and to log. **
              # CLOSED by bon-brev-p4-c6, which owns nn.6-9 and logs the
              # page-crossing runover.
    247: 8,   # band-read in full by p4-c6, split by CAPITULUM one note BELOW a
              # block break that coincides with the anchor break: left block
              # opens UNNUMBERED with p.246 n.9's tail ("A possunt, et habent
              # pro habet. Subinde cum A B C F G I K L M N O et 2 vocibus
              # dupliciter cognosci interseruimus esse et.") then nn.1-4,
              # closing complete; right block opens NUMBERED at n.5 and carries
              # nn.5-8, closing complete. Anchors 4/4 (nn.1-4 left, nn.5-8
              # right) = blocks 4/4, but the Cap. VI / Cap. VII boundary falls
              # BETWEEN nn.5 AND 6, i.e. inside the right block: n.5 anchors in
              # Cap. VI (owned by p4-c6) and nn.6-8 anchor in Cap. VII and are
              # a legitimate forwarded PENDING until bon-brev-p4-c7 lands. The
              # p.247 GUTTER RUNOVER is NEGATIVE (logged by p4-c6); the
              # p.247 -> p.248 test is negative from the p.247 side only and
              # stays open for p4-c7, which owns n.8. The unnumbered
              # continuation is p.246 n.9's tail and is NOT counted here.
              # CLOSED NEGATIVE from the p.248 side by p4-c7: p.248's left
              # block opens NUMBERED at n.1 ("Cfr. supra c. 5, ...").
    248: 8,   # band-read in full by p4-c7. The BLOCK SPLIT FALLS INSIDE n.5,
              # the note whose anchor stands first in the right column, so the
              # same entry supplies the left block's last line and the right
              # block's first: left block carries nn.1-4 complete then breaks
              # off inside n.5 at "Isai. 26, 12: Domine, dabis pacem nobis;
              # omnia enim"; right block opens UNNUMBERED with n.5's tail
              # ("opera nostra operatus es nobis. -- Seq. locus est Ps. 15, 2.
              # -- Cfr. III. Sent. d. 20. q. 3. seq. et IV. Sent. d. 15. p. I.
              # q. 1.") then nn.6-8, closing complete. So the p.248 GUTTER
              # RUNOVER is POSITIVE (logged by p4-c7, which owns n.5). Anchors
              # 4/4 (nn.1-4 left, nn.5-8 right); blocks 4.5/3.5; and the
              # Cap. VII / Cap. VIII boundary falls BETWEEN nn.5 AND 6, so
              # nn.1-5 are owned by p4-c7 and nn.6-8 anchor in Cap. VIII and
              # are a legitimate forwarded PENDING until bon-brev-p4-c8 lands.
              # The p.248 -> p.249 test is negative from the p.248 side only
              # (right block ends complete at n.8) and stays open for p4-c8,
              # which owns n.8. The unnumbered continuation is n.5's own tail
              # and is NOT counted as a separate entry.
    249: 8,   # band-read in full by p4-c8. Same shape as p.248 but shifted one
              # note: the BLOCK SPLIT FALLS INSIDE n.6, whose anchor is ALREADY
              # in the right column, so the runover crosses the gutter in the
              # same direction the anchor did. Left block carries nn.1-5
              # complete then breaks off MID-WORD inside n.6 at "Hugo a S. Vict.
              # in Libello de Quatuor Voluntat. in Chri-"; right block opens
              # UNNUMBERED with n.6's tail ("sto. In textu originali plura
              # interseruntur. Cfr. I. Sent. d. 48. a. 2. q. 2. in corp. et
              # III. Sent. d. 17. a. 4. q. 3. in corp.") then nn.7-8, closing
              # complete. So the p.249 GUTTER RUNOVER is POSITIVE (logged by
              # p4-c8, which owns n.6). Anchors 5/3 (nn.1-5 left, nn.6-8
              # right); blocks 5.5/2.5; and the Cap. VIII / Cap. IX boundary
              # falls BETWEEN nn.6 AND 7, matching neither split, so nn.1-6 are
              # owned by p4-c8 and nn.7-8 anchor in Cap. IX and are a
              # legitimate forwarded PENDING until bon-brev-p4-c9 lands.
              # The p.248 -> p.249 test is CLOSED NEGATIVE by p4-c8: p.249's
              # left block opens NUMBERED at n.1 ("A Boethio, de Una Persona
              # et duabus naturis, c. 8."). The p.249 -> p.250 test is negative
              # from the p.249 side only and stays open for p4-c9, which owns
              # n.8. NOTE: the printer's signature "S. Bonav. -- Tom. V."
              # returns here at the foot of the LEFT block (last seen p.241)
              # and the quire signature "32" stands at the foot of the RIGHT
              # block. NEITHER is an entry, and the printer's signature sits
              # exactly where n.6's missing text would otherwise be looked for.
    250: 9,   # band-read in full by p4-c9. A NEW CONFIGURATION: the Cap. IX /
              # Cap. X boundary FALLS ON THIS PAGE (Cap. X opens part-way down
              # the right column) but ALL NINE notes anchor in Cap. IX, so the
              # capitulum line sits BELOW the whole register and the page is
              # owned entire by ONE chunk. Anchors 5/4 (nn.1-5 left, nn.6-9
              # right); blocks 2.5/6.5 -- the left block carries nn.1-2 then
              # breaks off INSIDE n.3 at "Immediate post respicitur Ps. 68, 5:
              # Quae", a WORD BOUNDARY INSIDE A QUOTED VERSE; the right block
              # opens UNNUMBERED with n.3's tail ("non rapui tunc exsolvebam.
              # Cfr. August. in hunc loc., ex quo quaedam referuntur II. Sent.
              # lit. Magistri, d. XXII. c. 4.") then nn.4-9, closing complete.
              # So the p.250 GUTTER RUNOVER is POSITIVE (logged by p4-c9) and
              # the block line stands TWO NOTES ABOVE the anchor line -- the
              # widest three-line spread yet. The unnumbered continuation is
              # n.3's own tail and is NOT a separate entry. The p.249 -> p.250
              # test is CLOSED NEGATIVE by p4-c9: p.250's left block opens
              # NUMBERED at n.1 ("Epist. I. Ioan. 3, 16."). The p.250 -> p.251
              # test is negative from the p.250 side only and stays open for
              # p4-c10. Neither the printer's signature nor a quire signature
              # falls on p.250.
    251: 7,   # band-read in full by p4-c10, which owns ALL SEVEN. p.251 is
              # Cap. X entire, top to bottom -- no capitulum line on the page,
              # and the only running head in Pars IV that is simply correct.
              # Anchors 3/4 (nn.1-3 left, nn.4-7 right); blocks 3.5/3.5 -- the
              # left block carries nn.1-3 then breaks off INSIDE n.4 at "Iuxta
              # August., Enarrat.", a word boundary that SPLITS A WORK'S TITLE
              # (Enarrationes in Psalmos); the right block opens UNNUMBERED
              # with n.4's tail ("in Ps. 149, 6. n. 12, et Isidor., XVIII.
              # Etymolog. c. 6, ...") then nn.5-7, closing complete. So the
              # p.251 GUTTER RUNOVER is POSITIVE (logged by p4-c10) and the
              # block line falls INSIDE the note whose anchor stands FIRST in
              # the second column -- the p.248 configuration, second instance.
              # The unnumbered continuation is n.4's own tail and is NOT a
              # separate entry. The p.250 -> p.251 test is CLOSED NEGATIVE by
              # p4-c10: p.251's left block opens NUMBERED at n.1 ("Cfr. Marc.
              # 16, 19."). Neither signature falls on p.251.
    252: 6,   # band-read in full by p4-c10, which owns n.1 ONLY. The PARS IV /
              # PARS V boundary falls on this page: Cap. X's tail runs across
              # the top of both columns, then the full-width PARS QUINTA
              # display heading. Register splits 1/5 by pars -- the most
              # lopsided division in Pars IV. n.1 ("Epist. I. Cor. 12, 8-11.")
              # anchors on "prout vult" in Cap. X; nn.2-6 anchor in PARS V
              # Cap. I and are FORWARDED to bon-brev-p5-c1 as a PENDING.
              # Blocks 3/3 (nn.1-3 left, nn.4-6 right). The p.251 -> p.252
              # test is CLOSED NEGATIVE by p4-c10 (p.252's left block opens
              # NUMBERED at n.1), as is p.252's own gutter test (right block
              # opens NUMBERED at n.4). The p.252 -> p.253 test is NOT run --
              # p.253 is not imaged -- and is forwarded to p5-c1.
    253: 9,   # band-read in full by p5-c1, split by CAPITULUM: anchors 4/5
              # (nn.1-4 Cap. I, nn.5-9 Cap. II) but blocks 6/3 (nn.1-6 left,
              # nn.7-9 right), so the BLOCK line stands TWO NOTES BELOW the
              # anchor line -- the mirror of p.245, and the first page on which
              # the capitulum line agrees with the anchor line while the block
              # line disagrees with both. nn.1-4 anchor in Pars V Cap. I (owned
              # by p5-c1); nn.5-9 anchor in Cap. II and are a legitimate
              # forwarded PENDING until bon-brev-p5-c2 lands. The p.252 ->
              # p.253 test is CLOSED NEGATIVE by p5-c1 (left block opens
              # NUMBERED at n.1), as is p.253's own gutter test (right block
              # opens NUMBERED at n.7). n.9 BREAKS OFF MID-WORD at the page
              # foot ("Gen. 15, 1: Ego [Deus] pro-"), so p.253 -> p.254 is a
              # POSITIVE page-crossing runover for p5-c2 to close and log.
    254: 6,   # band-read in full by p5-c2. A FIFTEENTH CONFIGURATION and the
              # mirror of pp.248/251: anchors 3/3 (nn.1-3 left, nn.4-6 right)
              # and the BLOCK SPLIT FALLS INSIDE n.3, whose anchor stands LAST
              # in the FIRST column -- so the runover crosses the gutter in the
              # direction OPPOSITE to its own anchor, where on pp.248/251 it
              # crossed in the same direction. The block line and the anchor
              # line COINCIDE; the CAPITULUM line stands ONE NOTE BELOW both,
              # falling between nn.4 and 5. BOTH blocks open UNNUMBERED on this
              # page and neither opener is an entry: the left block opens with
              # p.253 n.9's tail ("tector tuus sum et merces tua magna nimis.
              # -- Mox pro et propria 1 ex propria, ...") -- which CLOSES the
              # p.253 -> p.254 page-crossing runover POSITIVE, the halves
              # meeting exactly where Gen. 15, 1 says they must, at "pro-" /
              # "tector" (logged as p.253 n.9:page on p5-c2's ledger line) --
              # and the right block opens with n.3's own tail ("pro digni;
              # subinde pro augmentandi et infundentis plures codd. augendi et
              # influentis."), n.3 having broken off at a word boundary INSIDE
              # AN EDITORIAL LEMMA, stopping ON the variant ("Inferius edd.,
              # excepta 2, cum pluribus codd. condigni"), so the p.254 GUTTER
              # RUNOVER is POSITIVE (logged as p.254 n.3:gutter by p5-c2).
              # nn.1-4 anchor in Pars V Cap. II (owned by p5-c2); nn.5-6 anchor
              # in Cap. III and are a legitimate forwarded PENDING until
              # bon-brev-p5-c3 lands. The p.254 -> p.255 test is NOT p5-c2's --
              # Cap. II closes part-way down p.254's right column and Cap. III
              # opens below it -- and belongs to p5-c3, which owns n.6.
              # Neither the printer's signature nor a quire signature falls on
              # p.254; the next is due around p.257.
    255: 10,  # band-read in full by p5-c3, which owns ALL TEN: no capitulum
              # boundary falls on p.255, so a page whose register is undivided
              # sits between two pages whose registers are not. A SIXTEENTH
              # CONFIGURATION, and the SECOND OCCURRENCE of p.253's shape:
              # anchors divide 6/4 (nn.1-6 left, nn.7-10 right) while the
              # BLOCKS divide 8/2 with the split falling INSIDE n.8 -- so the
              # left block OVERRUNS the anchor line by two whole notes and then
              # by half of a third. Unlike p.253, where the overrunning notes
              # were the FIRST two of the page, here they are the LAST two of an
              # eight-entry block, so no seam is visible in the register.
              # n.8 breaks off at a FULL STOP on a half-entry that reads as a
              # complete citation ("Serm. 169. (alias 15. de Verbis Apostoli)
              # c. 11. n. 13.") and the right block opens UNNUMBERED with its
              # continuation ("Cfr. tom. IV. pag. 327, nota 2. -- Seq. locus est
              # Rom. 9, 16. ..."), so the p.255 GUTTER RUNOVER is POSITIVE
              # (logged as p.255 n.8:gutter by p5-c3), confirmed three ways:
              # no numeral on the opener, "Seq. locus est" naming Rom. 9, 16
              # which IS the body's next italic quotation, and the grammar.
              # BOTH page-crossing tests on this leaf-pair are NEGATIVE: p.255's
              # left block opens NUMBERED ("1 Secundum Ambros. supra pag. 237,
              # nota 4. allegatum."), closing p.254 -> p.255, and p.256's left
              # block opens NUMBERED ("1 De his agitur hic et 2 seqq. capp."),
              # closing p.255 -> p.256. Nothing is forwarded out of p5-c3:
              # p.256's register is Cap. IV's entire, because Cap. III's two
              # closing lines at the head of p.256's left column carry NO anchor
              # -- verified negatively on the band. Neither the printer's
              # signature nor a quire signature falls on p.255 or p.256; both
              # last fell on p.249 and are now overdue.
    256: 6,   # band-read in full by p5-c4, which owns ALL SIX. The Cap. III /
              # Cap. IV boundary falls two lines below the top of the LEFT
              # column and the register is nonetheless undivided -- the mirror
              # of p.250, and the negative that establishes it (Cap. III's two
              # surviving lines carry no anchor) was re-derived by p5-c4 rather
              # than adopted from p5-c3's hand-off. Anchors divide 3/3 (nn.1-3
              # left, nn.4-6 right) while the BLOCKS divide 4/2, so the left
              # block OVERRUNS the anchor line by exactly ONE note (n.4 prints
              # left, anchors right) -- p.243's shape, in its second occurrence.
              # The p.256 GUTTER RUNOVER is NEGATIVE: the left block ends
              # complete at n.4 ("Cfr. III. Sent. d. 34. p. I. a. 1. q. 1.")
              # and the right block opens NUMBERED ("5 Vide supra p. I. c. 6.").
              # Neither signature falls on p.256.
    257: 9,   # band-read in full by p5-c4, which owns n.1 ONLY. The Cap. IV /
              # Cap. V boundary falls part-way down the LEFT column, between
              # nn.1 and 2 -- matching NEITHER the anchor split (3/6: nn.1-3
              # left, nn.4-9 right) NOR the block split (5/4), so all three
              # lines are distinct. The left block's five-note OVERRUN of the
              # anchor line by TWO notes is the THIRD occurrence of p.253's and
              # p.255's shape, the first configuration in the corpus to reach
              # three. nn.2-9 are FORWARDED to p5-c5 (Pars V Cap. V).
              # The p.256 -> p.257 page-crossing runover is NEGATIVE: p.256's
              # right block ends complete at n.6 and p.257's left block opens
              # NUMBERED ("1 Cfr. III. Sent. d. 23. a. 2. q. 5."). p.257's own
              # gutter test was run and is likewise NEGATIVE (left block ends
              # complete at n.5, right block opens NUMBERED with n.6), but it
              # is p5-c5's to LOG, not p5-c4's -- p5-c5 owns eight of the nine.
              # *** THE PRINTER'S SIGNATURE "S. Bonav. -- Tom. V." STANDS ON
              # p.257, unnumbered, on its own line at the foot of the LEFT
              # block below n.5 -- first appearance since p.249, exactly the
              # ~8-leaf cadence p5-c3 predicted. The quire signature "33"
              # stands below n.9 at the foot of the RIGHT block. NEITHER IS AN
              # ENTRY: p.257's register is NINE, and a reader counting block
              # lines rather than numerals would reach ten.
    258: 7,   # band-read in full by p5-c5, which owns nn.1-4. A NINETEENTH
              # configuration and the MIRROR of p.245's: anchors divide 4/3
              # (nn.1-4 LEFT, nn.5-7 RIGHT) while the BLOCKS divide 2/5, so the
              # block break stands TWO NOTES ABOVE the anchor break -- and the
              # CAPITULUM line (Cap. V / Cap. VI, which falls at the TOP of the
              # RIGHT column) coincides EXACTLY with the anchor line while
              # dissenting from the block line. n.2 is a single entry filling
              # most of the left block (Origen + Hugh of St Victor + Gregory,
              # an Additamentum in all but name), which is WHY the block break
              # sits so high: block extent is a function of entry LENGTH, not
              # of anchor count. nn.5-7 are FORWARDED to p5-c6 (Pars V Cap. VI).
              # The p.257 -> p.258 page-crossing runover is NEGATIVE (p.257's
              # right block ends complete at n.9 with the quire signature "33"
              # below it, and p.258's left block opens NUMBERED with n.1);
              # p.258's own gutter test is NEGATIVE too (left block ends
              # complete at n.2, right block opens NUMBERED with n.3).
    259: 9,   # band-read in full by p5-c6, which owns ALL NINE: p.259 is Pars V
              # Cap. VI from its first line to its last, so there is NO capitulum
              # line on this page at all. A TWENTIETH configuration: anchors
              # divide 4/5 (nn.1-4 LEFT column, nn.5-9 RIGHT) while the BLOCKS
              # divide 5/4 (nn.1-5 LEFT, nn.6-9 RIGHT), so the block break
              # stands ONE NOTE BELOW the anchor break -- and the dissenting
              # note, n.5, is precisely the one that then RUNS OVER the gutter,
              # broken at "G substituit quam pro" and completed unnumbered at
              # the head of the right block ("quod. Superius pro hanc vallem
              # I K L M O P hac valle ..."). So one entry is physically present
              # in BOTH blocks while anchoring in a column it does not print
              # under. The p.258 -> p.259 page-crossing runover is NEGATIVE
              # (p.258's right block ends complete at n.7 and p.259's left block
              # opens NUMBERED with n.1).
    260: 7,   # band-read in full by p5-c6, which owns nn.1-3. Split by
              # CAPITULUM: the Cap. VI / Cap. VII heading stands about two-thirds
              # down the LEFT column, and nn.1-3 anchor above it (Cap. VI),
              # nn.4-7 below it (Cap. VII, FORWARDED to p5-c7).
              # *** CORRECTED by p5-c7 from the band: n.4's ANCHOR is in the
              # LEFT column (on "orationis dominicae", six lines below the
              # Cap. VII heading), which p5-c6's own hand-off states. So
              # anchors divide 4/3, blocks divide 3/4, and the capitulum line
              # falls between nn.3 and 4 -- THREE LINES, THREE POSITIONS. The
              # earlier "all three lines coincide, for the first time in
              # Pars V" claim is WITHDRAWN. nn.5-7 anchor in the RIGHT column
              # (on "fundamenta", "universalis", "obsequium Christi"), all
              # three read by p5-c7. n.3 RUNS OVER the gutter (broken at
              # "ubi in textu verba", completed unnumbered at the head of the
              # right block with "Dionysii de raptu in caliginem ..."), and it
              # belongs to p5-c6 because its ANCHOR is Cap. VI's, even though
              # the block it completes in carries four of p5-c7's notes. The
              # p.259 -> p.260 page-crossing runover is NEGATIVE (p.259's right
              # block ends complete at n.9 "Gal. 5, 22. seq." and p.260's left
              # block opens NUMBERED with n.1).
    261: 9,   # band-read in full by p5-c7, which owns nn.1-5. Split by
              # CAPITULUM: the Cap. VII / Cap. VIII heading stands about
              # one-third down the RIGHT column, and nn.1-5 anchor above it
              # (Cap. VII), nn.6-9 below it (Cap. VIII, FORWARDED to p5-c8).
              # Anchors divide 4/5, blocks divide 5/4, and the capitulum line
              # falls between nn.5 and 6 -- THREE LINES, THREE POSITIONS, the
              # exact mirror of p.260 (there the capitulum line sits ON the
              # anchor break; here it sits ON the block break). The dissenting
              # note is n.5, whose anchor is on Cap. VII's LAST line in the
              # RIGHT column while its entry prints in the LEFT block -- the
              # same geometry as p.259 n.5, but this one does NOT run over.
              # BOTH runover tests NEGATIVE: p.260 -> p.261 (p.260's right
              # block ends complete at n.7 "plures codd. improbatae)." and
              # p.261's left block opens NUMBERED with n.1) and p.261's own
              # gutter (left block ends complete at n.5 "substituit
              # aedificatione." and the right block opens NUMBERED with n.6).
    262: 7,   # band-read in full by p5-c8, which owns nn.1-3. Split by
              # CAPITULUM: Cap. VIII ends at the FOOT of the LEFT column and
              # the Cap. IX heading stands at the very TOP of the RIGHT column,
              # so nn.1-3 anchor in Cap. VIII (on "pondus mentis", "simul et
              # ordinate", "Dominus orat", all three read on the band) and
              # nn.4-7 in Cap. IX (FORWARDED to p5-c9; nn.4-5 anchors read on
              # the band at "digito Dei" and "qui vult esse perfectus", nn.6-7
              # anchors left UNREAD and deliberately NOT inferred).
              # Anchors divide 3/4, blocks divide 3/4, and the capitulum line
              # falls between nn.3 and 4 -- all THREE LINES COINCIDE on this
              # leaf, with no dissenting note anywhere on it. Derived from
              # p5-c8's own per-note list; the mechanism is that the capitulum
              # boundary here IS the column boundary, so the three structures
              # are measured against one physical line. NO claim is made that
              # this is a first for Pars V -- that would need pp.252-259's
              # anchors re-derived, which p5-c8 did not do (cf. the withdrawn
              # p.260 claim above). BOTH runover tests NEGATIVE: p.261 -> p.262
              # (p.261's right block ends complete at n.9 "excepta 2, quatuor
              # tanquam." and p.262's left block opens NUMBERED with n.1) and
              # p.262's own gutter (left block ends complete at n.3 "perperam
              # Quae universitas." and the right block opens NUMBERED with n.4
              # "Exod. 31, 18.").
    263: 8,   # band-read in full by p5-c9, which owns nn.1-6. THE PAGE WAS
              # NEVER IMAGED BEFORE THIS CHUNK -- extracted at 450 dpi and
              # measured fresh (gutter 1195). Split by CAPITULUM: Cap. IX runs
              # from the head of the left column to about 55% down the RIGHT
              # column, where the Cap. X heading stands, so nn.1-6 anchor in
              # Cap. IX (on "ista vivificans", "ius suum unicuique reddere"
              # [marker INSIDE the guillemets], "debetur veracitas", "non
              # concupisces rem alienam", "superbiae vitae", "verum etiam
              # abundantem" -- all six read on the band) and nn.7-8 in Cap. X
              # (FORWARDED to p5-c10; both anchors READ on the band, at
              # "petitio decentium a Deo" and "donum perfectum", neither
              # inferred). Anchors divide 4/4 and blocks divide 4/4, but the
              # CAPITULUM LINE falls between nn.6 and 7 -- two notes below
              # both, because Cap. X opens INSIDE the right column rather than
              # at its head. So two of the three lines coincide and the third
              # dissents by two: the exact inverse of p.262, where the
              # capitulum boundary WAS the column boundary. Derived from
              # p5-c9's own per-note list; NO claim is made about how often
              # this shape has occurred in Pars V, which would need pp.252-261
              # re-derived. ONE runover POSITIVE, one NEGATIVE: p.263's own
              # gutter is POSITIVE (n.4 breaks at "Sub-" at the foot of the
              # left block and resumes UNNUMBERED at "inde" at the head of the
              # right; logged as p.263 n.4:gutter) while p.262 -> p.263 is
              # NEGATIVE (p.262's right block ends complete at n.7 "Inferius
              # pro documentorum E mandatorum." and p.263's left block opens
              # NUMBERED with n.1 "Epist. II. Cor. 3, 6:").
              # CLOSED by bon-brev-p5-c10, which owns nn.7-8. Both forwarded
              # anchors HELD; ONE forwarded DETAIL did not -- p5-c9's
              # transcription italicised "verum" in "sicut est summe verum et
              # bonum in se ipso", and the plate sets it ROMAN (only
              # "misericors" and "iustum" are italic). Corrected in p5-c10.
    264: 6,   # band-read in full by p5-c10, which owns ALL SIX. THE PAGE WAS
              # NEVER IMAGED BEFORE THIS CHUNK -- extracted at 450 dpi and
              # measured fresh (gutter 1365, band midpoint; the tool's default
              # 1367 came off a 53 px run and the 45-92% window is UNSAFE on
              # this leaf because both body columns END at ~66% of page height,
              # so six lower windows returned 237-457 px blow-outs). NO
              # capitulum line on the leaf: Cap. X is the only capitulum on it.
              # Anchors divide 2/4 (nn.1-2 LEFT column on "per sensum verborum"
              # and "sunt septem", nn.3-6 RIGHT on "cum dicitur: Fiat voluntas
              # tua", "universaliter", "ut apparebit inferius", "septies in
              # die") against a 3/3 BLOCK split -- n.3's anchor is on the
              # SECOND body line of the RIGHT column while its entry prints in
              # the LEFT block, a one-note overrun of the left block past the
              # column division. NOTHING IS FORWARDED: Cap. X, and with it
              # PARS V, closes about 66% down p.264's right column, fixed
              # POSITIVELY from the full-width "PARS SEXTA. / De medicina
              # sacramentali." display heading standing at the HEAD of p.265
              # (which BREAKS the precedent of PARS QUARTA and PARS QUINTA,
              # both of which opened part-way down a leaf). ALL THREE runover
              # tests NEGATIVE, each closed from both sides: p.263 -> p.264
              # (p.263 R block ends complete at n.8 "...omittunt miseriam."
              # and p.264 L block opens NUMBERED "Cfr. IV. Sent. d. 15."),
              # p.264's own gutter (L block ends complete at n.3 "D F G M U et
              # 2 subditur." and R block opens NUMBERED at n.4 "F N utiliter."),
              # and p.264 -> p.265 (p.264 R block ends complete at n.6 "Psalm.
              # 118, 164." and p.265 L block opens NUMBERED "Isidor., VI.
              # Etymolog. c. 19. n. 40."). p.265's register is SIX and is
              # PARS VI's entire -- it is deliberately NOT entered here; it is
              # bon-brev-p6-c1's to read and to own. The printer's signature
              # "S. Bonav. -- Tom. V." and the quire signature "34" both stand
              # on p.265 (not on p.264); neither is an entry and neither is
              # counted.
    265: 6,   # band-read in full by p6-c1, which owns ALL SIX. PARS VI's
              # opening leaf: the full-width "PARS SEXTA. / De medicina
              # sacramentali." display heading stands at the HEAD of the page,
              # so the whole leaf is Cap. I and no Pars V text is on it.
              # Gutter 1150 (per-column ink profile: blank band x=1125-1177,
              # printed column rule inked at x=1142-1159 peaking on x=1151,
              # band midpoint 1151; the tool's no-constant default of 1121 on
              # a 4 px run is a LOUD failure and was rejected). ANCHORS DIVIDE
              # 3/3 AGAINST A 2/4 BLOCK SPLIT: nn.1-3 anchor in the LEFT column
              # ("operatur", "quia divinum", "a sensibus carnis") and nn.4-6 in
              # the RIGHT ("sanetur et curetur", "gratiae vasa", "Sacramentis"),
              # while the LEFT footer block holds only nn.1-2 and the RIGHT
              # block opens at n.3 -- i.e. n.3's entry prints one block to the
              # RIGHT of its anchor's column, the mirror of p.264's overrun.
              # Both runover tests NEGATIVE, each closed from both sides:
              # p.265's own gutter (L block ends complete at n.2 "...I K L O U
              # disponit." and R block opens NUMBERED "Cfr. supra p. III.
              # c. 3.") and p.265 -> p.266 (p.265 R block ends complete at n.6
              # "...substituimus potentiam pro gratiam." and p.266 L block
              # opens NUMBERED "Secundum Aristot., II. de Anima, text. 49.").
              # p.266's register is NOT entered here: p6-c1 owns only p.266
              # n.1 (anchor "a forma et a fine", LEFT column, inside Cap. I's
              # tail); nn.2 ff. anchor in Cap. II and are a legitimate
              # forwarded PENDING until bon-brev-p6-c2 lands, which must also
              # log p.266's POSITIVE gutter runover (n.3 breaks at a comma on
              # "...vitium editionis," and continues unnumbered in the right
              # block).
    266: 6,   # band-read in full by p6-c2, which owns nn.2-6; n.1 is p6-c1's
              # (anchor "a forma et a fine", LEFT column, in Cap. I's tail).
              # Gutter 1422, re-derived here rather than adopted (per-column
              # ink profile: near-zero band x=1398-1446, printed column rule
              # inked at x=1413-1431 peaking 517 rows on x=1415, midpoint
              # 1422; the tool's default 1425 on a 53 px run stays REJECTED).
              # THE BLOCK SPLIT IS 3/3 AND THE ANCHOR SPLIT IS 2/4, AND THEY
              # ARE NOT THE SAME 3/3: nn.1-2 anchor in the LEFT column
              # ("a forma et a fine", "virtute efficaciora") and nn.3-6 in the
              # RIGHT ("evidentior appareret", "sicut dicit Hugo", "veritatis
              # et gratiae", "exercerent imperfectos"), while the LEFT footer
              # block holds nn.1-3 and the RIGHT block opens with n.3's
              # UNNUMBERED continuation before nn.4-6. n.3 therefore straddles
              # both: anchor in the right column, entry beginning in the left
              # block -- p.266's own gutter runover, POSITIVE, logged by p6-c2
              # as `p.266 n.3:gutter` (breaks at a comma on "...vitium
              # editionis," and resumes at "quam, relictis codicibus...").
              # The p.266 -> p.267 page-crossing test is NEGATIVE, closed from
              # both sides (p.266 R block ends complete at n.6 "...in libertate
              # spiritus ambulare permittit." and p.267 L block opens NUMBERED
              # "Cfr. IV. Sent. d. 1. p. I. q. 2. ad 4"). p.267's register is
              # NOT entered here: p6-c2 owns only nn.1-2 (anchors "de
              # longinquo" and "et pleniori", both LEFT column, in Cap. II's
              # tail); nn.3 ff. anchor in Cap. III and are a legitimate
              # forwarded PENDING until bon-brev-p6-c3 lands, which must also
              # log p.267's own POSITIVE gutter runover (n.4 breaks at a comma
              # on "...post reparativum Vat.," and continues unnumbered in the
              # right block).
    267: 8,   # band-read in full by p6-c3, which owns nn.3-8; nn.1-2 are
              # p6-c2's (anchors "de longinquo" and "et pleniori", both LEFT
              # column, in Cap. II's tail). Gutter 1163, re-derived by p6-c3
              # from the tool's own default plus an eleven-window sweep: nine
              # sound windows 1161-1169 on runs 58-63 px, while the 15-35% and
              # 25-45% windows blew out to 387 px and 119 px runs on Cap. III's
              # heading and were discarded. Figure for figure the value p6-c2
              # reached independently by the ink profile (near-zero band
              # x=1137-1190, column rule x=1159-1171, midpoint 1163).
              # THE BLOCK SPLIT AND THE ANCHOR SPLIT ARE BOTH 4/4 AND ON THIS
              # LEAF THEY COINCIDE: nn.1-4 anchor in the LEFT column ("de
              # longinquo", "et pleniori", "resurrectionis universalis", "Dei
              # virtus et sapientia") and nn.5-8 in the RIGHT ("conservatio
              # introductae salutis", "sicut dicit Hieronymus", "complementum
              # et summa", "castrorum acies ordinata"), while the LEFT footer
              # block holds nn.1-4 and the RIGHT block opens with n.4's
              # UNNUMBERED continuation before nn.5-8. This coincidence is a
              # fact about THIS leaf only -- p.266, one leaf back, ran 3/3
              # against 2/4 -- and nothing may be predicted from it.
              # p.267's own gutter runover is POSITIVE and is logged by p6-c3
              # as `p.267 n.4:gutter` (n.4 breaks at a comma on "...Superius
              # post reparativum Vat.," and the right block resumes UNNUMBERED
              # at "1 et 3 addunt et curativum nostrorum morborum..."). The
              # p.267 -> p.268 page-crossing test is NEGATIVE, closed from both
              # sides (p.267 R block ends complete at n.8 "Cantic. 6, 3. et 9."
              # and p.268 L block opens NUMBERED "Eph. 5, 32: Sacramentum hoc
              # magnum est."). p.268's register is NOT entered here: p6-c3 owns
              # only p.268 n.1 (anchor "sit Sacramentum magnum", LEFT column,
              # in Cap. III's closing period); nn.2 ff. anchor in Cap. IV and
              # are a legitimate forwarded PENDING until bon-brev-p6-c4 lands,
              # which must also run p.268's own gutter test and re-derive n.3's
              # long "d. 3 ... d. 26" chain, the densest 1/4 risk in Pars VI.
    268: 8,   # band-read in full by p6-c4, which owns nn.2-8; n.1 is p6-c3's
              # (anchor "sit Sacramentum magnum", LEFT column, in Cap. III's
              # closing period). Gutter 1370, re-derived by p6-c4 from scratch
              # rather than adopted: the tool's default 1374 on a 49 px run
              # stays REJECTED, five windows blow out on the Cap. IV heading,
              # and an independent per-column ink profile over rows 35-85%
              # reproduced p6-c3's band edges digit for digit (near-zero band
              # x=1341-1400, printed column rule inked x=1367-1373 peaking 176
              # rows on x=1369, midpoint 1370).
              # THE BLOCK SPLIT IS 4/4 AND THE ANCHOR SPLIT IS 3/5, AND THEY DO
              # NOT COINCIDE: nn.1-3 anchor in the LEFT column ("sit
              # Sacramentum magnum", "novi testamenti mediator", "et etiam
              # primus suscepit") and nn.4-8 in the RIGHT ("via, veritas et
              # vita", "in quantum incarnatum", "plenum gratiae et veritatis",
              # "absque omni fictione", "ex diversis Evangelii locis"), while
              # the LEFT footer block holds nn.1-4 and the RIGHT block opens
              # with n.4's UNNUMBERED continuation before nn.5-8. n.4 therefore
              # straddles: anchor in the right column, entry begun in the left
              # block. ONE LEAF BACK p.267 ran 4/4 against 4/4; the same block
              # shape over two different anchor splits is why block, column and
              # capitulum structure stay three independent things.
              # p.268's own gutter runover is POSITIVE and is logged by p6-c4
              # as `p.268 n.4:gutter`. NOTE THE FORM: n.4 ends the left block
              # with a COMPLETED SENTENCE ("...A S beneficia.") and continues
              # unnumbered at the head of the right block ("Subinde pro
              # repararetur 2 cum pluribus codd. reparetur, et E perveniatur
              # pro perveniretur.") -- the apparatus-level case of the frozen
              # rule that a grammatically complete tail is not evidence a unit
              # ended. p6-c3 read the left block as ending "COMPLETE" here and
              # correctly declined to log the test, not having read the right
              # block. The p.268 -> p.269 page-crossing test is NEGATIVE,
              # closed from both sides (p.268 R block ends complete at n.8
              # "- Matth. 19, 4. seqq." and p.269 L block opens NUMBERED "Cap.
              # 6, 13. - Ibid. 10, 13..."). p.269's register is NOT entered
              # here: p6-c4 owns only p.269 nn.1-2 (anchors "sicut dicitur in
              # Marco" and "et ceteris publicando", both LEFT column, inside
              # Cap. IV's Pro thesi 3 period); nn.3 ff. anchor in Cap. V and
              # are a legitimate forwarded PENDING until bon-brev-p6-c5 lands,
              # which must also run p.269's own gutter test (forwarded UNLOGGED
              # -- the left block breaks off mid-word inside n.4 at "...ubi de
              # in-", but n.4 is Cap. V's) and the p.269 -> p.270 test.
    269: 8,   # band-read in full by p6-c5, which owns nn.3-8; nn.1-2 are
              # p6-c4's (anchors "sicut dicitur in Marco" and "et ceteris
              # publicando", both LEFT column, inside Cap. IV's Pro thesi 3
              # period). Gutter 1186, RE-DERIVED by p6-c5 from scratch rather
              # than adopted: the tool's default 1185 sits on a 59 px run, one
              # pixel below the trust floor, six windows blow out (146-394 px)
              # on the Cap. V heading and the short right-column footer, six
              # survivors agree 1185-1188 on runs 61-64 px, and an independent
              # per-column ink profile over rows 35-85% reproduced p6-c4's band
              # edges digit for digit (near-zero band x=1156-1215, printed
              # column rule inked x=1183-1189 peaking 767 rows on x=1186,
              # midpoint 1185.5 -> 1186). The heavy rule is WHY the default run
              # is pinched to 59 px.
              # THE BLOCK SPLIT IS 4/4 AND THE ANCHOR SPLIT IS 3/5, AND THEY DO
              # NOT COINCIDE -- the same shape p.268 showed one leaf back.
              # nn.1-3 anchor in the LEFT column ("sicut dicitur in Marco",
              # "et ceteris publicando", "requiritur ordo sacerdotalis") and
              # nn.4-8 in the RIGHT ("dispensentur secundum veritatem",
              # "quia in quantum Deus et homo", "operatus est enim salutem",
              # "et ex intentione", "media mediocribus"), while the LEFT footer
              # block holds nn.1-4 and the RIGHT block opens with n.4's
              # UNNUMBERED continuation before nn.5-8. The Cap. IV/Cap. V
              # boundary falls INSIDE the left block, between nn.2 and 3 --
              # block, column and capitulum structure, three independent things
              # again on one leaf.
              # p.269's own gutter runover is POSITIVE and is logged by p6-c5
              # as `p.269 n.4:gutter`. NOTE THE FORM, which is NOT p.268's:
              # n.4 breaks off MID-WORD AND HYPHENATED at the left block's foot
              # ("...ubi de in-") and continues unnumbered at the head of the
              # right block ("tentione; d. 5. a. 1. et 2, ubi de ministro
              # baptismi..."). p6-c4 forwarded this test UNLOGGED, having read
              # only the left side; p6-c5 closed it from BOTH sides. The
              # p.269 -> p.270 page-crossing test is NEGATIVE, closed from both
              # sides (p.269 R block ends complete at n.8 "Vat., 1 et 3
              # mediis." and p.270 L block opens NUMBERED "Eccle. 9, 1.").
    270: 5,   # band-read in full by p6-c5, which owns only nn.1-2 (anchors
              # "utrum amore, an odio dignus sit" and "Unde Augustinus contra
              # Donatistas", both LEFT column, inside Cap. V's Postremo
              # period); nn.3-5 anchor in Cap. VI in the RIGHT column and are a
              # legitimate forwarded PENDING until bon-brev-p6-c6 lands.
              # Gutter 1373, SETTLED FRESH with no constant on a leaf that had
              # not been imaged: default 1374 on a 59 px run, four windows blow
              # out (93-305 px) -- three of them on the Cap. VI heading set
              # mid-right-column, the p.263 failure mode exactly -- eight
              # survivors agree 1371-1373 on runs 61-64 px, and the ink profile
              # fixes the near-zero band at x=1344-1402 with the printed column
              # rule at x=1371-1376 peaking 573 rows on x=1372 (midpoint 1373).
              # p.270 REPEATS p.269's straddle in the same place: n.4's entry
              # begins in the LEFT block, breaks off mid-quotation at "quod
              # baptismus sit fundamentum omnium", and continues unnumbered at
              # the head of the RIGHT block, while its anchor is in the right
              # column. p.270's own gutter runover is therefore POSITIVE, but
              # n.4 is Cap. VI's and p6-c5 forwarded the test UNLOGGED rather
              # than double-logging someone else's runover. p6-c6 CLOSED that
              # test from both sides and logged it as `p.270 n.4:gutter`; the
              # page is now fully consumed (nn.1-2 p6-c5, nn.3-5 p6-c6, with
              # n.4 anchoring on "non fuisse factum" and n.5 on "potissime
              # tamen hoc observare debet", both first-read by p6-c6, which the
              # hand-off had explicitly declined to claim).
    271: 8,   # band-read in full by p6-c6, which owns nn.1-4; nn.5-8 anchor in
              # Cap. VII in the RIGHT column and are a legitimate forwarded
              # PENDING until bon-brev-p6-c7 lands.
              # Gutter 1202, SETTLED FRESH with no constant on a leaf that had
              # not been imaged: default 1204 on a 61 px run -- inside the sound
              # band for the first time in this quire, and still not adopted on
              # its own showing -- ONE window blows out (15-35% -> 1271 on a
              # 204 px run, on Cap. VI's "Rursus" opening and the Pro thesi 2
              # gloss), twelve survivors run 1200-1204 on runs 60-64 px with the
              # value drifting monotonically down the leaf (page skew, not
              # disagreement), and the ink profile fixes the near-zero band at
              # x=1173-1232 (60 px) with the printed column rule at x=1200-1206
              # peaking 541 rows on x=1202 (band midpoint 1202.5) -> 1202.
              # The rule inked more lightly here (541 rows against p.269's 767
              # and p.270's 573), which is WHY this default was not pinched.
              # THE BLOCK SPLIT IS 4/4 AND THE ANCHOR SPLIT IS 3/5, AND THEY DO
              # NOT COINCIDE -- the same shape as pp. 268 and 269, with p.270
              # between them NOT sharing it. Left block nn.1-4, ALL COMPLETE,
              # no straddle; right block nn.5-8. Anchors: nn.1-3 LEFT column
              # ("quaedam etiam", "videlicet in acie", "qui ad pugnandum"),
              # nn.4-8 RIGHT ("debet poena imponi" and Cap. VII's). n.4 is the
              # divergence: its entry closes the LEFT block, its anchor is in
              # the RIGHT column. The Cap. VI / Cap. VII boundary falls exactly
              # AT the block break, between nn.4 and 5 -- a coincidence on this
              # leaf, not a rule; it fell inside the left block one leaf back.
              # p.271's own gutter test is NEGATIVE and is logged by p6-c6
              # (left block ends complete at n.4 "multi codd. sua, 2 alia.",
              # right block opens NUMBERED at "C I K L M O V cuiuslibet."), as
              # is the p.270 -> p.271 page-crossing test, also NEGATIVE (p.270's
              # right block ends complete at n.5 "in hoc." and p.271's left
              # block opens NUMBERED at "Ed. 1 addit quae."). p6-c7 MUST NOT
              # re-log either.
    272: 8,   # band-read in full by p6-c7, which owns nn.1-7; n.8 anchors in
              # Cap. VIII ("audacter et publice confitendum", RIGHT column) and
              # is a legitimate forwarded PENDING until bon-brev-p6-c8 lands.
              # Gutter 1326, SETTLED FRESH with no constant on a leaf that had
              # not been imaged: default 1326 on a 62 px run, and still not
              # adopted on its own showing. SEVEN of twelve windows blow out
              # (1401/223, 1401/222, 1340/95, 1333/246, 1347/106, 1256/336,
              # 1224/271, 1224/272) -- the heaviest crop in Pars VI, because the
              # Cap. VIII heading is set mid-right-column at ~40% AND the left
              # column runs short of the right. The five survivors agree to
              # 4 px (1322/65, 1326/63, 1326/64, 1326/64, 1326/62), and the ink
              # profile fixes the near-zero band at x=1296-1357 (62 px) with the
              # printed column rule at x=1323-1328 peaking 220 rows on x=1327
              # (band midpoint 1326.5) -> 1326. The rule inked LIGHTLY here
              # (220 rows against p.271's 541 and p.270's 573), which is WHY
              # this default was not pinched.
              # BLOCK SPLIT 5/3 AND ANCHOR SPLIT 5/3 -- THEY COINCIDE, AND THE
              # CAPITULUM BOUNDARY DOES NOT FALL AT EITHER. Left block nn.1-5
              # with n.5 STRADDLING the gutter; right block n.5's unnumbered
              # continuation, then nn.6-8. Anchors: nn.1-5 LEFT column, nn.6-8
              # RIGHT. The Cap. VII / Cap. VIII boundary falls two notes lower
              # than the block break, INSIDE the right block between nn.7 and 8.
              # The 4/4-block-vs-3/5-anchor shape of pp.268, 269 and 271 does
              # NOT recur here.
              # p.272's own gutter test is POSITIVE and is logged by p6-c7 as
              # `p.272 n.5:gutter` (n.5 breaks off at "Vat., 1 et 3 addunt seu"
              # and the right block opens UNNUMBERED with "diaphaneitate.");
              # the p.271 -> p.272 page-crossing test is NEGATIVE and is also
              # closed by p6-c7 (p.271's right block ends complete at n.8
              # "neque deficiunt in necessariis." and p.272's left block opens
              # NUMBERED at "Epist. I. Cor. 15, 4."). p6-c8 MUST NOT re-log
              # either.
    273: 7,   # band-read in full by p6-c8, which owns nn.1-6; n.7 anchors in
              # Cap. IX ("super panem scilicet: Hoc est corpus meum", RIGHT
              # column) and is a legitimate forwarded PENDING until
              # bon-brev-p6-c9 lands.
              # Gutter 1164, SETTLED FRESH with no constant on a leaf that had
              # not been imaged, and THE DEFAULT WAS REJECTED: colcrop returns
              # 1161 on a 54 px run, below the 60 px trust floor. Two windows
              # blow out (1283/283, 1241/201); the TEN survivors run 1172/62,
              # 1170/63, 1169/61, 1167/60, 1164/59, 1164/59, 1163/60, 1161/59,
              # 1159/59, 1158/61 -- a 14 px spread that drifts MONOTONICALLY
              # down the leaf, i.e. page skew, not disagreement. The ink profile
              # fixes the blank band at x~1138-1189 with the printed column rule
              # inside it as a SKEWED island (x~1164-1171 in the upper body rows,
              # x~1156-1161 in the lower) peaking 382 rows; band midpoint 1163.5,
              # rule centre ~1164 -> 1164 adopted. The rule inked HEAVILY here
              # (382 rows against p.272's 220), which is WHY the default was
              # pinched.
              # BLOCK SPLIT 5/3, ANCHOR SPLIT 4/3 -- THEY DO NOT COINCIDE, AND
              # THE CAPITULUM BOUNDARY FALLS AT NEITHER. Left block nn.1-5 with
              # n.5 STRADDLING the gutter; right block n.5's unnumbered
              # continuation, then nn.6-7. Anchors: nn.1-4 LEFT column, nn.5-7
              # RIGHT -- so n.5's ENTRY is in the left block while its ANCHOR is
              # in the right column. The Cap. VIII / Cap. IX boundary falls one
              # note lower still, between nn.6 and 7 inside the right block:
              # three different places. p.272's coincident 5/3 did NOT propagate.
              # p.273's own gutter test is POSITIVE and is logged by p6-c8 as
              # `p.273 n.5:gutter` (n.5 breaks off at "Subinde pro propulsandam
              # I M O V" and the right block opens UNNUMBERED with
              # "propellendam, L repellendam"); the p.272 -> p.273 page-crossing
              # test is NEGATIVE and is also closed by p6-c8 (p.272's right block
              # ends complete at n.8 "Post crucis aliqui codd. addunt et." and
              # p.273's left block opens NUMBERED at "De hac veritatis
              # definitione cfr. tom. I. pag. 707, nota 5."). p6-c9 MUST NOT
              # re-log either.
              # NOTE: p.273 carries the printer's signature "S. Bonav. - Tom. V."
              # at the foot of the left block and the quire number 35 at the foot
              # of the right; neither is a footer entry.
    274: 8,   # band-read in full by p6-c9, which owns ALL EIGHT -- the first leaf
              # in Pars VI that no capitulum boundary touches at all.
              # Gutter 1403, SETTLED FRESH with no constant on a leaf that had not
              # been imaged, and THE DEFAULT WAS NOT ADOPTED ON ITS OWN SHOWING:
              # colcrop returns 1403 on a pinched 56 px run. ONE window blows out
              # (70-89% -> 1261/341 px); the ELEVEN survivors run 1399/64, 1399/64,
              # 1399/64, 1401/60, 1403/60, 1403/60, 1404/62, 1405/63, 1404/63,
              # 1405/60, 1404/57 -- a 6 px spread drifting MONOTONICALLY UP the
              # leaf, i.e. page skew in the OPPOSITE direction from p.273's, not
              # disagreement. The ink profile fixes the near-zero band at
              # x=1372-1432 with Quaracchi's printed column rule inside it at
              # x=1398-1405 peaking 871 rows on x=1403 -- BY FAR the heaviest
              # inking measured anywhere in Pars VI (p.273's 382, p.272's 220),
              # and precisely why the default run came back pinched. Band midpoint
              # 1402, rule centre 1403 -> 1403 adopted.
              # BLOCK SPLIT 5/3 AND ANCHOR SPLIT 5/3 -- THEY COINCIDE, AND THERE
              # IS NO CAPITULUM BREAK ON THE LEAF. Left block nn.1-5 with n.5
              # STRADDLING the gutter; right block n.5's unnumbered continuation,
              # then nn.6-8. Anchors: nn.1-5 LEFT column, nn.6-8 RIGHT.
              # p.274's own gutter test is POSITIVE and is logged by p6-c9 as
              # `p.274 n.5:gutter` (n.5 breaks off at "ut nos redimeret etc. --"
              # and the right block opens UNNUMBERED with "Pro ad finem plures
              # codd. in finem."); the p.273 -> p.274 page-crossing test is
              # NEGATIVE and is also closed by p6-c9 (p.273's right block ends
              # complete at n.7 "Vat., 1 et 3 addunt nec localiter." with the
              # quire number 35 beneath, and p.274's left block opens NUMBERED at
              # "Epist. I. Cor. 11, 29."). p6-c10 MUST NOT re-log either.
              # NOTE: p.274's LEFT COLUMN FOOT carries a large blank of some
              # fifteen lines. It is NOT a boundary.
    275: 7,   # band-read in full by p6-c9, which owns nn.1-4; nn.5-7 anchor in
              # Cap. X and are legitimate forwarded PENDINGs until bon-brev-p6-c10
              # lands. n.5 anchors on Cap. X's "secunda tabula post naufragium" in
              # the LEFT column; nn.6-7 fall in the RIGHT column, which p6-c9 did
              # not set -- their column is INFERRED, not read.
              # Gutter 1145, SETTLED FRESH, AND THE DEFAULT WAS REJECTED OUTRIGHT:
              # colcrop returns 1127 on an 18 px run, three px above the tool's own
              # 15 px failure flag. The windows FORK: the EIGHT sound upper windows
              # run 1156/62, 1156/61, 1155/60, 1154/61, 1152/60, 1151/60, 1148/59,
              # 1147/59 (a 9 px MONOTONIC drift), while the FOUR lower windows
              # collapse to 1129/23, 1124/28, 1124/27, 1123/26 and are discarded.
              # The ink profile explains the fork: the blank band runs x~1119-1170
              # with the printed column rule inside it as a SKEWED island moving
              # from x~1152-1158 in the upper body rows to x~1138-1150 in the
              # lower, peaking 372-447 rows -- so low on the leaf the rule sits
              # well right of centre and leaves only the left sub-band as a zero
              # run. Band midpoint 1144.5, rule centre 1145.5 -> 1145 adopted.
              # BLOCK SPLIT 4/3, ANCHOR SPLIT 5/2, CAPITULUM BREAK AT THE BLOCK
              # BREAK. Left block nn.1-4 with n.4 STRADDLING the gutter; right
              # block n.4's unnumbered continuation, then nn.5-7. Anchors: nn.1-5
              # LEFT column, nn.6-7 RIGHT -- the FIRST leaf in this pars where the
              # anchor split runs LOWER than the block split rather than higher.
              # p.275's own gutter test is POSITIVE and is logged by p6-c9 as
              # `p.275 n.4:gutter` (n.4 breaks off at "qui etiam inferius cum" and
              # the right block opens UNNUMBERED with "nonnullis aliis codd. pro
              # excessivum substituunt excellentissimum"); the p.274 -> p.275
              # page-crossing test is NEGATIVE and is also closed by p6-c9
              # (p.274's right block ends complete at n.8 "cum uno alteroque cod.
              # in qua." and p.275's left block opens NUMBERED at "Edd., excepta
              # 2, vel."). p6-c10 MUST NOT re-log either.
              # ** p6-c10 RE-DERIVED all of this. nn.5-7 are now owned; the
              # INFERRED column of nn.6-7 was READ and the inference proved
              # RIGHT: n.6 anchors on "ab Ecclesiae sponso" nine lines into the
              # RIGHT column, n.7 on "clementissimi, non semel nec bis" ~70%
              # down it. Gutter 1145 re-measured from scratch and confirmed
              # (same fork, same ink profile). **
    276: 6,   # band-read in full by p6-c10, which owns nn.1-5; n.6 anchors in
              # Cap. XI (on "loco et tempore", closing its Thesis 4, in the
              # RIGHT column below the CAP. XI. heading) and is a legitimate
              # forwarded PENDING until bon-brev-p6-c11 lands.
              # Gutter 1392, SETTLED FRESH with no constant on a leaf never
              # before imaged, and THE DEFAULT IS SOUND ON ITS OWN SHOWING for
              # the first time in this quire: colcrop returns 1392 on a 63 px
              # run, inside the 58-64 px trust band. Five surviving windows run
              # 1394/64, 1394/63, 1394/63, 1393/64, 1392/63 -- a 2 px spread --
              # against blow-outs of 117, 86, 86, 354, 164 and 325 px thrown by
              # the mid-column Cap. XI heading and by the short columns above a
              # tall footer register. Ink profile: over rows 45-92% the zero
              # band runs x=1360-1423 with the printed column rule inside it at
              # x=1390-1395 peaking 336 rows (midpoint 1391.5, rule centre
              # 1392.5); over rows 15-55% the band runs x=1362-1424 with the
              # rule at x=1392-1396 peaking 1227 rows (midpoint 1393, centre
              # 1394). The rule inks far more heavily in the UPPER half of this
              # leaf than the lower, and the run stayed sound anyway -- heavy
              # inking pinches a run only when the rule sits off the band's
              # centre. 1392 adopted.
              # BLOCK SPLIT 3/3, ANCHOR SPLIT 4/2, CAPITULUM BREAK AT 5/1 --
              # THREE DIFFERENT PLACES, and the first leaf in Pars VI where the
              # capitulum break falls BELOW both the block and the column break.
              # Left block nn.1-3 with n.3 STRADDLING the gutter; right block
              # n.3's unnumbered continuation, then nn.4, 5, 6. Anchors: nn.1-4
              # LEFT column, nn.5-6 RIGHT.
              # p.276's own gutter test is POSITIVE and is logged by p6-c10 as
              # `p.276 n.3:gutter` (n.3 breaks off at "ubi sub hoc triplici" and
              # the right block opens UNNUMBERED with "respectu explicantur
              # diversae definitiones poenitentiae"); the p.275 -> p.276
              # page-crossing test is NEGATIVE and is also closed by p6-c10
              # (p.275's right block ends complete at n.7 "excepta 2,
              # convertibilis." with blank paper beneath and p.276's left block
              # opens NUMBERED at "Vat., 1 et 3 praefigunt apparere et.").
              # p6-c11 MUST NOT re-log either.
              # NOTE: the p.275 -> p.276 BODY crossing falls at a PARAGRAPH
              # boundary -- p.275's right column ends a complete sentence and
              # p.276's left column opens "Rursus," -- and Cap. X nevertheless
              # runs a whole further leaf. Not a boundary.
    277: 7,   # band-read in full by p6-c11, which owns nn.1-6; n.7 anchors in
              # Cap. XII (on "quo spiritualis potestas traditur ordinato",
              # closing its Thesis 1, in the RIGHT column below the CAP. XII.
              # heading) and is a legitimate forwarded PENDING until
              # bon-brev-p6-c12 lands.
              # Gutter 1247, SETTLED FRESH with no constant on a leaf never
              # before imaged, and THE DEFAULT IS NOT SOUND: colcrop returns
              # 1245 on a 56 px run, BELOW the 58-64 px trust band -- so p.276's
              # sound default set no trend. Thirteen row windows drift
              # MONOTONICALLY 1257 -> 1243 on runs held at 58-63 px (10-30% ->
              # 1257/62, 15-35% -> 1255/60, 20-40% -> 1254/58, 25-45% -> 1254/58,
              # 30-50% -> 1252/59, 35-55% -> 1251/60, 40-60% -> 1250/63,
              # 45-65% -> 1248/62, 50-70% -> 1248/62, 55-75% -> 1247/61,
              # 60-80% -> 1245/60, 70-90% -> 1243/61), with one blow-out
              # discarded (65-85% -> 1253 on an 80 px run). A monotonic drift is
              # the leaf's SKEW, not disagreement. Ink profile confirms and
              # measures the skew directly: over rows 45-92% the zero band runs
              # x=1221-1273 with the printed column rule inside it at
              # x=1240-1252 peaking 596 rows (midpoint 1247, rule centre 1246);
              # over rows 15-55% the band runs x=1226-1281 with the same rule at
              # x=1248-1259 peaking 451 rows (midpoint 1253.5). The band itself
              # moves 6.5 px down the leaf. Body-band midpoint decides: 1247.
              # BLOCK SPLIT 4/3, ANCHOR SPLIT 4/3, CAPITULUM BREAK AT 6/1 --
              # block and column COINCIDE for the first time in six leaves, and
              # the capitulum break sits two notes below both. Left block
              # nn.1-4 with NO straddle (n.4 ends complete at "nota 4."); right
              # block opens NUMBERED at n.5, then nn.6, 7. Anchors: nn.1-4 LEFT
              # column, nn.5-7 RIGHT.
              # BOTH runover tests on this leaf are NEGATIVE and are closed by
              # p6-c11 from both sides: p.277's own gutter (left block ends
              # complete, right block opens numbered) and the p.276 -> p.277
              # page crossing (p.276's right block ends complete at n.6
              # "d. 23. per totam." with blank paper beneath, p.277's left block
              # opens NUMBERED at "Epist. I. Tim. 2, 5."). p6-c12 MUST NOT
              # re-log either; it owes the p.277 -> p.278 test and p.278's own
              # gutter test.
              # NOTE: the p.276 -> p.277 BODY crossing falls MID-SENTENCE and
              # MID-PHRASE ("Verbum" / "scilicet incarnatum") -- the exact
              # opposite shape from the p.275 -> p.276 paragraph-boundary
              # crossing one leaf earlier. Neither shape is evidence about
              # where a capitulum ends; only the next Cap. N. heading is.
    278: 5,   # band-read in full by p6-c12, which owns ALL FIVE -- the leaf lies
              # wholly inside Cap. XII. Anchors: n.1 "Dominus pars hereditatis
              # meae 1 etc." in the LEFT column; nn.2-5 in the RIGHT
              # ("ad thronum Salomonis 2;", "purgandi et illuminandi 3;",
              # "ordines ordinarie dispensare 4.", "in ecclesiastica
              # hierarchia 5."). BLOCK 2.5/3.5, ANCHORS 1/4, NO capitulum split
              # -- a tenth distinct arrangement in Pars VI, and the first whose
              # LEFT block opens with an INHERITED continuation (p.277 n.7's).
              # Gutter 1351, settled fresh with no constant: the default gave
              # 1350 on a 56 px run (below the 58-64 px trust band), thirteen
              # row windows agreed 1345-1352 on runs of 59-63 px with no fork
              # and no blow-out, and the ink profile put the zero band at
              # x=1323-1380 with Quaracchi's printed column rule inside it at
              # x=1348-1355 peaking 1062 rows -- band midpoint 1351.5, rule
              # centre 1351.5. The rule sits dead square and is simply inked
              # hard, which pinches the run without moving the centre.
              # RUNOVERS: the p.277 -> p.278 page crossing is POSITIVE and is
              # logged by p6-c12 as `p.277 n.7:page` (p.277's right block ends
              # INCOMPLETE at "cfr. IV. Sent. d. 24." and p.278's left block
              # opens UNNUMBERED at "et 25. -- P hic et infra ordinando");
              # p.278's own gutter is POSITIVE and is logged as
              # `p.278 n.2:gutter` (n.2 breaks off at "habebat sex gradus etc.
              # -- De perfectione" and the right block opens UNNUMBERED at
              # "numeri senarii cfr. I. Sent. d. 2. q. 4. scholion."); the
              # p.278 -> p.279 crossing is NEGATIVE. p6-c13 MUST NOT re-log any
              # of these.
              # NOTE: the leaf's BODY crosses this gutter at a CLEAN PARAGRAPH
              # BREAK while its FOOTER straddles -- block, column and capitulum
              # structure remain three independent things.
    279: 7,   # band-read in full by p6-c12, which owns n.1 ONLY; nn.2-7 anchor
              # in Cap. XIII and belong to p6-c13 (legitimately PENDING, not a
              # gap). n.1 anchors on "et dedicatio ecclesiarum 1;" in the LEFT
              # column, in Cap. XII's closing period; n.2 on "individuam vitae
              # consuetudinem retinens 2 »." in Cap. XIII's Thesis 1, also LEFT
              # but BELOW the Cap. XIII heading; nn.3 LEFT, nn.4-7 RIGHT.
              # BLOCK 3/4, ANCHORS 3/4, CAPITULUM 1/6 -- an eleventh distinct
              # arrangement in seventeen leaves of Pars VI.
              # Gutter 1191, settled fresh with no constant: the default gave
              # 1191 on a 51 px run, one blow-out discarded (15-35% -> 1151 on
              # a 138 px run), the surviving windows drifting 1188->1197, and
              # the ink profile put the zero band at x=1166-1216 with the
              # printed column rule OFF CENTRE inside it at x=1189-1199 peaking
              # 747 rows (band midpoint 1191, rule centre 1194). The body-band
              # midpoint decides: 1191. The windows reading 1195-1197 are
              # reading the rule, not the gutter.
              # RUNOVER: p.279's own gutter is POSITIVE and is logged by p6-c12
              # as `p.279 n.3:gutter` (n.3 breaks off at "(praeter impedimentum
              # aetatis, quod includitur secundum" and the right block opens
              # UNNUMBERED with the last two impediment verses). The straddling
              # note is Cap. XIII's, but the LEAF's gutter test is run by the
              # chunk that first reaches the leaf -- as p6-c10 did for p.276.
              # p6-c13 MUST NOT re-log it; it owes the p.279 -> p.280 test and
              # p.280's own gutter test.
              # NOTE: Cap. XII's close is fixed POSITIVELY from the Cap. XIII
              # heading in p.279's LEFT column, ~50% down. The running head
              # reads "PARS VI. C. XIII." while 43% of the left column is still
              # Cap. XII.
    280: 6,   # band-read in full by p6-c13, which owns ALL SIX -- the leaf lies
              # wholly inside Cap. XIII and PARS VI CLOSES HERE with its last
              # register complete and NOTHING forwarded.
              # BLOCK 2/4 (left nn.1-2, right nn.3-6, the right block opening
              # NUMBERED), ANCHORS 3/3 (nn.1-3 LEFT, nn.4-6 RIGHT), CAPITULUM
              # 6/0 -- a twelfth distinct arrangement in eighteen leaves of
              # Pars VI, and still block and anchor disagree by one note.
              # Gutter 1331, settled fresh with no constant. The default gave
              # 1328 on a 30 px run -- HALF the trust band -- because Cap. XIII's
              # body ENDS at row 2415/3823 (63.2%), the leaf is bare from 63% to
              # 80%, and the footer register sits at 80-89%: the tool's default
              # 45-92% window therefore straddles three regions with three
              # different ink geometries. Nine windows confined to rows 10-65%
              # agree 1330-1331 on runs of 61-64 px (the tightest agreement in
              # the quire), and the body-rows (12-62%) ink profile puts the zero
              # band at x=1301-1361 with the printed column rule inside it at
              # x=1328-1334 peaking 1622 rows -- band midpoint 1331 and rule
              # centre 1331 coinciding exactly. A NEW member of the "body window
              # is not safe" family: A UNIT'S EARLY END, with the blank tail and
              # the footer both inside the default window. Expect it at every
              # pars and work boundary in Vols V-X.
              # RUNOVERS: p.279 -> p.280 page-crossing NEGATIVE (p.279's right
              # block ends complete at "in corp." with blank paper; p.280's left
              # block opens NUMBERED). p.280's own gutter NEGATIVE (left block
              # ends complete at "ponit communis."; right block opens NUMBERED).
              # p.280 -> p.281 PARS-BOUNDARY test NEGATIVE (p.281's left block
              # opens NUMBERED; p.281's right block opens unnumbered with the
              # continuation of p.281's OWN n.3, "Cfr. su-" / "pra p. II. c. 9.
              # et 12."). Nothing crosses the pars boundary.
              # [?] p.280 n.6 ends "homo non separe" -- no final t, no period,
              # and the far-side test proves it is NOT a runover. Plate defect,
              # transcribed as printed and flagged.
              # NOTE: Cap. XIII's close -- and the close of PARS VI -- is fixed
              # POSITIVELY from the full-width PARS SEPTIMA display heading and
              # its "De statu finalis iudicii" subtitle at the head of p.281,
              # never from p.280's very large blank tail.
    281: 5,   # band-read in full by p7-c1, which owns ALL FIVE -- the leaf lies
              # wholly inside Cap. I, the first capitulum of PARS VII.
              # BLOCK 3/2 (left nn.1-3, right n.3's UNNUMBERED continuation then
              # nn.4-5), ANCHORS 3/2 (nn.1-3 LEFT, nn.4-5 RIGHT), CAPITULUM 5/0.
              # Block and anchor coincide here; on p.280 they did not, and no
              # inference is drawn from the coincidence.
              # Gutter 1231, RE-MEASURED with no constant. The default gave 1230
              # on a 55 px run, below the trust band, and this leaf is the
              # structurally unsafe kind the frozen rule names: the full-width
              # PARS SEPTIMA display heading CROSSES THE GUTTER and blows out
              # every window above 30% (5-25% -> 1315/347 px, 15-35% -> 1328/351,
              # 20-40% -> 1210/115). Nine windows confined to body rows 30-90%
              # agree 1227-1236 on runs of 60-63 px, and the body-rows ink
              # profile puts the zero band at x=1206-1258 with the printed column
              # rule inside it at x=1227-1239 peaking 658 rows -- band midpoint
              # 1231, rule centre 1233 -- stable across noise floors 1, 2 and 3.
              # RUNOVER: p.281's own gutter is POSITIVE and is logged by p7-c1 as
              # `p.281 n.3:gutter` (n.3 breaks off at "Cfr. su-"; the right block
              # opens UNNUMBERED at "pra p. II. c. 9. et 12."). NOTE that the
              # printer's signature "S. Bonav. -- Tom. V." sits directly beneath
              # that "Cfr. su-", so the test could NOT be closed from the upper
              # side and had to be closed from p.281's right block.
              # p.281 -> p.282 page-crossing NEGATIVE (p.281's right block ends
              # complete at "Vat., 1 et 3 boni." with quire 36 beneath it; p.282's
              # left block opens NUMBERED).
    282: 7,   # band-read in full by p7-c1, which owns nn.1-2 ONLY; nn.3-7 anchor
              # in Cap. II and are p7-c2's. n.1 anchors on "ut vult Augustinus 1,"
              # and n.2 on "facie ad faciem 2" -- BOTH in the LEFT column, inside
              # Cap. I. n.3 anchors on "suffragia ecclesiastica 3." ALSO in the
              # LEFT column, but inside Cap. II.
              # BLOCK 4/3 (left nn.1-4, right n.4's UNNUMBERED continuation then
              # nn.5-7), CAPITULUM 2/5 -- the capitulum boundary falls INSIDE the
              # left footer block AND inside the left column, three notes above
              # the block break. Three independent structures, none cutting where
              # another does.
              # Gutter 1357, settled fresh with no constant. The default gave
              # 1361 on a 56 px run; fourteen windows drift monotonically
              # 1345 -> 1364 on 51-64 px runs (the signature of an OFF-CENTRE
              # column rule), and the body-rows ink profile puts the zero band at
              # x=1333-1382 with the rule at x=1349-1367 peaking 461 rows --
              # band midpoint 1357, rule centre 1358.
              # RUNOVER: p.282's own gutter is POSITIVE and is logged by p7-c1 as
              # `p.282 n.4:gutter` (n.4 breaks off at "De hoc cap. vide IV. Sent.
              # d. 20. p. I. per totam. --"; the right block opens UNNUMBERED at
              # "Pro quibus sufficienter purgatis P ..."). THE STRADDLING NOTE IS
              # NOT p7-c1's -- it is p7-c2's -- but the test is logged by p7-c1
              # under the standing rule that a leaf's gutter test belongs to the
              # chunk that FIRST reaches the leaf, exactly as p6-c12 logged
              # `p.279 n.3:gutter` for a note p6-c13 owned. p7-c2 MUST NOT re-log
              # it and MUST render n.4 joined.
              # p.282 -> p.283 page-crossing NEGATIVE, closed from both sides by
              # p7-c1 (p.282's right block ends complete at "B Q et 2 lenius."
              # with blank paper; p.283's left block opens NUMBERED at
              # "I L O alium, quam sit eorum."). p7-c2 need not re-run it.
              # NOTE: Cap. I's close is fixed POSITIVELY from the Cap. II heading
              # and its TWO-line "De antecedentibus ad iudicium, cuiusmodi est
              # poena purgatoria" subtitle at ~40% of p.282's LEFT column --
              # never from the index, never from p.282's running head (which
              # already reads "BREVILOQUII PARS VII. C. II." while 40% of the
              # leaf is still Cap. I), never from white space.
              # ANCHOR SPLIT COMPLETED by p7-c2: nn.1-3 LEFT, nn.4-7 RIGHT, so
              # the anchor split is 3/4 while the BLOCK split is 4/3 -- the block
              # break falls one note BELOW the anchor break.
    283: 6,   # band-read in full by p7-c2, which owns nn.1-3 ONLY; nn.4-6 anchor
              # in Cap. III and are p7-c3's. n.1 anchors on "in quo sunt illi 1
              # qui in inferno irremediabiliter cruciantur.", n.2 on "vel, ut
              # magis credo 2," and n.3 on "cum inveniat 3 receptaculum idoneum"
              # -- ALL THREE in the LEFT column, inside Cap. II. n.4 anchors on
              # "« nec valde" ALSO in the LEFT column, but inside Cap. III.
              # BLOCK 4/2 (left nn.1-4, right n.4's UNNUMBERED continuation then
              # nn.5-6), CAPITULUM 3/3 -- the capitulum boundary again falls
              # INSIDE the left footer block and inside the left column, above
              # the block break. Same architecture as p.282; a coincidence, and
              # nothing is inferred from it for p.284.
              # Gutter 1169, settled fresh with no constant -- AND THE DEFAULT IS
              # RIGHT. The default's 55 px run is NOT a truncated run: the left
              # column's ink dies at x=1142 and the right column's resumes at
              # x=1197, so the blank band is x=1143-1196, genuinely 54 px wide.
              # Thirteen windows 10-89% agree 1166-1174 on 58-63 px runs; the
              # 5-25% window blows out to 1339 on a 364 px run and is discarded.
              # The printed rule stands inside the band at x=1164-1178 peaking
              # 1455 rows -- the heaviest inking met anywhere in the quire -- but
              # is close enough to centred (rule centre 1171, band midpoint
              # 1169.5) not to corrupt the answer.
              # RUNOVER: p.283's own gutter is POSITIVE and is logged by p7-c2 as
              # `p.283 n.4:gutter` (n.4 ends at "Enchirid. c. 109. n. 29." with
              # blank paper beneath; the right block opens UNNUMBERED at "Ibid.
              # in Comment. a. 2. agitur de suffragiis Ecclesiae pro defunctis").
              # THE STRADDLING NOTE IS NOT p7-c2's -- it is p7-c3's -- but the
              # test is logged by p7-c2 under the standing rule that a leaf's
              # gutter test belongs to the chunk that FIRST reaches the leaf.
              # p7-c3 MUST NOT re-log it and MUST render n.4 joined.
              # p.283 -> p.284 page-crossing NEGATIVE, closed from both sides by
              # p7-c2 (p.283's right block ends complete at "ex G H I K L M V ad
              # iunximus Deo." with blank paper; p.284's left block opens
              # NUMBERED at "Cap. 2. n. 4. -- Superius pro accuratio F P
              # curatio."). p7-c3 need not re-run it.
              # NOTE: Cap. II's close is fixed POSITIVELY from the Cap. III
              # heading and its TWO-line "De antecedentibus ad iudicium,
              # cuiusmodi sunt suffragia ecclesiastica" subtitle at ~55% of
              # p.283's LEFT column -- never from the index, never from p.283's
              # running head (which already reads "PARS VII. C. III." while more
              # than half the left column is still Cap. II), and never from the
              # grammatically complete tail at "spiritus iam purgatus."
    284: 10,  # band-read in full by p7-c3, which owns nn.1-6 ONLY; nn.7-10
              # anchor in Cap. IV and are p7-c4's. The LARGEST register on any
              # leaf of Pars VII so far. n.1 anchors on "de Cura pro mortuis
              # agenda 1,", n.2 on "salvetur ordo et symbolum 2", n.3 on "ut et
              # ipsi suffragentur nobis 3", n.4 on "dum erant in statu viae 4.",
              # n.5 on "licet sint spiritualia 5," -- ALL FIVE in the LEFT
              # column -- and n.6 on "et mensuram 6." in the RIGHT column, on
              # Cap. III's last words.
              # BLOCK 5/5 (left nn.1-5, right nn.6-10), ANCHOR 5/5, CAPITULUM
              # 6/4 -- block and anchor coincide at the gutter and the capitulum
              # boundary falls INSIDE the right footer block, between nn.6 and
              # 7. That is the mirror of p.283, where the capitulum cut inside
              # the LEFT block while block and anchor coincided. Nothing is
              # inferred from either for p.285.
              # Gutter 1386, settled fresh with no constant. The default is a
              # LOUD FAILURE: 1404 on a 21 px run. Eight windows from 5-65%
              # agree 1385-1388 on 61-64 px runs; every window from 50% down
              # collapses to 1404-1405 on 21-24 px runs and is discarded. The
              # body-rows ink profile puts the zero band at x=1354-1417 (64 px)
              # with a LIGHTLY inked rule inside it at x=1382-1388 peaking 69
              # rows -- a twentieth of p.283's inking -- band midpoint 1385.5,
              # rule centre 1385. The 21 px "run" is the zero sub-band lying to
              # the RIGHT of the rule only. p.283 and p.284 are exact
              # complements: a heavy centred rule that did not move the answer,
              # and a faint centred rule that destroyed the run anyway because
              # this leaf's noise floor is 2 rows. Ink weight and displacement
              # are independent and neither predicts the other.
              # RUNOVERS: p.284's own gutter NEGATIVE (left block ends complete
              # at n.5's "(L fiunt)." with a very large blank tail and no
              # printer's signature; right block opens NUMBERED at n.6).
              # p.284 -> p.285 page-crossing NEGATIVE, closed from both sides
              # (p.284's right block ends complete at n.10's "Cfr. supra Prolog.
              # § 2. et p. II. c. 4. in fine." with blank paper; p.285's left
              # block opens NUMBERED at "Vide Glossam in Isai. 30, 26."). p.285
              # was extracted and measured (gutter 1234, fourteen windows
              # 1234-1235 on 61-65 px runs, band x=1204-1264) for that test
              # alone -- p7-c4 must re-derive it.
              # NOTE: Cap. III's close is fixed POSITIVELY from the Cap. IV
              # heading and its TWO-line "De concomitantibus iudicium, sicut est
              # conflagratio ignium" subtitle at ~22% of p.284's RIGHT column --
              # never from the index, never from p.284's running head (which
              # already reads "BREVILOQUII PARS VII. C. IV." while the whole
              # left column and the head of the right are still Cap. III), never
              # from white space, and never from the grammatically complete tail
              # at "numerum et mensuram."
              # ⚠⚠ WITHDRAWN BY p7-c4 (2026-08-01). This comment previously
              # read "THE RAW CARRIES NO FOOTER BLOCK FOR THIS LEAF AT ALL ...
              # not a degraded footer but a MISSING one". THAT IS FALSE. The
              # raw carries p.284's footer IN FULL, all ten notes, at
              # doctorisseraphic05bona_djvu.txt L~51528-51562, in the ordinary
              # moderate grade -- and it independently confirms "Gen. 7, 1" and
              # "p. II. c. 4.", two of the four hardest digits on the leaf. The
              # claim was a structural generalisation, written once and never
              # re-derived, and it contradicted nothing in its own chunk's
              # per-note data because per-note data cannot speak to it. The
              # frozen rules it was cited for stand: apparatus IS bands-only,
              # the raw IS a cross-check and never the base.
    285: 8,   # band-read in full and OWNED IN FULL by p7-c4 -- the only leaf of
              # that chunk of which both are true. Left block nn.1-4 with n.4
              # STRADDLING the gutter, breaking off MID-WORD at "sola avaritia
              # iu-" with no blank tail; right block opens UNNUMBERED at
              # "venescit. -- Pro refrigerium D refrigidationem..." then nn.5-8,
              # ending complete at "B I K L T quia amplius." with blank paper.
              # ANCHORS: n.1 "debuit quietari 1.", n.2 "divinum accipiat zelum
              # 2", n.3 "cum homine expurgando 3;", n.4 "propter refrigerium
              # caritatis 4" -- all four LEFT; n.5 "sensibilis facies exuretur
              # 5.", n.6 "cum homine innovato 6;", n.7 "necesse est, facta 7",
              # n.8 "posito statu in animabus 8," -- all four RIGHT.
              # BLOCK 4/4, ANCHOR 4/4, CAPITULUM 8/0.
              # Gutter 1234, RE-DERIVED with no constant rather than adopted
              # from p7-c3's recorded value: sixteen windows from 5-95% agree
              # 1234-1235 on 61-65 px runs, and the body-rows ink profile puts
              # the zero band at x=1204-1264 (61 px) with a moderately inked
              # CENTRED rule at x=1231-1236 peaking 185 rows. Midpoint 1234.
              # RUNOVERS: p.285's own gutter POSITIVE (logged p.285 n.4:gutter,
              # closed from both sides). p.285 -> p.286 page-crossing NEGATIVE,
              # closed from both sides (p.285's right block ends complete with
              # blank paper; p.286's left block opens NUMBERED at "Cfr. tom.
              # III. pag. 40, nota 8.").
              # RAW: footer PRESENT and moderate, but wrong in TWO places --
              # "Serm. i8." for "Serm. 48." and "K P U" for "F P U". The band
              # decides both.
    286: 8,   # band-read in full by p7-c4, which owns n.1 ONLY; nn.2-8 anchor
              # in Cap. V and are p7-c5's. Left block nn.1-4 with n.4
              # STRADDLING the gutter, breaking off at "Inferius pro
              # stipendiorum I K L" with a large blank tail and no printer's
              # signature; right block opens UNNUMBERED at "O P V praemiorum,
              # D ..." then nn.5-8, ending complete at "in resurrectionem
              # iudicii." with blank paper.
              # n.1 anchors on "cum omni genere creaturae 1;" in the LEFT
              # column, five lines above the Cap. V heading.
              # BLOCK 4/4, CAPITULUM 1/7 -- the capitulum boundary falls INSIDE
              # the LEFT footer block, between nn.1 and 2, while the block break
              # falls at the gutter.
              # Gutter 1342, measured fresh: sixteen windows 1341-1343 on 59-62
              # px runs, ink band x=1313-1371 (59 px) with a VERY HEAVILY inked
              # rule at x=1339-1344 peaking 473 rows, almost exactly centred,
              # against a 3-row noise floor -- and it does not corrupt the
              # answer at all. p.283's case, not p.284's.
              # RUNOVERS: p.286's own gutter POSITIVE (logged p.286 n.4:gutter
              # by p7-c4 on the standing rule that a leaf's gutter test belongs
              # to the chunk that FIRST reaches the leaf; p7-c5 owns n.4, must
              # render it JOINED, and must NOT re-log it). The p.286 -> p.287
              # page-crossing was NOT run and is p7-c5's to close.
              # NOTE: Cap. IV's close is fixed POSITIVELY from the Cap. V
              # heading and its TWO-line "De concomitantibus iudicium, sicut est
              # resurrectio corporum" subtitle at ~20% of p.286's LEFT column --
              # never from the index, never from p.286's running head (which
              # already reads "BREVILOQUII PARS VII. C. V." while its first six
              # lines are still Cap. IV), never from white space, and never from
              # the grammatically complete tail at "quodam modo praemiari."
    287: 9,   # band-read in full by p7-c5, which owns nn.1-5 ONLY; nn.6-9 anchor
              # in Cap. VI and are p7-c6's. Left block nn.1-5 with n.5
              # STRADDLING the gutter, breaking off MID-WORD at "in corp., ex
              # qua quae-" with a blank tail and no printer's signature; right
              # block opens UNNUMBERED at "dam supra pag. 216, nota 3. ..."
              # then nn.6-9, ending complete at "et pro summa D divina, M sua."
              # with blank paper.
              # Anchors: nn.1-5 LEFT (n.1 "licet non in mole 1", n.2 "habet
              # fieri 2", n.3 "caro secundum materiam 3", n.4 "facere frustra
              # 4", n.5 "generabile sit corruptibile 5"); nn.6-9 RIGHT.
              # BLOCK 5/4, ANCHOR 5/4, CAPITULUM 5/4 -- all three coincide on
              # this leaf, because the Cap. VI heading falls three lines into
              # the right column and above every one of that column's anchors.
              # A fact about this leaf, NOT a pattern: p.286 one leaf back has
              # block and anchor coinciding at 4/4 while the capitulum splits
              # 1/7.
              # Gutter 1163, measured fresh, DEFAULT REJECTED: colcrop with no
              # constant returns 1160 on a 55 px run -- a quiet failure under
              # the 60 px floor. Twelve windows 20-75% agree 1162-1163 on 61-64
              # px runs; ink band x=1133-1193 (61 px), midpoint 1163, with the
              # HEAVIEST centre rule met anywhere in this quire at x=1158-1164
              # peaking 1127 rows, sitting 2 px LEFT of the band centre, which
              # is what dragged the default down.
              # RUNOVERS: p.287's own gutter POSITIVE (logged p.287 n.5:gutter
              # by p7-c5); the p.286 -> p.287 page-crossing NEGATIVE, closed
              # from both sides by p7-c5 (p.286's right block ends complete at
              # n.8 with blank paper; p.287's left block opens NUMBERED at
              # "1 Ut ait August. XXII. de Civ. Dei, c. 14."). The p.287 ->
              # p.288 crossing was NOT run and is p7-c6's to close; its upper
              # side is done (n.9 ends complete, blank paper, no signature).
              # NOTE: Cap. V's close is fixed POSITIVELY from the Cap. VI
              # heading and its TWO-line "De consequentibus ad iudicium, sicut
              # est poena infernalis" subtitle three lines down p.287's RIGHT
              # column -- never from the index, never from p.287's running head
              # (which already reads "PARS VII. C. VI." while its whole left
              # column and the head of its right column are still Cap. V),
              # never from white space, never from a break shape.
              # CORRECTION carried here: p.286 n.5 reads "I. Phys. text. 81.",
              # NOT "text. 84." as the p7-c4 hand-off transcribed it (glyph at
              # 12x, the raw at L~51882, and Book I of the Physics having only
              # 83 texts, all three agreeing).
    288: 6,   # band-read in full by p7-c6, which owns ALL SIX -- the four lines
              # of Cap. VII printed beneath its heading on this leaf carry NO
              # anchor, so nothing is forwarded from p.288's footer to p7-c7.
              # Left block nn.1-4 with n.4 STRADDLING the gutter, breaking off
              # ON A COLON, mid-citation, at "... Soph. 1, 12:" with a blank
              # tail and no printer's signature; right block opens UNNUMBERED
              # at "Visitabo super viros defixos in faecibus suis. Cfr. supra
              # c. 2. -- Superius pro affligendus K L O puniendus ..." then
              # nn.5-6, ending complete at "Vide supra pag. 180, nota 6. et
              # pag. 224, nota 8." with a very large blank tail.
              # Anchors: nn.1-4 LEFT (n.1 "Primo igitur 1", n.2 "in suo
              # perpetuo 2", n.3 "et partiale 3", n.4 "igne et sulphure
              # concremetur 4."); nn.5-6 RIGHT (n.5 "aliter comburitur
              # lignum 5.", n.6 "dictamen rationis rectae 6:").
              # BLOCK 4/2, ANCHOR 4/2, CAPITULUM 6/0 -- block and anchor
              # coincide at the gutter while the capitulum boundary falls
              # BELOW the whole register. On p.287, one leaf back, all three
              # coincided; nothing was inferred from that and nothing is
              # inferred from this.
    289: 10,  # band-read in full by p7-c7, which owns ALL TEN. Left block
              # nn.1-6 with n.6 STRADDLING the gutter, breaking off ON A
              # COLON, mid-citation, at "August., de Quantitate animae,
              # c. 36. n. 80 :" -- and THE PRINTER'S SIGNATURE
              # "S. Bonav. -- Tom. V." stands DIRECTLY BENEATH it, so this
              # leaf's gutter test cannot be closed from the upper side and
              # was closed from the lower. Right block opens UNNUMBERED at
              # "Subiicit [Deus] animae corpus, animam sibi et sic omnia
              # sibi. Cfr. VI. Music. c. 5. n. 13. et Enarrat. in Ps. 145.
              # n. 5. -- Paulo ante pro ordinate C D F G H ordinat." then
              # nn.7-10, ending complete at "... K O V vere beata et plene."
              # with the QUIRE NUMBER 37 beneath it. Neither the signature
              # nor the quire number is a footer entry.
              # Anchors: nn.1-6 LEFT (n.1 "facie ad faciem 1,", n.2 "qua 2
              # resumta", n.3 "continentiae virginali 3.", n.4 "per opera
              # 4;", n.5 "aliquid prope se 5,", n.6 "quam illustrat 6,");
              # nn.7-10 RIGHT (n.7 "in miseria constitutae 7.", n.8 "et
              # productio 8 Dei", n.9 "congregatione perfecto 9 >>", n.10
              # "naturaliter insertam 10;").
              # BLOCK 6/4, ANCHOR 6/4 -- they coincide, with the split
              # falling INSIDE n.6. CAPITULUM 0/10: all ten are Cap. VII's.
              # Gutter 1216, measured fresh with no constant: default
              # 1216/56px, fourteen of fifteen row windows sound and
              # agreeing 1213-1222 on 59-66px runs, ink profile band
              # x=1189-1245 (57px) midpoint 1217, centre rule x=1211-1213
              # peaking 672 rows and sitting WELL LEFT of the band centre.
    290: 7,   # band-read in full by p7-c7, which owns ALL SEVEN. Left block
              # nn.1-5 with n.5 STRADDLING the gutter, breaking off at a
              # WORD BOUNDARY after "Subinde post vita creata"; right block
              # opens UNNUMBERED at "P quanto melior vita creatrix...
              # quanto iucundior salus... quanto amabilior sapientia; cod. P
              # primum locum Anselmi tantum affert, ceteros omittit..." then
              # nn.6-7, ending complete at "... permulti codd. corporis tui,
              # ut." with a very large blank tail and no signature.
              # Anchors: nn.1-4 LEFT (n.1 "fit corpus spiritui conforme 1",
              # n.2 "in oram vestimenti 2,", n.3 "exercitia exteriora 3;",
              # n.4 "speciali 4 formositate"); nn.5-7 RIGHT (n.5 "Ait enim
              # in fine 5 Proslogii", n.6 "Qui hoc bono fruetur 6,", n.7
              # "fulgebunt iusti sicut sol 7.").
              # BLOCK 5/2 against ANCHOR 4/3 -- A ONE-NOTE OVERRUN: n.5
              # prints in the LEFT block and anchors in the RIGHT column.
              # CAPITULUM 0/7: all seven are Cap. VII's.
              # Gutter 1365, measured fresh with no constant, and ALL
              # SIXTEEN row windows FAILED (runs 208-452px, scattering
              # 1239-1427) while the default 1365/62px was right to half a
              # pixel: ink profile band x=1335-1396 (62px) midpoint 1365.5,
              # centre rule x=1363-1367 peaking 302 rows, exactly centred.
    291: 8,   # band-read in full by p7-c7, which owns ALL EIGHT. THE WORK'S
              # LAST REGISTER. Left block nn.1-4 ending COMPLETE at n.4's
              # four-word "Matth. 22, 37." with a very large blank tail and
              # NO straddle; right block opens NUMBERED at "5 Anselm. loc.
              # cit. c. 26." then nn.6-8, ending complete at "... substituit
              # es trinus." with a very large blank tail and no signature.
              # Anchors: nn.1-3 LEFT (n.1 "sine fine Deum laudantes 1.",
              # n.2 "supra multa constituet 2,", n.3 "quale aut quantum est
              # 3,"); nn.4-8 RIGHT (n.4 "toto corde, tota mente, tota anima
              # 4,", n.5 "Nondum ergo 5,", n.6 "vel 6 proficiam", n.7
              # "nostrum plenum sit 7.", n.8 "Amen 8 >>.").
              # BLOCK 4/4 against ANCHOR 3/5 -- a SECOND one-note overrun on
              # consecutive leaves (n.4 prints left, anchors right), and
              # this one with no straddle to disguise it.
              # CAPITULUM 0/8: all eight are Cap. VII's, and NOTHING is
              # forwarded -- the Breviloquium ends on this leaf, closed
              # POSITIVELY by the full-width centred colophon EXPLICIT
              # BREVILOQUIUM FRATRIS BONAVENTURAE printed across both
              # columns beneath the body. p.292 is BLANK PAPER ENTIRE and
              # p.293 is the Itinerarium's display half-title.
              # Gutter 1165, measured fresh: the default 1159/45px is a
              # QUIET SUB-60 FAILURE and was rejected; eleven of sixteen
              # windows sound at 1162-1168 on 60-63px runs; ink profile band
              # x=1137-1193 (57px) midpoint 1165, with the centre rule
              # printing as TWO parallel islands (x=1160-1163 peak 422 and
              # x=1166-1169 peak 483) spanning 1160-1169, centre 1164.5.
              # Gutter 1347, settled fresh with no constant, and the DEFAULT'S
              # PROVENANCE IS REJECTED even though its value is close: colcrop
              # returns 1348 on a healthy-looking 61 px run, but ELEVEN of
              # fifteen row windows blow out to 145-413 px and the four sound
              # survivors spread 11 px (1336/64, 1346/64, 1346/64, 1347/65) --
              # not a consensus. Step (3) settles it: left column dies at
              # x=1315, right resumes at x=1380, zero band x=1316-1379 (64 px),
              # midpoint 1347.5, with a moderately inked and almost exactly
              # CENTRED rule at x=1345-1350 peaking 166 rows. The band is also
              # split into four sub-runs by faint speckle, not by the rule.
              # LESSON: a sound 61 px default run can sit on a leaf whose
              # windows are in open disorder. Run width alone would not have
              # caught it; the per-column profile did.
              # RUNOVERS: p.288's own gutter POSITIVE (logged p.288 n.4:gutter
              # by p7-c6, closed from both sides). p.287 -> p.288 page-crossing
              # NEGATIVE, closed from both sides by p7-c6 (p.287's right block
              # ends complete at n.9 with blank paper and no signature;
              # p.288's left block opens NUMBERED at "1 B H addunt ratione.").
              # The p.288 -> p.289 crossing was NOT run and is p7-c7's; its
              # upper side is done (n.6 ends complete, large blank tail, no
              # printer's signature -- so quire 37 is NOT on p.288 and is due
              # on p.289).
              # NOTE: Cap. VI's close is fixed POSITIVELY from the Cap. VII
              # heading and its ONE-line "De gloria paradisi." subtitle at
              # ~60% of p.288's RIGHT column -- never from the index, never
              # from p.288's running head (which already reads "BREVILOQUII
              # PARS VII. C. VII." while the whole leaf down to 60% of its
              # right column is still Cap. VI), never from white space, and
              # NEVER FROM THE TAIL, which is the doxological "Amen." -- the
              # most boundary-looking end any unit in this work can have, and
              # still not evidence.
              # RAW: p.288's body moderate on the left and WORSE on the right,
              # printing "divino impeiio ordinanti" for the band's "divino
              # imperio ordinante," -- and n.5 corroborates the band by
              # lemmatising "ordinante". Its footer is good on every digit and
              # wrong on THREE siglum letters in three consecutive notes
              # ("1!}|" for B H, "U P" for G P, "K I K L 0 P" for E I K L O P).
    # --- ITINERARIUM (pp. 295-316) ---
    295: 8,   # band-read in full by bon-itin-prol, which owns ALL EIGHT.
              # Left block nn.1-5 ending COMPLETE at n.5's "montem quietum.";
              # right block opens NUMBERED at "6 Cfr. Vitae primae" then
              # nn.7-8, ending complete at "civitatem." No runovers.
              # Anchors: nn.1-5 LEFT, nn.6-8 RIGHT. p.293 = Itinerarium
              # half-title (verified), p.294 = MEASURED BLANK.
              # Gutter 1162: default 1163/55px borderline-suspect, confirmed
              # by re-profiling (three windows 1159-1163 on 55-64px runs).
    296: 6,   # band-read in full by bon-itin-prol. nn.1-4 = the prologue's
              # (nn.1-2 anchor LEFT, nn.3-4 RIGHT); n.5 anchors on
              # "EXPLICIUNT CAPITULA" -> FORWARDED to bon-itin-capitula;
              # n.6 anchors at "in loco, quem posuit" (Cap. I, right col
              # top) -> FORWARDED to bon-itin-c1. Blocks: nn.1-3 left,
              # nn.4-6 right. No runovers.
              # Gutter 1387: default 1363/48px pointed at the true channel;
              # direct ink profile shows the low channel x=1375-1399 in all
              # four page regions. Narrow-window "runs" of 300-450px on this
              # five-region leaf are the min-collection artifact, not bands.
    297: 10,  # band-read in full by bon-itin-c1, which owns ALL TEN. Left block
              # nn.1-6, n.6 breaking MID-WORD at "-- Su-" just above the
              # signature line "S. Bonav. -- Tom. V."; right block opens with
              # n.6's unnumbered continuation then nn.7-10. Blocks 6/4 but
              # anchors 5/5 (nn.1-5 LEFT column, nn.6-10 RIGHT) -- n.6 anchors
              # RIGHT and prints LEFT, a one-note underrun on top of a runover.
              # Gutter 1187: default 1178/44px REJECTED (under the 60px floor);
              # thirteen windows agree 1187-1188 on 60-63px runs, direct body
              # profile band x=1157-1215 with the centre rule inking at
              # x~1181-1190 (midpoint 1186). RAW: this page's body is the worst
              # in the Itinerarium so far -- it DROPS A WHOLE LINE at the page
              # foot ("posuit eum Deus in paradiso" jumps straight to p.298's
              # "commutabile bonum"), losing "deliciarum 10. Sed avertens se a
              # vero lumine ad", which n.10 independently lemmatises.
    298: 9,   # band-read in full by bon-itin-c1, which owns ALL NINE. Left
              # block nn.1-6 closing complete at "Prolog. sec. 2."; right block
              # opens NUMBERED at n.7 then nn.8-9. NO runover. Blocks 6/3 but
              # anchors 4/5 (nn.1-4 LEFT, nn.5-9 RIGHT) -- a two-note overrun.
              # Gutter 1377: default 1378/60px, eleven sound windows spread
              # 1375-1378, direct profile band x=1345-1408 (rule ~1374-1380).
              # SIX of twenty-six windows returned 1245-1311 on 209-458px runs
              # -- min-collection artifact, discarded on run width alone.
    299: 10,  # band-read in full by bon-itin-c1, which owns NINE; n.10 anchors
              # at "est altius" in Cap. II sec. 1 -> FORWARDED to bon-itin-c2.
              # Left block nn.1-7, n.7 breaking at a PUNCTUATION boundary after
              # "Aristot., de Praedicam. c. de Priori."; right block opens with
              # n.7's unnumbered continuation then nn.8-10. Of the nine owned,
              # blocks and anchors COINCIDE 7/2. Gutter 1172: default 1172/59px
              # borderline, twenty-five windows spread 1169-1175 on 59-65px
              # runs, direct band x=1142-1203 (rule ~1169-1174).
              # *** THIS PAGE IS THE RUNNING-HEAD TRAP: its head already reads
              # "... C. II." while Cap. I still fills the left column and most
              # of the right. Cap. I's terminus was fixed from the in-place
              # "Cap. II." HEADING in the right column, never from the head.
    300: 7,   # band-read in full by bon-itin-c2, which owns ALL SEVEN. Blocks
              # 5 L / 2 R but anchors 3 L / 4 R -- nn.4-5 PRINT LEFT and ANCHOR
              # RIGHT, a TWO-note overrun, the largest on the span. n.5 carries
              # this chunk's only runover: left block breaks at "Ibid. VIII.",
              # right footer opens with its unnumbered continuation "text. 27.
              # seqq. (c. 4.) agitur de motu animalium." Corroborated from the
              # plate itself: p.301 n.7 cites "supra pag. 300, nota 7", so the
              # register is independently known to be exactly 7. Gutter 1364:
              # default 1365/62px looks healthy but sits ON the centre rule
              # (peak 457 rows); true band x=1334-1393, midpoint 1364.
    301: 8,   # band-read in full by bon-itin-c2, which owns ALL EIGHT. Blocks
              # 5 L / 3 R, anchors 4 L / 4 R -- n.5 prints LEFT, anchors RIGHT,
              # a one-note overrun. No runover: both blocks open numbered and
              # close complete. Gutter 1228 confirmed (default 1228/60px; band
              # x=1198-1259, rule 1229 at 1078 rows).
    302: 8,   # band-read in full by bon-itin-c2, which owns ALL EIGHT. Blocks
              # 4 L / 4 R, anchors 3 L / 5 R -- n.4 prints LEFT, anchors RIGHT,
              # a one-note overrun, the THIRD consecutive leaf on which the
              # left block overran the column division. No runover. Gutter
              # 1346: colcrop's 1344 on a 55px run REJECTED under the sub-60
              # floor; band x=1317-1376 with the rule OFF-CENTRE at 1349, which
              # is what dragged the default low.
    303: 7,   # band-read in full by bon-itin-c2, which owns only nn.1-2 (both
              # anchor LEFT, in Cap. II sec. 12-13); nn.3-7 are Cap. III's and
              # are FORWARDED to bon-itin-c3. Blocks 5 L / 2 R. n.5 breaks
              # mid-entry across the gutter -- that runover is c3's to log, NOT
              # c2's. Gutter 1196: default 1198/60px sits on a very heavily
              # inked rule (peak 1518 rows), band x=1166-1225, midpoint 1196.
              # Cap. II's terminus fixed from the in-place "Cap. III." heading
              # ~40% down the LEFT column, never from the running head.
    304: 6,   # band-read in full by bon-itin-c3, which owns ALL SIX. Blocks
              # 5 L / 1 R but anchors 3 L / 3 R -- nn.4-5 PRINT LEFT and ANCHOR
              # RIGHT, a two-note overrun, the FIFTH consecutive leaf (300-304)
              # on which the left block overran the column division. n.5 carries
              # a gutter runover breaking MID-WORD at "cum te tran-" |
              # "scendis, ratiocinantem animam te transcendere". Gutter 1330:
              # default 1330 on a 58px run -- under the frozen floor, so
              # re-derived and CONFIRMED at the band midpoint (x=1301-1359,
              # rule 1322-1334 at 618 rows).
    305: 5,   # band-read in full by bon-itin-c3, which owns ALL FIVE. Blocks
              # 3 L / 2 R but anchors 4 L / 1 R -- n.4 PRINTS RIGHT and ANCHORS
              # LEFT, an UNDERRUN, reversing the direction after five straight
              # leaves of leftward overrun. This is why the block/anchor rule is
              # stated symmetrically: do not infer the sixth leaf from the five.
              # n.3 carries a gutter runover breaking just above the signature
              # line "S. Bonav. - Tom. V.". Gutter 1229: default 1229 on a 58px
              # run, CONFIRMED at the profile (band x=1201-1258); the centre
              # rule is the LIGHTEST inked on the span (peak 267 rows).
    306: 9,   # band-read in full by bon-itin-c3, which owns only n.1 (Psalm.
              # 75, 5, anchoring in Cap. III's four-line tail at the head of the
              # LEFT column); nn.2-9 are Cap. IV's and are FORWARDED to
              # bon-itin-c4. Blocks 4 L / 5 R; n.4 runs over the gutter and is
              # c4's to log, NOT c3's. Gutter 1325 (default 1325/59px, band
              # x=1296-1355, confirmed at the profile).
              # *** THE RUNNING-HEAD TRAP FIRED A THIRD TIME HERE: the head
              # reads "... C. IV." while Cap. III still holds the top of the
              # left column. Cap. III's terminus was fixed from the in-place
              # "Cap. IV." HEADING and its subtitle, never from the head.
    307: 9,   # band-read in full by bon-itin-c4, which owns ALL NINE. Blocks
              # 5 L / 4 R and anchors 5 L / 4 R -- they COINCIDE, as they also
              # do on p.306, after six straight leaves (300-305) on which they
              # came apart. Carry no licence from that: read anchors every leaf.
              # *** THE LEFT BLOCK OPENS WITH AN UNNUMBERED FRAGMENT -- it is
              # p.306 n.9's PAGE-CROSSING continuation ("electa ut sol. Tertius
              # ibid. 8, 5. ..."), logged under bon-itin-c4. A reader assuming
              # every block opens numbered would mis-assign it to n.1 or lose
              # it outright. Gutter 1263 (default 1262/60px, band x=1233-1293).
    308: 9,   # band-read in full by bon-itin-c4, which owns only nn.1-2 (both
              # anchor LEFT, in Cap. IV secs. 7-8); nn.3-9 are Cap. V's and are
              # FORWARDED to bon-itin-c5. Blocks 7 L / 2 R; n.7 runs over the
              # gutter and is c5's to log, NOT c4's.
              # *** GUTTER 1317, AND THE BODY-ONLY WINDOW FAILS ON THIS LEAF:
              # profiled over body rows alone it returns a 161 px "band"
              # (1286-1446) because Cap. V's heading + subtitle sit inside the
              # left column at ~40% depth. The body+footer profile gives the
              # true band x=1286-1349 (64 px), matching the 1317/61px default.
              # A 161px run is as much a failure signal as a 20px one.
              # *** AND p.308 n.9 CARRIES A PAGE-CROSSING RUNOVER that c4's
              # hand-off did not name, because c4 never read p.309's footer:
              # n.9 breaks at "...cognitione creaturae in se," and continues
              # UNNUMBERED at the head of p.309's LEFT footer ("de qua est
              # sermo in hoc capitulo..."). The seventh in all of Vol V, and
              # the second in consecutive chunks of this work. bon-itin-c5
              # logs it; c4 does not.
    309: 8,   # band-read in full by bon-itin-c5, which owns ALL EIGHT. The
              # left block opens with p.308 n.9's unnumbered continuation and
              # then carries nn.1-3 (n.3 runs over the gutter); the right
              # block carries nn.4-8. Blocks 3 L / 5 R, ANCHORS 4 L / 4 R --
              # the left block UNDERRUNS the column division by one note
              # (n.4 anchors LEFT, in sec. 5, but prints RIGHT). Direction
              # reverses again: p.308 overran left by four, p.309 underruns.
              # *** GUTTER 1164, from the direct body+footer ink profile:
              # true band x=1135-1194 (60 px), split by the centre rule into
              # two ~20 px sub-bands (1137-1156, 1173-1191). The tool's 1161
              # default sits toward the LEFT sub-band, 3 px off the band's
              # midpoint -- a healthy-looking 60 px run that is still not the
              # centre.
    310: 9,   # band-read in full by bon-itin-c5, which owns only nn.1-5
              # (nn.1-4 anchor LEFT; n.5 anchors RIGHT at Cap. V sec. 8's
              # "sunt omnia"5, the last paragraph of the chapter, which runs
              # over into the right column). nn.6-9 are Cap. VI's and are
              # FORWARDED to bon-itin-c6. Blocks 7 L / 2 R, ANCHORS 4 L / 5 R
              # -- the left block overruns by three notes, and *** THE
              # CAPITULUM BOUNDARY FALLS INSIDE THE LEFT BLOCK, between nn.5
              # and 6. Block, column and capitulum structure are three
              # independent things (the p.247 shape, recurring).
              # p.310 n.7 runs over the gutter; n.7 is c6's to log, NOT c5's.
              # *** GUTTER 1397: true band x=1365-1429 (65 px), two ~28 px
              # sub-bands (1367-1394, 1401-1428). The 1396/58px default was
              # sound -- a sub-60 run that was RIGHT, on the same span as a
              # 60 px run that was WRONG. Run width triggers the look; it
              # does not decide the answer.
    311: 7,   # band-read in full by bon-itin-c6, which owns ALL SEVEN.
              # Blocks 5 L / 2 R, ANCHORS 4 L / 3 R -- the left block
              # overruns by one note. nn.1-4 anchor LEFT (sec. 2's
              # "permixto"1 and "omnimodam"2, sec. 3's "nostrae"3 and
              # "ideo"4); nn.5-7 anchor RIGHT (sec. 4's "propitiatorium"5,
              # sec. 5's "formato"6, sec. 6's "substantiarum"7).
              # p.311 n.5 runs over the GUTTER, breaking mid-parenthesis
              # and mid-phrase at "...versis etc. (Non | pauci codd. in
              # propitiatorio)" -- the fragment reads as a fresh note if
              # you do not check. Logged by bon-itin-c6; NOT forwarded by
              # anyone. The left footer block opens NUMBERED, so nothing
              # crosses from p.310; checked, not assumed.
              # *** GUTTER 1172: true band x=1143-1202 (60 px) with the
              # centre rule inked at 1168-1174. The 1172/59px default --
              # under the frozen floor -- landed exactly on the band's
              # midpoint and was RIGHT.
    312: 9,   # band-read in full by bon-itin-c6, which owns ONLY nn.1-2
              # (both anchor LEFT, in Cap. VI sec. 7: "imaginem Dei"1 and
              # "quod patrarat"2 -- the chapter's last words). nn.3-9 are
              # Cap. VII's and are FORWARDED to bon-itin-c7. Blocks
              # 6 L / 3 R. *** THE CAPITULUM BOUNDARY FALLS INSIDE THE
              # LEFT BLOCK AGAIN, between nn.2 and 3, two leaves after the
              # same shape at p.310. For c6's own two notes block and
              # anchor COINCIDE -- the first coincidence since p.307, and
              # a fact about two notes, not about the leaf.
              # p.312 n.6 runs over the gutter into the right block
              # ("...Et comedetis [agnum paschalem] festi- | nanter; est
              # enim phase..."); n.6 is c7's to log, NOT c6's.
              # The left footer block opens NUMBERED, so nothing crosses
              # from p.311; checked, not assumed.
              # *** GUTTER 1388: true band x=1356-1420 (65 px), centre
              # rule at 1388-1389. Default confirmed at the midpoint.
    313: 6,   # band-read in full by bon-itin-c7, which owns ALL SIX --
              # *** EVEN THOUGH CAP. VII FILLS ONLY THE TOP TWO-FIFTHS OF
              # THE PAGE AND THE WORK-LEVEL SCHOLION FILLS THE MIDDLE.
              # Every one of the six answers to a Cap. VII anchor (nn.1-3
              # in sec. 5's Dionysian quotation, LEFT column; nn.4-6 in
              # sec. 6, RIGHT column), and the Scholion's own text carries
              # NO footnote anchors at all -- it cites inline instead.
              # bon-itin-scholion therefore inherits NOTHING from p.313.
              # Divide by anchor even when the anchors are in a different
              # WORK-UNIT, not merely a different column.
              # Blocks 3 L / 3 R, ANCHORS 3 L / 3 R -- they COINCIDE.
              # p.313 n.3 runs over the GUTTER, and the printer's
              # signature line "S. Bonav. -- Tom. V." prints BETWEEN its
              # two halves, at the foot of the left block. Logged by
              # bon-itin-c7. The left footer block opens NUMBERED, so
              # nothing crosses from p.312; checked, not assumed.
              # *** GUTTER: THIS PAGE HAS TWO, AND THE TOOL RETURNS THE
              # WRONG ONE. p.313 stacks three regions set to different
              # measures. Cap. VII body: band 1137-1195 (59 px), rule
              # 1165-1170 -> 1166, which is what c7 uses. Scholion body:
              # band 1129-1194 (66 px), rule 1160-1162 -> 1161. The
              # colcrop default row window (45-92%) straddles both bodies
              # and reports 1161 on a 49 px run -- the SCHOLION's value.
              # The footer band reads 149 px and is unusable (the left
              # block is narrower than the column, so its band runs on
              # into white space). *** PROFILE THE REGION YOU ARE
              # TRANSCRIBING, NOT THE PAGE, on any leaf where a work ends
              # and the next unit begins in a different type. This will
              # be constant in the Sermones.

    # ---- De reductione artium ad theologiam (bon-red, pp. 319-325) ----
    # Every page's FULL footer register was read off the 450 dpi bands in
    # one sitting. The whole work is a single chunk, so no page is shared
    # with a neighbour and nothing is forwarded in or out. Four gutter
    # runovers (319 n.3, 320 n.6, 323 n.8, 325 n.5) are rendered joined
    # and counted once each. *** NO page-crossing runover anywhere in the
    # work: pp. 320-325 each open their left footer block NUMBERED, and
    # all six joints were checked, not assumed.
    319: 6,
    320: 8,
    321: 8,   # left block closes on the signature line "S. Bonav. -- Tom. V."
    322: 8,
    323: 11,  # the heaviest leaf of the work
    324: 9,
    325: 9,   # last leaf; the bare centred colophon EXPLICIT. stands below both columns

    # ---- Collationes in Hexaemeron, Collatio I (bon-hex-c1, pp. 329-335) ----
    # The Hexaemeron's pilot chunk. Every page's full register read off the
    # 450 dpi bands. *** p. 331 n. 7 RUNS OVER TO p. 332, whose left footer
    # block opens UNNUMBERED with the Averroes exposition -- the first
    # page-crossing runover in this work and the eighth in Vol V. It is
    # rendered joined in [^p331-7] and is NOT counted again on p. 332.
    # p. 329's left block holds n. 1 alone: the note on the work's title in
    # the codices fills the whole block and then runs over the gutter.
    329: 6,
    330: 8,
    331: 7,
    332: 9,
    333: 9,
    334: 9,
    335: 9,   # Collatio I ends part-way down the right column; COLLATIO II opens p. 336

    # ---- Collatio II (bon-hex-c2, pp. 336-342) ----
    # Every register read off the 450 dpi bands. TWO page-crossing runovers,
    # both found only because the joints were read: *** p. 340 n. 9 continues
    # UNNUMBERED at the head of p. 341's left block ("sub nomine Dionysii
    # vulgati sunt..."), and *** p. 341 n. 10 continues UNNUMBERED at the head
    # of p. 342's left block ("de Trin. c. 1. n. 1. seqq. ..."). Both are
    # rendered joined in the note they belong to and are NOT counted again on
    # the receiving page. p. 341's block split is 2 L / 8 R against a 5 / 5
    # anchor split -- a THREE-note underrun, the widest divergence in this work
    # so far. Collatio II ends part-way down p. 342; COLLATIO III opens below it
    # in the same leaf and claims none of p. 342's seven notes.
    336: 8,
    337: 9,
    338: 9,
    339: 9,
    340: 9,
    341: 10,
    342: 7,

    # ---- Collatio III (bon-hex-c3, pp. 342-348) ----
    # Collatio III opens at the FOOT of p. 342 and carries NO anchor of its own,
    # so p. 342's seven notes are all Collatio II's; it closes part-way down
    # p. 348, where COLLATIO IV opens below it and likewise claims none of that
    # leaf's seven notes. Registers read off the bands. TWO gutter-crossing
    # runovers (p. 343 n. 5, p. 346 n. 7) and *** ZERO page-crossing -- checked
    # leaf by leaf, every left block opening numbered, after c2 had two.
    343: 8,
    344: 6,
    345: 11,
    346: 12,
    347: 12,
    348: 7,

    # ---- Collatio IV (bon-hex-c4, pp. 348-353) ----
    # Opens at the foot of p. 348 (no anchor on its heading) and closes
    # part-way down p. 353. *** p. 353's register SPLITS ACROSS THE WORK-UNIT
    # BOUNDARY: four notes, of which nn. 1-3 answer to Collatio IV's anchors
    # (n. 1 is the Augustine "fumo viso" note against IV n. 20's own text) and
    # n. 4 is Collatio V's first, forwarded to bon-hex-c5. That leaf also
    # carries Collatio V's full-width heading and Summarium AND its two-column
    # body. Three gutter runovers (350 n. 3, 351 n. 4, 352 n. 6); ZERO
    # page-crossing, checked leaf by leaf.
    349: 9,
    350: 6,
    351: 7,
    352: 7,
    353: 4,   # nn.1-3 Collatio IV, n.4 Collatio V — both now claimed
    354: 10,
    355: 12,  # nn.11-12 print side by side on one line
    356: 11,  # n.11 runs over onto p.357's left block, unnumbered
    357: 8,
    358: 7,
    359: 7,   # Collatio V closes here; nothing forwarded
    360: 6,
    361: 8,
    362: 8,
    363: 8,   # n.8 runs over onto p.364's left block, unnumbered
    364: 6,   # the left block holds ONLY that runover; all six print right
    365: 5,
    366: 8,
    367: 11,
    368: 7,   # all seven are Collatio VII's; Collatio VIII opens below, unanchored
    369: 11,
    370: 11,
    371: 6,
    372: 3,   # n.1 Collatio VIII, nn.2-3 Collatio IX
    373: 9,
    374: 10,  # n.10 runs over the page foot into p.375's left block, unnumbered
    375: 9,
    376: 10,
    377: 5,
    378: 8,
    379: 6,   # nn.1-5 Collatio X, n.6 Collatio XI
    380: 9,
    381: 11,
    382: 9,
    383: 8,
    384: 3,   # nn.1-2 Collatio XI, n.3 Collatio XII
    385: 10,
    386: 10,  # n.5 runs over the gutter; the right block opens unnumbered
    387: 4,   # ALL FOUR are Collatio XII's -- XIII's text on this leaf carries no anchor
    388: 9,
    389: 8,   # n.4 runs over the gutter; the right block opens unnumbered
    390: 7,   # block and anchor splits coincide
    391: 9,   # n.5 runs over the gutter; the right block opens unnumbered
    392: 7,   # ALL SEVEN are Collatio XIII's -- Collatio XIV contributes only heading+Summarium
    393: 7,   # n.4 runs over the gutter; the right block opens unnumbered
    394: 8,   # n.4 runs over the gutter
    395: 9,
    396: 8,
    397: 10,  # n.5 runs over the gutter
    398: 5,   # nn.1-2 Collatio XIV, nn.3-5 Collatio XV -- boundary leaf, now complete
    399: 11,  # block split 1-3 L / 4-11 R; anchor split 1-5 L / 6-11 R
    400: 12,  # n.7 runs over the gutter; the right block opens unnumbered
    401: 9,   # n.4 runs over the gutter; the right block opens unnumbered
    402: 7,   # block and anchor splits coincide; n.7 closes the collatio
    403: 4,   # Collatio XVI opens at the head of the leaf; left block overruns by one
    404: 9,   # block split 1-3 L / 4-9 R; anchor split 1-5 L / 6-9 R
    405: 11,  # n.7 runs over the gutter; the right block opens unnumbered
    406: 10,  # both blocks open numbered; no runover
    407: 7,   # n.5 runs over the gutter; n.7 runs over the PAGE into p.408's left block
    408: 8,   # left block opens unnumbered with p.407 n.7's tail; nothing forwarded to XVII
    409: 6,   # Collatio XVII opens at the head of the leaf; block and anchor splits coincide
    410: 7,   # SKEWED leaf; n.5 runs over the gutter, right block opens unnumbered
    411: 7,   # n.4 runs over the gutter; right block opens unnumbered
    412: 8,   # n.2 runs over the gutter; n.1 is long enough to push five entries right
    413: 10,  # both blocks open numbered; no runover
    414: 4,   # BOUNDARY LEAF: nn.1-3 are Collatio XVII's, n.4 is Collatio XVIII's -- both owners now present
    415: 8,   # left block underruns by one; right block opens numbered, no runover
    416: 9,   # n.7 runs over the gutter; right block opens unnumbered
    417: 9,   # both blocks open numbered; the S. Bonav. signature line is not an entry
    418: 9,   # both blocks open numbered; no runover
    419: 5,   # BOUNDARY LEAF: all five are Collatio XVIII's; n.4 runs over the gutter
    420: 9,   # Collatio XIX's register opens here, not on p. 419; n.8 runs over the gutter
    421: 8,   # both blocks open numbered; no runover
    422: 8,   # n.4 runs over the gutter; right block opens unnumbered
    423: 11,  # both blocks open numbered; no runover
    424: 7,   # BOUNDARY LEAF: all seven are Collatio XIX's; Collatio XX carries no anchor here
    425: 4,   # Collatio XX's register opens here; both blocks open numbered, no runover
    426: 8,   # n.4 runs over the gutter; right block opens unnumbered
    427: 8,   # n.4 runs over the gutter; left block underruns the column division by two
    428: 7,   # n.4 runs over the gutter; left block overruns by one
    429: 10,  # n.5 runs over the gutter; block and anchor splits coincide at 5/5
    430: 9,   # n.6 runs over the gutter; left block overruns by one
    431: 3,   # BOUNDARY LEAF: n.1 is Collatio XX's, nn.2-3 are Collatio XXI's
    432: 7,   # both blocks open numbered; no runover; block and anchor splits coincide at 4/3
    433: 8,   # n.5 runs over the gutter; splits coincide at 4/4; left block closes with the tome signature
    434: 6,   # left block UNDERRUNS the column division by one (n.4 anchors left, prints right)
    435: 9,   # both blocks open numbered; no runover; splits coincide at 4/5
    436: 6,   # n.4 (Dionysius) runs over the gutter; left block OVERRUNS by two
    437: 2,   # BOUNDARY LEAF: n.1 is Collatio XXI's, n.2 is Collatio XXII's
    438: 7,   # block splits 5/2, anchors 4/3 — n.5 prints left and anchors right
    439: 8,   # block splits 5/3, anchors 3/5 — the widest disagreement of the collatio
    440: 7,   # n.4 runs over the gutter; block 4/3, anchors 3/4
    441: 10,  # block 6/4, anchors 5/5; left block closes with the tome signature, right with the sheet number 56
    442: 8,   # n.5 runs over the gutter; block 5/3, anchors 3/5
    443: 11,  # n.11 RUNS OVER onto p. 444; block 5/6, anchors 4/7
    444: 3,   # BOUNDARY LEAF: p.443 n.11's runover, then nn.1-2 Collatio XXII's, n.3 Collatio XXIII's
    445: 10,  # all Collatio XXIII's; n.10 runs over onto p.446
    446: 9,   # all Collatio XXIII's
    447: 10,  # all Collatio XXIII's
    448: 10,  # all Collatio XXIII's
    449: 10,  # all Collatio XXIII's; n.10 explains EXPLICIUNT + ADDITAMENTUM.
              # The Additamentum's own heading+text is transcribed separately
              # as bare (non-page-qualified) apparatus entry `51`, anchored on
              # the colophon; it is not one of this page's ten numbered
              # footer notes and so is correctly invisible to this map.
    450: 1,   # bon-hex-scholion's sole entry: the reportator's colophon, an
              # unnumbered/unanchored page-foot quotation (not a Bonaventure
              # footnote) transcribed as bare entry p450-1.

    # --- Collationes de septem donis Spiritus Sancti (pp. 457-) ---
    # Every total below was read off the 450 dpi footer bands at 2.1-2.4x,
    # both blocks per leaf, on 2026-08-27.
    457: 7,   # block 2/5, anchors 4/3 (the left block underruns by two).
              # The signature line "S. Bonav. - Tom. V." and the gathering
              # signature "58" are furniture, not entries.
    458: 9,   # block 3/6, anchors 3/6.
    459: 11,  # block 7/4, anchors 7/4.
    460: 10,  # block 4/6, anchors 5/5. n. 10 BREAKS at the foot of the page
              # ("...Ego autem") and continues unnumbered at the head of
              # p. 461's left block; it is counted once, here.
    461: 8,   # block 5/3, anchors 5/3, PLUS the inherited unnumbered runover
              # of p. 460 n. 10 standing above n. 1 - which is p. 460's entry
              # and is not counted again here.
    462: 5,   # block 3/2, anchors 3/2.
    463: 8,   # block 4/4, anchors 2/6 (the left block OVERRUNS by two - the
              # mirror of p. 457's underrun).
    464: 7,   # block 5/2, anchors 3/4. n. 5 breaks across the COLUMN division
              # mid-sentence ("...apud Petr. Lombardum" / "(in hunc locum)
              # extensiore modo exhibetur"); it is one entry, counted once.
    465: 12,  # block 5/7, anchors 6/6. n. 5 breaks across the column division
              # mid-citation ("- Gen. 19," / "26: Respiciensque uxor eius").
              # The signature line "S. Bonav. - Tom. V." and the gathering
              # signature "59" are furniture, not entries.
    466: 11,  # block 6/5, anchors 5/6.
    467: 8,   # block 6/2, anchors 3/5. n. 8 closes cleanly; p. 468 opens
              # Collatio III, so no runover is forwarded.
    468: 4,   # block 3/1, anchors 3/1.
    469: 11,  # block 6/5, anchors 5/6 (the left block overruns by one: n. 6
              # prints left, anchors right).
    470: 7,   # block 4/3, anchors 4/3. n. 4 (the long Bernard citation) breaks
              # across the COLUMN division mid-sentence.
    471: 10,  # block 4/6, anchors 4/6.
    472: 10,  # block 5/5, anchors 4/6 (n. 5 prints left, anchors right). n. 3
              # is set flush right on n. 2's last line, not on its own line.
    473: 8,   # block 4/4. ONLY nn. 1-5 are Collatio III's; nn. 6-8 anchor in
              # Collatio IV, whose display heading stands MID-LEAF on p. 473.
              # bon-don-c4 owns 6-8; do not let c4 restart p. 473 at 1.
    474: 8,   # block 6/2, anchors 4/4 (nn. 5-6 print left, anchor right).
    475: 10,  # block 4/6, anchors 6/4 (nn. 5-6 anchor left, print right) --
              # the exact mirror of p. 474 on the facing leaf.
    476: 11,  # block 6/5, anchors 6/5. The only leaf of the c4 span on which
              # block and anchor splits coincide.
    477: 12,  # block 4/8, anchors 6/6. nn. 6 and 7 are set ON THE SAME LINE
              # (n. 7 flush right) -- read the block by numeral, not by line.
    478: 8,   # block 5/3, anchors 4/4. n. 5 breaks across the column division
              # mid-sentence. n. 7 reads Psalm. 118, 125 (the raw's 123 is wrong).
    479: 6,   # SHARED leaf: COLLATIO V.'s display heading stands mid-leaf, so
              # n. 1 is Collatio IV's and nn. 2-6 are Collatio V's. Full-leaf
              # block 3/3; of c5's five, block 2/3 and anchors 3/2 (n. 4 prints
              # right, anchors left). n. 6 RUNS OVER onto p. 480 and eats most of
              # that leaf's left block.
    480: 11,  # block 3/8, anchors 5/6. The left block is short only because
              # p. 479 n. 6's runover occupies it. n. 1 reads Isai. 52, 1 (raw
              # 32); n. 4 reads ibid. 10, 15 (raw 13); n. 5 reads et 24. seqq.
              # (raw 21).
    481: 9,   # block 5/4, anchors 2/7 -- the widest divergence in the c5 span.
              # nn. 3 and 4 are set ON THE SAME LINE (third attestation of that
              # mechanism). n. 1 reads Hexaem. collat. 14 (raw 11), confirmed by
              # bon-hex-c14 n. 23 being the Samson paragraph.
    482: 10,  # block 4/6, anchors 4/6 -- they coincide. n. 4 breaks across the
              # column division mid-sentence. ⚠ gutter is 1401, NOT colcrop's
              # default 1317 (448 px run: the window straddles the body/footer
              # gap); settled from the ink profile's band 1369-1433.
    483: 7,   # SHARED leaf: COLLATIO VI.'s display heading stands mid-leaf, so
              # nn. 1-2 are Collatio V's and nn. 3-7 are Collatio VI's. Full-leaf
              # block 3/4; of c6's five, block 1/4 and anchors 1/4 -- the only
              # leaf of the c6 span on which block and anchor splits coincide.
    484: 9,   # block 4.5/4.5, anchors 3/6. n. 5 (Bernard, Homil. 2 n. 4) BEGINS
              # in the left block and finishes in the right; rendered joined.
    485: 7,   # block 1.5/5.5, anchors 2/5. n. 2 -- the long editorial note on the
              # rubus as a figure of Mary -- eats most of the left block and runs
              # over into the right. It reads Hexaem. collat. 11. n. 15 (raw 13),
              # confirmed by bon-hex-c11 n. 15 being the burning-bush paragraph.
              # ⚠ gutter is 1388, NOT colcrop's default 1296: this leaf is FADED,
              # so thresh=110 starves and the run blows out to 436 px. Re-profile
              # at thresh 140-180.  (Applies to p. 486 too; see below.)
    486: 9,   # block 2.5/6.5, anchors 6/3 -- this leaf INVERTS the usual
              # asymmetry, six of nine anchoring left. n. 3 (the Humbelina
              # exemplum) spans both blocks; rendered joined. ⚠ FADED leaf:
              # gutter is 1388 against colcrop's default 1296 on a 436 px run.
    487: 9,   # block 5/4, anchors 4/5. n. 5 prints left, anchors right.
              # ⚠ FADED leaf: gutter is 1174 against colcrop's default 1330 on a
              # 404 px run -- 156 px wrong, the largest miss recorded in Vol V.
    488: 9,   # block 5.5/3.5, anchors 5/4. n. 6 (Gregory / Jahel / Isidore)
              # spans both blocks; rendered joined. Three digits corrected: n. 3
              # reads Cap. 3, 14. et 15. (raw 13); n. 4 reads n. 53 and n. 51
              # (raw 33 and 31); n. 5 reads Luc. 2, 35. (raw 33). n. 8 is the
              # `Epist. <roman>. <ch>, <v>` cousin shape (I Petr. 2, 6), third
              # attestation -- invisible to the citation index, never mis-bound.
    489: 5,   # SHARED leaf: COLLATIO VII.'s display heading stands mid-leaf, so
              # n. 1 is Collatio VI's and nn. 2-5 are Collatio VII's (forwarded
              # to bon-don-c7). Full-leaf block 3/2.
    490: 8,   # block 4.5/3.5, anchors 4/4. FOURTH attestation of two notes set on
              # ONE LINE: n. 2 (the Bonelli codex-collation note) ends flush left
              # and n. 3 (Cap. 8, 12.) is set flush right on that same line. Read
              # the block by numeral, never by line. ⚠ gutter 1383 measured on a
              # 46 px run; step (3) fired and REPRODUCED the default at thresh
              # 110/140/160/180 -- a narrow run, not a starved threshold.
    491: 7,   # block 3/4, anchors 2/5. n. 3 (Isaias / Bernard, identifying the
              # Epist. ad Fratres de Monte Dei as Guigo's) spans both blocks;
              # rendered joined. n. 1 reads Exod. 25, 18. (raw 23).
    492: 9,   # block 4/5, anchors 5/4. n. 7 reads Ps. 65, 15 (raw 63). n. 6 is
              # Epist. I. Tim. 4, 8 -- names its book, so NOT the cousin shape.
    493: 7,   # SHARED leaf: COLLATIO VIII.'s display heading stands mid-leaf, so
              # nn. 1-6 are Collatio VII's and n. 7 is Collatio VIII's (forwarded
              # to bon-don-c8). Full-leaf block 3/4. n. 2 reads c. 6, 25. 30. et
              # 31. (raw 23). n. 4 is Libr. I. 5, 3. -- NINTH attestation of the
              # book-number-only genre trait. ⚠ gutter 1183, measured on the
              # UPPER region (rows 0.08-0.38) only: the default returns 1532 on a
              # 1 px run because the leaf stacks four regions.
    494: 10,  # block 5.5/4.5, anchors 3/7. n. 6 (the Cato/Aristotle note) spans both
              # blocks; rendered joined. n. 6 reads (pag. 154) (raw 134) and n. 9 reads
              # Epist. II. Cor. 10, 5 (raw 10, 3) -- both 3/5 class, the second settled
              # by sense (10:5 is the verse the note quotes). ⚠ gutter 1352 on a 54 px
              # run: step (3) fired and found a 14 px centre-rule island inside the
              # band, i.e. the frozen "heavily inked rule" case. Default adopted.
    495: 10,  # block 6/4, anchors 3/7. FIFTH attestation of two notes set on ONE LINE:
              # n. 3 (Psalm. 48, 13.) ends flush left and n. 4 (Prov. 2, 3-5.) is set
              # flush right on that same line. n. 10 reads Ps. 35, 10 (raw 33).
              # ⚠ gutter 1160, corrected from a default of 1154 measured on a 74 px run
              # -- ABOVE the sound band, which is as much a failure signal as below it.
    496: 11,  # block 6.5/4.5, anchors 5/6. n. 7 (Gen. 2, 19 / II. Sent. littera
              # Magistri) spans both blocks; rendered joined. Gutter 1387 on a healthy
              # 62 px run, confirmed by the ink profile.
    497: 6,   # block 4.5/1.5, anchors 2/4. The lightest register of the span BY COUNT
              # and the heaviest by measure: n. 5 (Boethius on the cyclic number, with
              # Rupert of Deutz and Richard of St Victor) is the longest single entry in
              # the Septem Donis and fills most of the leaf's foot. The signature line
              # S. Bonav. -- Tom. V. and the sheet number 63 print inside this register.
              # Gutter 1223 on a 58 px run with the most heavily inked centre rule of
              # the span (island peak 1052).
    498: 9,   # SHARED leaf: COLLATIO IX.'s display heading stands mid-leaf, BUT ALL NINE
              # NOTES ARE COLLATIO VIII's -- Collatio IX has only a heading, a subtitle
              # and an (unanchored) Summarium on this leaf, so NOTHING is forwarded to
              # bon-don-c9. A shared leaf implies a runover only when the incoming unit's
              # BODY reaches the leaf. Block 4.5/4.5, anchors 3/6; n. 5 spans both
              # blocks. n. 2 is Libr. II. 7, 28. -- TENTH attestation of the
              # book-number-only genre trait. n. 8 reads Sap. 9, 15. (raw 9, 13).
              # ⚠ gutter 1306, measured on the UPPER region (rows 0.06-0.52) only: the
              # default returns 1294 on a 13 px run because the leaf stacks four regions.
    499: 7,   # bon-don-c9 opens here: Collatio IX's FIRST numbered paragraph is on this
              # leaf, and p. 498 forwarded nothing, so the register restarts at 1 legitimately.
              # Block 4/3, anchors 4/3 -- the two splits coincide, no note crosses the gutter.
              # n. 1 reads III. Sent. d. 35. q. 1. (raw 33); n. 7 reads et v. 25 (raw 23) and
              # is the FOURTH attestation of the cousin shape Epist. <roman>. <ch>, <v>
              # (Epist. I. 1, 19. = I Cor. 1:19, book named only in the body).
              # ⚠ n. 3 ends "In Vulgata interseruntur multa" with NO final period, as printed.
              # Gutter 1229: default sat on a 55 px run, profile band 1199-1257 midpoint 1228,
              # so the default was CONFIRMED, not corrected.
    500: 8,   # block 5/3, anchors 4/4 -- the splits do NOT coincide: n. 5 prints in the left
              # block and anchors in paragraph 6, which opens the right column. No note crosses
              # the gutter. Gutter 1347 on a healthy 62 px run, used as measured.
    501: 7,   # block 3.5/3.5, anchors 4/3. n. 3 -- the Rufinus/Baronius/Peter de Natalibus
              # dossier on Gregory Nazianzen's dream -- spans both blocks and is the longest
              # entry of the span. ⚠ gutter 1169, NOT the default 1147: colcrop returned 1147
              # on a 3 px run (WEAK RUN) and 21 of 24 windows repeated it; the ink profile gave
              # band 1140-1198, midpoint 1169, island 1165-1173 at peak 659 -- a heavily inked
              # centre rule sitting on the minimum. 22 px correction.
    502: 11,  # block 5/6, anchors 5/6, no note crossing the gutter. The heaviest register of
              # the span. n. 5 reads Prov. 25, 12. (raw 23) and n. 7 tertius Sap. 3, 15.
              # (raw 1S), both settled by the verses the body quotes.
              # ⚠ gutter 1399, NOT the default 1303-1329: this is the body/footer-gap mechanism
              # in its blown-out form (388-453 px runs) on a leaf with NO inked centre rule
              # (island peak 5-8). Every window from 0.12-0.72 to 0.40-0.72 returned band
              # 1365-1433, midpoint ~1399. ~96 px correction.
              # ⚠ The scan (not the printing) is smeared across "melius" and "adulatione" in
              # the right column; the reading is fixed by n. 6's own citation, Eccle. 7, 6.
    503: 7,   # THE LAST LEAF OF THE WORK. block 4/3, anchors 4/3. The full-measure line
              # EXPLICIUNT COLLATIONES DE DONIS SPIRITUS S. stands between the columns and the
              # footer rule, and fixes the work's end POSITIVELY at 503 (the work map's ~503).
              # n. 3 reads Isai. 5, 20 (raw S). ⚠ n. 7 prints "Seq locus est" with NO period
              # after Seq, verified at 4x and set as printed. n. 5 is Libr. III. Reg. 10, 18.,
              # which NAMES its book and is therefore NOT the bare genre trait.
              # Gutter 1147: the whole-leaf profile returns a 32 px island because the default
              # window straddles body, EXPLICIUNT line and register; re-profiled over rows
              # 0.10-0.55 the default is CONFIRMED (band 1118-1176, midpoint 1147).

    # --- Collationes de decem praeceptis (the third reportatio, pp. 507-532) ---
    507: 6,   # OPENING LEAF. block 2/4, anchors 2/4. COLLATIO I. carries NO apparatus
              # anchor (4x). The left footer holds only TWO notes: the OCR reads an em-dash
              # inside n. 2 as a third marker, but on the plate the codex-C addition
              # "Et multum convenienter praemittitur motivum" is the SECOND HALF OF n. 2.
              # Gutter 1157 adopted per the mini-pilot (colcrop gives 1178 on a 15 px run --
              # the stacked heading + subtitle + Summarium failure).
    508: 8,   # block 6/2, anchors 6/2. n. 1 is Cap. 14, 15. et 16. (raw "U, 13."); n. 5 is
              # Cap. 26, 14. et 16 (raw "26, U."); n. 6 is Psalm. 37, 11. (raw "37, M.");
              # n. 8 is Matth. 25, 41 (raw "25, il"). Four raw digits, four corrections.
              # Gutter 1418 measured clean on a 56 px run.
    509: 9,   # block 8/1, anchors 8/1. n. 3 is `Epist. I. 5, 3.` -- the cousin shape the
              # build-citations barrier does NOT cover (the body names John aloud).
              # n. 8's long Augustine block carries I. Cor. 15, 27. and [Rom. 8, 35.]
              # (raw "13, 27" and "8, 33"). n. 9 is Libr. I. Confess., which NAMES its work.
              # Gutter 1285 measured clean on a 59 px run.
    510: 7,   # SHARED LEAF -- and it forwards NOTHING. All seven notes are Collatio I's;
              # COLLATIO II's heading and Summarium stand on this leaf but its numbered
              # body does not begin until p. 511, so the p. 498 rule governs. block 3/4.
              # n. 1 is Hexaem. collat. 4. n. 19 (raw "collat. i."). ⚠ n. 3's
              # "supra pag. 121, nota 3" reads as 124 at 1.3x -- re-read at 4x, it is 121.
              # Gutter 1298: colcrop's 16 px run is the loud value, but two row windows
              # clearing the COLLATIO II block (0.15-0.55, 0.20-0.60) return a 58 px band
              # 1270-1327 with the SAME midpoint 1298. Default confirmed.
    511: 6,   # bon-praec-c2 opens its register here: Collatio II's FIRST numbered
              # paragraph is on this leaf, p. 510 forwarded nothing, so the register
              # restarts at 1 legitimately -- the p. 498 rule attested from the receiving
              # side at this seam. The Summarium finishes at the head of this leaf, above
              # the body, and is unanchored on BOTH leaves. Block 2/4, anchors 2/4.
              # n. 1 reads Ps. 118, 115. Gutter 1263 measured clean on a 61 px run.
    512: 8,   # block 2.5/5.5, anchors 3/5. n. 3 (the long Vatican longior expositio)
              # spans both blocks; rendered joined. n. 2 is Hexaem. collat. 8. n. 4. seqq.
              # (raw "n. l."); n. 8 is Enarrat. in Ps. 69. n. 13 (raw "Ps. C9.").
              # ⚠ n. 8 RUNS OVER onto p. 513's footer block -- its last two lines are set
              # above p. 513's own n. 1. A register runover, NOT a hand-off: the note
              # belongs to p. 512's sequence throughout, and reading it as p. 513's would
              # invent a spurious tenth entry there. Gutter 1302 clean on a 60 px run.
              # ⚠ The marginale at paragraph 9 is PRINTED INCOMPLETE -- it reads
              # "Duplex no-" and nothing follows (read at 3x and 4x; the line beneath is
              # blank and the marginale sits well inside the trimmed edge).
    513: 9,   # block 4/5, anchors 5/4 -- the splits do NOT coincide; no note crosses the
              # gutter. n. 8 reads Psalm. 95, 5. (raw 93), confirmed by sense: Ps. 95:5 is
              # the omnes dii gentium daemonia that paragraph 20 quotes. n. 7 is
              # Epist. I. Cor. 8, 4 -- names its book, so NOT the cousin shape. The
              # signature line S. Bonav. -- Tom. V. and the sheet number 65 print inside
              # this register. ⚠ gutter 1213 on a 48 px run -- BELOW the sound band, so
              # step (3) fired and found a 13 px centre-rule island (peak 466) inside a
              # band 1186-1238 whose midpoint is 1212, with 24 row windows agreeing within
              # 3 px. The frozen "heavily inked rule" case; default adopted.
    514: 6,   # block 4/2, anchors 4/2. n. 6 reads haeres. 25. n. 1 (raw "2S.") and
              # sub n. 104. de Saracenis (raw "n. 101."). n. 2 is Libr. II. de Doctr.
              # christiana -- names its WORK, so NOT the book-number-only genre trait.
              # ⚠ gutter 1290 on a 52 px run: the skew screen shows the gutter walking
              # 15 px down the leaf, so the narrow run is DRIFT, not an inked rule. One
              # split still suffices (max left 1262 < min right 1309) and the windows
              # cluster at 1290-1294; default adopted.
    515: 5,   # SHARED leaf -- and unlike p. 510 it DOES forward. COLLATIO III's display
              # heading, subtitle and Summarium stand mid-leaf AND its numbered body
              # begins on the leaf, so the register splits: nn. 1-3 are Collatio II's
              # (bon-praec-c2) and nn. 4-5 are Collatio III's (forwarded to bon-praec-c3).
              # ★ The two interior boundaries of this work so far answer OPPOSITE ways
              # under one test -- the p. 498 rule -- so no boundary's answer may be copied
              # forward to the remaining four (pp. 519, 522, 525, 529). Full-leaf block
              # 3/2. ⚠ gutter 1258, measured on the UPPER region (rows 0.09-0.33) only:
              # the default returns 1274 on a 1 px run because the leaf stacks the
              # COLLATIO III block across the gutter at roughly 65-73 % down the page.
              # Four windows over that region agree on a 64 px band 1227-1290.
              # ⚠ c3 re-measured the LOWER region (rows 0.75-0.93, the two columns
              # beneath that block) and got 1254 on a clean 63 px band 1223-1285. The two
              # halves of the leaf differ by 4 px and BOTH are right -- region rule.
    516: 6,   # block 4/2, anchors 2/4 -- the left block holds nn. 1-4 although nn. 3 and 4
              # anchor in the right column (the standing overrun case). gutter 1336: the
              # default returns 1327 on an 8 px run because the centre rule inked heavily
              # (island 1333-1342, peak 510); band 1307-1365 (59 px) and every wide window
              # agree at 1335-1338. The skew screen's 45 px drift is the head slice
              # catching the running head, not skew.
    517: 8,   # block 6/2, anchors 4/4 -- left block overruns by two. gutter 1209 (61 px)
              # clean as returned. n. 4 is `Libr. IV. Reg. 1, 13`, the FIRST instance in
              # this work of the unresolvable `Libr. <roman>.` scripture-book shape;
              # settled by sense (the third captain of fifty before Elijah).
    518: 8,   # block 3/5, anchors 4/4 -- here the left block UNDERRUNS by one: n. 4
              # anchors at ¶ 20 in the left column, its entry prints in the right block.
              # gutter 1363 (58 px) clean. ⚠ n. 3 is the densest raw failure in the span
              # (`oejttos` for `veritas`, `ceritatv!` for `veritatis`, `adiscrete` for
              # `« discrete`); the plate is the only witness and the body prose either
              # side of it is clean.
    519: 8,   # SHARED leaf -- and it FORWARDS, as p. 515 did and p. 510 did not. nn. 1-7
              # are Collatio III's (bon-praec-c3; n. 1 answers ¶ 25's `ad Titum`, n. 7
              # ¶ 27's `in Levitico`) and n. 8 (`Exod. 20, 8.`) is Collatio IV's, because
              # Collatio IV's numbered ¶ 1 begins on the leaf and carries the anchor.
              # ★ The tally is now one "no" and two "yes" across three boundaries, and it
              # may NOT be summed: the p. 498 rule is re-asked on the plate at pp. 522,
              # 525 and 529. Two consecutive "yes" answers are not a pattern.
              # Block 2/6, anchors 2/5 -- the only leaf in c3's span where the block break
              # coincides with the anchor break. ⚠ gutter 1177, measured on the UPPER
              # region (rows 0.10-0.40) only: the default returns 1164 on a 1 px run
              # because the COLLATIO IV block occupies roughly 45-60 % of the leaf.
              # Band 1146-1207 (62 px), 3 px centre-rule island.
              # ⚠ bon-praec-c4 re-measured the LOWER region (below the COLLATIO IV
              # block) and got 1178 on band 1164-1193 with a 26 px island. The two
              # halves of THIS leaf agree to within 1 px where p. 515's differed by
              # 4 px -- both are the region rule; a region value is checkable against
              # the other region, never predictable from it.
    520: 8,   # block 3/5, anchors 3/5 -- the only exact block/anchor coincidence in
              # c4's span. ⚠ gutter 1320: the default is a LOUD failure, 1347 on an
              # 8 px run, because the centre rule inked heavily and off centre (5 px
              # island, peak 582) inside a clean 63 px band 1289-1351. The skew screen
              # reports 61 px of drift, but six of its eight slices read 1283-1351 and
              # only the two head slices fork -- the frozen INKED-RULE case, not skew.
              # ⚠ n. 5 is `Epist. I. 3, 15.` where the raw gives `3, 13.`: the 3/5 class
              # in an apparatus digit, settled by sense (I Pet. 3:15 is the sentence the
              # note answers). ⚠ n. 3 opens a SECOND quotation with a guillemet and
              # never closes it -- the printing, read at 2.4x; transcribed as printed
              # on the p. 512 `Duplex no-` precedent.
    521: 7,   # block 4/3, anchors 3/4 -- the left block overruns by one AND n. 4's own
              # text runs over into the right block. That runover is an IN-PAGE COLUMN
              # runover: not a page runover, not a hand-off, and it changes no numbering.
              # ⚠ gutter 1255 on a 51 px run -- under the 60 px confidence floor, so
              # escalated; 23 of 24 windows agree within 4 px at 1253-1257 and the band
              # 1230-1281 gives midpoint 1255. The default is CONFIRMED, not corrected.
              # The skew screen's 185 px "drift" is two head slices catching the running
              # head and the body/footer gap, and is discarded.
    522: 8,   # SHARED leaf -- and it FORWARDS, as pp. 515 and 519 did and p. 510 did not.
              # nn. 1-7 are Collatio IV's (bon-praec-c4; n. 1 answers ¶ 14's `volatilia`,
              # n. 7 ¶ 16's `dicit Psalmus`) and n. 8 (`Exod. 20, 12: Honora... dabit
              # tibi.`) is Collatio V's, because Collatio V's numbered ¶ 1 (`Honora
              # patrem tuum`) begins on the leaf, below the COLLATIO V heading and
              # Summarium, and carries the anchor.
              # ⛔ The tally is now one "no" and three "yes" across four boundaries, and
              # it STILL may not be summed: the p. 498 rule is re-asked on the plate at
              # pp. 525 and 529. Three consecutive "yes" answers are not a pattern.
              # ⭐ p. 522 is structurally the SAME leaf-shape as p. 510, which forwarded
              # nothing -- heading + subtitle + Summarium full-measure mid-leaf. The
              # difference is one line of body. Leaf shape does not decide it.
              # Block 3/5, Collatio IV's anchors 3/4. ⚠ gutter 1316, measured on the
              # UPPER region (rows 0.15-0.45): the default returns 1374 on a 326 px run,
              # nonsense far ABOVE the sound band, because the COLLATIO V block fills the
              # lower half. Band 1300-1334, 13 px island, window median 1315.
              # ⭐ bon-praec-c5 re-measured the LOWER region of this leaf -- the three
              # lines of Collatio V's ¶ 1, a region only 0.04 of the leaf deep and so too
              # thin for the window loop, which needs 0.12 and returns nothing. Step 3
              # alone decides, and only at a RAISED threshold: at ink<110 the region
              # gives a meaningless 101 px run with NO island, because the centre rule
              # printed grey on this forme. At thr 150-200 the columns close at 1284 and
              # 1345 with an isolated island 1313-1316 (peak 142), midpoint 1314 -- 2 px
              # from c4's 1316 for the upper region. A region value is checkable against
              # the other region and never predictable from it, and here the check is
              # what licenses the number: the region alone could not have produced one.
    523: 8,   # block 5/3, anchors 3/5 -- an exact inversion. gutter 1276 on a 60 px run,
              # exactly at the confidence floor, so escalated: 21 of 24 windows agree at
              # 1276-1277, band 1247-1306, 8 px island peak 492 dead centre. The default
              # is CONFIRMED, not corrected. The skew screen's 197 px drift is the two
              # head slices forking; discarded.
    524: 8,   # block 4/4, anchors 4/4 -- the SECOND exact block/anchor coincidence in
              # this work, after p. 520.
              # ⭐⭐ NEW GUTTER MECHANISM, the INVERSE of the frozen inked-rule case:
              # THE CENTRE RULE CAN PRINT TOO LIGHT FOR THE ink<110 THRESHOLD, and then
              # the profile reports NO island and a run that is too WIDE. The default
              # returns 1356 on a 75 px run -- wider than the sound 58-64 px band -- and
              # the window consensus blows out (69 px spread, runs of 211-458 px),
              # because the criterion had no rule to hold on to. At thr 180 the rule
              # stands isolated at 1360-1364; four separate row regions all return band
              # 1332-1392, midpoint 1362 ADOPTED. ⚠ The same faintness is visible in the
              # TYPE of the right column (intelligitur, debilitantur, adiutorio print
              # grey), so it is ONE physical fact about the forme -- rule and type inked
              # together -- not two coincidences. The tell is a wide run with no island,
              # on a volume where the island is on essentially every leaf.
    525: 4,   # SHARED leaf -- and it FORWARDS, as pp. 515, 519 and 522 did and p. 510
              # did not. nn. 1-3 are Collatio V's (bon-praec-c5; n. 1 answers ¶ 20's
              # `episcopus Parisiensis`, n. 2 ¶ 21's `tenellis`, n. 3 ¶ 21's closing
              # `mortuus est ille`) and n. 4 (`Exod. 20, 13-15. -- Seq. locus est Ps.
              # 118, 6; tertius Iac. 2, 10...`) is Collatio VI's, because Collatio VI's
              # numbered ¶ 1 (`Non occides. Non moechaberis. Non furtum facies`) begins
              # on the leaf, below the COLLATIO VI heading and Summarium, and carries the
              # anchor at `facies`.
              # ⛔ The tally is now one "no" and four "yes" and it STILL may not be
              # summed. ONLY p. 529 is left, and it is the work's LAST boundary -- there
              # is no later chunk to catch a wrong answer there. Re-ask it on the plate.
              # ⭐ Sharpest block-vs-anchor case in the work: block 1/3, and NOT ONE of
              # Collatio V's three anchors stands in the left column, yet the left block
              # carries n. 1 (six lines long, it opened the block); meanwhile Collatio
              # VI's n. 4 anchors LEFT and prints last in the RIGHT block. Uncorrelated
              # in both directions on one leaf. Read anchors, only anchors.
              # ⚠ gutter 1216 for the UPPER region (rows 0.08-0.50): the default returns
              # 1168 on a 4 px run because the COLLATIO VI heading, subtitle, Summarium
              # and ¶ 1 fill the leaf below 50 %. Band 1186-1247 (62 px), 2 px island
              # peak 301, 15 of 23 windows agree at 1216-1217.
    526: 6,   # bon-praec-c6, own register (6 numbered + 1 unanchored editorial note,
              # the unanchored one not counted in this per-page footnote total).
    527: 8,   # bon-praec-c6, own register.
    528: 9,   # bon-praec-c6, own register.
    529: 6,   # SHARED leaf -- FORWARDS, the work's last boundary and the sixth
              # measured (bon-praec-c6/c7). n. 1 is Collatio VI's (bon-praec-c6); nn.
              # 2-6 are Collatio VII's (bon-praec-c7), because Collatio VII's numbered
              # ¶ 1 (`Non loqueris contra proximum tuum falsum testimonium...`) begins
              # on the leaf, below the COLLATIO VII heading and Summarium, and carries
              # the anchor at `eius`².
    530: 7,   # bon-praec-c7, own register -- ordinary two-column leaf, no shared
              # boundary at either end.
    531: 12,  # bon-praec-c7, own register.
    532: 2,   # bon-praec-c7, own register -- the work's last leaf; EXPLICIUNT
              # COLLATIONES DE DECEM PRAECEPTIS. closes the work full-measure beneath
              # both columns, with these two notes printed below it.
}


def section(text, name):
    """Return the body of a `## name` section, up to the next `## ` heading."""
    m = re.search(r"^## %s\s*$" % re.escape(name), text, re.M)
    if not m:
        return ""
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def main():
    expect = dict(KNOWN_TOTALS)
    for arg in sys.argv[1:]:
        if arg.startswith("--expect-max"):
            _, _, spec = arg.partition("=")
            pg, _, n = spec.partition(":")
            if pg and n:
                expect[int(pg)] = int(n)

    files = sorted(glob.glob(os.path.join(VOL5, "*.md")))
    if not files:
        print("no chunks in vol5/ — nothing to check")
        return 0

    owners = defaultdict(dict)   # page -> {note_number: [chunk, ...]}
    problems = []
    unregistered = []
    total_entries = 0

    print("Per-chunk label pairing")
    print("-" * 62)
    for path in files:
        name = os.path.basename(path)
        text = open(path, encoding="utf-8").read()
        la = section(text, "Latin")
        en = section(text, "English")
        app = section(text, "Apparatus")

        defs = re.findall(r"^\[\^([^\]]+)\]:", app, re.M)
        la_anchors = re.findall(r"\[\^([^\]]+)\]", la)
        en_anchors = re.findall(r"\[\^([^\]]+)\]", en)
        total_entries += len(defs)

        dupes = sorted({d for d in defs if defs.count(d) > 1})
        if dupes:
            problems.append("%s: DUPLICATE defs %s" % (name, dupes))

        paired = sorted(defs) == sorted(la_anchors) == sorted(en_anchors)
        if not paired:
            missing_la = sorted(set(defs) - set(la_anchors))
            missing_en = sorted(set(defs) - set(en_anchors))
            orphan = sorted((set(la_anchors) | set(en_anchors)) - set(defs))
            detail = []
            if missing_la:
                detail.append("no Latin anchor: %s" % missing_la)
            if missing_en:
                detail.append("no English anchor: %s" % missing_en)
            if orphan:
                detail.append("anchored but undefined: %s" % orphan)
            problems.append("%s: PAIRING — %s" % (name, "; ".join(detail)))

        print("  %-24s %2d entries  La %2d  En %2d  %s"
              % (name, len(defs), len(la_anchors), len(en_anchors),
                 "ok" if paired and not dupes else "** FAIL **"))

        for pg, num in re.findall(r"^\[\^p(\d+)-(\d+)\]:", app, re.M):
            owners[int(pg)].setdefault(int(num), []).append(name)

    print()
    print("Footer ownership by printed page")
    print("-" * 62)
    for pg in sorted(owners):
        nums = owners[pg]
        top = max(nums)
        gaps = [i for i in range(1, top + 1) if i not in nums]
        doubles = sorted(n for n, who in nums.items() if len(who) > 1)
        known = expect.get(pg)
        pending = []
        if known is not None and known > top:
            pending = list(range(top + 1, known + 1))

        status = "ok"
        if gaps:
            problems.append("p.%d: INTERIOR GAP — notes %s owned by no chunk" % (pg, gaps))
            status = "** GAP %s **" % gaps
        if doubles:
            for n in doubles:
                problems.append("p.%d n.%d: DOUBLE-CLAIMED by %s" % (pg, n, nums[n]))
            status = "** DOUBLE %s **" % doubles

        line = "  p.%d: 1-%-2d (%d notes)  %s" % (pg, top, len(nums), status)
        if pending:
            line += "   PENDING n.%s -> not yet written" % (
                ",".join(str(p) for p in pending))
        elif known is None:
            # An unregistered page cannot be checked for a trailing shortfall:
            # with no recorded total, a page whose last notes are still
            # unwritten is indistinguishable from a page that is complete, and
            # it prints "ok". That is the failure mode this whole script exists
            # to prevent, so say so loudly rather than let it read as clean.
            line += "   ?? NOT IN KNOWN_TOTALS -- trailing notes unverifiable"
        print(line)

        if known is not None and top > known:
            problems.append(
                "p.%d: claims n.%d but the page is recorded as holding only %d"
                % (pg, top, known))
        if known is None:
            unregistered.append(pg)

    if unregistered:
        print()
        print("?? %d page(s) not in KNOWN_TOTALS: %s" % (
            len(unregistered), ", ".join("p.%d" % p for p in unregistered)))
        print("   Their trailing notes cannot be checked. Read the page's full")
        print("   footer register off the bands and add the total to KNOWN_TOTALS.")

    print()
    print("%d chunks, %d apparatus entries" % (len(files), total_entries))
    if problems:
        print()
        print("PROBLEMS (%d)" % len(problems))
        for p in problems:
            print("  - %s" % p)
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
