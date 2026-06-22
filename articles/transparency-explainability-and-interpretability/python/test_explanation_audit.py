from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import transparency_explainability_interpretability_audit as audit


def test_explanation_audit_detects_review_or_escalation() -> None:
    config = audit.ExplanationAuditConfig()
    rows = [audit.score_explanation(row, config) for row in audit.explanation_cases()]
    assert any(row["status"] in {"review", "escalate"} for row in rows)


def test_explanation_scores_are_bounded() -> None:
    config = audit.ExplanationAuditConfig()
    row = audit.score_explanation(audit.explanation_cases()[0], config)
    assert 0.0 <= row["explanation_quality_score"] <= 1.0
    assert 0.0 <= row["transparency_capacity_score"] <= 1.0
    assert 0.0 <= row["accountability_capacity_score"] <= 1.0


def test_governance_register_has_contestability() -> None:
    rows = audit.governance_register()
    assert any(row["item"] == "contestability" for row in rows)


def main() -> None:
    test_explanation_audit_detects_review_or_escalation()
    test_explanation_scores_are_bounded()
    test_governance_register_has_contestability()
    print("All transparency, explainability, and interpretability tests passed.")


if __name__ == "__main__":
    main()
