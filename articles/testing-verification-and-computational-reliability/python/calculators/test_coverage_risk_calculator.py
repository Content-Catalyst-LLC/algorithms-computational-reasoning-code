#!/usr/bin/env python3
import argparse, json
from pathlib import Path
def compute(total_paths, tested_paths, weak_oracles, missing_edge_cases, unreproducible_tests, unmonitored_runtime_paths):
    coverage_gap=max(0,total_paths-tested_paths)/max(1,total_paths)
    risk=min(100, round(100*(0.35*coverage_gap + 0.20*weak_oracles/max(1,total_paths) + 0.20*missing_edge_cases/max(1,total_paths) + 0.15*unreproducible_tests/max(1,total_paths) + 0.10*unmonitored_runtime_paths/max(1,total_paths)),2))
    return {"coverage_gap":round(coverage_gap,4),"test_coverage_risk_score":risk,"interpretation":"Coverage risk rises when paths are untested, oracles are weak, edge cases are missing, tests are unreproducible, or runtime behavior is unmonitored."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--total-paths",type=int,default=40)
    p.add_argument("--tested-paths",type=int,default=30)
    p.add_argument("--weak-oracles",type=int,default=4)
    p.add_argument("--missing-edge-cases",type=int,default=5)
    p.add_argument("--unreproducible-tests",type=int,default=3)
    p.add_argument("--unmonitored-runtime-paths",type=int,default=5)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args(); result=compute(a.total_paths,a.tested_paths,a.weak_oracles,a.missing_edge_cases,a.unreproducible_tests,a.unmonitored_runtime_paths)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"test_coverage_risk_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
