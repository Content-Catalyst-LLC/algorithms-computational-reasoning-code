const scores = [0.94, 0.78, 0.56, 0.70];
const pressure = scores.reduce((a, b) => a + b, 0) / scores.length;
console.log(`non_use_pressure_score=${pressure.toFixed(4)}`);
