WITH theme(theme_id, sequence_structure, timing_control, mechanical_embodiment, conditional_action, repeatability, documentation_quality, historical_significance, ethical_caution, modern_resonance) AS (
  VALUES ('clocks_as_timed_state_change', 0.98, 0.98, 0.94, 0.90, 0.94, 0.92, 0.96, 0.82, 0.96)
)
SELECT
  theme_id,
  (sequence_structure + timing_control + mechanical_embodiment + conditional_action + repeatability + documentation_quality + historical_significance + ethical_caution + modern_resonance) / 9.0 AS sequenced_action_score,
  CASE
    WHEN ((sequence_structure + timing_control + mechanical_embodiment + conditional_action + repeatability + documentation_quality + historical_significance + ethical_caution + modern_resonance) / 9.0) >= 0.80
      AND sequence_structure >= 0.86 THEN 'core_sequenced_mechanical_action_thread'
    WHEN ((sequence_structure + timing_control + mechanical_embodiment + conditional_action + repeatability + documentation_quality + historical_significance + ethical_caution + modern_resonance) / 9.0) >= 0.80 THEN 'major_sequenced_mechanical_action_thread'
    ELSE 'supporting_sequenced_mechanical_action_thread'
  END AS interpretive_status
FROM theme;
