from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import proxy_variables_measurement_error_audit as audit


def test_proxy_audit_detects_escalations() -> None:
    config = audit.ProxyAuditConfig()
    rows = [audit.audit_proxy(row, config) for row in audit.proxy_cases()]
    assert any(row["status"] == "escalate" for row in rows)


def test_validity_gap_is_one_minus_validity() -> None:
    config = audit.ProxyAuditConfig()
    row = audit.audit_proxy(audit.proxy_cases()[0], config)
    assert abs(row["validity_gap"] - (1.0 - row["proxy_validity"])) < 1e-9


def test_governance_register_has_construct_definition() -> None:
    rows = audit.measurement_governance_register()
    assert any(row["item"] == "construct_definition" for row in rows)


def main() -> None:
    test_proxy_audit_detects_escalations()
    test_validity_gap_is_one_minus_validity()
    test_governance_register_has_construct_definition()
    print("All proxy measurement-error tests passed.")


if __name__ == "__main__":
    main()
