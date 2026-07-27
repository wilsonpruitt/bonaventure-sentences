import { Illumination, CrossDivider, FleuronDivider } from "@/components/decorations";

export const metadata = {
  title: "Rights and Reuse",
  description:
    "The Quaracchi Latin is public domain. The English translation, notes, and structured text are licensed CC BY-NC 4.0 — free to share and build on, not to sell.",
};

// The human-readable face of the LICENSE file at the repo root. The two must
// agree; if the terms change, change both. The distinction doing the work:
// the Quaracchi text is public domain and stays that way, and what is licensed
// is our English, our apparatus, and our encoding.
export default function RightsPage() {
  return (
    <div style={{ maxWidth: "750px", margin: "0 auto" }}>
      <div style={{ textAlign: "center", marginBottom: "2rem" }}>
        <Illumination size={70} letter="I" color="#3D1308" />
        <h2 className="h2" style={{ fontSize: "24px", marginTop: "1rem" }}>
          De Iure Utendi
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
          Rights and Reuse
        </p>
      </div>

      <CrossDivider />

      <div className="body-text">
        <p style={{ marginBottom: "1.25rem", fontStyle: "italic" }}>
          The short version: the Latin is free without condition. The English is free for
          everything except selling.
        </p>

        <div className="section-title">The Quaracchi Latin Is Public Domain</div>
        <p style={{ marginBottom: "1.25rem" }}>
          Bonaventure died in 1274, and the Quaracchi critical edition
          (1882&ndash;1902) is long out of copyright &mdash; text and editorial apparatus
          alike. Transcribing a public-domain text faithfully creates no new copyright in
          it, and nothing here pretends otherwise. Take the Latin and do as you like with
          it. You need nothing from us.
        </p>

        <FleuronDivider />

        <div className="section-title">The English Translation Is Licensed</div>
        <p style={{ marginBottom: "1.25rem" }}>
          The translation is new &mdash; littera, articuli, quaestiones, responsiones, and
          dubia, together with the scholia and the full critical apparatus, rendered
          literally rather than paraphrased. So are the apparatus labels, the translator&apos;s
          notes, and the explanatory text throughout this site.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          So, less obviously, is the <em>structure</em>: the
          book&#8211;distinction&#8211;part&#8211;article&#8211;question addressing scheme and its
          slugs, the chunking and segmentation, the alignment of each English passage to its
          Latin, the normalized Latin, and every correction recorded in the audit and
          manual-review queues. That structure is what makes the Quaracchi text citable and
          readable rather than a wall of scanned column. It is claimed here as a compilation
          &mdash; the arrangement and the encoding, not the text underneath. Lifting the
          Latin is free. Lifting our addressing, segmentation, and alignment is not.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          All of it is offered to the public under the{" "}
          <a
            href="https://creativecommons.org/licenses/by-nc/4.0/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Creative Commons Attribution&#8209;NonCommercial 4.0 International License
          </a>
          .
        </p>

        <FleuronDivider />

        <div className="section-title">So, Concretely</div>
        <p style={{ marginBottom: "1.25rem" }}>
          <strong>Yes, freely, and there is no need to ask.</strong> Quote a quaestio in a
          sermon. Assign a distinction to a seminar. Post a translation to a friary or parish
          site. Cite it in a dissertation. Put a whole article into a study guide you give
          away. Translate our English into another language. Correct us and publish the
          correction. Mirror the entire site. Just credit the work, link the license, and note
          if you changed something.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          <strong>Ask first.</strong> Selling it &mdash; a print or ebook edition offered for
          sale, a subscription or paywalled database, a commercial reference product or piece
          of software with the translation inside it.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          <strong>Asking works.</strong> Permission is given readily, and given free for
          scholarly and ecclesial projects. What the license is actually for is the case this
          project exists against: the commercial databases that have kept the scholastics
          behind a login for a generation, and the reprint shops that would scrape a corpus
          like this one and sell it back to the people it was made for. Write to{" "}
          <a href="mailto:wilson@wrootlabs.com">wilson@wrootlabs.com</a> and say what you have
          in mind.
        </p>

        <FleuronDivider />

        <div className="section-title">Attribution</div>
        <p style={{ marginBottom: "1.25rem" }}>Anything along these lines will do:</p>
        <blockquote
          style={{
            margin: "1.5rem 0 1.5rem 1.5rem",
            paddingLeft: "1rem",
            borderLeft: "2px solid #8B6914",
            fontStyle: "italic",
          }}
        >
          English translation of Bonaventure&apos;s <em>Commentary on the Sentences</em> by
          Wilson Pruitt (Wroot Press), licensed CC&nbsp;BY&#8209;NC&nbsp;4.0. Latin source:
          Quaracchi edition, public domain.
        </blockquote>
        <p style={{ marginBottom: "1.25rem" }}>
          Note that this translation is a working draft; passages under review are marked as
          such. Cite it as a draft, and check back for revisions.
        </p>

        <p style={{ fontSize: "13px", opacity: 0.75, marginTop: "2.5rem" }}>
          This is a Wroot Press work; Wroot Press is an imprint of Wroot Labs LLC. The
          copyright holder retains all rights and is not bound by this license &mdash; Wroot
          Press publishes print editions drawn from this material, which is part of how the
          translation gets paid for. The full legal statement lives in the{" "}
          <code>LICENSE</code> file in the project repository.
        </p>
      </div>
    </div>
  );
}
