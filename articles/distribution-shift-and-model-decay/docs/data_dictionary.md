# Data Dictionary

## deployment_snapshots.csv

- `period`: monitoring period.
- `input_drift`: synthetic input-distribution shift score.
- `label_drift`: synthetic outcome/base-rate shift score.
- `accuracy`: observed performance estimate.
- `calibration_gap`: confidence-outcome mismatch.
- `subgroup_gap`: difference between best and worst subgroup performance.
- `override_rate`: rate of human override or rejection.

## drift_decay_audit.csv

- `performance_decay`: baseline accuracy minus current accuracy.
- `high_input_drift`: 1 if input drift exceeds threshold.
- `high_label_drift`: 1 if label drift exceeds threshold.
- `high_performance_decay`: 1 if performance loss exceeds threshold.
- `high_calibration_drift`: 1 if calibration gap exceeds threshold.
- `high_subgroup_gap`: 1 if subgroup gap exceeds threshold.
- `decay_risk_score`: summary monitoring score.
- `status`: pass, review, or escalate.

## drift_decay_governance_register.csv

- `item`: lifecycle governance item.
- `review_question`: question to answer before trusting continued deployment.
- `status`: requirement status.
