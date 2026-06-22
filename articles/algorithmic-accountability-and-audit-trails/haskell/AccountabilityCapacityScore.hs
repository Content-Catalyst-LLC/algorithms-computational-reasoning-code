module Main where

main :: IO ()
main = do
  let scores = [0.72, 0.68, 0.64, 0.58, 0.52, 0.66]
      capacity = sum scores / fromIntegral (length scores)
  putStrLn ("accountability_capacity_score=" ++ show capacity)
