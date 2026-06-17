from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class DecompositionCase:
    case_name: str
    whole_problem: str
    decomposition_strategy: str
    subproblem_clarity: float
    boundary_definition: float
    input_output_clarity: float
    sequencing_quality: float
    dependency_visibility: float
    testability: float
    traceability: float
    recomposition_quality: float
    governance_readiness: float
    risk_awareness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def load_cases(path: Path) -> list[DecompositionCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            DecompositionCase(
                case_name=row["case_name"],
                whole_problem=row["whole_problem"],
                decomposition_strategy=row["decomposition_strategy"],
                subproblem_clarity=float(row["subproblem_clarity"]),
                boundary_definition=float(row["boundary_definition"]),
                input_output_clarity=float(row["input_output_clarity"]),
                sequencing_quality=float(row["sequencing_quality"]),
                dependency_visibility=float(row["dependency_visibility"]),
                testability=float(row["testability"]),
                traceability=float(row["traceability"]),
                recomposition_quality=float(row["recomposition_quality"]),
                governance_readiness=float(row["governance_readiness"]),
                risk_awareness=float(row["risk_awareness"]),
            )
            for row in reader
        ]


def decomposition_score(case: DecompositionCase) -> float:
    return clamp(
        100.0 * (
            0.12 * case.subproblem_clarity
            + 0.10 * case.boundary_definition
            + 0.10 * case.input_output_clarity
            + 0.10 * case.sequencing_quality
            + 0.10 * case.dependency_visibility
            + 0.12 * case.testability
            + 0.10 * case.traceability
            + 0.10 * case.recomposition_quality
            + 0.08 * case.governance_readiness
            + 0.08 * case.risk_awareness
        )
    )


def decomposition_risk(case: DecompositionCase) -> float:
    weak_points = [
        1.0 - case.boundary_definition,
        1.0 - case.dependency_visibility,
        1.0 - case.traceability,
        1.0 - case.recomposition_quality,
        1.0 - case.governance_readiness,
        1.0 - case.risk_awareness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 80 and risk <= 25:
        return "strong decomposition with clear stepwise reasoning"
    if score >= 65 and risk <= 40:
        return "usable decomposition with review needs"
    if risk >= 55:
        return "high decomposition risk; relationships and recomposition need review"
    return "partial decomposition; boundaries, dependencies, or governance need strengthening"


def evaluate_cases(cases: list[DecompositionCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        score = decomposition_score(case)
        risk = decomposition_risk(case)
        rows.append({
            **asdict(case),
            "decomposition_score": round(score, 3),
            "decomposition_risk": round(risk, 3),
            "diagnostic": diagnose(score, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_decomposition_score": round(mean(float(row["decomposition_score"]) for row in rows), 3),
        "average_decomposition_risk": round(mean(float(row["decomposition_risk"]) for row in rows), 3),
        "highest_score_case": max(rows, key=lambda row: float(row["decomposition_score"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["decomposition_risk"]))["case_name"],
        "interpretation": "Decomposition quality depends on clear subproblems, boundaries, inputs, outputs, sequencing, dependencies, tests, traceability, recomposition, governance, and risk awareness."
    }


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def run_workflow(article_root: Path) -> None:
    cases = load_cases(article_root / "data" / "synthetic_decomposition_cases.csv")
    rows = evaluate_cases(cases)
    summary = summarize(rows)

    write_csv(article_root / "outputs" / "tables" / "decomposition_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "decomposition_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "decomposition_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "decomposition_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
