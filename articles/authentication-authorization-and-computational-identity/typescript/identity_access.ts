const weights: number[] = [0.10,0.11,0.11,0.09,0.09,0.10,0.09,0.09,0.08,0.06,0.06,0.02];
const score = weights.reduce((total, weight) => total + 0.75 * weight, 0) * 100;
console.log(score.toFixed(3));
