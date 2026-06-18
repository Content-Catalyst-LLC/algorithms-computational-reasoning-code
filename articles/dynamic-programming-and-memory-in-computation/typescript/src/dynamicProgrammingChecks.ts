export function fibonacciMemo(n: number, memo = new Map<number, number>()): number {
  if (memo.has(n)) return memo.get(n)!;
  const value = n <= 1 ? n : fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo);
  memo.set(n, value);
  return value;
}
export function stateSpaceSize(dimensions: number[]): number {
  return dimensions.reduce((acc, value) => acc * value, 1);
}
