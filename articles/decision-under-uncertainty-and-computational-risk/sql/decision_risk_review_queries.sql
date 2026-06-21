-- Cases requiring uncertainty escalation or human review.
SELECT case_id, recommended_option, baseline_risk, confidence_score, decision
FROM threshold_review
WHERE decision IN ('escalate_uncertainty', 'human_review_required')
ORDER BY baseline_risk DESC;

-- Average expected value by option.
SELECT option_name,
       COUNT(*) AS n,
       AVG(expected_net_value) AS mean_expected_net_value,
       AVG(downside_exposure) AS mean_downside_exposure,
       AVG(regret) AS mean_regret
FROM decision_metrics
GROUP BY option_name
ORDER BY mean_expected_net_value DESC;

-- High severity risk register items.
SELECT case_id, recommended_option, downside_exposure, confidence_score, mitigation
FROM risk_register
WHERE severity = 'high'
ORDER BY downside_exposure DESC;
