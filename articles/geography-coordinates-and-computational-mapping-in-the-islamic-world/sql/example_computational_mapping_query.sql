WITH theme(theme_id, spatial_representation, coordinate_structure, procedural_clarity, institutional_use, correction_awareness, transmission_importance, modern_resonance) AS (
  VALUES ('coordinates_as_spatial_data', 0.98, 0.98, 0.88, 0.86, 0.90, 0.90, 0.96)
)
SELECT
  theme_id,
  (spatial_representation + coordinate_structure + procedural_clarity + institutional_use + correction_awareness + transmission_importance + modern_resonance) / 7.0 AS mapping_score,
  CASE
    WHEN ((spatial_representation + coordinate_structure + procedural_clarity + institutional_use + correction_awareness + transmission_importance + modern_resonance) / 7.0) >= 0.80
      AND spatial_representation >= 0.86 THEN 'core_computational_mapping_thread'
    WHEN ((spatial_representation + coordinate_structure + procedural_clarity + institutional_use + correction_awareness + transmission_importance + modern_resonance) / 7.0) >= 0.80 THEN 'major_computational_mapping_thread'
    ELSE 'supporting_computational_mapping_thread'
  END AS interpretive_status
FROM theme;
