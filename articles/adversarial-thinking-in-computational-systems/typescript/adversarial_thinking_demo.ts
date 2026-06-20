function readiness(threat: number, surface: number, monitoring: number, defense: number, incident: number, governance: number): number {
  return 100 * (0.18 * threat + 0.18 * surface + 0.18 * monitoring + 0.18 * defense + 0.14 * incident + 0.14 * governance);
}

console.log(`adversarial readiness=${readiness(0.86, 0.82, 0.88, 0.82, 0.80, 0.78).toFixed(3)}`);
