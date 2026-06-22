const scores = [0.72, 0.68, 0.64, 0.58, 0.52, 0.66];
const capacity = scores.reduce((a, b) => a + b, 0) / scores.length;
console.log(`accountability_capacity_score=${capacity.toFixed(4)}`);
