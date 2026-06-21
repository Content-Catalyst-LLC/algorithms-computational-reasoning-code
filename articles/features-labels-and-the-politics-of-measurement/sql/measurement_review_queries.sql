-- Review high-risk proxy features.
SELECT feature_name, construct_role, proxy_risk, review_question
FROM feature_register
WHERE proxy_risk IN ('high', 'medium')
ORDER BY proxy_risk DESC, feature_name;

-- Review groups with substantial label disagreement.
SELECT group_name, n, label_disagreement_rate, false_positive_rate, false_negative_rate
FROM measurement_metrics_by_group
WHERE label_disagreement_rate >= 0.20
ORDER BY label_disagreement_rate DESC;

-- Review governance items requiring action.
SELECT check_name, status, review_question
FROM measurement_governance_checklist
WHERE status IN ('needs_review', 'required')
ORDER BY status, check_name;
