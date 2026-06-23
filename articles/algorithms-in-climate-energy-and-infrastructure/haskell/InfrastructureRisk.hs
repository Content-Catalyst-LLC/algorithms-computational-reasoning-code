module Main where

main :: IO ()
main = do
  let hazard = 0.80
      exposure = 0.75
      vulnerability = 0.60
      risk = hazard * exposure * vulnerability
  putStrLn ("infrastructure_risk=" ++ show risk)
