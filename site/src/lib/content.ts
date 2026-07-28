import contentData from "@/data/content.json";

export interface ApparatusEntry {
  id: string;
  la: string;
  en: string;
}

export interface Question {
  id: string;
  title: string;
  titleLa?: string;
  titleEn?: string;
  type: string;
  latin: string;
  english: string;
  latinScholion: string;
  englishScholion: string;
  apparatus: ApparatusEntry[];
  notes: string;
  hasTranslation: boolean;
  pars?: number;
  articulus?: number;
  quaestio?: number;
  capitulum?: number;
  section?: number;
}

export interface Distinction {
  id: number;
  title: string;
  questions: Question[];
}

export interface Book {
  id: number;
  title: string;
  distinctions: Distinction[];
  // Vol V+ works only (Tome V onward holds multiple independent works;
  // each work is a Book whose divisions replace the Sentences' distinctions):
  tome?: number;
  initial?: string; // Illumination glyph, e.g. "B" for Breviloquium
  divisionLabel?: string; // e.g. "Parts" — UI label replacing "Distinctions"
}

export function loadAllContent(): Book[] {
  return contentData as Book[];
}
