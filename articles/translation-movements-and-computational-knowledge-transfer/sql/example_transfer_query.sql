WITH theme(theme_id, procedural_fidelity, vocabulary_mapping, diagram_table_preservation, institutional_support, error_control, adaptation, historical_significance, ethical_caution, modern_resonance) AS (
  VALUES ('procedural_fidelity', 0.98, 0.90, 0.94, 0.88, 0.94, 0.90, 0.96, 0.84, 0.96)
)
SELECT
  theme_id,
  (procedural_fidelity + vocabulary_mapping + diagram_table_preservation + institutional_support + error_control + adaptation + historical_significance + ethical_caution + modern_resonance) / 9.0 AS transfer_score,
  CASE
    WHEN ((procedural_fidelity + vocabulary_mapping + diagram_table_preservation + institutional_support + error_control + adaptation + historical_significance + ethical_caution + modern_resonance) / 9.0) >= 0.80
      AND procedural_fidelity >= 0.86 THEN 'core_computational_knowledge_transfer_thread'
    WHEN ((procedural_fidelity + vocabulary_mapping + diagram_table_preservation + institutional_support + error_control + adaptation + historical_significance + ethical_caution + modern_resonance) / 9.0) >= 0.80 THEN 'major_computational_knowledge_transfer_thread'
    ELSE 'supporting_computational_knowledge_transfer_thread'
  END AS interpretive_status
FROM theme;
