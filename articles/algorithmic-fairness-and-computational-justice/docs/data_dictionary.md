# Data Dictionary

## fairness_group_records.csv

- `group`: synthetic group label.
- `n`: number of cases.
- `selected`: number receiving positive prediction or outcome.
- `true_positive`: correctly selected positive cases.
- `false_positive`: incorrectly selected negative cases.
- `false_negative`: incorrectly rejected positive cases.
- `true_negative`: correctly rejected negative cases.
- `mean_score`: average predicted score.
- `observed_rate`: observed outcome rate.
- `measurement_validity`: proxy or construct-validity score.
- `contestability`: ability to understand and challenge outcomes.
- `remediation`: ability to correct and repair harm.

## fairness_group_metrics.csv

- `selection_rate`: selected / n.
- `false_positive_rate`: false_positive / actual_negative.
- `false_negative_rate`: false_negative / actual_positive.
- `true_positive_rate`: true_positive / actual_positive.
- `calibration_gap`: absolute difference between mean_score and observed_rate.
- `fairness_evidence_score`: simplified evidence score based on error and calibration.
- `justice_capacity_score`: average of fairness evidence, measurement validity, contestability, and remediation.

## fairness_audit_summary.csv

- `selection_gap`: max minus min group selection rate.
- `false_positive_gap`: max minus min false-positive rate.
- `false_negative_gap`: max minus min false-negative rate.
- `max_calibration_gap`: maximum calibration gap.
- `mean_justice_capacity_score`: average justice capacity.
- `status`: pass, review, or escalate.
