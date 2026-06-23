from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute learning gain = posttest - pretest.")
parser.add_argument("--pretest", type=float, required=True)
parser.add_argument("--posttest", type=float, required=True)
args = parser.parse_args()

gain = args.posttest - args.pretest
print(f"learning_gain={gain:.6f}")
