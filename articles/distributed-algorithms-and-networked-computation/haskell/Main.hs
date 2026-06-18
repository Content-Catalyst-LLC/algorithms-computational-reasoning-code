module Main where
quorumSize :: Int -> Int
quorumSize n = div n 2 + 1
crashFaultTolerance :: Int -> Int
crashFaultTolerance n = div (n - 1) 2
availability :: Double -> Double -> Double
availability replicas nodeAvailability = 1 - ((1 - nodeAvailability) ** replicas)
latency :: Double -> Double -> Double -> Double
latency compute network queue = compute + network + queue
main :: IO ()
main = putStrLn ("test_name,value\nquorum_5_nodes," ++ show (quorumSize 5) ++ "\nfault_tolerance_5_nodes," ++ show (crashFaultTolerance 5) ++ "\navailability_3_replicas," ++ show (availability 3 0.99) ++ "\ndistributed_latency_ms," ++ show (latency 35 80 20))
