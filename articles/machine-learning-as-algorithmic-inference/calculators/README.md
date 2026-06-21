# Calculators

These calculators are intentionally small and dependency-light. They are designed for article examples, teaching demonstrations, and future website-tool prototypes.

## Examples

```bash
python3 calculators/python/threshold_confusion_calculator.py --tp 80 --fp 25 --tn 140 --fn 35
python3 calculators/python/expected_prediction_value_calculator.py --score 0.72 --benefit 10 --harm 4
python3 calculators/python/train_test_gap_calculator.py --train-metric 0.84 --test-metric 0.76
python3 calculators/python/calibration_gap_calculator.py --average-score 0.62 --observed-rate 0.55
```
