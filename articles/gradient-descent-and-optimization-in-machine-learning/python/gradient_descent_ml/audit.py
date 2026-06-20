# gradient_descent_ml_optimization_audit.py
# Dependency-light workflow for auditing gradient descent and machine learning optimization.

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import json
import random

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class OptimizationTrainingCase:
    case_name: str
    model_context: str
    training_goal: str
    objective_documentation: float
    data_documentation: float
    feature_scaling_review: float
    optimizer_documentation: float
    learning_rate_rationale: float
    validation_discipline: float
    regularization_review: float
    robustness_review: float
    fairness_review: float
    reproducibility: float
    traceability: float
    governance_review: float
    communication_clarity: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def ml_optimization_governance_score(case: OptimizationTrainingCase) -> float:
    return clamp(
        100.0 * (
            0.09 * case.objective_documentation
            + 0.09 * case.data_documentation
            + 0.07 * case.feature_scaling_review
            + 0.08 * case.optimizer_documentation
            + 0.08 * case.learning_rate_rationale
            + 0.10 * case.validation_discipline
            + 0.08 * case.regularization_review
            + 0.09 * case.robustness_review
            + 0.09 * case.fairness_review
            + 0.08 * case.reproducibility
            + 0.08 * case.traceability
            + 0.05 * case.governance_review
            + 0.02 * case.communication_clarity
        )
    )


