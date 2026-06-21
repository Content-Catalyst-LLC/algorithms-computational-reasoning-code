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
    metrics_path = TABLES / "decision_metrics.csv"
    if not metrics_path.exists():
        raise SystemExit("Run decision_uncertainty_risk_workflow.py first.")
    metrics = read_csv(metrics_path)
    thresholds = [0.00, 0.05, 0.08, 0.12, 0.18, 0.25]
    rows: list[dict[str, object]] = []
    for threshold in thresholds:
        best_by_case: dict[int, dict[str, str]] = {}
        for row in metrics:
            case_id = int(row["case_id"])
            if case_id not in best_by_case or float(row["expected_net_value"]) > float(best_by_case[case_id]["expected_net_value"]):
                best_by_case[case_id] = row
        act_count = 0
        monitor_count = 0
        review_count = 0
        for row in best_by_case.values():
            risk = float(row["baseline_risk"])
            value = float(row["expected_net_value"])
            confidence = float(row["confidence_score"])
            if value >= threshold and risk >= 0.35 and confidence >= 0.55:
                act_count += 1
            elif confidence < 0.55:
                review_count += 1
            else:
                monitor_count += 1
        total = len(best_by_case)
        rows.append({
            "action_threshold": threshold,
            "act_count": act_count,
            "human_review_count": review_count,
            "monitor_or_defer_count": monitor_count,
            "act_rate": round(act_count / total, 6),
            "interpretation": "Changing thresholds changes the population affected by action; thresholds require governance review.",
        })
    write_csv(TABLES / "threshold_grid.csv", rows)
    print(TABLES / "threshold_grid.csv")


if __name__ == "__main__":
    main()
