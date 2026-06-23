from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate maintenance burden from code size, readability, documentation, and tests.")
parser.add_argument("--lines-of-code", type=float, required=True)
parser.add_argument("--readability", type=float, required=True, help="0 to 1, higher is better")
parser.add_argument("--documentation", type=float, required=True, help="0 to 1, higher is better")
parser.add_argument("--test-coverage", type=float, required=True, help="0 to 1, higher is better")
args = parser.parse_args()

quality = max(0.01, (args.readability + args.documentation + args.test_coverage) / 3.0)
burden = args.lines_of_code / (1000.0 * quality)
print(f"maintenance_burden_index={burden:.6f}")
