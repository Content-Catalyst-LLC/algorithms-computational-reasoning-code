# Data Dictionary

## feedback_loop_cases.csv

- `case_id`: synthetic feedback-loop case.
- `system`: system type.
- `feedback_path`: short description of output-to-input loop.
- `amplification`: synthetic score from 0 to 1.
- `exposure_concentration`: synthetic score for visibility concentration.
- `intervention_influence`: synthetic score for how much outputs drive intervention.
- `drift`: synthetic score for distribution change.
- `recursive_data`: synthetic score for model-mediated data entering future inputs.

## feedback_loop_audit.csv

- `high_amplification`: 1 if amplification exceeds threshold.
- `high_concentration`: 1 if exposure concentration exceeds threshold.
- `high_drift`: 1 if drift exceeds threshold.
- `high_recursive_data`: 1 if recursive data exceeds threshold.
- `feedback_risk_score`: mean of feedback risk components.
- `status`: pass, review, or escalate.

## feedback_governance_register.csv

- `item`: governance item.
- `review_question`: question to answer before trusting feedback-shaped data.
- `status`: requirement status.
