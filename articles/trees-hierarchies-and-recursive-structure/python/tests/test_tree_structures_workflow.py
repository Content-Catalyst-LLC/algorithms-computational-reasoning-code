from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from tree_structures.workflow import TreeStructureCase, tree_structure_quality, false_hierarchy_risk
from tree_structures.examples import demo_tree, Node, height, preorder, postorder
from calculators.tree_structure_quality_calculator import compute


def test_tree_scores_in_range():
    case = TreeStructureCase("Test", "Context", "Choice", 0.8, 0.8, 0.8, 0.75, 0.75, 0.75, 0.7, 0.75, 0.7, 0.7)
    assert 0 <= tree_structure_quality(case) <= 100
    assert 0 <= false_hierarchy_risk(case) <= 100


def test_tree_demo_shape():
    demo = demo_tree()
    assert demo["height"] == 2
    assert demo["preorder"][0] == "root"
    assert demo["postorder"][-1] == "root"
    assert demo["heap_priority_order"][0] == "urgent"


def test_recursive_height_single_leaf():
    assert height(Node("leaf", [])) == 0


def test_calculator_returns_interpretation():
    assert "interpretation" in compute([0.75] * 10)
