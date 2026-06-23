# Calculators

These small calculators support article concepts without external packages.

## Python calculators

- `ranking_score_calculator.py` — combine relevance, engagement, freshness, and risk.
- `engagement_probability_calculator.py` — simple logistic engagement probability.
- `attention_risk_calculator.py` — average engagement pressure, creator impact, public-knowledge impact, weak user control, and weak contestability.
- `governance_readiness_calculator.py` — average transparency, contestability, moderation readiness, user control, governance, and monitoring.
- `platform_risk_calculator.py` — attention risk multiplied by weak governance readiness.
- `moderation_threshold_calculator.py` — classify content action from a harm score and thresholds.

## R calculators

- `attention_system_score.R` — compute attention risk, governance readiness, and platform risk.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
