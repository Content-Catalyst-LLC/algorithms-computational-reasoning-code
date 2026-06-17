export type CaseRecord = { case_id: string; status: "draft" | "review" | "approved" | "rejected" | "archived"; score: number };
export function validateRecord(record: Partial<CaseRecord>): boolean {
  return typeof record.case_id === "string" && typeof record.score === "number" && typeof record.status === "string";
}
