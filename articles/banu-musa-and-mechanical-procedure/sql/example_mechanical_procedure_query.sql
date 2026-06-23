WITH theme(theme_id, mechanical_structure, procedural_sequence, conditional_control, hidden_state, feedback_potential, historical_significance, ethical_caution, modern_resonance) AS (
  VALUES ('valves_floats_thresholds', 0.96, 0.92, 0.98, 0.88, 0.92, 0.94, 0.82, 0.96)
)
SELECT
  theme_id,
  (mechanical_structure + procedural_sequence + conditional_control + hidden_state + feedback_potential + historical_significance + ethical_caution + modern_resonance) / 8.0 AS mechanical_score,
  CASE
    WHEN ((mechanical_structure + procedural_sequence + conditional_control + hidden_state + feedback_potential + historical_significance + ethical_caution + modern_resonance) / 8.0) >= 0.80
      AND conditional_control >= 0.86 THEN 'core_mechanical_procedure_thread'
    WHEN ((mechanical_structure + procedural_sequence + conditional_control + hidden_state + feedback_potential + historical_significance + ethical_caution + modern_resonance) / 8.0) >= 0.80 THEN 'major_mechanical_procedure_thread'
    ELSE 'supporting_mechanical_procedure_thread'
  END AS interpretive_status
FROM theme;
