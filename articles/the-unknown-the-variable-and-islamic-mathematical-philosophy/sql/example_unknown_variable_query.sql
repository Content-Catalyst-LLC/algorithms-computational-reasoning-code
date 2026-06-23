WITH theme(theme_id, unknown_representation, procedural_transformation, abstraction, proof_relation, translation_continuity, practical_grounding, philosophical_depth, historical_significance, ethical_caution, modern_resonance) AS (
  VALUES ('unknown_as_named_object', 0.98, 0.94, 0.96, 0.88, 0.90, 0.92, 0.96, 0.98, 0.86, 0.98)
)
SELECT
  theme_id,
  (unknown_representation + procedural_transformation + abstraction + proof_relation + translation_continuity + practical_grounding + philosophical_depth + historical_significance + ethical_caution + modern_resonance) / 10.0 AS unknown_variable_score,
  CASE
    WHEN ((unknown_representation + procedural_transformation + abstraction + proof_relation + translation_continuity + practical_grounding + philosophical_depth + historical_significance + ethical_caution + modern_resonance) / 10.0) >= 0.80
      AND unknown_representation >= 0.86 THEN 'core_unknown_variable_philosophy_thread'
    WHEN ((unknown_representation + procedural_transformation + abstraction + proof_relation + translation_continuity + practical_grounding + philosophical_depth + historical_significance + ethical_caution + modern_resonance) / 10.0) >= 0.80 THEN 'major_unknown_variable_philosophy_thread'
    ELSE 'supporting_unknown_variable_philosophy_thread'
  END AS interpretive_status
FROM theme;
