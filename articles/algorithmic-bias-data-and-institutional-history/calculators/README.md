# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `selection_gap_calculator.py` — compute max minus min selection-rate gap.
- `representation_gap_calculator.py` — compute absolute data/deployment representation gap.
- `label_gap_calculator.py` — compute label/verified-outcome gap.
- `historical_risk_calculator.py` — combine provenance risk, measurement weakness, proxy risk, and weak remediation.

## R calculators

- `bias_history_score.R` — compute representation, label, and historical-risk indicators.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
