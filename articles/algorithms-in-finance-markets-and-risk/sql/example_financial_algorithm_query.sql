WITH system(system_id, market_impact, consumer_impact, model_risk, transparency, human_review, validation, monitoring, governance, liquidity_risk) AS (
  VALUES ('consumer_credit_scorecard', 0.34, 0.92, 0.68, 0.58, 0.62, 0.70, 0.66, 0.64, 0.20)
)
SELECT
  system_id,
  (market_impact + consumer_impact + liquidity_risk) / 3.0 AS impact_score,
  (transparency + human_review + validation + monitoring + governance) / 5.0 AS governance_readiness_score,
  (model_risk + ((market_impact + consumer_impact + liquidity_risk) / 3.0) + (1.0 - ((transparency + human_review + validation + monitoring + governance) / 5.0))) / 3.0 AS financial_algorithm_risk_score
FROM system;
