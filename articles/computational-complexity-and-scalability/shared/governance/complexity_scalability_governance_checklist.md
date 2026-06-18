# Complexity and Scalability Governance Checklist

- Define input size and all relevant dimensions of growth.
- State time complexity, space complexity, I/O cost, communication cost, and review capacity.
- Benchmark on representative, stress, and adversarial workloads.
- Identify bottlenecks with profiling, traces, load tests, or capacity tests.
- Estimate thresholds for runtime, memory, latency, cost, and human review.
- Define degradation behavior under overload.
- Monitor live performance, queue growth, cost, and failure modes.
- Review equity under scale: who receives slower service, less review, or worse outcomes?
- Communicate scale limits honestly.
- Assign ownership for compute, infrastructure, energy, and governance costs.
