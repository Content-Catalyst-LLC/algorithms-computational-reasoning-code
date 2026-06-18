.headers on
.mode column
SELECT case_name, online_decision,
ROUND(100.0*(0.11*information_at_decision_clarity+0.10*arrival_model_clarity+0.10*commitment_awareness+0.09*threshold_transparency+0.10*prediction_error_handling+0.10*competitive_or_regret_evidence+0.10*queue_and_capacity_awareness+0.09*fairness_under_arrival_review+0.08*fallback_readiness+0.07*governance_readiness+0.06*communication_clarity),2) AS online_decision_quality
FROM online_decision_cases ORDER BY online_decision_quality DESC;
