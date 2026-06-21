-- Models requiring evaluation review.
SELECT model, accuracy, calibration_gap, safety_flag_rate, status
FROM model_evaluation_summary
WHERE status IN ('review', 'escalate')
ORDER BY status DESC, safety_flag_rate DESC;

-- Saturated benchmark scores may need harder or more diagnostic tests.
SELECT model, accuracy, saturated
FROM model_evaluation_summary
WHERE saturated = 1;

-- Benchmark limits that must be documented before deployment claims.
SELECT limit_name, review_question, status
FROM benchmark_limit_register
WHERE status = 'required';

-- High-confidence wrong examples.
SELECT model, task, group_name, confidence
FROM benchmark_items
WHERE correct = 0 AND confidence >= 0.75
ORDER BY confidence DESC;
