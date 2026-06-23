WITH theme(theme_id, classification, transformation, representation, demonstration, practical_use, transmission, modern_resonance) AS (
  VALUES ('restoration_al_jabr', 0.82, 0.94, 0.84, 0.78, 0.84, 0.90, 0.92)
)
SELECT
  theme_id,
  (classification + transformation + representation + demonstration + practical_use + transmission + modern_resonance) / 7.0 AS procedure_score,
  CASE
    WHEN ((classification + transformation + representation + demonstration + practical_use + transmission + modern_resonance) / 7.0) >= 0.80
      AND transformation >= 0.85 THEN 'core_rule_governed_algebra_thread'
    WHEN ((classification + transformation + representation + demonstration + practical_use + transmission + modern_resonance) / 7.0) >= 0.80 THEN 'major_rule_governed_algebra_thread'
    ELSE 'supporting_rule_governed_algebra_thread'
  END AS interpretive_status
FROM theme;
