from __future__ import annotations
from pathlib import Path
import csv

def score_in_range(score: float) -> bool:
    return 0.0 <= score <= 100.0

def nondecreasing(values: list[float]) -> bool:
    return all(values[i] <= values[i+1] for i in range(len(values)-1))

def round_trip(value: str) -> bool:
    return value.encode("utf-8").decode("utf-8") == value

def load_test_results(root: Path) -> list[dict[str, str]]:
    with (root/"data"/"synthetic_test_results.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def test_result_summary(rows: list[dict[str, str]]) -> dict[str, int]:
    return {"pass":sum(1 for r in rows if r["status"]=="pass"),"fail":sum(1 for r in rows if r["status"]=="fail"),"total":len(rows)}
