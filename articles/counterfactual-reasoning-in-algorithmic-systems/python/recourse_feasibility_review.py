from __future__ import annotations

from pathlib import Path
import csv
import json

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    recourse = read_rows(TABLES / "minimal_recourse_actions.csv")
    buckets = {
        "low_burden": [],
        "moderate_burden": [],
        "high_burden": [],
    }
    for row in recourse:
        cost = float(row["recourse_cost"])
        if cost <= 0.20:
            buckets["low_burden"].append(row)
        elif cost <= 0.45:
            buckets["moderate_burden"].append(row)
        else:
            buckets["high_burden"].append(row)
    rows = [{
        "burden_bucket": bucket,
        "case_count": len(items),
        "share_of_recourse_cases": round(len(items) / max(1, len(recourse)), 6),
        "interpretation": "Feasible recourse should be evaluated by burden, not only by mathematical possibility.",
    } for bucket, items in buckets.items()]
    write_csv(TABLES / "recourse_burden_review.csv", rows)
    JSON_DIR.mkdir(parents=True, exist_ok=True)
    (JSON_DIR / "recourse_burden_review.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print("Recourse feasibility review complete.")


if __name__ == "__main__":
    main()
