#!/usr/bin/env python3
import argparse, json
from pathlib import Path
def compute(local_optimum_risk, seed_variance, parameter_sensitivity, edge_case_failure_rate):
    risk=100*(0.30*local_optimum_risk+0.25*seed_variance+0.25*parameter_sensitivity+0.20*edge_case_failure_rate)
    quality=100-risk
    return {"local_search_risk":round(risk,3),"local_search_quality_proxy":round(quality,3),"interpretation":"Risk proxy for local-optimum traps, seed fragility, parameter sensitivity, and edge-case failure."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--local-optimum-risk",type=float,default=0.35)
    p.add_argument("--seed-variance",type=float,default=0.25)
    p.add_argument("--parameter-sensitivity",type=float,default=0.30)
    p.add_argument("--edge-case-failure-rate",type=float,default=0.20)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.local_optimum_risk,a.seed_variance,a.parameter_sensitivity,a.edge_case_failure_rate)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"local_search_risk_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
