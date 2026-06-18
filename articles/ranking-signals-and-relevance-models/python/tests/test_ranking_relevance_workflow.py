from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from ranking_relevance.workflow import tokenize, precision_at_k, freshness_boost, ranking_signal_calculator, bm25_score

def test_tokenize():
    assert tokenize("Ranking, Signals!") == ["ranking","signals"]

def test_precision_at_k():
    assert precision_at_k({"d1","d2"}, ["d1","d3"], 2) == 0.5

def test_freshness_boost():
    assert freshness_boost(0) == 1.0

def test_ranking_signal_calculator():
    assert ranking_signal_calculator(1,1,1,1,1,1)["ranking_signal_score"] == 100.0

def test_bm25_score_nonnegative():
    assert bm25_score("ranking search", "ranking search systems", ["ranking search systems"]) >= 0
