#!/usr/bin/env python3
"""Audit cryptographic algorithms and secure communication governance.

This module is dependency-light by design. It does not implement production
cryptography. It demonstrates message-authentication checks with Python's
standard library and scores secure-communication governance readiness across
threat modeling, protocols, key management, validation, integrity,
authentication, randomness, implementation review, and incident response.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import base64
import csv
import hashlib
import hmac
import json
import secrets

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class SecureCommunicationCase:
    case_name: str
    system_context: str
    security_goal: str
    threat_model_clarity: float
    approved_protocols: float
    key_management: float
    certificate_validation: float
    message_integrity: float
    authentication_design: float
    randomness_quality: float
    secret_storage: float
    rotation_revocation: float
    implementation_review: float
    monitoring_logging: float
    incident_response: float
    communication_clarity: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def secure_communication_score(case: SecureCommunicationCase) -> float:
    return clamp(
        100.0
        * (
            0.10 * case.threat_model_clarity
            + 0.09 * case.approved_protocols
            + 0.11 * case.key_management
            + 0.09 * case.certificate_validation
            + 0.09 * case.message_integrity
            + 0.09 * case.authentication_design
            + 0.08 * case.randomness_quality
            + 0.09 * case.secret_storage
            + 0.08 * case.rotation_revocation
            + 0.08 * case.implementation_review
            + 0.05 * case.monitoring_logging
            + 0.04 * case.incident_response
            + 0.01 * case.communication_clarity
        )
    )


def secure_communication_risk(case: SecureCommunicationCase) -> float:
    weak_points = [
        1.0 - case.threat_model_clarity,
        1.0 - case.approved_protocols,
        1.0 - case.key_management,
        1.0 - case.certificate_validation,
        1.0 - case.message_integrity,
        1.0 - case.authentication_design,
        1.0 - case.randomness_quality,
        1.0 - case.secret_storage,
        1.0 - case.rotation_revocation,
        1.0 - case.implementation_review,
        1.0 - case.monitoring_logging,
        1.0 - case.incident_response,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong secure-communication governance"
    if score >= 70 and risk <= 35:
        return "usable cryptographic process with review needs"
    if risk >= 55:
        return "high risk; threat model, protocols, keys, validation, integrity, authentication, rotation, implementation, or incident response may be weak"
    return "partial discipline; strengthen threat modeling, key management, validation, integrity, authentication, randomness, secret storage, rotation, implementation review, monitoring, and governance"


def make_hmac_tag(message: bytes, key: bytes) -> str:
    tag = hmac.new(key, message, hashlib.sha256).digest()
    return base64.urlsafe_b64encode(tag).decode("ascii")


def verify_hmac_tag(message: bytes, key: bytes, expected_tag: str) -> bool:
    actual_tag = make_hmac_tag(message, key)
    return hmac.compare_digest(actual_tag, expected_tag)


def educational_message_authentication_demo() -> list[dict[str, object]]:
    key = secrets.token_bytes(32)
    message = b"approved software update manifest"
    altered_message = b"tampered software update manifest"
    tag = make_hmac_tag(message, key)

    return [
        {
            "check_name": "original message",
            "message": message.decode("utf-8"),
            "tag_prefix": tag[:16],
            "verified": verify_hmac_tag(message, key, tag),
            "interpretation": "Original message verifies with the shared secret.",
        },
        {
            "check_name": "altered message",
            "message": altered_message.decode("utf-8"),
            "tag_prefix": tag[:16],
            "verified": verify_hmac_tag(altered_message, key, tag),
            "interpretation": "Altered message fails verification with the original tag.",
        },
    ]


def approved_primitive_inventory() -> list[dict[str, object]]:
    return [
        {
            "primitive_area": "symmetric encryption",
            "preferred_property": "authenticated encryption",
            "review_question": "Does the implementation protect confidentiality and integrity together?",
            "governance_note": "Use reviewed libraries and approved protocol configurations rather than custom encryption code.",
        },
        {
            "primitive_area": "public-key cryptography",
            "preferred_property": "validated key exchange or signature scheme",
            "review_question": "Are public keys correctly bound to identities and validated before trust?",
            "governance_note": "Certificate validation and trust-anchor management must be documented.",
        },
        {
            "primitive_area": "message integrity",
            "preferred_property": "cryptographic hash, MAC, or digital signature",
            "review_question": "Is integrity anchored to a trusted reference, shared secret, or public key?",
            "governance_note": "A bare hash is not sender authentication unless the reference is trusted.",
        },
        {
            "primitive_area": "randomness",
            "preferred_property": "cryptographic random generation",
            "review_question": "Are keys, nonces, salts, and tokens generated with appropriate randomness?",
            "governance_note": "Predictable randomness can undermine strong algorithms.",
        },
        {
            "primitive_area": "key lifecycle",
            "preferred_property": "generation, storage, access, rotation, revocation, destruction",
            "review_question": "Can every secret be inventoried and retired after compromise?",
            "governance_note": "Key lifecycle failures are common causes of security breakdown.",
        },
    ]


def build_cases() -> list[SecureCommunicationCase]:
    return [
        SecureCommunicationCase(
            case_name="Web service secure channel",
            system_context="Public web service using authenticated secure sessions and certificate validation.",
            security_goal="protect confidentiality, integrity, authentication, and session freshness",
            threat_model_clarity=0.86,
            approved_protocols=0.88,
            key_management=0.82,
            certificate_validation=0.90,
            message_integrity=0.86,
            authentication_design=0.84,
            randomness_quality=0.84,
            secret_storage=0.82,
            rotation_revocation=0.78,
            implementation_review=0.80,
            monitoring_logging=0.76,
            incident_response=0.74,
            communication_clarity=0.80,
        ),
        SecureCommunicationCase(
            case_name="Signed software update workflow",
            system_context="Software distribution process using signed manifests and controlled release keys.",
            security_goal="verify update authenticity, integrity, authorization, and revocation status",
            threat_model_clarity=0.84,
            approved_protocols=0.82,
            key_management=0.86,
            certificate_validation=0.72,
            message_integrity=0.90,
            authentication_design=0.86,
            randomness_quality=0.78,
            secret_storage=0.88,
            rotation_revocation=0.82,
            implementation_review=0.84,
            monitoring_logging=0.80,
            incident_response=0.76,
            communication_clarity=0.78,
        ),
        SecureCommunicationCase(
            case_name="Internal API token exchange",
            system_context="Service-to-service API calls using shared secrets and rotating tokens.",
            security_goal="authenticate services and protect requests from tampering and replay",
            threat_model_clarity=0.76,
            approved_protocols=0.74,
            key_management=0.70,
            certificate_validation=0.62,
            message_integrity=0.78,
            authentication_design=0.76,
            randomness_quality=0.80,
            secret_storage=0.68,
            rotation_revocation=0.64,
            implementation_review=0.70,
            monitoring_logging=0.72,
            incident_response=0.66,
            communication_clarity=0.70,
        ),
        SecureCommunicationCase(
            case_name="Legacy encrypted file transfer",
            system_context="Old workflow using unclear encryption tools, shared passwords, and manual verification.",
            security_goal="protect sensitive files in transit",
            threat_model_clarity=0.36,
            approved_protocols=0.28,
            key_management=0.24,
            certificate_validation=0.18,
            message_integrity=0.34,
            authentication_design=0.28,
            randomness_quality=0.30,
            secret_storage=0.22,
            rotation_revocation=0.16,
            implementation_review=0.20,
            monitoring_logging=0.24,
            incident_response=0.20,
            communication_clarity=0.34,
        ),
    ]


def run_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in build_cases():
        score = secure_communication_score(case)
        risk = secure_communication_risk(case)
        rows.append(
            {
                **asdict(case),
                "secure_communication_score": round(score, 3),
                "secure_communication_risk": round(risk, 3),
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


def summarize(audit_rows: list[dict[str, object]], auth_rows: list[dict[str, object]], inventory_rows: list[dict[str, object]]) -> dict[str, object]:
    failed_auth_checks = sum(1 for row in auth_rows if not bool(row["verified"]))
    return {
        "case_count": len(audit_rows),
        "average_secure_communication_score": round(mean(float(row["secure_communication_score"]) for row in audit_rows), 3),
        "average_secure_communication_risk": round(mean(float(row["secure_communication_risk"]) for row in audit_rows), 3),
        "highest_score_case": max(audit_rows, key=lambda row: float(row["secure_communication_score"]))["case_name"],
        "highest_risk_case": max(audit_rows, key=lambda row: float(row["secure_communication_risk"]))["case_name"],
        "message_authentication_checks": len(auth_rows),
        "failed_message_authentication_checks": failed_auth_checks,
        "primitive_inventory_count": len(inventory_rows),
        "interpretation": "Secure communication depends on threat modeling, approved protocols, key management, certificate validation, message integrity, authentication, randomness, secret storage, rotation, implementation review, monitoring, incident response, and clear communication of limits.",
    }


def main() -> None:
    audit_rows = run_audit()
    auth_rows = educational_message_authentication_demo()
    inventory_rows = approved_primitive_inventory()
    summary = summarize(audit_rows, auth_rows, inventory_rows)

    write_csv(TABLES / "secure_communication_governance_audit.csv", audit_rows)
    write_csv(TABLES / "secure_communication_governance_summary.csv", [summary])
    write_csv(TABLES / "message_authentication_demo.csv", auth_rows)
    write_csv(TABLES / "approved_primitive_inventory.csv", inventory_rows)

    write_json(JSON_DIR / "secure_communication_governance_audit.json", audit_rows)
    write_json(JSON_DIR / "secure_communication_governance_summary.json", summary)
    write_json(JSON_DIR / "message_authentication_demo.json", auth_rows)
    write_json(JSON_DIR / "approved_primitive_inventory.json", inventory_rows)

    print("Cryptographic algorithms and secure communication audit complete.")
    print(TABLES / "secure_communication_governance_audit.csv")
    print("Failed authentication checks in demo:", summary["failed_message_authentication_checks"])
    print("Highest risk case:", summary["highest_risk_case"])


if __name__ == "__main__":
    main()
