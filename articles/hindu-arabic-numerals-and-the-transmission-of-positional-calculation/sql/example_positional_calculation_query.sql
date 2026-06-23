WITH theme(theme_id, representation, procedure, transmission, practical_use, pedagogy, modern_resonance) AS (
  VALUES ('decimal_place_value', 0.98, 0.94, 0.88, 0.92, 0.92, 0.96)
)
SELECT
  theme_id,
  (representation + procedure + transmission + practical_use + pedagogy + modern_resonance) / 6.0 AS positional_score,
  CASE
    WHEN ((representation + procedure + transmission + practical_use + pedagogy + modern_resonance) / 6.0) >= 0.80
      AND representation >= 0.86 THEN 'core_positional_calculation_thread'
    WHEN ((representation + procedure + transmission + practical_use + pedagogy + modern_resonance) / 6.0) >= 0.80 THEN 'major_positional_calculation_thread'
    ELSE 'supporting_positional_calculation_thread'
  END AS interpretive_status
FROM theme;
