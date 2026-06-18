from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from tractability_hardness.workflow import subset_count, permutation_count, feasibility_table

def test_search_space_examples():
    assert subset_count(10) == 1024
    assert permutation_count(5) == 120
    assert feasibility_table()[0]["linear_feasibility"] == "comfortable"
