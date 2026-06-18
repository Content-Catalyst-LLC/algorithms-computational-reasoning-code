export type CloudLayer = "compute" | "storage" | "network" | "data" | "observability" | "security" | "governance";
export function totalLatency(computeMs: number, storageMs: number, networkMs: number, queueMs: number, coordinationMs: number): number {
  return computeMs + storageMs + networkMs + queueMs + coordinationMs;
}
export function nominalCapacity(nodes: number, capacityPerNode: number): number { return nodes * capacityPerNode; }
export function unitCost(compute: number, storage: number, network: number, managed: number, observability: number, completed: number): number {
  return completed === 0 ? 0 : (compute + storage + network + managed + observability) / completed;
}
