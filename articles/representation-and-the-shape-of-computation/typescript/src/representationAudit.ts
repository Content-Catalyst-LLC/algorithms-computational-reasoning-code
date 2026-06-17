export type RepresentationShape = "list" | "table" | "tree" | "graph" | "vector" | "state";
export type RepresentationCase = { name: string; shape: RepresentationShape; representationQuality: number };
export const cases: RepresentationCase[] = [
  { name: "Route planning graph", shape: "graph", representationQuality: 80.52 },
  { name: "Institutional records table", shape: "table", representationQuality: 81.20 },
  { name: "Document embedding index", shape: "vector", representationQuality: 76.08 },
  { name: "Simulation state model", shape: "state", representationQuality: 82.20 }
];
