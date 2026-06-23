from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute procedural readiness.")
parser.add_argument("--due-process", type=float, required=True)
parser.add_argument("--transparency", type=float, required=True)
parser.add_argument("--human-review", type=float, required=True)
parser.add_argument("--appeal-readiness", type=float, required=True)
args = parser.parse_args()

score = (args.due_process + args.transparency + args.human_review + args.appeal_readiness) / 4.0
print(f"procedural_readiness_score={score:.6f}")
