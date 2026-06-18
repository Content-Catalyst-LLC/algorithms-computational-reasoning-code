#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(missing_count: int, total_count: int):
    rate=missing_count/total_count if total_count else 0.0
    return {"missing_count": missing_count, "total_count": total_count, "missingness_rate": round(rate,4), "completeness_score": round(1-rate,4)}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--missing-count",type=int,default=45)
    p.add_argument("--total-count",type=int,default=1000)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.missing_count,a.total_count)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"missingness_rate_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
