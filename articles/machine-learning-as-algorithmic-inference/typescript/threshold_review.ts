const tp = 80, fp = 25, tn = 140, fnCount = 35;
const total = tp + fp + tn + fnCount;
console.log(`accuracy=${((tp + tn) / total).toFixed(6)}`);
console.log(`precision=${(tp / (tp + fp)).toFixed(6)}`);
console.log(`recall=${(tp / (tp + fnCount)).toFixed(6)}`);
