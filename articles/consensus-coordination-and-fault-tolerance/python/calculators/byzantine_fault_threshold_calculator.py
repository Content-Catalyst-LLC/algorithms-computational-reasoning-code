#!/usr/bin/env python3
import argparse, json
from pathlib import Path
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--faults",type=int,default=2)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result={"byzantine_faults":a.faults,"minimum_replicas_3f_plus_1":3*a.faults+1}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"byzantine_fault_threshold_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
