# Calculators

These small calculators support article concepts without external packages. They are educational conceptual scaffolds, not hardware performance tools.

## Python calculators

- `architecture_score_calculator.py` — average von Neumann architecture dimensions.
- `fetch_execute_cycle.py` — simulate a tiny fetch-execute trace.
- `memory_bandwidth_calculator.py` — estimate data movement time from bytes and bandwidth.
- `bottleneck_calculator.py` — compare compute rate and memory bandwidth constraints.
- `program_as_data_classifier.py` — classify program-as-data benefits and risks.
- `branch_trace_calculator.py` — trace simple branch/loop behavior.
- `locality_score_calculator.py` — estimate locality from repeated address access.
- `architecture_governance_caution_calculator.py` — flag architecture-governance risks.

## R calculators

- `architecture_score.R` — compute architecture score.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
