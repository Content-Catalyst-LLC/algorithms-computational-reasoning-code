-- Health systems requiring special review.
SELECT system_id, impact_score, governance_readiness_score, health_algorithm_risk_score, recommendation
FROM health_algorithm_safety_audit
WHERE recommendation <> 'governed_use_with_monitoring'
ORDER BY health_algorithm_risk_score DESC;

-- Systems requiring clinical safety review.
SELECT system_id, impact_score, governance_readiness_score, health_algorithm_risk_score
FROM health_algorithm_safety_audit
WHERE recommendation = 'clinical_safety_review_required';

-- Systems requiring public-health governance review.
SELECT system_id, impact_score, governance_readiness_score, health_algorithm_risk_score
FROM health_algorithm_safety_audit
WHERE recommendation = 'public_health_governance_review_required';

-- Required health algorithm governance controls.
SELECT control, review_question
FROM health_governance_register
WHERE status = 'required';
