from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import contestability_appeals_algorithmic_due_process_audit as audit


def test_due_process_audit_detects_escalations() -> None:
    config = audit.DueProcessConfig()
    rows = [audit.audit_context(row, config) for row in audit.decision_contexts()]
    assert any(row["status"] == "escalate" for row in rows)


def test_contestability_score_between_zero_and_one() -> None:
    config = audit.DueProcessConfig()
    row = audit.audit_context(audit.decision_contexts()[0], config)
    assert 0.0 <= row["contestability_score"] <= 1.0


def test_governance_register_has_audit_trail() -> None:
    rows = audit.governance_register()
    assert any(row["item"] == "audit_trail" for row in rows)


def main() -> None:
    test_due_process_audit_detects_escalations()
    test_contestability_score_between_zero_and_one()
    test_governance_register_has_audit_trail()
    print("All due-process tests passed.")


if __name__ == "__main__":
    main()
