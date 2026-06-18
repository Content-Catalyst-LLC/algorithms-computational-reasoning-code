majority_quorum(n)=floor(Int,n/2)+1
crash_fault_tolerance(n)=floor(Int,(n-1)/2)
byzantine_replica_requirement(f)=3*f+1
println("test_name,value")
println("majority_quorum_5_nodes,$(majority_quorum(5))")
println("crash_fault_tolerance_5_nodes,$(crash_fault_tolerance(5))")
println("byzantine_replicas_for_2_faults,$(byzantine_replica_requirement(2))")
