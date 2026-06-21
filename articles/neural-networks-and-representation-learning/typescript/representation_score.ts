function sigmoid(x: number): number {
  return 1 / (1 + Math.exp(-x));
}
function representationScore(x1: number, x2: number, x3: number, bias = 0): number {
  return sigmoid(0.9 * x1 - 0.7 * x2 + 0.35 * x3 + bias);
}
console.log(representationScore(0.5, -0.2, 0.7).toFixed(6));
