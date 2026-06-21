# algorithms_in_scientific_computing_audit.py
# Dependency-light workflow for numerical approximation, convergence, and scientific computing review.

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from statistics import mean, pstdev
import csv
import json
import math
import random

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class ApproximationResult:
    method: str
    step_size: float
    estimate: float
    true_value: float
    absolute_error: float
    interpretation: str


def f(x: float) -> float:
    return math.sin(x)


def df_true(x: float) -> float:
    return math.cos(x)


def derivative_forward(x: float, h: float) -> float:
    return (f(x + h) - f(x)) / h


def derivative_central(x: float, h: float) -> float:
    return (f(x + h) - f(x - h)) / (2.0 * h)


def derivative_study(x: float = 1.0) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    true_value = df_true(x)
    for h in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
        for method_name, estimator in [("forward_difference", derivative_forward), ("central_difference", derivative_central)]:
            estimate = estimator(x, h)
            rows.append(asdict(ApproximationResult(
                method=method_name,
                step_size=h,
                estimate=round(estimate, 12),
                true_value=round(true_value, 12),
                absolute_error=round(abs(estimate - true_value), 12),
                interpretation="Derivative approximation error depends on method and step size.",
            )))
    return rows


def integrate_trapezoid(a: float, b: float, n: int) -> float:
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return h * total


def integration_study() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    a, b, true_value = 0.0, math.pi, 2.0
    for n in [10, 20, 50, 100, 200, 500]:
        estimate = integrate_trapezoid(a, b, n)
        rows.append({
            "method": "trapezoid_rule",
            "interval_start": a,
            "interval_end": b,
            "subintervals": n,
            "estimate": round(estimate, 12),
            "true_value": true_value,
            "absolute_error": round(abs(estimate - true_value), 12),
            "interpretation": "Numerical integration improves as resolution increases for this smooth example.",
        })
    return rows


def ode_rhs(t: float, y: float, rate: float = 0.4) -> float:
    return rate * y


def euler_solver(y0: float, t0: float, t_end: float, h: float) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    t, y = t0, y0
    while t <= t_end + 1e-12:
        rows.append({"time": round(t, 10), "value": y})
        y = y + h * ode_rhs(t, y)
        t += h
    return rows


def rk4_solver(y0: float, t0: float, t_end: float, h: float) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    t, y = t0, y0
    while t <= t_end + 1e-12:
        rows.append({"time": round(t, 10), "value": y})
        k1 = ode_rhs(t, y)
        k2 = ode_rhs(t + 0.5 * h, y + 0.5 * h * k1)
        k3 = ode_rhs(t + 0.5 * h, y + 0.5 * h * k2)
        k4 = ode_rhs(t + h, y + h * k3)
        y = y + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        t += h
    return rows


def ode_convergence_study() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    y0, t0, t_end, rate = 1.0, 0.0, 5.0, 0.4
    true_final = y0 * math.exp(rate * t_end)
    for h in [0.5, 0.25, 0.125, 0.0625]:
        for method_name, solver in [("euler", euler_solver), ("rk4", rk4_solver)]:
            trajectory = solver(y0, t0, t_end, h)
            final_value = trajectory[-1]["value"]
            rows.append({
                "method": method_name,
                "step_size": h,
                "final_estimate": round(final_value, 12),
                "true_final": round(true_final, 12),
                "absolute_error": round(abs(final_value - true_final), 12),
                "trajectory_points": len(trajectory),
                "interpretation": "ODE solver accuracy depends on method order and time-step size.",
            })
    return rows


def monte_carlo_pi(samples: int, seed: int) -> dict[str, object]:
    rng = random.Random(seed)
    inside = 0
    for _ in range(samples):
        x, y = rng.random(), rng.random()
        if x * x + y * y <= 1.0:
            inside += 1
    estimate = 4.0 * inside / samples
    return {"samples": samples, "seed": seed, "pi_estimate": round(estimate, 10), "true_pi": round(math.pi, 10), "absolute_error": round(abs(estimate - math.pi), 10)}


def monte_carlo_study() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []
    for samples in [100, 1000, 10000]:
        estimates = []
        for seed in range(1, 21):
            result = monte_carlo_pi(samples, seed)
            rows.append(result)
            estimates.append(float(result["pi_estimate"]))
        summary_rows.append({
            "samples": samples,
            "runs": len(estimates),
            "mean_estimate": round(mean(estimates), 10),
            "std_estimate": round(pstdev(estimates), 10),
            "mean_absolute_error": round(mean(abs(value - math.pi) for value in estimates), 10),
            "interpretation": "Monte Carlo error generally decreases as sample size increases, but individual runs vary.",
        })
    return rows, summary_rows


