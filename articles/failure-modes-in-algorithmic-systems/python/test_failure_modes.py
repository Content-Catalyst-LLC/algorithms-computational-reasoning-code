from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import failure_modes_algorithmic_systems_audit as audit


def test_failure_audit_detects_review_or_escalation() -> None:
    config = audit.FailureModeConfig()
    rows = [audit.audit_failure(row, config) for row in audit.failure_modes()]
    assert any(row["status"] in {"review", "escalate"} for row in rows)


def test_failure_risk_is_nonnegative() -> None:
    config = audit.FailureModeConfig()
    row = audit.audit_failure(audit.failure_modes()[0], config)
    assert row["failure_risk_score"] >= 0.0


def test_governance_register_has_rollback() -> None:
    rows = audit.governance_register()
    assert any(row["item"] == "rollback" for row in rows)


def main() -> None:
    test_failure_audit_detects_review_or_escalation()
    test_failure_risk_is_nonnegative()
    test_governance_register_has_rollback()
    print("All failure-mode tests passed.")


if __name__ == "__main__":
    main()
