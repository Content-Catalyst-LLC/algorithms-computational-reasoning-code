module Main where

main :: IO ()
main = do
  let acceptance = 0.93
      quality = 0.71
      uncertainty = 0.29
      reviewDeficit = 0.65
      overrideFriction = 0.72
      weakContestability = 0.0
      overrelianceGap = max 0 (acceptance - quality)
      score = (acceptance + overrelianceGap + uncertainty + reviewDeficit + overrideFriction + weakContestability) / 6
  putStrLn ("automation_bias_risk_score=" ++ show score)
