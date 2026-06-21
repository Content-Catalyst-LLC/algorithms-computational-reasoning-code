function f(x: number): number { return Math.sin(x); }
function centralDifference(x: number, h: number): number { return (f(x + h) - f(x - h)) / (2 * h); }
function trapezoid(n: number): number {
  const a = 0, b = Math.PI, h = (b - a) / n;
  let total = 0.5 * (f(a) + f(b));
  for (let i = 1; i < n; i += 1) total += f(a + i * h);
  return h * total;
}
console.log({ centralDifference: centralDifference(1.0, 1e-4), trapezoidIntegral: trapezoid(200) });
