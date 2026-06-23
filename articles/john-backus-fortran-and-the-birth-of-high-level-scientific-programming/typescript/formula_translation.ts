function formula(x: number, a: number, b: number, c: number): number {
  return a * x * x + b * x + c;
}

for (const x of [-2, -1, 0, 1, 2, 3]) {
  console.log(`x=${x}, y=${formula(x, 2, -3, 1).toFixed(6)}`);
}
