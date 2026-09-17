import Link from "next/link";
import { Illumination, CrossDivider, FleuronDivider } from "@/components/decorations";
import progress from "@/data/progress.json";

// Every figure on this page comes out of src/data/progress.json, which
// scripts/build-progress.mjs regenerates from the corpus on each build. Nothing
// here is typed by hand, because a hand-typed number would be wrong inside a
// week. If a figure looks wrong, the script is where it is wrong.

export const metadata = {
  title: "Progress",
  description:
    "How much of the Quaracchi Opera Omnia of St. Bonaventure is translated, measured in printed pages.",
};

type Volume = (typeof progress.volumes)[number] & {
  works?: {
    slug: string;
    title: string;
    extent: string;
    done: number;
    total: number;
    complete: boolean;
    approxEnd?: boolean;
  }[];
  pendingPages?: number;
  nonTextLeaves?: number;
  approxEnd?: boolean;
};

const n = (x: number) => x.toLocaleString("en-US");

function Bar({
  done,
  total,
  estimated = false,
  headline = false,
  editionTotal,
}: {
  done: number;
  total: number;
  estimated?: boolean;
  headline?: boolean;
  editionTotal?: number;
}) {
  // A per-volume bar is scaled to its own volume. The headline bar is scaled to
  // the whole edition, so the hatched estimate can be shown at true width.
  const span = editionTotal ?? total;
  const pct = (v: number) => `${(v / span) * 100}%`;
  return (
    <div className={`prog-bar${headline ? " prog-bar--headline" : ""}`}>
      <div className="prog-seg prog-seg--done" style={{ width: pct(done) }} />
      <div
        className={`prog-seg ${estimated ? "prog-seg--est" : "prog-seg--todo"}`}
        style={{ width: pct(Math.max(total - done, 0)) }}
      />
      {editionTotal !== undefined && (
        <div
          className="prog-seg prog-seg--est"
          style={{ width: pct(Math.max(editionTotal - total, 0)) }}
        />
      )}
    </div>
  );
}

