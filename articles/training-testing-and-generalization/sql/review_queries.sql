SELECT split, n, accuracy, brier_score, log_loss
FROM split_performance_metrics
ORDER BY CASE split WHEN 'train' THEN 1 WHEN 'test' THEN 2 ELSE 3 END;

SELECT risk, value, status, review_question
FROM generalization_risk_register
WHERE status <> 'acceptable_for_teaching'
ORDER BY risk;

SELECT feature, absolute_standardized_shift, interpretation
FROM distribution_shift_diagnostics
ORDER BY absolute_standardized_shift DESC;
