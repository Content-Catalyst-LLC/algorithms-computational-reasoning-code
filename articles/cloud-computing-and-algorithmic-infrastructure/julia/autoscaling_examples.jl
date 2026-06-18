total_latency(compute, storage, network, queue, coordination) = compute + storage + network + queue + coordination
nominal_capacity(nodes, capacity_per_node) = nodes * capacity_per_node
unit_cost(compute, storage, network, managed, observability, completed) = completed == 0 ? 0 : (compute + storage + network + managed + observability) / completed
println("test_name,value")
println("cloud_response_latency_ms,$(total_latency(80,45,60,25,15))")
println("nominal_capacity,$(nominal_capacity(12,250))")
println("unit_cost,$(unit_cost(120,35,25,90,18,144000))")
