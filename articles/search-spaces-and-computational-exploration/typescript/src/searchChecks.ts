export type SearchStrategy = "breadth_first" | "depth_first" | "uniform_cost" | "best_first" | "heuristic" | "local_search";
export function branchingStateCount(branchingFactor: number, depth: number): number { let total = 0; for (let i = 0; i <= depth; i++) total += branchingFactor ** i; return total; }
export function pathCost(edgeCosts: number[]): number { return edgeCosts.reduce((a, b) => a + b, 0); }
export function heuristicScore(knownCost: number, estimatedRemainingCost: number): number { return knownCost + estimatedRemainingCost; }
export function ratio(numerator: number, denominator: number): number { return denominator === 0 ? 0 : numerator / denominator; }
