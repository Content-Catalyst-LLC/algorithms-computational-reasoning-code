export type KnowledgeLayer = "schema" | "constraint" | "query" | "metadata" | "provenance" | "governance";
export function schemaQuality(fields: number, keys: number, constraints: number, metadata: number, lineage: number): number {
  return 100 * (0.22*fields + 0.20*keys + 0.20*constraints + 0.20*metadata + 0.18*lineage);
}
