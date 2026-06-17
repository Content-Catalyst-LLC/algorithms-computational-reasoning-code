export type GraphKind = "route_graph" | "dependency_graph" | "knowledge_graph" | "workflow_network" | "flow_network";
export type GraphRelationshipCase = { name: string; kind: GraphKind; graphReasoningQuality: number };
export const cases: GraphRelationshipCase[] = [
  { name: "Transportation route graph", kind: "route_graph", graphReasoningQuality: 86.28 },
  { name: "Software dependency graph", kind: "dependency_graph", graphReasoningQuality: 85.18 },
  { name: "Knowledge graph", kind: "knowledge_graph", graphReasoningQuality: 82.12 },
  { name: "Institutional workflow network", kind: "workflow_network", graphReasoningQuality: 83.16 }
];
