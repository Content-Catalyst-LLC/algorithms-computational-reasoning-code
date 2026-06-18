#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def response_time(network_ms, queue_ms, compute_ms, storage_ms, coordination_ms):
    return network_ms + queue_ms + compute_ms + storage_ms + coordination_ms

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--network-ms",type=float,default=45.0)
    p.add_argument("--queue-ms",type=float,default=20.0)
    p.add_argument("--compute-ms",type=float,default=85.0)
    p.add_argument("--storage-ms",type=float,default=35.0)
    p.add_argument("--coordination-ms",type=float,default=15.0)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result={"network_ms":a.network_ms,"queue_ms":a.queue_ms,"compute_ms":a.compute_ms,"storage_ms":a.storage_ms,"coordination_ms":a.coordination_ms,"response_time_ms":round(response_time(a.network_ms,a.queue_ms,a.compute_ms,a.storage_ms,a.coordination_ms),3)}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"response_time_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
