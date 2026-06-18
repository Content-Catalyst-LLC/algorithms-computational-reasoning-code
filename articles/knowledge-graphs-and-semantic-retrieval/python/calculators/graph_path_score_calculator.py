#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(path_length: int, relationship_confidence: float, provenance_strength: float, review_status: float):
    length_factor=1/(1+max(path_length-1,0))
    score=100*(0.25*length_factor+0.30*relationship_confidence+0.30*provenance_strength+0.15*review_status)
    return {"path_length": path_length, "relationship_confidence": relationship_confidence, "provenance_strength": provenance_strength, "review_status": review_status, "graph_path_score": round(score,3), "diagnostic": "strong source-backed path" if score >= 84 else "review path length, confidence, provenance, and review status"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--path-length",type=int,default=3)
    p.add_argument("--relationship-confidence",type=float,default=0.90)
    p.add_argument("--provenance-strength",type=float,default=0.92)
    p.add_argument("--review-status",type=float,default=0.95)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.path_length,a.relationship_confidence,a.provenance_strength,a.review_status)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"graph_path_score_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
