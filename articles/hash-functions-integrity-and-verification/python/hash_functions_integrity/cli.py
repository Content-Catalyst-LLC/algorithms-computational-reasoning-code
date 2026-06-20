#!/usr/bin/env python3
"""Small CLI for hash verification demo outputs."""

from __future__ import annotations

import csv
from pathlib import Path

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
SUMMARY_PATH = ARTICLE_ROOT / "outputs" / "tables" / "hash_verification_governance_summary.csv"
OUT_PATH = ARTICLE_ROOT / "outputs" / "cli" / "hash_verification_cli_summary.txt"


def main() -> None:
    if not SUMMARY_PATH.exists():
        raise SystemExit("Run python/hash_functions_integrity/audit.py first.")
    with SUMMARY_PATH.open(newline="", encoding="utf-8") as handle:
        row = next(csv.DictReader(handle))
    lines = [
        "Hash Functions, Integrity, and Verification CLI Summary",
        f"Cases: {row['case_count']}",
        f"Average score: {row['average_hash_verification_score']}",
        f"Average risk: {row['average_hash_verification_risk']}",
        f"Highest score case: {row['highest_score_case']}",
        f"Highest risk case: {row['highest_risk_case']}",
        f"Manifest artifacts: {row['manifest_artifact_count']}",
        f"Tamper detected count: {row['tamper_detected_count']}",
        f"Merkle root prefix: {row['merkle_root'][:32]}",
    ]
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
