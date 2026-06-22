-- Objects requiring editorial, metadata, link, maintenance, or rebuild review.
SELECT object_id, architecture_readiness_score, maintenance_risk_score, governance_readiness_score, recommendation
FROM knowledge_architecture_audit
WHERE recommendation <> 'knowledge_architecture_ready'
ORDER BY maintenance_risk_score DESC;

-- Low architecture readiness.
SELECT object_id, architecture_readiness_score, recommendation
FROM knowledge_architecture_audit
WHERE architecture_readiness_score < 0.65
ORDER BY architecture_readiness_score ASC;

-- High maintenance risk.
SELECT object_id, maintenance_risk_score, recommendation
FROM knowledge_architecture_audit
WHERE maintenance_risk_score >= 0.70
ORDER BY maintenance_risk_score DESC;

-- Required governance controls.
SELECT control, review_question
FROM knowledge_architecture_register
WHERE status = 'required';
