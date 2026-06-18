export function mergeSort(values: number[]): number[] {
  if (values.length <= 1) return [...values];
  const mid = Math.floor(values.length / 2);
  return [...mergeSort(values.slice(0, mid)), ...mergeSort(values.slice(mid))].sort((a, b) => a - b);
}
export function binarySearch(values: number[], target: number): number {
  let lo = 0, hi = values.length - 1;
  while (lo <= hi) {
    const mid = Math.floor((lo + hi) / 2);
    if (values[mid] === target) return mid;
    if (values[mid] < target) lo = mid + 1; else hi = mid - 1;
  }
  return -1;
}
