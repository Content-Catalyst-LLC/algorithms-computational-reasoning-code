export type SequenceShape = "array" | "list" | "stack" | "queue" | "deque" | "circular_buffer";
export type SequenceStructureCase = { name: string; shape: SequenceShape; sequenceStructureQuality: number };
export const cases: SequenceStructureCase[] = [
  { name: "Numerical time series array", shape: "array", sequenceStructureQuality: 83.20 },
  { name: "Undo action stack", shape: "stack", sequenceStructureQuality: 83.80 },
  { name: "Case review queue", shape: "queue", sequenceStructureQuality: 85.04 },
  { name: "Streaming circular buffer", shape: "circular_buffer", sequenceStructureQuality: 83.80 }
];
