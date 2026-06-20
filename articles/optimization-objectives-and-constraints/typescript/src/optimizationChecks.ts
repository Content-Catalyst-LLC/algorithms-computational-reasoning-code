export type ObjectiveDirection = "minimize" | "maximize";
export type ConstraintType = "hard" | "soft" | "penalty";
export function linearObjective(coefficients: number[], decisionValues: number[]): number {
  return coefficients.reduce((total, c, i) => total + c * decisionValues[i], 0);
}
export function constraintMargin(limit: number, observedValue: number): number { return limit - observedValue; }
export function penaltyObjective(baseObjective: number, penalty: number, penaltyWeight: number): number {
  return baseObjective + penaltyWeight * penalty;
}
export function normalizedTradeoffScore(costScore: number, qualityScore: number, riskScore: number): number {
  return 0.35 * (1 - costScore) + 0.40 * qualityScore + 0.25 * (1 - riskScore);
}
