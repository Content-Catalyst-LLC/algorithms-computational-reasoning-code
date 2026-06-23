WITH theme(theme_id, procedure, representation, institutional_importance, verification, transmission, modern_resonance) AS (
  VALUES ('inheritance_allocation', 0.94, 0.88, 0.96, 0.92, 0.88, 0.90)
)
SELECT
  theme_id,
  (procedure + representation + institutional_importance + verification + transmission + modern_resonance) / 6.0 AS practical_score,
  CASE
    WHEN ((procedure + representation + institutional_importance + verification + transmission + modern_resonance) / 6.0) >= 0.80
      AND institutional_importance >= 0.86 THEN 'core_practical_calculation_thread'
    WHEN ((procedure + representation + institutional_importance + verification + transmission + modern_resonance) / 6.0) >= 0.80 THEN 'major_practical_calculation_thread'
    ELSE 'supporting_practical_calculation_thread'
  END AS interpretive_status
FROM theme;
