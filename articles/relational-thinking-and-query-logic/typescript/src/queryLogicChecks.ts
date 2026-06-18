export type RelationalOperation = "selection" | "projection" | "join" | "anti_join" | "aggregation" | "recursive_query";
export function queryLogicScore(entity: number, relationship: number, predicate: number, join: number, keys: number, missingness: number): number {
  return 100 * (0.18*entity + 0.18*relationship + 0.18*predicate + 0.18*join + 0.14*keys + 0.14*missingness);
}
