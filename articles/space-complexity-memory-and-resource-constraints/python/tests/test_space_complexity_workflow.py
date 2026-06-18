from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from space_complexity.workflow import graph_storage, memory_budget_table

def test_graph_storage():
    row = graph_storage(1000, 5000)
    assert row["adjacency_matrix_units"] == 1000000
    assert row["adjacency_list_units"] == 6000

def test_memory_budget_table():
    rows = memory_budget_table()
    assert rows[0]["fits_budget_1k_linear"] is True
