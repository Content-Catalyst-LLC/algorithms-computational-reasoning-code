# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `hiring_score_calculator.py` — weighted hiring score from job relevance, evidence, experience, and support needs.
- `scheduling_coverage_calculator.py` — coverage margin from scheduled labor and demand.
- `productivity_metric_calculator.py` — weighted quantity, quality, and reliability score with context penalty.
- `workload_burden_calculator.py` — simple burden score from pace, hours, fatigue, and schedule volatility.
- `governance_readiness_calculator.py` — average fairness, privacy, contestability, safety, human review, monitoring, and governance.
- `workplace_algorithm_risk_calculator.py` — average impact, weak fairness, weak privacy, weak contestability, and weak governance.

## R calculators

- `workplace_algorithm_score.R` — compute workplace algorithm indicators.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
