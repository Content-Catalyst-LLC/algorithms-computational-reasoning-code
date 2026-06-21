from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
import math

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class ErrorRecord:
    method: str
    resolution: float
    estimate: float
    reference: float
    absolute_error: float
    relative_error: float
    interpretation: str


def safe_relative_error(estimate: float, reference: float) -> float:
    if reference == 0:
        return float("nan")
    return abs(estimate - reference) / abs(reference)


def target_function(x: float) -> float:
    return math.sin(x) + 0.25 * x * x


def target_derivative(x: float) -> float:
    return math.cos(x) + 0.5 * x


def forward_difference(x: float, h: float) -> float:
    return (target_function(x + h) - target_function(x)) / h


def central_difference(x: float, h: float) -> float:
    return (target_function(x + h) - target_function(x - h)) / (2.0 * h)


def derivative_audit(x: float = 1.0) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    reference = target_derivative(x)
    for h in [1e-1, 5e-2, 1e-2, 5e-3, 1e-3, 1e-4]:
        for method_name, estimator in [("forward_difference", forward_difference), ("central_difference", central_difference)]:
            estimate = estimator(x, h)
            rows.append(asdict(ErrorRecord(
                method=method_name,
                resolution=h,
                estimate=round(estimate, 12),
                reference=round(reference, 12),
                absolute_error=round(abs(estimate - reference), 12),
                relative_error=round(safe_relative_error(estimate, reference), 12),
                interpretation="Derivative approximation depends on method, smoothness, step size, and floating-point behavior."
            )))
    return rows


def integrate_trapezoid(a: float, b: float, n: int) -> float:
    h = (b - a) / n
    total = 0.5 * (target_function(a) + target_function(b))
    for i in range(1, n):
        total += target_function(a + i * h)
    return h * total


def integrate_simpson(a: float, b: float, n: int) -> float:
    if n % 2 != 0:
        raise ValueError("Simpson rule requires an even number of subintervals.")
    h = (b - a) / n
    total = target_function(a) + target_function(b)
    for i in range(1, n):
        total += (4 if i % 2 == 1 else 2) * target_function(a + i * h)
    return total * h / 3.0


def integration_reference(a: float, b: float) -> float:
    return (-math.cos(b) + b ** 3 / 12.0) - (-math.cos(a) + a ** 3 / 12.0)


def integration_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    a = 0.0
    b = math.pi
    reference = integration_reference(a, b)
    for n in [10, 20, 40, 80, 160, 320]:
        for method_name, integrator in [("trapezoid_rule", integrate_trapezoid), ("simpson_rule", integrate_simpson)]:
            estimate = integrator(a, b, n)
            rows.append(asdict(ErrorRecord(
                method=method_name,
                resolution=float(n),
                estimate=round(estimate, 12),
                reference=round(reference, 12),
                absolute_error=round(abs(estimate - reference), 12),
                relative_error=round(safe_relative_error(estimate, reference), 12),
                interpretation="Quadrature accuracy depends on smoothness, interval count, and rule choice."
            )))
    return rows


def root_function(x: float) -> float:
    return x * x - 2.0


def root_derivative(x: float) -> float:
    return 2.0 * x


def bisection(a: float, b: float, tolerance: float, max_iter: int = 100) -> dict[str, object]:
    fa = root_function(a)
    fb = root_function(b)
    if fa * fb > 0:
        raise ValueError("Bisection requires a sign change.")
    midpoint = 0.5 * (a + b)
    iterations = 0
    for iterations in range(1, max_iter + 1):
        midpoint = 0.5 * (a + b)
        fm = root_function(midpoint)
        if abs(fm) < tolerance or 0.5 * abs(b - a) < tolerance:
            break
        if fa * fm <= 0:
            b = midpoint
            fb = fm
        else:
            a = midpoint
            fa = fm
    return {
        "method": "bisection",
        "tolerance": tolerance,
        "estimate": round(midpoint, 12),
        "reference": round(math.sqrt(2.0), 12),
        "absolute_error": round(abs(midpoint - math.sqrt(2.0)), 12),
        "iterations": iterations,
        "residual": round(abs(root_function(midpoint)), 12),
        "interpretation": "Bisection trades speed for bracketing reliability."
    }


def newton(start: float, tolerance: float, max_iter: int = 100) -> dict[str, object]:
    x = start
    iterations = 0
    for iterations in range(1, max_iter + 1):
        derivative = root_derivative(x)
        if derivative == 0:
            break
        next_x = x - root_function(x) / derivative
        if abs(next_x - x) < tolerance or abs(root_function(next_x)) < tolerance:
            x = next_x
            break
        x = next_x
    return {
        "method": "newton",
        "tolerance": tolerance,
        "estimate": round(x, 12),
        "reference": round(math.sqrt(2.0), 12),
        "absolute_error": round(abs(x - math.sqrt(2.0)), 12),
        "iterations": iterations,
        "residual": round(abs(root_function(x)), 12),
        "interpretation": "Newton iteration can converge quickly with a good starting point and well-behaved derivative."
    }


def root_finding_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for tolerance in [1e-2, 1e-4, 1e-6, 1e-8]:
        rows.append(bisection(1.0, 2.0, tolerance))
        rows.append(newton(1.0, tolerance))
    return rows


