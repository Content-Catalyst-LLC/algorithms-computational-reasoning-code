function clamp(x: number, lo = 0, hi = 1): number {
  return Math.max(lo, Math.min(hi, x));
}
function model(demand: number, capacity: number, failure: number, adaptation: number): number {
  return clamp(0.5 + 0.30 * demand + 0.25 * failure - 0.20 * capacity - 0.15 * adaptation);
}
console.log(`baseline_risk=${model(0.45, 0.35, 0.25, 0.30).toFixed(6)}`);
