from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import feedback_loops_algorithmic_systems_audit as audit


def test_feedback_audit_detects_escalations() -> None:
    config = audit.FeedbackAuditConfig()
    rows = [audit.audit_feedback(row, config) for row in audit.feedback_cases()]
    assert any(row["status"] == "escalate" for row in rows)


def test_feedback_risk_has_expected_fields() -> None:
    config = audit.FeedbackAuditConfig()
    row = audit.audit_feedback(audit.feedback_cases()[0], config)
    assert "feedback_risk_score" in row
    assert "high_amplification" in row
    assert "high_concentration" in row


def test_governance_register_has_feedback_map() -> None:
    rows = audit.feedback_governance_register()
    assert any(row["item"] == "feedback_map" for row in rows)


def main() -> None:
    test_feedback_audit_detects_escalations()
    test_feedback_risk_has_expected_fields()
    test_governance_register_has_feedback_map()
    print("All feedback-loop tests passed.")


if __name__ == "__main__":
    main()
