#!/usr/bin/env python3
"""CLI entry point for multi-objective trade-off analysis."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from audit import build_alternatives, mark_pareto, weighted_scores, write_csv, write_json  # type: ignore
else:
    from .audit import build_alternatives, mark_pareto, weighted_scores, write_csv, write_json

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
OUTPUTS = ARTICLE_ROOT / "outputs"


def main() -> None:
    alternatives = build_alternatives()
    objectives = ["cost", "risk", "emissions", "service_quality", "access", "robustness", "burden"]
    pareto_rows = mark_pareto(alternatives, objectives)
    weights = {"cost": 0.20, "risk": 0.20, "emissions": 0.15, "service_quality": 0.15, "access": 0.15, "robustness": 0.10, "burden": 0.05}
    weighted_rows = weighted_scores(alternatives, weights)

    cli_dir = OUTPUTS / "cli"
    write_csv(cli_dir / "multi_objective_cli_pareto.csv", pareto_rows)
    write_csv(cli_dir / "multi_objective_cli_weighted_scores.csv", weighted_rows)
    write_json(cli_dir / "multi_objective_cli_pareto.json", pareto_rows)
    write_json(cli_dir / "multi_objective_cli_weighted_scores.json", weighted_rows)

    print("Top weighted alternative:", weighted_rows[0]["alternative"])
    print("Pareto-efficient alternatives:", ",".join(str(row["alternative"]) for row in pareto_rows if row["pareto_efficient"]))


if __name__ == "__main__":
    main()
