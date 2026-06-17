from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class TreeStructureCase:
    case_name: str
    problem_context: str
    tree_structure_choice: str
    hierarchy_fit: float
    recursive_clarity: float
    invariant_documentation: float
    traversal_support: float
    balance_awareness: float
    path_interpretability: float
    relationship_loss_control: float
    complexity_awareness: float
    representation_risk_documentation: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def tree_structure_quality(case: TreeStructureCase) -> float:
    return clamp(100.0 * (
        0.12 * case.hierarchy_fit
        + 0.12 * case.recursive_clarity
        + 0.10 * case.invariant_documentation
        + 0.10 * case.traversal_support
        + 0.08 * case.balance_awareness
        + 0.10 * case.path_interpretability
        + 0.10 * case.relationship_loss_control
        + 0.08 * case.complexity_awareness
        + 0.10 * case.representation_risk_documentation
        + 0.10 * case.governance_readiness
    ))


def false_hierarchy_risk(case: TreeStructureCase) -> float:
    weak_points = [
        1.0 - case.hierarchy_fit,
        1.0 - case.recursive_clarity,
        1.0 - case.invariant_documentation,
        1.0 - case.traversal_support,
        1.0 - case.path_interpretability,
        1.0 - case.relationship_loss_control,
        1.0 - case.representation_risk_documentation,
        1.0 - case.governance_readiness,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 82 and risk <= 22:
        return "strong tree-structure posture with clear hierarchy, recursion, invariants, traversal, and governance"
    if quality >= 68 and risk <= 38:
        return "usable tree-structure posture with review needs"
    if risk >= 55:
        return "high false-hierarchy risk; tree shape may hide relationships or force rigid classification"
    return "partial tree-structure posture; strengthen hierarchy fit, invariants, traversal, or governance"


def load_cases(path: Path) -> list[TreeStructureCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            TreeStructureCase(
                row["case_name"],
                row["problem_context"],
                row["tree_structure_choice"],
                float(row["hierarchy_fit"]),
                float(row["recursive_clarity"]),
                float(row["invariant_documentation"]),
                float(row["traversal_support"]),
                float(row["balance_awareness"]),
                float(row["path_interpretability"]),
                float(row["relationship_loss_control"]),
                float(row["complexity_awareness"]),
                float(row["representation_risk_documentation"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[TreeStructureCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = tree_structure_quality(case)
        risk = false_hierarchy_risk(case)
        rows.append({
            **asdict(case),
            "tree_structure_quality": round(quality, 3),
            "false_hierarchy_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_tree_structure_quality": round(mean(float(row["tree_structure_quality"]) for row in rows), 3),
        "average_false_hierarchy_risk": round(mean(float(row["false_hierarchy_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["tree_structure_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["false_hierarchy_risk"]))["case_name"],
        "interpretation": "Tree quality depends on hierarchy fit, recursive clarity, invariants, traversal, balance, path interpretability, relationship-loss control, complexity, risk documentation, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_tree_structure_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "tree_structure_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "tree_structure_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "tree_structure_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "tree_structure_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
