from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Compute idealized AWGN capacity C = B log2(1 + SNR).")
parser.add_argument("--bandwidth-hz", type=float, required=True)
parser.add_argument("--snr", type=float, required=True, help="Linear signal-to-noise ratio, not dB.")
args = parser.parse_args()

if args.bandwidth_hz < 0 or args.snr < 0:
    raise SystemExit("bandwidth and snr must be nonnegative")
capacity = args.bandwidth_hz * math.log2(1 + args.snr)
print(f"capacity_bits_per_second={capacity:.6f}")
