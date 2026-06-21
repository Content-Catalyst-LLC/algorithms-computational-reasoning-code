# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `classification_metrics_calculator.py` — compute accuracy, precision, recall, and F1 from confusion-matrix counts.
- `calibration_gap_calculator.py` — compute absolute gap between average confidence and observed accuracy.
- `benchmark_saturation_calculator.py` — flag whether a benchmark score is near ceiling.

## R calculators

- `evaluation_risk_score.R` — combine calibration gap and safety flag rate into a simple review score.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
