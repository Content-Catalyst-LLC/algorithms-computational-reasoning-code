from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute expected loss: EL = PD * LGD * EAD.")
parser.add_argument("--pd", type=float, required=True, help="Probability of default")
parser.add_argument("--lgd", type=float, required=True, help="Loss given default")
parser.add_argument("--ead", type=float, required=True, help="Exposure at default")
args = parser.parse_args()

expected_loss = args.pd * args.lgd * args.ead
print(f"expected_loss={expected_loss:.6f}")
