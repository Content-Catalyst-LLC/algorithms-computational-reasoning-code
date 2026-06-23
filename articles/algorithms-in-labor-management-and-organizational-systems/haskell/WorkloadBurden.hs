module Main where

main :: IO ()
main = do
  let pace = 0.84
      hours = 0.72
      fatigue = 0.70
      scheduleVolatility = 0.78
      burden = (pace + hours + fatigue + scheduleVolatility) / 4.0
  putStrLn ("workload_burden_score=" ++ show burden)
