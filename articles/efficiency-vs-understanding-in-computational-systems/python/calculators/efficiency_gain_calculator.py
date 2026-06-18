#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(baseline_cost: float, optimized_cost: float) -> dict[str, float]:
    gain=(baseline_cost-optimized_cost)/baseline_cost
    return {
        "baseline_cost": baseline_cost,
        "optimized_cost": optimized_cost,
        "absolute_savings": round(baseline_cost-optimized_cost, 6),
        "efficiency_gain": round(gain, 6),
        "efficiency_gain_percent": round(gain*100, 3)
    }

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--baseline-cost",type=float,default=100.0)
    p.add_argument("--optimized-cost",type=float,default=64.0)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.baseline_cost,a.optimized_cost)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"efficiency_gain_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
