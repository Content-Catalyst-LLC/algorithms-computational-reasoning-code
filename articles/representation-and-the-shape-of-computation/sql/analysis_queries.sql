.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * structural_fidelity +
    0.12 * operation_fit +
    0.10 * validation_discipline +
    0.10 * information_loss_control +
    0.10 * traceability +
    0.10 * interpretability +
    0.08 * retrieval_support +
    0.08 * transformation_readiness +
    0.10 * risk_documentation +
    0.10 * governance_readiness
  ), 2) AS representation_quality
FROM representation_cases
ORDER BY representation_quality DESC;
