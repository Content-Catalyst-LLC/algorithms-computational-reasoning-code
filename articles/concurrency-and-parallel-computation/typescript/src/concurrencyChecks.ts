export type ConcurrencyModel = "threads" | "processes" | "async_tasks" | "actors" | "queues" | "distributed_workers";
export type ParallelPattern = "data_parallel" | "task_parallel" | "pipeline_parallel" | "map_reduce" | "vectorized" | "gpu_parallel";
export function speedup(sequentialTime: number, parallelTime: number): number { return parallelTime === 0 ? 0 : sequentialTime / parallelTime; }
export function amdahl(processors: number, sequentialFraction: number): number { return processors === 0 ? 0 : 1 / (sequentialFraction + ((1 - sequentialFraction) / processors)); }
export function efficiency(processors: number, observedSpeedup: number): number { return processors === 0 ? 0 : observedSpeedup / processors; }
