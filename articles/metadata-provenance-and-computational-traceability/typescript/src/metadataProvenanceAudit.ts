export type ProvenanceRelation = "used" | "was_generated_by" | "was_derived_from" | "was_attributed_to";
export type TraceEvent = { fromId: string; toId: string; relation: ProvenanceRelation; timestamp: string };
export const cases = [
  { name: "Research dataset repository", traceabilityQuality: 89.10 },
  { name: "AI model registry", traceabilityQuality: 87.00 },
  { name: "Institutional case workflow", traceabilityQuality: 87.08 },
  { name: "Knowledge library article system", traceabilityQuality: 83.68 }
];
