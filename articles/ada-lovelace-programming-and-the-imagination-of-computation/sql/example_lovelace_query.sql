WITH theme(theme_id, programming_structure, symbolic_generality, machine_orientation, mathematical_grounding, imaginative_reach, limit_awareness, collaboration, authorship, modern_resonance, ai_caution) AS (
  VALUES ('note_g_bernoulli_procedure', 0.98, 0.86, 0.98, 0.94, 0.86, 0.76, 0.92, 0.90, 0.98, 0.82)
)
SELECT
  theme_id,
  (programming_structure + symbolic_generality + machine_orientation + mathematical_grounding + imaginative_reach + limit_awareness + collaboration + authorship + modern_resonance + ai_caution) / 10.0 AS imagination_score,
  CASE
    WHEN ((programming_structure + symbolic_generality + machine_orientation + mathematical_grounding + imaginative_reach + limit_awareness + collaboration + authorship + modern_resonance + ai_caution) / 10.0) >= 0.80
      AND programming_structure >= 0.86 THEN 'core_lovelace_computation_thread'
    WHEN ((programming_structure + symbolic_generality + machine_orientation + mathematical_grounding + imaginative_reach + limit_awareness + collaboration + authorship + modern_resonance + ai_caution) / 10.0) >= 0.80 THEN 'major_lovelace_computation_thread'
    ELSE 'supporting_lovelace_computation_thread'
  END AS interpretive_status
FROM theme;
