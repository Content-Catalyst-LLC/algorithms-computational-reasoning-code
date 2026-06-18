# Search and Sorting Governance Checklist

- Define the search space and document exclusions.
- Define match predicates, keys, comparators, ranking signals, and tie-breaking rules.
- Check algorithm preconditions such as sortedness, key range, index freshness, and graph structure.
- Choose data structures that match lookup, update, memory, and audit needs.
- Test empty, duplicate, missing, unsorted, cyclic, stale, and adversarial cases.
- Measure complexity, recall, ranking stability, and worst-case behavior.
- Preserve query logs, index versions, ranking scores, source metadata, and run traces.
- Review exposure effects, proxy priority, false completeness, and ranking governance.
