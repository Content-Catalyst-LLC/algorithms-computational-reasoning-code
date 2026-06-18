from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from streaming_algorithms.workflow import sliding_window_counts, reservoir_sample, queue_pressure_table

def test_sliding_window_counts():
    rows = sliding_window_counts(["A","B","A"], 2)
    assert rows[-1]["event"] == "A"
    assert "A" in rows[-1]["counts"]

def test_reservoir_sample_size():
    assert len(reservoir_sample(["A","B","C","D"], 2)) == 2

def test_queue_pressure():
    rows = queue_pressure_table([90, 100], 100)
    assert rows[0]["stable_under_simple_model"] is True
    assert rows[1]["stable_under_simple_model"] is False
