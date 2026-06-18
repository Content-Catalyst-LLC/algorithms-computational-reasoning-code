export type MissingnessReason = "unknown" | "not_applicable" | "not_collected" | "withheld" | "pending" | "invalid" | "redacted" | "structural_zero";
export function missingnessRate(missing: number, total: number): number { return total === 0 ? 0 : missing / total; }
export function quality(completeness: number, validity: number, timeliness: number, provenance: number, validation: number): number {
  return 100 * (0.25*completeness + 0.20*validity + 0.15*timeliness + 0.22*provenance + 0.18*validation);
}
