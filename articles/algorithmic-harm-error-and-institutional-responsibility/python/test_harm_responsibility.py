from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithmic_harm_error_institutional_responsibility_audit as audit


def test_harm_audit_detects_escalations() -> None:
    config = audit.HarmResponsibilityConfig()
    rows = [audit.audit_harm(row, config) for row in audit.harm_contexts()]
    assert any(row["status"] == "escalate" for row in rows)


def test_harm_risk_is_nonnegative() -> None:
    config = audit.HarmResponsibilityConfig()
    row = audit.audit_harm(audit.harm_contexts()[0], config)
    assert row["harm_risk_score"] >= 0.0


def test_incident_register_has_remediation_status() -> None:
    rows = audit.incident_register()
    assert any(row["field"] == "remediation_status" for row in rows)


def main() -> None:
    test_harm_audit_detects_escalations()
    test_harm_risk_is_nonnegative()
    test_incident_register_has_remediation_status()
    print("All harm and responsibility tests passed.")


if __name__ == "__main__":
    main()
