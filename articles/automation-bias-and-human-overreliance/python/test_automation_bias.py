from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import automation_bias_human_overreliance_audit as audit


def test_automation_bias_audit_detects_escalations() -> None:
    config = audit.AutomationBiasConfig()
    rows = [audit.audit_oversight(row, config) for row in audit.oversight_cases()]
    assert any(row["status"] == "escalate" for row in rows)


def test_overreliance_gap_is_positive_difference() -> None:
    config = audit.AutomationBiasConfig()
    row = audit.audit_oversight(audit.oversight_cases()[1], config)
    assert abs(row["overreliance_gap"] - max(0.0, row["acceptance_rate"] - row["model_quality"])) < 1e-9


def test_governance_register_has_override_logging() -> None:
    rows = audit.governance_register()
    assert any(row["item"] == "override_logging" for row in rows)


def main() -> None:
    test_automation_bias_audit_detects_escalations()
    test_overreliance_gap_is_positive_difference()
    test_governance_register_has_override_logging()
    print("All automation bias tests passed.")


if __name__ == "__main__":
    main()
