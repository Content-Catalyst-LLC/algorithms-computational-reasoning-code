function thresholdUnit(inputs: number[], weights: number[], threshold: number): number {
  const total = inputs.reduce((sum, x, i) => sum + x * weights[i], 0);
  return total >= threshold ? 1 : 0;
}

console.log(thresholdUnit([1, 1], [1, 1], 2));
