from __future__ import annotations
import argparse
parser = argparse.ArgumentParser(description="Estimate abstraction and representation loss.")
parser.add_argument("--omitted-context", type=float, required=True)
parser.add_argument("--measurement-error", type=float, required=True)
parser.add_argument("--proxy-distance", type=float, required=True)
parser.add_argument("--temporal-drift", type=float, required=True)
args = parser.parse_args()
loss = (args.omitted_context + args.measurement_error + args.proxy_distance + args.temporal_drift) / 4.0
print(f"representation_loss={loss:.6f}")
