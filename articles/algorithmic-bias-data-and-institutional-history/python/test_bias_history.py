from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithmic_bias_data_institutional_history_audit as audit


def test_bias_audit_detects_review_or_escalation() -> None:
    config = audit.BiasHistoryConfig()
    metrics = [audit.compute_group_bias_metrics(row) for row in audit.group_history_records()]
    result = audit.audit_bias(metrics, config)
    assert result["status"] in {"review", "escalate"}


def test_group_bias_metrics_are_bounded() -> None:
    metric = audit.compute_group_bias_metrics(audit.group_history_records()[0])
    assert 0.0 <= metric["representation_gap"] <= 1.0
    assert 0.0 <= metric["label_gap"] <= 1.0
    assert 0.0 <= metric["historical_risk_score"] <= 1.0


def test_governance_register_has_provenance() -> None:
    rows = audit.governance_register()
    assert any(row["item"] == "data_provenance" for row in rows)


def main() -> None:
    test_bias_audit_detects_review_or_escalation()
    test_group_bias_metrics_are_bounded()
    test_governance_register_has_provenance()
    print("All bias, data, and institutional history tests passed.")


if __name__ == "__main__":
    main()
