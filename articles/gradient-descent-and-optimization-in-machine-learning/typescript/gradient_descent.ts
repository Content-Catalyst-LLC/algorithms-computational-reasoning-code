type Point = { x: number; y: number };

const rows: Point[] = [
  { x: -2, y: -2.85 },
  { x: -1, y: -0.67 },
  { x: 0, y: 1.47 },
  { x: 1, y: 3.63 },
  { x: 2, y: 5.82 },
];

function mse(weight: number, bias: number): number {
  return rows.reduce((sum, row) => sum + Math.pow(row.y - (weight * row.x + bias), 2), 0) / rows.length;
}

let weight = 0;
let bias = 0;
const eta = 0.08;

for (let step = 0; step < 80; step += 1) {
  let gradW = 0;
  let gradB = 0;
  for (const row of rows) {
    const err = (weight * row.x + bias) - row.y;
    gradW += (2 / rows.length) * err * row.x;
    gradB += (2 / rows.length) * err;
  }
  weight -= eta * gradW;
  bias -= eta * gradB;
}

console.log({ weight, bias, loss: mse(weight, bias) });
