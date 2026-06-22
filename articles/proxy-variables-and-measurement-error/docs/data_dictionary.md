# Data Dictionary

## proxy_variable_cases.csv

- `case_id`: synthetic proxy-variable case.
- `construct`: underlying target construct.
- `proxy`: observed stand-in variable.
- `proxy_validity`: synthetic score from 0 to 1 representing construct validity.
- `missingness_rate`: fraction of records missing or structurally unrecorded.
- `differential_error`: synthetic group/context error-gap score.
- `label_error`: synthetic label error score.

## proxy_measurement_error_audit.csv

- `validity_gap`: 1 minus proxy validity.
- `weak_validity`: 1 if validity gap exceeds threshold.
- `high_missingness`: 1 if missingness exceeds threshold.
- `high_differential_error`: 1 if differential error exceeds threshold.
- `high_label_error`: 1 if label error exceeds threshold.
- `measurement_risk_score`: summary score combining validity gap, missingness, differential error, and label error.
- `status`: pass, review, or escalate.

## measurement_governance_register.csv

- `item`: governance item.
- `review_question`: question to answer before trusting the proxy.
- `status`: requirement status.
