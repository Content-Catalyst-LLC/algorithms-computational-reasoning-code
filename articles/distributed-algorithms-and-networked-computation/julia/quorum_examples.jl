quorum_size(n) = floor(Int, n/2) + 1
crash_fault_tolerance(n) = floor(Int, (n - 1)/2)
availability_with_replication(replicas, node_availability) = 1 - ((1 - node_availability)^replicas)
distributed_latency(compute_ms, network_ms, queue_ms) = compute_ms + network_ms + queue_ms
println("test_name,value")
println("quorum_5_nodes,$(quorum_size(5))")
println("fault_tolerance_5_nodes,$(crash_fault_tolerance(5))")
println("availability_3_replicas,$(availability_with_replication(3,0.99))")
println("distributed_latency_ms,$(distributed_latency(35,80,20))")
