-- Models with large generalization gaps.
SELECT model_name, degree, train_mse, test_mse, generalization_gap_mse, pattern_classification
FROM model_complexity_metrics
ORDER BY generalization_gap_mse DESC;

-- Models with shifted-test fragility.
SELECT model_name, test_mse, shifted_test_mse, shift_penalty_mse
FROM model_complexity_metrics
ORDER BY shift_penalty_mse DESC;

-- Governance items needing review.
SELECT review_item, status, review_question
FROM model_error_governance_review
WHERE status LIKE '%review%' OR status LIKE '%documentation%';
