#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def label(units: int, budget: int) -> str:
    if units <= 0.25 * budget:
        return "comfortable"
    if units <= budget:
        return "near budget"
    return "exceeds budget"

def compute(n: int, budget: int) -> dict[str, object]:
    linear=n
    quadratic=n*n
    return {
        "n": n,
        "budget_units": budget,
        "linear": {"units": linear, "feasibility": label(linear, budget)},
        "quadratic": {"units": quadratic, "feasibility": label(quadratic, budget)}
    }

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--n",type=int,default=10000)
    p.add_argument("--budget",type=int,default=1000000)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.n,a.budget)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"memory_budget_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
