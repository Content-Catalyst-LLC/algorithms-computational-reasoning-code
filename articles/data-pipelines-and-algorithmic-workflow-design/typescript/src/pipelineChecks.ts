export type PipelineStage = "source" | "ingestion" | "validation" | "transformation" | "storage" | "delivery" | "monitoring";
export function freshness(days: number, decay = 0.025): number { return Math.exp(-decay * days); }
export function quality(validation: number, freshnessScore: number, completeness: number, lineage: number, monitoring: number): number {
  return 100 * (0.25*validation + 0.18*freshnessScore + 0.20*completeness + 0.22*lineage + 0.15*monitoring);
}
