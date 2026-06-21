-- Cases requiring review or escalation.
SELECT case_id, task, stakes, status, overall_score, risk_flags, missing_sources
FROM llm_reasoning_audit
WHERE status IN ('review', 'escalate')
ORDER BY stakes DESC, overall_score ASC;

-- Average diagnostic scores by stakes level.
SELECT stakes,
       AVG(procedural_score) AS avg_procedural_score,
       AVG(source_score) AS avg_source_score,
       AVG(risk_score) AS avg_risk_score,
       AVG(overall_score) AS avg_overall_score
FROM llm_reasoning_audit
GROUP BY stakes;

-- Tool types that require approval before use.
SELECT tool_type, risk, control
FROM llm_tool_permission_matrix
WHERE allowed_without_approval = 0;
