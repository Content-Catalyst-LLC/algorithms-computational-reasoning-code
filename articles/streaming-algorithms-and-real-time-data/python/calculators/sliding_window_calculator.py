#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(items: list[str], window_size: int) -> list[dict[str, object]]:
    rows=[]
    for t in range(1, len(items)+1):
        window=items[max(0,t-window_size):t]
        counts={item: window.count(item) for item in sorted(set(window))}
        rows.append({"time":t,"event":items[t-1],"window_items":window,"counts":counts})
    return rows

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--items",type=str,default="A,B,A,C,A,D,B,E")
    p.add_argument("--window-size",type=int,default=3)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute([x.strip() for x in a.items.split(",") if x.strip()], a.window_size)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"sliding_window_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
