from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    cases_path = TABLES / "synthetic_decision_cases.csv"
    if not cases_path.exists():
        raise SystemExit("Run decision_uncertainty_risk_workflow.py first.")
    cases = read_csv(cases_path)
    probability_multipliers = [0.75, 1.00, 1.25]
    cost_multipliers = [0.75, 1.00, 1.25, 1.50]
    rows: list[dict[str, object]] = []
    for p_mult in probability_multipliers:
        for c_mult in cost_multipliers:
            act_count = 0
            total_expected_value = 0.0
            high_exposure_count = 0
            for case in cases:
                p = max(0.0, min(1.0, float(case["baseline_risk"]) * p_mult))
                benefit = float(case["benefit_if_success"])
                loss = float(case["loss_if_failure"])
                cost = float(case["intervention_cost"]) * c_mult
                expected_value = 0.85 * benefit * p - (p * (1.0 - 0.22) * loss) - cost
                total_expected_value += expected_value
                if expected_value >= 0.08 and p >= 0.35:
                    act_count += 1
                if p * loss + cost > 180:
                    high_exposure_count += 1
            rows.append({
                "probability_multiplier": p_mult,
                "cost_multiplier": c_mult,
                "act_count": act_count,
                "act_rate": round(act_count / len(cases), 6),
                "mean_expected_value": round(total_expected_value / len(cases), 6),
                "high_exposure_count": high_exposure_count,
                "interpretation": "Sensitivity grid shows how recommendations shift when probability or cost assumptions change.",
            })
    write_csv(TABLES / "uncertainty_sensitivity_grid.csv", rows)
    print(TABLES / "uncertainty_sensitivity_grid.csv")


if __name__ == "__main__":
    main()
