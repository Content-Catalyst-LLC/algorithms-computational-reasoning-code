# Counterfactual Calculators

These calculators are small, dependency-light scripts that can be reused as article companions or later website tools.

## Python calculators

```bash
python3 calculators/python/threshold_flip_calculator.py --score 0.58 --threshold 0.62 --feature-weight 1.2
python3 calculators/python/recourse_distance_calculator.py --current 0.48 --target 0.70 --unit-cost 0.75
python3 calculators/python/counterfactual_contrast_calculator.py --original-score 0.57 --counterfactual-score 0.65 --threshold 0.62
python3 calculators/python/feasibility_score_calculator.py --delta 0.20 --unit-cost 0.75 --feasibility 0.80
```

Run all calculator smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
