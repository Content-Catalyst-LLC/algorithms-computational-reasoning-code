# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `proxy_gap_calculator.py` — compute proxy gap from proxy-goal alignment.
- `goodhart_risk_calculator.py` — combine proxy gap, pressure, gaming risk, and guardrail weakness.
- `guardrail_sufficiency_calculator.py` — check whether guardrail count meets a threshold.

## R calculators

- `metric_pressure_score.R` — combine optimization pressure and gaming risk into a simple warning score.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
