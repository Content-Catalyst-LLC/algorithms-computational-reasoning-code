#!/usr/bin/env python3
import argparse, json
from pathlib import Path
def compute(problem_type, algorithm_value, bound_value):
    if bound_value == 0:
        return {"error":"bound_value must be nonzero"}
    if problem_type == "minimization":
        absolute_gap=algorithm_value-bound_value
        relative_gap=absolute_gap/bound_value
        ratio=algorithm_value/bound_value
    else:
        absolute_gap=bound_value-algorithm_value
        relative_gap=absolute_gap/bound_value
        ratio=algorithm_value/bound_value
    return {"problem_type":problem_type,"algorithm_value":algorithm_value,"bound_value":bound_value,"absolute_gap":round(absolute_gap,6),"relative_gap":round(relative_gap,6),"ratio":round(ratio,6),"interpretation":"Gap uses a known bound as reference; true optimum may differ unless bound is tight."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--problem-type",choices=["minimization","maximization"],default="minimization")
    p.add_argument("--algorithm-value",type=float,default=12.0)
    p.add_argument("--bound-value",type=float,default=10.0)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.problem_type,a.algorithm_value,a.bound_value)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"optimality_gap_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
