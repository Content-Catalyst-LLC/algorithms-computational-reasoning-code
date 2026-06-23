from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate language ecosystem strength.")
parser.add_argument("--compiler-or-interpreter", type=float, required=True)
parser.add_argument("--standard-library", type=float, required=True)
parser.add_argument("--package-manager", type=float, required=True)
parser.add_argument("--documentation", type=float, required=True)
parser.add_argument("--community", type=float, required=True)
parser.add_argument("--institutional-use", type=float, required=True)
args = parser.parse_args()

score = (
    args.compiler_or_interpreter +
    args.standard_library +
    args.package_manager +
    args.documentation +
    args.community +
    args.institutional_use
) / 6.0
print(f"ecosystem_score={score:.6f}")
