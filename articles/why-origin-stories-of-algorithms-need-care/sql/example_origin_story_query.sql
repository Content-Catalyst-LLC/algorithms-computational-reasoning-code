WITH theme(theme_id, evidence_grounding, scope_clarity, anachronism_control, network_awareness, etymology_caution, transmission_depth, credit_distribution, public_usefulness, historical_significance, modern_resonance) AS (
  VALUES ('word_history_not_concept_history', 0.96, 0.98, 0.96, 0.88, 0.98, 0.90, 0.90, 0.96, 0.98, 0.98)
)
SELECT
  theme_id,
  (evidence_grounding + scope_clarity + anachronism_control + network_awareness + etymology_caution + transmission_depth + credit_distribution + public_usefulness + historical_significance + modern_resonance) / 10.0 AS origin_care_score,
  CASE
    WHEN ((evidence_grounding + scope_clarity + anachronism_control + network_awareness + etymology_caution + transmission_depth + credit_distribution + public_usefulness + historical_significance + modern_resonance) / 10.0) >= 0.80
      AND anachronism_control >= 0.86 THEN 'core_origin_story_care_thread'
    WHEN ((evidence_grounding + scope_clarity + anachronism_control + network_awareness + etymology_caution + transmission_depth + credit_distribution + public_usefulness + historical_significance + modern_resonance) / 10.0) >= 0.80 THEN 'major_origin_story_care_thread'
    ELSE 'supporting_origin_story_care_thread'
  END AS interpretive_status
FROM theme;
