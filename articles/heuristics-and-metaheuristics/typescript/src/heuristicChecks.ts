export function relativeImprovementMinimize(baseline: number, heuristic: number): number {
  return (baseline - heuristic) / baseline;
}
export function simulatedAnnealingAcceptance(deltaCost: number, temperature: number): number {
  return Math.exp(-deltaCost / Math.max(temperature, 1e-9));
}
