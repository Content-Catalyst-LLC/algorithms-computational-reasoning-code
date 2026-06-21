# Calculators

Self-contained calculators for the article **Features, Labels, and the Politics of Measurement**.

These scripts are deliberately small so they can be reused as teaching tools or adapted later for website interactivity.

## Examples

```bash
python3 calculators/python/confusion_metric_calculator.py --tp 72 --fp 18 --tn 88 --fn 22
python3 calculators/python/label_noise_impact_calculator.py --sample-size 1000 --noise-rate 0.18
python3 calculators/python/proxy_weight_audit_calculator.py --proxy-weight 0.42 --construct-weight 0.21 --missingness-rate 0.19
Rscript calculators/r/measurement_error_calculator.R 72 18 88 22
```
