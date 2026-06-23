SELECT domain_id, review_score, review_status
FROM algorithmic_philosophy_review_map
WHERE review_status = 'high_priority_philosophical_review'
ORDER BY review_score DESC;

SELECT domain_id, contestability_need, institutional_consequence, governance_urgency, review_score
FROM algorithmic_philosophy_review_map
WHERE contestability_need >= 0.90 AND governance_urgency >= 0.90
ORDER BY review_score DESC;

SELECT case_id, decision_severity, automation_level, opacity, delegation_risk
FROM delegation_risk_examples
ORDER BY delegation_risk DESC;

SELECT caution, meaning
FROM philosophical_cautions
ORDER BY caution;
