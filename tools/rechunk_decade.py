#!/usr/bin/env python3.11
"""Config-driven Vol II decade re-chunk driver.

Session 34 (2026-05-17). Generalizes tools/rechunk_d{2,3,4}.py into one
reusable driver: a per-distinction config of semantic chunk boundaries
(verified by grep/awk on raw markers + the +22 PDF running heads, never
the OCR digits) drives clean-slate skeleton regeneration for a whole
decade in one run. First use: the d.5–d.10 decade-batch trial.

CRITICAL: split on "\n" only — NEVER splitlines(). The Vol II raw has
1056 form feeds (\f); str.splitlines() also splits on \f and would shift
every line number ~1055 off from grep/awk (which all boundary numbers
below were derived with). Same fix as rechunk_d2/d3/d4.py.

Conventions (locked d.1–d.4, applied throughout the config):
  - Single Lombard `littera` per distinction (covers all pars's Caps;
    d.3 precedent — no per-pars littera).
  - One `divisio` per pars (COMMENTARIUS + DIVISIO TEXTUS + TRACTATIO
    QUAESTIONUM), ending before that pars's ARTICULUS I.
  - Short ARTICULUS opener (header + title + sub-divisio) folds into
    that article's q1 — no standalone article-divisio chunk; q1's
    line_start = the ARTICULUS header line.
  - ARTICULUS UNICUS → articulus=1 (existing d.9 skeleton convention).
  - `dubia` per pars where present.
  - DISTINCTIO/QUAESTIO/ARTICULUS OCR headers are routinely garbled;
    boundaries resolved by content + running-head text, then awk-verified.

Latin body = raw OCR; English/apparatus are skeleton placeholders.
title_la here is PROVISIONAL — Tier-2 promotion finalizes title_la/_en
and re-sets the body against the 450 dpi column-band PDF.

Per-distinction clean-slate: every `bon-sent-II-d{N}-*.md` is deleted
(clearing auto-chunk dup2/dup3/commentary orphans) and replaced by the
config's chunks. Backups taken by the caller before running.
"""
from pathlib import Path

ROOT = Path("/Users/wilsonpruitt/bonaventure-sentences")
RAW = ROOT / "raw/bonaventure_vol2_raw.txt"
OUT = ROOT / "vol2"
SESSION = "rechecked 2026-05-17 session 34 (decade-batch d.5-d.10 trial — correct semantic boundaries)"

lines = RAW.read_text().split("\n")  # NOT splitlines() — form-feed safe


def extract(start, end):
    return "\n".join(lines[start - 1:end]).strip()


