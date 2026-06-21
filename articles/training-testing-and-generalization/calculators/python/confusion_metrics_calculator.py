from __future__ import annotations
import argparse
parser = argparse.ArgumentParser(description="Compute accuracy, precision, recall, and F1 from confusion counts.")
parser.add_argument("--tp", type=int, required=True)
parser.add_argument("--tn", type=int, required=True)
parser.add_argument("--fp", type=int, required=True)
parser.add_argument("--fn", type=int, required=True)
args = parser.parse_args()
total = args.tp + args.tn + args.fp + args.fn
if total <= 0: raise SystemExit("confusion counts must sum to a positive value")
accuracy = (args.tp + args.tn) / total
precision = args.tp / max(1, args.tp + args.fp)
recall = args.tp / max(1, args.tp + args.fn)
f1 = 0.0 if precision + recall == 0 else 2 * precision * recall / (precision + recall)
print(f"accuracy={accuracy:.6f}")
print(f"precision={precision:.6f}")
print(f"recall={recall:.6f}")
print(f"f1={f1:.6f}")
