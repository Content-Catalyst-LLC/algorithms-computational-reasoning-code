export type StructureShape = "array" | "list" | "stack" | "queue" | "set" | "map" | "tree" | "heap" | "graph" | "table" | "vector";
export type DataStructureCase = { name: string; shape: StructureShape; structureReasoningQuality: number };
export const cases: DataStructureCase[] = [
  { name: "Task scheduling priority queue", shape: "heap", structureReasoningQuality: 82.32 },
  { name: "Relationship analysis graph", shape: "graph", structureReasoningQuality: 82.36 },
  { name: "Case records table", shape: "table", structureReasoningQuality: 82.60 },
  { name: "Document similarity vector index", shape: "vector", structureReasoningQuality: 79.80 }
];
