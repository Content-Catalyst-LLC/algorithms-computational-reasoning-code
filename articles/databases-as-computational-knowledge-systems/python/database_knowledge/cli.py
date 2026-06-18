from pathlib import Path
import json
from database_knowledge.workflow import run_workflow, schema_quality, governance_risk

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "schema_quality_sample": schema_quality(0.90,0.85,0.80,0.88,0.82),
        "governance_risk_sample": governance_risk(0.80,0.84,0.78,0.76,0.82)
    }
    (root/"outputs"/"json"/"database_knowledge_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Database knowledge system workflow complete.")
