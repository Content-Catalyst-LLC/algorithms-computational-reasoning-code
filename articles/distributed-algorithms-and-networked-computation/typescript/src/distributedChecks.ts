export type FailureModel = "crash" | "delay" | "partition" | "overload" | "byzantine";
export type ConsistencyModel = "strong" | "eventual" | "causal" | "snapshot" | "linearizable";
export function quorumSize(nodeCount: number): number { return Math.floor(nodeCount / 2) + 1; }
export function crashFaultTolerance(nodeCount: number): number { return Math.floor((nodeCount - 1) / 2); }
export function availabilityWithReplication(replicaCount: number, nodeAvailability: number): number {
  return 1 - Math.pow(1 - nodeAvailability, replicaCount);
}
export function distributedLatency(computeMs: number, networkMs: number, queueMs: number): number {
  return computeMs + networkMs + queueMs;
}
