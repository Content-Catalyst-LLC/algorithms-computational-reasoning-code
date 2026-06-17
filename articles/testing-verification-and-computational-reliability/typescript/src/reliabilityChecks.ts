export function scoreInRange(score: number): boolean {
  return score >= 0 && score <= 100;
}
export function nondecreasing(values: number[]): boolean {
  return values.every((value, index) => index === 0 || values[index - 1] <= value);
}
