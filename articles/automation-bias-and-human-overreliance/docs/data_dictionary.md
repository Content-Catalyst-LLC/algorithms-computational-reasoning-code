# Data Dictionary

## automation_oversight_cases.csv

- `case_id`: synthetic oversight case.
- `context`: operating domain.
- `acceptance_rate`: rate at which humans accept automated recommendations.
- `model_quality`: context-specific model reliability score.
- `uncertainty`: synthetic uncertainty score.
- `review_time_minutes`: average review time.
- `override_friction`: difficulty of overriding or rejecting output.
- `appeal_pathway`: 1 if a contestability pathway exists, otherwise 0.

## automation_bias_overreliance_audit.csv

- `calibration_gap`: absolute difference between acceptance and model quality.
- `overreliance_gap`: positive difference between acceptance and model quality.
- `high_acceptance`: 1 if acceptance exceeds threshold.
- `low_quality`: 1 if model quality is below threshold.
- `low_review_time`: 1 if review time is too short.
- `high_override_friction`: 1 if overrides are difficult.
- `weak_contestability`: 1 if appeal pathway is missing.
- `automation_bias_risk_score`: summary oversight risk score.
- `status`: pass, review, or escalate.

## automation_oversight_governance_register.csv

- `item`: oversight governance item.
- `review_question`: question to answer before relying on human oversight claims.
- `status`: requirement status.
