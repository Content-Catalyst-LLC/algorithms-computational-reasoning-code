export type EdgeLayer = "device" | "gateway" | "local_edge_server" | "network_edge" | "cloud_core";
export function edgeResponseTime(senseMs: number, filterMs: number, computeMs: number, actuateMs: number): number {
  return senseMs + filterMs + computeMs + actuateMs;
}
export function cloudResponseTime(senseMs: number, uplinkMs: number, cloudComputeMs: number, downlinkMs: number, actuateMs: number): number {
  return senseMs + uplinkMs + cloudComputeMs + downlinkMs + actuateMs;
}
export function batteryLifeHours(batteryWh: number, averagePowerW: number): number { return averagePowerW === 0 ? 0 : batteryWh / averagePowerW; }
export function localAction(signal: number, threshold: number): "alert" | "monitor" { return signal >= threshold ? "alert" : "monitor"; }
