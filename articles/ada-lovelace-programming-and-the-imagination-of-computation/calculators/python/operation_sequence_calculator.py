from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Summarize an ordered operation sequence.")
parser.add_argument("--operations", type=str, required=True, help="Comma-separated operations, e.g. multiply,subtract,store,repeat")
args = parser.parse_args()

ops = [op.strip() for op in args.operations.split(",") if op.strip()]
print(f"operation_count={len(ops)}")
print(f"first_operation={ops[0] if ops else 'none'}")
print(f"last_operation={ops[-1] if ops else 'none'}")
print(f"has_repetition={str(any(op in {'repeat','loop','iterate'} for op in ops)).lower()}")
print("sequence=" + " -> ".join(ops))
