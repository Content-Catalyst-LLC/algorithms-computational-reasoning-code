#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from math import log2
from pathlib import Path


def estimate(n: int) -> dict[str, float | int]:
    if n <= 0:
        raise ValueError("n must be positive")
    return {
        "n": n,
        "constant": 1,
        "log_n": round(log2(max(2, n)), 6),
        "linear": n,
        "n_log_n": round(n * log2(max(2, n)), 6),
        "quadratic": n * n,
        "exponential_2_power_n_warning": "Only compute exact 2^n for small n in production contexts."
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple complexity-growth calculator.")
    parser.add_argument("--n", type=int, default=1024)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    args = parser.parse_args()

    result = estimate(args.n)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "complexity_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
