from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from efficiency_understanding.workflow import efficiency_gain, understanding_composite

def test_efficiency_gain():
    result = efficiency_gain(100.0, 64.0)
    assert result["efficiency_gain_percent"] == 36.0

def test_understanding_composite():
    result = understanding_composite(1,1,1,1,1)
    assert result["understanding_score"] == 100.0
