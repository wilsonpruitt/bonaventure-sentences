import Link from "next/link";
import type { Question } from "@/lib/content";

// ----------------------------------------------------------------------------
// Grouping: partition a distinction's questions into logical sections.
//   - littera   → Lombard's text, at the top
//   - divisio   → its own section
//   - article   → one section per (pars, articulus)
//   - dubia     → one section at the bottom
// ----------------------------------------------------------------------------

type Section = {
  key: string;
  kind: "littera" | "divisio" | "article" | "dubia";
  pars?: number;
  articulus?: number;
  questions: Question[];
};

function groupQuestions(questions: Question[]): Section[] {
  const sections: Section[] = [];
  for (const q of questions) {
    let key: string;
    let kind: Section["kind"];
    if (q.type === "littera-magistri" || q.type === "littera") {
      key = "littera";
      kind = "littera";
    } else if (q.type === "divisio") {
      key = "divisio";
      kind = "divisio";
    } else if (q.type === "dubia") {
      key = "dubia";
      kind = "dubia";
    } else {
      key = `art-${q.pars ?? 0}-${q.articulus ?? 0}`;
      kind = "article";
    }
    const existing = sections.find((s) => s.key === key);
    if (existing) {
      existing.questions.push(q);
    } else {
      sections.push({
        key,
        kind,
        pars: q.pars,
        articulus: q.articulus,
        questions: [q],
      });
    }
  }
  return sections;
}

function sectionHeading(section: Section): string {
  if (section.kind === "littera") return "Littera Magistri";
  if (section.kind === "divisio") return "Division of the Text";
  if (section.kind === "dubia") return "Dubia";
  const parts: string[] = [];
  if (section.pars) parts.push(`Part ${romanize(section.pars)}`);
  if (section.articulus !== undefined && section.articulus > 0) {
    parts.push(`Article ${section.articulus}`);
  } else if (section.articulus === 0) {
    parts.push("Sole Article");
  }
  return parts.join(" · ") || "Questions";
}

export function romanize(n: number): string {
  const map: [number, string][] = [
    [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"],
  ];
  let out = "";
  let rem = n;
  for (const [v, s] of map) {
    while (rem >= v) {
      out += s;
      rem -= v;
    }
  }
  return out || String(n);
}

function cardEyebrow(q: Question): string | null {
  if (q.type === "littera-magistri" || q.type === "littera") return null;
  if (q.type === "dubia") return null;
  if (q.type === "divisio") return null;
  if (q.quaestio === undefined) return null;
  if (q.quaestio === 0) return "Sole Question";
  return `Q. ${q.quaestio}`;
}

function cardTitle(q: Question): string {
  if (q.type === "littera-magistri" || q.type === "littera")
    return "Lombard's Text";
  if (q.type === "dubia") return "Dubia";
  if (q.type === "divisio") return "Divisio Textus";
  // Prefer English title if the chunk has been rebuilt in unified format.
  if (q.titleEn) return q.titleEn;
  if (q.quaestio !== undefined) {
    return q.quaestio === 0 ? "Sole Question" : `Question ${q.quaestio}`;
  }
  return q.title;
}

// ----------------------------------------------------------------------------
// <DistinctionContent> — renders a distinction's sections + question cards.
// Used by both the distinction detail page and the book-page accordion.
// ----------------------------------------------------------------------------

export function DistinctionContent({
  bookId,
  distId,
  questions,
}: {
  bookId: number;
  distId: number;
  questions: Question[];
}) {
  const sections = groupQuestions(questions);
  return (
    <div className="dist-sections">
      {sections.map((section) => (
        <section key={section.key} className="dist-section">
          <h3 className="article-heading">{sectionHeading(section)}</h3>
          <ul className="question-list">
            {section.questions.map((q) => {
              const eyebrow = cardEyebrow(q);
              const title = cardTitle(q);
              return (
                <li key={q.id}>
                  <Link
                    href={`/browse/${bookId}/d/${distId}/q/${encodeURIComponent(q.id)}`}
                    className="question-card"
                  >
                    <div className="question-card-body">
                      {eyebrow && (
                        <span className="question-card-eyebrow">{eyebrow}</span>
                      )}
                      <span className="question-card-title">{title}</span>
                    </div>
                    {q.hasTranslation && (
                      <span className="translated-dot" aria-label="translated" />
                    )}
                  </Link>
                </li>
              );
            })}
          </ul>
        </section>
      ))}
    </div>
  );
}
