from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
import csv
import json
import math
import random

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"
LOGS = ARTICLE_ROOT / "outputs" / "logs"
DATA_DIR = ARTICLE_ROOT / "data"


@dataclass(frozen=True)
class CounterfactualConfig:
    article: str
    seed: int
    n: int
    decision_threshold: float
    review_band_low: float
    max_counterfactual_delta: float
    step: float


@dataclass(frozen=True)
class FeatureRule:
    feature: str
    allowed_for_recourse: bool
    min_value: float
    max_value: float
    unit_cost: float
    reason: str


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def sigmoid(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


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


def read_feature_rules() -> dict[str, FeatureRule]:
    path = DATA_DIR / "allowed_feature_changes.csv"
    rules: dict[str, FeatureRule] = {}
    with path.open("r", newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            rules[row["feature"]] = FeatureRule(
                feature=row["feature"],
                allowed_for_recourse=row["allowed_for_recourse"].strip().lower() == "true",
                min_value=float(row["min_value"]),
                max_value=float(row["max_value"]),
                unit_cost=float(row["unit_cost"]),
                reason=row["reason"],
            )
    return rules


def default_config() -> CounterfactualConfig:
    return CounterfactualConfig(
        article="counterfactual_reasoning_in_algorithmic_systems",
        seed=2026,
        n=500,
        decision_threshold=0.62,
        review_band_low=0.52,
        max_counterfactual_delta=0.40,
        step=0.05,
    )


def score_case(row: dict[str, float]) -> float:
    # A transparent synthetic decision score. This is intentionally simple.
    raw = (
        -1.10
        + 1.45 * row["baseline_score"]
        + 1.20 * row["document_quality"]
        + 0.80 * row["timeliness"]
        - 0.55 * row["prior_flag"]
        - 0.70 * row["access_constraint"]
        + 0.55 * row["risk_adjustment"]
    )
    return sigmoid(raw)


def decision_label(score: float, config: CounterfactualConfig) -> str:
    if score >= config.decision_threshold:
        return "favorable"
    if score >= config.review_band_low:
        return "review"
    return "unfavorable"


def generate_synthetic_decisions(config: CounterfactualConfig) -> list[dict[str, object]]:
    rng = random.Random(config.seed)
    rows: list[dict[str, object]] = []
    for case_id in range(1, config.n + 1):
        access_constraint = 1.0 if rng.random() < 0.28 else 0.0
        prior_flag = 1.0 if rng.random() < 0.22 else 0.0
        baseline_score = clamp(rng.gauss(0.58 - 0.18 * access_constraint - 0.08 * prior_flag, 0.18))
        document_quality = clamp(rng.gauss(0.60 - 0.20 * access_constraint + 0.10 * baseline_score, 0.18))
        timeliness = clamp(rng.gauss(0.62 - 0.18 * access_constraint, 0.20))
        risk_adjustment = clamp(rng.gauss(0.50 + 0.10 * baseline_score - 0.06 * prior_flag, 0.16))
        features = {
            "baseline_score": baseline_score,
            "document_quality": document_quality,
            "timeliness": timeliness,
            "prior_flag": prior_flag,
            "access_constraint": access_constraint,
            "risk_adjustment": risk_adjustment,
        }
        score = score_case(features)
        rows.append({
            "case_id": case_id,
            **{key: round(value, 6) for key, value in features.items()},
            "decision_score": round(score, 6),
            "decision": decision_label(score, config),
            "threshold": config.decision_threshold,
            "interpretation": "Synthetic decision record for testing counterfactual reasoning, recourse, and feasibility review.",
        })
    return rows


def candidate_counterfactuals(
    rows: list[dict[str, object]],
    config: CounterfactualConfig,
    rules: dict[str, FeatureRule],
) -> list[dict[str, object]]:
    candidates: list[dict[str, object]] = []
    steps = [round(config.step * i, 2) for i in range(1, int(config.max_counterfactual_delta / config.step) + 1)]
    for row in rows:
        original_features = {key: float(row[key]) for key in rules.keys()}
        original_score = float(row["decision_score"])
        original_decision = str(row["decision"])
        for feature, rule in rules.items():
            for delta in steps:
                proposed = dict(original_features)
                proposed[feature] = clamp(proposed[feature] + delta, rule.min_value, rule.max_value)
                if proposed[feature] == original_features[feature]:
                    continue
                new_score = score_case(proposed)
                new_decision = decision_label(new_score, config)
                flipped = original_decision != "favorable" and new_decision == "favorable"
                candidates.append({
                    "case_id": row["case_id"],
                    "original_decision": original_decision,
                    "original_score": round(original_score, 6),
                    "counterfactual_feature": feature,
                    "original_value": round(original_features[feature], 6),
                    "counterfactual_value": round(proposed[feature], 6),
                    "delta": round(proposed[feature] - original_features[feature], 6),
                    "counterfactual_score": round(new_score, 6),
                    "counterfactual_decision": new_decision,
                    "score_change": round(new_score - original_score, 6),
                    "flipped_to_favorable": flipped,
                    "allowed_for_recourse": rule.allowed_for_recourse,
                    "recourse_cost": round(abs(proposed[feature] - original_features[feature]) * rule.unit_cost, 6),
                    "feasibility_note": rule.reason,
                })
    return candidates


def minimal_recourse(candidates: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[int, list[dict[str, object]]] = {}
    for row in candidates:
        if bool(row["flipped_to_favorable"]) and bool(row["allowed_for_recourse"]):
            grouped.setdefault(int(row["case_id"]), []).append(row)
    minimal: list[dict[str, object]] = []
    for case_id, rows in grouped.items():
        best = sorted(rows, key=lambda r: (float(r["recourse_cost"]), float(r["delta"]), str(r["counterfactual_feature"])))[0]
        minimal.append({
            "case_id": case_id,
            "recommended_feature": best["counterfactual_feature"],
            "original_value": best["original_value"],
            "counterfactual_value": best["counterfactual_value"],
            "delta": best["delta"],
            "original_score": best["original_score"],
            "counterfactual_score": best["counterfactual_score"],
            "recourse_cost": best["recourse_cost"],
            "interpretation": "Lowest-cost single-feature feasible counterfactual that flips the synthetic decision to favorable.",
        })
    return sorted(minimal, key=lambda r: int(r["case_id"]))


def feasibility_review(candidates: list[dict[str, object]]) -> list[dict[str, object]]:
    summary: dict[str, dict[str, object]] = {}
    for row in candidates:
        feature = str(row["counterfactual_feature"])
        item = summary.setdefault(feature, {
            "feature": feature,
            "candidate_count": 0,
            "flip_count": 0,
            "allowed_for_recourse": row["allowed_for_recourse"],
            "average_cost_for_flips": 0.0,
            "feasibility_note": row["feasibility_note"],
            "_costs": [],
        })
        item["candidate_count"] = int(item["candidate_count"]) + 1
        if bool(row["flipped_to_favorable"]):
            item["flip_count"] = int(item["flip_count"]) + 1
            item["_costs"].append(float(row["recourse_cost"]))
    rows: list[dict[str, object]] = []
    for item in summary.values():
        costs = item.pop("_costs")
        item["average_cost_for_flips"] = round(mean(costs), 6) if costs else None
        item["governance_status"] = "actionable_candidate" if item["allowed_for_recourse"] else "do_not_present_as_recourse"
        rows.append(item)
    return sorted(rows, key=lambda r: str(r["feature"]))


def threshold_sensitivity(rows: list[dict[str, object]], config: CounterfactualConfig) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    thresholds = [round(0.50 + 0.02 * i, 2) for i in range(0, 11)]
    for threshold in thresholds:
        favorable = sum(1 for row in rows if float(row["decision_score"]) >= threshold)
        review = sum(1 for row in rows if config.review_band_low <= float(row["decision_score"]) < threshold)
        unfavorable = len(rows) - favorable - review
        output.append({
            "threshold": threshold,
            "favorable_count": favorable,
            "review_count": review,
            "unfavorable_count": unfavorable,
            "favorable_share": round(favorable / len(rows), 6),
            "interpretation": "Changing the decision threshold changes outcomes even when underlying cases do not change.",
        })
    return output


def audit_summary(
    rows: list[dict[str, object]],
    candidates: list[dict[str, object]],
    minimal: list[dict[str, object]],
    feasibility: list[dict[str, object]],
    config: CounterfactualConfig,
) -> dict[str, object]:
    unfavorable_or_review = [row for row in rows if row["decision"] != "favorable"]
    feasible_flip_cases = {int(row["case_id"]) for row in minimal}
    non_actionable_flip_count = sum(
        1 for row in candidates
        if bool(row["flipped_to_favorable"]) and not bool(row["allowed_for_recourse"])
    )
    return {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "n_cases": len(rows),
        "decision_threshold": config.decision_threshold,
        "favorable_count": sum(1 for row in rows if row["decision"] == "favorable"),
        "review_count": sum(1 for row in rows if row["decision"] == "review"),
        "unfavorable_count": sum(1 for row in rows if row["decision"] == "unfavorable"),
        "counterfactual_candidate_count": len(candidates),
        "candidate_flip_count": sum(1 for row in candidates if bool(row["flipped_to_favorable"])),
        "non_actionable_flip_count": non_actionable_flip_count,
        "cases_with_feasible_single_feature_recourse": len(feasible_flip_cases),
        "share_of_nonfavorable_cases_with_feasible_recourse": round(len(feasible_flip_cases) / max(1, len(unfavorable_or_review)), 6),
        "features_marked_do_not_present_as_recourse": [row["feature"] for row in feasibility if row["governance_status"] == "do_not_present_as_recourse"],
        "interpretation": "Counterfactual reasoning should distinguish decision-flipping mathematical alternatives from feasible, causal, contestable, and responsible recourse explanations.",
    }


def main() -> None:
    config = default_config()
    rules = read_feature_rules()
    rows = generate_synthetic_decisions(config)
    candidates = candidate_counterfactuals(rows, config, rules)
    minimal = minimal_recourse(candidates)
    feasibility = feasibility_review(candidates)
    thresholds = threshold_sensitivity(rows, config)
    summary = audit_summary(rows, candidates, minimal, feasibility, config)

    write_csv(TABLES / "synthetic_algorithmic_decisions.csv", rows)
    write_csv(TABLES / "counterfactual_candidates.csv", candidates)
    write_csv(TABLES / "minimal_recourse_actions.csv", minimal)
    write_csv(TABLES / "feasibility_review.csv", feasibility)
    write_csv(TABLES / "threshold_sensitivity.csv", thresholds)
    write_csv(TABLES / "counterfactual_audit_summary.csv", [summary])

    write_json(JSON_DIR / "counterfactual_config.json", asdict(config))
    write_json(JSON_DIR / "counterfactual_candidates.json", candidates[:500])
    write_json(JSON_DIR / "minimal_recourse_actions.json", minimal)
    write_json(JSON_DIR / "feasibility_review.json", feasibility)
    write_json(JSON_DIR / "counterfactual_audit_summary.json", summary)
    write_json(LOGS / "workflow_manifest.json", {
        "generated_at": timestamp_utc(),
        "workflow": "counterfactual_reasoning_audit_workflow",
        "outputs": [
            "synthetic_algorithmic_decisions.csv",
            "counterfactual_candidates.csv",
            "minimal_recourse_actions.csv",
            "feasibility_review.csv",
            "threshold_sensitivity.csv",
            "counterfactual_audit_summary.json",
        ],
        "synthetic_only": True,
    })

    print("Counterfactual reasoning audit complete.")
    print(TABLES / "counterfactual_audit_summary.csv")


if __name__ == "__main__":
    main()
