from pathlib import Path
from abstraction_audit.workflow import run_workflow

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
    print("Abstraction audit workflow complete.")
