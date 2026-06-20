#!/usr/bin/env python3
"""Audit strategic behavior in algorithmic systems.

This module is dependency-light by design. It builds a small payoff game,
identifies pure-strategy Nash equilibria, computes welfare loss from selfish
behavior, runs incentive-sensitivity examples, and scores governance readiness
for strategic algorithmic systems.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from itertools import product
from pathlib import Path
from statistics import mean
import csv
import json

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class StrategicGovernanceCase:
    case_name: str
    system_context: str
    strategic_goal: str
    agent_inventory: float
    action_space_clarity: float
    payoff_documentation: float
    mechanism_documentation: float
    incentive_alignment: float
    manipulation_review: float
    sensitivity_review: float
    equilibrium_review: float
    welfare_review: float
    fairness_review: float
    traceability: float
    governance_review: float
    communication_clarity: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def strategic_governance_score(case: StrategicGovernanceCase) -> float:
    return clamp(
        100.0
        * (
            0.08 * case.agent_inventory
            + 0.08 * case.action_space_clarity
            + 0.09 * case.payoff_documentation
            + 0.09 * case.mechanism_documentation
            + 0.11 * case.incentive_alignment
            + 0.10 * case.manipulation_review
            + 0.10 * case.sensitivity_review
            + 0.08 * case.equilibrium_review
            + 0.08 * case.welfare_review
            + 0.08 * case.fairness_review
            + 0.06 * case.traceability
            + 0.04 * case.governance_review
            + 0.01 * case.communication_clarity
        )
    )


def strategic_governance_risk(case: StrategicGovernanceCase) -> float:
    weak_points = [
        1.0 - case.agent_inventory,
        1.0 - case.action_space_clarity,
        1.0 - case.payoff_documentation,
        1.0 - case.mechanism_documentation,
        1.0 - case.incentive_alignment,
        1.0 - case.manipulation_review,
        1.0 - case.sensitivity_review,
        1.0 - case.equilibrium_review,
        1.0 - case.welfare_review,
        1.0 - case.fairness_review,
        1.0 - case.traceability,
        1.0 - case.governance_review,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong strategic-governance discipline"
    if score >= 70 and risk <= 35:
        return "usable strategic mechanism with review needs"
    if risk >= 55:
        return "high risk; incentives, manipulation pathways, sensitivity, equilibrium behavior, welfare, fairness, or governance may be underdefined"
    return "partial discipline; strengthen agent inventories, payoff models, mechanism documentation, manipulation review, sensitivity testing, welfare analysis, fairness, traceability, and governance"


def build_payoff_game() -> dict[tuple[str, str], tuple[float, float]]:
    return {
        ("cooperate", "cooperate"): (3.0, 3.0),
        ("cooperate", "defect"): (0.0, 5.0),
        ("defect", "cooperate"): (5.0, 0.0),
        ("defect", "defect"): (1.0, 1.0),
    }


def best_response_player_one(game: dict[tuple[str, str], tuple[float, float]], player_two_strategy: str) -> list[str]:
    strategies = sorted({profile[0] for profile in game})
    payoffs = [(strategy, game[(strategy, player_two_strategy)][0]) for strategy in strategies]
    best_value = max(value for _, value in payoffs)
    return [strategy for strategy, value in payoffs if value == best_value]


def best_response_player_two(game: dict[tuple[str, str], tuple[float, float]], player_one_strategy: str) -> list[str]:
    strategies = sorted({profile[1] for profile in game})
    payoffs = [(strategy, game[(player_one_strategy, strategy)][1]) for strategy in strategies]
    best_value = max(value for _, value in payoffs)
    return [strategy for strategy, value in payoffs if value == best_value]


def pure_nash_equilibria(game: dict[tuple[str, str], tuple[float, float]]) -> list[dict[str, object]]:
    equilibria: list[dict[str, object]] = []
    for player_one_strategy, player_two_strategy in sorted(game):
        p1_best = best_response_player_one(game, player_two_strategy)
        p2_best = best_response_player_two(game, player_one_strategy)
        payoff = game[(player_one_strategy, player_two_strategy)]
        if player_one_strategy in p1_best and player_two_strategy in p2_best:
            equilibria.append(
                {
                    "player_one_strategy": player_one_strategy,
                    "player_two_strategy": player_two_strategy,
                    "player_one_payoff": payoff[0],
                    "player_two_payoff": payoff[1],
                    "total_welfare": payoff[0] + payoff[1],
                }
            )
    return equilibria


def payoff_table_rows(game: dict[tuple[str, str], tuple[float, float]]) -> list[dict[str, object]]:
    equilibria_profiles = {
        (row["player_one_strategy"], row["player_two_strategy"])
        for row in pure_nash_equilibria(game)
    }
    rows: list[dict[str, object]] = []
    for profile, payoff in sorted(game.items()):
        rows.append(
            {
                "player_one_strategy": profile[0],
                "player_two_strategy": profile[1],
                "player_one_payoff": payoff[0],
                "player_two_payoff": payoff[1],
                "total_welfare": payoff[0] + payoff[1],
                "pure_nash_equilibrium": profile in equilibria_profiles,
            }
        )
    return rows


def price_of_anarchy(game: dict[tuple[str, str], tuple[float, float]]) -> dict[str, object]:
    rows = payoff_table_rows(game)
    equilibria = [row for row in rows if row["pure_nash_equilibrium"]]
    optimal_welfare = max(float(row["total_welfare"]) for row in rows)
    worst_equilibrium_welfare = min(float(row["total_welfare"]) for row in equilibria) if equilibria else 0.0
    ratio = None if worst_equilibrium_welfare == 0 else round(optimal_welfare / worst_equilibrium_welfare, 6)
    return {
        "optimal_welfare": optimal_welfare,
        "worst_equilibrium_welfare": worst_equilibrium_welfare,
        "welfare_price_of_anarchy": ratio,
        "interpretation": "For welfare maximization, this ratio compares best possible welfare with the worst equilibrium welfare.",
    }


def incentive_sensitivity_examples() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    base_reward = 10.0
    manipulation_costs = [1.0, 3.0, 6.0, 9.0, 12.0]
    penalties = [0.0, 2.0, 5.0, 8.0]
    for cost, penalty in product(manipulation_costs, penalties):
        net_gain = base_reward - cost - penalty
        rows.append(
            {
                "base_reward": base_reward,
                "manipulation_cost": cost,
                "penalty": penalty,
                "net_gain_from_manipulation": round(net_gain, 3),
                "manipulation_attractive": net_gain > 0,
            }
        )
    return rows


def build_cases() -> list[StrategicGovernanceCase]:
    return [
        StrategicGovernanceCase(
            case_name="Truthful auction mechanism",
            system_context="Allocate scarce inventory through an auction with documented allocation and payment rules.",
            strategic_goal="encourage truthful bidding while preserving efficiency, fairness, and auditability",
            agent_inventory=0.86,
            action_space_clarity=0.84,
            payoff_documentation=0.82,
            mechanism_documentation=0.88,
            incentive_alignment=0.84,
            manipulation_review=0.78,
            sensitivity_review=0.76,
            equilibrium_review=0.80,
            welfare_review=0.82,
            fairness_review=0.74,
            traceability=0.82,
            governance_review=0.78,
            communication_clarity=0.80,
        ),
        StrategicGovernanceCase(
            case_name="Marketplace ranking rule",
            system_context="Rank sellers using relevance, price, delivery quality, reputation, and conversion signals.",
            strategic_goal="surface useful options while limiting ranking manipulation and unfair visibility concentration",
            agent_inventory=0.82,
            action_space_clarity=0.76,
            payoff_documentation=0.70,
            mechanism_documentation=0.72,
            incentive_alignment=0.64,
            manipulation_review=0.82,
            sensitivity_review=0.78,
            equilibrium_review=0.62,
            welfare_review=0.68,
            fairness_review=0.72,
            traceability=0.70,
            governance_review=0.68,
            communication_clarity=0.72,
        ),
        StrategicGovernanceCase(
            case_name="Congestion routing policy",
            system_context="Recommend routes across shared infrastructure where individual choices affect congestion.",
            strategic_goal="reduce total congestion while preserving user trust, fairness, and resilience",
            agent_inventory=0.80,
            action_space_clarity=0.82,
            payoff_documentation=0.78,
            mechanism_documentation=0.76,
            incentive_alignment=0.72,
            manipulation_review=0.62,
            sensitivity_review=0.84,
            equilibrium_review=0.82,
            welfare_review=0.86,
            fairness_review=0.70,
            traceability=0.76,
            governance_review=0.72,
            communication_clarity=0.74,
        ),
        StrategicGovernanceCase(
            case_name="Opaque engagement platform",
            system_context="Distribute visibility through hidden engagement metrics with weak strategic abuse review.",
            strategic_goal="maximize engagement",
            agent_inventory=0.48,
            action_space_clarity=0.34,
            payoff_documentation=0.24,
            mechanism_documentation=0.26,
            incentive_alignment=0.22,
            manipulation_review=0.18,
            sensitivity_review=0.20,
            equilibrium_review=0.16,
            welfare_review=0.18,
            fairness_review=0.20,
            traceability=0.24,
            governance_review=0.18,
            communication_clarity=0.34,
        ),
    ]


def run_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in build_cases():
        score = strategic_governance_score(case)
        risk = strategic_governance_risk(case)
        rows.append(
            {
                **asdict(case),
                "strategic_governance_score": round(score, 3),
                "strategic_governance_risk": round(risk, 3),
                "diagnostic": diagnose(score, risk),
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def summarize(audit_rows: list[dict[str, object]], equilibria: list[dict[str, object]], poa: dict[str, object], sensitivity_rows: list[dict[str, object]]) -> dict[str, object]:
    attractive_count = sum(1 for row in sensitivity_rows if row["manipulation_attractive"])
    return {
        "case_count": len(audit_rows),
        "average_strategic_governance_score": round(mean(float(row["strategic_governance_score"]) for row in audit_rows), 3),
        "average_strategic_governance_risk": round(mean(float(row["strategic_governance_risk"]) for row in audit_rows), 3),
        "highest_score_case": max(audit_rows, key=lambda row: float(row["strategic_governance_score"]))["case_name"],
        "highest_risk_case": max(audit_rows, key=lambda row: float(row["strategic_governance_risk"]))["case_name"],
        "pure_nash_equilibrium_count": len(equilibria),
        "welfare_price_of_anarchy": poa["welfare_price_of_anarchy"],
        "attractive_manipulation_scenarios": attractive_count,
        "interpretation": "Strategic governance depends on agent inventories, action-space clarity, payoff documentation, mechanism documentation, incentive alignment, manipulation review, sensitivity testing, equilibrium review, welfare analysis, fairness review, traceability, and governance.",
    }


def main() -> None:
    game = build_payoff_game()
    game_rows = payoff_table_rows(game)
    equilibria = pure_nash_equilibria(game)
    poa = price_of_anarchy(game)
    sensitivity_rows = incentive_sensitivity_examples()
    audit_rows = run_audit()
    summary = summarize(audit_rows, equilibria, poa, sensitivity_rows)
    write_csv(TABLES / "algorithmic_game_theory_strategic_governance_audit.csv", audit_rows)
    write_csv(TABLES / "algorithmic_game_theory_strategic_governance_summary.csv", [summary])
    write_csv(TABLES / "payoff_game_table.csv", game_rows)
    write_csv(TABLES / "pure_nash_equilibria.csv", equilibria)
    write_csv(TABLES / "incentive_sensitivity_examples.csv", sensitivity_rows)
    write_json(JSON_DIR / "algorithmic_game_theory_strategic_governance_audit.json", audit_rows)
    write_json(JSON_DIR / "algorithmic_game_theory_strategic_governance_summary.json", summary)
    write_json(JSON_DIR / "payoff_game_table.json", game_rows)
    write_json(JSON_DIR / "pure_nash_equilibria.json", equilibria)
    write_json(JSON_DIR / "price_of_anarchy.json", poa)
    write_json(JSON_DIR / "incentive_sensitivity_examples.json", sensitivity_rows)
    print("Algorithmic game theory and strategic behavior audit complete.")
    print(TABLES / "algorithmic_game_theory_strategic_governance_audit.csv")
    print(f"Pure Nash equilibria: {len(equilibria)}")
    print(f"Welfare price of anarchy: {poa['welfare_price_of_anarchy']}")


if __name__ == "__main__":
    main()