def ml_optimization_governance_risk(case: OptimizationTrainingCase) -> float:
    weak_points = [
        1.0 - case.objective_documentation,
        1.0 - case.data_documentation,
        1.0 - case.feature_scaling_review,
        1.0 - case.optimizer_documentation,
        1.0 - case.learning_rate_rationale,
        1.0 - case.validation_discipline,
        1.0 - case.regularization_review,
        1.0 - case.robustness_review,
        1.0 - case.fairness_review,
        1.0 - case.reproducibility,
        1.0 - case.traceability,
        1.0 - case.governance_review,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong machine-learning optimization governance"
    if score >= 70 and risk <= 35:
        return "usable training process with review needs"
    if risk >= 55:
        return "high risk; objective, data, optimizer, validation, robustness, fairness, reproducibility, or governance may be underdefined"
    return "partial discipline; strengthen objective documentation, validation, reproducibility, fairness, robustness, traceability, and governance"


def read_cases(path: Path | None = None) -> list[OptimizationTrainingCase]:
    path = path or ARTICLE_ROOT / "data" / "synthetic_training_cases.csv"
    cases: list[OptimizationTrainingCase] = []

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            cases.append(
                OptimizationTrainingCase(
                    case_name=row["case_name"],
                    model_context=row["model_context"],
                    training_goal=row["training_goal"],
                    objective_documentation=float(row["objective_documentation"]),
                    data_documentation=float(row["data_documentation"]),
                    feature_scaling_review=float(row["feature_scaling_review"]),
                    optimizer_documentation=float(row["optimizer_documentation"]),
                    learning_rate_rationale=float(row["learning_rate_rationale"]),
                    validation_discipline=float(row["validation_discipline"]),
                    regularization_review=float(row["regularization_review"]),
                    robustness_review=float(row["robustness_review"]),
                    fairness_review=float(row["fairness_review"]),
                    reproducibility=float(row["reproducibility"]),
                    traceability=float(row["traceability"]),
                    governance_review=float(row["governance_review"]),
                    communication_clarity=float(row["communication_clarity"]),
                )
            )
    return cases


def synthetic_regression_data(seed: int = 42) -> list[dict[str, float]]:
    random.seed(seed)
    rows: list[dict[str, float]] = []

    for i in range(40):
        x = -2.0 + 4.0 * i / 39.0
        noise = random.uniform(-0.35, 0.35)
        y = 1.5 + 2.2 * x + noise
        rows.append({"x": x, "y": y})

    return rows


def mse(rows: list[dict[str, float]], weight: float, bias: float) -> float:
    errors = [(row["y"] - (weight * row["x"] + bias)) ** 2 for row in rows]
    return sum(errors) / len(errors)


def gradient_step(rows: list[dict[str, float]], weight: float, bias: float, learning_rate: float) -> tuple[float, float]:
    n = len(rows)
    grad_w = 0.0
    grad_b = 0.0

    for row in rows:
        prediction = weight * row["x"] + bias
        error = prediction - row["y"]
        grad_w += (2.0 / n) * error * row["x"]
        grad_b += (2.0 / n) * error

    return weight - learning_rate * grad_w, bias - learning_rate * grad_b


def run_gradient_descent_example(steps: int = 80, learning_rate: float = 0.08) -> list[dict[str, float]]:
    rows = synthetic_regression_data()
    weight = 0.0
    bias = 0.0
    trace: list[dict[str, float]] = []

    for step in range(steps + 1):
        loss = mse(rows, weight, bias)
        trace.append({
            "step": step,
            "weight": round(weight, 6),
            "bias": round(bias, 6),
            "loss": round(loss, 6),
            "learning_rate": learning_rate,
        })

        if step < steps:
            weight, bias = gradient_step(rows, weight, bias, learning_rate)

    return trace


def learning_rate_sensitivity(rates: list[float] | None = None, steps: int = 40) -> list[dict[str, float]]:
    rates = rates or [0.005, 0.02, 0.08, 0.20, 0.50]
    rows = synthetic_regression_data()
    output: list[dict[str, float]] = []

    for rate in rates:
        weight = 0.0
        bias = 0.0
        diverged = False
        for _ in range(steps):
            weight, bias = gradient_step(rows, weight, bias, rate)
            loss = mse(rows, weight, bias)
            if loss > 1_000_000:
                diverged = True
                break
        output.append({
            "learning_rate": rate,
            "final_weight": round(weight, 6),
            "final_bias": round(bias, 6),
            "final_loss": round(mse(rows, weight, bias), 6),
            "diverged": diverged,
        })
    return output


def run_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    for case in read_cases():
        score = ml_optimization_governance_score(case)
        risk = ml_optimization_governance_risk(case)
        rows.append({
            **asdict(case),
            "ml_optimization_governance_score": round(score, 3),
            "ml_optimization_governance_risk": round(risk, 3),
            "diagnostic": diagnose(score, risk),
        })

    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    if not rows:
        path.write_text("", encoding="utf-8")
        return

    fieldnames = sorted({key for row in rows for key in row.keys()})

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def summarize(rows: list[dict[str, object]], trace: list[dict[str, float]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_ml_optimization_governance_score": round(mean(float(row["ml_optimization_governance_score"]) for row in rows), 3),
        "average_ml_optimization_governance_risk": round(mean(float(row["ml_optimization_governance_risk"]) for row in rows), 3),
        "highest_score_case": max(rows, key=lambda row: float(row["ml_optimization_governance_score"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["ml_optimization_governance_risk"]))["case_name"],
        "initial_loss": trace[0]["loss"],
        "final_loss": trace[-1]["loss"],
        "loss_reduction": round(trace[0]["loss"] - trace[-1]["loss"], 6),
        "interpretation": "Machine learning optimization governance depends on objective documentation, data documentation, feature scaling, optimizer documentation, learning-rate rationale, validation discipline, regularization review, robustness review, fairness review, reproducibility, traceability, governance, and communication clarity.",
    }


def main() -> None:
    audit_rows = run_audit()
    trace = run_gradient_descent_example()
    sensitivity = learning_rate_sensitivity()
    summary = summarize(audit_rows, trace)

    write_csv(TABLES / "gradient_descent_ml_optimization_audit.csv", audit_rows)
    write_csv(TABLES / "gradient_descent_ml_optimization_audit_summary.csv", [summary])
    write_csv(TABLES / "gradient_descent_training_trace.csv", trace)
    write_csv(TABLES / "learning_rate_sensitivity.csv", sensitivity)

    write_json(JSON_DIR / "gradient_descent_ml_optimization_audit.json", audit_rows)
    write_json(JSON_DIR / "gradient_descent_ml_optimization_audit_summary.json", summary)
    write_json(JSON_DIR / "gradient_descent_training_trace.json", trace)
    write_json(JSON_DIR / "learning_rate_sensitivity.json", sensitivity)

    print("Gradient descent and machine learning optimization audit complete.")
    print(TABLES / "gradient_descent_ml_optimization_audit.csv")


if __name__ == "__main__":
    main()
