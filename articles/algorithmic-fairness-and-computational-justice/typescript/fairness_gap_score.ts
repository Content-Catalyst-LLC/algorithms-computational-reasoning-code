const rates = [0.42, 0.31, 0.36];
const selectionGap = Math.max(...rates) - Math.min(...rates);
console.log(`selection_gap=${selectionGap.toFixed(4)}`);
