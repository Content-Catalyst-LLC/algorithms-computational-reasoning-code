# adversarial_thinking_computational_systems_audit.py
# Dependency-light workflow for adversarial risk and defense review.

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import json
import math
import random

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class AdversarialSystemCase:
    case_name: str
    system_context: str
    primary_adversary: str
    threat_model_clarity: float
    attack_surface_mapping: float
    trust_boundary_review: float
    abuse_case_coverage: float
    input_validation: float
    monitoring_detection: float
    defense_in_depth: float
    incident_response: float
    red_team_testing: float
    false_positive_review: float
    governance_ownership: float
    communication_clarity: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def adversarial_readiness_score(case: AdversarialSystemCase) -> float:
    return clamp(
        100.0 * (
            0.10 * case.threat_model_clarity
            + 0.10 * case.attack_surface_mapping
            + 0.09 * case.trust_boundary_review
            + 0.10 * case.abuse_case_coverage
            + 0.08 * case.input_validation
            + 0.10 * case.monitoring_detection
            + 0.10 * case.defense_in_depth
            + 0.09 * case.incident_response
            + 0.08 * case.red_team_testing
            + 0.07 * case.false_positive_review
            + 0.07 * case.governance_ownership
            + 0.02 * case.communication_clarity
        )
    )


def adversarial_risk_score(case: AdversarialSystemCase) -> float:
    weak_points = [
        1.0 - case.threat_model_clarity,
        1.0 - case.attack_surface_mapping,
        1.0 - case.trust_boundary_review,
        1.0 - case.abuse_case_coverage,
        1.0 - case.input_validation,
        1.0 - case.monitoring_detection,
        1.0 - case.defense_in_depth,
        1.0 - case.incident_response,
        1.0 - case.red_team_testing,
        1.0 - case.false_positive_review,
        1.0 - case.governance_ownership,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong adversarial readiness"
    if score >= 70 and risk <= 35:
        return "usable adversarial posture with review needs"
    if risk >= 55:
        return "high risk; threat model, attack surface, abuse cases, monitoring, defense depth, or governance may be weak"
    return "partial readiness; strengthen threat modeling, abuse-case analysis, monitoring, red teaming, incident response, and governance"


def build_cases() -> list[AdversarialSystemCase]:
    return [
        AdversarialSystemCase(
            case_name="Fraud detection platform",
            system_context="Transaction-scoring system facing adaptive fraud patterns.",
            primary_adversary="fraud network",
            threat_model_clarity=0.86,
            attack_surface_mapping=0.82,
            trust_boundary_review=0.78,
            abuse_case_coverage=0.84,
            input_validation=0.80,
            monitoring_detection=0.88,
            defense_in_depth=0.82,
            incident_response=0.80,
            red_team_testing=0.76,
            false_positive_review=0.72,
            governance_ownership=0.78,
            communication_clarity=0.74,
        ),
        AdversarialSystemCase(
            case_name="AI assistant with tool access",
            system_context="Language-model assistant can retrieve documents and call approved workflow tools.",
            primary_adversary="prompt injector or malicious document",
            threat_model_clarity=0.78,
            attack_surface_mapping=0.82,
            trust_boundary_review=0.84,
            abuse_case_coverage=0.80,
            input_validation=0.72,
            monitoring_detection=0.70,
            defense_in_depth=0.78,
            incident_response=0.66,
            red_team_testing=0.82,
            false_positive_review=0.68,
            governance_ownership=0.74,
            communication_clarity=0.76,
        ),
        AdversarialSystemCase(
            case_name="Content ranking system",
            system_context="Recommendation and ranking system shaped by engagement signals.",
            primary_adversary="coordinated manipulation network",
            threat_model_clarity=0.72,
            attack_surface_mapping=0.76,
            trust_boundary_review=0.68,
            abuse_case_coverage=0.74,
            input_validation=0.64,
            monitoring_detection=0.76,
            defense_in_depth=0.68,
            incident_response=0.62,
            red_team_testing=0.58,
            false_positive_review=0.70,
            governance_ownership=0.66,
            communication_clarity=0.62,
        ),
        AdversarialSystemCase(
            case_name="Unreviewed public form automation",
            system_context="Public form triggers automated routing and downstream decisions.",
            primary_adversary="spam, abuse, or malicious submitter",
            threat_model_clarity=0.28,
            attack_surface_mapping=0.34,
            trust_boundary_review=0.30,
            abuse_case_coverage=0.22,
            input_validation=0.38,
            monitoring_detection=0.24,
            defense_in_depth=0.20,
            incident_response=0.18,
            red_team_testing=0.10,
            false_positive_review=0.24,
            governance_ownership=0.22,
            communication_clarity=0.30,
        ),
    ]


def threshold_evasion_demo() -> list[dict[str, object]]:
    threshold = 0.70
    examples = [
        {"case_id": "ordinary_low_risk", "original_score": 0.42, "adversarial_shift": 0.00},
        {"case_id": "near_threshold_evasion", "original_score": 0.72, "adversarial_shift": -0.05},
        {"case_id": "strong_signal_case", "original_score": 0.91, "adversarial_shift": -0.08},
        {"case_id": "gaming_success_case", "original_score": 0.76, "adversarial_shift": -0.10},
    ]

    rows: list[dict[str, object]] = []

    for item in examples:
        original_score = float(item["original_score"])
        shifted_score = original_score + float(item["adversarial_shift"])
        rows.append({
            **item,
            "threshold": threshold,
            "shifted_score": round(shifted_score, 3),
            "original_flagged": original_score >= threshold,
            "after_shift_flagged": shifted_score >= threshold,
            "evasion_success": original_score >= threshold and shifted_score < threshold,
        })

    return rows


def perturbation_sensitivity_demo(seed: int = 7) -> list[dict[str, object]]:
    rng = random.Random(seed)
    rows: list[dict[str, object]] = []

    for index in range(1, 11):
        base_margin = rng.uniform(-0.25, 0.25)
        perturbation = rng.uniform(-0.18, 0.18)
        original_label = "positive" if base_margin >= 0 else "negative"
        shifted_margin = base_margin + perturbation
        shifted_label = "positive" if shifted_margin >= 0 else "negative"
        rows.append({
            "example_id": f"example_{index:02d}",
            "base_margin": round(base_margin, 4),
            "perturbation": round(perturbation, 4),
            "shifted_margin": round(shifted_margin, 4),
            "original_label": original_label,
            "shifted_label": shifted_label,
            "label_changed": original_label != shifted_label,
        })

    return rows


def attack_surface_inventory() -> list[dict[str, object]]:
    return [
        {
            "surface": "public API",
            "possible_attack": "credential abuse, scraping, injection, denial of service",
            "control": "authentication, authorization, quotas, input validation, monitoring",
            "risk_level": "high",
        },
        {
            "surface": "training data pipeline",
            "possible_attack": "poisoning, label manipulation, source compromise",
            "control": "provenance, anomaly detection, label audit, source review",
            "risk_level": "high",
        },
        {
            "surface": "prompt and retrieved context",
            "possible_attack": "prompt injection, instruction conflict, data exfiltration",
            "control": "context isolation, tool permissioning, instruction hierarchy",
            "risk_level": "high",
        },
        {
            "surface": "ranking feedback signals",
            "possible_attack": "coordinated manipulation, bot engagement, gaming",
            "control": "behavioral monitoring, graph analysis, abuse-case review",
            "risk_level": "medium",
        },
        {
            "surface": "human review queue",
            "possible_attack": "review fatigue, social engineering, appeal flooding",
            "control": "escalation policy, reviewer support, sampling audits",
            "risk_level": "medium",
        },
    ]


def attack_success_probability(capability: float, exposure: float, control_strength: float) -> float:
    return clamp(100.0 * capability * exposure * (1.0 - control_strength))


def attack_probability_demo() -> list[dict[str, object]]:
    cases = [
        {"attack": "prompt injection", "capability": 0.80, "exposure": 0.75, "control_strength": 0.62},
        {"attack": "threshold evasion", "capability": 0.72, "exposure": 0.68, "control_strength": 0.55},
        {"attack": "data poisoning", "capability": 0.58, "exposure": 0.52, "control_strength": 0.70},
        {"attack": "credential replay", "capability": 0.60, "exposure": 0.46, "control_strength": 0.82},
    ]
    return [
        {
            **case,
            "estimated_attack_success_probability": round(
                attack_success_probability(case["capability"], case["exposure"], case["control_strength"]), 3
            ),
        }
        for case in cases
    ]


def run_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    for case in build_cases():
        readiness = adversarial_readiness_score(case)
        risk = adversarial_risk_score(case)
        rows.append({
            **asdict(case),
            "adversarial_readiness_score": round(readiness, 3),
            "adversarial_risk_score": round(risk, 3),
            "diagnostic": diagnose(readiness, risk),
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
    evasion_rows: list[dict[str, object]],
    perturbation_rows: list[dict[str, object]],
    surfaces: list[dict[str, object]],
    attack_rows: list[dict[str, object]],
) -> dict[str, object]:
    evasion_successes = sum(1 for row in evasion_rows if bool(row["evasion_success"]))
    label_changes = sum(1 for row in perturbation_rows if bool(row["label_changed"]))
    high_risk_surfaces = sum(1 for row in surfaces if row["risk_level"] == "high")
    max_attack_probability = max(float(row["estimated_attack_success_probability"]) for row in attack_rows)

    return {
        "case_count": len(audit_rows),
        "average_adversarial_readiness_score": round(mean(float(row["adversarial_readiness_score"]) for row in audit_rows), 3),
        "average_adversarial_risk_score": round(mean(float(row["adversarial_risk_score"]) for row in audit_rows), 3),
        "highest_readiness_case": max(audit_rows, key=lambda row: float(row["adversarial_readiness_score"]))["case_name"],
        "highest_risk_case": max(audit_rows, key=lambda row: float(row["adversarial_risk_score"]))["case_name"],
        "threshold_evasion_successes": evasion_successes,
        "perturbation_label_changes": label_changes,
        "high_risk_attack_surfaces": high_risk_surfaces,
        "max_estimated_attack_success_probability": max_attack_probability,
        "interpretation": "Adversarial readiness depends on threat-model clarity, attack-surface mapping, trust-boundary review, abuse-case coverage, validation, monitoring, defense depth, incident response, red teaming, false-positive review, governance ownership, and communication of residual risk."
    }


def main() -> None:
    audit_rows = run_audit()
    evasion_rows = threshold_evasion_demo()
    perturbation_rows = perturbation_sensitivity_demo()
    surfaces = attack_surface_inventory()
    attack_rows = attack_probability_demo()
    summary = summarize(audit_rows, evasion_rows, perturbation_rows, surfaces, attack_rows)

    write_csv(TABLES / "adversarial_readiness_audit.csv", audit_rows)
    write_csv(TABLES / "adversarial_readiness_summary.csv", [summary])
    write_csv(TABLES / "threshold_evasion_demo.csv", evasion_rows)
    write_csv(TABLES / "perturbation_sensitivity_demo.csv", perturbation_rows)
    write_csv(TABLES / "attack_surface_inventory.csv", surfaces)
    write_csv(TABLES / "attack_probability_demo.csv", attack_rows)

    write_json(JSON_DIR / "adversarial_readiness_audit.json", audit_rows)
    write_json(JSON_DIR / "adversarial_readiness_summary.json", summary)
    write_json(JSON_DIR / "threshold_evasion_demo.json", evasion_rows)
    write_json(JSON_DIR / "perturbation_sensitivity_demo.json", perturbation_rows)
    write_json(JSON_DIR / "attack_surface_inventory.json", surfaces)
    write_json(JSON_DIR / "attack_probability_demo.json", attack_rows)

    print("Adversarial thinking in computational systems audit complete.")
    print(TABLES / "adversarial_readiness_audit.csv")


if __name__ == "__main__":
    main()
