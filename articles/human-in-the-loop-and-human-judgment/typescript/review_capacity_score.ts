const scores = [0.56, 0.62, 0.58, 0.60, 0.48];
const capacity = scores.reduce((a, b) => a + b, 0) / scores.length;
console.log(`review_capacity_score=${capacity.toFixed(4)}`);
