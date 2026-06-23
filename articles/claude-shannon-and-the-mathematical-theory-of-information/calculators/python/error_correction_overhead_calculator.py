from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate redundancy overhead from payload and total encoded bits.")
parser.add_argument("--payload-bits", type=float, required=True)
parser.add_argument("--encoded-bits", type=float, required=True)
args = parser.parse_args()

if args.payload_bits <= 0 or args.encoded_bits <= 0:
    raise SystemExit("bit counts must be positive")
overhead = args.encoded_bits - args.payload_bits
rate = args.payload_bits / args.encoded_bits
print(f"redundancy_overhead_bits={overhead:.6f}")
print(f"code_rate={rate:.9f}")
