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
