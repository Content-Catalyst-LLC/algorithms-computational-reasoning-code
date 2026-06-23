WITH use_case(use_case_id, rights_impact, due_process, transparency, human_review, data_quality, vendor_accountability, appeal_readiness, monitoring, public_value) AS (
  VALUES ('benefits_eligibility_screening', 0.94, 0.58, 0.52, 0.60, 0.66, 0.48, 0.54, 0.56, 0.70)
)
SELECT
  use_case_id,
  (due_process + transparency + human_review + appeal_readiness) / 4.0 AS procedural_readiness_score,
  (data_quality + vendor_accountability + monitoring + ((due_process + transparency + human_review + appeal_readiness) / 4.0)) / 4.0 AS governance_readiness_score,
  rights_impact * (1.0 - ((data_quality + vendor_accountability + monitoring + ((due_process + transparency + human_review + appeal_readiness) / 4.0)) / 4.0)) AS public_algorithmic_risk_score
FROM use_case;
