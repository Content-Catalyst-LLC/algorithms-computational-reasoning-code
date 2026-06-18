.headers on
.mode column
SELECT case_name,
ROUND(100.0*(0.30*performance_gain+0.25*memory_gain+0.25*cost_gain+0.20*energy_awareness),2) AS efficiency_score,
ROUND(100.0*(0.12*readability+0.12*debuggability+0.12*explainability+0.12*observability+0.12*auditability+0.10*reproducibility+0.12*maintainability+0.10*governance_readiness+0.08*communication_clarity),2) AS understanding_score
FROM efficiency_cases ORDER BY efficiency_score DESC;
