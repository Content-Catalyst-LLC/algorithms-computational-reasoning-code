export type NodeType = "Concept" | "Article" | "Reference" | "Repository" | "Dataset" | "Source";
export type EdgeType = "related_to" | "uses" | "requires" | "supports" | "cites" | "implements";
export function hybridScore(lexical: number, vector: number, graph: number, provenance: number): number {
  return 100 * (0.25*lexical + 0.25*vector + 0.25*graph + 0.25*provenance);
}
export function graphPathScore(pathLength: number, relationshipConfidence: number, provenanceStrength: number, reviewStatus: number): number {
  const lengthFactor = 1 / (1 + Math.max(pathLength - 1, 0));
  return 100 * (0.25*lengthFactor + 0.30*relationshipConfidence + 0.30*provenanceStrength + 0.15*reviewStatus);
}
