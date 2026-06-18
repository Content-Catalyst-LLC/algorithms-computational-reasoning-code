# Parallelism and Distributed Scale Governance Checklist

- Define the workload and scale dimension being claimed.
- Identify what can be decomposed safely.
- Specify task, data, pipeline, model, GPU, or distributed parallelism.
- Document partitioning, load balancing, and data locality assumptions.
- Estimate communication, shuffle, serialization, and synchronization overhead.
- Identify race conditions, nondeterminism, retries, and idempotency needs.
- Test worker failure, message duplication, queue overload, timeouts, and recovery.
- State consistency model and conflict-resolution rules.
- Benchmark speedup, efficiency, cost, latency, and quality under load.
- Include human review, audit, incident response, and governance capacity in scale claims.
