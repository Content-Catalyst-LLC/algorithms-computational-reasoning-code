WITH theme(theme_id, stored_program, memory_organization, control_structure, program_as_data, implementation_influence, bottleneck_awareness, collaboration_context, software_relevance, ai_infrastructure, governance_caution) AS (
  VALUES ('stored_program_concept', 0.98, 0.96, 0.94, 0.98, 0.96, 0.82, 0.86, 0.98, 0.90, 0.88)
)
SELECT
  theme_id,
  (stored_program + memory_organization + control_structure + program_as_data + implementation_influence + bottleneck_awareness + collaboration_context + software_relevance + ai_infrastructure + governance_caution) / 10.0 AS architecture_score,
  CASE
    WHEN ((stored_program + memory_organization + control_structure + program_as_data + implementation_influence + bottleneck_awareness + collaboration_context + software_relevance + ai_infrastructure + governance_caution) / 10.0) >= 0.80
      AND stored_program >= 0.86 THEN 'core_von_neumann_architecture_thread'
    WHEN ((stored_program + memory_organization + control_structure + program_as_data + implementation_influence + bottleneck_awareness + collaboration_context + software_relevance + ai_infrastructure + governance_caution) / 10.0) >= 0.80 THEN 'major_von_neumann_architecture_thread'
    ELSE 'supporting_von_neumann_architecture_thread'
  END AS interpretive_status
FROM theme;
