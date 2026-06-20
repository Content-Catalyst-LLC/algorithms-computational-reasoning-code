# secure_computation_privacy_preserving_algorithms_audit.py
# Dependency-light workflow for auditing privacy-preserving computation.
# Educational examples only; not a production privacy or cryptography library.

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from random import Random
from statistics import mean
import csv
import json
import math

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class PrivacyPreservingCase:
    case_name: str
    system_context: str
    privacy_goal: str
    data_minimization: float
    threat_model_clarity: float
    method_fit: float
    parameter_documentation: float
    privacy_budget_governance: float
    secure_aggregation_review: float
    output_leakage_review: float
    reidentification_review: float
    utility_validation: float
    access_control: float
    audit_logging: float
    incident_response: float
    communication_clarity: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def privacy_governance_score(case: PrivacyPreservingCase) -> float:
    return clamp(
        100.0 * (
            0.09 * case.data_minimization
            + 0.10 * case.threat_model_clarity
            + 0.10 * case.method_fit
            + 0.09 * case.parameter_documentation
            + 0.10 * case.privacy_budget_governance
            + 0.08 * case.secure_aggregation_review
            + 0.09 * case.output_leakage_review
            + 0.09 * case.reidentification_review
            + 0.08 * case.utility_validation
            + 0.07 * case.access_control
            + 0.05 * case.audit_logging
            + 0.04 * case.incident_response
            + 0.02 * case.communication_clarity
        )
    )


