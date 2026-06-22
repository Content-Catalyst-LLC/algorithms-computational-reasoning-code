WITH delegation_context(context_id, evidence_quality, validation, reversibility, contestability, governance, human_review, automated_final_actions, total_decisions, stakes) AS (
  VALUES ('benefits_eligibility_denial', 0.62, 0.58, 0.46, 0.52, 0.60, 0.58, 760, 1000, 0.92)
)
SELECT
  context_id,
  (evidence_quality + validation + reversibility + contestability + governance + human_review) / 6.0 AS delegation_readiness_score,
  CAST(automated_final_actions AS REAL) / total_decisions AS automation_reliance_score,
  stakes * (1.0 - ((evidence_quality + validation + reversibility + contestability + governance + human_review) / 6.0)) AS delegation_risk_score
FROM delegation_context;
