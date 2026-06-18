response_time(network, queue, compute, storage, coordination) = network + queue + compute + storage + coordination
throughput(completed, seconds) = seconds == 0 ? 0 : completed / seconds
utilization(arrival, service) = service == 0 ? 0 : arrival / service
little_law(arrival, time_in_system) = arrival * time_in_system
println("test_name,value")
println("response_time_ms,$(response_time(45,20,85,35,15))")
println("throughput,$(throughput(12000,60))")
println("utilization,$(utilization(180,200))")
println("little_law_items,$(little_law(180,0.45))")
