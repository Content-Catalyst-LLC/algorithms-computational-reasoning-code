module Main where

main :: IO ()
main = do
  let inputDrift = 0.31
      labelDrift = 0.16
      performanceDecay = 0.10
      calibrationGap = 0.14
      subgroupGap = 0.15
      overrideRate = 0.11
      score = (inputDrift + labelDrift + performanceDecay + calibrationGap + subgroupGap + overrideRate) / 6
  putStrLn ("decay_risk_score=" ++ show score)
