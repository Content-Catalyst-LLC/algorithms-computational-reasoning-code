const total = 1200;
const weights = [2, 1, 1];
const sum = weights.reduce((a, b) => a + b, 0);
weights.forEach((w, i) => console.log(`share_${i + 1}=${(total * w / sum).toFixed(4)}`));
