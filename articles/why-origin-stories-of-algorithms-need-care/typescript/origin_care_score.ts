const scores = [0.96, 0.98, 0.96, 0.88, 0.98, 0.90, 0.90, 0.96, 0.98, 0.98];
const score = scores.reduce((a, b) => a + b, 0) / scores.length;
console.log(`origin_care_score=${score.toFixed(6)}`);
