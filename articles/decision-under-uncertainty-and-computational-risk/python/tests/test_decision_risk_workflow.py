from __future__ import annotations

from pathlib import Path
import csv
import subprocess
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]


def run_script(rel_path: str) -> None:
    subprocess.run([sys.executable, rel_path], cwd=ARTICLE_ROOT, check=True)


def read_rows(rel_path: str) -> list[dict[str, str]]:
    with (ARTICLE_ROOT / rel_path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    run_script("python/decision_uncertainty_risk_workflow.py")
    run_script("python/risk_threshold_review.py")
    run_script("python/uncertainty_sensitivity_analysis.py")

    cases = read_rows("outputs/tables/synthetic_decision_cases.csv")
    metrics = read_rows("outputs/tables/decision_metrics.csv")
    thresholds = read_rows("outputs/tables/threshold_review.csv")
    grid = read_rows("outputs/tables/uncertainty_sensitivity_grid.csv")

    assert len(cases) == 300, len(cases)
    assert len(metrics) == 1200, len(metrics)
    assert len(thresholds) == 300, len(thresholds)
    assert len(grid) == 12, len(grid)
    assert any(row["decision"] == "act_with_review" for row in thresholds)
    assert all("expected_net_value" in row for row in metrics)
    print("Decision risk workflow tests passed.")


if __name__ == "__main__":
    main()
