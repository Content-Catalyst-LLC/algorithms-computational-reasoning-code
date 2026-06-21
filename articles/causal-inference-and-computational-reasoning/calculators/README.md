# Calculators

These calculators are intentionally small, transparent, and self-contained. They are designed for article support and future website reuse.

## Calculators

- `python/causal_effect_calculator.py` — treated/control mean contrast.
- `python/difference_in_differences_calculator.py` — difference-in-differences contrast.
- `python/ipw_effect_calculator.py` — inverse probability weighting from CSV input.
- `python/sensitivity_bias_calculator.py` — simple unmeasured-bias adjustment.
- `r/causal_effect_calculator.R` — base-R treated/control contrast.

Run all calculator smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