# Per-distinction config.
# Each entry: distinctio -> list of chunks
#   (suffix, type, pars, articulus, quaestio, line_start, line_end, title_la, note)
# id = f"bon-sent-II-d{distinctio}-{suffix}"
DECADE = {
    5: [
        ("littera", "littera", None, None, None, 10586, 10672,
         "Distinctio V. Magistri Sententiarum.",
         "DISTINCTIO V (10586) + Lombard Caps. Ends before COMMENTARIUS (10673)."),
        ("divisio", "divisio", None, None, None, 10673, 10717,
         "Commentarius in Distinctionem V — Divisio textus.",
         "COMMENTARIUS (10673) + DIVISIO TEXTUS (10678) + TRACTATIO (10697) + NOTAE AD COMMENTARIUM (10711). ART I (10718) folds into a1-q1."),
        ("a1-q1", "quaestio", None, 1, 1, 10718, 10934,
         "Utrum lucifer peccaverit peccato superbiae.",
         "ART I opener (10718) + De aversione luciferi + QUAESTIO I (10722) folded. Ends before QUAESTIO II (10935)."),
        ("a1-q2", "quaestio", None, 1, 2, 10935, 11100,
         "Utrum lucifer appetiverit Deo aequiparari.",
         "QUAESTIO II (garbled 'QU.\\ESTIO 11.' 10935). Ends before ARTICULUS II (11101)."),
        ("a2-q1", "quaestio", None, 2, 1, 11101, 11224,
         "Utrum minores Angeli peccaverint peccato superbiae.",
         "ART II opener (11101) + De aversione minorum Angelorum + QUAESTIO I (11111) folded. Ends before QUAESTIO II (11225)."),
        ("a2-q2", "quaestio", None, 2, 2, 11225, 11353,
         "Utrum peccatum minorum Angelorum iudicet ordinem ad peccatum luciferi.",
         "QUAESTIO II (garbled 'OUAESTIO II.' 11225). Ends before ARTICULUS III (11354)."),
        ("a3-q1", "quaestio", None, 3, 1, 11354, 11537,
         "Utrum conversio bonorum Angelorum fuerit virtute naturae, vel auxilio gratiae.",
         "ART III opener (11354) + De conversione bonorum Angelorum + QUAESTIO I (garbled 'QUAESTiO' 11363) folded. Ends before QUAESTIO II (11538)."),
        ("a3-q2", "quaestio", None, 3, 2, 11538, 11655,
         "Utrum in conversione bonorum Angelorum meritum praecesserit praemium, vel e converso.",
         "QUAESTIO II (11538). Ends before DUBIA (11656)."),
        ("dubia", "dubia", None, None, None, 11656, 11699,
         "Dubia circa litteram Magistri.",
         "DUBIA CIRCA LITTERAM MAGISTRI (11656). Ends before DISTINCTIO VI (11700)."),
    ],
    6: [
        ("littera", "littera", None, None, None, 11700, 11800,
         "Distinctio VI. Magistri Sententiarum.",
         "DISTINCTIO VI (11700) + Lombard Caps. Ends before COMMENTARIUS (11801)."),
        ("divisio", "divisio", None, None, None, 11801, 11846,
         "Commentarius in Distinctionem VI — Divisio textus.",
         "COMMENTARIUS (11801) + DIVISIO TEXTUS (11807) + NOTAE AD COMMENTARIUM (11826) + TRACTATIO (11836). ART I (11847) folds into a1-q1."),
        ("a1-q1", "quaestio", None, 1, 1, 11847, 11970,
         "Utrum lucifer fuerit de supremo ordine Angelorum.",
         "ART I opener (11847) + De quo ordine mali angeli ceciderunt + QUAESTIO I (11852) folded. Ends before QUAESTIO II (11971)."),
        ("a1-q2", "quaestio", None, 1, 2, 11971, 12033,
         "Quaestio II — de quo ordine mali angeli ceciderunt.",
         "QUAESTIO II (11971). Ends before ARTICULUS II (12034)."),
        ("a2-q1", "quaestio", None, 2, 1, 12034, 12138,
         "Utrum angeli in locum infernalem ceciderint.",
         "ART II opener (12034) + In quid ceciderint angeli lapsi + QUAESTIO I (garbled 'QU,\\ESTIO I.' 12042) folded. Ends before QUAESTIO II (12139)."),
        ("a2-q2", "quaestio", None, 2, 2, 12139, 12397,
         "Quaestio II — in quid ceciderint angeli lapsi.",
         "QUAESTIO II (12139). Ends before DUBIA (12398)."),
        ("dubia", "dubia", None, None, None, 12398, 12469,
         "Dubia circa litteram Magistri.",
         "DUBIA CIRCA LITTERAM MAGISTRI (12398): DUB I (12400), DUB II, DUB III (12446), DUB IV (12447). Ends before DISTINCTIO VII (12470)."),
    ],
    7: [
        ("littera", "littera", None, None, None, 12470, 12655,
         "Distinctio VII. Magistri Sententiarum (Pars I et II).",
         "Single Lombard block, both pars's Caps (Pars I 12472, Pars II 12547 are Cap section markers, not chunk bounds). Ends before COMMENTARIUS Pars I (12656)."),
        ("p1-divisio", "divisio", 1, None, None, 12656, 12684,
         "Commentarius in Distinctionem VII, Pars I — Divisio textus.",
         "COMMENTARIUS Pars I (12656) + DIVISIO TEXTUS (12663) + TRACTATIO (12676). ARTICULUS I (12685) folds into a1-q1."),
        ("p1-a1-q1", "quaestio", 1, 1, 1, 12685, 12992,
         "Utrum affectus vel voluntas daemonis possit rectificari.",
         "ART I opener (garbled 'AUTICULUS I' 12685) + QUAESTIO I (12689) folded. Ends before QUAESTIO II (12993)."),
        ("p1-a1-q2", "quaestio", 1, 1, 2, 12993, 13179,
         "Utrum in daemonibus sit malae voluntatis continuatio.",
         "QUAESTIO II (garbled 'QU.\\EST10 II.' 12994). Ends before QUAESTIO III (13180)."),
        ("p1-a1-q3", "quaestio", 1, 1, 3, 13180, 13350,
         "Utrum mala voluntas in daemonibus intendatur.",
         "QUAESTIO III (13180). Ends before ARTICULUS II (13351)."),
        ("p1-a2-q1", "quaestio", 1, 2, 1, 13351, 13494,
         "Utrum confirmatio mutet libertatis arbitrium.",
         "ART II opener (13351) + QUAESTIO I (13362) folded. Ends before QUAESTIO II (13495)."),
        ("p1-a2-q2", "quaestio", 1, 2, 2, 13495, 13611,
         "Utrum obstinatio tollat a daemonibus libertatis usum.",
         "QUAESTIO II (garbled 'QUAESTIO n.' 13495). Ends before QUAESTIO III (13612)."),
        ("p1-a2-q3", "quaestio", 1, 2, 3, 13612, 13723,
         "Utrum haec vel illa minuat libertatis dominium.",
         "QUAESTIO III (garbled 'QUAESTIO m.' 13612). Ends before COMMENTARIUS Pars II (13724)."),
        ("p2-divisio", "divisio", 2, None, None, 13724, 13754,
         "Commentarius in Distinctionem VII, Pars II — Divisio textus.",
         "COMMENTARIUS Pars II (13724) + DIVISIO TEXTUS (13732) + TRACTATIO (13747). ARTICULUS I (13755) folds into a1-q1."),
        ("p2-a1-q1", "quaestio", 2, 1, 1, 13755, 13932,
         "Utrum in daemonibus cadat deceptio circa praesentia.",
         "ART I opener (13755) + QUAESTIO I (13759) folded. Ends before QUAESTIO II (13933)."),
        ("p2-a1-q2", "quaestio", 2, 1, 2, 13933, 14055,
         "Utrum in daemonibus cadat oblivio.",
         "QUAESTIO II (garbled 'OUAESTIO U.' 13933). Ends before QUAESTIO III (14056)."),
        ("p2-a1-q3", "quaestio", 2, 1, 3, 14056, 14236,
         "Utrum in daemonibus sit praecognitio quoad futura.",
         "QUAESTIO III (garbled 'QU.VESTIO III.' 14057). Ends before ARTICULUS II (14237)."),
        ("p2-a2-q1", "quaestio", 2, 2, 1, 14237, 14530,
         "Utrum omnes formae inducantur a Creatore, vel ab agente creato.",
         "ART II opener (garbled 'ARTICULUS IL' 14237, De virtute daemonum) + QUAESTIO I (14245) folded. Ends before QUAESTIO II (14531)."),
        ("p2-a2-q2", "quaestio", 2, 2, 2, 14531, 14766,
         "Utrum verarum formarum inductio sit a spiritu maligno.",
         "QUAESTIO II (garbled 'QU.\\ESTIO II.' 14531). Ends before QUAESTIO III (14767)."),
        ("p2-a2-q3", "quaestio", 2, 2, 3, 14767, 14890,
         "Utrum quis magicis artibus uti possit absque peccato.",
         "QUAESTIO III (14767). Ends before DUBIA (14891)."),
        ("p2-dubia", "dubia", 2, None, None, 14891, 14994,
         "Dubia circa litteram Magistri (Pars II).",
         "DUBIA CIRCA LITTERAM MAGISTRI (14891): DUB I (14893) through DUB V (two-column block). Ends before DISTINCTIO VIII (14995)."),
    ],
    8: [
        ("littera", "littera", None, None, None, 14995, 15126,
         "Distinctio VIII. Magistri Sententiarum (Pars I et II).",
         "DISTINCTIO VIII (garbled 'DISTINCTIO YIII.' 14995) + Pars I (14996) + both pars's Lombard Caps. Ends before COMMENTARIUS Pars I (15127)."),
        ("p1-divisio", "divisio", 1, None, None, 15127, 15173,
         "Commentarius in Distinctionem VIII, Pars I — Divisio textus.",
         "COMMENTARIUS Pars I (15127) + DIVISIO TEXTUS (15136) + TRACTATIO (15164). ARTICULUS I (15174) folds into a1-q1."),
        ("p1-a1-q1", "quaestio", 1, 1, 1, 15174, 15303,
         "Utrum Angeli habeant corpora naturaliter sibi unita.",
         "ART I opener (15174) + QUAESTIO I (15179) folded. Ends before QUAESTIO II (15304)."),
        ("p1-a1-q2", "quaestio", 1, 1, 2, 15304, 15408,
         "Utrum Angeli quandoque assumant sibi corpora.",
         "QUAESTIO II (15304). Ends before ARTICULUS II (15409)."),
        ("p1-a2-q1", "quaestio", 1, 2, 1, 15409, 15585,
         "Utrum corpus assumtum habeat veram formam corporis humani.",
         "ART II opener (15409) + QUAESTIO I (15422) folded. Ends before QUAESTIO II (15586)."),
        ("p1-a2-q2", "quaestio", 1, 2, 2, 15586, 15735,
         "Utrum corpora ab Angelis assumta fiant de natura caelesti an elementari.",
         "QUAESTIO II (15586). Ends before ARTICULUS III (15736)."),
        ("p1-a3-q1", "quaestio", 1, 3, 1, 15736, 15901,
         "Utrum Angelus in corporibus assumtis exerceat operationes potentiae vegetativae.",
         "ART III opener (15736) + QUAESTIO I (15755) folded. Ends before QUAESTIO II (15902)."),
        ("p1-a3-q2", "quaestio", 1, 3, 2, 15902, 16057,
         "Utrum Angeli in corporibus assumtis exerceant operationes convenientes potentiae sensitivae.",
         "QUAESTIO II (15902). Ends before DUBIA Pars I (16058)."),
        ("p1-dubia", "dubia", 1, None, None, 16058, 16127,
         "Dubia circa litteram Magistri (Pars I).",
         "DUBIA CIRCA LITTERAM MAGISTRI Pars I (16058): DUB I (16060), DUB II (16088), DUB III (16077) — two-column. Ends before COMMENTARIUS Pars II (16128)."),
        ("p2-divisio", "divisio", 2, None, None, 16128, 16151,
         "Commentarius in Distinctionem VIII, Pars II — Divisio textus.",
         "COMMENTARIUS Pars II (16128) + Pars II (16129) + DIVISIO TEXTUS (16135) + TRACTATIO (16144). ARTICULUS UNICUS (16152) folds into a1-q1."),
        ("p2-a1-q1", "quaestio", 2, 1, 1, 16152, 16253,
         "Utrum daemones habitare possint in corporibus humanis.",
         "ARTICULUS UNICUS opener (16152, De potestate daemonum respectu hominum) + QUAESTIO I (16155) folded. Ends before QUAESTIO II (16254)."),
        ("p2-a1-q2", "quaestio", 2, 1, 2, 16254, 16350,
         "Utrum daemones animabus illabi possint.",
         "QUAESTIO II (16254). Ends before QUAESTIO III (16351)."),
        ("p2-a1-q3", "quaestio", 2, 1, 3, 16351, 16533,
         "Utrum daemones possint illudere sensus.",
         "QUAESTIO III (16351). Ends before QUAESTIO IV (16534)."),
        ("p2-a1-q4", "quaestio", 2, 1, 4, 16534, 16627,
         "Utrum daemones cogitationes immittere possint.",
         "QUAESTIO IV (16534). Ends before QUAESTIO V (16628)."),
        ("p2-a1-q5", "quaestio", 2, 1, 5, 16628, 16699,
         "Utrum daemones possint malas affectiones incendere.",
         "QUAESTIO V (16628). Ends before QUAESTIO VI (16700)."),
        ("p2-a1-q6", "quaestio", 2, 1, 6, 16700, 16857,
         "Utrum daemones scrutari possint secreta conscientiae nostrae.",
         "QUAESTIO VI (16700). No Pars II dubia. Ends before DISTINCTIO IX (16858; the IX at 16846 is a running-head bleed)."),
    ],
    9: [
        ("littera", "littera", None, None, None, 16858, 17003,
         "Distinctio IX. Magistri Sententiarum.",
         "DISTINCTIO IX (16858) + Lombard Caps (De ordinum distinctione). Ends before COMMENTARIUS (17004)."),
        ("divisio", "divisio", None, None, None, 17004, 17301,
         "Commentarius in Distinctionem IX — Divisio textus (de ordinibus Angelorum).",
         "COMMENTARIUS (17004) + DIVISIO TEXTUS (17009) + TRACTATIO (17290). ARTICULUS UNICUS (17302) folds into a1-q1."),
        ("a1-q1", "quaestio", None, 1, 1, 17302, 17466,
         "Quaestio I — de ordinum distinctione Angelorum.",
         "ARTICULUS UNICUS opener (17302, De ordinibus Angelorum) + QUAESTIO I (17306) folded. Ends before QUAESTIO II (17467)."),
        ("a1-q2", "quaestio", None, 1, 2, 17467, 17534,
         "Utrum distinctio Angelorum sit a natura, an a gratia.",
         "QUAESTIO II (17467). Ends before QUAESTIO III (17535)."),
        ("a1-q3", "quaestio", None, 1, 3, 17535, 17696,
         "Utrum secundum maiorem capacitatem naturalium dentur a Deo maiora dona gratuita.",
         "QUAESTIO III (17535). Ends before QUAESTIO IV (17697)."),
        ("a1-q4", "quaestio", None, 1, 4, 17697, 17874,
         "Quaestio IV — de ordinibus Angelorum.",
         "QUAESTIO IV (17697). Ends before QUAESTIO V (17875)."),
        ("a1-q5", "quaestio", None, 1, 5, 17875, 17988,
         "Quaestio V — de ordinibus Angelorum.",
         "QUAESTIO V (17875). Ends before QUAESTIO VI (17989)."),
        ("a1-q6", "quaestio", None, 1, 6, 17989, 18080,
         "Quaestio VI — de ordinibus Angelorum.",
         "QUAESTIO VI (17989). Ends before QUAESTIO VII (18081)."),
        ("a1-q7", "quaestio", None, 1, 7, 18081, 18208,
         "Quaestio VII — de ordinibus Angelorum.",
         "QUAESTIO VII (18081). Ends before QUAESTIO VIII (18209)."),
        ("a1-q8", "quaestio", None, 1, 8, 18209, 18311,
         "Quaestio VIII — de ordinibus Angelorum.",
         "QUAESTIO VIII (18209). Ends before QUAESTIO IX (18312)."),
        ("a1-q9", "quaestio", None, 1, 9, 18312, 18419,
         "Quaestio IX — de ordinibus Angelorum.",
         "QUAESTIO IX (18312). No dubia in d.9. Ends before DISTINCTIO X (18420)."),
    ],
    10: [
        ("littera", "littera", None, None, None, 18420, 18488,
         "Distinctio X. Magistri Sententiarum.",
         "DISTINCTIO X (18420) + Lombard Caps (An omnes caelestes spiritus mittantur). Ends before COMMENTARIUS (18489)."),
        ("divisio", "divisio", None, None, None, 18489, 18516,
         "Commentarius in Distinctionem X — Divisio textus.",
         "COMMENTARIUS (18489) + DIVISIO TEXTUS (18494) + TRACTATIO (18508). ARTICULUS I (18517) folds into a1-q1."),
        ("a1-q1", "quaestio", None, 1, 1, 18517, 18634,
         "Quaestio I — utrum boni Angeli mittantur.",
         "ART I opener (18517, Utrum boni Angeli mittantur) + QUAESTIO I (18521) folded. Ends before QUAESTIO II (18635)."),
        ("a1-q2", "quaestio", None, 1, 2, 18635, 18741,
         "Quaestio II — utrum boni Angeli mittantur.",
         "QUAESTIO II (18635). Ends before ARTICULUS II (18742)."),
        ("a2-q1", "quaestio", None, 2, 1, 18742, 18855,
         "Quaestio I — ad quid boni Angeli mittantur.",
         "ART II opener (18742, Ad quid boni Angeli mittantur) + QUAESTIO I (18750) folded. Ends before QUAESTIO II (18856)."),
        ("a2-q2", "quaestio", None, 2, 2, 18856, 19030,
         "Utrum Angeli mittantur ad illuminandum nostrum intellectum.",
         "QUAESTIO II (18856). Ends before ARTICULUS III (19031)."),
        ("a3-q1", "quaestio", None, 3, 1, 19031, 19308,
         "Quaestio I — qualiter Angeli officium suum exsequantur.",
         "ART III opener (19031, Qualiter Angeli officium suum exsequantur) + QUAESTIO I (19044) folded. Ends before QUAESTIO II (19309)."),
        ("a3-q2", "quaestio", None, 3, 2, 19309, 19451,
         "Utrum eorum locutio possit esse a Deo et ab Angelo.",
         "QUAESTIO II (garbled 'QUAESTIO 11.' 19309). Ends before DUBIA (19452)."),
        ("dubia", "dubia", None, None, None, 19452, 19517,
         "Dubia circa litteram Magistri.",
         "DUBIA CIRCA LITTERAM MAGISTRI (19452): DUB I (19454), DUB III (19512). Ends before DISTINCTIO XI (19518)."),
    ],
}

ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI",
         7: "VII", 8: "VIII", 9: "IX", 10: "X"}


