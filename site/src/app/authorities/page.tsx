import Link from "next/link";
import { Illumination, CrossDivider } from "@/components/decorations";
import { authorityToc } from "@/lib/authorities";

export const metadata = {
  title: "Index of Authorities — Bonaventure, Opera Omnia",
  description:
    "Every author and work cited in the translated Opera Omnia of St. Bonaventure, "
    + "with the Quaracchi locus as printed — derived from the Quaracchi apparatus.",
};

export default function AuthoritiesIndexPage() {
  const authors = authorityToc();
  const total = authors.reduce((n, a) => n + a.count, 0);
  const works = authors.reduce((n, a) => n + a.works.filter((w) => w.id !== "unassigned").length, 0);

  return (
    <div>
      <Link href="/" className="back-link">
        &larr; Home
      </Link>
      <div style={{ display: "flex", alignItems: "center", gap: "1rem", marginBottom: "1rem" }}>
        <Illumination size={50} letter="A" />
        <h2 className="h2">Index of Authorities</h2>
      </div>
      <CrossDivider />

      <div className="body-text" style={{ marginBottom: "2rem" }}>
        <p>
          The authors and works cited in the translated portion of the <em>Opera Omnia</em> —{" "}
          {total.toLocaleString()} citations of {works} works by {authors.length} authors. The
          index is <strong>derived</strong> from the Quaracchi apparatus and Bonaventure&rsquo;s
          own text rather than tagged by hand, and it grows with the translation.
        </p>
        <p>
          Each citation is listed under the work Quaracchi names, with the locus{" "}
          <strong>as Quaracchi prints it</strong>; references are not converted to modern
          editions. Attributions follow Quaracchi: a work now known to be by another hand is
          marked <em>attributed</em> where the editors themselves treat it so.
        </p>
        <p>
          Two kinds of reference are kept apart. A <strong>citation</strong> is a source
          Bonaventure or his editors point to. <strong>On the same passage</strong> lists the
          other doctors whom the editors cite on the same text (<em>S. Thom., hic</em>) — on the
          same distinction of the <em>Sentences</em>, or on the same verse of Scripture.
        </p>
      </div>

      <div className="question-list">
        {authors.map((a) => (
          <Link key={a.id} href={`/authorities/${a.id}`} className="card card-link">
            <div className="card-title">{a.en}</div>
            <div className="card-meta">
              <span style={{ fontStyle: "italic" }}>{a.la}</span>
              {" · "}
              {a.cited.toLocaleString()} citation{a.cited !== 1 ? "s" : ""}
              {a.samePassage > 0 && <> · {a.samePassage.toLocaleString()} on the same passage</>}
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
