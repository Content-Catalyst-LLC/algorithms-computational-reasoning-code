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
    decisions = read_rows(TABLES / "synthetic_algorithmic_decisions.csv")
    review_rows: list[dict[str, object]] = []
    for threshold in [0.56, 0.58, 0.60, 0.62, 0.64, 0.66, 0.68]:
        favorable = [row for row in decisions if float(row["decision_score"]) >= threshold]
        near_boundary = [row for row in decisions if abs(float(row["decision_score"]) - threshold) <= 0.03]
        review_rows.append({
            "threshold": threshold,
            "favorable_count": len(favorable),
            "near_boundary_count": len(near_boundary),
            "near_boundary_share": round(len(near_boundary) / len(decisions), 6),
            "interpretation": "Near-boundary cases deserve special explanation and appeal review because small threshold changes alter outcomes.",
        })
    write_csv(TABLES / "threshold_boundary_review.csv", review_rows)
    JSON_DIR.mkdir(parents=True, exist_ok=True)
    (JSON_DIR / "threshold_boundary_review.json").write_text(json.dumps(review_rows, indent=2), encoding="utf-8")
    print("Threshold boundary review complete.")


if __name__ == "__main__":
    main()
