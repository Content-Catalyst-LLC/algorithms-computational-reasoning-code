export function nondecreasing(values: number[]): boolean {
  return values.every((value, index) => index === 0 || values[index - 1] <= value);
}
export function validateNonnegativeWeights(edges: Array<[string, string, number]>): boolean {
  return edges.every(([, , weight]) => weight >= 0);
}
