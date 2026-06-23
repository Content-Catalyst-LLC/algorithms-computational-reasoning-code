from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for computational knowledge transfer.")
parser.add_argument("--procedural-fidelity", type=float, required=True)
parser.add_argument("--vocabulary-mapping", type=float, required=True)
parser.add_argument("--diagram-table-preservation", type=float, required=True)
parser.add_argument("--institutional-support", type=float, required=True)
parser.add_argument("--error-control", type=float, required=True)
parser.add_argument("--adaptation", type=float, required=True)
parser.add_argument("--historical-significance", type=float, required=True)
parser.add_argument("--ethical-caution", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.procedural_fidelity +
    args.vocabulary_mapping +
    args.diagram_table_preservation +
    args.institutional_support +
    args.error_control +
    args.adaptation +
    args.historical_significance +
    args.ethical_caution +
    args.modern_resonance
) / 9.0
print(f"transfer_score={score:.6f}")
