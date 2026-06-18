export function binaryFitness(candidate: number[]): number {
  return candidate.reduce((acc, value) => acc + value, 0);
}
export function hammingDiversity(a: number[], b: number[]): number {
  return a.filter((value, index) => value !== b[index]).length / a.length;
}