def ode_rhs(t: float, y: float) -> float:
    return 0.3 * y


def euler_final(y0: float, t_end: float, h: float) -> float:
    y = y0
    t = 0.0
    while t < t_end - 1e-12:
        y = y + h * ode_rhs(t, y)
        t += h
    return y


def rk4_final(y0: float, t_end: float, h: float) -> float:
    y = y0
    t = 0.0
    while t < t_end - 1e-12:
        k1 = ode_rhs(t, y)
        k2 = ode_rhs(t + 0.5 * h, y + 0.5 * h * k1)
        k3 = ode_rhs(t + 0.5 * h, y + 0.5 * h * k2)
        k4 = ode_rhs(t + h, y + h * k3)
        y = y + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        t += h
    return y


def ode_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    y0 = 1.0
    t_end = 5.0
    reference = y0 * math.exp(0.3 * t_end)
    for h in [0.5, 0.25, 0.125, 0.0625]:
        for method_name, solver in [("euler_method", euler_final), ("runge_kutta_4", rk4_final)]:
            estimate = solver(y0, t_end, h)
            rows.append(asdict(ErrorRecord(
                method=method_name,
                resolution=h,
                estimate=round(estimate, 12),
                reference=round(reference, 12),
                absolute_error=round(abs(estimate - reference), 12),
                relative_error=round(safe_relative_error(estimate, reference), 12),
                interpretation="Time-stepping accuracy depends on step size, method order, and stability."
            )))
    return rows


def approximation_review_checklist() -> list[dict[str, object]]:
    return [
        {"check": "problem_formulated", "status": "complete", "question": "Is the mathematical problem stated before selecting a numerical method?"},
        {"check": "method_justified", "status": "complete", "question": "Is the approximation method appropriate for the problem type?"},
        {"check": "resolution_tested", "status": "complete", "question": "Were step size, interval count, grid size, or tolerance varied?"},
        {"check": "error_reported", "status": "complete", "question": "Are absolute error, relative error, residual, or uncertainty reported?"},
        {"check": "floating_point_reviewed", "status": "partial", "question": "Were roundoff, cancellation, overflow, and precision limits considered?"},
        {"check": "stopping_condition_documented", "status": "complete", "question": "Are tolerances and maximum iterations documented?"},
        {"check": "validation_linked", "status": "partial", "question": "Are outputs compared with theory, benchmark, data, or expert expectations?"},
        {"check": "interpretation_limits_stated", "status": "complete", "question": "Are the limits of the numerical result communicated clearly?"},
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


def summarize(derivative_rows, integration_rows, root_rows, ode_rows, checklist_rows) -> dict[str, object]:
    best_derivative = min(derivative_rows, key=lambda row: float(row["absolute_error"]))
    best_integration = min(integration_rows, key=lambda row: float(row["absolute_error"]))
    best_root = min(root_rows, key=lambda row: float(row["absolute_error"]))
    best_ode = min(ode_rows, key=lambda row: float(row["absolute_error"]))
    review_attention = sum(1 for row in checklist_rows if row["status"] in {"partial", "needs_review"})
    return {
        "derivative_records": len(derivative_rows),
        "integration_records": len(integration_rows),
        "root_finding_records": len(root_rows),
        "ode_records": len(ode_rows),
        "best_derivative_method": best_derivative["method"],
        "best_derivative_resolution": best_derivative["resolution"],
        "best_integration_method": best_integration["method"],
        "best_integration_resolution": best_integration["resolution"],
        "best_root_method": best_root["method"],
        "best_root_tolerance": best_root["tolerance"],
        "best_ode_method": best_ode["method"],
        "best_ode_resolution": best_ode["resolution"],
        "review_items_needing_attention": review_attention,
        "interpretation": "Numerical approximation requires method selection, resolution testing, error reporting, convergence review, floating-point awareness, validation evidence, and interpretation limits."
    }


def main() -> None:
    derivative_rows = derivative_audit()
    integration_rows = integration_audit()
    root_rows = root_finding_audit()
    ode_rows = ode_audit()
    checklist_rows = approximation_review_checklist()
    summary = summarize(derivative_rows, integration_rows, root_rows, ode_rows, checklist_rows)
    write_csv(TABLES / "derivative_approximation_audit.csv", derivative_rows)
    write_csv(TABLES / "integration_approximation_audit.csv", integration_rows)
    write_csv(TABLES / "root_finding_audit.csv", root_rows)
    write_csv(TABLES / "ode_time_stepping_audit.csv", ode_rows)
    write_csv(TABLES / "numerical_approximation_checklist.csv", checklist_rows)
    write_csv(TABLES / "numerical_approximation_summary.csv", [summary])
    write_json(JSON_DIR / "derivative_approximation_audit.json", derivative_rows)
    write_json(JSON_DIR / "integration_approximation_audit.json", integration_rows)
    write_json(JSON_DIR / "root_finding_audit.json", root_rows)
    write_json(JSON_DIR / "ode_time_stepping_audit.json", ode_rows)
    write_json(JSON_DIR / "numerical_approximation_checklist.json", checklist_rows)
    write_json(JSON_DIR / "numerical_approximation_summary.json", summary)
    print("Numerical methods and algorithmic approximation audit complete.")
    print(TABLES / "numerical_approximation_summary.csv")


if __name__ == "__main__":
    main()
