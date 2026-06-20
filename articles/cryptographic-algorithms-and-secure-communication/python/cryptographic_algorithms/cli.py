#!/usr/bin/env python3
"""Small CLI summary for cryptographic algorithms and secure communication."""

from __future__ import annotations

from pathlib import Path
import csv
import sys

CURRENT = Path(__file__).resolve()
if str(CURRENT.parent) not in sys.path:
    sys.path.insert(0, str(CURRENT.parent))

from audit import educational_message_authentication_demo, run_audit  # noqa: E402

ARTICLE_ROOT = CURRENT.parents[2]
OUTPUT = ARTICLE_ROOT / "outputs" / "cli" / "secure_communication_cli_summary.csv"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    audit_rows = run_audit()
    auth_rows = educational_message_authentication_demo()

    summary_rows = [
        {
            "metric": "case_count",
            "value": len(audit_rows),
            "interpretation": "Number of secure-communication governance cases evaluated.",
        },
        {
            "metric": "highest_risk_case",
            "value": max(audit_rows, key=lambda row: float(row["secure_communication_risk"]))["case_name"],
            "interpretation": "Case with the weakest governance posture in the synthetic audit.",
        },
        {
            "metric": "message_authentication_demo_checks",
            "value": len(auth_rows),
            "interpretation": "Educational HMAC verification checks generated with Python's standard library.",
        },
    ]

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["metric", "value", "interpretation"])
        writer.writeheader()
        writer.writerows(summary_rows)

    for row in summary_rows:
        print(f"{row['metric']}: {row['value']}")
    print(OUTPUT)


if __name__ == "__main__":
    main()
