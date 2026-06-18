export function approximationRatioMinimization(algorithmValue: number, boundValue: number): number {
  return algorithmValue / boundValue;
}
export function relativeGapMinimization(algorithmValue: number, boundValue: number): number {
  return (algorithmValue - boundValue) / boundValue;
}
