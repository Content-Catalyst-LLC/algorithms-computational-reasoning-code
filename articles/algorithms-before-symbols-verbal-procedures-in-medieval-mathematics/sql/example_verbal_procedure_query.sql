WITH theme(theme_id, procedural_clarity, representation_dependence, pedagogical_value, transmission_importance, practical_use, modern_resonance) AS (
  VALUES ('rhetorical_algebra', 0.90, 0.86, 0.88, 0.90, 0.82, 0.88)
)
SELECT
  theme_id,
  (procedural_clarity + representation_dependence + pedagogical_value + transmission_importance + practical_use + modern_resonance) / 6.0 AS verbal_procedure_score,
  CASE
    WHEN ((procedural_clarity + representation_dependence + pedagogical_value + transmission_importance + practical_use + modern_resonance) / 6.0) >= 0.80
      AND procedural_clarity >= 0.86 THEN 'core_verbal_procedure_thread'
    WHEN ((procedural_clarity + representation_dependence + pedagogical_value + transmission_importance + practical_use + modern_resonance) / 6.0) >= 0.80 THEN 'major_verbal_procedure_thread'
    ELSE 'supporting_verbal_procedure_thread'
  END AS interpretive_status
FROM theme;
