-- Infrastructure systems requiring special review.
SELECT system_id, impact_score, governance_score, resilience_risk_score, recommendation
FROM infrastructure_algorithm_risk_audit
WHERE recommendation <> 'governed_use_with_monitoring'
ORDER BY resilience_risk_score DESC;

-- Systems requiring reliability and safety review.
SELECT system_id, impact_score, governance_score, resilience_risk_score
FROM infrastructure_algorithm_risk_audit
WHERE recommendation = 'reliability_and_safety_review_required';

-- Systems requiring climate-equity review.
SELECT system_id, impact_score, governance_score, resilience_risk_score
FROM infrastructure_algorithm_risk_audit
WHERE recommendation = 'climate_equity_review_required';

-- Required governance controls.
SELECT control, review_question
FROM infrastructure_governance_register
WHERE status = 'required';
