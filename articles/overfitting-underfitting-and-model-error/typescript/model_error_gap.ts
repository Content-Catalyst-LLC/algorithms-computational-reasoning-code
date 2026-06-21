const trainError = 0.04;
const testError = 0.09;
console.log(`generalization_gap=${(testError - trainError).toFixed(4)}`);
