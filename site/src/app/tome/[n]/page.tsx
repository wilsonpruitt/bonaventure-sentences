import { notFound } from "next/navigation";
import { loadAllContent, tomeGroups } from "@/lib/content";
import { TomeView } from "@/components/tome-view";

// /tome/{n}: a tome that holds several works (Tome V onward).
export const dynamicParams = false;

export function generateStaticParams() {
  return tomeGroups(loadAllContent()).map((t) => ({ n: `${t.tome}` }));
}

export async function generateMetadata({ params }: { params: Promise<{ n: string }> }) {
  const { n } = await params;
  const t = tomeGroups(loadAllContent()).find((x) => `${x.tome}` === n);
  return t ? { title: t.title, alternates: { canonical: `https://bonaventure.wrootpress.com/tome/${n}` } } : {};
}

export default async function Page({ params }: { params: Promise<{ n: string }> }) {
  const { n } = await params;
  const tome = tomeGroups(loadAllContent()).find((t) => `${t.tome}` === n);
  if (!tome) notFound();
  return <TomeView tome={tome} />;
}
