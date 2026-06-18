from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from parallelism_scale.workflow import speedup, capacity_table

def test_speedup():
    assert round(speedup(0.10, 16), 4) == 6.4

def test_capacity():
    rows = capacity_table(100.0, [1, 2])
    assert rows[0]["effective_capacity"] == 100.0
