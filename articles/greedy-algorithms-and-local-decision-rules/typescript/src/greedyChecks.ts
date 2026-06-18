export type Interval = { id: string; start: number; finish: number };
export function intervalScheduling(intervals: Interval[]): Interval[] {
  const ordered = [...intervals].sort((a, b) => a.finish - b.finish);
  const selected: Interval[] = [];
  let currentFinish = Number.NEGATIVE_INFINITY;
  for (const interval of ordered) {
    if (interval.start >= currentFinish) {
      selected.push(interval);
      currentFinish = interval.finish;
    }
  }
  return selected;
}
export function highestPriority<T>(items: T[], score: (item: T) => number): T | undefined {
  return [...items].sort((a, b) => score(b) - score(a))[0];
}
