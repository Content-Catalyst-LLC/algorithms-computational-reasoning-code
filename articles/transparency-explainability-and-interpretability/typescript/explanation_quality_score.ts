const scores = [0.70, 0.74, 0.62, 0.58, 0.46];
const quality = scores.reduce((a, b) => a + b, 0) / scores.length;
console.log(`explanation_quality_score=${quality.toFixed(4)}`);
