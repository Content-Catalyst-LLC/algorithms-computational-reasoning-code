# security_failures_as_algorithmic_failures_audit.py
# Dependency-light workflow for auditing security failures as algorithmic failures.

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
class SecurityFailureCase:
    case_name: str
    system_context: str
    failure_pattern: str
    assumption_quality: float
    threat_model_coverage: float
    input_boundary_control: float
    authorization_control: float
    cryptographic_procedure: float
    dependency_governance: float
    configuration_safety: float
    state_timing_control: float
    logging_traceability: float
    monitoring_detection: float
    incident_response: float
    lifecycle_review: float
    governance_ownership: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def failure_resistance_score(case: SecurityFailureCase) -> float:
    return clamp(
        100.0 * (
            0.08 * case.assumption_quality
            + 0.10 * case.threat_model_coverage
            + 0.10 * case.input_boundary_control
            + 0.10 * case.authorization_control
            + 0.08 * case.cryptographic_procedure
            + 0.08 * case.dependency_governance
            + 0.08 * case.configuration_safety
            + 0.08 * case.state_timing_control
            + 0.08 * case.logging_traceability
            + 0.08 * case.monitoring_detection
            + 0.06 * case.incident_response
            + 0.05 * case.lifecycle_review
            + 0.03 * case.governance_ownership
        )
    )


