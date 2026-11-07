import { notFound } from "next/navigation";
import { loadAllContent } from "@/lib/content";
import { BookView } from "@/components/book-view";

// /sentences/{book}: one book of the Commentary on the Sentences (Tomes I–IV).
export const dynamicParams = false;

export function generateStaticParams() {
  return loadAllContent()
    .filter((b) => b.slug === "sentences")
    .map((b) => ({ book: String(b.id) }));
}

export async function generateMetadata({ params }: { params: Promise<{ book: string }> }) {
  const { book } = await params;
  const b = loadAllContent().find((x) => x.path === `/sentences/${book}`);
  return b ? { title: b.title, alternates: { canonical: `https://bonaventure.wrootpress.com${b.path}` } } : {};
}

export default async function Page({ params }: { params: Promise<{ book: string }> }) {
  const { book } = await params;
  const b = loadAllContent().find((x) => x.path === `/sentences/${book}`);
  if (!b) notFound();
  return <BookView book={b} />;
}
