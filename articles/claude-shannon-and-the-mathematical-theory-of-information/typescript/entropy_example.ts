function entropy(probs: number[]): number {
  return -probs
    .filter((p) => p > 0)
    .map((p) => p * Math.log2(p))
    .reduce((a, b) => a + b, 0);
}

console.log(`entropy_bits=${entropy([0.5, 0.5]).toFixed(9)}`);
