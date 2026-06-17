from pathlib import Path
from boundary_reliability.workflow import run_workflow

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
    print("Termination, invariant, and edge-case audit workflow complete.")
