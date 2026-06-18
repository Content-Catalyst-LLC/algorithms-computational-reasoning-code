export function amplificationFailureProbability(singleTrialFailure: number, trials: number): number {
  return singleTrialFailure ** trials;
}
export function sampleMean(values: number[]): number {
  return values.reduce((acc, value) => acc + value, 0) / values.length;
}
