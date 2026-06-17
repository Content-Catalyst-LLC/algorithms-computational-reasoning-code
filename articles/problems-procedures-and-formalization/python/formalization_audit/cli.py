from pathlib import Path
from formalization_audit.workflow import run_workflow

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
    print("Formalization audit workflow complete.")
