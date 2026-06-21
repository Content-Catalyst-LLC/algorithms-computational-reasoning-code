const weights: number[] = [0.08,0.10,0.10,0.10,0.08,0.08,0.08,0.08,0.08,0.08,0.06,0.05,0.03];
const score = weights.reduce((total, weight) => total + 0.65 * weight, 0) * 100;
console.log(score.toFixed(3));