def frontmatter(cid, dist, ctype, pars, art, q, s, e, title_la, note, wc):
    fm = ["---", f'id: "{cid}"', "volume: 2", "book: 2", f"distinctio: {dist}"]
    if pars is not None:
        fm.append(f"pars: {pars}")
    if art is not None:
        fm.append(f"articulus: {art}")
    if q is not None:
        fm.append(f"quaestio: {q}")
    fm += [
        f"type: {ctype}",
        f'title_la: "{title_la}"',
        'title_en: ""',
        f"line_start: {s}",
        f"line_end: {e}",
        f"word_count_latin: {wc}",
        f'transcription_status: "auto-chunked 2026-05-13; {SESSION}, raw {s}-{e}) — {note}"',
        "format_version: 1",
        "---",
    ]
    return "\n".join(fm)


def main():
    total = 0
    for dist, chunks in DECADE.items():
        # contiguity self-check
        for i in range(1, len(chunks)):
            prev_end = chunks[i - 1][6]
            cur_start = chunks[i][5]
            if cur_start != prev_end + 1:
                raise SystemExit(
                    f"CONTIGUITY ERROR d.{dist}: chunk {chunks[i][0]} starts "
                    f"{cur_start}, prev ended {prev_end} (expected {prev_end+1})")
        new_ids = {f"bon-sent-II-d{dist}-{c[0]}" for c in chunks}
        existing = sorted(OUT.glob(f"bon-sent-II-d{dist}-*.md"))
        print(f"\n=== d.{dist} ({len(chunks)} chunks) ===")
        for p in existing:
            tag = "OVERWRITE" if p.stem in new_ids else "DELETE (orphan)"
            print(f"  {p.name}: {tag}")
        for p in existing:
            p.unlink()
        for suffix, ctype, pars, art, q, s, e, title_la, note in chunks:
            cid = f"bon-sent-II-d{dist}-{suffix}"
            body = extract(s, e)
            wc = len(body.split())
            fm = frontmatter(cid, dist, ctype, pars, art, q, s, e,
                             title_la, note, wc)
            md = (f"{fm}\n\n# {cid}\n\n## Latin\n\n{body}\n\n"
                  f"## English\n\n[Translation pending]\n\n"
                  f"## Apparatus\n\n[Apparatus pending]\n")
            (OUT / f"{cid}.md").write_text(md)
            print(f"  wrote {cid}.md ({s}-{e}, {e-s+1} lines, {wc} w)")
            total += 1
    print(f"\nDone. {total} chunks across d.{min(DECADE)}-d.{max(DECADE)}.")


if __name__ == "__main__":
    main()
