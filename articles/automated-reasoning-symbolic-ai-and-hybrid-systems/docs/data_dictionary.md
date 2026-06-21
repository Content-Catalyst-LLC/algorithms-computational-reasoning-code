# Data Dictionary

## symbolic_initial_facts.csv

- `fact`: an initial proposition accepted by the toy knowledge base.

## symbolic_rules.csv

- `rule_id`: stable rule identifier.
- `premises`: semicolon-separated premises required by the rule.
- `conclusion`: derived proposition.
- `provenance`: policy, architecture, or review source for the rule.

## symbolic_inference_trace.csv

- `rule_id`: rule applied.
- `premises`: premises that were present.
- `conclusion`: inferred proposition.
- `provenance`: rule provenance.
- `trace_note`: explanation of the inference.

## symbolic_contradiction_checks.csv

- `left_claim`, `right_claim`: claims treated as incompatible.
- `conflict_detected`: 1 if both claims are present.
- `interpretation`: review guidance.

## symbolic_constraint_review.csv

- `constraint`: required governance condition.
- `satisfied`: 1 if present in the known facts.
- `interpretation`: review guidance.
