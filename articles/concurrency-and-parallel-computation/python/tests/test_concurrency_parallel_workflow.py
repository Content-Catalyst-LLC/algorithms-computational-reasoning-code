from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from concurrency_parallel.workflow import speedup, amdahl_speedup, parallel_efficiency, topological_order

def test_speedup():
    assert speedup(120, 30) == 4.0

def test_amdahl_one_processor():
    assert amdahl_speedup(1, .12) == 1.0

def test_efficiency():
    assert parallel_efficiency(4, 2) == 0.5

def test_topological_order():
    tasks=[{"task_id":"a","depends_on":""},{"task_id":"b","depends_on":"a"}]
    assert topological_order(tasks) == ["a","b"]
