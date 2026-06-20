#!/usr/bin/env python3
"""Audit hash functions, integrity, and verification workflows.

This dependency-light module creates synthetic artifacts, builds SHA-256 and
SHA3-256 manifests, verifies current artifacts against reference digests,
demonstrates tamper detection, builds a simple Merkle root, demonstrates HMAC
verification, and scores hash-verification governance cases.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import hashlib
import hmac
import json
import secrets

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ARTICLE_ROOT / "data" / "hash_demo_artifacts"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class HashVerificationCase:
    case_name: str
    system_context: str
    verification_goal: str
    algorithm_inventory: float
    reference_hash_protection: float
    manifest_signing: float
    verification_automation: float
    mismatch_escalation: float
    provenance_metadata: float
    legacy_hash_review: float
    key_or_signature_binding: float
    reproducibility_support: float
    audit_logging: float
    governance_review: float
    communication_clarity: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def hash_verification_score(case: HashVerificationCase) -> float:
    return clamp(
        100.0
        * (
            0.10 * case.algorithm_inventory
            + 0.11 * case.reference_hash_protection
            + 0.09 * case.manifest_signing
            + 0.10 * case.verification_automation
            + 0.09 * case.mismatch_escalation
            + 0.09 * case.provenance_metadata
            + 0.09 * case.legacy_hash_review
            + 0.09 * case.key_or_signature_binding
            + 0.08 * case.reproducibility_support
            + 0.07 * case.audit_logging
            + 0.07 * case.governance_review
            + 0.02 * case.communication_clarity
        )
    )


def hash_verification_risk(case: HashVerificationCase) -> float:
    weak_points = [
        1.0 - case.algorithm_inventory,
        1.0 - case.reference_hash_protection,
        1.0 - case.manifest_signing,
        1.0 - case.verification_automation,
        1.0 - case.mismatch_escalation,
        1.0 - case.provenance_metadata,
        1.0 - case.legacy_hash_review,
        1.0 - case.key_or_signature_binding,
        1.0 - case.reproducibility_support,
        1.0 - case.audit_logging,
        1.0 - case.governance_review,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong hash-verification governance"
    if score >= 70 and risk <= 35:
        return "usable integrity workflow with review needs"
    if risk >= 55:
        return "high risk; reference protection, algorithm inventory, manifest signing, automation, provenance, or governance may be weak"
    return "partial discipline; strengthen algorithm inventory, protected references, signed manifests, automation, mismatch escalation, provenance, legacy review, audit logging, and governance"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha3_256_file(path: Path) -> str:
    digest = hashlib.sha3_256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def prepare_demo_artifacts() -> list[Path]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    artifacts = {
        "release_manifest.txt": "file=analysis_report.csv\nversion=1.0\nstatus=approved\n",
        "analysis_report.csv": "record_id,value,verified\nA,42,true\nB,51,true\nC,39,true\n",
        "model_config.json": json.dumps({"model": "demo", "threshold": 0.72, "seed": 1234}, indent=2) + "\n",
        "governance_note.md": "# Verification Note\n\nSynthetic artifact for hash-integrity demonstration.\n",
    }

    paths: list[Path] = []
    for name, content in artifacts.items():
        path = DATA_DIR / name
        path.write_text(content, encoding="utf-8")
        paths.append(path)
    return paths


def build_manifest(paths: list[Path]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for path in sorted(paths):
        rows.append(
            {
                "file_name": path.name,
                "relative_path": str(path.relative_to(ARTICLE_ROOT)),
                "sha256": sha256_file(path),
                "sha3_256": sha3_256_file(path),
                "size_bytes": path.stat().st_size,
            }
        )
    return rows


def verify_manifest(manifest: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for row in manifest:
        path = ARTICLE_ROOT / str(row["relative_path"])
        current_sha256 = sha256_file(path)
        current_sha3 = sha3_256_file(path)
        rows.append(
            {
                "file_name": row["file_name"],
                "expected_sha256": row["sha256"],
                "current_sha256": current_sha256,
                "sha256_verified": hmac.compare_digest(str(row["sha256"]), current_sha256),
                "expected_sha3_256": row["sha3_256"],
                "current_sha3_256": current_sha3,
                "sha3_256_verified": hmac.compare_digest(str(row["sha3_256"]), current_sha3),
            }
        )
    return rows


def tamper_demo(manifest: list[dict[str, object]]) -> list[dict[str, object]]:
    original = DATA_DIR / "analysis_report.csv"
    target = DATA_DIR / "analysis_report_tampered.csv"
    target.write_text(original.read_text(encoding="utf-8").replace("51", "510"), encoding="utf-8")

    original_row = next(row for row in manifest if row["file_name"] == "analysis_report.csv")
    tampered_sha256 = sha256_file(target)
    return [
        {
            "original_file": "analysis_report.csv",
            "tampered_file": target.name,
            "expected_sha256": original_row["sha256"],
            "tampered_sha256": tampered_sha256,
            "verified_against_original": hmac.compare_digest(str(original_row["sha256"]), tampered_sha256),
            "interpretation": "The tampered file fails verification against the original reference digest.",
        }
    ]


def merkle_root_from_hex_digests(hex_digests: list[str]) -> str:
    if not hex_digests:
        return ""
    level = [bytes.fromhex(value) for value in hex_digests]
    while len(level) > 1:
        if len(level) % 2 == 1:
            level.append(level[-1])
        next_level: list[bytes] = []
        for index in range(0, len(level), 2):
            next_level.append(hashlib.sha256(level[index] + level[index + 1]).digest())
        level = next_level
    return level[0].hex()


def merkle_summary(manifest: list[dict[str, object]]) -> dict[str, object]:
    digests = [str(row["sha256"]) for row in sorted(manifest, key=lambda item: str(item["file_name"]))]
    return {
        "leaf_count": len(digests),
        "hash_algorithm": "sha256",
        "merkle_root": merkle_root_from_hex_digests(digests),
        "interpretation": "The Merkle root commits to the ordered set of artifact digests in this synthetic manifest.",
    }


def hmac_demo() -> list[dict[str, object]]:
    key = secrets.token_bytes(32)
    message = b"verified artifact manifest"
    altered_message = b"verified artifact manifest!"
    tag = hmac.new(key, message, hashlib.sha256).hexdigest()
    return [
        {
            "message_case": "original",
            "tag_prefix": tag[:16],
            "verified": hmac.compare_digest(hmac.new(key, message, hashlib.sha256).hexdigest(), tag),
            "interpretation": "Original message verifies with the keyed digest.",
        },
        {
            "message_case": "altered",
            "tag_prefix": tag[:16],
            "verified": hmac.compare_digest(hmac.new(key, altered_message, hashlib.sha256).hexdigest(), tag),
            "interpretation": "Altered message fails verification with the original keyed digest.",
        },
    ]


def build_cases() -> list[HashVerificationCase]:
    return [
        HashVerificationCase(
            case_name="Signed software release manifest",
            system_context="Release workflow publishes file hashes inside a signed manifest.",
            verification_goal="verify artifact integrity and release authenticity before installation",
            algorithm_inventory=0.88,
            reference_hash_protection=0.90,
            manifest_signing=0.92,
            verification_automation=0.84,
            mismatch_escalation=0.82,
            provenance_metadata=0.84,
            legacy_hash_review=0.80,
            key_or_signature_binding=0.90,
            reproducibility_support=0.78,
            audit_logging=0.80,
            governance_review=0.82,
            communication_clarity=0.78,
        ),
        HashVerificationCase(
            case_name="Research data provenance workflow",
            system_context="Research project records hashes of raw data, cleaned data, code, configuration, and outputs.",
            verification_goal="support reproducibility, auditability, and exact artifact comparison",
            algorithm_inventory=0.82,
            reference_hash_protection=0.76,
            manifest_signing=0.62,
            verification_automation=0.80,
            mismatch_escalation=0.72,
            provenance_metadata=0.90,
            legacy_hash_review=0.74,
            key_or_signature_binding=0.60,
            reproducibility_support=0.88,
            audit_logging=0.82,
            governance_review=0.76,
            communication_clarity=0.78,
        ),
        HashVerificationCase(
            case_name="Internal file-transfer checksum process",
            system_context="Team compares published digests after moving files between systems.",
            verification_goal="detect accidental corruption and some unauthorized alteration",
            algorithm_inventory=0.62,
            reference_hash_protection=0.46,
            manifest_signing=0.28,
            verification_automation=0.54,
            mismatch_escalation=0.48,
            provenance_metadata=0.50,
            legacy_hash_review=0.42,
            key_or_signature_binding=0.26,
            reproducibility_support=0.52,
            audit_logging=0.44,
            governance_review=0.40,
            communication_clarity=0.58,
        ),
        HashVerificationCase(
            case_name="Decorative hash publication",
            system_context="Project lists an unspecified hash beside downloads without signing or verification process.",
            verification_goal="claim integrity assurance",
            algorithm_inventory=0.22,
            reference_hash_protection=0.14,
            manifest_signing=0.08,
            verification_automation=0.10,
            mismatch_escalation=0.12,
            provenance_metadata=0.18,
            legacy_hash_review=0.12,
            key_or_signature_binding=0.08,
            reproducibility_support=0.18,
            audit_logging=0.10,
            governance_review=0.12,
            communication_clarity=0.26,
        ),
    ]


def run_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in build_cases():
        score = hash_verification_score(case)
        risk = hash_verification_risk(case)
        rows.append({**asdict(case), "hash_verification_score": round(score, 3), "hash_verification_risk": round(risk, 3), "diagnostic": diagnose(score, risk)})
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


def summarize(audit_rows, manifest, verification_rows, tamper_rows, merkle, hmac_rows) -> dict[str, object]:
    verified_count = sum(1 for row in verification_rows if bool(row["sha256_verified"]) and bool(row["sha3_256_verified"]))
    tamper_detected = sum(1 for row in tamper_rows if not bool(row["verified_against_original"]))
    hmac_failures = sum(1 for row in hmac_rows if not bool(row["verified"]))
    return {
        "case_count": len(audit_rows),
        "average_hash_verification_score": round(mean(float(row["hash_verification_score"]) for row in audit_rows), 3),
        "average_hash_verification_risk": round(mean(float(row["hash_verification_risk"]) for row in audit_rows), 3),
        "highest_score_case": max(audit_rows, key=lambda row: float(row["hash_verification_score"]))["case_name"],
        "highest_risk_case": max(audit_rows, key=lambda row: float(row["hash_verification_risk"]))["case_name"],
        "manifest_artifact_count": len(manifest),
        "fully_verified_artifact_count": verified_count,
        "tamper_detected_count": tamper_detected,
        "hmac_failure_count": hmac_failures,
        "merkle_root": merkle["merkle_root"],
        "interpretation": "Hash verification depends on current algorithms, protected reference values, signed manifests, automation, mismatch escalation, provenance metadata, legacy review, key or signature binding, audit logging, and governance.",
    }


def main() -> None:
    paths = prepare_demo_artifacts()
    manifest = build_manifest(paths)
    verification_rows = verify_manifest(manifest)
    tamper_rows = tamper_demo(manifest)
    merkle = merkle_summary(manifest)
    hmac_rows = hmac_demo()
    audit_rows = run_audit()
    summary = summarize(audit_rows, manifest, verification_rows, tamper_rows, merkle, hmac_rows)

    write_csv(TABLES / "hash_verification_governance_audit.csv", audit_rows)
    write_csv(TABLES / "hash_verification_governance_summary.csv", [summary])
    write_csv(TABLES / "hash_manifest.csv", manifest)
    write_csv(TABLES / "hash_verification_results.csv", verification_rows)
    write_csv(TABLES / "tamper_detection_demo.csv", tamper_rows)
    write_csv(TABLES / "hmac_verification_demo.csv", hmac_rows)

    write_json(JSON_DIR / "hash_verification_governance_audit.json", audit_rows)
    write_json(JSON_DIR / "hash_verification_governance_summary.json", summary)
    write_json(JSON_DIR / "hash_manifest.json", manifest)
    write_json(JSON_DIR / "hash_verification_results.json", verification_rows)
    write_json(JSON_DIR / "tamper_detection_demo.json", tamper_rows)
    write_json(JSON_DIR / "merkle_summary.json", merkle)
    write_json(JSON_DIR / "hmac_verification_demo.json", hmac_rows)

    print("Hash functions, integrity, and verification audit complete.")
    print(TABLES / "hash_verification_governance_audit.csv")
    print("Merkle root:", merkle["merkle_root"][:32] + "...")
    print("Tamper detected count:", summary["tamper_detected_count"])


if __name__ == "__main__":
    main()
