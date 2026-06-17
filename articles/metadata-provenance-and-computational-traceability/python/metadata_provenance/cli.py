from pathlib import Path
import json
from metadata_provenance.workflow import run_workflow
from metadata_provenance.examples import provenance_demo

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    demo = provenance_demo(root)
    (root / "outputs" / "json" / "provenance_graph_demo.json").write_text(json.dumps(demo, indent=2), encoding="utf-8")
    print("Metadata and provenance audit workflow complete.")
    print("Provenance demo:", demo)
