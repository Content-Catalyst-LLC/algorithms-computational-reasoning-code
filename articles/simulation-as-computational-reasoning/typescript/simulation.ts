function step(x: number): number {
  return Math.max(0, x + 0.08 * x - 0.03 * x - 0.04 * x);
}

let stock = 100;
for (let t = 0; t <= 30; t += 1) {
  console.log(`time_step=${t},stock=${stock.toFixed(6)}`);
  stock = step(stock);
}
