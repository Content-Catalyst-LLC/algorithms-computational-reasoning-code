module Main where
freshness :: Double -> Double -> Double
freshness days decay = exp (negate decay * days)
quality :: Double -> Double -> Double -> Double -> Double -> Double
quality validation fresh completeness lineage monitoring =
  100 * (0.25*validation + 0.18*fresh + 0.20*completeness + 0.22*lineage + 0.15*monitoring)
main :: IO ()
main = putStrLn ("test_name,value\nfreshness_3_days," ++ show (freshness 3 0.025) ++ "\npipeline_quality_score," ++ show (quality 0.92 0.86 0.90 0.88 0.82))
