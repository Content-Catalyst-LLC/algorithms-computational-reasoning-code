from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import metrics_objectives_goodharts_law_audit as audit


def test_goodhart_audit_detects_escalations() -> None:
    config = audit.GoodhartAuditConfig()
    rows = [audit.audit_case(row, config) for row in audit.metric_cases()]
    assert any(row["status"] == "escalate" for row in rows)


def test_proxy_gap_is_one_minus_alignment() -> None:
    config = audit.GoodhartAuditConfig()
    row = audit.audit_case(audit.metric_cases()[0], config)
    assert abs(row["proxy_gap"] - (1.0 - row["proxy_alignment"])) < 1e-9


def test_guardrail_register_has_required_items() -> None:
    guardrails = audit.guardrail_register()
    assert len(guardrails) >= 3
    assert any(row["guardrail"] == "drift_monitor" for row in guardrails)


def main() -> None:
    test_goodhart_audit_detects_escalations()
    test_proxy_gap_is_one_minus_alignment()
    test_guardrail_register_has_required_items()
    print("All Goodhart metric tests passed.")


if __name__ == "__main__":
    main()
