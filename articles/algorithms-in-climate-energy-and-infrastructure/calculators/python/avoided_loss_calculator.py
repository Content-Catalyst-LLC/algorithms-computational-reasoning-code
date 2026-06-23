from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute avoided expected loss.")
parser.add_argument("--loss-without", type=float, required=True)
parser.add_argument("--loss-with", type=float, required=True)
args = parser.parse_args()

benefit = args.loss_without - args.loss_with
print(f"avoided_expected_loss={benefit:.6f}")
