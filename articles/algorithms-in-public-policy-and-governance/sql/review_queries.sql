-- Public algorithmic systems that are not ready for deployment.
SELECT use_case_id, procedural_readiness_score, governance_readiness_score, public_algorithmic_risk_score, recommendation
FROM public_governance_audit
WHERE recommendation = 'do_not_deploy_without_due_process_redesign'
ORDER BY public_algorithmic_risk_score DESC;

-- Systems requiring governance review or independent oversight.
SELECT use_case_id, procedural_readiness_score, governance_readiness_score, public_algorithmic_risk_score, recommendation
FROM public_governance_audit
WHERE recommendation IN ('governance_review_required', 'deploy_only_with_independent_oversight')
ORDER BY public_algorithmic_risk_score DESC;

-- Required public algorithmic governance controls.
SELECT control, review_question
FROM public_governance_register
WHERE status = 'required';
