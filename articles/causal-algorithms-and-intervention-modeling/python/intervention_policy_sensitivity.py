from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
INPUT = TABLES / "intervention_scenarios.csv"
OUTPUT = TABLES / "policy_sensitivity_grid.csv"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if not INPUT.exists():
        raise SystemExit("Run intervention_modeling_workflow.py before sensitivity review.")
    rows = read_rows(INPUT)
    thresholds = [0.48, 0.52, 0.55, 0.58, 0.62]
    out: list[dict[str, object]] = []
    names = sorted({row["intervention_name"] for row in rows})
    for name in names:
        subset = [row for row in rows if row["intervention_name"] == name]
        for threshold in thresholds:
            act_rate = sum(1 for row in subset if float(row["intervention_outcome"]) >= threshold) / len(subset)
            out.append({
                "intervention_name": name,
                "outcome_threshold": threshold,
                "modeled_action_rate": round(act_rate, 6),
                "cases_evaluated": len(subset),
                "interpretation": "Threshold sensitivity shows how rule choices change modeled action rates.",
            })
    write_rows(OUTPUT, out)
    print(OUTPUT)


if __name__ == "__main__":
    main()
