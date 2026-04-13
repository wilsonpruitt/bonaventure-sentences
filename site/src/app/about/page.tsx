import { Illumination, CrossDivider, FleuronDivider } from "@/components/decorations";

export default function AboutPage() {
  return (
    <div style={{ maxWidth: "750px", margin: "0 auto" }}>
      <div style={{ textAlign: "center", marginBottom: "2rem" }}>
        <Illumination size={70} letter="D" color="#3D1308" />
        <h2 className="h2" style={{ fontSize: "24px", marginTop: "1rem" }}>
          De Hoc Opere
        </h2>
        <p
          style={{
            fontFamily: "var(--font-cinzel), serif",
            fontSize: "13px",
            letterSpacing: "0.12em",
            color: "#8B6914",
            textTransform: "uppercase",
          }}
        >
          About this Project
        </p>
      </div>

      <CrossDivider />

      <div className="body-text">
        <p style={{ marginBottom: "1.25rem" }}>
          This project presents an English translation of the <em>Opera Omnia</em> of St. Bonaventure
          of Bagnoregio (1221&ndash;1274), the Seraphic Doctor — drawn from the Quaracchi critical
          edition (Vols. I&ndash;X, 1882&ndash;1902) prepared by the Fathers of the Collegium
          S. Bonaventurae.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          We begin with Volume I, the <em>Commentary on Book I of the Sentences of Peter Lombard</em>,
          and intend over time to publish all ten volumes — the remaining commentaries on the
          Sentences (Books II&ndash;IV), the <em>Breviloquium</em>, the <em>Itinerarium mentis in
          Deum</em>, the <em>Collationes in Hexaemeron</em>, and the rest of the opuscula and sermons.
          No complete English edition of the Opera Omnia has ever been published.
        </p>

        <FleuronDivider />

        <div className="section-title">Translation Methodology</div>
        <p style={{ marginBottom: "1.25rem" }}>
          This translation aims for formal academic English suitable for theological scholarship. We
          maintain a paragraph-for-paragraph correspondence with the Latin text, preserving the
          structural markers that appear in the source (distinctions, articles, questions) without
          adding editorial apparatus beyond what the original contains.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          Standard scholastic formulae are translated consistently throughout:{" "}
          <em>Videtur quod</em> as &ldquo;It seems that,&rdquo; <em>Sed contra</em> as &ldquo;On
          the contrary,&rdquo; <em>Respondeo dicendum quod</em> as &ldquo;I respond: It must be
          said that,&rdquo; and so on. Key philosophical and theological terms are rendered according
          to established conventions in the English-language study of medieval thought.
        </p>

        <div className="section-title">The Latin Text</div>
        <p style={{ marginBottom: "1.25rem" }}>
          Our source text is the Quaracchi critical edition (
          <em>Opera Omnia S. Bonaventurae</em>, 1882&ndash;1902), digitized via OCR from Internet
          Archive scans. Common OCR artifacts (broken words, letter substitutions, garbled marginal
          glosses) have been silently corrected. We additionally provide literal English translations
          of the Quaracchi <em>scholia</em> and apparatus footnotes alongside the original Latin —
          since these editorial notes form an essential part of the scholarly value of this edition,
          and have themselves never been translated.
        </p>

        <div className="section-title">Key Terms</div>
        <p style={{ marginBottom: "1.25rem" }}>
          The following scholastic terms are rendered consistently: <em>uti</em> &rarr; to use;{" "}
          <em>frui</em> &rarr; to enjoy; <em>ratio</em> &rarr; account/ground;{" "}
          <em>processio</em> &rarr; procession; <em>suppositum</em> &rarr; supposit;{" "}
          <em>potentia</em> &rarr; potency/power; <em>actus</em> &rarr; act/actuality;{" "}
          <em>caritas</em> &rarr; charity; <em>exemplar</em> &rarr; exemplar;{" "}
          <em>vestigium</em> &rarr; vestige; <em>similitudo</em> &rarr; likeness;{" "}
          <em>honestum</em> &rarr; the honorable; <em>complacentia</em> &rarr; complacency;{" "}
          <em>actus quietativus</em> &rarr; quietative act.
        </p>

        <div className="section-title">Status &amp; Contributors</div>
        <p style={{ marginBottom: "1.25rem" }}>
          This is a working draft and collaborative effort. The translations presented here are
          provisional and subject to revision as the project continues. We welcome inquiries from
          scholars interested in contributing to or reviewing this work.
        </p>

        <FleuronDivider />

        <div
          className="card"
          style={{ cursor: "default", background: "rgba(61,19,8,0.04)", textAlign: "center" }}
        >
          <p style={{ fontFamily: "var(--font-cinzel), serif", fontSize: "14px", color: "#3D1308", marginBottom: "0.25rem" }}>
            Ad Maiorem Dei Gloriam
          </p>
          <p style={{ fontSize: "13px", color: "#8B6914", fontStyle: "italic" }}>
            &ldquo;For the perfection of the Christian, I propose a work that pertains to the
            beginning of learning.&rdquo;
          </p>
          <p style={{ fontSize: "12px", color: "#6B4A3A", marginTop: "0.5rem" }}>
            &mdash; Bonaventure, <em>Breviloquium</em>, Prol.
          </p>
        </div>
      </div>
    </div>
  );
}
