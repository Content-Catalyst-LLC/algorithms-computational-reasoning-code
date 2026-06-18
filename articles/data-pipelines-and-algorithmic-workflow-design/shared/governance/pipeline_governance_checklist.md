# Data Pipeline and Algorithmic Workflow Governance Checklist

- Define pipeline purpose and downstream use.
- Inventory sources, ownership, permissions, formats, update frequency, and limits.
- Specify input and output contracts.
- Validate schemas, types, ranges, completeness, uniqueness, integrity, and freshness.
- Document every transformation and feature construction rule.
- Map task dependencies and failure propagation.
- Make tasks idempotent and retry-safe.
- Preserve lineage from output to source records, code, parameters, and run metadata.
- Monitor record counts, null rates, drift, latency, freshness, and validation outcomes.
- Add human review gates for source changes, schema changes, validation failures, model updates, and public release.
