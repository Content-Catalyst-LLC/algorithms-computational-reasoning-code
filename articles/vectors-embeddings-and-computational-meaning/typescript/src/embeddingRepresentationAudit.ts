export type EmbeddingUse = "semantic_search" | "case_similarity" | "recommendation" | "image_text_retrieval" | "graph_embedding";
export type EmbeddingCase = { name: string; use: EmbeddingUse; embeddingQuality: number };
export const cases: EmbeddingCase[] = [
  { name: "Semantic article search", use: "semantic_search", embeddingQuality: 83.92 },
  { name: "Case similarity review", use: "case_similarity", embeddingQuality: 84.20 },
  { name: "Content recommendation", use: "recommendation", embeddingQuality: 80.48 },
  { name: "Image-text retrieval", use: "image_text_retrieval", embeddingQuality: 81.80 }
];
