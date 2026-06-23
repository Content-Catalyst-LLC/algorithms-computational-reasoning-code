WITH system(system_id, worker_impact, managerial_impact, fairness_readiness, privacy_readiness, contestability, safety_readiness, human_review, monitoring, governance) AS (
  VALUES ('applicant_screening_ranker', 0.88, 0.72, 0.58, 0.66, 0.52, 0.70, 0.60, 0.58, 0.56)
)
SELECT
  system_id,
  (worker_impact + managerial_impact) / 2.0 AS impact_score,
  (fairness_readiness + privacy_readiness + contestability + safety_readiness + human_review + monitoring + governance) / 7.0 AS governance_readiness_score,
  (((worker_impact + managerial_impact) / 2.0) + (1.0 - fairness_readiness) + (1.0 - privacy_readiness) + (1.0 - contestability) + (1.0 - ((fairness_readiness + privacy_readiness + contestability + safety_readiness + human_review + monitoring + governance) / 7.0))) / 5.0 AS workplace_algorithm_risk_score
FROM system;
