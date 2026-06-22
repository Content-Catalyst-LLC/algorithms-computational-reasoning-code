-- Risks requiring review or escalation.
SELECT risk_id, system, inherent_risk_score, governance_readiness_score, residual_risk_score, status
FROM risk_governance_audit
WHERE status IN ('review', 'escalate')
ORDER BY residual_risk_score DESC;

-- Weak governance readiness.
SELECT risk_id, system, governance_readiness_score
FROM risk_governance_audit
WHERE governance_readiness_score < 0.70
ORDER BY governance_readiness_score ASC;

-- High residual risk.
SELECT risk_id, system, residual_risk_score
FROM risk_governance_audit
WHERE residual_risk_score >= 0.30
ORDER BY residual_risk_score DESC;

-- Required governance controls.
SELECT control, review_question
FROM risk_governance_controls
WHERE status = 'required';
