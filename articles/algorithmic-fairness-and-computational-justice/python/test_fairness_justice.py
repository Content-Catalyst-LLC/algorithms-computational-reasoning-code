from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithmic_fairness_computational_justice_audit as audit


def test_fairness_audit_detects_review_or_escalation() -> None:
    config = audit.FairnessJusticeConfig()
    metrics = [audit.compute_group_metrics(row) for row in audit.group_records()]
    result = audit.audit_fairness(metrics, config)
    assert result["status"] in {"review", "escalate"}


def test_group_metrics_are_bounded() -> None:
    metric = audit.compute_group_metrics(audit.group_records()[0])
    assert 0.0 <= metric["selection_rate"] <= 1.0
    assert 0.0 <= metric["false_positive_rate"] <= 1.0
    assert 0.0 <= metric["false_negative_rate"] <= 1.0
    assert 0.0 <= metric["justice_capacity_score"] <= 1.0


def test_governance_register_has_contestability() -> None:
    rows = audit.governance_register()
    assert any(row["item"] == "contestability" for row in rows)


def main() -> None:
    test_fairness_audit_detects_review_or_escalation()
    test_group_metrics_are_bounded()
    test_governance_register_has_contestability()
    print("All fairness and computational justice tests passed.")


if __name__ == "__main__":
    main()
