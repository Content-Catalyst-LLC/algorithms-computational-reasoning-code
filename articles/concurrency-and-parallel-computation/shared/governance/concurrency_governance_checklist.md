# Concurrency and Parallel Computation Governance Checklist

- Define workload and task boundaries.
- Map dependencies before parallelizing.
- Identify shared state, mutable state, external side effects, and ownership.
- Prefer immutable data, message passing, staging, or single-writer rules where possible.
- Design synchronization and lock ordering explicitly.
- Test for race conditions, deadlocks, livelocks, starvation, and partial writes.
- Make retries idempotent and outputs atomically publishable.
- Version code, data, parameters, worker configurations, and output snapshots.
- Monitor queue depth, latency, throughput, failures, retries, lock contention, and partial-success rates.
- Preserve logs and traces sufficient to reconstruct event order.
