function automationRisk(stakes: number, opacity: number, delegation: number, irreversibility: number): number {
  return Math.max(0, Math.min(1, stakes * opacity * delegation * irreversibility));
}

console.log(automationRisk(0.95, 0.85, 0.90, 0.80).toFixed(6));
