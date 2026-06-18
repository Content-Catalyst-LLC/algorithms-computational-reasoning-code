#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def latency(compute_ms: float, network_ms: float, queue_ms: float) -> float:
    return compute_ms + network_ms + queue_ms

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--compute-ms",type=float,default=35.0)
    p.add_argument("--network-ms",type=float,default=80.0)
    p.add_argument("--queue-ms",type=float,default=20.0)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result={"compute_ms":a.compute_ms,"network_ms":a.network_ms,"queue_ms":a.queue_ms,"response_ms":round(latency(a.compute_ms,a.network_ms,a.queue_ms),3)}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"distributed_latency_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
