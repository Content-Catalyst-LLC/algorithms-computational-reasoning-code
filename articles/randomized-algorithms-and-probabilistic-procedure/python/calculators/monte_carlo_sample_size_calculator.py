#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
def compute(margin_of_error, confidence_z, proportion):
    n=(confidence_z**2 * proportion * (1-proportion)) / (margin_of_error**2)
    return {"margin_of_error":margin_of_error,"confidence_z":confidence_z,"assumed_proportion":proportion,"recommended_sample_size":math.ceil(n),"interpretation":"Simple binomial proportion sample-size estimate; adjust for population, design effect, stratification, and nonresponse when needed."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--margin-of-error",type=float,default=0.05)
    p.add_argument("--confidence-z",type=float,default=1.96)
    p.add_argument("--proportion",type=float,default=0.5)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args(); result=compute(a.margin_of_error,a.confidence_z,a.proportion)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"monte_carlo_sample_size_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
