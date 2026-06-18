#!/usr/bin/env python3
import argparse,json
from pathlib import Path
def compute(io_cost,cpu_cost,memory_cost): return {'io_cost':io_cost,'cpu_cost':cpu_cost,'memory_cost':memory_cost,'total_plan_cost':round(io_cost+cpu_cost+memory_cost,3)}
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--io-cost',type=float,default=420); p.add_argument('--cpu-cost',type=float,default=180); p.add_argument('--memory-cost',type=float,default=75); p.add_argument('--output-dir',type=Path,default=Path('outputs/json')); a=p.parse_args(); r=compute(a.io_cost,a.cpu_cost,a.memory_cost); a.output_dir.mkdir(parents=True,exist_ok=True); (a.output_dir/'query_cost_estimator.json').write_text(json.dumps(r,indent=2),encoding='utf-8'); print(json.dumps(r,indent=2))
