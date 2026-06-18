.headers on
.mode column
SELECT case_name, scale_claim,
ROUND(100.0*(0.10*decomposability+0.09*partitioning_clarity+0.10*communication_awareness+0.08*synchronization_control+0.09*load_balance_evidence+0.08*data_locality_awareness+0.10*fault_tolerance+0.08*consistency_clarity+0.10*benchmark_support+0.07*cost_awareness+0.06*governance_readiness+0.05*communication_clarity),2) AS scale_claim_quality
FROM parallelism_scale_cases ORDER BY scale_claim_quality DESC;
