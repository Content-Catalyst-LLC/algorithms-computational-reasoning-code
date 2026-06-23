WITH theme(theme_id, procedural_explicitness, transmission_importance, practical_application, representation_importance, modern_resonance) AS (
  VALUES ('al_khwarizmi_algorism', 0.92, 0.96, 0.88, 0.94, 0.96)
)
SELECT
  theme_id,
  (procedural_explicitness + transmission_importance + practical_application + representation_importance + modern_resonance) / 5.0 AS significance_score,
  CASE
    WHEN ((procedural_explicitness + transmission_importance + practical_application + representation_importance + modern_resonance) / 5.0) >= 0.78
      AND transmission_importance >= 0.80 THEN 'core_algorithmic_reasoning_thread'
    WHEN ((procedural_explicitness + transmission_importance + practical_application + representation_importance + modern_resonance) / 5.0) >= 0.78 THEN 'major_algorithmic_reasoning_thread'
    ELSE 'supporting_algorithmic_reasoning_thread'
  END AS interpretive_status
FROM theme;
