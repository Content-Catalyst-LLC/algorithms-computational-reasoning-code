-- Systems requiring documentation review or escalation.
SELECT system_id, documentation_completeness_score, artifact_coverage_score, documentation_quality_score, documentation_risk_score, status
FROM documentation_audit
WHERE status IN ('review', 'escalate')
ORDER BY documentation_risk_score DESC;

-- Systems with incomplete documentation.
SELECT system_id, documentation_completeness_score
FROM documentation_audit
WHERE documentation_completeness_score < 0.80
ORDER BY documentation_completeness_score ASC;

-- Systems with weak artifact coverage.
SELECT system_id, artifact_coverage_score
FROM documentation_audit
WHERE artifact_coverage_score < 0.80
ORDER BY artifact_coverage_score ASC;

-- Required documentation artifacts.
SELECT artifact, review_question
FROM documentation_register
WHERE status = 'required';
