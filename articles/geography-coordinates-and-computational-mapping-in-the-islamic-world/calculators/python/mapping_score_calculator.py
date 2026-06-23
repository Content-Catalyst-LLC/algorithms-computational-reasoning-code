from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for computational mapping.")
parser.add_argument("--spatial-representation", type=float, required=True)
parser.add_argument("--coordinate-structure", type=float, required=True)
parser.add_argument("--procedural-clarity", type=float, required=True)
parser.add_argument("--institutional-use", type=float, required=True)
parser.add_argument("--correction-awareness", type=float, required=True)
parser.add_argument("--transmission-importance", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.spatial_representation +
    args.coordinate_structure +
    args.procedural_clarity +
    args.institutional_use +
    args.correction_awareness +
    args.transmission_importance +
    args.modern_resonance
) / 7.0
print(f"mapping_score={score:.6f}")
