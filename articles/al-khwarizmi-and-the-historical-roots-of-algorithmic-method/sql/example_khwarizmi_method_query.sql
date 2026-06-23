WITH theme(theme_id, arithmetic_method, algebraic_procedure, representation, transformation, proof_relation, transmission, etymology, institutional_adoption, historiographic_caution, modern_resonance) AS (
  VALUES ('algorism_written_calculation', 0.98, 0.76, 0.98, 0.88, 0.78, 0.98, 0.98, 0.94, 0.92, 0.98)
)
SELECT
  theme_id,
  (arithmetic_method + algebraic_procedure + representation + transformation + proof_relation + transmission + etymology + institutional_adoption + historiographic_caution + modern_resonance) / 10.0 AS method_score,
  CASE
    WHEN ((arithmetic_method + algebraic_procedure + representation + transformation + proof_relation + transmission + etymology + institutional_adoption + historiographic_caution + modern_resonance) / 10.0) >= 0.80
      AND CASE WHEN arithmetic_method > algebraic_procedure THEN arithmetic_method ELSE algebraic_procedure END >= 0.86 THEN 'core_khwarizmi_algorithmic_method_thread'
    WHEN ((arithmetic_method + algebraic_procedure + representation + transformation + proof_relation + transmission + etymology + institutional_adoption + historiographic_caution + modern_resonance) / 10.0) >= 0.80 THEN 'major_khwarizmi_algorithmic_method_thread'
    ELSE 'supporting_khwarizmi_algorithmic_method_thread'
  END AS interpretive_status
FROM theme;
