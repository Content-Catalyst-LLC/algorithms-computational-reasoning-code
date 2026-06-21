-- Estimators ordered by reported effect size.
SELECT estimate_type, estimated_effect, identification_warning
FROM causal_effect_estimates
ORDER BY estimated_effect DESC;

-- Assumptions still requiring review.
SELECT assumption, review_question, status
FROM causal_assumption_register
WHERE status <> 'complete';

-- Balance diagnostics requiring attention.
SELECT covariate, absolute_standardized_difference, review_flag
FROM covariate_balance_diagnostics
WHERE absolute_standardized_difference > 0.10
ORDER BY absolute_standardized_difference DESC;
