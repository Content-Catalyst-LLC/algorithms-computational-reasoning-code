export type ConstraintType = "hard" | "soft" | "equality" | "inequality" | "compatibility";
export type Feasibility = "feasible" | "infeasible" | "unsatisfiable";
export function violationCount(assign: Record<string,string>, constraints: Array<[string,string]>): number {
  return constraints.filter(([left,right]) => assign[left] === assign[right]).length;
}
