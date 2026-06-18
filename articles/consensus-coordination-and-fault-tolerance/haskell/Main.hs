module Main where
majorityQuorum n = div n 2 + 1
crashFaultTolerance n = div (n - 1) 2
byzantineReplicaRequirement f = 3*f + 1
main = putStrLn ("test_name,value\nmajority_quorum_5_nodes," ++ show (majorityQuorum 5) ++ "\ncrash_fault_tolerance_5_nodes," ++ show (crashFaultTolerance 5) ++ "\nbyzantine_replicas_for_2_faults," ++ show (byzantineReplicaRequirement 2))
