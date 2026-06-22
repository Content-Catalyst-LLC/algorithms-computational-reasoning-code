module Main where

main :: IO ()
main = do
  let scores = [0.94, 0.78, 0.56, 0.70]
      pressure = sum scores / fromIntegral (length scores)
  putStrLn ("non_use_pressure_score=" ++ show pressure)
