WITH layer(layer_id, procedural_explicitness, representation, proof_correctness, portability, mechanization, formalization, programmability, institutional_adoption, governance_relevance, modern_resonance) AS (
  VALUES ('islamic_world_algorism_and_algebra', 0.98, 0.94, 0.92, 0.98, 0.54, 0.84, 0.42, 0.94, 0.72, 0.98)
)
SELECT
  layer_id,
  (procedural_explicitness + representation + proof_correctness + portability + mechanization + formalization + programmability + institutional_adoption + governance_relevance + modern_resonance) / 10.0 AS history_score,
  CASE
    WHEN ((procedural_explicitness + representation + proof_correctness + portability + mechanization + formalization + programmability + institutional_adoption + governance_relevance + modern_resonance) / 10.0) >= 0.80
      AND procedural_explicitness >= 0.86 THEN 'core_algorithm_history_layer'
    WHEN ((procedural_explicitness + representation + proof_correctness + portability + mechanization + formalization + programmability + institutional_adoption + governance_relevance + modern_resonance) / 10.0) >= 0.80 THEN 'major_algorithm_history_layer'
    ELSE 'supporting_algorithm_history_layer'
  END AS interpretive_status
FROM layer;
