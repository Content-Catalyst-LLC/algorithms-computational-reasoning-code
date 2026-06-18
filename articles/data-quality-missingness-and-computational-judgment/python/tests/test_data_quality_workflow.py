from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from data_quality.workflow import missingness_rate, completeness_score, freshness_score, data_quality_calculator

def test_missingness_rate():
    assert missingness_rate(45,1000) == 0.045

def test_completeness_score():
    assert completeness_score(45,1000) == 0.955

def test_freshness_score():
    assert freshness_score(0) == 1.0

def test_data_quality_calculator():
    assert data_quality_calculator(1,1,1,1,1)["data_quality_score"] == 100.0
