#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def quorum_size(node_count: int) -> int:
    return (node_count // 2) + 1

def crash_fault_tolerance(node_count: int) -> int:
    return (node_count - 1) // 2

def availability_with_replication(replica_count: int, node_availability: float) -> float:
    return 1 - ((1 - node_availability) ** replica_count)

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--node-count",type=int,default=5)
    p.add_argument("--node-availability",type=float,default=0.99)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result={"node_count":a.node_count,"majority_quorum":quorum_size(a.node_count),"crash_fault_tolerance":crash_fault_tolerance(a.node_count),"node_availability":a.node_availability,"replicated_availability":round(availability_with_replication(a.node_count,a.node_availability),6)}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"quorum_fault_tolerance_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
