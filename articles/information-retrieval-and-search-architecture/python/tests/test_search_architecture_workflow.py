from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from search_architecture.workflow import tokenize, build_inverted_index, precision_recall, search_architecture_calculator

def test_tokenize():
    assert tokenize("Search, Architecture!") == ["search", "architecture"]

def test_inverted_index():
    index=build_inverted_index({"d1":"search retrieval", "d2":"database search"})
    assert index["search"] == ["d1","d2"]

def test_precision_recall():
    result=precision_recall({"d1","d2"}, ["d1","d3"])
    assert result["precision"] == 0.5
    assert result["recall"] == 0.5

def test_search_architecture_calculator():
    assert search_architecture_calculator(1,1,1,1,1,1)["search_architecture_core_score"] == 100.0
