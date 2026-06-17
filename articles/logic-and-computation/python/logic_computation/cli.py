from pathlib import Path
from logic_computation.workflow import run_workflow

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
    print("Logic and computation audit workflow complete.")
