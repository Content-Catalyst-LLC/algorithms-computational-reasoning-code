# Calculators

These small calculators support article concepts without external packages. They are educational conceptual scaffolds, not formal-verification tools.

## Python calculators

- `discipline_score_calculator.py` — average Dijkstra structured-programming dimensions.
- `invariant_check_helper.py` — check a simple loop-invariant-style condition over a trace.
- `weakest_precondition_assignment.py` — compute a simple assignment precondition by substitution.
- `dijkstra_shortest_path_calculator.py` — run Dijkstra shortest path on a small graph.
- `control_flow_complexity_calculator.py` — estimate simplified control-flow complexity.
- `loop_termination_helper.py` — assess a simple decreasing variant.
- `proof_obligation_helper.py` — list proof obligations for a loop.
- `ai_generated_code_caution_calculator.py` — flag generated-code overclaims.

## R calculators

- `discipline_score.R` — compute structured-programming discipline score.

Run smoke tests:

```bash
bash calculators/run_calculator_smoke_tests.sh
```
