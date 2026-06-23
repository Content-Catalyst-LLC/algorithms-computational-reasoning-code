from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Toy cam activation check using rotation angle.")
parser.add_argument("--angle", type=float, required=True)
parser.add_argument("--activation-angle", type=float, required=True)
parser.add_argument("--tolerance", type=float, default=5.0)
args = parser.parse_args()

angle = args.angle % 360.0
activation = args.activation_angle % 360.0
distance = min(abs(angle - activation), 360.0 - abs(angle - activation))
active = distance <= args.tolerance
print(f"cam_active={str(active).lower()}")
print(f"angle_distance={distance:.6f}")
