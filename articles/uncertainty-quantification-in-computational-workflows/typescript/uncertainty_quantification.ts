function clamp(value: number, low: number, high: number): number {
  return Math.max(low, Math.min(high, value));
}

function riskModel(demand: number, capacity: number, failureRate: number, adaptationRate: number, noise = 0): number {
  return clamp(0.42 + 0.38 * demand - 0.31 * capacity + 0.27 * failureRate - 0.18 * adaptationRate + noise, 0, 1);
}

console.log(JSON.stringify({ risk_score: riskModel(0.55, 0.50, 0.22, 0.30) }, null, 2));
