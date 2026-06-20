from __future__ import annotations

from dataclasses import asdict, dataclass
from itertools import product
from pathlib import Path
from statistics import mean
import csv
import json

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class OptimizationCase:
    case_name: str
    decision_context: str
    optimization_goal: str
    variable_clarity: float
    objective_documentation: float
    constraint_documentation: float
    data_provenance: float
    feasibility_logic: float
    sensitivity_review: float
    robustness_review: float
    fairness_review: float
    traceability: float
    governance_review: float
    communication_clarity: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def optimization_governance_score(case: OptimizationCase) -> float:
    return clamp(
        100.0 * (
            0.10 * case.variable_clarity
            + 0.11 * case.objective_documentation
            + 0.11 * case.constraint_documentation
            + 0.09 * case.data_provenance
            + 0.10 * case.feasibility_logic
            + 0.10 * case.sensitivity_review
            + 0.09 * case.robustness_review
            + 0.09 * case.fairness_review
            + 0.09 * case.traceability
            + 0.08 * case.governance_review
            + 0.04 * case.communication_clarity
        )
    )


def optimization_governance_risk(case: OptimizationCase) -> float:
    weak_points = [
        1.0 - case.variable_clarity,
        1.0 - case.objective_documentation,
        1.0 - case.constraint_documentation,
        1.0 - case.data_provenance,
        1.0 - case.feasibility_logic,
        1.0 - case.sensitivity_review,
        1.0 - case.robustness_review,
        1.0 - case.fairness_review,
        1.0 - case.traceability,
        1.0 - case.governance_review,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong optimization-governance discipline"
    if score >= 70 and risk <= 35:
        return "usable optimization model with review needs"
    if risk >= 55:
        return "high risk; objectives, constraints, data provenance, feasibility, robustness, fairness, or governance may be underdefined"
    return "partial discipline; strengthen objectives, constraints, sensitivity, robustness, traceability, fairness, and governance"


def feasible_plan(x: int, y: int, labor_limit: int = 8, material_limit: int = 8) -> bool:
    labor = 2 * x + 1 * y
    material = 1 * x + 2 * y
    return labor <= labor_limit and material <= material_limit and x >= 0 and y >= 0


def objective_value(x: int, y: int) -> float:
    return 3 * x + 4 * y


def brute_force_linear_program(labor_limit: int = 8, material_limit: int = 8) -> dict[str, object]:
    candidates: list[dict[str, object]] = []

    for x, y in product(range(0, 10), range(0, 10)):
        if feasible_plan(x, y, labor_limit, material_limit):
            candidates.append({
                "x": x,
                "y": y,
                "objective_value": objective_value(x, y),
                "labor_used": 2 * x + y,
                "material_used": x + 2 * y,
                "labor_slack": labor_limit - (2 * x + y),
                "material_slack": material_limit - (x + 2 * y),
            })

    best = max(candidates, key=lambda row: float(row["objective_value"]))
    return {
        "candidate_count": len(candidates),
        "best_solution": best,
        "interpretation": "Small integer grid enumeration used only as a transparent teaching calculator for a two-variable linear program.",
    }


def convex_quadratic_example() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for x in [-3, -2, -1, 0, 1, 2, 3, 4, 5]:
        value = (x - 2) ** 2 + 1
        rows.append({"x": x, "convex_objective_value": value, "is_global_minimum": x == 2})
    return rows


def build_cases() -> list[OptimizationCase]:
    return [
        OptimizationCase("Production planning model", "Choose production quantities under labor, material, machine, and demand constraints.", "maximize feasible profit while documenting constraints and sensitivity", 0.88, 0.86, 0.84, 0.78, 0.86, 0.80, 0.74, 0.62, 0.82, 0.76, 0.80),
        OptimizationCase("Public resource allocation", "Allocate limited public-service resources across regions and needs.", "balance service coverage, cost, capacity, equity, and accountability", 0.82, 0.78, 0.84, 0.72, 0.80, 0.76, 0.78, 0.86, 0.80, 0.84, 0.78),
        OptimizationCase("Portfolio optimization", "Choose asset weights under expected return, risk, liquidity, and exposure constraints.", "optimize risk-return trade-offs while testing sensitivity to uncertain estimates", 0.80, 0.76, 0.78, 0.68, 0.82, 0.84, 0.82, 0.50, 0.76, 0.72, 0.74),
        OptimizationCase("Opaque cost minimization", "Minimize operational cost using undocumented constraints and incomplete impact measures.", "reduce total reported cost", 0.42, 0.30, 0.28, 0.24, 0.36, 0.20, 0.18, 0.16, 0.24, 0.22, 0.34),
    ]


def run_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in build_cases():
        score = optimization_governance_score(case)
        risk = optimization_governance_risk(case)
        rows.append({**asdict(case), "optimization_governance_score": round(score, 3), "optimization_governance_risk": round(risk, 3), "diagnostic": diagnose(score, risk)})
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_optimization_governance_score": round(mean(float(row["optimization_governance_score"]) for row in rows), 3),
        "average_optimization_governance_risk": round(mean(float(row["optimization_governance_risk"]) for row in rows), 3),
        "highest_score_case": max(rows, key=lambda row: float(row["optimization_governance_score"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["optimization_governance_risk"]))["case_name"],
        "interpretation": "Optimization governance depends on variable clarity, objective documentation, constraint documentation, data provenance, feasibility logic, sensitivity review, robustness review, fairness review, traceability, governance review, and communication clarity.",
    }


def main() -> None:
    audit_rows = run_audit()
    summary = summarize(audit_rows)
    lp_example = brute_force_linear_program()
    convex_rows = convex_quadratic_example()

    write_csv(TABLES / "linear_programming_convex_optimization_audit.csv", audit_rows)
    write_csv(TABLES / "linear_programming_convex_optimization_audit_summary.csv", [summary])
    write_csv(TABLES / "linear_programming_example_best_solution.csv", [lp_example["best_solution"]])
    write_csv(TABLES / "convex_quadratic_example.csv", convex_rows)

    write_json(JSON_DIR / "linear_programming_convex_optimization_audit.json", audit_rows)
    write_json(JSON_DIR / "linear_programming_convex_optimization_audit_summary.json", summary)
    write_json(JSON_DIR / "linear_programming_example.json", lp_example)
    write_json(JSON_DIR / "convex_quadratic_example.json", convex_rows)

    print("Linear programming and convex optimization audit complete.")
    print(TABLES / "linear_programming_convex_optimization_audit.csv")


if __name__ == "__main__":
    main()
