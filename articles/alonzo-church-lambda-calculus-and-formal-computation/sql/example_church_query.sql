WITH theme(theme_id, formalization, functional_abstraction, symbolic_transformation, substitution, reduction, computability, undecidability, type_influence, programming_relevance, ai_caution) AS (
  VALUES ('lambda_calculus_core', 0.98, 0.98, 0.98, 0.96, 0.96, 0.96, 0.86, 0.88, 0.98, 0.86)
)
SELECT
  theme_id,
  (formalization + functional_abstraction + symbolic_transformation + substitution + reduction + computability + undecidability + type_influence + programming_relevance + ai_caution) / 10.0 AS formal_score,
  CASE
    WHEN ((formalization + functional_abstraction + symbolic_transformation + substitution + reduction + computability + undecidability + type_influence + programming_relevance + ai_caution) / 10.0) >= 0.80
      AND formalization >= 0.86 THEN 'core_church_formal_computation_thread'
    WHEN ((formalization + functional_abstraction + symbolic_transformation + substitution + reduction + computability + undecidability + type_influence + programming_relevance + ai_caution) / 10.0) >= 0.80 THEN 'major_church_formal_computation_thread'
    ELSE 'supporting_church_formal_computation_thread'
  END AS interpretive_status
FROM theme;
