WITH theme(theme_id, procedure, representation, transmission, application, modern_resonance) AS (
  VALUES ('algorism_written_arithmetic', 0.94, 0.96, 0.92, 0.90, 0.94)
)
SELECT
  theme_id,
  (procedure + representation + transmission + application + modern_resonance) / 5.0 AS legacy_score,
  CASE
    WHEN ((procedure + representation + transmission + application + modern_resonance) / 5.0) >= 0.82
      AND transmission >= 0.80 THEN 'core_procedural_legacy'
    WHEN ((procedure + representation + transmission + application + modern_resonance) / 5.0) >= 0.82 THEN 'major_procedural_legacy'
    ELSE 'supporting_procedural_legacy'
  END AS interpretive_status
FROM theme;
