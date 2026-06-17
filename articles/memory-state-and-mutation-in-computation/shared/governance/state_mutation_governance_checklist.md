# State and Mutation Governance Checklist

- Inventory local, object-level, global, persistent, distributed, and external state.
- Identify every mutation point.
- Make ownership and lifecycle rules explicit.
- Separate pure computation from effect boundaries.
- Define valid and invalid state transitions.
- Use transactions, snapshots, event logs, or audit trails for consequential changes.
- Control aliases to mutable objects.
- Document cache invalidation and staleness rules.
- Test concurrency, retries, rollback, and recovery behavior.
- Preserve enough state history for reproducibility and accountability.
