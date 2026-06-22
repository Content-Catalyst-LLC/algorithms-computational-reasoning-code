module Main where

main :: IO ()
main = do
  let validityGap = 0.42
      missingness = 0.12
      differentialError = 0.24
      labelError = 0.08
      score = (validityGap + missingness + differentialError + labelError) / 4
  putStrLn ("measurement_risk_score=" ++ show score)