def workflow_review_checklist() -> list[dict[str, object]]:
    return [
        {"check": "mathematical_problem_defined", "status": "complete", "question": "Is the mathematical problem stated before the algorithm is chosen?"},
        {"check": "algorithm_choice_documented", "status": "complete", "question": "Is the numerical method documented and justified?"},
        {"check": "step_size_or_resolution_tested", "status": "complete", "question": "Has resolution or step-size sensitivity been checked?"},
        {"check": "floating_point_risk_reviewed", "status": "partial", "question": "Have roundoff, cancellation, overflow, and precision limits been considered?"},
        {"check": "convergence_checked", "status": "complete", "question": "Does the workflow test convergence or stability where relevant?"},
        {"check": "validation_evidence_linked", "status": "partial", "question": "Are results compared with theory, benchmark, data, or expert expectations?"},
        {"check": "uncertainty_communicated", "status": "complete", "question": "Are uncertainty, variability, or error estimates communicated?"},
        {"check": "workflow_reproducible", "status": "complete", "question": "Are scripts, parameters, outputs, and seeds preserved?"},
    ]


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


def summarize(derivative_rows: list[dict[str, object]], integration_rows: list[dict[str, object]], ode_rows: list[dict[str, object]], mc_summary_rows: list[dict[str, object]], checklist_rows: list[dict[str, object]]) -> dict[str, object]:
    best_derivative = min(derivative_rows, key=lambda row: float(row["absolute_error"]))
    best_integral = min(integration_rows, key=lambda row: float(row["absolute_error"]))
    best_ode = min(ode_rows, key=lambda row: float(row["absolute_error"]))
    review_attention = sum(1 for row in checklist_rows if row["status"] in {"partial", "needs_review"})
    return {
        "derivative_methods_reviewed": len(set(row["method"] for row in derivative_rows)),
        "integration_resolutions_reviewed": len(integration_rows),
        "ode_solver_runs": len(ode_rows),
        "monte_carlo_sample_levels": len(mc_summary_rows),
        "best_derivative_method": best_derivative["method"],
        "best_derivative_step_size": best_derivative["step_size"],
        "best_integration_subintervals": best_integral["subintervals"],
        "best_ode_method": best_ode["method"],
        "best_ode_step_size": best_ode["step_size"],
        "review_items_needing_attention": review_attention,
        "interpretation": "Scientific computing requires attention to approximation, discretization, finite precision, solver behavior, convergence, uncertainty, validation, reproducibility, and interpretation.",
    }


def main() -> None:
    derivative_rows = derivative_study()
    integration_rows = integration_study()
    ode_rows = ode_convergence_study()
    mc_rows, mc_summary_rows = monte_carlo_study()
    checklist_rows = workflow_review_checklist()
    summary = summarize(derivative_rows, integration_rows, ode_rows, mc_summary_rows, checklist_rows)

    write_csv(TABLES / "finite_difference_derivative_study.csv", derivative_rows)
    write_csv(TABLES / "numerical_integration_study.csv", integration_rows)
    write_csv(TABLES / "ode_convergence_study.csv", ode_rows)
    write_csv(TABLES / "monte_carlo_pi_runs.csv", mc_rows)
    write_csv(TABLES / "monte_carlo_pi_summary.csv", mc_summary_rows)
    write_csv(TABLES / "scientific_computing_workflow_checklist.csv", checklist_rows)
    write_csv(TABLES / "scientific_computing_audit_summary.csv", [summary])

    write_json(JSON_DIR / "finite_difference_derivative_study.json", derivative_rows)
    write_json(JSON_DIR / "numerical_integration_study.json", integration_rows)
    write_json(JSON_DIR / "ode_convergence_study.json", ode_rows)
    write_json(JSON_DIR / "monte_carlo_pi_runs.json", mc_rows)
    write_json(JSON_DIR / "monte_carlo_pi_summary.json", mc_summary_rows)
    write_json(JSON_DIR / "scientific_computing_workflow_checklist.json", checklist_rows)
    write_json(JSON_DIR / "scientific_computing_audit_summary.json", summary)

    print("Algorithms in scientific computing audit complete.")
    print(TABLES / "scientific_computing_audit_summary.csv")


if __name__ == "__main__":
    main()
