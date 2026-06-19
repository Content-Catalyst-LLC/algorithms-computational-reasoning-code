#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def ratio(numerator, denominator): return numerator / denominator if denominator else 0.0

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--explored-states",type=float,default=850); p.add_argument("--reachable-states",type=float,default=5000)
    p.add_argument("--pruned-states",type=float,default=1200); p.add_argument("--generated-states",type=float,default=4200)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json")); a=p.parse_args()
    result={"explored_states":a.explored_states,"reachable_states":a.reachable_states,"coverage_ratio":round(ratio(a.explored_states,a.reachable_states),6),"pruned_states":a.pruned_states,"generated_states":a.generated_states,"pruning_ratio":round(ratio(a.pruned_states,a.generated_states),6)}
    a.output_dir.mkdir(parents=True,exist_ok=True); (a.output_dir/"search_coverage_pruning_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8"); print(json.dumps(result,indent=2))
