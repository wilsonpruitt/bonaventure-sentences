import { notFound } from "next/navigation";
import { loadAllContent } from "@/lib/content";
import { BookView } from "@/components/book-view";

// /{slug}: a work's landing page (Tome V onward). Divisions are anchors on it
// (`#d-N`). Static routes (/about, /search…) take precedence over this one,
// and addresses.mjs refuses a slug that would shadow them.
export const dynamicParams = false;

export function generateStaticParams() {
  return loadAllContent()
    .filter((b) => b.slug !== "sentences")
    .map((b) => ({ work: b.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ work: string }> }) {
  const { work } = await params;
  const b = loadAllContent().find((x) => x.path === `/${work}`);
  return b ? { title: b.title, alternates: { canonical: `https://bonaventure.wrootpress.com${b.path}` } } : {};
}

export default async function Page({ params }: { params: Promise<{ work: string }> }) {
  const { work } = await params;
  const b = loadAllContent().find((x) => x.path === `/${work}`);
  if (!b) notFound();
  return <BookView book={b} />;
}
