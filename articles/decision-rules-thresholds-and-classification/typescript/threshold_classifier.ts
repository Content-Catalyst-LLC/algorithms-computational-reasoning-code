function classify(score: number, threshold: number): number {
  return score >= threshold ? 1 : 0;
}

console.log(classify(0.72, 0.50));
