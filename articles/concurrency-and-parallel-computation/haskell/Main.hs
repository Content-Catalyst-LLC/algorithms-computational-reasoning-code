module Main where
speedup :: Double -> Double -> Double
speedup t1 tp = if tp == 0 then 0 else t1 / tp
amdahl :: Double -> Double -> Double
amdahl p s = if p == 0 then 0 else 1 / (s + ((1 - s) / p))
efficiency :: Double -> Double -> Double
efficiency p sp = if p == 0 then 0 else sp / p
main :: IO ()
main = putStrLn ("test_name,value\nobserved_speedup_120_to_28," ++ show (speedup 120 28) ++ "\namdahl_speedup_8_workers," ++ show (amdahl 8 0.12) ++ "\nefficiency_8_workers," ++ show (efficiency 8 (speedup 120 28)))
