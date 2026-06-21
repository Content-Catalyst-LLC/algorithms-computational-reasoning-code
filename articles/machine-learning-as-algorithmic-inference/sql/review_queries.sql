-- Review threshold trade-offs.
SELECT threshold, accuracy, false_positive_rate, false_negative_rate
FROM ml_threshold_sweep
ORDER BY threshold;

-- Identify governance items requiring review.
SELECT review_area, signal, evidence
FROM ml_inference_governance_register
WHERE status = 'review_required'
ORDER BY review_area;

-- Inspect feature and label concerns.
SELECT item, risk, review_question
FROM ml_feature_label_audit
ORDER BY item;
