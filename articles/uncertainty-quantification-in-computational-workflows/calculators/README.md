# Calculator Layer

This layer provides self-contained calculators for uncertainty propagation and threshold exceedance.

## Python

```bash
python3 calculators/python/model_calculator.py --mode ensemble --runs 1000 --threshold 0.62
python3 calculators/python/model_calculator.py --mode single --demand 0.55 --capacity 0.50 --failure-rate 0.22 --adaptation-rate 0.30
```

## R

```bash
Rscript calculators/r/model_calculator.R ensemble 1000 0.62
Rscript calculators/r/model_calculator.R single
```
