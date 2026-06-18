# Dynamic Programming Governance Checklist

- Define the objective, value function, and unit of measurement.
- Define the state schema and justify state sufficiency.
- Document recurrence, transitions, base cases, boundaries, and invalid states.
- Identify overlapping subproblems and optimal-substructure assumptions.
- Choose memory strategy: memoization, tabulation, sparse map, rolling array, or backpointer table.
- Estimate state count, transition count, time cost, and memory cost.
- Preserve table versions, cache metadata, transition logs, and reconstruction backpointers.
- Test empty inputs, terminal states, invalid states, stale caches, and state-space explosion.
- Review whether stored values encode sensitive, proxy, uncertain, or outdated assumptions.
