#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(lexical: float, metadata: float, freshness: float, authority: float, semantic: float, provenance: float):
    score=100*(0.22*lexical+0.18*metadata+0.12*freshness+0.16*authority+0.17*semantic+0.15*provenance)
    return {"ranking_signal_score": round(score,3), "diagnostic": "strong ranking signal balance" if score >= 84 else "review lexical, metadata, freshness, authority, semantic, and provenance balance"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--lexical",type=float,default=0.84)
    p.add_argument("--metadata",type=float,default=0.88)
    p.add_argument("--freshness",type=float,default=0.76)
    p.add_argument("--authority",type=float,default=0.82)
    p.add_argument("--semantic",type=float,default=0.78)
    p.add_argument("--provenance",type=float,default=0.86)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.lexical,a.metadata,a.freshness,a.authority,a.semantic,a.provenance)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"ranking_signal_score_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
