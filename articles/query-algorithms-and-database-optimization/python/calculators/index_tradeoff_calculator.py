#!/usr/bin/env python3
import argparse,json
from pathlib import Path
def compute(read_benefit,write_cost,storage_cost,maintenance_cost):
    net=read_benefit-write_cost-storage_cost-maintenance_cost
    return {'read_benefit':read_benefit,'write_cost':write_cost,'storage_cost':storage_cost,'maintenance_cost':maintenance_cost,'net_index_value':round(net,3),'diagnostic':'positive index value' if net>0 else 'index cost may exceed read benefit'}
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--read-benefit',type=float,default=82); p.add_argument('--write-cost',type=float,default=14); p.add_argument('--storage-cost',type=float,default=9); p.add_argument('--maintenance-cost',type=float,default=6); p.add_argument('--output-dir',type=Path,default=Path('outputs/json')); a=p.parse_args(); r=compute(a.read_benefit,a.write_cost,a.storage_cost,a.maintenance_cost); a.output_dir.mkdir(parents=True,exist_ok=True); (a.output_dir/'index_tradeoff_calculator.json').write_text(json.dumps(r,indent=2),encoding='utf-8'); print(json.dumps(r,indent=2))
