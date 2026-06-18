# Scalability, Latency, and System Performance Governance Checklist

- Define workload, concurrency, input size, request mix, and success criteria.
- Report mean, median, P95, P99, throughput, error rate, and partial-result rate.
- Decompose latency into network, queue, compute, storage, and coordination components.
- Identify bottlenecks and critical paths before optimizing.
- Track queue depth, wait time, utilization, retry rate, and backpressure behavior.
- Review cache freshness, invalidation, stale-output risk, and user disclosure.
- Test normal load, peak load, stress conditions, soak behavior, and failure modes.
- Preserve trace IDs, performance baselines, benchmark configurations, and versioned outputs.
- Review cost per unit work, energy implications, and operational complexity.
- Communicate degraded mode, load shedding, throttling, and service-level objectives.
