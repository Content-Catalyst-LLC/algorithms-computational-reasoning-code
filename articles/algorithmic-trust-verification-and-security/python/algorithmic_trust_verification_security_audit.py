# algorithmic_trust_verification_security_audit.py
# Dependency-light workflow for algorithmic trust, verification, and security review.

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import json

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class AlgorithmicTrustCase:
    case_name: str
    system_context: str
    trust_claim: str
    specification_clarity: float
    verification_evidence: float
    validation_evidence: float
    security_controls: float
    provenance_traceability: float
    audit_logging: float
    monitoring_lifecycle: float
    incident_response: float
    robustness_testing: float
    human_trust_calibration: float
    governance_ownership: float
    communication_clarity: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def trust_quality_score(case: AlgorithmicTrustCase) -> float:
    return clamp(
        100.0 * (
            0.09 * case.specification_clarity
            + 0.10 * case.verification_evidence
            + 0.10 * case.validation_evidence
            + 0.10 * case.security_controls
            + 0.09 * case.provenance_traceability
            + 0.08 * case.audit_logging
            + 0.10 * case.monitoring_lifecycle
            + 0.08 * case.incident_response
            + 0.08 * case.robustness_testing
            + 0.07 * case.human_trust_calibration
            + 0.08 * case.governance_ownership
            + 0.03 * case.communication_clarity
        )
    )


