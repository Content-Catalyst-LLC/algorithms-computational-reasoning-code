module Main where
missingnessRate :: Double -> Double -> Double
missingnessRate missing total = if total == 0 then 0 else missing / total
quality :: Double -> Double -> Double -> Double -> Double -> Double
quality c v t p val = 100 * (0.25*c + 0.20*v + 0.15*t + 0.22*p + 0.18*val)
main :: IO ()
main = putStrLn ("test_name,value\nmissingness_rate_45_of_1000," ++ show (missingnessRate 45 1000) ++ "\ncompleteness_score_45_of_1000," ++ show (1 - missingnessRate 45 1000) ++ "\ndata_quality_score," ++ show (quality 0.92 0.88 0.86 0.90 0.89))
