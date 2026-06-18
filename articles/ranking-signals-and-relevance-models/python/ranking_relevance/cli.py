from pathlib import Path
import json
from ranking_relevance.workflow import run_workflow, ranking_signal_calculator, precision_at_k, freshness_boost

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "ranking_signal_sample": ranking_signal_calculator(.84,.88,.76,.82,.78,.86),
        "precision_at_3_sample": {"precision_at_3": precision_at_k({"doc_1","doc_4"}, ["doc_4","doc_2","doc_1"], 3)},
        "freshness_30_days": {"freshness_boost": freshness_boost(30)}
    }
    (root/"outputs"/"json"/"ranking_relevance_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Ranking signals and relevance models workflow complete.")
