from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "python" / "lp_convex" / "audit.py"

spec = importlib.util.spec_from_file_location("audit", AUDIT)
audit = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(audit)


def test_brute_force_lp_best_solution():
    result = audit.brute_force_linear_program()
    best = result["best_solution"]
    assert best["objective_value"] >= 16
    assert best["labor_used"] <= 8
    assert best["material_used"] <= 8


def test_convex_quadratic_minimum():
    rows = audit.convex_quadratic_example()
    minima = [row for row in rows if row["is_global_minimum"]]
    assert minima == [{"x": 2, "convex_objective_value": 1, "is_global_minimum": True}]
