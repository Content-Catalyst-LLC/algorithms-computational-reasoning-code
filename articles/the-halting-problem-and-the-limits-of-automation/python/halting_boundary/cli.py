from pathlib import Path
from halting_boundary.workflow import run_workflow

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
    print("Halting boundary audit workflow complete.")
