function expectedNetValue(p: number, benefit: number, loss: number, cost: number): number {
  const bounded = Math.max(0, Math.min(1, p));
  return bounded * benefit - bounded * loss - cost;
}

console.log(expectedNetValue(0.42, 150, 80, 25).toFixed(6));
