from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute simple transmission-weight score.")
parser.add_argument("--languages", type=float, required=True, help="Normalized language-crossing score in [0, 1].")
parser.add_argument("--teaching", type=float, required=True, help="Normalized teaching/curriculum score in [0, 1].")
parser.add_argument("--manuscript", type=float, required=True, help="Normalized manuscript/copying score in [0, 1].")
parser.add_argument("--practical-use", type=float, required=True, help="Normalized practical-use score in [0, 1].")
args = parser.parse_args()

score = (args.languages + args.teaching + args.manuscript + args.practical_use) / 4.0
print(f"transmission_weight_score={score:.6f}")
