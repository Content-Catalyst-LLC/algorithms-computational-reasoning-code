export type RetrievalStructure = "hash_map" | "database_index" | "inverted_index" | "cache" | "content_addressing";
export type RetrievalCase = { name: string; structure: RetrievalStructure; retrievalQuality: number };
export const cases: RetrievalCase[] = [
  { name: "Article metadata dictionary", structure: "hash_map", retrievalQuality: 84.24 },
  { name: "Case status database index", structure: "database_index", retrievalQuality: 84.20 },
  { name: "Search inverted index", structure: "inverted_index", retrievalQuality: 83.24 },
  { name: "Cache for expensive computations", structure: "cache", retrievalQuality: 82.92 }
];
