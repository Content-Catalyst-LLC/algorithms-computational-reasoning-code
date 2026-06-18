export function linearSearch(values: number[], target: number): number {
  return values.findIndex((value) => value === target);
}
export function sorted(values: number[]): number[] {
  return [...values].sort((a, b) => a - b);
}
export function stableRank<T>(items: T[], score: (item: T) => number): T[] {
  return items.map((item, index) => ({ item, index })).sort((a, b) => score(b.item) - score(a.item) || a.index - b.index).map((row) => row.item);
}
