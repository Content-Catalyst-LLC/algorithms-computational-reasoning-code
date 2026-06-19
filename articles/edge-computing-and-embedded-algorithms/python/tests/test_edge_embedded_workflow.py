from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from edge_embedded.workflow import edge_response_time, cloud_dependent_response_time, meets_deadline, battery_life_hours, local_threshold_action

def test_edge_response_time():
    assert edge_response_time(8,6,14,5) == 33

def test_cloud_dependent_response_time():
    assert cloud_dependent_response_time(8,90,60,90,5) == 253

def test_meets_deadline():
    assert meets_deadline(33,50) is True
    assert meets_deadline(253,50) is False

def test_battery_life():
    assert battery_life_hours(12,0.08) == 150

def test_local_threshold_action():
    assert local_threshold_action(0.82,0.75) == "alert"
