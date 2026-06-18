.headers on
.mode column
SELECT case_name, ROUND(100.0*(0.12*path_clarity+0.10*loop_structure+0.10*recursion_structure+0.10*state_update_discipline+0.12*termination_evidence+0.12*invariant_evidence+0.10*edge_case_coverage+0.08*error_handling+0.08*traceability+0.08*governance_readiness),2) AS control_flow_quality
FROM control_flow_cases ORDER BY control_flow_quality DESC;
