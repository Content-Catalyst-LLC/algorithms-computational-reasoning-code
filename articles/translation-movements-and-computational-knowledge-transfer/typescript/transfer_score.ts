const scores = [0.98, 0.90, 0.94, 0.88, 0.94, 0.90, 0.96, 0.84, 0.96];
const score = scores.reduce((a, b) => a + b, 0) / scores.length;
console.log(`transfer_score=${score.toFixed(6)}`);
