from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithmic_risk_management_ai_governance_audit as audit


def test_risk_governance_audit_detects_review_or_escalation() -> None:
    config = audit.RiskGovernanceConfig()
    rows = [audit.score_risk(row, config) for row in audit.risk_items()]
    assert any(row["status"] in {"review", "escalate"} for row in rows)


def test_scores_are_bounded_or_nonnegative() -> None:
    config = audit.RiskGovernanceConfig()
    row = audit.score_risk(audit.risk_items()[0], config)
    assert 0.0 <= row["inherent_risk_score"] <= 1.0
    assert 0.0 <= row["governance_readiness_score"] <= 1.0
    assert row["residual_risk_score"] >= 0.0


def test_governance_controls_have_pause_authority() -> None:
    rows = audit.governance_controls()
    assert any(row["control"] == "pause_retirement_authority" for row in rows)


def main() -> None:
    test_risk_governance_audit_detects_review_or_escalation()
    test_scores_are_bounded_or_nonnegative()
    test_governance_controls_have_pause_authority()
    print("All algorithmic risk management and AI governance tests passed.")


if __name__ == "__main__":
    main()
