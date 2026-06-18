#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def verify_sat(clauses, assignment):
    return all(any((lit > 0 and assignment.get(str(abs(lit)), False)) or (lit < 0 and not assignment.get(str(abs(lit)), False)) for lit in clause) for clause in clauses)

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    clauses=[[1,-2],[2,3],[-1,3]]
    assignment={"1":True,"2":False,"3":True}
    result={"problem":"synthetic_sat_certificate","clauses":clauses,"assignment":assignment,"certificate_valid":verify_sat(clauses,assignment)}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"certificate_verifier_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
