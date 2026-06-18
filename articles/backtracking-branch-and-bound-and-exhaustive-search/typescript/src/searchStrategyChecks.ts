export function searchSpaceGrowth(branchingFactor: number, depth: number): number {
  let total = 0;
  let power = 1;
  for (let level = 0; level <= depth; level += 1) {
    total += power;
    power *= branchingFactor;
  }
  return total;
}
export function exhaustiveSubsets<T>(items: T[]): T[][] {
  const result: T[][] = [[]];
  for (const item of items) {
    result.push(...result.map(existing => [...existing, item]));
  }
  return result;
}
