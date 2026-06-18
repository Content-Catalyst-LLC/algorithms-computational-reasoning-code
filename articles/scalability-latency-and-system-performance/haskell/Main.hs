module Main where
responseTime n q c s o = n + q + c + s + o
throughput completed seconds = if seconds == 0 then 0 else completed / seconds
utilization arrival service = if service == 0 then 0 else arrival / service
littleLaw arrival timeInSystem = arrival * timeInSystem
main :: IO ()
main = putStrLn ("test_name,value\nresponse_time_ms," ++ show (responseTime 45 20 85 35 15) ++ "\nthroughput," ++ show (throughput 12000 60) ++ "\nutilization," ++ show (utilization 180 200) ++ "\nlittle_law_items," ++ show (littleLaw 180 0.45))
