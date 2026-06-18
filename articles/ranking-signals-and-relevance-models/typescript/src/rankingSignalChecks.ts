export type RankingSignal = "lexical" | "field_weight" | "metadata" | "freshness" | "authority" | "semantic" | "feedback" | "provenance";
export function precisionAtK(tp: number, k: number): number { return k === 0 ? 0 : tp / k; }
export function rankingScore(lexical: number, metadata: number, freshness: number, authority: number, semantic: number, provenance: number): number {
  return 100 * (0.22*lexical + 0.18*metadata + 0.12*freshness + 0.16*authority + 0.17*semantic + 0.15*provenance);
}
