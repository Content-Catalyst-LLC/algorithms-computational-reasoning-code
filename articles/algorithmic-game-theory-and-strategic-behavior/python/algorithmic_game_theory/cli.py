#!/usr/bin/env python3
"""CLI for algorithmic game theory and strategic behavior examples."""

from __future__ import annotations

from pathlib import Path
import json
import sys

try:
    from .audit import build_payoff_game, incentive_sensitivity_examples, payoff_table_rows, price_of_anarchy, pure_nash_equilibria, write_csv
except ImportError:
    sys.path.append(str(Path(__file__).resolve().parent))
    from audit import build_payoff_game, incentive_sensitivity_examples, payoff_table_rows, price_of_anarchy, pure_nash_equilibria, write_csv

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
CLI_DIR = ARTICLE_ROOT / "outputs" / "cli"


def main() -> None:
    CLI_DIR.mkdir(parents=True, exist_ok=True)
    game = build_payoff_game()
    rows = payoff_table_rows(game)
    equilibria = pure_nash_equilibria(game)
    poa = price_of_anarchy(game)
    sensitivity = incentive_sensitivity_examples()
    attractive = [row for row in sensitivity if row["manipulation_attractive"]]
    write_csv(CLI_DIR / "payoff_game_table_cli.csv", rows)
    write_csv(CLI_DIR / "pure_nash_equilibria_cli.csv", equilibria)
    write_csv(CLI_DIR / "incentive_sensitivity_cli.csv", sensitivity)
    payload = {
        "pure_nash_equilibrium_count": len(equilibria),
        "welfare_price_of_anarchy": poa["welfare_price_of_anarchy"],
        "attractive_manipulation_scenarios": len(attractive),
        "summary": "Strategic algorithm review should document agents, actions, payoffs, mechanisms, manipulation paths, sensitivity, welfare, fairness, and governance.",
    }
    (CLI_DIR / "strategic_behavior_cli_summary.json").write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print("CLI strategic behavior outputs written to", CLI_DIR)
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
