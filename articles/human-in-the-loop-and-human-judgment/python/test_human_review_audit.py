from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import human_in_the_loop_judgment_audit as audit


def test_human_review_audit_detects_review_or_escalation() -> None:
    config = audit.HumanReviewConfig()
    rows = [audit.score_review_context(row, config) for row in audit.review_contexts()]
    assert any(row["status"] in {"review", "escalate"} for row in rows)


def test_scores_are_bounded() -> None:
    config = audit.HumanReviewConfig()
    row = audit.score_review_context(audit.review_contexts()[0], config)
    assert 0.0 <= row["review_capacity_score"] <= 1.0
    assert 0.0 <= row["reliance_score"] <= 1.0
    assert 0.0 <= row["override_rate"] <= 1.0
    assert 0.0 <= row["judgment_capacity_score"] <= 1.0


def test_governance_register_has_review_authority() -> None:
    rows = audit.governance_register()
    assert any(row["item"] == "review_authority" for row in rows)


def main() -> None:
    test_human_review_audit_detects_review_or_escalation()
    test_scores_are_bounded()
    test_governance_register_has_review_authority()
    print("All human-in-the-loop and human judgment tests passed.")


if __name__ == "__main__":
    main()
