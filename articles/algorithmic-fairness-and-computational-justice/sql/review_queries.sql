-- Group-level fairness and justice metrics.
SELECT group_id, selection_rate, false_positive_rate, false_negative_rate, true_positive_rate, calibration_gap, justice_capacity_score
FROM fairness_group_metrics
ORDER BY justice_capacity_score ASC;

-- Groups with weak justice capacity.
SELECT group_id, justice_capacity_score
FROM fairness_group_metrics
WHERE justice_capacity_score < 0.65;

-- Groups with high calibration gaps.
SELECT group_id, calibration_gap
FROM fairness_group_metrics
WHERE calibration_gap >= 0.08;

-- Required governance items.
SELECT item, review_question
FROM fairness_governance_register
WHERE status = 'required';
