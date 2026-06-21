-- Cases near the threshold deserve heightened explanation and appeal review.
SELECT
  case_id,
  decision_score,
  decision,
  ABS(decision_score - threshold) AS distance_to_threshold
FROM algorithmic_decisions
ORDER BY distance_to_threshold ASC
LIMIT 25;

-- Features that flip decisions but should not be presented as individual recourse.
SELECT
  counterfactual_feature,
  COUNT(*) AS non_actionable_flip_count
FROM counterfactual_candidates
WHERE flipped_to_favorable = 1
  AND allowed_for_recourse = 0
GROUP BY counterfactual_feature
ORDER BY non_actionable_flip_count DESC;

-- Lowest-cost feasible recourse paths.
SELECT
  case_id,
  recommended_feature,
  delta,
  recourse_cost,
  original_score,
  counterfactual_score
FROM recourse_review
ORDER BY recourse_cost ASC, delta ASC;
