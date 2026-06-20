#!/usr/bin/env python3
"""Audit multi-objective optimization and trade-off reasoning workflows.

The workflow is intentionally dependency-light. It identifies Pareto-efficient
alternatives, computes weighted scores, and scores governance readiness for
trade-off decisions.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import json

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"

MINIMIZE = {"cost", "risk", "emissions", "burden"}
MAXIMIZE = {"service_quality", "access", "robustness"}


@dataclass(frozen=True)
class TradeOffGovernanceCase:
    case_name: str
    decision_context: str
    tradeoff_goal: str
    objective_inventory: float
    metric_validity: float
    weight_documentation: float
    constraint_clarity: float
    pareto_analysis: float
    sensitivity_review: float
    robustness_review: float
    fairness_review: float
    stakeholder_review: float
    traceability: float
    governance_review: float
    communication_clarity: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def tradeoff_governance_score(case: TradeOffGovernanceCase) -> float:
    return clamp(
        100.0
        * (
            0.10 * case.objective_inventory
            + 0.09 * case.metric_validity
            + 0.09 * case.weight_documentation
            + 0.09 * case.constraint_clarity
            + 0.10 * case.pareto_analysis
            + 0.10 * case.sensitivity_review
            + 0.09 * case.robustness_review
            + 0.10 * case.fairness_review
            + 0.09 * case.stakeholder_review
            + 0.07 * case.traceability
            + 0.06 * case.governance_review
            + 0.02 * case.communication_clarity
        )
    )


def tradeoff_governance_risk(case: TradeOffGovernanceCase) -> float:
    weak_points = [
        1.0 - case.objective_inventory,
        1.0 - case.metric_validity,
        1.0 - case.weight_documentation,
        1.0 - case.constraint_clarity,
        1.0 - case.pareto_analysis,
        1.0 - case.sensitivity_review,
        1.0 - case.robustness_review,
        1.0 - case.fairness_review,
        1.0 - case.stakeholder_review,
        1.0 - case.traceability,
        1.0 - case.governance_review,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong trade-off governance"
    if score >= 70 and risk <= 35:
        return "usable multi-objective process with review needs"
    if risk >= 55:
        return "high risk; objectives, weights, constraints, Pareto analysis, sensitivity, fairness, stakeholders, or governance may be underdefined"
    return "partial discipline; strengthen objectives, metrics, weights, constraints, sensitivity, fairness, stakeholder review, traceability, and governance"


def build_alternatives() -> list[dict[str, object]]:
    return [
        {"alternative": "A", "cost": 72, "risk": 34, "emissions": 42, "service_quality": 82, "access": 76, "robustness": 71, "burden": 28},
        {"alternative": "B", "cost": 64, "risk": 41, "emissions": 38, "service_quality": 76, "access": 70, "robustness": 66, "burden": 34},
        {"alternative": "C", "cost": 81, "risk": 26, "emissions": 35, "service_quality": 88, "access": 82, "robustness": 78, "burden": 22},
        {"alternative": "D", "cost": 58, "risk": 52, "emissions": 50, "service_quality": 69, "access": 63, "robustness": 58, "burden": 46},
        {"alternative": "E", "cost": 70, "risk": 31, "emissions": 30, "service_quality": 80, "access": 79, "robustness": 74, "burden": 26},
        {"alternative": "F", "cost": 90, "risk": 24, "emissions": 28, "service_quality": 91, "access": 84, "robustness": 82, "burden": 20},
        {"alternative": "G", "cost": 62, "risk": 39, "emissions": 36, "service_quality": 75, "access": 77, "robustness": 67, "burden": 30},
    ]


def dominates(a: dict[str, object], b: dict[str, object], objectives: list[str]) -> bool:
    no_worse = True
    strictly_better = False

    for objective in objectives:
        av = float(a[objective])
        bv = float(b[objective])
        if objective in MINIMIZE:
            if av > bv:
                no_worse = False
            if av < bv:
                strictly_better = True
        elif objective in MAXIMIZE:
            if av < bv:
                no_worse = False
            if av > bv:
                strictly_better = True
        else:
            raise ValueError(f"Unknown objective direction for {objective}")

    return no_worse and strictly_better


def mark_pareto(alternatives: list[dict[str, object]], objectives: list[str]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for candidate in alternatives:
        dominated_by: list[str] = []
        for challenger in alternatives:
            if challenger["alternative"] == candidate["alternative"]:
                continue
            if dominates(challenger, candidate, objectives):
                dominated_by.append(str(challenger["alternative"]))
        rows.append({**candidate, "pareto_efficient": len(dominated_by) == 0, "dominated_by": ",".join(dominated_by)})
    return rows


def normalize(value: float, values: list[float], direction: str) -> float:
    low = min(values)
    high = max(values)
    if high == low:
        return 1.0
    if direction == "min":
        return (high - value) / (high - low)
    if direction == "max":
        return (value - low) / (high - low)
    raise ValueError(direction)


def weighted_scores(alternatives: list[dict[str, object]], weights: dict[str, float]) -> list[dict[str, object]]:
    objectives = list(weights.keys())
    value_lists = {objective: [float(row[objective]) for row in alternatives] for objective in objectives}
    rows: list[dict[str, object]] = []

    for row in alternatives:
        score = 0.0
        components: dict[str, float] = {}
        for objective, weight in weights.items():
            direction = "min" if objective in MINIMIZE else "max"
            normalized_value = normalize(float(row[objective]), value_lists[objective], direction)
            components[f"normalized_{objective}"] = round(normalized_value, 6)
            score += weight * normalized_value
        rows.append({"alternative": row["alternative"], "weighted_score": round(score, 6), **components})

    return sorted(rows, key=lambda item: float(item["weighted_score"]), reverse=True)


def build_cases() -> list[TradeOffGovernanceCase]:
    return [
        TradeOffGovernanceCase(
            case_name="Public infrastructure planning",
            decision_context="Balance cost, reliability, access, climate resilience, service quality, and distributional burden.",
            tradeoff_goal="choose a resilient investment portfolio while documenting trade-offs and affected communities",
            objective_inventory=0.88,
            metric_validity=0.82,
            weight_documentation=0.78,
            constraint_clarity=0.84,
            pareto_analysis=0.82,
            sensitivity_review=0.80,
            robustness_review=0.86,
            fairness_review=0.84,
            stakeholder_review=0.82,
            traceability=0.80,
            governance_review=0.84,
            communication_clarity=0.78,
        ),
        TradeOffGovernanceCase(
            case_name="Machine learning threshold policy",
            decision_context="Balance precision, recall, calibration, fairness, review burden, and decision latency.",
            tradeoff_goal="select threshold and review policy with explicit error-cost and fairness analysis",
            objective_inventory=0.84,
            metric_validity=0.80,
            weight_documentation=0.72,
            constraint_clarity=0.76,
            pareto_analysis=0.78,
            sensitivity_review=0.82,
            robustness_review=0.76,
            fairness_review=0.86,
            stakeholder_review=0.70,
            traceability=0.78,
            governance_review=0.80,
            communication_clarity=0.74,
        ),
        TradeOffGovernanceCase(
            case_name="Recommendation diversity policy",
            decision_context="Balance relevance, diversity, novelty, freshness, safety, exposure, and user satisfaction.",
            tradeoff_goal="avoid narrow relevance optimization while preserving useful discovery and accountable visibility",
            objective_inventory=0.78,
            metric_validity=0.70,
            weight_documentation=0.62,
            constraint_clarity=0.68,
            pareto_analysis=0.66,
            sensitivity_review=0.64,
            robustness_review=0.60,
            fairness_review=0.72,
            stakeholder_review=0.62,
            traceability=0.66,
            governance_review=0.68,
            communication_clarity=0.70,
        ),
        TradeOffGovernanceCase(
            case_name="Opaque weighted-score allocation",
            decision_context="Rank allocation options using unexplained weights and incomplete stakeholder review.",
            tradeoff_goal="select highest composite score",
            objective_inventory=0.42,
            metric_validity=0.34,
            weight_documentation=0.18,
            constraint_clarity=0.28,
            pareto_analysis=0.20,
            sensitivity_review=0.16,
            robustness_review=0.18,
            fairness_review=0.22,
            stakeholder_review=0.14,
            traceability=0.24,
            governance_review=0.20,
            communication_clarity=0.36,
        ),
    ]


def run_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in build_cases():
        score = tradeoff_governance_score(case)
        risk = tradeoff_governance_risk(case)
        rows.append({**asdict(case), "tradeoff_governance_score": round(score, 3), "tradeoff_governance_risk": round(risk, 3), "diagnostic": diagnose(score, risk)})
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


def summarize(rows: list[dict[str, object]], pareto_rows: list[dict[str, object]], weighted_rows: list[dict[str, object]]) -> dict[str, object]:
    efficient = [row["alternative"] for row in pareto_rows if row["pareto_efficient"]]
    top_weighted = weighted_rows[0]["alternative"] if weighted_rows else ""
    return {
        "case_count": len(rows),
        "average_tradeoff_governance_score": round(mean(float(row["tradeoff_governance_score"]) for row in rows), 3),
        "average_tradeoff_governance_risk": round(mean(float(row["tradeoff_governance_risk"]) for row in rows), 3),
        "highest_score_case": max(rows, key=lambda row: float(row["tradeoff_governance_score"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["tradeoff_governance_risk"]))["case_name"],
        "pareto_efficient_alternatives": ",".join(str(item) for item in efficient),
        "top_weighted_alternative": top_weighted,
        "interpretation": "Multi-objective governance depends on objective inventories, valid metrics, documented weights, clear constraints, Pareto analysis, sensitivity review, robustness review, fairness review, stakeholder review, traceability, governance, and communication clarity.",
    }


def main() -> None:
    alternatives = build_alternatives()
    objectives = ["cost", "risk", "emissions", "service_quality", "access", "robustness", "burden"]
    pareto_rows = mark_pareto(alternatives, objectives)
    balanced_weights = {"cost": 0.15, "risk": 0.15, "emissions": 0.15, "service_quality": 0.15, "access": 0.15, "robustness": 0.15, "burden": 0.10}
    weighted_rows = weighted_scores(alternatives, balanced_weights)
    audit_rows = run_audit()
    summary = summarize(audit_rows, pareto_rows, weighted_rows)

    write_csv(TABLES / "multi_objective_tradeoff_governance_audit.csv", audit_rows)
    write_csv(TABLES / "multi_objective_tradeoff_governance_summary.csv", [summary])
    write_csv(TABLES / "multi_objective_alternatives.csv", alternatives)
    write_csv(TABLES / "multi_objective_pareto_analysis.csv", pareto_rows)
    write_csv(TABLES / "multi_objective_weighted_scores.csv", weighted_rows)

    write_json(JSON_DIR / "multi_objective_tradeoff_governance_audit.json", audit_rows)
    write_json(JSON_DIR / "multi_objective_tradeoff_governance_summary.json", summary)
    write_json(JSON_DIR / "multi_objective_alternatives.json", alternatives)
    write_json(JSON_DIR / "multi_objective_pareto_analysis.json", pareto_rows)
    write_json(JSON_DIR / "multi_objective_weighted_scores.json", weighted_rows)

    print("Multi-objective optimization and trade-off audit complete.")
    print(TABLES / "multi_objective_tradeoff_governance_audit.csv")


if __name__ == "__main__":
    main()
