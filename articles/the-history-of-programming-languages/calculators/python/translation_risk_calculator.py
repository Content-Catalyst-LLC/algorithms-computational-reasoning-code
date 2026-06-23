from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate risk across source, translator, runtime, and dependencies.")
parser.add_argument("--source-ambiguity", type=float, required=True)
parser.add_argument("--translator-risk", type=float, required=True)
parser.add_argument("--runtime-risk", type=float, required=True)
parser.add_argument("--dependency-risk", type=float, required=True)
parser.add_argument("--test-coverage-gap", type=float, required=True)
args = parser.parse_args()

risk = (
    args.source_ambiguity +
    args.translator_risk +
    args.runtime_risk +
    args.dependency_risk +
    args.test_coverage_gap
) / 5.0
print(f"translation_layer_risk={risk:.6f}")
