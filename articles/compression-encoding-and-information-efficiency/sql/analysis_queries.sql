.headers on
.mode column

SELECT
  case_name,
  ROUND(100.0 * (
    0.12 * fidelity_requirement +
    0.10 * encoding_clarity +
    0.10 * compression_suitability +
    0.10 * metadata_preservation +
    0.10 * interoperability +
    0.10 * integrity_checks +
    0.10 * storage_efficiency +
    0.08 * transmission_efficiency +
    0.10 * accessibility_preservation +
    0.10 * governance_readiness
  ), 2) AS representation_quality
FROM compression_encoding_cases
ORDER BY representation_quality DESC;

SELECT sample_id, encoding, use_case, LENGTH(sample_text) AS character_count
FROM encoding_samples
ORDER BY sample_id;
