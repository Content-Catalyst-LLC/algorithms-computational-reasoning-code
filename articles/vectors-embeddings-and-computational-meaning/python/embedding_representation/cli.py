from pathlib import Path
import json
from embedding_representation.workflow import run_workflow
from embedding_representation.examples import demo_embedding_space

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    demo = demo_embedding_space(root)
    (root / "outputs" / "json" / "embedding_space_demo.json").write_text(json.dumps(demo, indent=2), encoding="utf-8")
    print("Embedding representation audit workflow complete.")
    print("Embedding demo:", demo)
