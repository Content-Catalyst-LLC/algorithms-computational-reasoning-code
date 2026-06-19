from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from search_spaces.workflow import branching_state_count, path_cost, heuristic_score, coverage_ratio, pruning_ratio

def test_branching_state_count(): assert branching_state_count(3,5) == 364
def test_path_cost(): assert path_cost([2.5,3.0,1.25,4.75]) == 11.5
def test_heuristic_score(): assert heuristic_score(8.0,5.5) == 13.5
def test_coverage_ratio(): assert coverage_ratio(850,5000) == 0.17
def test_pruning_ratio(): assert pruning_ratio(1200,4200) == 0.285714
