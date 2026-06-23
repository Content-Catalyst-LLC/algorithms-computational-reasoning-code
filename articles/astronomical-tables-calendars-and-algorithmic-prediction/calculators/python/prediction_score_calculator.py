from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for astronomical prediction.")
parser.add_argument("--table-structure", type=float, required=True)
parser.add_argument("--procedural-clarity", type=float, required=True)
parser.add_argument("--predictive-function", type=float, required=True)
parser.add_argument("--institutional-use", type=float, required=True)
parser.add_argument("--correction-awareness", type=float, required=True)
parser.add_argument("--transmission-importance", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.table_structure +
    args.procedural_clarity +
    args.predictive_function +
    args.institutional_use +
    args.correction_awareness +
    args.transmission_importance +
    args.modern_resonance
) / 7.0
print(f"prediction_score={score:.6f}")
