import Link from "next/link";
import { loadAllContent } from "@/lib/content";
import { Illumination, CrossDivider, FleuronDivider } from "@/components/decorations";

// The ten tomes of the Quaracchi Opera Omnia (Ad Claras Aquas, 1882–1902).
// Verified against the Quaracchi publisher listing, the Internet Archive
// catalogue records, and per-work page citations. Status reflects this
// project's progress; href is set only for volumes with published content.
type ScopeStatus = "published" | "in-preparation" | "planned";
const OPERA_OMNIA: {
  tome: string;
  year: number;
  title: string;
  gloss: string;
  status: ScopeStatus;
  href?: string;
}[] = [
  { tome: "I", year: 1882, title: "Commentarius in I librum Sententiarum", gloss: "Commentary on Book I of the Sentences — the Trinity", status: "published", href: "/browse/1" },
  { tome: "II", year: 1885, title: "Commentarius in II librum Sententiarum", gloss: "Commentary on Book II — creation, the angels, and sin", status: "published", href: "/browse/2" },
  { tome: "III", year: 1887, title: "Commentarius in III librum Sententiarum", gloss: "Commentary on Book III — the Incarnation and the virtues", status: "published", href: "/browse/3" },
  { tome: "IV", year: 1889, title: "Commentarius in IV librum Sententiarum", gloss: "Commentary on Book IV — the sacraments and the last things", status: "planned" },
  { tome: "V", year: 1891, title: "Opuscula varia theologica", gloss: "Breviloquium, Itinerarium mentis in Deum, Collationes in Hexaemeron", status: "planned" },
  { tome: "VI", year: 1893, title: "Commentarii in Sacram Scripturam", gloss: "Commentaries on Ecclesiastes, Wisdom, and John", status: "planned" },
  { tome: "VII", year: 1895, title: "Commentarius in Evangelium S. Lucae", gloss: "The full commentary on the Gospel of Luke", status: "planned" },
  { tome: "VIII", year: 1898, title: "Opuscula ad theologiam mysticam et res Ordinis", gloss: "Mystical and ascetic opuscula; Franciscan-order writings", status: "planned" },
  { tome: "IX", year: 1901, title: "Sermones", gloss: "Sermons — de tempore, de sanctis, Marian, and diverse", status: "planned" },
  { tome: "X", year: 1902, title: "Operum omnium complementum", gloss: "Supplements, general indices, and editorial apparatus", status: "planned" },
];
const SCOPE_LABEL: Record<ScopeStatus, string> = {
  published: "Published",
  "in-preparation": "In preparation",
  planned: "Planned",
};

export default function HomePage() {
  const books = loadAllContent();
  const totalTranslated = books.reduce(
    (sum, b) =>
      sum + b.distinctions.reduce((s, d) => s + d.questions.filter((q) => q.hasTranslation).length, 0),
    0
  );
  const totalQuestions = books.reduce(
    (sum, b) => sum + b.distinctions.reduce((s, d) => s + d.questions.length, 0),
    0
  );

  return (
    <div>
      <div style={{ textAlign: "center", margin: "2rem 0 3rem" }}>
        <Illumination size={80} letter="B" />
        <h2
          style={{
            fontFamily: "var(--font-cinzel-decorative), serif",
            fontSize: "28px",
            color: "#3D1308",
            margin: "1.5rem 0 0.5rem",
            fontWeight: 400,
          }}
        >
          The Bonaventure Opera Omnia
        </h2>
        <p
          style={{
            fontFamily: "var(--font-cinzel), serif",
            fontSize: "14px",
            letterSpacing: "0.15em",
            color: "#8B6914",
            textTransform: "uppercase",
          }}
        >
          A New English Translation
        </p>
        <CrossDivider />
        <p className="body-text" style={{ maxWidth: "700px", margin: "0 auto", textAlign: "center" }}>
          An English translation of the <em>Opera Omnia</em>&thinsp; of St. Bonaventure of Bagnoregio
          (1221&ndash;1274), the Seraphic Doctor, from the Quaracchi critical edition (1882&ndash;1902).
          The project will eventually present all ten volumes; currently published are Volumes I, II,
          and III, the <em>Commentaries on Books I, II, and III of the Sentences of Peter Lombard</em>. Future
          volumes will include the remaining commentary on Book IV of the Sentences, the{" "}
          <em>Breviloquium</em>, <em>Itinerarium mentis in Deum</em>, the{" "}
          <em>Collationes in Hexaemeron</em>, and other opuscula and sermons.
        </p>
      </div>

      <FleuronDivider />

      <div className="section-title">Published Volumes</div>
      {books.map((book) => {
        const translated = book.distinctions.reduce(
          (s, d) => s + d.questions.filter((q) => q.hasTranslation).length,
          0
        );
        const total = book.distinctions.reduce((s, d) => s + d.questions.length, 0);
        return (
          <Link key={book.id} href={`/browse/${book.id}`} className="card-link">
            <div className="card">
              <div style={{ display: "flex", alignItems: "flex-start", gap: "1rem" }}>
                <Illumination size={44} letter={`${book.id}`} />
                <div>
                  <h3 className="card-title">{book.title}</h3>
                  <p className="card-meta">
                    {book.distinctions.length} distinction
                    {book.distinctions.length !== 1 ? "s" : ""} &middot; {translated} of {total}{" "}
                    questions translated
                  </p>
                </div>
              </div>
            </div>
          </Link>
        );
      })}

      <FleuronDivider />

      <div className="section-title">The Full Opera Omnia &mdash; Project Scope</div>
      <p className="body-text" style={{ marginBottom: "1.5rem" }}>
        The Quaracchi <em>Opera Omnia</em>&thinsp; runs to ten volumes (1882&ndash;1902). Three are now
        complete &mdash; the commentaries on the first three books of the <em>Sentences</em>. The
        remaining seven, including Book IV of the <em>Sentences</em>&thinsp; and Bonaventure&rsquo;s
        opuscula, Scripture commentaries, and sermons, are still to come.
      </p>
      {OPERA_OMNIA.map((t) => {
        const row = (
          <div className={`scope-row scope-${t.status}`}>
            <span className="scope-num">{t.tome}</span>
            <div className="scope-body">
              <span className="scope-title">
                {t.title} <span className="scope-year">&middot; {t.year}</span>
              </span>
              <span className="scope-gloss">{t.gloss}</span>
            </div>
            <span className="scope-status">{SCOPE_LABEL[t.status]}</span>
          </div>
        );
        return t.href ? (
          <Link key={t.tome} href={t.href} className="card-link scope-link">
            {row}
          </Link>
        ) : (
          <div key={t.tome}>{row}</div>
        );
      })}

      <FleuronDivider />

      <div className="card" style={{ cursor: "default", background: "rgba(61,19,8,0.04)" }}>
        <div className="section-title">About this Project</div>
        <p className="body-text">
          Bonaventure of Bagnoregio (1221&ndash;1274), the Seraphic Doctor, composed his{" "}
          <em>Commentary on the Sentences</em>&thinsp; while teaching at the University of Paris. It remains
          one of the most important works of medieval theology, yet no complete English translation
          has ever been published. This project seeks to remedy that gap.
        </p>
        <Link href="/about" className="back-link" style={{ marginTop: "1rem", display: "inline-block" }}>
          Read More &rarr;
        </Link>
      </div>
    </div>
  );
}
