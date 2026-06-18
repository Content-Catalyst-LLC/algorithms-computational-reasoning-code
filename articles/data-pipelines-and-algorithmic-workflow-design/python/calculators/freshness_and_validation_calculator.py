#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path

def compute(days_since_update: int, passed_checks: int, total_checks: int, decay: float):
    freshness=math.exp(-decay*days_since_update)
    validation=passed_checks/total_checks if total_checks else 0.0
    combined=100*(0.45*freshness+0.55*validation)
    return {"days_since_update":days_since_update,"freshness_score":round(freshness,4),"validation_pass_rate":round(validation,4),"combined_freshness_validation_score":round(combined,3)}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--days-since-update",type=int,default=3)
    p.add_argument("--passed-checks",type=int,default=18)
    p.add_argument("--total-checks",type=int,default=20)
    p.add_argument("--decay",type=float,default=0.025)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.days_since_update,a.passed_checks,a.total_checks,a.decay)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"freshness_and_validation_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
