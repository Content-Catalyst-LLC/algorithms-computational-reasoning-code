# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `explanation_quality_calculator.py` — average faithfulness, stability, understandability, actionability, and uncertainty communication.
- `transparency_capacity_calculator.py` — average documentation completeness, governance readiness, and uncertainty communication.
- `accountability_capacity_calculator.py` — average explanation quality, transparency capacity, contestability, and governance readiness.
- `explanation_risk_calculator.py` — compute stakes multiplied by weak accountability capacity.

## R calculators

- `explanation_audit_score.R` — compute explanation quality, transparency capacity, accountability capacity, and explanation risk.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
