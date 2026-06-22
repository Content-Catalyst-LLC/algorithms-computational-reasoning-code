from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithmic_accountability_audit_trails_review as audit


def test_accountability_audit_detects_review_or_escalation() -> None:
    config = audit.AccountabilityConfig()
    rows = [audit.score_system(row, config) for row in audit.system_records()]
    assert any(row["status"] in {"review", "escalate"} for row in rows)


def test_scores_are_bounded() -> None:
    config = audit.AccountabilityConfig()
    row = audit.score_system(audit.system_records()[0], config)
    assert 0.0 <= row["audit_completeness_score"] <= 1.0
    assert 0.0 <= row["accountability_capacity_score"] <= 1.0
    assert row["reconstruction_risk_score"] >= 0.0


def test_governance_register_has_ownership() -> None:
    rows = audit.governance_register()
    assert any(row["item"] == "ownership" for row in rows)


def main() -> None:
    test_accountability_audit_detects_review_or_escalation()
    test_scores_are_bounded()
    test_governance_register_has_ownership()
    print("All algorithmic accountability and audit trail tests passed.")


if __name__ == "__main__":
    main()
