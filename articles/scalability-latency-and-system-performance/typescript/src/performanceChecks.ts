export type PerformanceMetric = "latency" | "throughput" | "utilization" | "tail_latency" | "error_rate" | "unit_cost";
export function responseTime(networkMs: number, queueMs: number, computeMs: number, storageMs: number, coordinationMs: number): number {
  return networkMs + queueMs + computeMs + storageMs + coordinationMs;
}
export function throughput(completedWork: number, timeSeconds: number): number { return timeSeconds === 0 ? 0 : completedWork / timeSeconds; }
export function utilization(arrivalRate: number, serviceRate: number): number { return serviceRate === 0 ? 0 : arrivalRate / serviceRate; }
export function littleLaw(arrivalRate: number, averageTimeInSystem: number): number { return arrivalRate * averageTimeInSystem; }
