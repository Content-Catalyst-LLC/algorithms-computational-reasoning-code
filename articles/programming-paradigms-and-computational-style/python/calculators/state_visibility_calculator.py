#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def compute(
    mutable_state_sites: int,
    explicit_state_records: int,
    side_effect_boundaries: int,
    audited_effects: int,
) -> dict[str, object]:
    total_state_sites = max(1, mutable_state_sites)
    explicit_ratio = min(1.0, explicit_state_records / total_state_sites)
    audit_ratio = min(1.0, audited_effects / max(1, side_effect_boundaries))
    visibility = round(100.0 * (0.6 * explicit_ratio + 0.4 * audit_ratio), 2)
    return {
        "mutable_state_sites": mutable_state_sites,
        "explicit_state_records": explicit_state_records,
        "side_effect_boundaries": side_effect_boundaries,
        "audited_effects": audited_effects,
        "state_visibility_score": visibility,
        "interpretation": "State visibility improves when mutable state and side-effect boundaries are explicit, documented, tested, and audited.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="State visibility calculator.")
    parser.add_argument("--mutable-state-sites", type=int, default=8)
    parser.add_argument("--explicit-state-records", type=int, default=6)
    parser.add_argument("--side-effect-boundaries", type=int, default=5)
    parser.add_argument("--audited-effects", type=int, default=4)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()
    result = compute(
        args.mutable_state_sites,
        args.explicit_state_records,
        args.side_effect_boundaries,
        args.audited_effects,
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "state_visibility_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
