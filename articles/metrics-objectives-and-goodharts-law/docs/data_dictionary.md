# Data Dictionary

## metric_objective_cases.csv

- `case_id`: synthetic metric-governance case.
- `objective`: real goal or value.
- `metric`: proxy measurement.
- `proxy_alignment`: synthetic score from 0 to 1 representing proxy-goal fit.
- `optimization_pressure`: synthetic score from 0 to 1 representing target pressure.
- `gaming_risk`: synthetic score from 0 to 1 representing strategic adaptation risk.
- `guardrails`: number of guardrail metrics or review mechanisms.

## goodhart_risk_audit.csv

- `proxy_gap`: 1 minus proxy alignment.
- `high_pressure`: 1 if optimization pressure exceeds threshold.
- `weak_proxy`: 1 if proxy gap exceeds threshold.
- `high_gaming`: 1 if gaming risk exceeds threshold.
- `weak_guardrails`: 1 if too few guardrails exist.
- `goodhart_risk_score`: summary risk score.
- `status`: pass, review, or escalate.

## metric_governance_register.csv

- `item`: governance review item.
- `review_question`: question to ask before trusting the metric.
- `status`: requirement status.
