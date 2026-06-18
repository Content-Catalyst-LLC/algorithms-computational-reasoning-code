.headers on
.mode column
SELECT case_name,
ROUND(100.0*(0.16*(1-agreement_clarity)+0.16*(1-quorum_design)+0.17*(1-failure_model)+0.15*(1-partition_behavior)+0.12*(1-retry_idempotence)+0.12*(1-observability)+0.12*(1-recovery_design)),2) AS consensus_risk_score
FROM consensus_cases ORDER BY consensus_risk_score DESC;
SELECT cluster_id,node_count,quorum_size,CAST(node_count/2 AS INTEGER)+1 AS majority_quorum,CAST((node_count-1)/2 AS INTEGER) AS crash_fault_tolerance,CASE WHEN 2*quorum_size > node_count THEN 'intersects' ELSE 'does_not_intersect' END AS quorum_intersection FROM quorum_records ORDER BY node_count;
