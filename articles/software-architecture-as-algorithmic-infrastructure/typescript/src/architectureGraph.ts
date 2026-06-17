export type Component = "api" | "domain" | "interfaces" | "worker" | "reporting" | "storage";
export type DependencyEdge = { source: Component; target: Component; relationship: string };
export const edges: DependencyEdge[] = [
  { source: "api", target: "domain", relationship: "uses" },
  { source: "domain", target: "interfaces", relationship: "depends_on_abstraction" },
  { source: "worker", target: "domain", relationship: "uses" },
  { source: "reporting", target: "storage", relationship: "reads" }
];
