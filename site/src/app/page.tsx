import Link from "next/link";
import { loadAllContent } from "@/lib/content";
import { Illumination, CrossDivider, FleuronDivider } from "@/components/decorations";

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
          An English translation of the <em>Opera Omnia</em> of St. Bonaventure of Bagnoregio
          (1221&ndash;1274), the Seraphic Doctor, from the Quaracchi critical edition (1882&ndash;1902).
          The project will eventually present all ten volumes; currently published is Volume I, the{" "}
          <em>Commentary on Book I of the Sentences of Peter Lombard</em>. Future volumes will include
          the remaining commentaries on Books II&ndash;IV of the Sentences, the <em>Breviloquium</em>,{" "}
          <em>Itinerarium mentis in Deum</em>, the <em>Collationes in Hexaemeron</em>, and other
          opuscula and sermons.
        </p>
      </div>

      <FleuronDivider />

      <div className="section-title">Volume I — Commentary on the Sentences</div>
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

      <div className="card" style={{ cursor: "default", background: "rgba(61,19,8,0.04)" }}>
        <div className="section-title">About this Project</div>
        <p className="body-text">
          Bonaventure of Bagnoregio (1221&ndash;1274), the Seraphic Doctor, composed his{" "}
          <em>Commentary on the Sentences</em> while teaching at the University of Paris. It remains
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