export default function ProgressPage() {
  const volumes = progress.volumes as Volume[];
  const volV = volumes.find((v) => v.n === 5)!;

  return (
    <div style={{ maxWidth: "820px", margin: "0 auto" }}>
      <div style={{ textAlign: "center", marginBottom: "2rem" }}>
        <Illumination size={70} letter="Q" color="#3D1308" />
        <h2 className="h2" style={{ fontSize: "24px", marginTop: "1rem" }}>
          Quantum Translatum Sit
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
          How Much Is Done
        </p>
      </div>

      <CrossDivider />

      {/* ---------------------------------------------------------------- */}
      {/* Headline                                                          */}
      {/* ---------------------------------------------------------------- */}
      <div style={{ margin: "2.5rem 0 1rem", textAlign: "center" }}>
        <div className="prog-headline-figure">
          {n(progress.pagesTranslated)}{" "}
          <span className="prog-of">
            of about {n(progress.editionTotal)} printed pages
          </span>
        </div>
      </div>

      <Bar
        done={progress.pagesTranslated}
        total={progress.measuredTotal}
        editionTotal={progress.editionTotal}
        headline
      />

      <div className="prog-legend">
        <span>
          <i className="prog-swatch prog-seg--done" /> Translated
        </span>
        <span>
          <i className="prog-swatch prog-seg--todo" /> Remaining, extent measured
        </span>
        <span>
          <i className="prog-swatch prog-seg--est" /> Remaining, extent estimated
        </span>
      </div>

      <p className="body-text" style={{ marginTop: "1.5rem" }}>
        The Quaracchi <em>Opera Omnia</em>&thinsp; (Vols. I&ndash;X, 1882&ndash;1902) is the
        critical edition of everything Bonaventure wrote.{" "}
        <strong>{n(progress.pagesTranslated)} of its printed pages are translated here</strong> —
        every page of the commentary on all four books of the <em>Sentences</em>, and{" "}
        {n(volV.done)} of the {n(volV.total)} pages of Volume V, the <em>Opuscula</em>.
      </p>
      <p className="body-text" style={{ marginTop: "1.25rem" }}>
        That is {progress.pctOfMeasured}% of the {n(progress.measuredTotal)} pages of Volumes
        I through V, which is the part of the edition whose extent has actually been measured,
        page by page, against the printed leaves. Volumes VI through X have not been set in type
        here at all &mdash; not a page of their source text is yet in hand &mdash; so their
        length is an <em>estimate</em>, drawn from the project&rsquo;s own scoping notes and
        rounded to the nearest hundred pages. Against the edition as a whole, estimate included,
        the figure is about {progress.pctOfEdition}%. The two numbers are kept apart on purpose:
        the first is measured, the second is not.
      </p>

      <FleuronDivider />

      {/* ---------------------------------------------------------------- */}
      {/* What is being counted                                             */}
      {/* ---------------------------------------------------------------- */}
      <div className="section-title">What Is Counted, and What &ldquo;Translated&rdquo; Means</div>
      <p className="body-text" style={{ marginBottom: "1.25rem" }}>
        The unit is the printed page of the Quaracchi edition &mdash; not the word, not the
        chapter, not the file. Each unit of text on this site records the printed pages it was
        set from, and the count above is the number of <em>distinct</em> pages those records
        cover. Distinct matters: consecutive passages share the leaf they straddle, and adding
        them up would count every shared leaf twice.
      </p>
      <p className="body-text" style={{ marginBottom: "1.25rem" }}>
        A page counts as translated only at what this project calls Tier 2: the Latin re-set from
        the edition&rsquo;s own text and checked against a high-resolution image of the printed
        column, a fresh literal English translation rather than a paraphrase, and the full
        critical apparatus read off the footer of that same page. Nothing is counted as a draft
        to be improved later. The procedure, and why it is built the way it is, is set out{" "}
        <Link href="/about" style={{ textDecoration: "underline" }}>
          on the About page
        </Link>
        .
      </p>

      <FleuronDivider />

      {/* ---------------------------------------------------------------- */}
      {/* Per volume                                                        */}
      {/* ---------------------------------------------------------------- */}
      <div className="section-title">By Volume</div>

      {volumes.map((v) => {
        const estimated = v.basis === "estimated";
        return (
          <div
            key={v.n}
            className={`prog-row${v.state === "planned" ? " prog-row--planned" : ""}`}
          >
            <span className="prog-tome">{v.tome}</span>
            <div>
              <span className="prog-title">
                {v.title}{" "}
                <span className="scope-year">&middot; {v.year}</span>
              </span>
              <br />
              <span className="prog-gloss">{v.gloss}</span>
            </div>
            <div className="prog-count">
              {estimated ? (
                <>
                  0 / ~{n(v.total)} pp.
                  <em>Estimated extent</em>
                </>
              ) : (
                <>
                  {n(v.done)} / {v.approxEnd ? "~" : ""}
                  {n(v.total)} pp.
                  <em>{v.state === "complete" ? "Complete" : "In progress"}</em>
                </>
              )}
            </div>

            <div className="prog-rowbar">
              <Bar done={v.done} total={v.total} estimated={estimated} />
            </div>

            {v.state === "complete" && v.shortfall > 0 && (
              <p className="prog-note">
                The commentary is complete. {v.shortfall}{" "}
                {v.shortfall === 1 ? "leaf of" : "leaves of"} this volume carry no page record:
                on the evidence gathered so far these are passages that were transcribed under a
                neighbouring page&rsquo;s number rather than text that is absent, and they are
                left out of the count above rather than claimed.
              </p>
            )}

            {v.n === 5 && v.works && (
              <>
                <p className="prog-note">
                  Nine of the ten works are finished; the sermons remain. Of the{" "}
                  {v.shortfall} pages still outstanding, {v.pendingPages} belong to the sermons
                  and {v.nonTextLeaves} are half-titles, blank versos, and the editorial tables of
                  chapters, which carry no text to translate.
                </p>
                <div className="prog-works">
                  {v.works.map((w) => (
                    <div
                      key={w.slug}
                      className={`prog-work${w.complete ? "" : " prog-work--pending"}`}
                    >
                      <span className="prog-work-title">
                        <em>{w.title}</em>{" "}
                        <span className="prog-work-count">{w.extent}</span>
                      </span>
                      <span className={w.complete ? "prog-work-done" : "prog-work-count"}>
                        {n(w.done)} / {w.approxEnd ? "~" : ""}
                        {n(w.total)} pp.
                        {w.complete ? " · Complete" : ""}
                      </span>
                    </div>
                  ))}
                </div>
              </>
            )}
          </div>
        );
      })}

      <FleuronDivider />

      <p
        className="body-text"
        style={{ fontSize: "13px", color: "rgba(107,74,58,0.9)", textAlign: "center" }}
      >
        Figures recomputed from the corpus each time this site is built. Corpus as of{" "}
        {progress.asOf}.
      </p>
    </div>
  );
}
