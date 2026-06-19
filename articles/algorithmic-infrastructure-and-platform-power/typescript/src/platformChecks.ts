export type PlatformLayer = "search" | "cloud" | "marketplace" | "identity" | "payments" | "ai_platform" | "analytics";
export function dependencyScore(access: number, visibility: number, cost: number, switching: number, evidence: number): number {
  return 100 * (0.22*access + 0.22*visibility + 0.18*cost + 0.24*switching + 0.14*evidence);
}
export function switchingCost(migration: number, rebuild: number, training: number, downtime: number, lostNetwork: number): number {
  return migration + rebuild + training + downtime + lostNetwork;
}
export function ratio(numerator: number, denominator: number): number { return denominator === 0 ? 0 : numerator / denominator; }