def algorithmic_failure_risk(case: SecurityFailureCase) -> float:
    weak_points = [
        1.0 - case.assumption_quality,
        1.0 - case.threat_model_coverage,
        1.0 - case.input_boundary_control,
        1.0 - case.authorization_control,
        1.0 - case.cryptographic_procedure,
        1.0 - case.dependency_governance,
        1.0 - case.configuration_safety,
        1.0 - case.state_timing_control,
        1.0 - case.logging_traceability,
        1.0 - case.monitoring_detection,
        1.0 - case.incident_response,
        1.0 - case.lifecycle_review,
        1.0 - case.governance_ownership,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong resistance to algorithmic security failure"
    if score >= 70 and risk <= 35:
        return "usable security posture with review needs"
    if risk >= 55:
        return "high risk; weak assumptions, missing controls, poor traceability, or lifecycle gaps may create exploitable failure"
    return "partial security posture; strengthen threat modeling, boundary control, authorization, dependency governance, monitoring, response, and ownership"


def build_cases() -> list[SecurityFailureCase]:
    return [
        SecurityFailureCase(
            case_name="Object-level access weakness",
            system_context="Application exposes records through predictable object identifiers.",
            failure_pattern="authorization decision does not bind subject to resource ownership",
            assumption_quality=0.34,
            threat_model_coverage=0.30,
            input_boundary_control=0.52,
            authorization_control=0.18,
            cryptographic_procedure=0.70,
            dependency_governance=0.62,
            configuration_safety=0.64,
            state_timing_control=0.56,
            logging_traceability=0.48,
            monitoring_detection=0.36,
            incident_response=0.44,
            lifecycle_review=0.42,
            governance_ownership=0.46,
        ),
        SecurityFailureCase(
            case_name="Overbroad service account",
            system_context="Scheduled job uses a long-lived token with broad production access.",
            failure_pattern="machine identity violates least privilege and lifecycle review",
            assumption_quality=0.42,
            threat_model_coverage=0.44,
            input_boundary_control=0.70,
            authorization_control=0.38,
            cryptographic_procedure=0.58,
            dependency_governance=0.56,
            configuration_safety=0.48,
            state_timing_control=0.54,
            logging_traceability=0.52,
            monitoring_detection=0.42,
            incident_response=0.46,
            lifecycle_review=0.22,
            governance_ownership=0.36,
        ),
        SecurityFailureCase(
            case_name="Signed release pipeline",
            system_context="Software release process uses signed artifacts, dependency pinning, and monitored deployment.",
            failure_pattern="supply-chain risk controlled through provenance and verification",
            assumption_quality=0.82,
            threat_model_coverage=0.80,
            input_boundary_control=0.78,
            authorization_control=0.82,
            cryptographic_procedure=0.88,
            dependency_governance=0.86,
            configuration_safety=0.82,
            state_timing_control=0.76,
            logging_traceability=0.86,
            monitoring_detection=0.82,
            incident_response=0.78,
            lifecycle_review=0.80,
            governance_ownership=0.84,
        ),
        SecurityFailureCase(
            case_name="Prompt-to-tool boundary failure",
            system_context="AI assistant reads external content and can call tools with user authority.",
            failure_pattern="untrusted text crosses into instruction and tool-use authority",
            assumption_quality=0.28,
            threat_model_coverage=0.26,
            input_boundary_control=0.18,
            authorization_control=0.34,
            cryptographic_procedure=0.64,
            dependency_governance=0.50,
            configuration_safety=0.44,
            state_timing_control=0.42,
            logging_traceability=0.46,
            monitoring_detection=0.34,
            incident_response=0.38,
            lifecycle_review=0.36,
            governance_ownership=0.40,
        ),
        SecurityFailureCase(
            case_name="Monitored public API",
            system_context="Public API validates inputs, scopes tokens, rate-limits requests, and monitors anomalies.",
            failure_pattern="external boundary controlled through layered checks",
            assumption_quality=0.78,
            threat_model_coverage=0.76,
            input_boundary_control=0.84,
            authorization_control=0.78,
            cryptographic_procedure=0.78,
            dependency_governance=0.70,
            configuration_safety=0.74,
            state_timing_control=0.72,
            logging_traceability=0.82,
            monitoring_detection=0.80,
            incident_response=0.76,
            lifecycle_review=0.70,
            governance_ownership=0.72,
        ),
    ]


def control_gap_register() -> list[dict[str, object]]:
    controls = [
        {"control": "server_side_object_authorization", "coverage": 0.42, "importance": 0.95, "detectability": 0.45},
        {"control": "service_account_lifecycle_review", "coverage": 0.36, "importance": 0.88, "detectability": 0.52},
        {"control": "signed_artifact_verification", "coverage": 0.78, "importance": 0.86, "detectability": 0.76},
        {"control": "prompt_tool_boundary_enforcement", "coverage": 0.28, "importance": 0.82, "detectability": 0.40},
        {"control": "centralized_security_logging", "coverage": 0.68, "importance": 0.84, "detectability": 0.74},
        {"control": "dependency_and_configuration_review", "coverage": 0.60, "importance": 0.80, "detectability": 0.66},
    ]
    rows: list[dict[str, object]] = []
    for control in controls:
        gap = (1.0 - float(control["coverage"])) * float(control["importance"])
        hidden_gap = gap * (1.0 - float(control["detectability"]))
        rows.append({
            **control,
            "control_gap_score": round(100.0 * gap, 3),
            "hidden_gap_score": round(100.0 * hidden_gap, 3),
            "priority": "high" if gap >= 0.45 else "medium" if gap >= 0.25 else "standard",
        })
    return rows


def incident_timeline_review() -> list[dict[str, object]]:
    incidents = [
        {"incident": "unexpected_admin_export", "detect_hours": 6, "triage_hours": 4, "contain_hours": 3, "remediate_hours": 36},
        {"incident": "dependency_vulnerability", "detect_hours": 24, "triage_hours": 8, "contain_hours": 12, "remediate_hours": 96},
        {"incident": "stolen_service_token", "detect_hours": 12, "triage_hours": 6, "contain_hours": 2, "remediate_hours": 48},
        {"incident": "prompt_tool_boundary_attempt", "detect_hours": 2, "triage_hours": 3, "contain_hours": 2, "remediate_hours": 24},
    ]
    rows: list[dict[str, object]] = []
    for incident in incidents:
        response_gap = int(incident["detect_hours"]) + int(incident["triage_hours"]) + int(incident["contain_hours"])
        total_time = response_gap + int(incident["remediate_hours"])
        rows.append({
            **incident,
            "response_gap_hours": response_gap,
            "total_resolution_hours": total_time,
            "response_priority": "urgent" if response_gap >= 24 else "review" if response_gap >= 10 else "standard",
        })
    return rows


def assumption_stress_tests() -> list[dict[str, object]]:
    tests = [
        {"assumption": "users cannot access records they do not own", "stress_condition": "user changes record identifier", "expected_control": "object-level authorization", "passed": False},
        {"assumption": "service tokens remain private", "stress_condition": "token appears in logs", "expected_control": "secret scanning and rotation", "passed": False},
        {"assumption": "downloaded model artifact is authentic", "stress_condition": "artifact hash differs from signed manifest", "expected_control": "signature and hash verification", "passed": True},
        {"assumption": "external text is data, not instruction", "stress_condition": "external content requests privileged tool call", "expected_control": "instruction/data separation and tool authorization", "passed": False},
        {"assumption": "rate limits prevent resource exhaustion", "stress_condition": "distributed burst exceeds ordinary traffic", "expected_control": "adaptive rate limiting and anomaly detection", "passed": True},
    ]
    rows: list[dict[str, object]] = []
    for test in tests:
        rows.append({
            **test,
            "result": "pass" if bool(test["passed"]) else "fail",
            "interpretation": "Stress condition is covered by current controls." if bool(test["passed"]) else "Assumption breaks under stress and requires remediation.",
        })
    return rows


def run_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in build_cases():
        score = failure_resistance_score(case)
        risk = algorithmic_failure_risk(case)
        rows.append({
            **asdict(case),
            "failure_resistance_score": round(score, 3),
            "algorithmic_failure_risk": round(risk, 3),
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


def summarize(audit_rows: list[dict[str, object]], gap_rows: list[dict[str, object]], incident_rows: list[dict[str, object]], stress_rows: list[dict[str, object]]) -> dict[str, object]:
    high_gap_count = sum(1 for row in gap_rows if row["priority"] == "high")
    failed_stress_tests = sum(1 for row in stress_rows if row["result"] == "fail")
    urgent_incidents = sum(1 for row in incident_rows if row["response_priority"] == "urgent")
    return {
        "case_count": len(audit_rows),
        "average_failure_resistance_score": round(mean(float(row["failure_resistance_score"]) for row in audit_rows), 3),
        "average_algorithmic_failure_risk": round(mean(float(row["algorithmic_failure_risk"]) for row in audit_rows), 3),
        "highest_risk_case": max(audit_rows, key=lambda row: float(row["algorithmic_failure_risk"]))["case_name"],
        "strongest_case": max(audit_rows, key=lambda row: float(row["failure_resistance_score"]))["case_name"],
        "high_priority_control_gaps": high_gap_count,
        "failed_assumption_stress_tests": failed_stress_tests,
        "urgent_incident_response_gaps": urgent_incidents,
        "interpretation": "Security failures often reveal mismatches among assumptions, threat models, boundary controls, authorization logic, cryptographic procedures, dependencies, configuration, state, timing, logging, monitoring, incident response, lifecycle review, and governance ownership."
    }


def main() -> None:
    audit_rows = run_audit()
    gap_rows = control_gap_register()
    incident_rows = incident_timeline_review()
    stress_rows = assumption_stress_tests()
    summary = summarize(audit_rows, gap_rows, incident_rows, stress_rows)

    write_csv(TABLES / "security_failure_pattern_audit.csv", audit_rows)
    write_csv(TABLES / "security_failure_summary.csv", [summary])
    write_csv(TABLES / "control_gap_register.csv", gap_rows)
    write_csv(TABLES / "incident_timeline_review.csv", incident_rows)
    write_csv(TABLES / "assumption_stress_tests.csv", stress_rows)

    write_json(JSON_DIR / "security_failure_pattern_audit.json", audit_rows)
    write_json(JSON_DIR / "security_failure_summary.json", summary)
    write_json(JSON_DIR / "control_gap_register.json", gap_rows)
    write_json(JSON_DIR / "incident_timeline_review.json", incident_rows)
    write_json(JSON_DIR / "assumption_stress_tests.json", stress_rows)

    print("Security failures as algorithmic failures audit complete.")
    print(TABLES / "security_failure_pattern_audit.csv")


if __name__ == "__main__":
    main()
