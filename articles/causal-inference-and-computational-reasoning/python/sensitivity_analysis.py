from __future__ import annotations

from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
ESTIMATES = ROOT / "outputs" / "tables" / "causal_effect_estimates.csv"
OUT = ROOT / "outputs" / "tables" / "tipping_point_sensitivity.csv"
OUT_JSON = ROOT / "outputs" / "json" / "tipping_point_sensitivity.json"


def main() -> None:
    if not ESTIMATES.exists():
        raise SystemExit("Run python/causal_inference_audit_workflow.py first.")
    with ESTIMATES.open(newline="", encoding="utf-8") as handle:
        estimates = list(csv.DictReader(handle))

    rows = []
    for estimate in estimates:
        effect = float(estimate["estimated_effect"])
        rows.append({
            "estimate_type": estimate["estimate_type"],
            "estimated_effect": round(effect, 6),
            "unmeasured_bias_needed_to_nullify": round(effect, 6),
            "review_interpretation": "This teaching value is the amount of directional hidden bias that would reduce the estimate to zero.",
        })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(rows, indent=2, sort_keys=True), encoding="utf-8")
    print("Tipping-point sensitivity complete.")
    print(OUT)


if __name__ == "__main__":
    main()
