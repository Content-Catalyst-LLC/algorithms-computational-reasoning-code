#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
def compute(dimensions, bytes_per_state, backpointer_bytes):
    state_count=math.prod(dimensions)
    value_memory=state_count*bytes_per_state
    backpointer_memory=state_count*backpointer_bytes
    total=value_memory+backpointer_memory
    return {"dimensions":dimensions,"state_count":state_count,"value_memory_bytes":value_memory,"backpointer_memory_bytes":backpointer_memory,"total_memory_bytes":total,"total_memory_megabytes":round(total/(1024*1024),3),"interpretation":"Memory estimate assumes dense tabulation; sparse or rolling storage may reduce memory but can reduce traceability."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--dimensions",type=str,default="100,50,20")
    p.add_argument("--bytes-per-state",type=int,default=8)
    p.add_argument("--backpointer-bytes",type=int,default=4)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    dims=[int(x.strip()) for x in a.dimensions.split(",") if x.strip()]
    result=compute(dims,a.bytes_per_state,a.backpointer_bytes)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"state_space_memory_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
