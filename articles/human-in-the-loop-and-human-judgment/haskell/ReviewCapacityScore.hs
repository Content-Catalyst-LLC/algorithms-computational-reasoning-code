module Main where

main :: IO ()
main = do
  let scores = [0.56, 0.62, 0.58, 0.60, 0.48]
      capacity = sum scores / fromIntegral (length scores)
  putStrLn ("review_capacity_score=" ++ show capacity)
