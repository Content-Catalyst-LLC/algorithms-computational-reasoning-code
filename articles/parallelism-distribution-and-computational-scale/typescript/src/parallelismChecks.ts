export type ParallelismType = "task" | "data" | "pipeline" | "model" | "gpu";
export function speedup(serialFraction: number, processors: number): number {
  return 1 / (serialFraction + ((1 - serialFraction) / processors));
}
export function efficiency(serialFraction: number, processors: number): number {
  return speedup(serialFraction, processors) / processors;
}
