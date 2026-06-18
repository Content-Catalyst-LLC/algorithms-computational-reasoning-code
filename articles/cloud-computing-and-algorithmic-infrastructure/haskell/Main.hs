module Main where
totalLatency compute storage network queue coordination = compute + storage + network + queue + coordination
nominalCapacity nodes capacityPerNode = nodes * capacityPerNode
unitCost compute storage network managed observability completed = if completed == 0 then 0 else (compute + storage + network + managed + observability) / completed
main :: IO ()
main = putStrLn ("test_name,value\ncloud_response_latency_ms," ++ show (totalLatency 80 45 60 25 15) ++ "\nnominal_capacity," ++ show (nominalCapacity 12 250) ++ "\nunit_cost," ++ show (unitCost 120 35 25 90 18 144000))
