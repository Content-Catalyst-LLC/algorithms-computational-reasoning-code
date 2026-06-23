from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compare compute throughput and memory-bandwidth-limited throughput.")
parser.add_argument("--compute-ops-per-sec", type=float, required=True)
parser.add_argument("--bytes-per-op", type=float, required=True)
parser.add_argument("--memory-gb-per-sec", type=float, required=True)
args = parser.parse_args()

memory_ops_per_sec = (args.memory_gb_per_sec * 1_000_000_000) / args.bytes_per_op
effective_ops = min(args.compute_ops_per_sec, memory_ops_per_sec)
limiter = "compute" if args.compute_ops_per_sec <= memory_ops_per_sec else "memory_bandwidth"
print(f"memory_limited_ops_per_sec={memory_ops_per_sec:.6f}")
print(f"effective_ops_per_sec={effective_ops:.6f}")
print(f"limiting_factor={limiter}")
