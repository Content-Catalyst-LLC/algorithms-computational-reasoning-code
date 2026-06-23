# Calculators

These small calculators support article concepts without external packages. They use synthetic toy examples only.

## Python calculators

- `frequency_table_calculator.py` — count alphabetic symbols and produce relative frequencies.
- `relative_frequency_calculator.py` — compute count divided by total.
- `caesar_demo_calculator.py` — encrypt/decrypt a toy Caesar shift.
- `substitution_apply_calculator.py` — apply a toy substitution map.
- `hypothesis_score_calculator.py` — score overlap between observed and expected symbol rankings.
- `sample_size_warning_calculator.py` — flag whether a ciphertext is likely too short for stable frequency estimates.
- `cryptanalysis_score_calculator.py` — average linguistic evidence, counting procedure, inference, cryptanalytic relevance, history, ethics, and modern resonance.

## R calculators

- `cryptanalysis_score.R` — compute cryptanalysis score.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
