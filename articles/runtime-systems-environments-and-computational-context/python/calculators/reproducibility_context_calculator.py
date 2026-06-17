#!/usr/bin/env python3
import argparse, json
from pathlib import Path
def compute(lockfile, runtime_manifest, data_snapshot, config_schema, output_hashes, run_logs):
    vals=[lockfile,runtime_manifest,data_snapshot,config_schema,output_hashes,run_logs]
    score=round(100*sum(1 for v in vals if v>0)/len(vals),2)
    return {"reproducibility_context_score":score,"interpretation":"Reproducibility improves when dependencies, runtime context, data, configuration, outputs, and logs are recorded."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    for f in ["lockfile","runtime-manifest","data-snapshot","config-schema","output-hashes","run-logs"]:
        p.add_argument("--"+f,type=int,default=1)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args(); result=compute(a.lockfile,a.runtime_manifest,a.data_snapshot,a.config_schema,a.output_hashes,a.run_logs)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"reproducibility_context_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
