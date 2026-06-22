const scores = [0.60, 0.62, 0.58, 0.52, 0.46, 0.50];
const readiness = scores.reduce((a, b) => a + b, 0) / scores.length;
console.log(`governance_readiness_score=${readiness.toFixed(4)}`);
