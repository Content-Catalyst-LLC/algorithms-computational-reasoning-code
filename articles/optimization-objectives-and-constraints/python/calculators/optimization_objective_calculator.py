#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def parse_floats(value):
    return [float(x.strip()) for x in value.split(",") if x.strip()]

def linear_objective(coefficients, decision_values):
    if len(coefficients) != len(decision_values):
        raise ValueError("coefficients and decision values must have the same length")
    return sum(c*x for c,x in zip(coefficients, decision_values))

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--coefficients",default="4.0,2.0,1.5")
    p.add_argument("--decision-values",default="10.0,20.0,5.0")
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    coefficients=parse_floats(a.coefficients)
    decision_values=parse_floats(a.decision_values)
    result={"coefficients":coefficients,"decision_values":decision_values,"linear_objective":round(linear_objective(coefficients,decision_values),6)}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"optimization_objective_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
