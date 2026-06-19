module Main where
edgeResponseTime sense filterT compute actuate = sense + filterT + compute + actuate
cloudResponseTime sense uplink cloudCompute downlink actuate = sense + uplink + cloudCompute + downlink + actuate
batteryLife batteryWh powerW = if powerW == 0 then 0 else batteryWh / powerW
localAction signal threshold = if signal >= threshold then "alert" else "monitor"
main :: IO ()
main = putStrLn ("test_name,value\nedge_response_time_ms," ++ show (edgeResponseTime 8 6 14 5) ++ "\ncloud_response_time_ms," ++ show (cloudResponseTime 8 90 60 90 5) ++ "\nbattery_life_hours," ++ show (batteryLife 12 0.08) ++ "\nlocal_action," ++ localAction 0.82 0.75)
