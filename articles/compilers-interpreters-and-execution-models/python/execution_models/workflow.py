from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class ExecutionModelCase:
    case_name: str
    problem_context: str
    execution_model_choice: str
    translation_clarity: float
    semantic_checking: float
    optimization_traceability: float
    runtime_visibility: float
    diagnostics_quality: float
    portability: float
    reproducibility: float
    security_boundaries: float
    performance_fit: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def execution_quality(case: ExecutionModelCase) -> float:
    return clamp(100.0 * (
        0.10 * case.translation_clarity
        + 0.10 * case.semantic_checking
        + 0.10 * case.optimization_traceability
        + 0.10 * case.runtime_visibility
        + 0.10 * case.diagnostics_quality
        + 0.10 * case.portability
        + 0.12 * case.reproducibility
        + 0.12 * case.security_boundaries
        + 0.08 * case.performance_fit
        + 0.08 * case.governance_readiness
    ))


def execution_risk(case: ExecutionModelCase) -> float:
    return clamp(100.0 * mean([
        1.0 - case.translation_clarity,
        1.0 - case.semantic_checking,
        1.0 - case.optimization_traceability,
        1.0 - case.runtime_visibility,
        1.0 - case.diagnostics_quality,
        1.0 - case.reproducibility,
        1.0 - case.security_boundaries,
        1.0 - case.governance_readiness,
    ]))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 84 and risk <= 20:
        return "strong execution model with clear translation, checks, diagnostics, reproducibility, security, and governance"
    if quality >= 70 and risk <= 35:
        return "usable execution model with review needs"
    if risk >= 55:
        return "high execution risk; translation, diagnostics, reproducibility, runtime visibility, or trust boundaries may be weak"
    return "partial execution discipline; strengthen build traceability, runtime visibility, diagnostics, or governance"


def load_cases(path: Path) -> list[ExecutionModelCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            ExecutionModelCase(
                row["case_name"],
                row["problem_context"],
                row["execution_model_choice"],
                float(row["translation_clarity"]),
                float(row["semantic_checking"]),
                float(row["optimization_traceability"]),
                float(row["runtime_visibility"]),
                float(row["diagnostics_quality"]),
                float(row["portability"]),
                float(row["reproducibility"]),
                float(row["security_boundaries"]),
                float(row["performance_fit"]),
                float(row["governance_readiness"]),
            )
            for row in reader
        ]


def evaluate_cases(cases: list[ExecutionModelCase]) -> list[dict[str, object]]:
    rows = []
    for case in cases:
        quality = execution_quality(case)
        risk = execution_risk(case)
        rows.append({
            **asdict(case),
            "execution_quality": round(quality, 3),
            "execution_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_execution_quality": round(mean(float(row["execution_quality"]) for row in rows), 3),
        "average_execution_risk": round(mean(float(row["execution_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["execution_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["execution_risk"]))["case_name"],
        "interpretation": "Execution quality depends on translation clarity, semantic checks, optimization traceability, runtime visibility, diagnostics, portability, reproducibility, security boundaries, performance fit, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_execution_model_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "execution_model_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "execution_model_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "execution_model_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "execution_model_audit_summary.json", summary)
