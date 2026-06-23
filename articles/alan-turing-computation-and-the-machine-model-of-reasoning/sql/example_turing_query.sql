WITH theme(theme_id, formalization, machine_abstraction, symbolic_representation, universality, decidability, limit_awareness, reasoning_relevance, ai_relevance, governance_caution, modern_resonance) AS (
  VALUES ('turing_machine_model', 0.98, 0.98, 0.96, 0.86, 0.90, 0.92, 0.96, 0.82, 0.86, 0.98)
)
SELECT
  theme_id,
  (formalization + machine_abstraction + symbolic_representation + universality + decidability + limit_awareness + reasoning_relevance + ai_relevance + governance_caution + modern_resonance) / 10.0 AS reasoning_score,
  CASE
    WHEN ((formalization + machine_abstraction + symbolic_representation + universality + decidability + limit_awareness + reasoning_relevance + ai_relevance + governance_caution + modern_resonance) / 10.0) >= 0.80
      AND formalization >= 0.86 THEN 'core_turing_machine_reasoning_thread'
    WHEN ((formalization + machine_abstraction + symbolic_representation + universality + decidability + limit_awareness + reasoning_relevance + ai_relevance + governance_caution + modern_resonance) / 10.0) >= 0.80 THEN 'major_turing_machine_reasoning_thread'
    ELSE 'supporting_turing_machine_reasoning_thread'
  END AS interpretive_status
FROM theme;
