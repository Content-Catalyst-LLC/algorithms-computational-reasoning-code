from pathlib import Path
import json
from relational_query_logic.workflow import run_workflow, query_logic_calculator, join_risk_calculator

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "query_logic_core_sample": query_logic_calculator(.88,.86,.84,.82,.84,.80),
        "join_risk_sample": join_risk_calculator(.84,.80,.78,.82,.84)
    }
    (root/"outputs"/"json"/"relational_query_logic_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Relational query logic workflow complete.")
