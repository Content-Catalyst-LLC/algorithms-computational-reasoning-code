from pathlib import Path
from lambda_formal.workflow import run_workflow
from lambda_formal.reducer import demo_identity_reduction

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
    print("Lambda expression audit workflow complete.")
    print("Identity reduction trace:", " -> ".join(demo_identity_reduction()))
