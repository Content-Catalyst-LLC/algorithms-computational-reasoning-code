# authentication_authorization_identity_audit.py
# Dependency-light workflow for identity, authentication, and authorization review.

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import hashlib
import hmac
import json
import secrets
import time

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class IdentityAccessCase:
    case_name: str
    system_context: str
    protected_resource: str
    authentication_strength: float
    authorization_granularity: float
    least_privilege_alignment: float
    session_token_control: float
    machine_identity_governance: float
    audit_logging: float
    access_lifecycle_review: float
    privilege_escalation_controls: float
    privacy_and_inclusion_review: float
    incident_response: float
    governance_ownership: float
    communication_clarity: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def identity_access_score(case: IdentityAccessCase) -> float:
    return clamp(
        100.0 * (
            0.10 * case.authentication_strength
            + 0.11 * case.authorization_granularity
            + 0.11 * case.least_privilege_alignment
            + 0.09 * case.session_token_control
            + 0.09 * case.machine_identity_governance
            + 0.10 * case.audit_logging
            + 0.09 * case.access_lifecycle_review
            + 0.09 * case.privilege_escalation_controls
            + 0.08 * case.privacy_and_inclusion_review
            + 0.06 * case.incident_response
            + 0.06 * case.governance_ownership
            + 0.02 * case.communication_clarity
        )
    )


