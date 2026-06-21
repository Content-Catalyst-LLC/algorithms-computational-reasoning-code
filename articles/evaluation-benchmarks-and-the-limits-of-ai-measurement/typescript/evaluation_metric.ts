const tp = 42;
const tn = 38;
const fp = 7;
const fn = 13;
const accuracy = (tp + tn) / (tp + tn + fp + fn);
console.log(`accuracy=${accuracy.toFixed(4)}`);
