export function factorial(n: number): number {
  if (n < 0) throw new Error("factorial requires n >= 0");
  return n === 0 ? 1 : n * factorial(n - 1);
}
export function iterativeSum(values: number[]): number {
  return values.reduce((acc, value) => acc + value, 0);
}
