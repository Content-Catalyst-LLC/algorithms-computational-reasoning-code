from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compare high-level generated runtime to hand-coded baseline.")
parser.add_argument("--generated-runtime", type=float, required=True)
parser.add_argument("--handcoded-runtime", type=float, required=True)
args = parser.parse_args()

if args.generated_runtime <= 0 or args.handcoded_runtime <= 0:
    raise SystemExit("runtimes must be positive")
ratio = args.generated_runtime / args.handcoded_runtime
if ratio <= 1.20:
    status = "high_performance_credibility"
elif ratio <= 2.00:
    status = "moderate_performance_credibility"
else:
    status = "low_performance_credibility"
print(f"runtime_ratio_generated_to_handcoded={ratio:.6f}")
print(f"status={status}")