def privacy_governance_risk(case: PrivacyPreservingCase) -> float:
    weak_points = [
        1.0 - case.data_minimization,
        1.0 - case.threat_model_clarity,
        1.0 - case.method_fit,
        1.0 - case.parameter_documentation,
        1.0 - case.privacy_budget_governance,
        1.0 - case.secure_aggregation_review,
        1.0 - case.output_leakage_review,
        1.0 - case.reidentification_review,
        1.0 - case.utility_validation,
        1.0 - case.access_control,
        1.0 - case.audit_logging,
        1.0 - case.incident_response,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong privacy-preserving computation governance"
    if score >= 70 and risk <= 35:
        return "usable privacy-preserving workflow with review needs"
    if risk >= 55:
        return "high risk; privacy method, threat model, budget, output leakage, re-identification, or governance may be weak"
    return "partial discipline; strengthen minimization, threat model, method fit, parameters, budget, output review, re-identification review, utility validation, access control, logging, and governance"


def laplace_noise(scale: float, rng: Random) -> float:
    # Inverse-CDF sampler for Laplace(0, scale).
    u = rng.random() - 0.5
    return -scale * math.copysign(math.log(1 - 2 * abs(u)), u)


def differentially_private_count(true_count: int, epsilon: float, sensitivity: float, seed: int = 42) -> dict[str, object]:
    rng = Random(seed)
    scale = sensitivity / epsilon
    noise = laplace_noise(scale, rng)
    noisy_count = true_count + noise

    return {
        "true_count": true_count,
        "epsilon": epsilon,
        "sensitivity": sensitivity,
        "laplace_scale": round(scale, 6),
        "noise": round(noise, 6),
        "noisy_count": round(noisy_count, 6),
        "absolute_error": round(abs(noisy_count - true_count), 6),
        "interpretation": "Lower epsilon increases the noise scale and can reduce precision while strengthening privacy."
    }


def privacy_budget_ledger() -> list[dict[str, object]]:
    releases = [
        {"release": "aggregate_count_by_region", "epsilon": 0.25, "purpose": "public reporting"},
        {"release": "aggregate_count_by_age_band", "epsilon": 0.20, "purpose": "equity analysis"},
        {"release": "aggregate_count_by_program", "epsilon": 0.30, "purpose": "operations planning"},
        {"release": "aggregate_outcome_rate", "epsilon": 0.25, "purpose": "performance monitoring"},
    ]

    cumulative = 0.0
    rows: list[dict[str, object]] = []

    for release in releases:
        cumulative += float(release["epsilon"])
        rows.append({
            **release,
            "cumulative_epsilon": round(cumulative, 6),
        })

    return rows


def toy_secure_aggregation() -> list[dict[str, object]]:
    # Educational masking example: masks cancel in the aggregate.
    participants = [
        {"participant": "site_a", "private_value": 18, "mask": 7},
        {"participant": "site_b", "private_value": 24, "mask": -3},
        {"participant": "site_c", "private_value": 15, "mask": -4},
    ]

    rows: list[dict[str, object]] = []

    for item in participants:
        masked_value = int(item["private_value"]) + int(item["mask"])
        rows.append({
            **item,
            "masked_value_sent": masked_value,
        })

    aggregate_private_value = sum(int(item["private_value"]) for item in participants)
    aggregate_masked_value = sum(int(item["masked_value_sent"]) for item in rows)
    aggregate_mask = sum(int(item["mask"]) for item in participants)

    rows.append({
        "participant": "aggregate",
        "private_value": aggregate_private_value,
        "mask": aggregate_mask,
        "masked_value_sent": aggregate_masked_value,
    })

    return rows


def federated_averaging_demo() -> list[dict[str, object]]:
    local_models = [
        {"client": "client_a", "examples": 100, "local_weight": 0.42},
        {"client": "client_b", "examples": 240, "local_weight": 0.55},
        {"client": "client_c", "examples": 160, "local_weight": 0.49},
    ]

    total_examples = sum(int(row["examples"]) for row in local_models)
    weighted_sum = sum(int(row["examples"]) * float(row["local_weight"]) for row in local_models)
    global_weight = weighted_sum / total_examples

    rows: list[dict[str, object]] = []

    for row in local_models:
        rows.append({
            **row,
            "client_share": round(int(row["examples"]) / total_examples, 6),
            "weighted_contribution": round(int(row["examples"]) * float(row["local_weight"]) / total_examples, 6),
        })

    rows.append({
        "client": "global_model",
        "examples": total_examples,
        "local_weight": round(global_weight, 6),
        "client_share": 1.0,
        "weighted_contribution": round(global_weight, 6),
    })

    return rows


def reidentification_risk_review() -> list[dict[str, object]]:
    groups = [
        {"group": "large_urban_region", "cell_count": 1280, "attribute_rarity": 0.10},
        {"group": "mid_sized_program", "cell_count": 185, "attribute_rarity": 0.22},
        {"group": "small_rural_region", "cell_count": 18, "attribute_rarity": 0.55},
        {"group": "rare_condition_group", "cell_count": 6, "attribute_rarity": 0.90},
    ]

    rows: list[dict[str, object]] = []

    for group in groups:
        count = int(group["cell_count"])
        rarity = float(group["attribute_rarity"])
        small_cell_risk = 1.0 if count < 10 else 0.65 if count < 25 else 0.25 if count < 100 else 0.05
        risk_score = clamp(100.0 * (0.65 * small_cell_risk + 0.35 * rarity))
        rows.append({
            **group,
            "small_cell_risk": round(small_cell_risk, 3),
            "reidentification_risk_score": round(risk_score, 3),
            "review_recommendation": "suppress or aggregate" if risk_score >= 70 else "review" if risk_score >= 35 else "standard release controls",
        })

    return rows


def build_cases() -> list[PrivacyPreservingCase]:
    return [
        PrivacyPreservingCase(
            case_name="Differentially private public statistics",
            system_context="Agency releases aggregate statistics with documented privacy budget and utility analysis.",
            privacy_goal="reduce individual disclosure risk while preserving useful public reporting",
            data_minimization=0.84,
            threat_model_clarity=0.86,
            method_fit=0.88,
            parameter_documentation=0.86,
            privacy_budget_governance=0.90,
            secure_aggregation_review=0.62,
            output_leakage_review=0.84,
            reidentification_review=0.86,
            utility_validation=0.82,
            access_control=0.78,
            audit_logging=0.80,
            incident_response=0.74,
            communication_clarity=0.82,
        ),
        PrivacyPreservingCase(
            case_name="Federated learning with secure aggregation",
            system_context="Distributed model training where local data remains on participating devices or sites.",
            privacy_goal="reduce raw-data centralization while limiting update exposure",
            data_minimization=0.82,
            threat_model_clarity=0.78,
            method_fit=0.82,
            parameter_documentation=0.76,
            privacy_budget_governance=0.64,
            secure_aggregation_review=0.88,
            output_leakage_review=0.74,
            reidentification_review=0.70,
            utility_validation=0.80,
            access_control=0.78,
            audit_logging=0.72,
            incident_response=0.68,
            communication_clarity=0.74,
        ),
        PrivacyPreservingCase(
            case_name="Private set intersection collaboration",
            system_context="Two institutions compare records to identify overlap without exchanging full lists.",
            privacy_goal="compute set overlap while limiting exposure of nonmatching records",
            data_minimization=0.78,
            threat_model_clarity=0.76,
            method_fit=0.80,
            parameter_documentation=0.70,
            privacy_budget_governance=0.52,
            secure_aggregation_review=0.60,
            output_leakage_review=0.78,
            reidentification_review=0.74,
            utility_validation=0.70,
            access_control=0.76,
            audit_logging=0.72,
            incident_response=0.66,
            communication_clarity=0.70,
        ),
        PrivacyPreservingCase(
            case_name="Informal anonymized data release",
            system_context="Dataset is released after direct identifiers are removed, without formal privacy analysis.",
            privacy_goal="share useful data while claiming anonymity",
            data_minimization=0.38,
            threat_model_clarity=0.24,
            method_fit=0.20,
            parameter_documentation=0.14,
            privacy_budget_governance=0.08,
            secure_aggregation_review=0.10,
            output_leakage_review=0.22,
            reidentification_review=0.18,
            utility_validation=0.42,
            access_control=0.30,
            audit_logging=0.20,
            incident_response=0.18,
            communication_clarity=0.28,
        ),
    ]


def run_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    for case in build_cases():
        score = privacy_governance_score(case)
        risk = privacy_governance_risk(case)
        rows.append({
            **asdict(case),
            "privacy_governance_score": round(score, 3),
            "privacy_governance_risk": round(risk, 3),
            "diagnostic": diagnose(score, risk),
        })

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


def summarize(
    audit_rows: list[dict[str, object]],
    dp_result: dict[str, object],
    budget_rows: list[dict[str, object]],
    secure_rows: list[dict[str, object]],
    fed_rows: list[dict[str, object]],
    risk_rows: list[dict[str, object]],
) -> dict[str, object]:
    high_reidentification_risk = sum(1 for row in risk_rows if float(row["reidentification_risk_score"]) >= 70)
    final_epsilon = budget_rows[-1]["cumulative_epsilon"] if budget_rows else 0.0
    aggregate_row = next(row for row in secure_rows if row["participant"] == "aggregate")
    global_row = next(row for row in fed_rows if row["client"] == "global_model")

    return {
        "case_count": len(audit_rows),
        "average_privacy_governance_score": round(mean(float(row["privacy_governance_score"]) for row in audit_rows), 3),
        "average_privacy_governance_risk": round(mean(float(row["privacy_governance_risk"]) for row in audit_rows), 3),
        "highest_score_case": max(audit_rows, key=lambda row: float(row["privacy_governance_score"]))["case_name"],
        "highest_risk_case": max(audit_rows, key=lambda row: float(row["privacy_governance_risk"]))["case_name"],
        "dp_noisy_count": dp_result["noisy_count"],
        "dp_absolute_error": dp_result["absolute_error"],
        "final_cumulative_epsilon": final_epsilon,
        "secure_aggregate_value": aggregate_row["private_value"],
        "federated_global_weight": global_row["local_weight"],
        "high_reidentification_risk_cells": high_reidentification_risk,
        "interpretation": "Privacy-preserving computation depends on data minimization, threat models, method fit, parameter documentation, privacy budgets, secure aggregation, output review, re-identification analysis, utility validation, access controls, audit logs, incident response, and clear communication of limits."
    }


def main() -> None:
    dp_result = differentially_private_count(true_count=248, epsilon=0.5, sensitivity=1.0)
    budget_rows = privacy_budget_ledger()
    secure_rows = toy_secure_aggregation()
    fed_rows = federated_averaging_demo()
    risk_rows = reidentification_risk_review()
    audit_rows = run_audit()
    summary = summarize(audit_rows, dp_result, budget_rows, secure_rows, fed_rows, risk_rows)

    write_csv(TABLES / "privacy_preserving_governance_audit.csv", audit_rows)
    write_csv(TABLES / "privacy_preserving_governance_summary.csv", [summary])
    write_csv(TABLES / "differential_privacy_count_demo.csv", [dp_result])
    write_csv(TABLES / "privacy_budget_ledger.csv", budget_rows)
    write_csv(TABLES / "toy_secure_aggregation.csv", secure_rows)
    write_csv(TABLES / "federated_averaging_demo.csv", fed_rows)
    write_csv(TABLES / "reidentification_risk_review.csv", risk_rows)

    write_json(JSON_DIR / "privacy_preserving_governance_audit.json", audit_rows)
    write_json(JSON_DIR / "privacy_preserving_governance_summary.json", summary)
    write_json(JSON_DIR / "differential_privacy_count_demo.json", dp_result)
    write_json(JSON_DIR / "privacy_budget_ledger.json", budget_rows)
    write_json(JSON_DIR / "toy_secure_aggregation.json", secure_rows)
    write_json(JSON_DIR / "federated_averaging_demo.json", fed_rows)
    write_json(JSON_DIR / "reidentification_risk_review.json", risk_rows)

    print("Secure computation and privacy-preserving algorithms audit complete.")
    print(TABLES / "privacy_preserving_governance_audit.csv")


if __name__ == "__main__":
    main()
