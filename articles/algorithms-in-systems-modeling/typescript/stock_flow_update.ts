const currentStock = 100.0;
const inflow = 12.0;
const outflow = 7.0;
const nextStock = currentStock + inflow - outflow;
console.log(`next_stock=${nextStock.toFixed(4)}`);
