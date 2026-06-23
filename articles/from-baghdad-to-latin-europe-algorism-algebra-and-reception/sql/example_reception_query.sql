WITH theme(theme_id, procedural_portability, notation_change, translation_pathway, teaching_value, practical_utility, institutional_adoption, trust_verification, historical_significance, ethical_caution, modern_resonance) AS (
  VALUES ('algorism_written_arithmetic', 0.98, 0.98, 0.92, 0.96, 0.96, 0.92, 0.90, 0.98, 0.84, 0.98)
)
SELECT
  theme_id,
  (procedural_portability + notation_change + translation_pathway + teaching_value + practical_utility + institutional_adoption + trust_verification + historical_significance + ethical_caution + modern_resonance) / 10.0 AS reception_score,
  CASE
    WHEN ((procedural_portability + notation_change + translation_pathway + teaching_value + practical_utility + institutional_adoption + trust_verification + historical_significance + ethical_caution + modern_resonance) / 10.0) >= 0.80
      AND procedural_portability >= 0.86 THEN 'core_algorism_algebra_reception_thread'
    WHEN ((procedural_portability + notation_change + translation_pathway + teaching_value + practical_utility + institutional_adoption + trust_verification + historical_significance + ethical_caution + modern_resonance) / 10.0) >= 0.80 THEN 'major_algorism_algebra_reception_thread'
    ELSE 'supporting_algorism_algebra_reception_thread'
  END AS interpretive_status
FROM theme;
