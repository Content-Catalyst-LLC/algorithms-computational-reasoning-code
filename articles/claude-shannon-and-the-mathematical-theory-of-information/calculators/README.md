# Calculators

These small calculators support article concepts without external packages. They are educational conceptual scaffolds, not communication-system engineering tools.

## Python calculators

- `entropy_calculator.py` — compute entropy from probabilities.
- `information_content_calculator.py` — compute self-information for a probability.
- `mutual_information_2x2_calculator.py` — compute mutual information for a 2x2 joint distribution.
- `channel_capacity_awgn_calculator.py` — compute idealized Gaussian-channel capacity.
- `compression_bound_calculator.py` — estimate entropy-based lower bound for average bits.
- `redundancy_calculator.py` — compare maximum entropy and observed entropy.
- `error_correction_overhead_calculator.py` — estimate redundancy overhead.
- `semantic_boundary_caution_calculator.py` — flag meaning/truth overclaims.

## R calculators

- `entropy_calculator.R` — compute entropy in R.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
