# Monte Carlo calculators

Self-contained calculators for teaching Monte Carlo uncertainty concepts.

```bash
python3 calculators/python/model_calculator.py pi --samples=10000 --seed=42
python3 calculators/python/model_calculator.py threshold --samples=10000 --seed=42 --threshold=1250000
Rscript calculators/r/model_calculator.R pi --samples=10000 --seed=42
Rscript calculators/r/model_calculator.R threshold --samples=10000 --seed=42 --threshold=1250000
```
