const scores = [0.62, 0.6875, 0.58, 0.50, 0.56, 0.52];
const quality = scores.reduce((a, b) => a + b, 0) / scores.length;
console.log(`documentation_quality_score=${quality.toFixed(4)}`);
