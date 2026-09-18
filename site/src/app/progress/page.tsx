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
  counted?: boolean;
  extent?: string;
  source?: {
    archiveId: string;
    identity: string;
    bodyStart: string;
    bodyEnd: string;
    confidence: string;
  };
};

const n = (x: number) => x.toLocaleString("en-US");
const round1 = (x: number) => Math.round(x * 10) / 10;

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
  const all = progress.volumes as Volume[];
  const volumes = all.filter((v) => v.counted !== false);
  const uncounted = all.filter((v) => v.counted === false);
  const volV = volumes.find((v) => v.n === 5)!;
  const anyEstimated = volumes.some((v) => v.basis === "estimated");

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
            of {anyEstimated ? "about " : ""}
            {n(progress.editionTotal)} printed pages
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
        {anyEstimated && (
          <span>
            <i className="prog-swatch prog-seg--est" /> Remaining, extent estimated
          </span>
        )}
      </div>

      <p className="body-text" style={{ marginTop: "1.5rem" }}>
        The Quaracchi <em>Opera Omnia</em>&thinsp; (Vols. I&ndash;X, 1882&ndash;1902) is the
        critical edition of everything Bonaventure wrote.{" "}
        <strong>{n(progress.pagesTranslated)} of its printed pages are translated here</strong> —
        every page of the commentary on all four books of the <em>Sentences</em>, and{" "}
        {n(volV.done)} of the {n(volV.total)} pages of Volume V, the <em>Opuscula</em>.
      </p>
      <p className="body-text" style={{ marginTop: "1.25rem" }}>
        That is {progress.pctOfMeasured}% of the {n(progress.measuredTotal)} pages this project
        counts as text to translate &mdash; and every one of those pages is{" "}
        <em>measured</em>, not estimated. Volumes I through V are measured from the corpus
        itself, page by page. Volumes VI through IX have not been set in type here at all, but
        their extent is no longer a guess either: each was measured in September 2026 against
        the digitized Quaracchi volume, by finding the last leaf of its body text and reading
        the page number off the running head. What that replaced were round hundreds carried
        over from the project&rsquo;s own scoping notes, which were never more than a guess and
        are now gone from this page.{anyEstimated ? " " : ""}
        {anyEstimated && (
          <>
            Volume{progress.estimatedTomes.length > 1 ? "s" : ""}{" "}
            {progress.estimatedTomes.join(", ")} could not be settled and{" "}
            {progress.estimatedTomes.length > 1 ? "remain estimates" : "remains an estimate"};{" "}
            {progress.estimatedTomes.length > 1 ? "they are" : "it is"} shown hatched above and
            counted apart, which is why the figure against the whole is{" "}
            {progress.pctOfEdition}% rather than {progress.pctOfMeasured}%.
          </>
        )}
      </p>
      {uncounted.length > 0 && (
        <p className="body-text" style={{ marginTop: "1.25rem" }}>
          One volume is deliberately outside that count. Volume X ({n(uncounted[0].total)}{" "}
          pages, also measured) is the edition&rsquo;s prolegomena, general indices and critical
          apparatus rather than a work of Bonaventure&rsquo;s; the indices this site offers are
          generated from the text itself, which supersedes Quaracchi&rsquo;s. It is therefore
          not counted as text to translate. That is a scope decision, and it is stated rather
          than made silently: counting it would put the figure at{" "}
          {round1(
            (progress.pagesTranslated / (progress.editionTotal + uncounted[0].total)) * 100
          )}
          % instead.
        </p>
      )}

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
                  {n(v.done)} / ~{n(v.total)} pp.
                  <em>Estimated extent</em>
                </>
              ) : v.state === "planned" ? (
                <>
                  {n(v.done)} / {n(v.total)} pp.
                  <em>Extent measured</em>
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

            {v.state === "planned" && v.source && (
              <p className="prog-note">
                Not yet begun. Its extent is measured, not assumed: pp. {v.extent?.replace("pp. ", "")}{" "}
                of the Quaracchi volume digitized as{" "}
                <a
                  href={`https://archive.org/details/${v.source.archiveId}`}
                  style={{ textDecoration: "underline" }}
                >
                  {v.source.archiveId}
                </a>
                , whose identity was confirmed from its {v.n === 10 ? "own contents leaf" : "title page and prolegomena"} rather than
                from its identifier, and whose last body page was read from the running head of
                the last leaf before the volume&rsquo;s own index.
              </p>
            )}

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

      {uncounted.length > 0 && (
        <>
          <div className="section-title" style={{ marginTop: "2rem" }}>
            Outside the Count
          </div>
          {uncounted.map((v) => (
            <div key={v.n} className="prog-row prog-row--planned">
              <span className="prog-tome">{v.tome}</span>
              <div>
                <span className="prog-title">
                  {v.title} <span className="scope-year">&middot; {v.year}</span>
                </span>
                <br />
                <span className="prog-gloss">{v.gloss}</span>
              </div>
              <div className="prog-count">
                {n(v.total)} pp.
                <em>Not counted</em>
              </div>
              <p className="prog-note">
                Quaracchi&rsquo;s prolegomena, general indices and critical apparatus &mdash; the
                editors&rsquo; volume about the edition, not a further work of
                Bonaventure&rsquo;s. This site generates its own indices from the translated
                text, which supersedes it. Its {n(v.total)} pages are measured all the same, from{" "}
                <a
                  href={`https://archive.org/details/${v.source?.archiveId}`}
                  style={{ textDecoration: "underline" }}
                >
                  {v.source?.archiveId}
                </a>
                , and they are named here rather than dropped out of sight.
              </p>
            </div>
          ))}
        </>
      )}

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
