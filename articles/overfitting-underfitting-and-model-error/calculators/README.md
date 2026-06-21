# Calculators

Self-contained calculators for model-error reasoning.

```bash
python3 calculators/python/generalization_gap_calculator.py --train-error 0.04 --test-error 0.09
python3 calculators/python/bias_variance_error_calculator.py --bias 0.20 --variance 0.04 --irreducible 0.02
python3 calculators/python/regularization_review_calculator.py --unregularized-test-error 0.13 --regularized-test-error 0.09
bash calculators/run_calculator_smoke_tests.sh
```
