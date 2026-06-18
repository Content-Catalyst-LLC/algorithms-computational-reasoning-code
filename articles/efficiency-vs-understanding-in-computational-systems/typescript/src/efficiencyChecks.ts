export type EfficiencyDimension = "time" | "space" | "cost" | "energy";
export type UnderstandingDimension = "readability" | "debuggability" | "explainability" | "auditability" | "maintainability";
export function efficiencyGain(baselineCost: number, optimizedCost: number): number {
  return (baselineCost - optimizedCost) / baselineCost;
}
export function understandingComposite(scores: number[]): number {
  return scores.reduce((sum, x) => sum + x, 0) / scores.length;
}
