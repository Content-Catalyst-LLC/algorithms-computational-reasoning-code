WITH theme(theme_id, table_structure, procedural_clarity, predictive_function, institutional_use, correction_awareness, transmission_importance, modern_resonance) AS (
  VALUES ('tables_as_stored_computation', 0.98, 0.90, 0.92, 0.86, 0.86, 0.90, 0.94)
)
SELECT
  theme_id,
  (table_structure + procedural_clarity + predictive_function + institutional_use + correction_awareness + transmission_importance + modern_resonance) / 7.0 AS prediction_score,
  CASE
    WHEN ((table_structure + procedural_clarity + predictive_function + institutional_use + correction_awareness + transmission_importance + modern_resonance) / 7.0) >= 0.80
      AND predictive_function >= 0.86 THEN 'core_astronomical_prediction_thread'
    WHEN ((table_structure + procedural_clarity + predictive_function + institutional_use + correction_awareness + transmission_importance + modern_resonance) / 7.0) >= 0.80 THEN 'major_astronomical_prediction_thread'
    ELSE 'supporting_astronomical_prediction_thread'
  END AS interpretive_status
FROM theme;
