# Query Optimization Governance Checklist

- State the plain-language query purpose.
- Preserve baseline query text, plan, timing, data size, and workload conditions.
- Review predicates, joins, missingness, and aggregation before tuning.
- Compare estimated rows with actual rows.
- Document indexes, index benefits, write costs, storage costs, and maintenance costs.
- Review join order, join algorithm, memory needs, and spill risk.
- Refresh or review statistics when estimates diverge from reality.
- Label caches, materialized views, freshness windows, and invalidation policies.
- Assess workload impact, concurrency, and operational risks.
- Communicate optimization trade-offs with evidence rather than speed claims alone.
