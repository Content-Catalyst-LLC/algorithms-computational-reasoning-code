# Data Structure Governance Checklist

- Define the problem shape: sequential, relational, hierarchical, keyed, priority-based, spatial, or vector-based.
- List required operations: search, insert, delete, traverse, rank, join, update, retrieve, or transform.
- Identify dominant operations and expected data scale.
- State invariants required for correctness.
- Compare time and space complexity trade-offs.
- Review interpretability and auditability.
- Preserve metadata, provenance, source, and transformation history.
- Document representation risks: flattening, false hierarchy, hidden priority, opaque similarity, or relationship overclaim.
- Test alternative structures when reasoning fit is uncertain.
- Govern changes in schema, operation load, domain meaning, and downstream reuse.
