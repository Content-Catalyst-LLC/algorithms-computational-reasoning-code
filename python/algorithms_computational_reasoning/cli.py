from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def complexity_demo() -> dict[str, list[float]]:
    n_values = [1, 10, 100, 1000]
    return {
        "n": n_values,
        "linear": [float(n) for n in n_values],
        "n_log_n": [float(n * math.log2(n)) for n in n_values],
        "quadratic": [float(n * n) for n in n_values],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Algorithms & Computational Reasoning demos")
    parser.add_argument("--demo", default="all", choices=["all", "complexity"])
    parser.parse_args()

    outputs = Path("outputs")
    outputs.mkdir(exist_ok=True)

    result = {"complexity": complexity_demo()}
    (outputs / "python_demo_output.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
