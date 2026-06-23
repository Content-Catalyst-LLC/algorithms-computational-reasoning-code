from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compare adjacency matrix and adjacency list storage units.")
parser.add_argument("--nodes", type=int, required=True)
parser.add_argument("--edges", type=int, required=True)
args = parser.parse_args()

if args.nodes < 0 or args.edges < 0:
    raise SystemExit("nodes and edges must be nonnegative")
matrix = args.nodes * args.nodes
adj_list = args.nodes + args.edges
print(f"adjacency_matrix_cells={matrix}")
print(f"adjacency_list_units={adj_list}")
print("more_compact=" + ("adjacency_list" if adj_list < matrix else "adjacency_matrix_or_tie"))
