performance_metric(latency).
performance_metric(throughput).
performance_metric(utilization).
performance_metric(tail_latency).
performance_metric(error_rate).
performance_metric(unit_cost).

requires_governance(cache_freshness).
requires_governance(tail_latency_reporting).
requires_governance(load_shedding_policy).
requires_governance(cost_performance_review).
requires_governance(partial_result_disclosure).

risk(average_hides_tail).
risk(throughput_hides_failure).
risk(cache_hides_staleness).
risk(benchmark_mismatch).
risk(traceability_removed_for_speed).
