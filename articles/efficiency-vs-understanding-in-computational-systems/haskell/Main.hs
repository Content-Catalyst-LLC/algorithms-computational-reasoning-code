module Main where
efficiencyGain :: Double -> Double -> Double
efficiencyGain baseline optimized = (baseline - optimized) / baseline
understanding :: [Double] -> Double
understanding xs = 100 * sum xs / fromIntegral (length xs)
main :: IO ()
main = putStrLn ("test_name,value\nefficiency_gain_percent," ++ show (100 * efficiencyGain 100 64) ++ "\nunderstanding_score," ++ show (understanding [0.80,0.75,0.70,0.78,0.82]))
