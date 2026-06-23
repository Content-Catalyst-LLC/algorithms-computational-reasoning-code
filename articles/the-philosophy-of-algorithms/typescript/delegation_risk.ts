function delegationRisk(a: number, b: number, c: number): number { return Math.max(0, Math.min(1, a*b*c)); }
console.log(delegationRisk(0.95, 0.95, 0.80).toFixed(6));
