from __future__ import annotations

import argparse
import json
import math


def reproducibility_score(has_code: bool, has_data: bool, has_parameters: bool, has_seed: bool, has_environment: bool, has_manifest: bool, has_validation: bool) -> dict[str, object]:
    checks = {
        "code": has_code,
        "data": has_data,
        "parameters": has_parameters,
        "seed": has_seed,
        "environment": has_environment,
        "manifest": has_manifest,
        "validation": has_validation,
    }
    score = sum(1 for value in checks.values() if value) / len(checks)
    return {
        "checks": checks,
        "score": round(score, 4),
        "percentage": round(100.0 * score, 2),
        "interpretation": "Higher score indicates more complete reproducibility evidence, not automatic model validity.",
    }


def monte_carlo_sample_error(std_dev: float, samples: int) -> dict[str, float]:
    if samples <= 0:
        raise ValueError("samples must be positive")
    standard_error = std_dev / math.sqrt(samples)
    return {
        "std_dev": std_dev,
        "samples": samples,
        "standard_error": round(standard_error, 8),
        "approx_95_margin": round(1.96 * standard_error, 8),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Small calculators for reproducible computational workflows.")
    parser.add_argument("--std-dev", type=float, default=10.0)
    parser.add_argument("--samples", type=int, default=1000)
    args = parser.parse_args()

    payload = {
        "reproducibility_score": reproducibility_score(True, True, True, True, True, True, False),
        "sample_error": monte_carlo_sample_error(args.std_dev, args.samples),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
