-- Financial systems requiring special review.
SELECT system_id, impact_score, governance_readiness_score, financial_algorithm_risk_score, recommendation
FROM financial_algorithm_risk_audit
WHERE recommendation <> 'governed_use_with_monitoring'
ORDER BY financial_algorithm_risk_score DESC;

-- Systems requiring consumer protection review.
SELECT system_id, impact_score, governance_readiness_score, financial_algorithm_risk_score
FROM financial_algorithm_risk_audit
WHERE recommendation = 'consumer_protection_review_required';

-- Systems requiring market stability review.
SELECT system_id, impact_score, governance_readiness_score, financial_algorithm_risk_score
FROM financial_algorithm_risk_audit
WHERE recommendation = 'market_stability_review_required';

-- Required governance controls.
SELECT control, review_question
FROM financial_governance_register
WHERE status = 'required';
