import type { MetadataRoute } from "next";
import { loadAllContent, tomeGroups, tomePath } from "@/lib/content";
import toc from "@/data/index-scripture-toc.json";
import { authorityToc } from "@/lib/authorities";

const BASE = "https://bonaventure.wrootpress.com";

// Mirrors the generateStaticParams of every route so the sitemap and the
// exported pages cannot drift apart.
export const dynamic = "force-static";

export default function sitemap(): MetadataRoute.Sitemap {
  const urls: string[] = [
    "/",
    "/about",
    "/browse",
    "/scripture",
    "/authorities",
    "/search",
    "/progress",
    "/rights",
    "/export",
  ];

  const books = loadAllContent();

  for (const tome of tomeGroups(books)) {
    urls.push(tomePath(tome.tome));
  }

  // Readable addresses only; a division of a work is an anchor, not a page.
  for (const book of books) {
    urls.push(book.path);
    for (const dist of book.distinctions) {
      if (!dist.path.includes("#")) urls.push(dist.path);
      for (const q of dist.questions) urls.push(q.path);
    }
  }

  for (const b of toc.books as { slug: string }[]) {
    urls.push(`/scripture/${b.slug}`);
  }

  for (const a of authorityToc()) {
    urls.push(`/authorities/${a.id}`);
    for (const w of a.works) urls.push(`/authorities/${a.id}/${w.id}`);
  }

  return urls.map((url) => ({ url: `${BASE}${url}` }));
}
