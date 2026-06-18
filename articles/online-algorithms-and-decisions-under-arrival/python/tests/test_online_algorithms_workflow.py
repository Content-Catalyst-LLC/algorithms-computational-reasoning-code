from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from online_algorithms.workflow import ski_rental_table, queue_pressure_table, lru_cache_simulation

def test_ski_rental_table():
    rows = ski_rental_table(10.0, 50.0, 8)
    assert rows[-1]["days"] == 8
    assert rows[-1]["offline_optimum_cost"] == 50.0

def test_queue_pressure():
    rows = queue_pressure_table([95, 100], 100)
    assert rows[0]["stable_under_simple_model"] is True
    assert rows[1]["stable_under_simple_model"] is False

def test_lru_cache_simulation():
    out = lru_cache_simulation(["A","B","A"], 2)
    assert out["hits"] == 1