def residual_trust_risk(case: AlgorithmicTrustCase) -> float:
    weak_points = [
        1.0 - case.specification_clarity,
        1.0 - case.verification_evidence,
        1.0 - case.validation_evidence,
        1.0 - case.security_controls,
        1.0 - case.provenance_traceability,
        1.0 - case.audit_logging,
        1.0 - case.monitoring_lifecycle,
        1.0 - case.incident_response,
        1.0 - case.robustness_testing,
        1.0 - case.human_trust_calibration,
        1.0 - case.governance_ownership,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong evidence-based trust posture"
    if score >= 70 and risk <= 35:
        return "usable trust posture with review needs"
    if risk >= 55:
        return "high risk; trust claim may lack verification, validation, security, traceability, monitoring, or governance"
    return "partial trust posture; strengthen evidence, controls, monitoring, incident response, calibration, and accountability"


def build_cases() -> list[AlgorithmicTrustCase]:
    return [
        AlgorithmicTrustCase(
            case_name="Signed release and model registry",
            system_context="Machine-learning service deploys signed model artifacts through a controlled registry.",
            trust_claim="deployed model artifact matches reviewed version and remains monitored after release",
            specification_clarity=0.86,
            verification_evidence=0.88,
            validation_evidence=0.82,
            security_controls=0.88,
            provenance_traceability=0.90,
            audit_logging=0.84,
            monitoring_lifecycle=0.84,
            incident_response=0.80,
            robustness_testing=0.78,
            human_trust_calibration=0.74,
            governance_ownership=0.82,
            communication_clarity=0.78,
        ),
        AlgorithmicTrustCase(
            case_name="Public eligibility decision support",
            system_context="Algorithmic triage tool supports public-service eligibility review.",
            trust_claim="system prioritizes cases consistently while preserving appeal and human review",
            specification_clarity=0.78,
            verification_evidence=0.74,
            validation_evidence=0.76,
            security_controls=0.70,
            provenance_traceability=0.78,
            audit_logging=0.82,
            monitoring_lifecycle=0.70,
            incident_response=0.68,
            robustness_testing=0.66,
            human_trust_calibration=0.72,
            governance_ownership=0.76,
            communication_clarity=0.74,
        ),
        AlgorithmicTrustCase(
            case_name="Research computation pipeline",
            system_context="Reproducible workflow generates models, figures, and reports from versioned data.",
            trust_claim="outputs can be reconstructed from documented inputs, code, parameters, and environment",
            specification_clarity=0.80,
            verification_evidence=0.76,
            validation_evidence=0.72,
            security_controls=0.62,
            provenance_traceability=0.88,
            audit_logging=0.78,
            monitoring_lifecycle=0.60,
            incident_response=0.52,
            robustness_testing=0.68,
            human_trust_calibration=0.70,
            governance_ownership=0.66,
            communication_clarity=0.76,
        ),
        AlgorithmicTrustCase(
            case_name="Unmonitored automated scoring script",
            system_context="Internal script scores records using undocumented thresholds and unversioned inputs.",
            trust_claim="system provides reliable scores for operational use",
            specification_clarity=0.24,
            verification_evidence=0.22,
            validation_evidence=0.18,
            security_controls=0.20,
            provenance_traceability=0.16,
            audit_logging=0.18,
            monitoring_lifecycle=0.10,
            incident_response=0.12,
            robustness_testing=0.14,
            human_trust_calibration=0.20,
            governance_ownership=0.18,
            communication_clarity=0.24,
        ),
    ]


def evidence_coverage_matrix() -> list[dict[str, object]]:
    evidence_items = [
        {"evidence": "formal specification", "verification": 0.90, "validation": 0.35, "security": 0.30, "traceability": 0.55, "governance": 0.45},
        {"evidence": "domain validation report", "verification": 0.30, "validation": 0.92, "security": 0.25, "traceability": 0.55, "governance": 0.65},
        {"evidence": "threat model and control map", "verification": 0.35, "validation": 0.40, "security": 0.92, "traceability": 0.60, "governance": 0.72},
        {"evidence": "signed artifact manifest", "verification": 0.78, "validation": 0.20, "security": 0.72, "traceability": 0.92, "governance": 0.70},
        {"evidence": "monitoring and incident log", "verification": 0.45, "validation": 0.55, "security": 0.68, "traceability": 0.86, "governance": 0.88},
        {"evidence": "user guidance and limitations note", "verification": 0.25, "validation": 0.65, "security": 0.30, "traceability": 0.35, "governance": 0.82},
    ]
    rows: list[dict[str, object]] = []
    for item in evidence_items:
        dimensions = [float(item[key]) for key in ["verification", "validation", "security", "traceability", "governance"]]
        rows.append({**item, "average_coverage": round(mean(dimensions) * 100.0, 3)})
    return rows


def residual_risk_register() -> list[dict[str, object]]:
    risks = [
        {"risk": "distribution shift", "initial_likelihood": 0.70, "initial_impact": 0.75, "control_strength": 0.62},
        {"risk": "dependency compromise", "initial_likelihood": 0.45, "initial_impact": 0.90, "control_strength": 0.70},
        {"risk": "audit log incompleteness", "initial_likelihood": 0.50, "initial_impact": 0.65, "control_strength": 0.52},
        {"risk": "automation overreliance", "initial_likelihood": 0.62, "initial_impact": 0.72, "control_strength": 0.48},
        {"risk": "unauthorized model artifact change", "initial_likelihood": 0.32, "initial_impact": 0.88, "control_strength": 0.78},
    ]
    rows: list[dict[str, object]] = []
    for risk in risks:
        initial = 100.0 * float(risk["initial_likelihood"]) * float(risk["initial_impact"])
        residual = initial * (1.0 - float(risk["control_strength"]))
        rows.append({
            **risk,
            "initial_risk_score": round(initial, 3),
            "residual_risk_score": round(residual, 3),
            "risk_reduction": round(initial - residual, 3),
            "review_priority": "high" if residual >= 25 else "medium" if residual >= 12 else "standard",
        })
    return rows


def trust_calibration_review() -> list[dict[str, object]]:
    cases = [
        {"user_group": "expert reviewers", "human_reliance": 0.62, "system_reliability": 0.76},
        {"user_group": "frontline operators", "human_reliance": 0.88, "system_reliability": 0.72},
        {"user_group": "new users", "human_reliance": 0.42, "system_reliability": 0.68},
        {"user_group": "managers", "human_reliance": 0.80, "system_reliability": 0.70},
    ]
    rows: list[dict[str, object]] = []
    for case in cases:
        gap = abs(float(case["human_reliance"]) - float(case["system_reliability"]))
        direction = "overreliance" if float(case["human_reliance"]) > float(case["system_reliability"]) else "underreliance"
        rows.append({
            **case,
            "calibration_gap": round(gap, 3),
            "calibration_direction": direction,
            "review_recommendation": "intervention needed" if gap >= 0.18 else "monitor" if gap >= 0.10 else "well calibrated",
        })
    return rows


def run_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in build_cases():
        score = trust_quality_score(case)
        risk = residual_trust_risk(case)
        rows.append({**asdict(case), "trust_quality_score": round(score, 3), "residual_trust_risk": round(risk, 3), "diagnostic": diagnose(score, risk)})
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


def summarize(audit_rows, evidence_rows, risk_rows, calibration_rows) -> dict[str, object]:
    high_priority_risks = sum(1 for row in risk_rows if row["review_priority"] == "high")
    calibration_interventions = sum(1 for row in calibration_rows if row["review_recommendation"] == "intervention needed")
    return {
        "case_count": len(audit_rows),
        "average_trust_quality_score": round(mean(float(row["trust_quality_score"]) for row in audit_rows), 3),
        "average_residual_trust_risk": round(mean(float(row["residual_trust_risk"]) for row in audit_rows), 3),
        "highest_trust_quality_case": max(audit_rows, key=lambda row: float(row["trust_quality_score"]))["case_name"],
        "highest_residual_risk_case": max(audit_rows, key=lambda row: float(row["residual_trust_risk"]))["case_name"],
        "average_evidence_coverage": round(mean(float(row["average_coverage"]) for row in evidence_rows), 3),
        "high_priority_residual_risks": high_priority_risks,
        "trust_calibration_interventions": calibration_interventions,
        "interpretation": "Algorithmic trust depends on verification, validation, security, provenance, auditability, monitoring, incident response, robustness testing, trust calibration, governance ownership, and clear communication of limits."
    }


def main() -> None:
    audit_rows = run_audit()
    evidence_rows = evidence_coverage_matrix()
    risk_rows = residual_risk_register()
    calibration_rows = trust_calibration_review()
    summary = summarize(audit_rows, evidence_rows, risk_rows, calibration_rows)

    write_csv(TABLES / "algorithmic_trust_audit.csv", audit_rows)
    write_csv(TABLES / "algorithmic_trust_summary.csv", [summary])
    write_csv(TABLES / "trust_evidence_coverage_matrix.csv", evidence_rows)
    write_csv(TABLES / "residual_risk_register.csv", risk_rows)
    write_csv(TABLES / "trust_calibration_review.csv", calibration_rows)

    write_json(JSON_DIR / "algorithmic_trust_audit.json", audit_rows)
    write_json(JSON_DIR / "algorithmic_trust_summary.json", summary)
    write_json(JSON_DIR / "trust_evidence_coverage_matrix.json", evidence_rows)
    write_json(JSON_DIR / "residual_risk_register.json", risk_rows)
    write_json(JSON_DIR / "trust_calibration_review.json", calibration_rows)

    print("Algorithmic trust, verification, and security audit complete.")
    print(TABLES / "algorithmic_trust_audit.csv")


if __name__ == "__main__":
    main()
