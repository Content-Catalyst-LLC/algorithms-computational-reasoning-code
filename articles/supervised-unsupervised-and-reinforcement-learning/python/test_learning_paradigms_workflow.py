from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
JSON_DIR = ROOT / "outputs" / "json"


def read_csv(name: str) -> list[dict[str, str]]:
    with (TABLES / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    supervised = read_csv("supervised_metrics.csv")
    assert any(row["split"] == "test" for row in supervised), "missing supervised test metrics"
    test = next(row for row in supervised if row["split"] == "test")
    assert 0.0 <= float(test["accuracy"]) <= 1.0, "accuracy outside [0,1]"
    clusters = read_csv("unsupervised_cluster_summary.csv")
    assert len(clusters) == 3, "expected three cluster summaries"
    assert sum(int(row["n"]) for row in clusters) > 0, "empty clusters summary"
    rl = read_csv("reinforcement_learning_summary.csv")
    assert len(rl) == 3, "expected three reinforcement-learning arms"
    governance = read_csv("learning_paradigm_governance_register.csv")
    assert any(row["status"] == "needs_review" for row in governance), "governance register should contain review items"
    payload = json.loads((JSON_DIR / "learning_paradigms_audit_summary.json").read_text(encoding="utf-8"))
    assert payload["n_observations"] >= 100, "expected substantial synthetic observations"
    assert payload["governance_items_needing_review"] >= 1, "expected governance review count"
    print("Learning paradigms workflow tests passed.")


if __name__ == "__main__":
    main()
