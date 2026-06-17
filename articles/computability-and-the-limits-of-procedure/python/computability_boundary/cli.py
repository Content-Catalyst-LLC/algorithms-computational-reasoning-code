from pathlib import Path
from computability_boundary.workflow import run_workflow

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
    print("Computability boundary audit workflow complete.")
