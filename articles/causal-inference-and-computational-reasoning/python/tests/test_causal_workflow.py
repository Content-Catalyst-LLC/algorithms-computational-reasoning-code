from __future__ import annotations

from pathlib import Path
import csv
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "python" / "causal_inference_audit_workflow.py")], check=True)
    estimates = read_csv(ROOT / "outputs" / "tables" / "causal_effect_estimates.csv")
    balance = read_csv(ROOT / "outputs" / "tables" / "covariate_balance_diagnostics.csv")
    assumptions = read_csv(ROOT / "outputs" / "tables" / "causal_assumption_register.csv")
    assert len(estimates) >= 4, "Expected multiple causal estimators."
    assert any(row["estimate_type"] == "naive_difference_in_means" for row in estimates)
    assert any(float(row["absolute_standardized_difference"]) > 0.05 for row in balance)
    assert any(row["status"] == "needs_review" for row in assumptions)
    print("Causal workflow smoke tests passed.")


if __name__ == "__main__":
    main()
