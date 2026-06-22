from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import responsible_automation_delegation_audit as audit


def test_delegation_audit_detects_escalation() -> None:
    config = audit.DelegationConfig()
    rows = [audit.score_context(row, config) for row in audit.delegation_contexts()]
    assert any(row["status"] == "escalate" for row in rows)


def test_scores_are_bounded() -> None:
    config = audit.DelegationConfig()
    row = audit.score_context(audit.delegation_contexts()[0], config)
    assert 0.0 <= row["delegation_readiness_score"] <= 1.0
    assert 0.0 <= row["automation_reliance_score"] <= 1.0
    assert row["delegation_risk_score"] >= 0.0


def test_governance_register_has_rollback() -> None:
    rows = audit.governance_register()
    assert any(row["item"] == "rollback_retirement" for row in rows)


def main() -> None:
    test_delegation_audit_detects_escalation()
    test_scores_are_bounded()
    test_governance_register_has_rollback()
    print("All responsible automation and decision delegation tests passed.")


if __name__ == "__main__":
    main()
