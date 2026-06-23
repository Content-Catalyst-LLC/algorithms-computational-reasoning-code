from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Trace a toy worked example: double input, add adjustment, check target.")
parser.add_argument("--input", type=float, required=True)
parser.add_argument("--adjustment", type=float, required=True)
parser.add_argument("--target", type=float, required=True)
args = parser.parse_args()

intermediate = args.input * 2
output = intermediate + args.adjustment
residual = output - args.target
print(f"input={args.input:.6f}")
print(f"intermediate_double={intermediate:.6f}")
print(f"output_after_adjustment={output:.6f}")
print(f"target={args.target:.6f}")
print(f"residual={residual:.6f}")
print(f"check_passed={str(abs(residual) < 1e-9).lower()}")
