from pathlib import Path
import csv
import subprocess
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]

required = [
    ARTICLE_ROOT / "article-metadata.yml",
    ARTICLE_ROOT / "README.md",
    ARTICLE_ROOT / "python" / "gradient_descent_ml" / "audit.py",
    ARTICLE_ROOT / "calculators" / "python" / "gradient_descent_calculator.py",
    ARTICLE_ROOT / "data" / "synthetic_training_cases.csv",
]

for path in required:
    assert path.exists(), f"Missing required file: {path}"

subprocess.run([sys.executable, str(ARTICLE_ROOT / "python" / "gradient_descent_ml" / "audit.py")], check=True)
subprocess.run([sys.executable, str(ARTICLE_ROOT / "calculators" / "python" / "gradient_descent_calculator.py")], check=True)

with (ARTICLE_ROOT / "outputs" / "tables" / "gradient_descent_training_trace.csv").open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))
    assert len(rows) >= 2
    assert float(rows[-1]["loss"]) < float(rows[0]["loss"])

print("Smoke tests passed for gradient descent and optimization in machine learning.")
