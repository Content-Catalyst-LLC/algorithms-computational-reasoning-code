WITH system(system_id, public_impact, climate_exposure, reliability_impact, equity_readiness, validation_readiness, monitoring_readiness, governance_readiness, maintenance_readiness) AS (
  VALUES ('grid_demand_forecast_dispatch', 0.82, 0.72, 0.92, 0.62, 0.74, 0.78, 0.66, 0.70)
)
SELECT
  system_id,
  (public_impact + climate_exposure + reliability_impact) / 3.0 AS impact_score,
  (equity_readiness + validation_readiness + monitoring_readiness + governance_readiness + maintenance_readiness) / 5.0 AS governance_score,
  (((public_impact + climate_exposure + reliability_impact) / 3.0) + (1.0 - equity_readiness) + (1.0 - validation_readiness) + (1.0 - ((equity_readiness + validation_readiness + monitoring_readiness + governance_readiness + maintenance_readiness) / 5.0))) / 4.0 AS resilience_risk_score
FROM system;
