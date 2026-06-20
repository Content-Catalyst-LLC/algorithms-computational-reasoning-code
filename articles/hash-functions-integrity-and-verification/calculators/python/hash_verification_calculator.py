#!/usr/bin/env python3
"""Self-contained hash verification calculator."""

from __future__ import annotations

from pathlib import Path
import csv
import hashlib
import hmac

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
OUT = ARTICLE_ROOT / "calculators" / "outputs" / "hash_verification_calculator.csv"


def digest_text(text: str, algorithm: str = "sha256") -> str:
    if algorithm == "sha256":
        return hashlib.sha256(text.encode("utf-8")).hexdigest()
    if algorithm == "sha3_256":
        return hashlib.sha3_256(text.encode("utf-8")).hexdigest()
    raise ValueError(f"Unsupported algorithm: {algorithm}")


def main() -> None:
    rows = []
    original = "verified artifact manifest"
    altered = "verified artifact manifest!"
    expected = digest_text(original)
    for label, text in [("original", original), ("altered", altered)]:
        actual = digest_text(text)
        rows.append({
            "case": label,
            "algorithm": "sha256",
            "digest_prefix": actual[:16],
            "matches_original": hmac.compare_digest(expected, actual),
            "text_length": len(text),
        })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(OUT)


if __name__ == "__main__":
    main()
