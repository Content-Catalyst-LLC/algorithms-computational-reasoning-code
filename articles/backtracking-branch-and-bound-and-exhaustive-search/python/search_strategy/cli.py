from pathlib import Path
import json
from search_strategy.workflow import run_workflow
from search_strategy.examples import backtracking_permutations, exhaustive_subset_search, graph_coloring_backtracking, search_space_growth

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "exhaustive_subset_search": exhaustive_subset_search([3,4,5,9],10),
        "backtracking_permutations_count": len(backtracking_permutations(["A","B","C"])),
        "graph_coloring": graph_coloring_backtracking({"A":["B"],"B":["A","C"],"C":["B"]}, ["red","blue"]),
        "search_space_growth": search_space_growth(3,5)
    }
    (root/"outputs"/"json"/"search_strategy_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Search strategy workflow complete.")
