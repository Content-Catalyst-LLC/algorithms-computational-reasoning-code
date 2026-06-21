from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

ARTICLE_ROOT = Path(__file__).resolve().parents[2]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    subprocess.run([sys.executable, str(ARTICLE_ROOT / "python" / "counterfactual_reasoning_audit_workflow.py")], check=True)
    decisions = read_csv(ARTICLE_ROOT / "outputs" / "tables" / "synthetic_algorithmic_decisions.csv")
    candidates = read_csv(ARTICLE_ROOT / "outputs" / "tables" / "counterfactual_candidates.csv")
    recourse = read_csv(ARTICLE_ROOT / "outputs" / "tables" / "minimal_recourse_actions.csv")
    assert len(decisions) == 500, f"expected 500 decisions, got {len(decisions)}"
    assert len(candidates) > len(decisions), "expected multiple counterfactual candidates per case"
    assert all(0.0 <= float(row["decision_score"]) <= 1.0 for row in decisions)
    assert any(row["flipped_to_favorable"] == "True" for row in candidates), "expected at least one flipping counterfactual"
    assert all(float(row["counterfactual_score"]) >= float(row["original_score"]) for row in recourse)
    print("Counterfactual workflow smoke tests passed.")


if __name__ == "__main__":
    main()