def identity_access_risk(case: IdentityAccessCase) -> float:
    weak_points = [
        1.0 - case.authentication_strength,
        1.0 - case.authorization_granularity,
        1.0 - case.least_privilege_alignment,
        1.0 - case.session_token_control,
        1.0 - case.machine_identity_governance,
        1.0 - case.audit_logging,
        1.0 - case.access_lifecycle_review,
        1.0 - case.privilege_escalation_controls,
        1.0 - case.privacy_and_inclusion_review,
        1.0 - case.incident_response,
        1.0 - case.governance_ownership,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong identity and access governance"
    if score >= 70 and risk <= 35:
        return "usable identity posture with review needs"
    if risk >= 55:
        return "high risk; authentication, authorization, least privilege, token control, machine identity, audit logging, or governance may be weak"
    return "partial identity posture; strengthen authentication, authorization, least privilege, token control, machine identity, access reviews, logging, privacy review, and governance"


def hash_secret(secret: str, salt: bytes) -> str:
    digest = hashlib.pbkdf2_hmac("sha256", secret.encode("utf-8"), salt, 200_000)
    return digest.hex()


def password_storage_demo() -> list[dict[str, object]]:
    salt = secrets.token_bytes(16)
    stored = hash_secret("correct horse battery staple", salt)
    candidate_good = hash_secret("correct horse battery staple", salt)
    candidate_bad = hash_secret("incorrect password", salt)

    return [
        {
            "case": "correct_candidate",
            "verified": hmac.compare_digest(stored, candidate_good),
            "algorithm": "PBKDF2-HMAC-SHA256",
            "iterations": 200000,
            "interpretation": "A stored derived secret verifies without storing the plaintext password.",
        },
        {
            "case": "incorrect_candidate",
            "verified": hmac.compare_digest(stored, candidate_bad),
            "algorithm": "PBKDF2-HMAC-SHA256",
            "iterations": 200000,
            "interpretation": "Incorrect secret fails verification against the stored derived value.",
        },
    ]


def policy_decision(subject: dict[str, object], resource: dict[str, object], action: str, context: dict[str, object]) -> dict[str, object]:
    role = str(subject.get("role", ""))
    department = str(subject.get("department", ""))
    resource_department = str(resource.get("department", ""))
    sensitivity = str(resource.get("sensitivity", "standard"))
    mfa = bool(context.get("mfa", False))
    emergency = bool(context.get("emergency", False))

    allowed = False
    reason = "default deny"

    if role == "admin" and mfa:
        allowed = True
        reason = "admin with MFA"
    elif role == "clinician" and action == "read" and department == resource_department and mfa:
        allowed = True
        reason = "same-department clinician read with MFA"
    elif role == "researcher" and action == "read" and sensitivity == "deidentified":
        allowed = True
        reason = "researcher read deidentified data"
    elif emergency and role in {"clinician", "admin"} and mfa:
        allowed = True
        reason = "break-glass emergency access with MFA"

    return {
        "subject": subject.get("subject"),
        "role": role,
        "resource": resource.get("resource"),
        "action": action,
        "sensitivity": sensitivity,
        "mfa": mfa,
        "emergency": emergency,
        "decision": "allow" if allowed else "deny",
        "reason": reason,
    }


def authorization_demo() -> list[dict[str, object]]:
    subjects = [
        {"subject": "alice", "role": "clinician", "department": "cardiology"},
        {"subject": "bob", "role": "researcher", "department": "analytics"},
        {"subject": "carol", "role": "admin", "department": "security"},
        {"subject": "service_ingest", "role": "service", "department": "platform"},
    ]
    resources = [
        {"resource": "patient_record_100", "department": "cardiology", "sensitivity": "restricted"},
        {"resource": "deidentified_dataset_7", "department": "analytics", "sensitivity": "deidentified"},
    ]

    scenarios = [
        (subjects[0], resources[0], "read", {"mfa": True, "emergency": False}),
        (subjects[0], resources[0], "delete", {"mfa": True, "emergency": False}),
        (subjects[1], resources[1], "read", {"mfa": False, "emergency": False}),
        (subjects[1], resources[0], "read", {"mfa": True, "emergency": False}),
        (subjects[2], resources[0], "delete", {"mfa": True, "emergency": False}),
        (subjects[3], resources[1], "write", {"mfa": False, "emergency": False}),
    ]

    return [policy_decision(subject, resource, action, context) for subject, resource, action, context in scenarios]


def access_risk_register() -> list[dict[str, object]]:
    cases = [
        {"access_path": "admin_console", "resource_sensitivity": 0.95, "privilege_level": 0.95, "credential_exposure": 0.35, "control_strength": 0.78},
        {"access_path": "service_account_data_export", "resource_sensitivity": 0.85, "privilege_level": 0.80, "credential_exposure": 0.55, "control_strength": 0.52},
        {"access_path": "standard_user_profile_edit", "resource_sensitivity": 0.45, "privilege_level": 0.35, "credential_exposure": 0.40, "control_strength": 0.66},
        {"access_path": "research_dataset_read", "resource_sensitivity": 0.70, "privilege_level": 0.50, "credential_exposure": 0.30, "control_strength": 0.70},
        {"access_path": "break_glass_emergency_access", "resource_sensitivity": 0.95, "privilege_level": 0.90, "credential_exposure": 0.50, "control_strength": 0.64},
    ]

    rows: list[dict[str, object]] = []
    for case in cases:
        inherent = 100.0 * float(case["resource_sensitivity"]) * float(case["privilege_level"]) * float(case["credential_exposure"])
        residual = inherent * (1.0 - float(case["control_strength"]))
        rows.append({
            **case,
            "inherent_access_risk": round(inherent, 3),
            "residual_access_risk": round(residual, 3),
            "review_priority": "high" if residual >= 20 else "medium" if residual >= 10 else "standard",
        })
    return rows


def access_lifecycle_review() -> list[dict[str, object]]:
    now = int(time.time())
    day = 86400
    accounts = [
        {"identity": "alice", "identity_type": "human", "last_review_days": 42, "privileged": False, "active": True},
        {"identity": "carol_admin", "identity_type": "human", "last_review_days": 110, "privileged": True, "active": True},
        {"identity": "service_ingest", "identity_type": "service", "last_review_days": 210, "privileged": True, "active": True},
        {"identity": "legacy_export_job", "identity_type": "service", "last_review_days": 390, "privileged": True, "active": True},
        {"identity": "former_contractor", "identity_type": "human", "last_review_days": 270, "privileged": False, "active": False},
    ]

    rows: list[dict[str, object]] = []
    for account in accounts:
        last_review_age = int(account["last_review_days"])
        privileged = bool(account["privileged"])
        active = bool(account["active"])
        needs_review = last_review_age > 90 or (privileged and last_review_age > 45) or not active
        rows.append({
            **account,
            "approx_last_review_timestamp": now - last_review_age * day,
            "needs_review": needs_review,
            "recommendation": "remove or disable" if not active else "urgent review" if privileged and last_review_age > 90 else "review" if needs_review else "standard monitoring",
        })
    return rows


def build_cases() -> list[IdentityAccessCase]:
    return [
        IdentityAccessCase(
            case_name="Clinical record access platform",
            system_context="Healthcare system with sensitive records, clinician roles, emergency access, and audit obligations.",
            protected_resource="patient records",
            authentication_strength=0.88,
            authorization_granularity=0.84,
            least_privilege_alignment=0.78,
            session_token_control=0.82,
            machine_identity_governance=0.70,
            audit_logging=0.90,
            access_lifecycle_review=0.80,
            privilege_escalation_controls=0.78,
            privacy_and_inclusion_review=0.76,
            incident_response=0.82,
            governance_ownership=0.84,
            communication_clarity=0.76,
        ),
        IdentityAccessCase(
            case_name="Cloud analytics workspace",
            system_context="Research and analytics platform with datasets, notebooks, service accounts, and shared projects.",
            protected_resource="institutional datasets and compute environment",
            authentication_strength=0.82,
            authorization_granularity=0.76,
            least_privilege_alignment=0.70,
            session_token_control=0.72,
            machine_identity_governance=0.66,
            audit_logging=0.78,
            access_lifecycle_review=0.68,
            privilege_escalation_controls=0.66,
            privacy_and_inclusion_review=0.72,
            incident_response=0.70,
            governance_ownership=0.72,
            communication_clarity=0.70,
        ),
        IdentityAccessCase(
            case_name="Public benefits portal",
            system_context="Public-facing portal requiring account recovery, identity proofing, appeals, and privacy-sensitive access.",
            protected_resource="applicant records and benefit status",
            authentication_strength=0.70,
            authorization_granularity=0.72,
            least_privilege_alignment=0.74,
            session_token_control=0.68,
            machine_identity_governance=0.58,
            audit_logging=0.74,
            access_lifecycle_review=0.66,
            privilege_escalation_controls=0.64,
            privacy_and_inclusion_review=0.84,
            incident_response=0.68,
            governance_ownership=0.72,
            communication_clarity=0.76,
        ),
        IdentityAccessCase(
            case_name="Legacy internal admin script",
            system_context="Internal automation uses shared credentials and broad permissions for operational convenience.",
            protected_resource="production database",
            authentication_strength=0.28,
            authorization_granularity=0.18,
            least_privilege_alignment=0.16,
            session_token_control=0.20,
            machine_identity_governance=0.14,
            audit_logging=0.22,
            access_lifecycle_review=0.18,
            privilege_escalation_controls=0.14,
            privacy_and_inclusion_review=0.20,
            incident_response=0.24,
            governance_ownership=0.18,
            communication_clarity=0.26,
        ),
    ]


def run_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in build_cases():
        score = identity_access_score(case)
        risk = identity_access_risk(case)
        rows.append({
            **asdict(case),
            "identity_access_score": round(score, 3),
            "identity_access_risk": round(risk, 3),
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


def summarize(audit_rows, auth_rows, risk_rows, lifecycle_rows) -> dict[str, object]:
    allowed = sum(1 for row in auth_rows if row["decision"] == "allow")
    denied = sum(1 for row in auth_rows if row["decision"] == "deny")
    high_risk_paths = sum(1 for row in risk_rows if row["review_priority"] == "high")
    lifecycle_reviews = sum(1 for row in lifecycle_rows if bool(row["needs_review"]))

    return {
        "case_count": len(audit_rows),
        "average_identity_access_score": round(mean(float(row["identity_access_score"]) for row in audit_rows), 3),
        "average_identity_access_risk": round(mean(float(row["identity_access_risk"]) for row in audit_rows), 3),
        "highest_score_case": max(audit_rows, key=lambda row: float(row["identity_access_score"]))["case_name"],
        "highest_risk_case": max(audit_rows, key=lambda row: float(row["identity_access_risk"]))["case_name"],
        "authorization_allowed_count": allowed,
        "authorization_denied_count": denied,
        "high_risk_access_paths": high_risk_paths,
        "accounts_needing_lifecycle_review": lifecycle_reviews,
        "interpretation": "Identity and access governance depends on authentication strength, authorization granularity, least privilege, token control, machine identity, audit logging, lifecycle review, privilege escalation controls, privacy review, incident response, and governance ownership.",
    }


def main() -> None:
    audit_rows = run_audit()
    password_rows = password_storage_demo()
    auth_rows = authorization_demo()
    risk_rows = access_risk_register()
    lifecycle_rows = access_lifecycle_review()
    summary = summarize(audit_rows, auth_rows, risk_rows, lifecycle_rows)

    write_csv(TABLES / "identity_access_governance_audit.csv", audit_rows)
    write_csv(TABLES / "identity_access_governance_summary.csv", [summary])
    write_csv(TABLES / "password_storage_demo.csv", password_rows)
    write_csv(TABLES / "authorization_policy_demo.csv", auth_rows)
    write_csv(TABLES / "access_risk_register.csv", risk_rows)
    write_csv(TABLES / "access_lifecycle_review.csv", lifecycle_rows)

    write_json(JSON_DIR / "identity_access_governance_audit.json", audit_rows)
    write_json(JSON_DIR / "identity_access_governance_summary.json", summary)
    write_json(JSON_DIR / "password_storage_demo.json", password_rows)
    write_json(JSON_DIR / "authorization_policy_demo.json", auth_rows)
    write_json(JSON_DIR / "access_risk_register.json", risk_rows)
    write_json(JSON_DIR / "access_lifecycle_review.json", lifecycle_rows)

    print("Authentication, authorization, and computational identity audit complete.")
    print(TABLES / "identity_access_governance_audit.csv")


if __name__ == "__main__":
    main()
