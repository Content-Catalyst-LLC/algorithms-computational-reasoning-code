function feasible(x: number, y: number): boolean {
  return 2 * x + y <= 8 && x + 2 * y <= 8 && x >= 0 && y >= 0;
}

function objective(x: number, y: number): number {
  return 3 * x + 4 * y;
}

let best = { x: 0, y: 0, objective: -Infinity };
for (let x = 0; x < 10; x++) {
  for (let y = 0; y < 10; y++) {
    const value = objective(x, y);
    if (feasible(x, y) && value > best.objective) {
      best = { x, y, objective: value };
    }
  }
}
console.log(best);
